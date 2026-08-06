"""COMMISSION Z, BRICK 3: THE k/T0 BRANCH CHECK (W5/U4 adjudication).

FND-021's dispute: k/T0 = 2 (EM-RECON-009, chemical/nuclear spacings) vs
k/T0 >= 1.9e8 (QB-008 Bell timing). W's committed D_E = 1.1051029 ran the
LOW branch only. This brick runs the HIGH branch (k/T0 = 1.9e8) through
the IDENTICAL phase1c machinery and gate (5 configs, spread < 0.1%),
commits blind, then confronts.

Physics note (stated before running): at the high branch the quadratic
elastic term 0.5 k eps^2 is ACTIVE at the solution's strain scale
(k g^2 / 4 ~ O(1) for g^2 ~ 1e-8), so the profile and D_E genuinely
differ -- this is a real, independent computation, not a rescaling.

Geometry held fixed: the committed closure x* = e^{pi^2}, J_T, Omega (T's
anchor). CAVEAT registered: the full high-branch fixed point could shift
x*; if the result is a near-miss, that coupling is the named follow-up.

CONFRONTATION MENU (consulted only after the blind commit):
  - low-branch committed value 1.1051029 (does the branch matter at all?)
  - the closure-required D_req = (1/alpha_measured)/(4 pi^3)
Adjudication logic per W5: a branch landing on D_req within numerics
adjudicates FND-021 in its favor and closes alpha; both-miss registers
the branch spread as a bound.
"""
import numpy as np
from scipy.optimize import minimize
from scipy.integrate import solve_bvp
from scipy.interpolate import interp1d

PI=np.pi; XSTAR=float(np.exp(PI**2)); JT=PI**2*(XSTAR**2-1.0)/XSTAR
OMEGA=PI/XSTAR; NORM_TARGET=JT/OMEGA
K_HIGH=1.9e8

def make_grid(n,r_min,r_max):
    r=np.geomspace(r_min,r_max,n)
    w=np.zeros_like(r); w[1:-1]=(r[2:]-r[:-2])/2.0; w[0]=(r[1]-r[0])/2.0; w[-1]=(r[-1]-r[-2])/2.0
    return r,w*2.0*PI*r
def elastic_density(g2,k):
    e=np.sqrt(1.0+g2)-1.0; return e+0.5*k*e**2
def de_dg2(g2,k):
    E=np.sqrt(1.0+g2); return (1.0+k*(E-1.0))/(2.0*E)
def lbfgs_guess(k,n_grid,r_min,lam_pen=1e4,iters=40000):
    r,w=make_grid(n_grid,r_min,XSTAR)
    def obj_grad(f):
        df=np.gradient(f,r); g2=df**2+(f/r)**2
        E=float(np.sum((elastic_density(g2,k)+0.5*OMEGA**2*f**2)*w))
        J=OMEGA*float(np.sum(f**2*w)); pen=lam_pen*(J/JT-1.0)**2
        dd=de_dg2(g2,k); g=(2.0*dd*f/r**2+OMEGA**2*f)*w
        flux=2.0*dd*df*2.0*PI*r; g-=np.gradient(flux,r)*(w/(2.0*PI*r))
        g+=lam_pen*2.0*(J/JT-1.0)/JT*(2.0*OMEGA*f*w); return E+pen,g
    f0=np.ones_like(r); f0*=np.sqrt(NORM_TARGET/float(np.sum(f0**2*w)))
    res=minimize(obj_grad,f0,jac=True,method="L-BFGS-B",bounds=[(0.0,None)]*len(r),
                 options=dict(maxiter=iters,ftol=1e-15,gtol=1e-12))
    f=res.x*np.sqrt(NORM_TARGET/float(np.sum(res.x**2*w))); return r,f
def P_fun(g2,k):
    E=np.sqrt(1.0+g2); return k+(1.0-k)/E
def Pp_fun(g2,k):
    E=np.sqrt(1.0+g2); return (k-1.0)/(2.0*E**3)
def rhs(r,y,p,k):
    lam=p[0]; f,fp,_=y; g2=fp**2+(f/r)**2; P=P_fun(g2,k); Pp=Pp_fun(g2,k)
    RHS=r*(P*f/r**2+(OMEGA**2-2.0*lam*OMEGA)*f)
    num=RHS-P*fp-r*Pp*fp*(2.0*f*fp/r**2-2.0*f**2/r**3)
    den=r*P+2.0*r*Pp*fp**2
    return np.vstack([fp,num/den,2.0*PI*r*f**2])
