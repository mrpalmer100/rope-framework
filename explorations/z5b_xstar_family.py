"""BRICK 5b: second derived channel -- the full-closure x* family.
D(x*) along the committed ties Omega = pi/x*, J_T = pi^2(x*^2-1)/x*.
If T's anchor ln x* = pi^2 carries a small additive correction delta_ln,
then delta(1/alpha)/(1/alpha) = c_x * delta_ln with c_x = dln(D)/dln(x*)
(the 4 pi^3 prefactor is x*-independent). Required for closure:
delta_ln = -1.788e-4 / c_x  -- committed blind, then confronted."""
import numpy as np
from scipy.optimize import minimize
from scipy.integrate import solve_bvp
from scipy.interpolate import interp1d
PI=np.pi; K=2.0
def solve_D(XS,r_min=1e-3,tol=1e-8,n_mesh=4000):
    OM=PI/XS; JT=PI**2*(XS**2-1.0)/XS; NT=JT/OM
    def eld(g2):
        e=np.sqrt(1.0+g2)-1.0; return e+0.5*K*e**2
    def ddg(g2):
        E=np.sqrt(1.0+g2); return (1.0+K*(E-1.0))/(2.0*E)
    def guess(n_grid,lam_pen=1e4):
        r=np.geomspace(r_min,XS,n_grid)
        w=np.zeros_like(r); w[1:-1]=(r[2:]-r[:-2])/2.0; w[0]=(r[1]-r[0])/2.0; w[-1]=(r[-1]-r[-2])/2.0
        w=w*2.0*PI*r
        def og(f):
            df=np.gradient(f,r); g2=df**2+(f/r)**2
            E=float(np.sum((eld(g2)+0.5*OM**2*f**2)*w))
            J=OM*float(np.sum(f**2*w)); pen=lam_pen*(J/JT-1.0)**2
            dd=ddg(g2); g=(2.0*dd*f/r**2+OM**2*f)*w
            flux=2.0*dd*df*2.0*PI*r; g-=np.gradient(flux,r)*(w/(2.0*PI*r))
            g+=lam_pen*2.0*(J/JT-1.0)/JT*(2.0*OM*f*w); return E+pen,g
        f0=np.ones_like(r); f0*=np.sqrt(NT/float(np.sum(f0**2*w)))
        res=minimize(og,f0,jac=True,method="L-BFGS-B",bounds=[(0.0,None)]*len(r),options=dict(maxiter=20000,ftol=1e-14,gtol=1e-10))
        f=res.x*np.sqrt(NT/float(np.sum(res.x**2*w))); return r,f
    def P_(g2):
        E=np.sqrt(1.0+g2); return K+(1.0-K)/E
    def Pp_(g2):
        E=np.sqrt(1.0+g2); return (K-1.0)/(2.0*E**3)
    def rhs(r,y,p):
        lam=p[0]; f,fp,_=y; g2=fp**2+(f/r)**2; P=P_(g2); Pp=Pp_(g2)
        RHS=r*(P*f/r**2+(OM**2-2.0*lam*OM)*f)
        num=RHS-P*fp-r*Pp*fp*(2.0*f*fp/r**2-2.0*f**2/r**3)
        den=r*P+2.0*r*Pp*fp**2
        return np.vstack([fp,num/den,2.0*PI*r*f**2])
    def bcs(ya,yb,p):
        return np.array([ya[1],yb[1],ya[2],yb[2]-NT])
    r_g,f_g=guess(6400)
    r=np.geomspace(r_min,XS,n_mesh)
    fi=interp1d(r_g,f_g,kind="cubic",fill_value="extrapolate")(r)
    ni=np.concatenate([[0.0],np.cumsum(0.5*(2*PI*r[1:]*fi[1:]**2+2*PI*r[:-1]*fi[:-1]**2)*np.diff(r))])
    s=np.sqrt(NT/ni[-1]); fi=fi*s; ni=ni*s**2
    y0=np.vstack([fi,np.gradient(fi,r),ni])
    sol=solve_bvp(rhs,bcs,r,y0,p=[OM*0.7],tol=tol,max_nodes=400000,verbose=0)
    if not sol.success: return None
    rr=sol.x; f=sol.y[0]; fp=sol.y[1]; g2=fp**2+(f/rr)**2
    E_el=float(np.trapezoid(eld(g2)*2*PI*rr,rr))
    LOG=float(np.trapezoid((f**2/(2*rr**2))*2*PI*rr,rr))
    Erot=0.5*OM*JT
    return (E_el-LOG+Erot)/Erot
XS0=float(np.exp(PI**2))
print("== BRICK 5b: full-closure x* family ==")
vals={}
for eps in (-0.01,0.0,0.01):
    D=solve_D(XS0*(1+eps)); vals[eps]=D
    print(f"   eps={eps:+.2f}: D_E={D:.7f}")
cx=(vals[0.01]-vals[-0.01])/0.02/vals[0.0]
print(f"\n== COMMIT: c_x = d ln D_E / d ln x* (full closure) = {cx:.5f} ==")
print(f"\n== CONFRONTATION ==")
need=-1.788e-4
dln=need/cx
print(f"   required delta(ln x*) for closure = {dln:+.4e}")
print(f"   as a correction to T's anchor: ln x* = pi^2 + {dln:+.3e}")
print(f"   natural scales: 1/x* = {1/XS0:.3e}   pi/x* = {PI/XS0:.3e}   pi^2/x* = {PI**2/XS0:.3e}")
for lbl,v in (("1/x*",1/XS0),("pi/x*",PI/XS0),("pi^2/x*",PI**2/XS0),("-1/x*",-1/XS0),("-pi/x*",-PI/XS0),("-pi^2/x*",-PI**2/XS0)):
    print(f"      delta_ln / ({lbl:8s}) = {dln/v:+8.4f}")
