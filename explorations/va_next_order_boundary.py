"""COMMISSION V-A-NEXT-ORDER: THE BOUNDARY O(Omega) TERM (chartered; the
one-shot, pre-committed-bar attempt to close the +178.8 ppm residual).

CONSTRUCTION IDENTIFICATION (made ONCE, before any coefficient is computed,
per the NO SCAN bar -- this paragraph is the commitment):
  The V-A landing formula converts J0 to the confinement scale via the
  LUMINAL-EDGE condition: the terminus circulates where its edge speed
  meets the transverse wave speed (R Phase 1, registered; used at zeroth
  order in Gate 1's closure as Omega_t A = c). The boundary O(Omega) term
  the naive expansion drops is the FINITE-STRAIN correction to the wave
  speed AT the boundary of the committed profile: the landing actually
  reads Omega_t A = c_eff(g^2_boundary), where c_eff comes from the
  committed elastic structure P(g^2) = de/dg^2-normalized (the same P in
  the solver), and g^2_boundary is the committed solution's own strain at
  x*. This is a boundary quantity (evaluated at r = x*), it is dropped by
  power counting precisely because the strain scales with f(x*)/x* while
  Omega x* = pi keeps boundary products O(1), and it requires NO new
  structure -- profile, elastic law, and edge condition are all committed.
  NO other candidate will be computed. If this misses, the commission
  registers the miss and stops.

CHAIN DIRECTION (fixed by algebra before computing): the landing scale is
  A = pi lambda_bar_C x (c_eff/c). J0 = hbar at that A; alpha follows as
  1/alpha = 4 pi^3 D_E x (c/c_eff)... sign bookkeeping done symbolically
  below, not by hand.

PRE-COMMITTED BAR (from the charter, restated verbatim in effect):
  c_coeff (defined via 1/alpha = 4 pi^3 D_E (1 + c_coeff Omega),
  Omega = pi/x* = 1.624932e-4) must land in -1.10 +/- 20% WITH negative
  sign. Outside the band or wrong sign: MISS, registered, STOP.
  If the term lands, it is a LEAD until the second prediction holds.
"""
import numpy as np
import sympy as sp
import sys
sys.path.insert(0, 'explorations')
from w_dressing_phase1c import solve_el, lbfgs_guess, P_fun, K_LOW, XSTAR, OMEGA, JT, NORM_TARGET
from scipy.interpolate import interp1d
from scipy.integrate import solve_bvp

PI = np.pi

print("== STEP 1: THE COMMITTED BOUNDARY STRAIN (from the actual solver solution) ==")
# Re-solve the committed configuration properly (BVP, committed settings)
import w_dressing_phase1c as W
res = None
for r_min, tol in [(1e-3, 1e-8)]:
    r_g, f_g = W.lbfgs_guess(K_LOW, 6400, r_min)
    r = np.geomspace(r_min, XSTAR, 4000)
    fi = interp1d(r_g, f_g, kind="cubic", fill_value="extrapolate")(r)
    fpi = np.gradient(fi, r)
    ni = np.concatenate([[0.0], np.cumsum(0.5*(2*PI*r[1:]*fi[1:]**2 + 2*PI*r[:-1]*fi[:-1]**2)*np.diff(r))])
    s = np.sqrt(NORM_TARGET/ni[-1]); fi, fpi, ni = fi*s, fpi*s, ni*s**2
    y0 = np.vstack([fi, fpi, ni])
    sol = solve_bvp(lambda r_, y_, p_: W.rhs(r_, y_, p_, K_LOW), W.bcs, r, y0, p=[OMEGA*0.7], tol=tol, max_nodes=400000, verbose=0)
    if sol.success:
        res = sol; break
if res is None:
    print("   SOLVER FAILED -- no computation, no result. STOP."); raise SystemExit