def bcs(ya,yb,p):
    return np.array([ya[1],yb[1],ya[2],yb[2]-NORM_TARGET])
def solve_el(k,r_min,tol,n_mesh=4000):
    r_g,f_g=lbfgs_guess(k,6400,r_min)
    r=np.geomspace(r_min,XSTAR,n_mesh)
    fi=interp1d(r_g,f_g,kind="cubic",fill_value="extrapolate")(r); fpi=np.gradient(fi,r)
    ni=np.concatenate([[0.0],np.cumsum(0.5*(2*PI*r[1:]*fi[1:]**2+2*PI*r[:-1]*fi[:-1]**2)*np.diff(r))])
    s=np.sqrt(NORM_TARGET/ni[-1]); fi,fpi,ni=fi*s,fpi*s,ni*s**2
    y0=np.vstack([fi,fpi,ni]); lam0=OMEGA*0.7
    sol=solve_bvp(lambda r_,y_,p_:rhs(r_,y_,p_,k),bcs,r,y0,p=[lam0],tol=tol,max_nodes=400000,verbose=0)
    if not sol.success: return None
    rr=sol.x; f=sol.y[0]; fp=sol.y[1]; g2=fp**2+(f/rr)**2
    E_el=float(np.trapezoid(elastic_density(g2,k)*2.0*PI*rr,rr))
    LOG=float(np.trapezoid((f**2/(2.0*rr**2))*2.0*PI*rr,rr))
    E_rot=0.5*OMEGA*JT; D=(E_el-LOG+E_rot)/E_rot
    g2max=float(np.max(g2)); keps=float(np.max(k*(np.sqrt(1+g2)-1)))
    return dict(D=D,E_el=E_el,LOG=LOG,lam=float(sol.p[0]),nodes=len(rr),g2max=g2max,keps=keps)

print("== BRICK 3: HIGH BRANCH k/T0 = 1.9e8, identical machinery and gate ==")
print(f"   x*={XSTAR:.1f} omega={OMEGA:.4e} Jt={JT:.6e} E_rot={0.5*OMEGA*JT:.5f}\n")
runs=[]
for r_min,tol in [(1e-3,1e-6),(1e-3,1e-8),(1e-3,1e-10),(1e-4,1e-8),(3e-4,1e-8)]:
    out=solve_el(K_HIGH,r_min,tol)
    if out is None:
        print(f"  r_min={r_min:.0e} tol={tol:.0e}: BVP FAILED"); continue
    runs.append(out["D"])
    print(f"  r_min={r_min:.0e} tol={tol:.0e}: D_int={out['D']:.7f} (lam={out['lam']:.4e}, nodes={out['nodes']}, E_el={out['E_el']:.5f}, LOG={out['LOG']:.5f}, max k*eps={out['keps']:.3f})")
if len(runs)<3:
    print("\n  INSUFFICIENT runs -- no commit"); raise SystemExit
D=float(np.median(runs)); spread=(max(runs)-min(runs))/D*100
print(f"\n  median D_int[HIGH]={D:.7f}  spread={spread:.4f}% -> GATE {'PASS' if spread<0.1 else 'FAIL'}")
if spread>=0.1: raise SystemExit
print(f"\n== COMMIT D_int[k/T0=1.9e8] = {D:.7f} ==\n")
print("== CONFRONTATION (menu consulted now, first time) ==")
D_LOW=1.1051029
ALPHA_INV=137.035999084
D_REQ=ALPHA_INV/(4*PI**3)
print(f"   low branch (committed) = {D_LOW:.7f}   high/low - 1 = {(D/D_LOW-1)*1e6:+.1f} ppm")
print(f"   closure-required D_req = {D_REQ:.7f}")
for lbl,val in (("LOW ",D_LOW),("HIGH",D)):
    print(f"   {lbl}: 1/alpha = 4 pi^3 D = {4*PI**3*val:.6f}  ({(4*PI**3*val/ALPHA_INV-1)*1e6:+8.1f} ppm)")
