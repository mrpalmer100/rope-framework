"""COMMISSION Z, BRICK 5: LEAD-Omega -- THE O(Omega) EXPANSION OF THE
COMMITTED CHAIN (coefficient derivation, alpha out of the room).

LEAD-Omega (Brick 4, displayed-and-refused): the chain's irreducible
residual equals Omega x 1.10 to 0.4 percent. Graduation condition: a
coefficient ~ -1.10 must be DERIVED from the construction's O(Omega)
structure. This brick computes the one O(Omega) response the committed
machinery owns end to end: the Omega-expansion of the dressing itself.

METHOD (fixed before running): solve the identical EL-BVP at perturbed
rotation rates Omega' = Omega (1 + eps), eps in {-0.02,-0.01,+0.01,+0.02},
HOLDING THE COMMITTED GEOMETRY FIXED (x* = e^{pi^2}, J_T -- the closure's
invariants; the norm target J_T/Omega' and E_rot = Omega' J_T / 2 follow).
Extract by central differences:
    c1 = d ln D_E / d ln Omega   (and curvature for quality control)
Also record lam(Omega')/Omega' (the two-rate structure).

CONFRONTATION (only after c1 is committed):
The residual requires delta(1/alpha)/(1/alpha) = -1.788e-4 = c * Omega
with c = -1.100 (the LEAD-Omega coefficient). The derived channel:
a physical rate shift of relative size s produces delta D/D = c1 * s.
  - CLASS A (the genuine O(Omega) class): s = k * Omega with k = O(1).
    Match requires c1 * k = -1.100: report the k each c1 implies.
  - CLASS B (the two-rate O(1) shifts, s = (lam-Omega)/Omega etc.):
    these are O(1); they are EXCLUDED unless c1 is itself ~5e-4 (they
    would otherwise move D at percent scale, contradicting the chain).
Registrable outcomes: c1 ~ -1.10 with k = 1 (clean graduation path);
c1 = O(1) but different (k = -1.100/c1 named, its provenance owed);
c1 tiny (the dressing is Omega-stationary: LEAD-Omega must live in a
DIFFERENT chain element -- V-A's landing formula -- named for merge).
"""
import numpy as np
from scipy.optimize import minimize
from scipy.integrate import solve_bvp
from scipy.interpolate import interp1d

PI=np.pi; XSTAR=float(np.exp(PI**2)); JT=PI**2*(XSTAR**2-1.0)/XSTAR
OMEGA0=PI/XSTAR; K=2.0

def make_grid(n,r_min,r_max):
    r=np.geomspace(r_min,r_max,n)
    w=np.zeros_like(r); w[1:-1]=(r[2:]-r[:-2])/2.0; w[0]=(r[1]-r[0])/2.0; w[-1]=(r[-1]-r[-2])/2.0
    return r,w*2.0*PI*r
def elastic_density(g2):
    e=np.sqrt(1.0+g2)-1.0; return e+0.5*K*e**2
def de_dg2(g2):
    E=np.sqrt(1.0+g2); return (1.0+K*(E-1.0))/(2.0*E)
def P_fun(g2):
    E=np.sqrt(1.0+g2); return K+(1.0-K)/E
def Pp_fun(g2):
    E=np.sqrt(1.0+g2); return (K-1.0)/(2.0*E**3)