rr, f, fp = res.x, res.y[0], res.y[1]
f_b = float(f[-1]); fp_b = float(fp[-1])
g2_b = fp_b**2 + (f_b/rr[-1])**2
print(f"   f(x*) = {f_b:.6e}, f'(x*) = {fp_b:.2e} (Neumann, ~0), x* = {XSTAR:.1f}")
print(f"   boundary strain g^2(x*) = (f/x*)^2 + f'^2 = {g2_b:.6e}")

print("\n== STEP 2: THE EFFECTIVE BOUNDARY WAVE SPEED (committed elastic law) ==")
# Transverse wave speed under the committed density e(g2): c_eff^2/c^2 = 2 de/dg2
# (normalized so g2 -> 0 gives c_eff = c; same de_dg2 as the solver's).
de = W.de_dg2(np.array([g2_b]), K_LOW)[0]
c_ratio = np.sqrt(2.0*de)
delta = c_ratio - 1.0
print(f"   de/dg2 at boundary = {de:.9f}   (g2->0 value: 0.5)")
print(f"   c_eff/c = sqrt(2 de/dg2) = {c_ratio:.9f}   delta = {delta:+.3e}")

print("\n== STEP 3: SIGN BOOKKEEPING (symbolic, alpha out of the room) ==")
hbar, m, c, ceff, DE = sp.symbols('hbar m_e c c_eff D_E', positive=True)
lamC = hbar/(m*c)
# Gate 1 closure at next order: J0(A) = m c_land A / pi with the landing speed
# c_land = c_eff; J0 = hbar  =>  A = pi hbar/(m c_eff) = pi lamC (c/c_eff).
A_land = sp.solve(sp.Eq(m*ceff*sp.Symbol('A')/sp.pi, hbar), sp.Symbol('A'))[0]
print(f"   landing scale A = {A_land} = pi lambda_bar_C (c/c_eff)")
# The chain: 1/alpha = 4 pi^3 D_E scaled by the same landing shift. The anchor
# relation (Gate 1, target 1) J0(a0) = m c_land a0/pi = hbar/(pi alpha):
#   1/alpha = pi^2 m c_eff a0 ... net: 1/alpha proportional to c_eff
#   => 1/alpha = 4 pi^3 D_E (c_eff/c)
print("   anchor relation carries the SAME landing speed: 1/alpha ~ c_eff")
print("   => 1/alpha = 4 pi^3 D_E (1 + delta),  c_coeff = delta/Omega")

print("\n== STEP 4: THE COEFFICIENT, GRADED AGAINST THE PRE-COMMITTED BAR ==")
c_coeff = delta/OMEGA
print(f"   Omega = pi/x* = {OMEGA:.6e}")
print(f"   c_coeff = delta/Omega = {c_coeff:+.4f}")
print(f"   BAR: -1.10 +/- 20% (i.e. [-1.32, -0.88]), negative sign REQUIRED")
in_band = (-1.32 <= c_coeff <= -0.88)
print(f"   IN BAND: {in_band}   SIGN: {'negative' if c_coeff < 0 else 'POSITIVE (wrong)'}")

print("\n== VERDICT (pre-stated; one computation, no scan) ==")
if in_band:
    print("   c LANDS. Status: LEAD (charter outcome 2) pending the second")
    print("   prediction. Do NOT graduate without it.")
else:
    print("   MISS (charter outcome 3). The boundary finite-strain term of the")
    print("   committed landing condition is NOT the residual's source. Per the")
    print("   NO SCAN bar this commission computes nothing else and STOPS.")
    print("   Reading (registered with the miss): the residual ladder was already")
    print("   exhausted in-package; this was the last named classical candidate.")
    print("   Its miss points hard toward charter outcome 4 territory -- the")
    print("   residual as the radiative/quantum fence, the same physics class as")
    print("   the g=2 Schwinger residual -- but outcome 4 is NOT hereby claimed;")
    print("   it would need its own positive identification. What is registered")
    print("   today: outcome 3, one candidate honestly closed, the standing")
    print("   result untouched: 1/alpha = 4 pi^3 D_E, +178.8 +/- 0.4 ppm, every")
    print("   factor derived, three observables consistent.")
