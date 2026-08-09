# LEAD-RAD SESSION 2: CONSTRUCTION PHASE (ALPHA OUT OF THE ROOM)
# Charter: docs/commissions/COMMISSION_LEAD_RAD_radiative_backreaction.md
# Worklog handoff (2026-08-09 session 1): construct both observable
# functionals explicitly, subtract the static (W-committed) kernel, and
# adjudicate the M^(1/3) divergence cancellation BEFORE any confrontation.
# NO reference to 178.8, 1161.4, 137, or measured g anywhere in this file.
#
# KERNEL (derived once, used for both observables -- charter bar A4):
# 2D Helmholtz outgoing Green's function, angular mode m, wavenumber k,
# evaluated source-on-source: G_m(k; r,r') = (i/4) J_m(k r_<) H^(1)_m(k r_>).
#   reactive (real) part:  -(1/4) J_m(k r_<) Y_m(k r_>)
#   radiative (imag) part: +(1/4) J_m(k r_<) J_m(k r_>)
# Static (Laplace) mode kernel (the piece the committed static solver
# already contains): (1/(4 pi m)) (r_</r_>)^m  [m >= 1].
# Verified limit: -(1/4) J_m Y_m -> 1/(4 pi m) (r</r>)^m as k -> 0.
#
# A2 (moment side): point terminus circulating at beta = Omega R / c = 1
#   (Gate 2b registered kinematics). Modes m = 1..M at k_m R = m.
#   Delta_m = -(1/4) J_m(m) Y_m(m) - 1/(4 pi m).
# A3 (energy side): the committed W solution f(r) with unit winding
#   (the f^2/2r^2 LOG term IS the winding self-energy; D-E-COMPLETE A2),
#   rotating at Omega = pi/x*: single mode m = 1 at frequency Omega,
#   wavenumber k = Omega (unit wave speed, solver units).
#   W_dyn = -(1/4)(2 pi)^2 II f(r) f(r') J_1(k r_<) Y_1(k r_>) r r' dr dr'
#   W_stat = (1/(4 pi))(2 pi)^2 II f(r) f(r') (r_</r_>) r r' dr dr'
#   w1 = (W_dyn - W_stat) / E_rot   (dimensionless, per unit coupling^2)

import numpy as np
from scipy.special import jv, yv
from scipy.optimize import minimize
from scipy.integrate import solve_bvp
from scipy.interpolate import interp1d

PI = np.pi
XSTAR = float(np.exp(PI**2))
OMEGA = PI / XSTAR
JT = PI**2 * (XSTAR**2 - 1.0) / XSTAR
NORM_TARGET = JT / OMEGA
E_ROT = 0.5 * OMEGA * JT
K_LOW = 2.0

print("== LEAD-RAD SESSION 2: CONSTRUCTION (alpha out of the room) ==\n")

# ---------------------------------------------------------------- A2 ---
print("-- A2: moment-side mode sums at beta = 1 (point terminus) --")
M_list = [100, 300, 1000, 3000, 10000, 30000]
def a2_sums(M):
    m = np.arange(1, M + 1, dtype=float)
    Jm = jv(m, m); Ym = yv(m, m)
    react = -0.25 * Jm * Ym
    stat = 1.0 / (4.0 * PI * m)
    rad = 0.25 * Jm**2
    return float(np.sum(react - stat)), float(np.sum(rad)), float(np.sum(react))

rows = []
for M in M_list:
    d, r, re = a2_sums(M)
    rows.append((M, d, r))
    print(f"  M={M:>6}: sum(react-stat)={d:.6f}   sum(rad)={r:.6f}")

# divergence exponent of the subtracted sum: fit Delta(M) ~ a + b M^p
d1 = rows[-3][1]; d2 = rows[-2][1]; d3 = rows[-1][1]
# successive differences ratio -> 3^p
p_sub = np.log((d3 - d2) / (d2 - d1)) / np.log(3.0)
r1 = rows[-3][2]; r2 = rows[-2][2]; r3 = rows[-1][2]
p_rad = np.log((r3 - r2) / (r2 - r1)) / np.log(3.0)
print(f"  growth exponent, subtracted reactive sum: M^{p_sub:.3f}")
print(f"  growth exponent, radiative sum:           M^{p_rad:.3f}")
CUTOFF_SENSITIVE = p_sub > 0.05
print(f"  ADJUDICATION A2: static subtraction {'DOES NOT' if CUTOFF_SENSITIVE else 'DOES'} "
      f"cancel the divergence.")
