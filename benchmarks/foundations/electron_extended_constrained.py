"""ELEC-006: extended topology-preserving constrained variational solver.

Continues from ELEC-005's certified final K=8 state. Uses:
  * adaptive 128/256-point polygonal certification;
  * exact inter-component polygonal segment separation;
  * two-resolution Gauss-linking checks;
  * active-constraint tangent projection for the separation floor;
  * limited-memory BFGS directions in the feasible tangent cone;
  * topology-certified Armijo backtracking along every accepted path;
  * a longer deterministic convergence run.

The physical objective is unchanged from ELEC-002--005. Topology is not added
as an energy term: it is enforced as a feasibility condition on the line
search. Stationarity is assessed only with the feasible projected gradient.
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
CERT_LEVELS=(128,256); KAPPA=2.0; T0=1.0
FD=1e-4; FD_CON=2e-4; D_FLOOR=.06; D_ACTIVE=.012; LK_TOL=.03
MAXITER=4; MEMORY=6; ARMIJO=1e-4; MIN_STEP=2e-5


def segment_distance_min(A,B):
    P=A[:,None,:]; Q=np.roll(A,-1,axis=0)[:,None,:]
    R=B[None,:,:]; S=np.roll(B,-1,axis=0)[None,:,:]
    u=Q-P; v=S-R; w=P-R
    a=np.sum(u*u,axis=2); b=np.sum(u*v,axis=2); c=np.sum(v*v,axis=2)
    d=np.sum(u*w,axis=2); e=np.sum(v*w,axis=2)
    den=a*c-b*b
    sc=np.where(den>1e-14,(b*e-c*d)/den,0.0)
    tc=np.where(den>1e-14,(a*e-b*d)/den,np.where(c>1e-14,e/c,0.0))
    sc=np.clip(sc,0,1); tc=np.clip(tc,0,1)
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
        for M in (M_ENERGY,)+CERT_LEVELS:
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
    def cert_level(self,z,M):
        c1,c2=self.curves(z,M)
        return segment_distance_min(c1,c2),float(linking_number(c1,c2))
    def cert(self,z):
        vals=[self.cert_level(z,M) for M in CERT_LEVELS]
        d=min(v[0] for v in vals)
        lkerr=max(abs(abs(v[1])-1) for v in vals)
        agree=abs(vals[0][1]-vals[1][1]) <= .02 and abs(vals[0][0]-vals[1][0]) <= .01
        ok=d>=D_FLOOR and lkerr<=LK_TOL and agree
        return d,vals[-1][1],ok,vals
    def separation_gradient(self,z):
        g=np.empty_like(z)
        for i in range(len(z)):
            d=np.zeros_like(z); d[i]=FD_CON
            gp=self.cert_level(z+d,CERT_LEVELS[0])[0]
            gm=self.cert_level(z-d,CERT_LEVELS[0])[0]
            g[i]=(gp-gm)/(2*FD_CON)
        return g
    def path_cert(self,a,b):
        # Use the 128-point certificate along the path, then require the full
        # adaptive 128/256 certificate at the proposed endpoint. This is an
        # adaptive-refinement strategy: expensive refinement is concentrated
        # where a step may actually be accepted.
        delta=np.linalg.norm(b-a)
        ns=max(5,min(11,int(np.ceil(delta/.004))+1))
        wd=1e9; we=0.0
        for t in np.linspace(0,1,ns):
            z=(1-t)*a+t*b
            d,lk=self.cert_level(z,CERT_LEVELS[0])
            wd=min(wd,d); we=max(we,abs(abs(lk)-1))
            if d<D_FLOOR or abs(abs(lk)-1)>LK_TOL: return False,wd,we,ns
        d,lk,ok,vals=self.cert(b)
        wd=min(wd,d); we=max(we,max(abs(abs(v[1])-1) for v in vals))
        return ok,wd,we,ns
    def metrics(self,z):
        c1,c2=self.curves(z,CERT_LEVELS[-1]); p=np.vstack((c1,c2)); p-=p.mean(0)
        r=float(np.sqrt(np.mean(np.sum(p*p,axis=1))))
        d,lk,ok,vals=self.cert(z)
        return r,d,lk,ok,vals


def lbfgs_direction(g,S,Y):
    q=g.copy(); al=[]
    for s,y in zip(reversed(S),reversed(Y)):
        rho=1.0/max(np.dot(y,s),1e-14); a=rho*np.dot(s,q); al.append((a,rho)); q-=a*y
    if S:
        sy=np.dot(S[-1],Y[-1]); yy=np.dot(Y[-1],Y[-1]); q*=sy/max(yy,1e-14)
    for s,y,(a,rho) in zip(S,Y,reversed(al)):
        q+=s*(a-rho*np.dot(y,q))
    return -q


def project_feasible(x,p,g,blo,bhi,dmin,m):
    p=p.copy()
    p[(x<=blo+1e-9)&(p<0)]=0; p[(x>=bhi-1e-9)&(p>0)]=0
    cgrad=None
    if dmin-D_FLOOR < D_ACTIVE:
        cgrad=m.separation_gradient(x); cn=np.dot(cgrad,cgrad)
        # Tangent-cone projection: prevent first-order motion toward violation.
        cp=np.dot(cgrad,p)
        if cp < 0 and cn>1e-16: p-=cgrad*(cp/cn)
    # Guarantee descent; if quasi-Newton direction lost descent, use projected steepest descent.
    if np.dot(g,p)>=-1e-12:
        p=-g.copy(); p[(x<=blo+1e-9)&(p<0)]=0; p[(x>=bhi-1e-9)&(p>0)]=0
        if cgrad is not None:
            cn=np.dot(cgrad,cgrad); cp=np.dot(cgrad,p)
            if cp<0 and cn>1e-16: p-=cgrad*(cp/cn)
    return p,cgrad


def test():
    t0=time.time(); m=Model()
    prev_path=ROOT/'analysis'/'ELEC006_state.npz'
    if prev_path.exists():
        dat=np.load(prev_path); x=dat['x_final'].astype(float); campaign_e0=float(dat['campaign_energy_start']) if 'campaign_energy_start' in dat else float(dat['energy_start'])
    else:
        dat=np.load(ROOT/'analysis'/'ELEC005_state.npz'); x=dat['x_final'].astype(float); campaign_e0=float(dat['energy_final'])
    blo=np.r_[np.log(.35),np.full(len(x)-1,-.35)]; bhi=np.r_[np.log(1.8),np.full(len(x)-1,.35)]
    e=m.energy(x); e0=e; g=m.gradient(x); S=[]; Y=[]; hist=[]; accepted=0
    r,d,lk,ok,vals=m.metrics(x)
    print(f'start E={e:.9f} R={r:.6f} dmin={d:.6f} Lk256={lk:.8f} certified={ok}',flush=True)
    for it in range(MAXITER):
        p=lbfgs_direction(g,S,Y)
        p,cgrad=project_feasible(x,p,g,blo,bhi,d,m)
        pg=float(np.linalg.norm(p)); rel=pg/max(abs(e),1e-12)
        # A degenerate quasi-Newton direction is not evidence of stationarity;
        # verify with the active-projected steepest-descent residual.
        if rel<.03:
            pcheck,_=project_feasible(x,-g,g,blo,bhi,d,m)
            if np.linalg.norm(pcheck)/max(abs(e),1e-12)<.03: break
            p=pcheck; pg=float(np.linalg.norm(p)); rel=pg/max(abs(e),1e-12); S.clear(); Y.clear()
        # Normalize only if very large; preserve L-BFGS scale otherwise.
        if pg>.25: p*=.25/pg
        slope=float(np.dot(g,p))
        margin=max(d-D_FLOOR,0.0)
        alpha=min(1.0,max(.04,.35*margin/max(np.linalg.norm(p),1e-12)))
        took=False; wd=np.nan; we=np.nan; ns=0
        # First attempt the L-BFGS direction. If it cannot produce a certified
        # Armijo step, fall back deterministically to the active-projected
        # steepest-descent direction rather than terminating the campaign.
        for attempt in range(2):
            if attempt==1:
                p,_=project_feasible(x,-g,g,blo,bhi,d,m)
                pn=np.linalg.norm(p)
                if pn<1e-14: break
                p*=min(.25,pn)/pn
                slope=float(np.dot(g,p)); alpha=min(.04,max(.002,.2*max(d-D_FLOOR,0.0)/max(np.linalg.norm(p),1e-12)))
                S.clear(); Y.clear()
            for _ls in range(12):
                trial=np.clip(x+alpha*p,blo,bhi)
                feasible,wd,we,ns=m.path_cert(x,trial)
                if feasible:
                    en=m.energy(trial)
                    if en <= e+ARMIJO*alpha*slope:
                        gn=m.gradient(trial); s=trial-x; y=gn-g
                        if np.dot(s,y)>1e-9:
                            S.append(s); Y.append(y)
                            if len(S)>MEMORY: S.pop(0); Y.pop(0)
                        x,e,g=trial,en,gn; accepted+=1; took=True; break
                alpha*=.5
                if alpha<MIN_STEP: break
            if took: break
        r,d,lk,ok,vals=m.metrics(x)
        # Feasible projected gradient at the accepted point for stationarity reporting.
        pstat,_=project_feasible(x,-g,g,blo,bhi,d,m)
        pgn=float(np.linalg.norm(pstat)); relstat=pgn/max(abs(e),1e-12)
        hist.append((it,e,r,d,lk,vals[0][0],vals[0][1],pgn,relstat,alpha,int(took),wd,we,ns))
        print(f'iter={it:02d} E={e:.9f} R={r:.6f} d={d:.6f} Lk={lk:.7f} |Pg|/E={relstat:.5f} a={alpha:.3g} ok={took}',flush=True)
        if not took: break
    pfinal,_=project_feasible(x,-g,g,blo,bhi,d,m)
    rel=float(np.linalg.norm(pfinal)/max(abs(e),1e-12))
    r,d,lk,ok,vals=m.metrics(x)
    b1=ok
    b2=e<e0-1e-5
    b3=all(row[3]>=D_FLOOR and abs(abs(row[4])-1)<=LK_TOL for row in hist)
    b4=rel<.05
    b5=abs(vals[0][1]-vals[1][1])<=.02 and abs(vals[0][0]-vals[1][0])<=.01
    finding='CONSTRAINED_STATIONARY' if all((b1,b2,b3,b4,b5)) else ('EXTENDED_CERTIFIED_DESCENT_NOT_STATIONARY' if all((b1,b2,b3,b5)) else 'EXTENDED_CONSTRAINED_METHOD_FAILED')
    np.savez(ROOT/'analysis'/'ELEC006_state.npz',x_start=dat['x_final'],x_final=x,energy_start=e0,energy_final=e,campaign_energy_start=campaign_e0,gradient_final=g,projected_gradient_final=pfinal)
    with (ROOT/'analysis'/'ELEC006_history.csv').open('w',newline='') as f:
        w=csv.writer(f); w.writerow(['iteration','energy','R_rms','dmin_adaptive','Lk256','dmin128','Lk128','projected_gradient_norm','projected_gradient_over_E','alpha','accepted','path_worst_d','path_worst_lk_error','path_samples']); w.writerows(hist)
    print('\nELEC-006 extended constrained solver')
    print(f'start E={e0:.9f}; final E={e:.9f}; accepted={accepted}; evaluations={m.nfev}')
    print(f'final R={r:.6f}, dmin={d:.8f}, Lk128={vals[0][1]:.8f}, Lk256={vals[1][1]:.8f}')
    print(f'feasible projected-gradient/E={rel:.7g}')
    for name,b in [('B1 final adaptive certificate',b1),('B2 physical energy decreases',b2),('B3 all accepted states remain certified',b3),('B4 feasible projected stationarity <0.05',b4),('B5 128/256 certificate agreement',b5)]: print(name+': '+('PASS' if b else 'FAIL'))
    print('FINDING:',finding); print(f'elapsed={time.time()-t0:.1f}s')
    return locals()

if __name__=='__main__': test()
