"""COMMISSION Y, BRICK 2: the spatial f4 angular harmonic (reviewer's route).

CONSTRUCTION (pre-registered before any number is compared):
2D ansatz f(r,theta) = f0(r) + a4(r) cos 4theta. The rectified tether load
carries the exact angular structure
    (|cos th|+|sin th|) = (4/pi) [1 - (2/15) cos 4th + (2/63) cos 8th - ...]
so the tether (elastic) sector of the energy is modulated:
    E = int r dr dth/(2pi) [1 + m(th)] e(g^2)  +  rotational sector,
    m(th) = -(2/15) cos 4th          (leading harmonic; m=2 term audited)
with g^2 = (d_r f)^2 + (d_th f)^2 / r^2 + f^2/r^2 and the rotational sector
isotropic: (1/2)(Omega^2 - 2 lam Omega) f^2 per the committed EL structure
(lam from the committed solution; the norm constraint is second order in a4
and drops at this order).

Expansion to O(a4^2), angular averages <cos^2 4th> = <sin^2 4th> = 1/2,
<m cos 4th> = -1/15:

E[a4] - E0 =
  int 2 pi r dr {  -(1/15) * ep0 * 2 (f0' a4' + f0 a4 / r^2)          [linear]
    + (1/2)[ ep0 (a4'^2 + 16 a4^2/r^2 + a4^2/r^2)
             + 2 epp0 (f0' a4' + f0 a4/r^2)^2 ]                       [quad el]
    + (1/2)(Omega^2 - 2 lam Omega) a4^2 * (1/2) * 2                   [quad rot]
  }
where ep0 = de/dg2 (g0^2), epp0 = d2e/d(g2)^2 (g0^2), and the rotational
quadratic term is (1/2)(Om^2-2 lam Om) <(a4 cos4th)^2>*2pi r integrated,
i.e. coefficient (1/2)(Om^2-2 lam Om)*(1/2) per unit 2 pi r dr... implemented
directly as quadratic forms below; the linear solve minimizes E[a4].

PRE-REGISTERED MEASURE (the reviewer's eps_eff, three audited weights):
    eps_4[W] = int W(r) f0 a4 r dr / int W(r) f0^2 r dr
  W1 = |Omega^2 - 2 lam Omega|      (rotational/canonical weight)
  W2 = 1                            (plain norm)
  W3 = ep0 * (f0'^2 + f0^2/r^2)/f0^2-structure -> load weight: the linear
       tether-load pairing, eps_4 = int ep0 (f0' a4' + f0 a4/r^2) r dr /
                                    int ep0 (f0'^2 + f0^2/r^2) r dr
Closure test after all eps values printed:
    1/alpha = 4 pi^3 D_E (1 - eps_4/15) vs 137.035999084.
Higher harmonic audit: repeat with m(th) = +(2/63) cos 8th (a8 mode).
"""
import numpy as np
from scipy.optimize import minimize
from scipy.integrate import solve_bvp
from scipy.interpolate import interp1d

PI=np.pi; XSTAR=float(np.exp(PI**2)); JT=PI**2*(XSTAR**2-1.0)/XSTAR
OMEGA=PI/XSTAR; NORM_TARGET=JT/OMEGA; K=2.0

def make_grid(n,r_min,r_max):
    r=np.geomspace(r_min,r_max,n)
    w=np.zeros_like(r); w[1:-1]=(r[2:]-r[:-2])/2.0; w[0]=(r[1]-r[0])/2.0; w[-1]=(r[-1]-r[-2])/2.0
    return r,w*2.0*PI*r
def elastic_density(g2):
    eps=np.sqrt(1.0+g2)-1.0; return eps+0.5*K*eps**2
def de_dg2(g2):
    E=np.sqrt(1.0+g2); return (1.0+K*(E-1.0))/(2.0*E)
def d2e_dg2sq(g2):
    E=np.sqrt(1.0+g2)
    # d/dg2 [ (1+K(E-1))/(2E) ],  dE/dg2 = 1/(2E)
    return (K/(2*E)*(2*E) - (1.0+K*(E-1.0)))/(4.0*E**3)  # = (KE - (1+K(E-1)))/(4E^3)
def lbfgs_guess(n_grid,r_min,lam_pen=1e4):
    r,w=make_grid(n_grid,r_min,XSTAR)
    def obj_grad(f):
        df=np.gradient(f,r); g2=df**2+(f/r)**2
        E=float(np.sum((elastic_density(g2)+0.5*OMEGA**2*f**2)*w))
        J=OMEGA*float(np.sum(f**2*w)); pen=lam_pen*(J/JT-1.0)**2
        dd=de_dg2(g2); g=(2.0*dd*f/r**2+OMEGA**2*f)*w
        flux=2.0*dd*df*2.0*PI*r; g-=np.gradient(flux,r)*(w/(2.0*PI*r))
        g+=lam_pen*2.0*(J/JT-1.0)/JT*(2.0*OMEGA*f*w); return E+pen,g
    f0=np.ones_like(r); f0*=np.sqrt(NORM_TARGET/float(np.sum(f0**2*w)))
    res=minimize(obj_grad,f0,jac=True,method="L-BFGS-B",bounds=[(0.0,None)]*len(r),options=dict(maxiter=20000,ftol=1e-14,gtol=1e-10))
    f=res.x*np.sqrt(NORM_TARGET/float(np.sum(res.x**2*w))); return r,f
