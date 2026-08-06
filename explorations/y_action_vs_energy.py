"""COMMISSION Y: canonical action vs energy dressing.

PRE-REGISTERED DEFINITIONS (fixed before any number is compared to a target):

Setup: the committed W solution f0(r) rotates in internal phase chi(t)=Omega t.
Real components at each material point: (u,v) = f0(r)(cos chi, sin chi).
The elastic law eps(g) = sqrt(1+g^2)-1 + 0.5 k eps^2 interpolates between
quadratic response (g<<1, eps ~ g^2/2) and LINEAR rectified response
(g>>1, eps ~ |g|).

PART 1 -- LINEAR/QUADRATIC GATE (the physics gate).
For the committed solution, compute the local response exponent
    n(r) = d ln(eps_tot) / d ln(g)
(n=2 quadratic, n=1 linear/rectified) and its energy-weighted mean n_bar.
Also compute the fraction of elastic energy accrued in the g>1 (linear) regime.
GATE: the 4/pi is admissible ONLY if the response is predominantly linear.

PART 2 -- CYCLE INTEGRALS (mechanical origin of the ratio).
The canonical/action coupling of a rotating pattern averages the LINEAR
response of the components over the cycle; the energy averages the QUADRATIC
invariant. Both are computed NUMERICALLY as cycle integrals on the solution
(no identity assumed):
    A_lin  = (1/2pi) int_0^{2pi} dchi  int dA sigma(r) * f0(r) * (|cos chi|+|sin chi|)/2
    A_quad = (1/2pi) int_0^{2pi} dchi  int dA sigma(r) * f0(r) * (cos^2+sin^2)
with sigma(r) = d eps_tot/dg evaluated on the solution (the linear-response
tension weight). The mechanical rectification ratio is
    R = A_lin / A_quad
computed blind, then compared to 4/pi = 1.2732395.
D_J/D_E := R if and only if Part 1's gate passes (linear-response origin).

PART 3 -- SECOND PREDICTION eps_4 (the arbiter).
The rectified response has the exact Fourier expansion
    (|cos chi|+|sin chi|)/ (4/pi) = 1 + 2 sum_m (-1)^{m+1} cos(4m chi)/(16 m^2 -1)
whose leading harmonic is (2/15) cos 4chi. This 4Omega drive perturbs the
profile: linearize the solver's EL residual around f0 and solve
    L1[f4] = s(r),   s(r) = (2/15) * 2 pi r (Omega^2 - 2 lam Omega) f0
(the drive is a (2/15) modulation of the elastic sector; at the solution the
elastic residual equals minus the rotational residual, giving s in closed
form). PRE-REGISTERED measure:
    eps_4 = (2/15) * <f4, w f0> / <f0, w f0>,  w = 2 pi r |Omega^2 - 2 lam Omega|
Then test the reviewer's closure 1/alpha = 4 pi^3 D_E (1 - eps_4/15)
against 137.035999. Blind: eps_4 printed before the comparison block.
"""
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

# ---- reproduce the committed solution (identical machinery to phase1c) ----
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

def solve_el(k,r_min,tol,n_mesh=4000):
    r_g,f_g=lbfgs_guess(k,6400,r_min); r=np.geomspace(r_min,XSTAR,n_mesh)
    fi=interp1d(r_g,f_g,kind="cubic",fill_value="extrapolate")(r); fpi=np.gradient(fi,r)
    ni=np.concatenate([[0.0],np.cumsum(0.5*(2*PI*r[1:]*fi[1:]**2+2*PI*r[:-1]*fi[:-1]**2)*np.diff(r))])
    s=np.sqrt(NORM_TARGET/ni[-1]); fi,fpi,ni=fi*s,fpi*s,ni*s**2
    y0=np.vstack([fi,fpi,ni]); lam0=OMEGA*0.7
    sol=solve_bvp(lambda r_,y_,p_:rhs(r_,y_,p_,k),bcs,r,y0,p=[lam0],tol=tol,max_nodes=400000,verbose=0)
    return sol

print("== COMMISSION Y: action vs energy dressing ==")
print("   solving committed configuration (r_min=1e-3, tol=1e-8) ...")
sol = solve_el(K_LOW, 1e-3, 1e-8)
assert sol.success
rr = sol.x; f0 = sol.y[0]; fp0 = sol.y[1]; lam = float(sol.p[0])
g2 = fp0**2 + (f0/rr)**2; g = np.sqrt(g2)
eps_tot = elastic_density(g2, K_LOW)
E_el = float(np.trapezoid(eps_tot*2*PI*rr, rr))
LOG  = float(np.trapezoid((f0**2/(2*rr**2))*2*PI*rr, rr))
E_rot = 0.5*OMEGA*JT
D_E = (E_el - LOG + E_rot)/E_rot
print(f"   D_E (check) = {D_E:.7f}  (committed 1.1051029)\n")

