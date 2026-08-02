"""ELEC-007: augmented-Lagrangian / SQP-style certified linked-sector search.

Starts from ELEC-006.  The physical energy is unchanged.  A buffered
minimum-separation inequality is handled with a Powell-Hestenes-Rockafellar
augmented Lagrangian, while exact polygonal separation and Gauss-linking
certificates remain hard feasibility conditions on every accepted path.
Endpoint certification is adaptively refined through 128/256/512 samples.
"""
from pathlib import Path
import sys, time, csv
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from rope_solver.psi.solver import grid, solve_psi, field_energy, laplacian_3d
from rope_solver.topology.linking import hopf_curves, linking_number
from rope_solver.geometry.curve import tension_energy

N=14; L_BOX=8.0; A_THICK=.24; K=8; M_ENERGY=64
CERT_LEVELS=(128,256,512); KAPPA=2.0; T0=1.0
FD=1e-4; FD_CON=2e-4
D_HARD=.060; D_TARGET=.066; LK_TOL=.03
MAXITER=5; ARMIJO=1e-4; MIN_STEP=1e-5
RHO0=50.0; TRUST0=.12; TRUST_MIN=.006; TRUST_MAX=.25


def segment_distance_min(A,B):
    P=A[:,None,:]; Q=np.roll(A,-1,axis=0)[:,None,:]
    R=B[None,:,:]; S=np.roll(B,-1,axis=0)[None,:,:]
    u=Q-P; v=S-R; w=P-R
    a=np.sum(u*u,axis=2); b=np.sum(u*v,axis=2); c=np.sum(v*v,axis=2)
    d=np.sum(u*w,axis=2); e=np.sum(v*w,axis=2); den=a*c-b*b
    sc=np.where(den>1e-14,(b*e-c*d)/den,0.0)
    tc=np.where(den>1e-14,(a*e-b*d)/den,np.where(c>1e-14,e/c,0.0))
    sc=np.clip(sc,0,1); tc=np.clip(tc,0,1)
    tc=np.where(c>1e-14,np.clip((b*sc+e)/c,0,1),0.0)
    sc=np.where(a>1e-14,np.clip((b*tc-d)/a,0,1),0.0)
    D=w+sc[:,:,None]*u-tc[:,:,None]*v
    return float(np.sqrt(np.min(np.sum(D*D,axis=2))))

class Model:
    def __init__(self):
        _,X,Y,Z,self.H=grid(N,L_BOX); self.gp=np.stack([X.ravel(),Y.ravel(),Z.ravel()],1)
        self.L3=laplacian_3d(N,self.H); self.nfev=0
        self.basis={}
        for M in (M_ENERGY,)+CERT_LEVELS:
            t=np.linspace(0,2*np.pi,M,endpoint=False)
            self.basis[M]=np.array([f(k*t) for k in range(1,K+1) for f in (np.sin,np.cos)])
    def curves(self,z,M):
        R=float(np.exp(z[0])); c1,c2=hopf_curves(M,R=R); co=z[1:].reshape(2,3,2*K)
        out=[c+np.einsum('ak,kn->na',co[j],self.basis[M]) for j,c in enumerate((c1,c2))]
        cen=np.vstack(out).mean(0); return out[0]-cen,out[1]-cen
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
    def distance(self,z,M=128):
        c1,c2=self.curves(z,M); return segment_distance_min(c1,c2)
    def level(self,z,M):
        c1,c2=self.curves(z,M); return segment_distance_min(c1,c2),float(linking_number(c1,c2))
    def separation_gradient(self,z):
        g=np.empty_like(z)
        for i in range(len(z)):
            q=np.zeros_like(z); q[i]=FD_CON
            g[i]=(self.distance(z+q,128)-self.distance(z-q,128))/(2*FD_CON)
        return g
    def cert(self,z,full=True):
        levels=CERT_LEVELS if full else CERT_LEVELS[:1]
        vals=[self.level(z,M) for M in levels]
        d=min(v[0] for v in vals); lkerr=max(abs(abs(v[1])-1) for v in vals)
        agree=True
        if len(vals)>1:
            agree=max(abs(vals[i][1]-vals[i+1][1]) for i in range(len(vals)-1))<=.02
            agree &= max(abs(vals[i][0]-vals[i+1][0]) for i in range(len(vals)-1))<=.01
        return d,vals[-1][1],bool(d>=D_HARD and lkerr<=LK_TOL and agree),vals
    def path_cert(self,a,b):
        delta=np.linalg.norm(b-a); ns=max(7,min(17,int(np.ceil(delta/.003))+1))
        wd=1e9; we=0.0
        for t in np.linspace(0,1,ns):
            d,lk=self.level((1-t)*a+t*b,128); wd=min(wd,d); we=max(we,abs(abs(lk)-1))
            if d<D_HARD or abs(abs(lk)-1)>LK_TOL: return False,wd,we,ns
        d,lk,ok,vals=self.cert(b,full=True)
        wd=min(wd,d); we=max(we,max(abs(abs(v[1])-1) for v in vals))
        return ok,wd,we,ns
    def radius(self,z):
        c1,c2=self.curves(z,512); p=np.vstack((c1,c2)); p-=p.mean(0)
        return float(np.sqrt(np.mean(np.sum(p*p,axis=1))))