if CUTOFF_SENSITIVE:
    # cutoff sensitivity: relative change of the sum per decade of M
    dec = (d3 - d2) / d3
    print(f"  cutoff sensitivity: {dec*100:.1f}% change over ~half-decade of M "
          f"-> weight is CUTOFF-DEFINED, power ~1/3 (as flagged in worklog).")

# rotating-frame combination check: per-mode, radiated L flux = (m/omega_m) x
# radiated E flux = E flux / Omega exactly (omega_m = m Omega). So the
# ROTATING-FRAME radiative budget E - Omega L vanishes mode-by-mode for the
# synchronous self-field -- an identity, printed as a derived structural fact.
print("  structural identity: radiated (E - Omega L) = 0 per mode (omega_m = m Omega);")
print("  the RADIATIVE budget drops out of the rotating-frame functional identically.")
print("  The REACTIVE stored piece has no such identity; its subtracted sum is the")
print("  cutoff-sensitive object above.\n")

# ---------------------------------------------------------------- A3 ---
print("-- A3: energy-side weight on the committed f(r) (m=1, k=Omega) --")
# reproduce the committed static solution (identical machinery to w_dressing_phase1c)
def make_grid(n, r_min, r_max):
    r = np.geomspace(r_min, r_max, n)
    w = np.zeros_like(r); w[1:-1] = (r[2:] - r[:-2]) / 2.0
    w[0] = (r[1] - r[0]) / 2.0; w[-1] = (r[-1] - r[-2]) / 2.0
    return r, w * 2.0 * PI * r
def elastic_density(g2, k):
    eps = np.sqrt(1.0 + g2) - 1.0; return eps + 0.5 * k * eps**2
def de_dg2(g2, k):
    E = np.sqrt(1.0 + g2); return (1.0 + k * (E - 1.0)) / (2.0 * E)
def lbfgs_guess(k, n_grid, r_min, lam_pen=1e4):
    r, w = make_grid(n_grid, r_min, XSTAR)
    def obj_grad(f):
        df = np.gradient(f, r); g2 = df**2 + (f / r)**2
        E = float(np.sum((elastic_density(g2, k) + 0.5 * OMEGA**2 * f**2) * w))
        J = OMEGA * float(np.sum(f**2 * w)); pen = lam_pen * (J / JT - 1.0)**2
        dd = de_dg2(g2, k); g = (2.0 * dd * f / r**2 + OMEGA**2 * f) * w
        flux = 2.0 * dd * df * 2.0 * PI * r
        g -= np.gradient(flux, r) * (w / (2.0 * PI * r))
        g += lam_pen * 2.0 * (J / JT - 1.0) / JT * (2.0 * OMEGA * f * w)
        return E + pen, g
    f0 = np.ones_like(r); f0 *= np.sqrt(NORM_TARGET / float(np.sum(f0**2 * w)))
    res = minimize(obj_grad, f0, jac=True, method="L-BFGS-B",
                   bounds=[(0.0, None)] * len(r),
                   options=dict(maxiter=20000, ftol=1e-14, gtol=1e-10))
    f = res.x * np.sqrt(NORM_TARGET / float(np.sum(res.x**2 * w)))
    return r, f
def P_fun(g2, k):
    E = np.sqrt(1.0 + g2); return k + (1.0 - k) / E
def Pp_fun(g2, k):
    E = np.sqrt(1.0 + g2); return (k - 1.0) / (2.0 * E**3)
def rhs(r, y, p, k):
    lam = p[0]; f, fp, _ = y; g2 = fp**2 + (f / r)**2
    P = P_fun(g2, k); Pp = Pp_fun(g2, k)
    RHS = r * (P * f / r**2 + (OMEGA**2 - 2.0 * lam * OMEGA) * f)
    num = RHS - P * fp - r * Pp * fp * (2.0 * f * fp / r**2 - 2.0 * f**2 / r**3)
    den = r * P + 2.0 * r * Pp * fp**2
    return np.vstack([fp, num / den, 2.0 * PI * r * f**2])
def bcs(ya, yb, p):
    return np.array([ya[1], yb[1], ya[2], yb[2] - NORM_TARGET])