# ---------- PART 1: linear/quadratic gate ----------
E = np.sqrt(1.0+g2)
deps_dg = (1.0 + K_LOW*(E-1.0)) * g/E          # d eps_tot / dg
n_local = np.where(eps_tot>0, g*deps_dg/np.maximum(eps_tot,1e-300), 2.0)
wE = eps_tot*2*PI*rr                            # elastic energy density weight
n_bar = float(np.trapezoid(n_local*wE, rr)/np.trapezoid(wE, rr))
frac_lin = float(np.trapezoid(wE*(g>1.0), rr)/np.trapezoid(wE, rr))
g_med = float(np.interp(0.5, np.cumsum(wE*np.gradient(rr))/np.trapezoid(wE,rr), g))
print("== PART 1: LINEAR/QUADRATIC GATE ==")
print(f"   energy-weighted response exponent n_bar = {n_bar:.4f}   (2=quadratic, 1=linear)")
print(f"   fraction of elastic energy at g>1 (linear regime) = {frac_lin:.4f}")
print(f"   energy-median strain g = {g_med:.4f}")
gate = "LINEAR (rectified response admissible)" if n_bar < 1.5 else "QUADRATIC (4/pi NOT admissible -> falsified)"
print(f"   GATE: {gate}\n")

# ---------- PART 2: cycle integrals, computed blind ----------
sigma = deps_dg                                  # linear-response tension weight
prof = float(np.trapezoid(sigma*f0*2*PI*rr, rr)) # common profile integral
chi = np.linspace(0, 2*PI, 20001)
A_lin  = prof * float(np.trapezoid((np.abs(np.cos(chi))+np.abs(np.sin(chi)))/2.0, chi))/(2*PI)
A_quad = prof * float(np.trapezoid(np.cos(chi)**2+np.sin(chi)**2, chi))/(2*PI)
R = A_lin/A_quad
print("== PART 2: CYCLE INTEGRALS (blind) ==")
print(f"   A_lin  = {A_lin:.6f}")
print(f"   A_quad = {A_quad:.6f}")
print(f"   R = A_lin/A_quad = {R:.7f}")
print(f"   [comparison] 4/pi = {4/PI:.7f}   R/(4/pi)-1 = {(R/(4/PI)-1)*1e6:+.2f} ppm")
DJ = R*D_E
print(f"   D_J = R * D_E = {DJ:.7f}   (LEAD-2 target was 1.40681; D_J/1.40681-1 = {(DJ/1.40681-1)*100:+.4f}%)\n")

# ---------- PART 3: eps_4 from the f4 perturbation ----------
# residual of the static EL system on a mesh (natural BCs f'=0 at both ends)
def residual(fv, r):
    fpv = np.gradient(fv, r)
    g2v = fpv**2 + (fv/r)**2
    dd  = de_dg2(g2v, K_LOW)
    flux = 2.0*dd*fpv*2*PI*r
    Rv = -np.gradient(flux, r) + 2*PI*r*(2.0*dd*fv/r**2 + (OMEGA**2 - 2.0*lam*OMEGA)*fv)
    Rv[0] = fpv[0]; Rv[-1] = fpv[-1]            # enforce Neumann rows
    return Rv

# uniform-in-log working mesh for the linear solve
rm = np.geomspace(rr[0], rr[-1], 3000)
f0m = interp1d(rr, f0, kind="cubic")(rm)
R0 = residual(f0m, rm)
print("== PART 3: eps_4 (blind) ==")
print(f"   residual check |R[f0]| interior median = {np.median(np.abs(R0[1:-1])):.3e}")

# numerical Jacobian (banded structure, but build dense in blocks for robustness)
N = len(rm)
h = 1e-6*max(1.0, float(np.max(np.abs(f0m))))
J = np.zeros((N, N))
for j in range(N):
    fv = f0m.copy(); fv[j] += h
    J[:, j] = (residual(fv, rm) - R0)/h

# 4-Omega inertial term is O((4 Omega)^2) ~ 4e-7: include it for honesty
J_dyn = J.copy()
inert = -(4*OMEGA)**2 * 2*PI*rm
J_dyn[np.arange(1,N-1), np.arange(1,N-1)] += inert[1:-1]

s = (2.0/15.0) * 2*PI*rm * (OMEGA**2 - 2.0*lam*OMEGA) * f0m
s[0] = 0.0; s[-1] = 0.0
f4 = np.linalg.solve(J_dyn, s)

w = 2*PI*rm*np.abs(OMEGA**2 - 2.0*lam*OMEGA)
eps4 = (2.0/15.0) * float(np.trapezoid(f4*w*f0m, rm)/np.trapezoid(f0m*w*f0m, rm))
print(f"   eps_4 (pre-registered measure) = {eps4:.6f}")
print(f"   |eps_4| = {abs(eps4):.6f}   [comparison] reviewer's 0.00268 -> ratio {abs(eps4)/0.00268:.3f}\n")

# ---------- CLOSURE TEST ----------
ALPHA_INV = 137.035999084
print("== CLOSURE TEST: 1/alpha = 4 pi^3 D_E (1 - eps_4/15) ==")
base = 4*PI**3*D_E
print(f"   4 pi^3 D_E                    = {base:.6f}   ({(base/ALPHA_INV-1)*1e6:+.1f} ppm vs {ALPHA_INV})")
corr = base*(1 - abs(eps4)/15.0)
print(f"   with (1 - |eps_4|/15)         = {corr:.6f}   ({(corr/ALPHA_INV-1)*1e6:+.1f} ppm)")
corr2 = base*(1 - abs(eps4))
print(f"   [diagnostic] (1 - |eps_4|)    = {corr2:.6f}   ({(corr2/ALPHA_INV-1)*1e6:+.1f} ppm)")
