"""GATE 3: THE 13.6 eV SECOND PREDICTION (chartered: 'same anchor, same
convention, no new freedom' -- Z audit item 3, SYNC_STATE open gates).

WHAT THIS GATE IS AND IS NOT (stated before any number):
  O Phase 2 confronted the atomic coupling with the star-anchored constant
  alone and MISSED by 1903x (registered negative, O7). The chain built since
  (T..Z + Gates 1-2) supplies what O lacked: a DERIVED alpha. Gate 3 asks
  whether the atomic coupling now follows from registered structures with no
  new freedom. It is a CONSISTENCY CONFRONTATION of the derived alpha through
  registered mechanics -- its bite is the CONVENTION-COUNT DISCIPLINE:
    The binding energy is an ENERGY-type observable. Y Brick 4's theorem:
    energy invariants are smooth quadratic; NO rectified reading exists for
    them. Therefore the convention permits ZERO additional 4/pi factors
    beyond the one already inside the derived alpha (Gate 2's, applied once
    to e^2). Sneaking in one more would 'improve' nothing and is FORBIDDEN.

PRE-STATED CRITERION (fixed before computation):
  E_pred = e^2/(2 a0) with e^2 through alpha_chain = 1/(4 pi^3 D_E), a0 the
  registered anchor, the 1/2 from the virial theorem on the registered 1/d
  Coulomb form (EM-015, Derived), and ZERO additional convention factors.
    PASS: within 1000 ppm of the measured Rydberg. Exact expectation, forced
      by algebra if the chain is consistent: +2 x 178.8 = +357.6 ppm (the
      chain residual enters squared through alpha^2).
    COMPETITOR (convention-count violation): ONE extra rectified factor
      (4/pi) -> +27% miss. Its exclusion is the gate's discipline content.
    FAIL: anything else; registered negative.

Registered inputs: alpha_chain = 1/(4 pi^3 D_E), D_E = 1.1051029 (W, blind,
twice reproduced); a0 = lambda_bar_C/alpha (anchor); Coulomb 1/d with derived
sign (EM-015); m_e (the corpus's one measured mass input); virial 1/2 (derived
below, symbolic); Gate 2 (the single 4/pi lives inside e^2, applied ONCE).
"""
import sympy as sp

pi = sp.pi

print("== STEP 1: THE 1/2 FROM MECHANICS (virial on the registered 1/d form) ==")
r, e2, mm, J = sp.symbols('r e2 m J', positive=True)
# Bound mode at the anchor: kinetic from the frozen action (J-type), Coulomb
# from the registered 1/d form. E(r) = J^2/(2 m r^2) - e2/r  (registered forms)
E = J**2/(2*mm*r**2) - e2/r
rmin = sp.solve(sp.diff(E, r), r)[0]
Emin = sp.simplify(E.subs(r, rmin))
V_at = sp.simplify((-e2/r).subs(r, rmin))
print(f"   stationary scale: r* = {rmin}   (the anchor scale, self-consistently)")
print(f"   E(r*) = {Emin} = (1/2) V(r*) = {sp.simplify(V_at/2)}  -> ratio {sp.simplify(Emin/V_at)}")
print("   The 1/2 is the virial ratio of the registered 1/d form. DERIVED, exact.")
print("   E_bind = e^2/(2 a0), with a0 the registered anchor scale.")

print("\n== STEP 2: THE PREDICTION (no new freedom; alpha enters DERIVED) ==")
import numpy as np
PI = np.pi
D_E = 1.1051029                       # W, blind, twice reproduced
alpha_chain = 1.0/(4*PI**3*D_E)       # Gates 1+2: every factor derived
mc2_eV = 510998.95000                 # m_e c^2 (the one measured mass input)
Ry_meas = 13.605693122994             # measured Rydberg energy, eV
# E = e^2/(2 a0) = (1/2) alpha^2 m c^2   [a0 = lambda_bar_C/alpha, e^2 = alpha hbar c]
E_pred = 0.5*alpha_chain**2*mc2_eV
ppm = (E_pred/Ry_meas - 1)*1e6
print(f"   alpha_chain = 1/(4 pi^3 D_E) = 1/{4*PI**3*D_E:.6f}")
print(f"   E_pred = (1/2) alpha_chain^2 m c^2 = {E_pred:.6f} eV")
print(f"   measured Rydberg               = {Ry_meas:.6f} eV")
print(f"   landing: {ppm:+.1f} ppm   (pre-stated expectation: +357.6 ppm = 2 x 178.8)")

print("\n== STEP 3: THE CONVENTION-COUNT COMPETITOR (must fail) ==")
E_extra = E_pred*(4/PI)               # one forbidden extra rectified factor
print(f"   with ONE extra 4/pi: {E_extra:.4f} eV -> {(E_extra/Ry_meas-1)*100:+.2f}%  EXCLUDED")
print("   Y Brick 4's theorem forbids it: the binding is energy-type, smooth")
print("   quadratic, no rectified reading exists. The single 4/pi of the chain")
print("   lives inside e^2 (Gate 2), applied once, and nowhere else.")

print("\n== STEP 4: CLOSING THE O-B LOOP (why O missed 1903x and this does not) ==")
print("   O Phase 2 carried J0 = hbar/(pi alpha) but NO derived alpha and no")
print("   charge functional: the star-anchored constant alone cannot reach an")
print("   alpha^2-suppressed observable. The chain since supplies alpha derived")
print("   (Gates 1-2) and the Coulomb form registered (EM-015). The 1903x miss")
print("   is thereby EXPLAINED, not contradicted: O tested the wrong reduction.")

print("\n== VERDICT (pre-stated criterion) ==")
if abs(ppm) < 1000:
    print(f"   GATE 3 PASSES at {ppm:+.1f} ppm, exactly the chain residual squared")
    print("   through alpha^2 (+2 x 178.8 ppm), as consistency requires. Zero")
    print("   additional convention factors; the competitor excluded at +27%.")
    print("   FND-MATTER-001's atomic-coupling half REDUCES to the chain's one")
    print("   open number (+178.8 ppm). The gate's honest scope: this is the")
    print("   derived alpha confronted through registered mechanics -- a")
    print("   consistency PASS with convention-count discipline, NOT a new")
    print("   independent constant. The independent content is Steps 1+3:")
    print("   the 1/2 derived, the extra-4/pi excluded, the O-B negative resolved.")
else:
    print(f"   GATE 3 FAILS at {ppm:+.1f} ppm: registered negative, full volume.")
