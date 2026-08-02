"""ELEC-004A-R: deterministic stationarity repair of the matched K=8 state.

Starts from ELEC003A_states.npz:x_K8 and minimizes the same sourced Poisson
curve-field energy with bounded L-BFGS-B and an explicit central finite-
difference gradient.  The field is re-solved at every objective evaluation.

Locked bars:
 B1 linked/localized geometry retained.
 B2 energy does not increase.
 B3 relative finite-difference gradient ||grad E||/E < 0.02.
 B4 optimizer termination is supported by a separately recomputed gradient.

This is a finite-grid stationarity repair, not a continuum stability proof.
"""
from pathlib import Path
import sys, time, csv
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from scipy.optimize import minimize

ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from rope_solver.psi.solver import grid, solve_psi, field_energy, laplacian_3d
from rope_solver.topology.linking import hopf_curves, linking_number
from rope_solver.geometry.curve import tension_energy

N=14; L_BOX=8.0; A_THICK=.24; M=24; K=8; KAPPA=2.0; T0=1.0
FD_STEP=1.0e-4

class Model:
    def __init__(self):
        coords,X,Y,Z,self.H=grid(N,L_BOX)
        self.gp=np.stack([X.ravel(),Y.ravel(),Z.ravel()],axis=1)
        self.L3=laplacian_3d(N,self.H)
        t=np.linspace(0,2*np.pi,M,endpoint=False)
        self.basis=np.array([f(k*t) for k in range(1,K+1) for f in (np.sin,np.cos)])
        self.nfev=0; self.ngev=0
    def curves(self,z):
        R=float(np.exp(z[0])); c1,c2=hopf_curves(M,R=R)
        coeff=z[1:].reshape(2,3,2*K); out=[]
        for j,c in enumerate((c1,c2)):
            d=np.einsum('ak,kn->na',coeff[j],self.basis); out.append(c+d)
        cen=np.vstack(out).mean(0)
        return out[0]-cen,out[1]-cen
    def src(self,cs):
        d2=np.full(len(self.gp),np.inf)
        for c in cs:
            samples=np.vstack([c,.5*(c+np.roll(c,-1,axis=0))])
            for p in samples: d2=np.minimum(d2,np.sum((self.gp-p)**2,axis=1))
        s=np.exp(-d2/(2*A_THICK*A_THICK)).reshape(N,N,N)
        return s/(s.sum()*self.H**3)
    def physical_energy(self,z):
        self.nfev+=1
        cs=self.curves(z)
        psi=solve_psi(self.src(cs),self.H,L3=self.L3,rtol=1e-5,maxiter=600)
        return float(sum(tension_energy(c,T0) for c in cs)+KAPPA*field_energy(psi,self.H))
    def min_separation(self,z):
        c1,c2=self.curves(z)
        return float(np.sqrt(np.min(np.sum((c1[:,None,:]-c2[None,:,:])**2,axis=2))))
    def energy(self,z):
        # A short-range barrier prevents strand crossing while remaining inactive
        # at the reference state and for the finite-difference stencil.
        e=self.physical_energy(z)
        d=self.min_separation(z)
        deficit=max(0.0,0.012-d)
        return e + 1.0e7*deficit**4
    def gradient(self,z,h=FD_STEP):
        self.ngev+=1
        g=np.empty_like(z)
        for i in range(len(z)):
            d=np.zeros_like(z); d[i]=h
            g[i]=(self.energy(z+d)-self.energy(z-d))/(2*h)
        return g
    def metrics(self,z):
        cs=self.curves(z); p=np.vstack(cs); p-=p.mean(0)
        return float(np.sqrt(np.mean(np.sum(p*p,axis=1)))),float(linking_number(*cs))

def test(maxiter=45):
    t0=time.time(); state=ROOT/'analysis'/'ELEC003A_states.npz'
    x0=np.load(state)['x_K8'].astype(float)
    m=Model(); e0=m.physical_energy(x0); r0,lk0=m.metrics(x0); g0=m.gradient(x0)
    history=[]
    def fun(x): return m.energy(x)
    def jac(x): return m.gradient(x)
    def callback(xk):
        e=m.physical_energy(xk); r,lk=m.metrics(xk); history.append((len(history),e,r,lk))
        print(f'iter={len(history):02d} E={e:.9f} R={r:.6f} |Lk|={abs(lk):.6f}',flush=True)
    bounds=[(np.log(.35),np.log(1.8))]+[(-.35,.35)]*(len(x0)-1)
    res=minimize(fun,x0,jac=jac,method='L-BFGS-B',bounds=bounds,callback=callback,
                 options={'maxiter':maxiter,'maxfun':4000,'ftol':1e-10,'gtol':1e-5,'maxls':6,'maxcor':8})
    x=res.x; ef=m.physical_energy(x); rf,lkf=m.metrics(x)
    # Independent step checks to guard against finite-difference cancellation/noise.
    checks=[]
    for h in (5e-5,1e-4,2e-4):
        g=m.gradient(x,h); checks.append((h,float(np.linalg.norm(g)),float(np.linalg.norm(g)/max(ef,1e-12))))
    grad_rel=checks[1][2]
    b1=(.4<rf<2.0 and abs(abs(lkf)-1)<.22)
    b2=ef<=e0+1e-9
    b3=grad_rel<.02
    b4=max(c[2] for c in checks)<.03
    np.savez(ROOT/'analysis'/'ELEC004AR_state.npz',x_start=x0,x_repaired=x,
             energy_start=e0,energy_final=ef,gradient_start=g0,gradient_checks=np.array(checks,dtype=float))
    with (ROOT/'analysis'/'ELEC004AR_history.csv').open('w',newline='') as f:
        w=csv.writer(f); w.writerow(['iteration','energy','R_rms','linking_number']); w.writerows(history)
    print('\nELEC-004A-R deterministic stationarity repair')
    print(f'start: E={e0:.9f} R={r0:.6f} |Lk|={abs(lk0):.6f} grad_rel={np.linalg.norm(g0)/e0:.6g}')
    print(f'final: E={ef:.9f} R={rf:.6f} |Lk|={abs(lkf):.6f}')
    print(f'optimizer: success={res.success} status={res.status} nit={res.nit} message={res.message}')
    print(f'evaluations: energy={m.nfev} gradient={m.ngev}')
    for h,n,r in checks: print(f'gradient check h={h:.5g}: norm={n:.7g} relative={r:.7g}')
    for name,b in [('B1 linked/localized geometry',b1),('B2 energy nonincrease',b2),('B3 relative gradient <0.02',b3),('B4 step-robust relative gradient <0.03',b4)]:
        print(name+': '+('PASS' if b else 'FAIL'))
    if all((b1,b2,b3,b4)): finding='STATIONARITY_REPAIRED'
    elif b1 and b2 and not b3: finding='OPTIMIZATION_DEBT_REMAINS'
    elif not b1: finding='LEFT_LINKED_LOCALIZED_BASIN'
    else: finding='INCONCLUSIVE'
    print('FINDING:',finding); print(f'elapsed {time.time()-t0:.1f}s')
    return res,dict(B1=b1,B2=b2,B3=b3,B4=b4,finding=finding,checks=checks)

if __name__=='__main__': test()
