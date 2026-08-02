"""ELEC-005: topology-preserving constrained variational pilot.

Starts from the saved ELEC-003A K=8 coefficients, retracts them along a
coefficient homotopy to the nearest numerically certified linked polygonal
state, then minimizes the same Poisson curve-field energy with finite-
difference projected gradient descent and a topology-certified backtracking
line search.

Certification is exact for the sampled polygonal curves (M_CERT vertices):
all inter-component segment pairs must remain separated by D_FLOOR and the
high-resolution Gauss integral must remain within LK_TOL of unit linking at
all interpolation points along every accepted line-search step.
"""
from pathlib import Path
import sys, time, csv
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from rope_solver.psi.solver import grid, solve_psi, field_energy, laplacian_3d
from rope_solver.topology.linking import hopf_curves, linking_number
from rope_solver.geometry.curve import tension_energy

N=14; L_BOX=8.0; A_THICK=.24; K=8; M_ENERGY=64; M_CERT=128
KAPPA=2.0; T0=1.0; FD=1e-4; D_FLOOR=.06; LK_TOL=.03
MAXITER=6; PATH_SAMPLES=3


def segment_distance_min(A,B):
    """Minimum Euclidean distance between two closed polygonal curves."""
    P=A[:,None,:]; Q=np.roll(A,-1,axis=0)[:,None,:]
    R=B[None,:,:]; S=np.roll(B,-1,axis=0)[None,:,:]
    u=Q-P; v=S-R; w=P-R
    a=np.sum(u*u,axis=2); b=np.sum(u*v,axis=2); c=np.sum(v*v,axis=2)
    d=np.sum(u*w,axis=2); e=np.sum(v*w,axis=2)
    den=a*c-b*b
    sc=np.where(den>1e-14,(b*e-c*d)/den,0.0)
    tc=np.where(den>1e-14,(a*e-b*d)/den,np.where(c>1e-14,e/c,0.0))
    sc=np.clip(sc,0,1); tc=np.clip(tc,0,1)
    # Recompute one coordinate after clipping, twice, for segment endpoint cases.
    tc=np.where(c>1e-14,np.clip((b*sc+e)/c,0,1),0.0)
    sc=np.where(a>1e-14,np.clip((b*tc-d)/a,0,1),0.0)
    D=w+sc[:,:,None]*u-tc[:,:,None]*v
    return float(np.sqrt(np.min(np.sum(D*D,axis=2))))

class Model:
    def __init__(self):
        _,X,Y,Z,self.H=grid(N,L_BOX)
        self.gp=np.stack([X.ravel(),Y.ravel(),Z.ravel()],axis=1)
        self.L3=laplacian_3d(N,self.H)
        self.basis={}
        for M in (M_ENERGY,M_CERT):
            t=np.linspace(0,2*np.pi,M,endpoint=False)
            self.basis[M]=np.array([f(k*t) for k in range(1,K+1) for f in (np.sin,np.cos)])
        self.nfev=0
    def curves(self,z,M):
        R=float(np.exp(z[0])); c1,c2=hopf_curves(M,R=R)
        co=z[1:].reshape(2,3,2*K); out=[]
        for j,c in enumerate((c1,c2)):
            out.append(c+np.einsum('ak,kn->na',co[j],self.basis[M]))
        cen=np.vstack(out).mean(0)
        return out[0]-cen,out[1]-cen
    def src(self,cs):
        d2=np.full(len(self.gp),np.inf)
        for c in cs:
            samples=np.vstack([c,.5*(c+np.roll(c,-1,axis=0))])
            for p in samples: d2=np.minimum(d2,np.sum((self.gp-p)**2,axis=1))
        s=np.exp(-d2/(2*A_THICK*A_THICK)).reshape(N,N,N)
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
        return g
    def cert(self,z):
        c1,c2=self.curves(z,M_CERT)
        d=segment_distance_min(c1,c2); lk=float(linking_number(c1,c2))
        return d,lk,(d>=D_FLOOR and abs(abs(lk)-1)<=LK_TOL)
    def path_cert(self,a,b):
        worst_d=1e9; worst_lk=0.0
        for t in np.linspace(0,1,PATH_SAMPLES):
            z=(1-t)*a+t*b; d,lk,ok=self.cert(z)
            worst_d=min(worst_d,d); worst_lk=max(worst_lk,abs(abs(lk)-1))
            if not ok: return False,worst_d,worst_lk
        return True,worst_d,worst_lk
    def metrics(self,z):
        c1,c2=self.curves(z,M_CERT); p=np.vstack((c1,c2)); p-=p.mean(0)
        return float(np.sqrt(np.mean(np.sum(p*p,axis=1)))),*self.cert(z)[:2]