def project_bounds(x,p,lo,hi):
    p=p.copy(); p[(x<=lo+1e-10)&(p<0)]=0; p[(x>=hi-1e-10)&(p>0)]=0; return p

def test():
    t0=time.time(); m=Model(); dat=np.load(ROOT/'analysis'/'ELEC006_state.npz')
    x=dat['x_final'].astype(float); x_start=x.copy()
    lo=np.r_[np.log(.35),np.full(len(x)-1,-.35)]; hi=np.r_[np.log(1.8),np.full(len(x)-1,.35)]
    e=m.energy(x); e0=e; g=m.gradient(x); d,lk,ok,vals=m.cert(x); r=m.radius(x)
    lam=0.0; rho=RHO0; trust=TRUST0; Hscale=1.0; hist=[]; accepted=0
    print(f'start E={e:.9f} R={r:.6f} d={d:.8f} Lk512={lk:.8f} cert={ok}',flush=True)
    prev_x=None; prev_gL=None
    for it in range(MAXITER):
        c=d-D_TARGET; cg=m.separation_gradient(x)
        # PHR multiplier for g(x)=D_TARGET-d <= 0.
        mu=max(0.0,lam-rho*c)
        gL=g-mu*cg
        p=project_bounds(x,-gL/Hscale,lo,hi)
        # SQP tangent correction when buffered constraint is active/predicted active.
        if c<.004:
            cp=float(np.dot(cg,p)); required=-c
            if cp<required:
                cn=float(np.dot(cg,cg))
                if cn>1e-16: p += cg*((required-cp)/cn)
        pn=float(np.linalg.norm(p))
        if pn>trust: p*=trust/pn
        slope=float(np.dot(gL,p))
        if slope>=0:
            p=project_bounds(x,-gL,lo,hi); pn=np.linalg.norm(p)
            if pn>trust: p*=trust/pn
            slope=float(np.dot(gL,p))
        # merit = physical energy + inequality PHR term
        def merit(E,dist):
            cc=dist-D_TARGET; muv=max(0.0,lam-rho*cc)
            return E + (muv*muv-lam*lam)/(2*rho)
        phi=merit(e,d); alpha=1.0; took=False; wd=we=np.nan; ns=0
        for _ in range(16):
            trial=np.clip(x+alpha*p,lo,hi)
            feasible,wd,we,ns=m.path_cert(x,trial)
            if feasible:
                dt=m.cert(trial,full=False)[0]; et=m.energy(trial); phit=merit(et,dt)
                if phit <= phi + ARMIJO*alpha*slope:
                    gt=m.gradient(trial); d_full,lk_full,ok_full,vals_full=m.cert(trial,full=True)
                    # scalar BFGS curvature scaling for stable SQP steps
                    cnew=d_full-D_TARGET; mun=max(0.0,lam-rho*cnew); cgn=m.separation_gradient(trial)
                    gLn=gt-mun*cgn; s=trial-x; y=gLn-gL
                    sy=float(np.dot(s,y)); ss=float(np.dot(s,s))
                    if sy>1e-10 and ss>1e-14: Hscale=float(np.clip(sy/ss,.05,50.0))
                    prev_x=x; prev_gL=gL; x,e,g,d,lk,vals=trial,et,gt,d_full,lk_full,vals_full
                    lam=max(0.0,lam-rho*(d-D_TARGET)); accepted+=1; took=True
                    trust=min(TRUST_MAX,trust*1.25 if alpha>.5 else trust)
                    break
            alpha*=.5
            if alpha<MIN_STEP: break
        if not took:
            trust*=.5; rho=min(5000.0,rho*2.0)
        r=m.radius(x); c=d-D_TARGET; cg=m.separation_gradient(x); mu=max(0.0,lam-rho*c)
        gL=g-mu*cg; pstat=project_bounds(x,-gL,lo,hi)
        if c<.004:
            cp=np.dot(cg,pstat)
            if cp<0 and np.dot(cg,cg)>1e-16: pstat-=cg*cp/np.dot(cg,cg)
        rel=float(np.linalg.norm(pstat)/max(abs(e),1e-12))
        hist.append((it,e,r,d,lk,vals[0][0],vals[0][1],vals[1][0],vals[1][1],rel,lam,rho,trust,alpha,int(took),wd,we,ns))
        print(f'iter={it:02d} E={e:.9f} R={r:.6f} d={d:.6f} Lk512={lk:.7f} |PgL|/E={rel:.5f} lam={lam:.3g} rho={rho:.1f} tr={trust:.3g} a={alpha:.3g} ok={took}',flush=True)
        if rel<.05 and ok: break
        if trust<TRUST_MIN and not took: break
    d,lk,ok,vals=m.cert(x,full=True); r=m.radius(x)
    c=d-D_TARGET; cg=m.separation_gradient(x); mu=max(0.0,lam-rho*c); gL=g-mu*cg
    pstat=project_bounds(x,-gL,lo,hi)
    if c<.004 and np.dot(cg,pstat)<0 and np.dot(cg,cg)>1e-16: pstat-=cg*np.dot(cg,pstat)/np.dot(cg,cg)
    rel=float(np.linalg.norm(pstat)/max(abs(e),1e-12))
    b1=ok; b2=e<e0-1e-5; b3=all(row[3]>=D_HARD and abs(abs(row[4])-1)<=LK_TOL for row in hist); b4=rel<.05
    b5=max(abs(vals[i][1]-vals[i+1][1]) for i in range(2))<=.02 and max(abs(vals[i][0]-vals[i+1][0]) for i in range(2))<=.01
    finding='AUGLAG_CONSTRAINED_STATIONARY' if all((b1,b2,b3,b4,b5)) else ('AUGLAG_CERTIFIED_DESCENT_NOT_STATIONARY' if all((b1,b2,b3,b5)) else 'AUGLAG_METHOD_FAILED')
    np.savez(ROOT/'analysis'/'ELEC007_state.npz',x_start=x_start,x_final=x,energy_start=e0,energy_final=e,gradient_final=g,lagrangian_gradient_final=gL,projected_lagrangian_gradient_final=pstat,lambda_final=lam,rho_final=rho)
    with (ROOT/'analysis'/'ELEC007_history.csv').open('w',newline='') as f:
        w=csv.writer(f); w.writerow(['iteration','energy','R_rms','dmin512','Lk512','dmin128','Lk128','dmin256','Lk256','projected_L_gradient_over_E','lambda','rho','trust','alpha','accepted','path_worst_d','path_worst_lk_error','path_samples']); w.writerows(hist)
    print('\nELEC-007 augmented-Lagrangian constrained solver')
    print(f'start E={e0:.9f}; final E={e:.9f}; accepted={accepted}; evaluations={m.nfev}')
    print(f'final R={r:.6f}, dmin={d:.8f}, Lk128={vals[0][1]:.8f}, Lk256={vals[1][1]:.8f}, Lk512={vals[2][1]:.8f}')
    print(f'projected Lagrangian-gradient/E={rel:.7g}; lambda={lam:.6g}; rho={rho:.6g}')
    for name,b in [('B1 final 128/256/512 certificate',b1),('B2 physical energy decreases',b2),('B3 all accepted states remain certified',b3),('B4 constrained stationarity <0.05',b4),('B5 three-level certificate agreement',b5)]: print(name+': '+('PASS' if b else 'FAIL'))
    print('FINDING:',finding); print(f'elapsed={time.time()-t0:.1f}s')
    return locals()

if __name__=='__main__': test()