def solve_D(OMEGA,r_min=1e-3,tol=1e-8,n_mesh=4000):
    NT=JT/OMEGA
    def lbfgs_guess(n_grid,lam_pen=1e4):
        r,w=make_grid(n_grid,r_min,XSTAR)
        def obj_grad(f):
            df=np.gradient(f,r); g2=df**2+(f/r)**2
            E=float(np.sum((elastic_density(g2)+0.5*OMEGA**2*f**2)*w))
            J=OMEGA*float(np.sum(f**2*w)); pen=lam_pen*(J/JT-1.0)**2
            dd=de_dg2(g2); g=(2.0*dd*f/r**2+OMEGA**2*f)*w
            flux=2.0*dd*df*2.0*PI*r; g-=np.gradient(flux,r)*(w/(2.0*PI*r))
            g+=lam_pen*2.0*(J/JT-1.0)/JT*(2.0*OMEGA*f*w); return E+pen,g
        f0=np.ones_like(r); f0*=np.sqrt(NT/float(np.sum(f0**2*w)))
        res=minimize(obj_grad,f0,jac=True,method="L-BFGS-B",bounds=[(0.0,None)]*len(r),options=dict(maxiter=20000,ftol=1e-14,gtol=1e-10))
        f=res.x*np.sqrt(NT/float(np.sum(res.x**2*w))); return r,f
    def rhs(r,y,p):
        lam=p[0]; f,fp,_=y; g2=fp**2+(f/r)**2; P=P_fun(g2); Pp=Pp_fun(g2)
        RHS=r*(P*f/r**2+(OMEGA**2-2.0*lam*OMEGA)*f)
        num=RHS-P*fp-r*Pp*fp*(2.0*f*fp/r**2-2.0*f**2/r**3)
        den=r*P+2.0*r*Pp*fp**2
        return np.vstack([fp,num/den,2.0*PI*r*f**2])
    def bcs(ya,yb,p):
        return np.array([ya[1],yb[1],ya[2],yb[2]-NT])
    r_g,f_g=lbfgs_guess(6400)
    r=np.geomspace(r_min,XSTAR,n_mesh)
    fi=interp1d(r_g,f_g,kind="cubic",fill_value="extrapolate")(r); fpi=np.gradient(fi,r)
    ni=np.concatenate([[0.0],np.cumsum(0.5*(2*PI*r[1:]*fi[1:]**2+2*PI*r[:-1]*fi[:-1]**2)*np.diff(r))])
    s=np.sqrt(NT/ni[-1]); fi,fpi,ni=fi*s,fpi*s,ni*s**2
    y0=np.vstack([fi,fpi,ni]); lam0=OMEGA*0.7
    sol=solve_bvp(rhs,bcs,r,y0,p=[lam0],tol=tol,max_nodes=400000,verbose=0)
    if not sol.success: return None
    rr=sol.x; f=sol.y[0]; fp=sol.y[1]; g2=fp**2+(f/rr)**2
    E_el=float(np.trapezoid(elastic_density(g2)*2*PI*rr,rr))
    LOG=float(np.trapezoid((f**2/(2*rr**2))*2*PI*rr,rr))
    E_rot=0.5*OMEGA*JT
    return (E_el-LOG+E_rot)/E_rot, float(sol.p[0])/OMEGA

print("== BRICK 5: Omega-expansion of D_E (committed geometry held fixed) ==")
eps_list=[-0.02,-0.01,0.0,+0.01,+0.02]
res={}
for eps in eps_list:
    out=solve_D(OMEGA0*(1+eps))
    if out is None:
        print(f"   eps={eps:+.2f}: FAILED"); continue
    D,lam_ratio=out; res[eps]=(D,lam_ratio)
    print(f"   eps={eps:+.2f}: D_E={D:.7f}   lam/Omega={lam_ratio:.6f}")
D0=res[0.0][0]
c1_a=(res[0.01][0]-res[-0.01][0])/(0.02)/D0
c1_b=(res[0.02][0]-res[-0.02][0])/(0.04)/D0
curv=(res[0.01][0]+res[-0.01][0]-2*D0)/(0.01**2)/D0
print(f"\n== COMMIT: c1 = d ln D_E / d ln Omega ==")
print(f"   central(1%) = {c1_a:.5f}   central(2%) = {c1_b:.5f}   curvature = {curv:.3f}")
print(f"   lam/Omega at committed point = {res[0.0][1]:.6f}  (Omega-dependence: "
      f"{(res[0.01][1]-res[-0.01][1])/0.02:+.4f} per unit ln Omega)\n")

print("== CONFRONTATION (LEAD-Omega coefficient enters now) ==")
c_req=-1.100
print(f"   required: c = {c_req:.3f}  (delta(1/alpha) = c * Omega)")
print(f"   CLASS A (s = k Omega): k = c_req/c1 = {c_req/c1_a:.4f}")
print(f"   CLASS B (s = (lam-Omega)/Omega = {res[0.0][1]-1:+.4f}, O(1)):")
print(f"      would give delta D/D = {c1_a*(res[0.0][1]-1):+.3e} "
      f"({c1_a*(res[0.0][1]-1)*1e6:+.0f} ppm) vs required -179 ppm")