def P_fun(g2):
    E=np.sqrt(1.0+g2); return K+(1.0-K)/E
def Pp_fun(g2):
    E=np.sqrt(1.0+g2); return (K-1.0)/(2.0*E**3)
def rhs(r,y,p):
    lam=p[0]; f,fp,_=y; g2=fp**2+(f/r)**2; P=P_fun(g2); Pp=Pp_fun(g2)
    RHS=r*(P*f/r**2+(OMEGA**2-2.0*lam*OMEGA)*f)
    num=RHS-P*fp-r*Pp*fp*(2.0*f*fp/r**2-2.0*f**2/r**3)
    den=r*P+2.0*r*Pp*fp**2
    return np.vstack([fp,num/den,2.0*PI*r*f**2])
def bcs(ya,yb,p):
    return np.array([ya[1],yb[1],ya[2],yb[2]-NORM_TARGET])
def solve_el(r_min,tol,n_mesh=4000):
    r_g,f_g=lbfgs_guess(6400,r_min); r=np.geomspace(r_min,XSTAR,n_mesh)
    fi=interp1d(r_g,f_g,kind="cubic",fill_value="extrapolate")(r); fpi=np.gradient(fi,r)
    ni=np.concatenate([[0.0],np.cumsum(0.5*(2*PI*r[1:]*fi[1:]**2+2*PI*r[:-1]*fi[:-1]**2)*np.diff(r))])
    s=np.sqrt(NORM_TARGET/ni[-1]); fi,fpi,ni=fi*s,fpi*s,ni*s**2
    y0=np.vstack([fi,fpi,ni]); lam0=OMEGA*0.7
    return solve_bvp(lambda r_,y_,p_:rhs(r_,y_,p_),bcs,r,y0,p=[lam0],tol=tol,max_nodes=400000,verbose=0)

print("== BRICK 2: spatial f4 anisotropy (reviewer's construction) ==")
sol=solve_el(1e-3,1e-8); assert sol.success
rr=sol.x; f0=sol.y[0]; lam=float(sol.p[0])
g2=(sol.y[1])**2+(f0/rr)**2
E_el=float(np.trapezoid(elastic_density(g2)*2*PI*rr,rr))
LOG=float(np.trapezoid((f0**2/(2*rr**2))*2*PI*rr,rr))
E_rot=0.5*OMEGA*JT; D_E=(E_el-LOG+E_rot)/E_rot
print(f"   D_E check = {D_E:.7f}\n")

