"""ELEC-004A: gauge-fixed internal Hessian stability of the matched K=8 state.

This benchmark computes the deterministic projected finite-difference Hessian within a 20-dimensional subspace of the 97-parameter
K=8 curve basis used by ELEC-003A (one log-radius coordinate plus 96 Fourier
coefficients), with the sourced Poisson field re-solved at every evaluation.
The curve construction removes the centre of mass, so the three translational
zero modes are gauge-fixed out of this coordinate chart. Rotational zero modes
are not asserted as exact because the finite grid and Fourier discretisation
break continuous rotational symmetry weakly.

Locked interpretation bars:
 B1 reference state remains localized and linked.
 B2 finite-difference gradient is small relative to the energy scale.
 B3 no robust negative-curvature mode: lowest eigenvalue is nonnegative within
    the finite-difference stability tolerance and remains so under step checks.
 B4 all non-gauge internal modes are positive above tolerance.
 B5 a finite internal stiffness gap is resolved.

This is a reduced, finite-grid, adiabatic-field linear-stability result. It is
not a continuum proof and does not identify the object as an electron.
"""
from pathlib import Path
import csv, sys, time
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from rope_solver.psi.solver import grid, solve_psi, field_energy, laplacian_3d
from rope_solver.topology.linking import hopf_curves, linking_number
from rope_solver.geometry.curve import tension_energy

N=14; L_BOX=8.0; A_THICK=.24; M=24; K=8; KAPPA=2.0; T0=1.0
HSTEP=2.5e-3

def build_energy():
    coords,X,Y,Z,H=grid(N,L_BOX)
    gp=np.stack([X.ravel(),Y.ravel(),Z.ravel()],axis=1)
    L3=laplacian_3d(N,H)
    t=np.linspace(0,2*np.pi,M,endpoint=False)
    basis=np.array([f(k*t) for k in range(1,K+1) for f in (np.sin,np.cos)])
    def curves(z):
        R=float(np.exp(z[0])); c1,c2=hopf_curves(M,R=R)
        coeff=z[1:].reshape(2,3,2*K); out=[]
        for j,c in enumerate((c1,c2)):
            d=np.einsum('ak,kn->na',coeff[j],basis); out.append(c+d)
        cen=np.vstack(out).mean(0)
        return out[0]-cen,out[1]-cen
    def src(cs):
        d2=np.full(len(gp),np.inf)
        for c in cs:
            samples=np.vstack([c,.5*(c+np.roll(c,-1,axis=0))])
            for p in samples: d2=np.minimum(d2,np.sum((gp-p)**2,axis=1))
        s=np.exp(-d2/(2*A_THICK*A_THICK)).reshape(N,N,N)
        return s/(s.sum()*H**3)
    def energy(z):
        cs=curves(z)
        psi=solve_psi(src(cs),H,L3=L3,rtol=1e-5,maxiter=600)
        return float(sum(tension_energy(c,T0) for c in cs)+KAPPA*field_energy(psi,H))
    return energy,curves

def finite_gradient(E,x,h):
    n=len(x); g=np.empty(n)
    for i in range(n):
        d=np.zeros(n); d[i]=h
        g[i]=(E(x+d)-E(x-d))/(2*h)
    return g

def projected_hessian(E,x,Q,h):
    """Central-difference Hessian projected into columns of orthonormal Q."""
    m=Q.shape[1]; H=np.empty((m,m)); E0=E(x)
    steps=[h*Q[:,i] for i in range(m)]
    for i in range(m):
        H[i,i]=(E(x+steps[i])-2*E0+E(x-steps[i]))/(h*h)
    for i in range(m):
        for j in range(i+1,m):
            v=(E(x+steps[i]+steps[j])-E(x+steps[i]-steps[j])-E(x-steps[i]+steps[j])+E(x-steps[i]-steps[j]))/(4*h*h)
            H[i,j]=H[j,i]=v
    return .5*(H+H.T)

def directional_curvature(E,x,v,h):
    v=v/np.linalg.norm(v); e0=E(x)
    return (E(x+h*v)-2*e0+E(x-h*v))/(h*h)