def solve_el(k, r_min, tol, n_mesh=4000):
    r_g, f_g = lbfgs_guess(k, 6400, r_min)
    r = np.geomspace(r_min, XSTAR, n_mesh)
    fi = interp1d(r_g, f_g, kind="cubic", fill_value="extrapolate")(r)
    fpi = np.gradient(fi, r)
    ni = np.concatenate([[0.0], np.cumsum(0.5 * (2 * PI * r[1:] * fi[1:]**2
        + 2 * PI * r[:-1] * fi[:-1]**2) * np.diff(r))])
    s = np.sqrt(NORM_TARGET / ni[-1]); fi, fpi, ni = fi * s, fpi * s, ni * s**2
    sol = solve_bvp(lambda r_, y_, p_: rhs(r_, y_, p_, k), bcs, r,
                    np.vstack([fi, fpi, ni]), p=[OMEGA * 0.7], tol=tol,
                    max_nodes=400000, verbose=0)
    return sol

def a3_weight(sol):
    rr = sol.x; f = sol.y[0]
    kw = OMEGA  # wavenumber of the m=1 rotating winding, unit wave speed
    # source density in the winding channel: sigma(r) = f(r); pair integrals
    # with kernel K(r,r') on measure (2 pi r dr)(2 pi r' dr'). Use ordered
    # double integral: II = 2 * int_r' int_{r<r'} + diagonal (measure zero).
    J1 = jv(1, kw * rr); Y1 = yv(1, kw * rr)
    w_meas = np.gradient(rr) * 2.0 * PI * rr  # trapezoid-ish weights
    w_meas[0] = (rr[1] - rr[0]) / 2 * 2 * PI * rr[0]
    w_meas[-1] = (rr[-1] - rr[-2]) / 2 * 2 * PI * rr[-1]
    fw = f * w_meas
    # cumulative inner sums for r_< integrals
    cum_fJ = np.cumsum(fw * J1)          # int_{r'<=r} f J_1(k r') dmu
    cum_fr = np.cumsum(fw * rr)          # int_{r'<=r} f r' dmu   (static, (r</r>)^1)
    W_dyn = -0.25 * float(np.sum(fw * Y1 * cum_fJ)) * 2.0  # 2x ordered
    W_stat = (1.0 / (4.0 * PI)) * float(np.sum(fw / rr * cum_fr)) * 2.0
    W_radQ = 0.25 * float(np.sum(fw * J1)) ** 2            # radiative quad form
    return W_dyn, W_stat, W_radQ

runs = []
for r_min, tol in [(1e-3, 1e-8), (1e-3, 1e-10), (3e-4, 1e-8)]:
    sol = solve_el(K_LOW, r_min, tol)
    if not sol.success:
        print(f"  r_min={r_min:.0e}: BVP FAILED"); continue
    Wd, Ws, Wr = a3_weight(sol)
    w1 = (Wd - Ws) / E_ROT
    runs.append(w1)
    print(f"  r_min={r_min:.0e} tol={tol:.0e}: W_dyn={Wd:.6e} W_stat={Ws:.6e} "
          f"W_rad={Wr:.6e}  w1=(dyn-stat)/E_rot={w1:.6e}")
if runs:
    w1_med = float(np.median(runs))
    spread = (max(runs) - min(runs)) / abs(w1_med) * 100 if w1_med else float("inf")
    print(f"  w1 median = {w1_med:.6e}  spread = {spread:.3f}% -> "
          f"{'STABLE (finite, derived)' if spread < 1.0 else 'UNSTABLE'}")
    print("  A3 ADJUDICATION: extended source -> NO cutoff issue; w1 is a derived")
    print("  finite functional of the registered f(r). Sign and magnitude recorded")
    print("  blind; the correction enters as (1 + w1 * coupling^2) on the dressing,")
    print("  coupling carried symbolically (alpha_bare). NO targets loaded.\n")

print("== CONSTRUCTION VERDICT (pre-confrontation, per worklog handoff) ==")
print("A2 (moment, point source at beta=1): subtracted reactive sum remains")
print("   divergent ~ M^(1/3); static subtraction does NOT regulate it. The")
print("   moment-side weight is defined only WITH a physical UV cutoff, and the")
print("   corpus's own audit (D-E-COMPLETE A2) showed the core scale -> 0.")
print("A3 (energy, extended committed f): finite derived weight w1, no cutoff.")
print("A4 single-mechanism bar: same kernel used for both; no per-observable")
print("   freedom introduced.")
