"""ELEC-008: direct periodic-spline representation with adaptive remeshing.

Controlled change from ELEC-007:
  * replace the global K=8 Fourier chart with direct periodic cubic-spline
    control points;
  * adaptively redistribute and refine control points according to curvature
    and inter-strand proximity;
  * keep the Poisson curve-field physical energy unchanged;
  * retain hard minimum-separation and Gauss-linking certificates along every
    accepted line-search path;
  * test stationarity only with the physical-energy gradient projected into
    the active separation tangent cone.
"""
from pathlib import Path
import sys, time, csv
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.spatial import cKDTree

ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from rope_solver.psi.solver import grid, solve_psi, field_energy, laplacian_3d
from rope_solver.geometry.curve import tension_energy
from rope_solver.topology.linking import linking_number
from benchmarks.foundations.electron_augmented_lagrangian import Model as FourierModel, segment_distance_min

N=14; L_BOX=8.0; A_THICK=.24; M_ENERGY=64
KAPPA=2.0; T0=1.0
CERT_LEVELS=(128,256,512); D_FLOOR=.060; D_ACTIVE=.014; LK_TOL=.03
FD=1e-4; FD_CON=2e-4; ARMIJO=1e-4; MIN_STEP=1e-5
STAGES=(16,20); ITERS_PER_STAGE=(4,4); MEMORY=5
CURV_W=2.0; PROX_W=2.0; PROX_SCALE=.12

class DirectSplineModel:
    def __init__(self,nctrl,knots=None):
        self.nctrl=int(nctrl)
        self.knots=np.linspace(0.0,1.0,self.nctrl+1) if knots is None else np.r_[np.asarray(knots,float),1.0]
        _,X,Y,Z,self.H=grid(N,L_BOX)
        self.gp=np.stack([X.ravel(),Y.ravel(),Z.ravel()],axis=1)
        self.L3=laplacian_3d(N,self.H); self.nfev=0
    def controls(self,z):
        q=z.reshape(2,self.nctrl,3).copy(); q-=q.reshape(-1,3).mean(0); return q
    def curves(self,z,M):
        q=self.controls(z); t=self.knots; u=np.linspace(0,1,M,endpoint=False)
        out=[]
        for j in range(2):
            y=np.vstack([q[j],q[j,0]])
            out.append(CubicSpline(t,y,axis=0,bc_type='periodic')(u))
        return out[0],out[1]
    def src(self,cs):
        samples=np.vstack([np.vstack([c,.5*(c+np.roll(c,-1,axis=0))]) for c in cs])
        dist,_=cKDTree(samples).query(self.gp,k=1,workers=1)
        s=np.exp(-(dist*dist)/(2*A_THICK*A_THICK)).reshape(N,N,N)
        return s/(s.sum()*self.H**3)
    def energy(self,z):
        self.nfev+=1; cs=self.curves(z,M_ENERGY)
        psi=solve_psi(self.src(cs),self.H,L3=self.L3,rtol=1e-5,maxiter=600)
        return float(sum(tension_energy(c,T0) for c in cs)+KAPPA*field_energy(psi,self.H))
    def gradient(self,z):
        g=np.empty_like(z)
        for i in range(len(z)):
            d=np.zeros_like(z); d[i]=FD
            g[i]=(self.energy(z+d)-self.energy(z-d))/(2*FD)
        gg=g.reshape(2,self.nctrl,3); gg-=gg.reshape(-1,3).mean(0); return gg.ravel()
    def cert_level(self,z,M):
        a,b=self.curves(z,M); return segment_distance_min(a,b),float(linking_number(a,b))
    def cert(self,z):
        vals=[self.cert_level(z,M) for M in CERT_LEVELS]
        d=min(v[0] for v in vals); lk=vals[-1][1]
        lkerr=max(abs(abs(v[1])-1) for v in vals)
        lagree=max(v[1] for v in vals)-min(v[1] for v in vals)<=.02
        dagree=max(v[0] for v in vals)-min(v[0] for v in vals)<=.01
        return d,lk,bool(d>=D_FLOOR and lkerr<=LK_TOL and lagree and dagree),vals
    def separation_gradient(self,z):
        g=np.empty_like(z)
        for i in range(len(z)):
            d=np.zeros_like(z); d[i]=FD_CON
            g[i]=(self.cert_level(z+d,128)[0]-self.cert_level(z-d,128)[0])/(2*FD_CON)
        gg=g.reshape(2,self.nctrl,3); gg-=gg.reshape(-1,3).mean(0); return gg.ravel()
    def project(self,z,v,dmin):
        vv=v.reshape(2,self.nctrl,3).copy(); vv-=vv.reshape(-1,3).mean(0); v=vv.ravel()
        if dmin-D_FLOOR<D_ACTIVE:
            cg=self.separation_gradient(z); cn=np.dot(cg,cg); cv=np.dot(cg,v)
            if cv<0 and cn>1e-16: v-=cg*(cv/cn)
        return v
    def path_cert(self,a,b):
        delta=np.linalg.norm(b-a); ns=max(7,min(19,int(np.ceil(delta/.003))+1))
        wd=1e9; we=0.0
        for t in np.linspace(0,1,ns):
            d,lk=self.cert_level((1-t)*a+t*b,128); wd=min(wd,d); we=max(we,abs(abs(lk)-1))
            if d<D_FLOOR or abs(abs(lk)-1)>LK_TOL: return False,wd,we,ns
        d,lk,ok,vals=self.cert(b)
        return ok,min(wd,d),max(we,max(abs(abs(v[1])-1) for v in vals)),ns
    def metrics(self,z):
        a,b=self.curves(z,512); p=np.vstack([a,b]); p-=p.mean(0)
        r=float(np.sqrt(np.mean(np.sum(p*p,axis=1))))
        d,lk,ok,vals=self.cert(z); return r,d,lk,ok,vals

