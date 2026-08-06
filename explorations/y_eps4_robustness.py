"""COMMISSION Y, Part 3 robustness pass.

The physically standard second-order correction to a cycle-averaged coupling
under a harmonic modulation (1 + h cos 4m chi) of the elastic sector is
    Delta = (1/2) sum_m h_m^2 chi_m,
    h_m = 2 (-1)^{m+1} / (16 m^2 - 1)   (exact Fourier coefficients of the
                                          rectified response),
    chi_m = <f4m_unit, w f0> / <f0, w f0>   (unit-drive susceptibility).
Correction: 1/alpha = 4 pi^3 D_E (1 - Delta).

Freedom audited here (reported, not chosen post hoc):
  P1  pairing weight w = 2 pi r |Omega^2 - 2 lam Omega|   (rotational sector)
  P2  pairing weight w = 2 pi r                            (plain f0 norm)
  P3  energy pairing: Delta_E = -(1/2) h^2 <f4, s_unit>/E_ref with
      E_ref = E_el - LOG (the dressing excess) and s_unit the unit source
Mesh: N in {2000, 3000, 4500}; r_min from the committed run.
Harmonics m = 1..6 (coefficients fall as 1/m^2, chi_m quasi-static).
"""
import numpy as np
from scipy.optimize import minimize
from scipy.integrate import solve_bvp
from scipy.interpolate import interp1d

PI=np.pi; XSTAR=float(np.exp(PI**2)); JT=PI**2*(XSTAR**2-1.0)/XSTAR
OMEGA=PI/XSTAR; NORM_TARGET=JT/OMEGA; K_LOW=2.0
exec(open("explorations/w_dressing_phase1c.py").read().split("def main()")[0].split("import numpy")[1].replace("from scipy","#from scipy",0) if False else "")

# re-import solver machinery from the Y script namespace
import importlib.util
spec = importlib.util.spec_from_file_location("ycore","explorations/y_action_vs_energy_core.py")

# simpler: duplicate the needed functions
def make_grid(n,r_min,r_max):
    r=np.geomspace(r_min,r_max,n)
    w=np.zeros_like(r); w[1:-1]=(r[2:]-r[:-2])/2.0; w[0]=(r[1]-r[0])/2.0; w[-1]=(r[-1]-r[-2])/2.0
    return r,w*2.0*PI*r
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
    den=r*P+2.0*r*Pp*fp**2
    return np.vstack([fp,num/den,2.0*PI*r*f**2])
def bcs(ya,yb,p):
    return np.array([ya[1],yb[1],ya[2],yb[2]-NORM_TARGET])
def solve_el(k,r_min,tol,n_mesh=4000):
    r_g,f_g=lbfgs_guess(k,6400,r_min); r=np.geomspace(r_min,XSTAR,n_mesh)
    fi=interp1d(r_g,f_g,kind="cubic",fill_value="extrapolate")(r); fpi=np.gradient(fi,r)
    ni=np.concatenate([[0.0],np.cumsum(0.5*(2*PI*r[1:]*fi[1:]**2+2*PI*r[:-1]*fi[:-1]**2)*np.diff(r))])
    s=np.sqrt(NORM_TARGET/ni[-1]); fi,fpi,ni=fi*s,fpi*s,ni*s**2
    y0=np.vstack([fi,fpi,ni]); lam0=OMEGA*0.7
    return solve_bvp(lambda r_,y_,p_:rhs(r_,y_,p_,k),bcs,r,y0,p=[lam0],tol=tol,max_nodes=400000,verbose=0)

def residual(fv,r,lam):
    fpv=np.gradient(fv,r); g2v=fpv**2+(fv/r)**2; dd=de_dg2(g2v,K_LOW)
    flux=2.0*dd*fpv*2*PI*r
    Rv=-np.gradient(flux,r)+2*PI*r*(2.0*dd*fv/r**2+(OMEGA**2-2.0*lam*OMEGA)*fv)
    Rv[0]=fpv[0]; Rv[-1]=fpv[-1]
    return Rv

print("== Y PART 3 ROBUSTNESS ==")
sol=solve_el(K_LOW,1e-3,1e-8)
rr=sol.x; f0=sol.y[0]; lam=float(sol.p[0])
g2=(sol.y[1])**2+(f0/rr)**2
E_el=float(np.trapezoid(elastic_density(g2,K_LOW)*2*PI*rr,rr))
LOG=float(np.trapezoid((f0**2/(2*rr**2))*2*PI*rr,rr))
E_rot=0.5*OMEGA*JT; D_E=(E_el-LOG+E_rot)/E_rot
ALPHA_INV=137.035999084
base_ppm=(4*PI**3*D_E/ALPHA_INV-1)*1e6
print(f"   D_E={D_E:.7f}   base residual {base_ppm:+.1f} ppm\n")

hs=[2.0*(-1)**(m+1)/(16*m*m-1) for m in range(1,7)]

for N in (2000,3000,4500):
    rm=np.geomspace(rr[0],rr[-1],N)
    f0m=interp1d(rr,f0,kind="cubic")(rm)
    R0=residual(f0m,rm,lam)
    h=1e-6*max(1.0,float(np.max(np.abs(f0m))))
    J=np.zeros((N,N))
    for j in range(N):
        fv=f0m.copy(); fv[j]+=h
        J[:,j]=(residual(fv,rm,lam)-R0)/h
    s_unit=2*PI*rm*(OMEGA**2-2.0*lam*OMEGA)*f0m
    s_unit[0]=0.0; s_unit[-1]=0.0
    chis=[]
    for m,hm in enumerate(hs,start=1):
        Jd=J.copy()
        idx=np.arange(1,N-1)
        Jd[idx,idx]+=-(4*m*OMEGA)**2*2*PI*rm[1:-1]
        f4u=np.linalg.solve(Jd,s_unit)
        w1=2*PI*rm*np.abs(OMEGA**2-2.0*lam*OMEGA)
        chi_P1=float(np.trapezoid(f4u*w1*f0m,rm)/np.trapezoid(f0m*w1*f0m,rm))
        w2=2*PI*rm
        chi_P2=float(np.trapezoid(f4u*w2*f0m,rm)/np.trapezoid(f0m*w2*f0m,rm))
        dE=-0.5*float(np.trapezoid(f4u*s_unit,rm))
        chi_P3=dE/(E_el-LOG)
        chis.append((chi_P1,chi_P2,chi_P3))
    for label,k_ in (("P1 rot-weight",0),("P2 plain-norm",1),("P3 energy",2)):
        Delta=0.5*sum(hm*hm*c[k_] for hm,c in zip(hs,chis))
        corrected=4*PI**3*D_E*(1-Delta)
        ppm=(corrected/ALPHA_INV-1)*1e6
        eps4_equiv=15*Delta
        print(f"   N={N} {label:14s}: Delta={Delta:.6e}  eps4_equiv={eps4_equiv:.5f}  -> residual {ppm:+7.1f} ppm")
    m1only=0.5*hs[0]**2*chis[0][0]
    print(f"   N={N} (m=1 only, P1): Delta={m1only:.6e}  -> residual {(4*PI**3*D_E*(1-m1only)/ALPHA_INV-1)*1e6:+7.1f} ppm\n")