def solve_mode(N, M, hM):
    """Minimize the O(a^2) energy for angular mode cos(M theta) with elastic
    modulation m(th) = hM cos(M theta) (so <m cosM> = hM/2). Returns mesh,
    f0 interp, a(r)."""
    rm=np.geomspace(rr[0],rr[-1],N)
    f0m=interp1d(rr,f0,kind="cubic")(rm)
    f0p=np.gradient(f0m,rm)
    g2m=f0p**2+(f0m/rm)**2
    ep0=de_dg2(g2m); epp0=d2e_dg2sq(g2m)
    dr=np.gradient(rm)
    w=2*PI*rm*dr                       # radial integration weight
    # Build quadratic form  E[a] = -b.a + (1/2) a.A.a  on mesh values a_i,
    # derivatives via numerical differentiation matrix (2nd-order central).
    N_=len(rm)
    Dm=np.zeros((N_,N_))
    for i in range(1,N_-1):
        h1=rm[i]-rm[i-1]; h2=rm[i+1]-rm[i]
        Dm[i,i-1]=-h2/(h1*(h1+h2)); Dm[i,i]=(h2-h1)/(h1*h2); Dm[i,i+1]=h1/(h2*(h1+h2))
    Dm[0,0]=-1/(rm[1]-rm[0]); Dm[0,1]=1/(rm[1]-rm[0])
    Dm[-1,-2]=-1/(rm[-1]-rm[-2]); Dm[-1,-1]=1/(rm[-1]-rm[-2])
    # linear term: <m cosM>=hM/2 multiplies elastic first variation
    #   dE_lin/da(r) = 2*(hM/2)*[ep0*(f0' a' + f0 a/r^2)] integrated
    # b vector: b = -dE_lin/da  ->  E_lin = (hM) * int w ep0 (f0' a' + f0 a /r^2)
    b_vec = -( hM*( Dm.T@(w*ep0*f0p) + w*ep0*f0m/rm**2 ) )
    # quadratic terms:
    # (1/2)<cos^2>=1/4 ... assembled explicitly:
    # E_quad = int w { (1/2)[ ep0 (a'^2*(1/2)*2? ) ] } -- do it cleanly:
    # <(a' cosM)^2> = a'^2/2 ; <(M a sinM /r)^2> = M^2 a^2/(2 r^2);
    # <(a cosM)^2>/r^2 = a^2/(2 r^2)
    # elastic 2nd order: int w [ ep0*( a'^2 + M^2 a^2/r^2 + a^2/r^2 )/2
    #                    + epp0*2*(f0' a' + f0 a/r^2)^2 * (1/2) ]
    # rotational 2nd order: int w (1/2)(Om^2-2 lam Om) a^2 /2 *2 = int w (Om^2-2lamOm) a^2/2... 
    # rotational energy density in E0 is (1/2)(Om^2-2lamOm) f^2 (per EL); with
    # f -> f0 + a cosM: quadratic piece (1/2)(Om^2-2lamOm)<a^2 cos^2> = (Om^2-2lamOm) a^2/4
    c_rot=(OMEGA**2-2.0*lam*OMEGA)
    A = ( Dm.T@np.diag(w*ep0*0.5)@Dm
          + np.diag(w*ep0*(M*M+1.0)/(2.0*rm**2))
          + (Dm.T@np.diag(w*epp0*(f0p**2))@Dm)*1.0
          + np.diag(w*epp0*(f0m/rm**2)**2)
          + Dm.T@np.diag(w*epp0*f0p*f0m/rm**2) + np.diag(w*epp0*f0p*f0m/rm**2)@Dm
          + np.diag(w*c_rot*0.25*2.0) )
    # note: epp0 cross terms assembled from 2*epp0*(f0'a' + f0 a/r^2)^2*(1/2)
    #     = epp0[ f0'^2 a'^2 + 2 f0' f0 a' a /r^2 + f0^2 a^2/r^4 ]
    a=np.linalg.solve(A+A.T-np.diag(A.diagonal()), b_vec) if False else np.linalg.solve(0.5*(A+A.T), b_vec)
    return rm,f0m,f0p,ep0,a,w,dr

ALPHA_INV=137.035999084
for N in (2000,3500):
    rm,f0m,f0p,ep0,a4,w,dr=solve_mode(N,4,-2.0/15.0)
    # eps_4 under the three pre-registered weights
    W1=np.abs(OMEGA**2-2.0*lam*OMEGA)*np.ones_like(rm)
    e1=float(np.sum(W1*f0m*a4*rm*dr)/np.sum(W1*f0m**2*rm*dr))
    e2=float(np.sum(f0m*a4*rm*dr)/np.sum(f0m**2*rm*dr))
    a4p=np.gradient(a4,rm)
    e3=float(np.sum(ep0*(f0p*a4p+f0m*a4/rm**2)*rm*dr)/np.sum(ep0*(f0p**2+f0m**2/rm**2)*rm*dr))
    print(f"   N={N}: eps_4[W1 rot] = {e1:+.6f}   eps_4[W2 plain] = {e2:+.6f}   eps_4[W3 load] = {e3:+.6f}")
    print(f"          amplitude ratio max|a4|/max f0 = {np.max(np.abs(a4))/np.max(f0m):.5f}")
print(f"\n   [comparison] reviewer's target eps_4 = 0.002682")
print(f"\n== CLOSURE: 1/alpha = 4 pi^3 D_E (1 - eps_4/15) ==")
base=4*PI**3*D_E
print(f"   base = {base:.6f}  ({(base/ALPHA_INV-1)*1e6:+.1f} ppm)")
for lbl,e in (("W1",e1),("W2",e2),("W3",e3)):
    v=base*(1-e/15.0)
    print(f"   {lbl}: eps_4={e:+.6f} -> 1/alpha = {v:.6f}  ({(v/ALPHA_INV-1)*1e6:+7.1f} ppm)")
# m=8 audit
rm,f0m,f0p,ep0,a8,w,dr=solve_mode(2000,8,+2.0/63.0)
e3_8=float(np.sum(ep0*(f0p*np.gradient(a8,rm)+f0m*a8/rm**2)*rm*dr)/np.sum(ep0*(f0p**2+f0m**2/rm**2)*rm*dr))
print(f"\n   m=8 harmonic audit: eps_8[W3] = {e3_8:+.6f}  (correction coeff -1/63 vs -1/15)")
v=base*(1-e3/15.0-e3_8/63.0)
print(f"   combined W3 (m=4 + m=8): 1/alpha = {v:.6f}  ({(v/ALPHA_INV-1)*1e6:+7.1f} ppm)")