def test():
    t0=time.time(); state=ROOT/'analysis'/'ELEC003A_states.npz'
    if not state.exists():
        raise FileNotFoundError('Run ELEC-003A state export first: '+str(state))
    x=np.load(state)['x_K8']; E,curves=build_energy(); e0=E(x); cs=curves(x)
    pts=np.vstack(cs); pts-=pts.mean(0); rr=float(np.sqrt(np.mean(np.sum(pts*pts,axis=1))))
    lk=float(linking_number(*cs))
    g=finite_gradient(E,x,HSTEP)
    # A deterministic 20-dimensional internal subspace: radial direction,
    # normalized gradient, 10 harmonic-block directions, and seeded random
    # complements. Translation is already removed by centre-of-mass gauge fixing.
    dirs=[]
    er=np.zeros_like(x); er[0]=1.; dirs.append(er)
    if np.linalg.norm(g)>0: dirs.append(g/np.linalg.norm(g))
    coeff=x[1:].reshape(2,3,16)
    for rope in range(2):
        for k in range(5):
            v=np.zeros_like(x); block=v[1:].reshape(2,3,16)
            block[rope,:,2*k:2*k+2]=coeff[rope,:,2*k:2*k+2]
            if np.linalg.norm(v)>1e-12: dirs.append(v/np.linalg.norm(v))
    rng=np.random.default_rng(4048)
    while len(dirs)<20: dirs.append(rng.normal(size=len(x)))
    Q,_=np.linalg.qr(np.column_stack(dirs)); Q=Q[:,:20]
    Hm=projected_hessian(E,x,Q,HSTEP)
    vals,u=np.linalg.eigh(Hm); vecs=Q@u
    # Validate the six softest projected eigenvectors at independent step sizes.
    checks=[]
    for q in range(6):
        v=vecs[:,q]
        checks.append([directional_curvature(E,x,v,h) for h in (1.25e-3,2.5e-3,5e-3)])
    checks=np.asarray(checks)
    robust_min=float(np.min(checks))
    scale=max(1.0,float(np.max(np.abs(vals))))
    neg_tol=5e-3*scale
    zero_tol=1e-3*scale
    positive=vals[vals>zero_tol]
    gap=float(positive[0]) if len(positive) else float('nan')
    grad_rel=float(np.linalg.norm(g)/max(e0,1e-12))
    b1=(.4<rr<2.0 and abs(abs(lk)-1)<.22)
    b2=grad_rel<.10
    b3=(vals[0]>=-neg_tol and robust_min>=-neg_tol)
    b4=(np.sum(vals<-neg_tol)==0)
    b5=(np.isfinite(gap) and gap>zero_tol)
    np.savez(ROOT/'analysis'/'ELEC004A_hessian.npz',x=x,gradient=g,projected_hessian=Hm,subspace=Q,eigenvalues=vals,eigenvectors=vecs,soft_checks=checks)
    with (ROOT/'analysis'/'ELEC004A_spectrum.csv').open('w',newline='') as f:
        w=csv.writer(f); w.writerow(['index','eigenvalue'])
        for i,v in enumerate(vals): w.writerow([i,float(v)])
    print('ELEC-004A gauge-fixed internal Hessian')
    print(f'E={e0:.9f} R_rms={rr:.6f} |Lk|={abs(lk):.6f}')
    print(f'gradient norm={np.linalg.norm(g):.6g}; relative={grad_rel:.6g}')
    print('lowest 12 eigenvalues:',', '.join(f'{v:.7g}' for v in vals[:12]))
    print(f'max |lambda|={scale:.7g}; negative tolerance={neg_tol:.7g}; zero tolerance={zero_tol:.7g}')
    print(f'negative modes below tolerance={int(np.sum(vals<-neg_tol))}; near-zero modes={int(np.sum(np.abs(vals)<=zero_tol))}; positive gap={gap:.7g}')
    print('soft-mode step checks:')
    for i,row in enumerate(checks): print(f'  mode {i}: '+', '.join(f'{v:.7g}' for v in row))
    for name,b in [('B1 linked/localized reference',b1),('B2 near-stationary gradient',b2),('B3 no robust negative mode',b3),('B4 remaining internal spectrum nonnegative',b4),('B5 finite internal gap',b5)]:
        print(name+': '+('PASS' if b else 'FAIL'))
    if not b2:
        finding='NONSTATIONARY_REFERENCE: Hessian classification is not valid until the K=8 state is re-optimized to a small gradient.'
    elif all((b1,b2,b3,b4,b5)):
        finding='LINEARLY_STABLE_IN_PROJECTED_CHART'
    elif not b3 or not b4:
        finding='POSSIBLE_NEGATIVE_INTERNAL_MODE: requires step-stable confirmation.'
    else:
        finding='INCONCLUSIVE_GAP'
    print('FINDING:',finding); print(f'elapsed {time.time()-t0:.1f}s')
    return dict(B1=b1,B2=b2,B3=b3,B4=b4,B5=b5,finding=finding,eigenvalues=vals,gradient=g)

if __name__=='__main__': test()