def lbfgs(g,S,Y):
    q=g.copy(); rec=[]
    for s,y in zip(reversed(S),reversed(Y)):
        rho=1/max(np.dot(y,s),1e-14); a=rho*np.dot(s,q); rec.append((a,rho)); q-=a*y
    if S: q*=np.dot(S[-1],Y[-1])/max(np.dot(Y[-1],Y[-1]),1e-14)
    for s,y,(a,rho) in zip(S,Y,reversed(rec)): q+=s*(a-rho*np.dot(y,q))
    return -q

def initial_controls(nctrl):
    fm=FourierModel(); dat=np.load(ROOT/'analysis'/'ELEC007_state.npz')
    x=dat['x_final'] if 'x_final' in dat else np.load(ROOT/'analysis'/'ELEC006_state.npz')['x_final']
    a,b=fm.curves(x,512); idx=(np.arange(nctrl)*512//nctrl).astype(int)
    q=np.stack([a[idx],b[idx]]); q-=q.reshape(-1,3).mean(0); return q.ravel()

def adaptive_remesh(old_model,z,new_n):
    """Redistribute controls using curvature/proximity monitor density."""
    M=2048; curves=old_model.curves(z,M); out=[]
    for j,c in enumerate(curves):
        prev=np.roll(c,1,axis=0); nxt=np.roll(c,-1,axis=0)
        tan=nxt-prev; tn=np.linalg.norm(tan,axis=1)+1e-14
        curv=np.linalg.norm(nxt-2*c+prev,axis=1)/(tn*tn)
        other=curves[1-j]; prox=cKDTree(other).query(c,k=1,workers=1)[0]
        monitor=1.0+CURV_W*curv/(np.median(curv)+1e-12)+PROX_W*np.exp(-prox/PROX_SCALE)
        ds=np.linalg.norm(nxt-c,axis=1); w=monitor*ds
        cum=np.r_[0.0,np.cumsum(w)]; total=cum[-1]
        targets=np.linspace(0,total,new_n+1)[:-1]
        idx=np.searchsorted(cum,targets,side='right')-1; idx=np.clip(idx,0,M-1)
        frac=(targets-cum[idx])/np.maximum(w[idx],1e-14)
        pts=c[idx]+frac[:,None]*(nxt[idx]-c[idx]); out.append(pts)
    q=np.stack(out); q-=q.reshape(-1,3).mean(0); return q.ravel(), (targets/total)

def test():
    t0=time.time(); history=[]; remesh_rows=[]; accepted_total=0
    z=initial_controls(STAGES[0]); campaign_start=None
    final_model=None; final_g=None
    for si,nctrl in enumerate(STAGES):
        m=DirectSplineModel(nctrl)
        if si>0:
            e_before=prev_model.energy(z)
            z,new_knots=adaptive_remesh(prev_model,z,nctrl)
            m=DirectSplineModel(nctrl,knots=new_knots)
            e_after=m.energy(z); d,lk,ok,vals=m.cert(z)
            remesh_rows.append((si,prev_model.nctrl,nctrl,e_before,e_after,abs(e_after-e_before)/abs(e_before),d,lk,int(ok)))
            print(f'remesh {prev_model.nctrl}->{nctrl}: E {e_before:.9f}->{e_after:.9f} rel={abs(e_after-e_before)/abs(e_before):.4g} d={d:.6f} Lk={lk:.7f} cert={ok}',flush=True)
        e=m.energy(z); campaign_start=e if campaign_start is None else campaign_start
        g=m.gradient(z); S=[];Y=[]; r,d,lk,ok,vals=m.metrics(z)
        print(f'stage={si} nctrl={nctrl} start E={e:.9f} R={r:.6f} d={d:.6f} Lk={lk:.7f} cert={ok}',flush=True)
        for it in range(ITERS_PER_STAGE[si]):
            p=m.project(z,lbfgs(g,S,Y),d)
            if np.dot(g,p)>=-1e-12: p=m.project(z,-g,d); S.clear();Y.clear()
            pn=np.linalg.norm(p)
            if pn>.16:p*=.16/pn
            slope=float(np.dot(g,p)); alpha=min(1.0,max(.015,.25*max(d-D_FLOOR,.001)/max(np.linalg.norm(p),1e-12)))
            took=False;wd=we=np.nan;ns=0
            for _ in range(16):
                trial=z+alpha*p; feasible,wd,we,ns=m.path_cert(z,trial)
                if feasible:
                    et=m.energy(trial)
                    if et<=e+ARMIJO*alpha*slope:
                        gt=m.gradient(trial); s=trial-z; y=gt-g
                        if np.dot(s,y)>1e-9:
                            S.append(s);Y.append(y)
                            if len(S)>MEMORY:S.pop(0);Y.pop(0)
                        z,e,g=trial,et,gt;took=True;accepted_total+=1;break
                alpha*=.5
                if alpha<MIN_STEP:break
            r,d,lk,ok,vals=m.metrics(z); pstat=m.project(z,-g,d); rel=np.linalg.norm(pstat)/abs(e)
            history.append((si,nctrl,it,e,r,d,lk,rel,alpha,int(took),wd,we,ns))
            print(f'  it={it:02d} E={e:.9f} d={d:.6f} Lk={lk:.7f} |Pg|/E={rel:.5f} a={alpha:.3g} ok={took}',flush=True)
            if not took:break
        prev_model=m; final_model=m; final_g=g
    r,d,lk,ok,vals=final_model.metrics(z); pstat=final_model.project(z,-final_g,d); rel=float(np.linalg.norm(pstat)/abs(e))
    remesh_ok=all(row[8] and row[5]<.015 for row in remesh_rows)
    all_cert=all(row[5]>=D_FLOOR and abs(abs(row[6])-1)<=LK_TOL for row in history)
    b1=ok; b2=e<campaign_start-1e-5; b3=all_cert; b4=remesh_ok; b5=accepted_total>=8; b6=rel<.05
    finding='ADAPTIVE_DIRECT_CONSTRAINED_STATIONARY' if all((b1,b2,b3,b4,b5,b6)) else ('ADAPTIVE_DIRECT_CERTIFIED_DESCENT_NOT_STATIONARY' if all((b1,b2,b3,b4,b5)) else 'ADAPTIVE_DIRECT_METHOD_FAILED')
    np.savez(ROOT/'analysis'/'ELEC008_state.npz',z_final=z,nctrl_final=STAGES[-1],energy_start=campaign_start,energy_final=e,physical_gradient_final=final_g,projected_gradient_final=pstat)
    with (ROOT/'analysis'/'ELEC008_history.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['stage','nctrl','iteration','energy','R_rms','dmin','Lk512','projected_gradient_over_E','alpha','accepted','path_worst_d','path_worst_lk_error','path_samples']);w.writerows(history)
    with (ROOT/'analysis'/'ELEC008_remesh.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['stage','old_nctrl','new_nctrl','energy_before','energy_after','relative_energy_jump','dmin','Lk512','certified']);w.writerows(remesh_rows)
    print('\nELEC-008 adaptive direct-spline constrained solver')
    print(f'start E={campaign_start:.9f}; final E={e:.9f}; accepted={accepted_total}; final nctrl={STAGES[-1]}')
    print(f'final R={r:.6f}, dmin={d:.8f}, Lk={lk:.8f}, projected gradient/E={rel:.7g}')
    for name,b in [('B1 final 128/256/512 topology certificate',b1),('B2 physical energy decreases',b2),('B3 every accepted state certified',b3),('B4 remeshing topology/energy fidelity',b4),('B5 at least 8 accepted steps',b5),('B6 projected stationarity <0.05',b6)]: print(name+': '+('PASS' if b else 'FAIL'))
    print('FINDING:',finding); print(f'elapsed={time.time()-t0:.1f}s')
    return locals()
if __name__=='__main__':test()
