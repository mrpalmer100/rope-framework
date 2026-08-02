"""ELEC-007: direct periodic-spline constrained variational search.

Controlled change from ELEC-006:
  * replace the global K=8 Fourier chart by 16 direct periodic cubic-spline
    control points per component (96 coordinates after centering);
  * optimize a smooth augmented objective that activates before the certified
    separation floor;
  * retain hard adaptive 128/256/512 topology certification on every accepted
    line-search path;
  * assess stationarity with the physical-energy gradient projected into the
    active separation tangent cone.

The Poisson curve-field physical energy is unchanged. The smooth thickness
term guides feasible optimization but is excluded from the reported physical
energy and stationarity residual.
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
from benchmarks.foundations.electron_extended_constrained import Model as FourierModel, segment_distance_min

N=14; L_BOX=8.0; A_THICK=.24; NCTRL=16; M_ENERGY=64
CERT_BASE=(128,256); CERT_FINE=512; KAPPA=2.0; T0=1.0
FD=1e-4; FD_CON=2e-4
D_FLOOR=.06; D_TARGET=.072; D_ACTIVE=.014; LK_TOL=.03
PENALTY=80.0; BETA=90.0
MAXITER=10; MEMORY=6; ARMIJO=1e-4; MIN_STEP=1e-5

class SplineModel:
    def __init__(self):
        _,X,Y,Z,self.H=grid(N,L_BOX)
        self.gp=np.stack([X.ravel(),Y.ravel(),Z.ravel()],axis=1)
        self.L3=laplacian_3d(N,self.H); self.nfev=0
    def curves(self,z,M):
        q=z.reshape(2,NCTRL,3).copy()
        q-=q.reshape(-1,3).mean(0)
        t=np.linspace(0,1,NCTRL+1)
        u=np.linspace(0,1,M,endpoint=False)
        out=[]
        for j in range(2):
            y=np.vstack([q[j],q[j,0]])
            out.append(CubicSpline(t,y,axis=0,bc_type='periodic')(u))
        return out[0],out[1]
    def src(self,cs):
        samples=[]
        for c in cs: samples.append(np.vstack([c,.5*(c+np.roll(c,-1,axis=0))]))
        dist,_=cKDTree(np.vstack(samples)).query(self.gp,k=1,workers=1)
        s=np.exp(-(dist*dist)/(2*A_THICK*A_THICK)).reshape(N,N,N)
        return s/(s.sum()*self.H**3)
    def physical_energy(self,z):
        self.nfev+=1; cs=self.curves(z,M_ENERGY)
        psi=solve_psi(self.src(cs),self.H,L3=self.L3,rtol=1e-5,maxiter=600)
        return float(sum(tension_energy(c,T0) for c in cs)+KAPPA*field_energy(psi,self.H))
    def smooth_thickness_penalty(self,z):
        a,b=self.curves(z,96)
        d=np.sqrt(np.sum((a[:,None,:]-b[None,:,:])**2,axis=2)+1e-14)
        # Smooth hinge, averaged over near-contact pairs; negligible well above target.
        h=np.logaddexp(0.0,BETA*(D_TARGET-d))/BETA
        return float(PENALTY*np.sum(h*h))
    def augmented(self,z): return self.physical_energy(z)+self.smooth_thickness_penalty(z)
    def grad(self,z,augmented=True):
        f=self.augmented if augmented else self.physical_energy
        g=np.empty_like(z)
        for i in range(len(z)):
            d=np.zeros_like(z); d[i]=FD
            g[i]=(f(z+d)-f(z-d))/(2*FD)
        # Remove the exact global translation gauge.
        gg=g.reshape(2,NCTRL,3); gg-=gg.reshape(-1,3).mean(0)
        return gg.ravel()
    def cert_level(self,z,M):
        c1,c2=self.curves(z,M)
        return segment_distance_min(c1,c2),float(linking_number(c1,c2))
    def cert(self,z):
        vals=[self.cert_level(z,M) for M in CERT_BASE]
        need_fine=(min(v[0] for v in vals)<D_FLOOR+.012 or
                   abs(vals[0][1]-vals[1][1])>.008 or abs(vals[0][0]-vals[1][0])>.004)
        if need_fine: vals.append(self.cert_level(z,CERT_FINE))
        d=min(v[0] for v in vals); lk=vals[-1][1]
        lkerr=max(abs(abs(v[1])-1) for v in vals)
        agree=max(v[1] for v in vals)-min(v[1] for v in vals) <= .02
        dagree=max(v[0] for v in vals)-min(v[0] for v in vals) <= .01
        return d,lk,bool(d>=D_FLOOR and lkerr<=LK_TOL and agree and dagree),vals
    def separation_gradient(self,z):
        g=np.empty_like(z)
        for i in range(len(z)):
            d=np.zeros_like(z); d[i]=FD_CON
            g[i]=(self.cert_level(z+d,128)[0]-self.cert_level(z-d,128)[0])/(2*FD_CON)
        gg=g.reshape(2,NCTRL,3); gg-=gg.reshape(-1,3).mean(0)
        return gg.ravel()
    def project_tangent(self,z,v,dmin):
        v=v.copy().reshape(2,NCTRL,3); v-=v.reshape(-1,3).mean(0); v=v.ravel()
        cg=None
        if dmin-D_FLOOR<D_ACTIVE:
            cg=self.separation_gradient(z); cn=np.dot(cg,cg); cv=np.dot(cg,v)
            if cv<0 and cn>1e-16: v-=cg*(cv/cn)
        return v,cg
    def path_cert(self,a,b):
        delta=np.linalg.norm(b-a); ns=max(7,min(17,int(np.ceil(delta/.003))+1))
        wd=1e9; we=0.0
        for t in np.linspace(0,1,ns):
            z=(1-t)*a+t*b; d,lk=self.cert_level(z,128)
            wd=min(wd,d); we=max(we,abs(abs(lk)-1))
            if d<D_FLOOR or abs(abs(lk)-1)>LK_TOL: return False,wd,we,ns
        d,lk,ok,vals=self.cert(b)
        return ok,min(wd,d),max(we,max(abs(abs(v[1])-1) for v in vals)),ns
    def metrics(self,z):
        c1,c2=self.curves(z,256); p=np.vstack([c1,c2]); p-=p.mean(0)
        r=float(np.sqrt(np.mean(np.sum(p*p,axis=1))))
        d,lk,ok,vals=self.cert(z)
        return r,d,lk,ok,vals

def lbfgs(g,S,Y):
    q=g.copy(); rec=[]
    for s,y in zip(reversed(S),reversed(Y)):
        rho=1/max(np.dot(y,s),1e-14); a=rho*np.dot(s,q); rec.append((a,rho)); q-=a*y
    if S: q*=np.dot(S[-1],Y[-1])/max(np.dot(Y[-1],Y[-1]),1e-14)
    for s,y,(a,rho) in zip(S,Y,reversed(rec)): q+=s*(a-rho*np.dot(y,q))
    return -q

def initial_state(m):
    fm=FourierModel(); x=np.load(ROOT/'analysis'/'ELEC006_state.npz')['x_final']
    c1,c2=fm.curves(x,256)
    idx=(np.arange(NCTRL)*256//NCTRL).astype(int)
    z=np.stack([c1[idx],c2[idx]]).ravel()
    z=z.reshape(2,NCTRL,3); z-=z.reshape(-1,3).mean(0)
    return z.ravel()

def test():
    t0=time.time(); m=SplineModel(); z=initial_state(m)
    ep=m.physical_energy(z); ea=ep+m.smooth_thickness_penalty(z); ep0=ep
    ga=m.grad(z,True); S=[]; Y=[]; hist=[]; accepted=0
    r,d,lk,ok,vals=m.metrics(z)
    print(f'start Ephys={ep:.9f} Eaug={ea:.9f} R={r:.6f} d={d:.7f} Lk={lk:.8f} cert={ok}',flush=True)
    for it in range(MAXITER):
        p=lbfgs(ga,S,Y); p,_=m.project_tangent(z,p,d)
        if np.dot(ga,p)>=-1e-12: p,_=m.project_tangent(z,-ga,d); S.clear();Y.clear()
        pn=np.linalg.norm(p)
        if pn>.18: p*=.18/pn
        slope=float(np.dot(ga,p)); alpha=min(1.0,max(.02,.25*max(d-D_FLOOR,.001)/max(np.linalg.norm(p),1e-12)))
        took=False; wd=we=np.nan; ns=0
        for _ in range(16):
            trial=z+alpha*p
            feasible,wd,we,ns=m.path_cert(z,trial)
            if feasible:
                ept=m.physical_energy(trial); eat=ept+m.smooth_thickness_penalty(trial)
                if eat<=ea+ARMIJO*alpha*slope:
                    gan=m.grad(trial,True); s=trial-z; y=gan-ga
                    if np.dot(s,y)>1e-9:
                        S.append(s);Y.append(y)
                        if len(S)>MEMORY:S.pop(0);Y.pop(0)
                    z,ep,ea,ga=trial,ept,eat,gan; took=True; accepted+=1; break
            alpha*=.5
            if alpha<MIN_STEP: break
        r,d,lk,ok,vals=m.metrics(z)
        gp=m.grad(z,False); pstat,_=m.project_tangent(z,-gp,d)
        rel=float(np.linalg.norm(pstat)/max(abs(ep),1e-12))
        hist.append((it,ep,ea,r,d,lk,np.linalg.norm(pstat),rel,alpha,int(took),wd,we,ns,len(vals)))
        print(f'iter={it:02d} Ephys={ep:.9f} Eaug={ea:.9f} d={d:.7f} Lk={lk:.7f} |PTg|/E={rel:.5f} a={alpha:.3g} ok={took}',flush=True)
        if not took: break
    gp=m.grad(z,False); pstat,_=m.project_tangent(z,-gp,d); rel=float(np.linalg.norm(pstat)/abs(ep))
    r,d,lk,ok,vals=m.metrics(z)
    b1=ok; b2=ep<ep0-1e-5
    b3=all(h[4]>=D_FLOOR and abs(abs(h[5])-1)<=LK_TOL for h in hist)
    b4=accepted>=6; b5=rel<.05
    finding='SPLINE_CONSTRAINED_STATIONARY' if all((b1,b2,b3,b4,b5)) else ('SPLINE_CERTIFIED_DESCENT_NOT_STATIONARY' if all((b1,b2,b3,b4)) else 'SPLINE_CONSTRAINED_METHOD_FAILED')
    np.savez(ROOT/'analysis'/'ELEC007_state.npz',z_final=z,energy_start=ep0,energy_final=ep,physical_gradient_final=gp,projected_gradient_final=pstat)
    with (ROOT/'analysis'/'ELEC007_history.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['iteration','physical_energy','augmented_energy','R_rms','dmin','Lk','projected_physical_gradient_norm','projected_gradient_over_E','alpha','accepted','path_worst_d','path_worst_lk_error','path_samples','certificate_levels']);w.writerows(hist)
    print('\nELEC-007 direct-spline augmented constrained solver')
    print(f'start Ephys={ep0:.9f}; final Ephys={ep:.9f}; accepted={accepted}; evaluations={m.nfev}')
    print(f'final R={r:.6f}, dmin={d:.8f}, Lk={lk:.8f}, projected physical gradient/E={rel:.7g}')
    for name,b in [('B1 adaptive topology certificate',b1),('B2 physical energy decreases',b2),('B3 all accepted states certified',b3),('B4 at least 6 accepted steps',b4),('B5 projected physical stationarity <0.05',b5)]:print(name+': '+('PASS' if b else 'FAIL'))
    print('FINDING:',finding);print(f'elapsed={time.time()-t0:.1f}s')
    return locals()
if __name__=='__main__':test()