def test():
    t0=time.time(); m=Model(); saved=np.load(ROOT/'analysis'/'ELEC003A_states.npz')['x_K8'].astype(float)
    d_saved,lk_saved,ok_saved=m.cert(saved)
    # Retraction toward the canonical Hopf link, preserving radius, to find the
    # largest coefficient amplitude admitted by the numerical certificate.
    lo,hi=0.0,1.0
    for _ in range(24):
        mid=(lo+hi)/2; z=saved.copy(); z[1:]*=mid
        dmid,lkmid,okmid=m.cert(z)
        if okmid and dmid>=0.09: lo=mid
        else: hi=mid
    alpha=max(0.0,lo-1e-4); x=saved.copy(); x[1:]*=alpha
    x_start=x.copy(); e=m.energy(x); e0=e; g0=m.gradient(x); hist=[]
    bounds_lo=np.r_[np.log(.35),np.full(len(x)-1,-.35)]
    bounds_hi=np.r_[np.log(1.8),np.full(len(x)-1,.35)]
    accepted=0
    for it in range(MAXITER):
        g=m.gradient(x)
        # Project against active box constraints; the separation/topology
        # tangent cone is enforced by the certified trust-region line search.
        p=-g
        p[(x<=bounds_lo+1e-8)&(p<0)]=0; p[(x>=bounds_hi-1e-8)&(p>0)]=0
        pg=float(np.linalg.norm(p));
        if pg<1e-8: break
        p/=pg
        dcur,_,_=m.cert(x)
        # Geometric trust radius: no trial may consume more than 20% of the
        # current certified separation margin before full path certification.
        step=min(.04,max(.002,.2*(dcur-D_FLOOR)))
        took=False
        for _ls in range(14):
            trial=np.clip(x+step*p,bounds_lo,bounds_hi)
            ok,wd,wlk=m.path_cert(x,trial)
            if ok:
                en=m.energy(trial)
                if en < e-1e-8:
                    x,e=trial,en; accepted+=1; took=True; break
            step*=.5
        r,d,lk=m.metrics(x); hist.append((it,e,r,d,lk,pg,step,int(took)))
        print(f'iter={it:02d} E={e:.9f} R={r:.6f} dmin={d:.6f} Lk={lk:.6f} |Pg|={pg:.5g} accepted={took}',flush=True)
        if not took: break
    gf=m.gradient(x); pgf=np.linalg.norm(gf); r,d,lk=m.metrics(x)
    rel=pgf/max(abs(e),1e-12)
    b1=ok_saved is False
    b2=(d>=D_FLOOR and abs(abs(lk)-1)<=LK_TOL and accepted>0)
    b3=e<e0
    b4=rel<.05
    b5=all(row[3]>=D_FLOOR and abs(abs(row[4])-1)<=LK_TOL for row in hist)
    np.savez(ROOT/'analysis'/'ELEC005_state.npz',x_saved=saved,x_start=x_start,x_final=x,
             alpha_retraction=alpha,energy_start=e0,energy_final=e,gradient_final=gf)
    with (ROOT/'analysis'/'ELEC005_history.csv').open('w',newline='') as f:
        w=csv.writer(f); w.writerow(['iteration','energy','R_rms','dmin','linking_number','projected_gradient_norm','step','accepted']); w.writerows(hist)
    print('\nELEC-005 topology-preserving constrained variational pilot')
    print(f'saved-state certificate: dmin={d_saved:.8f}, Lk={lk_saved:.8f}, certified={ok_saved}')
    print(f'nearest certified homotopy retraction alpha={alpha:.6f}')
    print(f'start E={e0:.9f}; final E={e:.9f}; accepted steps={accepted}; evaluations={m.nfev}')
    print(f'final R={r:.6f}, dmin={d:.6f}, Lk={lk:.8f}, projected-gradient/E={rel:.6g}')
    for name,b in [('B1 saved K8 fails high-resolution certificate (diagnostic)',b1),('B2 certified linked manifold retained',b2),('B3 physical energy decreases',b3),('B4 projected stationarity <0.05',b4),('B5 every accepted state certified',b5)]: print(name+': '+('PASS' if b else 'FAIL'))
    finding='CONSTRAINED_STATIONARY' if all((b2,b3,b4,b5)) else ('CERTIFIED_DESCENT_NOT_STATIONARY' if all((b2,b3,b5)) else 'CONSTRAINED_METHOD_FAILED')
    print('FINDING:',finding); print(f'elapsed={time.time()-t0:.1f}s')
    return dict(B1=b1,B2=b2,B3=b3,B4=b4,B5=b5,finding=finding,alpha=alpha,rel=rel)

if __name__=='__main__': test()
