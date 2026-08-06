import numpy as np
from scipy.optimize import minimize
from scipy.integrate import solve_bvp
from scipy.interpolate import interp1d
PI = np.pi
XSTAR = float(np.exp(PI**2))
JT = PI**2 * (XSTAR**2 - 1.0) / XSTAR
OMEGA = PI / XSTAR
NORM_TARGET = JT / OMEGA
K_LOW = 2.0
def make_grid(n, r_min, r_max):
    r = np.geomspace(r_min, r_max, n)
    w = np.zeros_like(r); w[1:-1]=(r[2:]-r[:-2])/2.0; w[0]=(r[1]-r[0])/2.0; w[-1]=(r[-1]-r[-2])/2.0
    return r, w*2.0*PI*r
def elastic_density(g2,k):
    eps=np.sqrt(1.0+g2)-1.0; return eps+0.5*k*eps**2
def de_dg2(g2,k):
    E=np.sqrt(1.0+g2); return (1.0+k*(E-1.0))/(2.0*E)
def lbfgs_guess(k,n_grid,r_min,lam_pen=1e4):
    r,w=make_grid(n_grid,r_min,XSTAR)
    def obj_grad(f):
        df=np.gradient(f,r); g2=df**2+(f/r)**2
        E=float(np.sum((elastic_density(g2,k)+0.5*OMEGA**2*f**2)*w))
        J=OMEGA*float(np.sum(f**2*w)); pen=lam_pen*(J/JT-1.0)**2
        dd=de_dg2(g2,k); g=(2.0*dd*f/r**2+OMEGA**2*f)*w
        flux=2.0*dd*df*2.0*PI*r; g-=np.gradient(flux,r)*(w/(2.0*PI*r))
        g+=lam_pen*2.0*(J/JT-1.0)/JT*(2.0*OMEGA*f*w); return E+pen,g
    f0=np.ones_like(r); f0*=np.sqrt(NORM_TARGET/float(np.sum(f0**2*w)))
    res=minimize(obj_grad,f0,jac=True,method="L-BFGS-B",bounds=[(0.0,None)]*len(r),options=dict(maxiter=20000,ftol=1e-14,gtol=1e-10))
    f=res.x*np.sqrt(NORM_TARGET/float(np.sum(res.x**2*w))); return r,f
def P_fun(g2,k):
    E=np.sqrt(1.0+g2); return k+(1.0-k)/E
def Pp_fun(g2,k):
    E=np.sqrt(1.0+g2); return (k-1.0)/(2.0*E**3)
def rhs(r,y,p,k):
    lam=p[0]; f,fp,_=y; g2=fp**2+(f/r)**2; P=P_fun(g2,k); Pp=Pp_fun(g2,k)
    RHS=r*(P*f/r**2+(OMEGA**2-2.0*lam*OMEGA)*f)
    num=RHS-P*fp-r*Pp*fp*(2.0*f*fp/r**2-2.0*f**2/r**3)
    den=r*P+2.0*r*Pp*fp**2; fpp=num/den
    return np.vstack([fp,fpp,2.0*PI*r*f**2])
def bcs(ya,yb,p):
    return np.array([ya[1],yb[1],ya[2],yb[2]-NORM_TARGET])
def solve_el(k,r_min,tol,n_mesh=4000,verbose=False):
    r_g,f_g=lbfgs_guess(k,6400,r_min); r=np.geomspace(r_min,XSTAR,n_mesh)
    fi=interp1d(r_g,f_g,kind="cubic",fill_value="extrapolate")(r); fpi=np.gradient(fi,r)
    ni=np.concatenate([[0.0],np.cumsum(0.5*(2*PI*r[1:]*fi[1:]**2+2*PI*r[:-1]*fi[:-1]**2)*np.diff(r))])
    s=np.sqrt(NORM_TARGET/ni[-1]); fi,fpi,ni=fi*s,fpi*s,ni*s**2
    y0=np.vstack([fi,fpi,ni]); lam0=OMEGA*0.7
    sol=solve_bvp(lambda r_,y_,p_:rhs(r_,y_,p_,k),bcs,r,y0,p=[lam0],tol=tol,max_nodes=400000,verbose=0)
    if not sol.success: return None
    rr=sol.x; f=sol.y[0]; fp=sol.y[1]; g2=fp**2+(f/rr)**2
    E_el=float(np.trapezoid(elastic_density(g2,k)*2.0*PI*rr,rr))
    LOG=float(np.trapezoid((f**2/(2.0*rr**2))*2.0*PI*rr,rr))
    E_rot=0.5*OMEGA*JT; D_int=(E_el-LOG+E_rot)/E_rot
    return dict(D=D_int,E_el=E_el,LOG=LOG,lam=float(sol.p[0]),nodes=len(rr))
def main():
    print("== PHASE 1c: EL-BVP, low branch k/T0=2 ==")
    print(f"   x*={XSTAR:.1f} omega={OMEGA:.4e} Jt={JT:.6e} E_rot={0.5*OMEGA*JT:.5f}\n")
    runs=[]
    for r_min,tol in [(1e-3,1e-6),(1e-3,1e-8),(1e-3,1e-10),(1e-4,1e-8),(3e-4,1e-8)]:
        out=solve_el(K_LOW,r_min,tol)
        if out is None:
            print(f"  r_min={r_min:.0e} tol={tol:.0e}: BVP FAILED"); continue
        runs.append(out["D"])
        print(f"  r_min={r_min:.0e} tol={tol:.0e}: D_int={out['D']:.7f} (lam={out['lam']:.4e}, nodes={out['nodes']}, E_el={out['E_el']:.5f}, LOG={out['LOG']:.5f})")
    if len(runs)<3: print("\n  INSUFFICIENT runs -- no commit"); return
    D=float(np.median(runs)); spread=(max(runs)-min(runs))/D*100
    print(f"\n  median D_int={D:.7f}  spread={spread:.4f}% -> GATE {'PASS' if spread<0.1 else 'FAIL'}")
    if spread>=0.1: return
    print(f"\n== COMMIT D_int[k/T0=2]={D:.7f} ==\n== MENU ==")
    for m,v in {"1.40681 (LEAD-2)":1.40681,"pi^2/7":PI**2/7,"45/32":45/32,"sqrt(2)":np.sqrt(2)}.items():
        print(f"  vs {m:<20}={v:.6f}: {(D/v-1.0)*100:+8.4f}%")
main()
