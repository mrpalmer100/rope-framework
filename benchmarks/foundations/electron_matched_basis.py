"""ELEC-003A: matched-start Fourier-basis convergence study.

Determines whether ELEC-003's K=4->5 radius miss was caused by independent
initialization / insufficient optimization or reflects persistent high-mode
sensitivity. One converged K=4 state is projected exactly into K=5,6,8 by
zero-padding new coefficients; every stage uses a longer common optimization.
Finite numerical study, not a continuum proof or electron identification.
"""
from pathlib import Path
import csv, sys, time
import numpy as np
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0, str(ROOT))
from rope_solver.psi.solver import grid, solve_psi, field_energy, laplacian_3d
from rope_solver.topology.linking import hopf_curves, linking_number
from rope_solver.geometry.curve import tension_energy

L_BOX=8.0; KAPPA=2.0; T0=1.0; M=24

def project_exact(init, K):
    x=np.zeros(1+2*3*(2*K)); x[0]=init[0]
    oldK=((len(init)-1)//6)//2
    oldc=init[1:].reshape(2,3,2*oldK)
    newc=x[1:].reshape(2,3,2*K)
    keep=min(2*oldK,2*K); newc[:,:,:keep]=oldc[:,:,:keep]
    return x

def run_case(N=14,K=4,a_thick=.24,seed=404,iters=180,init=None,perturb=.05):
    coords,X,Y,Z,H=grid(N,L_BOX); gp=np.stack([X.ravel(),Y.ravel(),Z.ravel()],axis=1); L3=laplacian_3d(N,H)
    t=np.linspace(0,2*np.pi,M,endpoint=False)
    basis=np.array([f(k*t) for k in range(1,K+1) for f in (np.sin,np.cos)])
    rng=np.random.default_rng(seed); ncoef=2*3*(2*K)
    if init is None:
        x=np.zeros(1+ncoef); x[0]=np.log(.85); x[1:]=rng.normal(0,perturb,ncoef)
    else:
        x=project_exact(init,K)
    def curves(z):
        R=float(np.exp(z[0])); c1,c2=hopf_curves(M,R=R)
        coeff=z[1:].reshape(2,3,2*K); out=[]
        for j,c in enumerate((c1,c2)):
            d=np.einsum('ak,kn->na',coeff[j],basis); out.append(c+d)
        cen=np.vstack(out).mean(0); return out[0]-cen,out[1]-cen
    def src(cs):
        d2=np.full(len(gp),np.inf)
        for c in cs:
            samples=np.vstack([c,.5*(c+np.roll(c,-1,axis=0))])
            for p in samples: d2=np.minimum(d2,np.sum((gp-p)**2,axis=1))
        s=np.exp(-d2/(2*a_thick*a_thick)).reshape(N,N,N)
        return s/(s.sum()*H**3)
    def energy(z):
        cs=curves(z); psi=solve_psi(src(cs),H,L3=L3,rtol=1e-5,maxiter=600)
        return sum(tension_energy(c,T0) for c in cs)+KAPPA*field_energy(psi,H)
    e=energy(x); e0=e; hist=[e]; mom=np.zeros_like(x); var=np.zeros_like(x); accepted=0
    last_change=np.inf
    for it in range(1,iters+1):
        delta=rng.choice((-1.,1.),size=len(x)); ck=.022/(1+it/120)**.15
        ep=energy(x+ck*delta); em=energy(x-ck*delta); g=((ep-em)/(2*ck))*delta
        mom=.9*mom+.1*g; var=.999*var+.001*g*g
        step=.013/(1+it/180)**.45*(mom/(1-.9**it))/(np.sqrt(var/(1-.999**it))+1e-8)
        old=e
        for frac in (1.,.5,.25,.125):
            tr=x-frac*step; tr[0]=np.clip(tr[0],np.log(.35),np.log(1.8)); tr[1:]=np.clip(tr[1:],-.35,.35)
            lk=abs(linking_number(*curves(tr)))
            if abs(lk-1)>.22: continue
            en=energy(tr)
            if en<=e+1e-10: x,e=tr,en; accepted+=1; break
        last_change=abs(old-e)/max(abs(old),1e-12); hist.append(e)
    cs=curves(x); pts=np.vstack(cs); pts-=pts.mean(0)
    rr=float(np.sqrt(np.mean(np.sum(pts*pts,axis=1))))
    coeff=x[1:].reshape(2,3,2*K)
    mode_amp=[]
    for k in range(K):
        mode_amp.append(float(np.linalg.norm(coeff[:,:,2*k:2*k+2])))
    return dict(N=N,K=K,a=a_thick,seed=seed,E0=e0,Ef=e,drop=(e0-e)/e0,R=rr,
                Lk=float(linking_number(*cs)),monotone=bool(np.all(np.diff(hist)<=1e-9)),
                accepted=accepted,last_rel_change=last_change,mode_amp=mode_amp,x=x)

def test():
    rows=[]; t0=time.time()
    r4=run_case(K=4,seed=404,iters=220,init=None,perturb=.05); rows.append(r4)
    prev=r4
    for K,seed in ((5,405),(6,406),(8,408)):
        r=run_case(K=K,seed=seed,iters=220,init=prev['x']); rows.append(r); prev=r
    rel=[]
    for a,b in zip(rows[:-1],rows[1:]): rel.append(abs(b['R']-a['R'])/np.mean([a['R'],b['R']]))
    energy_noninc=all(rows[i+1]['Ef']<=rows[i]['Ef']+1e-8 for i in range(len(rows)-1))
    topo=all(abs(abs(r['Lk'])-1)<.22 for r in rows)
    localized=all(.4<r['R']<2 for r in rows)
    final_rel=abs(rows[-1]['R']-rows[-2]['R'])/np.mean([rows[-1]['R'],rows[-2]['R']])
    high_amp=rows[-1]['mode_amp'][-2:]
    low_scale=max(rows[-1]['mode_amp'][:4]) if max(rows[-1]['mode_amp'][:4])>0 else 1
    high_ratio=max(high_amp)/low_scale
    b1=topo and localized and all(r['monotone'] for r in rows)
    b2=energy_noninc
    b3=final_rel<.10
    b4=high_ratio<.25
    out=ROOT/'analysis'/'ELEC003A_results.csv'; out.parent.mkdir(exist_ok=True)
    with out.open('w',newline='') as f:
        fields=['K','E0','Ef','drop','R','Lk','accepted','last_rel_change','mode_amplitudes']
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
        for r in rows: w.writerow(dict(K=r['K'],E0=r['E0'],Ef=r['Ef'],drop=r['drop'],R=r['R'],Lk=r['Lk'],accepted=r['accepted'],last_rel_change=r['last_rel_change'],mode_amplitudes=';'.join(f'{v:.8g}' for v in r['mode_amp'])))
    print('ELEC-003A matched-start basis convergence')
    for r in rows:
        print('K=%d E=%.8f drop=%6.2f%% R=%.6f |Lk|=%.4f accepted=%d amps=%s'%(r['K'],r['Ef'],100*r['drop'],r['R'],abs(r['Lk']),r['accepted'],','.join(f'{v:.4f}' for v in r['mode_amp'])))
    print('adjacent radius shifts:', ', '.join(f'{100*x:.2f}%%' for x in rel))
    print('B1 topology/descent/localization:', 'PASS' if b1 else 'FAIL')
    print('B2 matched-sequence energy nonincrease:', 'PASS' if b2 else 'FAIL')
    print('B3 K=6->8 radius difference <10%%: %s (%.2f%%)'%(('PASS' if b3 else 'FAIL'),100*final_rel))
    print('B4 highest-mode amplitudes <25%% of low-mode scale: %s (%.2f%%)'%(('PASS' if b4 else 'FAIL'),100*high_ratio))
    if b3 and b4:
        finding='INCOMPLETE_CONVERGENCE: matched starts and longer optimization recover practical basis convergence.'
    elif not b3 and not b4:
        finding='HIGH_FREQUENCY_SENSITIVITY: radius remains basis-sensitive and newly admitted modes remain active.'
    else:
        finding='MIXED: one convergence diagnostic passes and one fails; no clean attribution yet.'
    print('FINDING:',finding); print('elapsed %.1fs'%(time.time()-t0))
    return dict(rows=rows,B1=b1,B2=b2,B3=b3,B4=b4,finding=finding,final_rel=final_rel,high_ratio=high_ratio)
if __name__=='__main__': test()
