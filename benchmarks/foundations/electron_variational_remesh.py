"""ELEC-009: variationally consistent adaptive spline remeshing.

Controlled numerical change from ELEC-008:
  * retain direct periodic cubic splines and unchanged Poisson curve-field energy;
  * use separate nonuniform periodic knot vectors for each strand;
  * choose remeshed controls by a topology-certified one-dimensional
    variational projection between geometry-faithful and monitor-adaptive maps;
  * require tighter remesh geometry and energy certificates;
  * test energy convergence under source-quadrature refinement.
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

N=14; L_BOX=8.0; A_THICK=.24; KAPPA=2.0; T0=1.0
M_ENERGY=64; CERT_LEVELS=(128,256,512); D_FLOOR=.060; LK_TOL=.03
FD=1e-4; FD_CON=2e-4; D_ACTIVE=.014; ARMIJO=1e-4
MIN_STEP=1e-5; MEMORY=5; STAGES=(16,20); ITERS_PER_STAGE=(2,3)
CURV_W=2.0; PROX_W=2.0; PROX_SCALE=.12

class Model:
    def __init__(self,nctrl,knots=None,m_energy=M_ENERGY):
        self.nctrl=int(nctrl); self.m_energy=int(m_energy)
        if knots is None:
            base=np.linspace(0,1,self.nctrl+1)[:-1]
            self.knots=np.stack([base,base])
        else:
            self.knots=np.asarray(knots,float).reshape(2,self.nctrl)
        _,X,Y,Z,self.H=grid(N,L_BOX)
        self.gp=np.stack([X.ravel(),Y.ravel(),Z.ravel()],axis=1)
        self.L3=laplacian_3d(N,self.H); self.nfev=0
    def controls(self,z):
        q=z.reshape(2,self.nctrl,3).copy(); q-=q.reshape(-1,3).mean(0); return q
    def curves(self,z,M):
        q=self.controls(z); u=np.linspace(0,1,M,endpoint=False); out=[]
        for j in range(2):
            t=np.r_[self.knots[j],1.0]; y=np.vstack([q[j],q[j,0]])
            out.append(CubicSpline(t,y,axis=0,bc_type='periodic')(u))
        return out[0],out[1]
    def src(self,cs):
        samples=np.vstack([np.vstack([c,.5*(c+np.roll(c,-1,axis=0))]) for c in cs])
        dist,_=cKDTree(samples).query(self.gp,k=1,workers=1)
        s=np.exp(-(dist*dist)/(2*A_THICK*A_THICK)).reshape(N,N,N)
        return s/(s.sum()*self.H**3)
    def energy(self,z):
        self.nfev+=1; cs=self.curves(z,self.m_energy)
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
        ok=(d>=D_FLOOR and max(abs(abs(v[1])-1) for v in vals)<=LK_TOL
            and max(v[1] for v in vals)-min(v[1] for v in vals)<=.02
            and max(v[0] for v in vals)-min(v[0] for v in vals)<=.01)
        return d,lk,bool(ok),vals
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
            if cv<0 and cn>1e-16:v-=cg*(cv/cn)
        return v
    def path_cert(self,a,b):
        ns=max(7,min(21,int(np.ceil(np.linalg.norm(b-a)/.003))+1)); wd=1e9; we=0.
        for t in np.linspace(0,1,ns):
            d,lk=self.cert_level((1-t)*a+t*b,128); wd=min(wd,d); we=max(we,abs(abs(lk)-1))
            if d<D_FLOOR or abs(abs(lk)-1)>LK_TOL:return False,wd,we,ns
        d,lk,ok,vals=self.cert(b); return ok,min(wd,d),max(we,max(abs(abs(v[1])-1) for v in vals)),ns
    def metrics(self,z):
        a,b=self.curves(z,512); p=np.vstack([a,b]); p-=p.mean(0)
        r=float(np.sqrt(np.mean(np.sum(p*p,axis=1))))
        d,lk,ok,vals=self.cert(z); return r,d,lk,ok,vals

def lbfgs(g,S,Y):
    q=g.copy(); rec=[]
    for s,y in zip(reversed(S),reversed(Y)):
        rho=1/max(np.dot(y,s),1e-14); a=rho*np.dot(s,q); rec.append((a,rho)); q-=a*y
    if S:q*=np.dot(S[-1],Y[-1])/max(np.dot(Y[-1],Y[-1]),1e-14)
    for s,y,(a,rho) in zip(S,Y,reversed(rec)):q+=s*(a-rho*np.dot(y,q))
    return -q

def initial_controls(nctrl):
    fm=FourierModel(); dat=np.load(ROOT/'analysis'/'ELEC006_state.npz')
    x=dat['x_final']; a,b=fm.curves(x,512); idx=(np.arange(nctrl)*512//nctrl).astype(int)
    q=np.stack([a[idx],b[idx]]); q-=q.reshape(-1,3).mean(0); return q.ravel()

def monitor_knots(old,z,new_n):
    M=4096; curves=old.curves(z,M); knots=[]; controls=[]
    for j,c in enumerate(curves):
        prev=np.roll(c,1,0); nxt=np.roll(c,-1,0)
        tan=nxt-prev; curv=np.linalg.norm(nxt-2*c+prev,axis=1)/(np.linalg.norm(tan,axis=1)**2+1e-14)
        prox=cKDTree(curves[1-j]).query(c,k=1,workers=1)[0]
        monitor=1+CURV_W*curv/(np.median(curv)+1e-12)+PROX_W*np.exp(-prox/PROX_SCALE)
        ds=np.linalg.norm(nxt-c,axis=1); w=monitor*ds; cum=np.r_[0,np.cumsum(w)]; total=cum[-1]
        targets=np.linspace(0,total,new_n+1)[:-1]; idx=np.searchsorted(cum,targets,side='right')-1; idx=np.clip(idx,0,M-1)
        frac=(targets-cum[idx])/np.maximum(w[idx],1e-14); pts=c[idx]+frac[:,None]*(nxt[idx]-c[idx])
        u=(idx+frac)/M; knots.append(u); controls.append(pts)
    q=np.stack(controls); q-=q.reshape(-1,3).mean(0)
    return q.ravel(),np.stack(knots)

def geometry_error(old,zold,new,znew,M=2048):
    co=old.curves(zold,M); cn=new.curves(znew,M)
    rms=max(float(np.sqrt(np.mean(np.sum((co[j]-cn[j])**2,axis=1)))) for j in range(2))
    haus=max(float(max(cKDTree(co[j]).query(cn[j])[0].max(),cKDTree(cn[j]).query(co[j])[0].max())) for j in range(2))
    return rms,haus

def variational_remesh(old,z,new_n):
    """Topology-certified energy selection around a geometry-faithful nonuniform remesh."""
    z0,k0=monitor_knots(old,z,new_n); base=Model(new_n,k0); eold=old.energy(z)
    # Candidate smoothing blends controls toward cyclic local averages. Select the
    # lowest-energy certified candidate satisfying strict geometry bounds.
    q0=z0.reshape(2,new_n,3); candidates=[]
    for lam in np.linspace(0,0.20,9):
        qs=(1-lam)*q0+lam*.5*(np.roll(q0,1,axis=1)+np.roll(q0,-1,axis=1)); zs=qs.ravel()
        d,lk,ok,_=base.cert(zs); rms,haus=geometry_error(old,z,base,zs)
        e=base.energy(zs); candidates.append((e,lam,zs,d,lk,ok,rms,haus))
    feasible=[c for c in candidates if c[5] and c[6]<.004 and c[7]<.012 and abs(c[0]-eold)/abs(eold)<.001]
    chosen=min(feasible,key=lambda c:c[0]) if feasible else min([c for c in candidates if c[5]],key=lambda c:(c[6],abs(c[0]-eold)))
    return base,chosen,candidates,eold

def run():
    t0=time.time(); hist=[]; rem=[]; accepted=0
    z=initial_controls(16); model=Model(16); campaign_start=model.energy(z)
    final_g=None
    for stage,nctrl in enumerate(STAGES):
        if stage:
            old,zold=model,z.copy(); model,choice,cands,eold=variational_remesh(old,zold,nctrl)
            e,lam,z,d,lk,ok,rms,haus=choice
            reljump=abs(e-eold)/abs(eold); rem.append((old.nctrl,nctrl,eold,e,reljump,lam,rms,haus,d,lk,int(ok)))
            print(f'remesh {old.nctrl}->{nctrl}: E {eold:.9f}->{e:.9f} rel={reljump:.6g} lambda={lam:.3f} rms={rms:.6g} haus={haus:.6g} cert={ok}',flush=True)
        e=model.energy(z); g=model.gradient(z); S=[];Y=[]; r,d,lk,ok,_=model.metrics(z)
        print(f'stage={stage} nctrl={nctrl} start E={e:.9f} R={r:.6f} d={d:.6f} Lk={lk:.8f}',flush=True)
        for it in range(ITERS_PER_STAGE[stage]):
            p=model.project(z,lbfgs(g,S,Y),d)
            if np.dot(g,p)>=-1e-12:p=model.project(z,-g,d);S.clear();Y.clear()
            if np.linalg.norm(p)>.14:p*=.14/np.linalg.norm(p)
            slope=np.dot(g,p); alpha=.015; took=False; wd=we=np.nan; ns=0
            for _ in range(17):
                trial=z+alpha*p; feasible,wd,we,ns=model.path_cert(z,trial)
                if feasible:
                    et=model.energy(trial)
                    if et<=e+ARMIJO*alpha*slope:
                        gt=model.gradient(trial); s=trial-z; y=gt-g
                        if np.dot(s,y)>1e-9:
                            S.append(s);Y.append(y);S=S[-MEMORY:];Y=Y[-MEMORY:]
                        z,e,g=trial,et,gt;took=True;accepted+=1;break
                alpha*=.5
                if alpha<MIN_STEP:break
            r,d,lk,ok,_=model.metrics(z); pg=model.project(z,-g,d); rel=np.linalg.norm(pg)/abs(e)
            hist.append((stage,nctrl,it,e,r,d,lk,rel,alpha,int(took),wd,we,ns))
            print(f'  it={it:02d} E={e:.9f} d={d:.6f} Lk={lk:.8f} |Pg|/E={rel:.6f} ok={took}',flush=True)
            if not took:break
        final_g=g
    # quadrature convergence at identical geometry
    qrows=[]
    for M in (48,64):
        mm=Model(STAGES[-1],model.knots,m_energy=M); qrows.append((M,mm.energy(z)))
    qrel=abs(qrows[-1][1]-qrows[-2][1])/abs(qrows[-1][1])
    r,d,lk,ok,vals=model.metrics(z); pg=model.project(z,-final_g,d); rel=np.linalg.norm(pg)/abs(e)
    rem_ok=all(x[4]<.001 and x[6]<.004 and x[7]<.012 and x[10] for x in rem)
    allcert=all(x[5]>=D_FLOOR and abs(abs(x[6])-1)<=LK_TOL for x in hist)
    bars=[ok,e<campaign_start-1e-5,allcert,rem_ok,qrel<.002,accepted>=5,rel<.05]
    finding='VARIATIONAL_REMESH_STATIONARY' if all(bars) else ('VARIATIONAL_REMESH_CERTIFIED_DESCENT_NOT_STATIONARY' if all(bars[:6]) else 'VARIATIONAL_REMESH_NUMERICAL_GATE_FAILED')
    np.savez(ROOT/'analysis'/'ELEC009_state.npz',z_final=z,knots_final=model.knots,energy_start=campaign_start,energy_final=e,gradient_final=final_g,projected_gradient_final=pg)
    with open(ROOT/'analysis'/'ELEC009_history.csv','w',newline='') as f:
        w=csv.writer(f);w.writerow(['stage','nctrl','iteration','energy','R_rms','dmin','Lk512','projected_gradient_over_E','alpha','accepted','path_worst_d','path_worst_lk_error','path_samples']);w.writerows(hist)
    with open(ROOT/'analysis'/'ELEC009_remesh.csv','w',newline='') as f:
        w=csv.writer(f);w.writerow(['old_nctrl','new_nctrl','energy_before','energy_after','relative_energy_jump','smoothing_lambda','rms_geometry_error','hausdorff_error','dmin','Lk512','certified']);w.writerows(rem)
    with open(ROOT/'analysis'/'ELEC009_quadrature.csv','w',newline='') as f:
        w=csv.writer(f);w.writerow(['curve_source_samples','energy']);w.writerows(qrows)
    print('\nELEC-009 variational remeshing')
    print(f'start E={campaign_start:.9f}; final E={e:.9f}; accepted={accepted}; q48->64={qrel:.6g}')
    print(f'final R={r:.6f}, dmin={d:.8f}, Lk={lk:.8f}, projected gradient/E={rel:.7g}')
    names=['B1 topology certificate','B2 physical energy decreases','B3 all accepted states certified','B4 strict remesh geometry/energy fidelity','B5 quadrature convergence <0.2%','B6 at least 5 accepted steps','B7 projected stationarity <0.05']
    for n,b in zip(names,bars):print(n+': '+('PASS' if b else 'FAIL'))
    print('FINDING:',finding);print(f'elapsed={time.time()-t0:.1f}s')
    return locals()
if __name__=='__main__':run()
