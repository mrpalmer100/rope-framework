"""PRED-003-XCHAIN: the two-alpha-chain consistency audit.

HBAR-011's named next-order. The corpus carries two expressions for the
fine-structure constant:

  CHAIN 1 (PRED-003):  alpha = 2 T^2 / (kappa a)          [derived chain, paper P6]
  CHAIN 2 (HBAR-011):  alpha = e^2 / (4 pi eps0 hbar c),  hbar = pi T A^2 / (2 c)
                       =>  alpha = e^2 / (2 pi^2 eps0 T A^2)

Bars locked in analysis/PRED003_XCHAIN_bars_LOCKED.md BEFORE computation.
All algebra symbolic. Verdict rule R1: consistency promotes nothing.
"""
import sympy as sp

T, kappa, a, A, e, eps0, c, p = sp.symbols('T kappa a A e eps0 c p', positive=True)

alpha1 = 2 * T**2 / (kappa * a)
hbar = sp.pi * T * A**2 / (2 * c)
alpha2 = e**2 / (4 * sp.pi * eps0 * hbar * c)


def dln(expr, var):
    return sp.simplify(sp.diff(sp.log(expr), var) * var)


def main():
    # ---- B1: the static locking identity, and its calibration closure ----------
    lock = sp.Eq(kappa * a, sp.simplify(4 * sp.pi**2 * eps0 * T**3 * A**2 / e**2))
    # alpha1 == alpha2  <=>  lock, verified:
    assert sp.simplify(alpha1.subs(kappa, sp.solve(lock, kappa)[0]) - alpha2) == 0
    print("B1a  the chains agree iff  kappa*a = 4 pi^2 eps0 T^3 A^2 / e^2  (symbolic)")
    # Calibration closure: substitute A^2 = 2 hbar_meas c/(pi T) (ELEC-054 readback)
    # and kappa*a = 2 T^2/alpha_meas (chain-1 calibration). The identity becomes
    # e^2 = 4 pi eps0 hbar_meas c alpha_meas — i.e. the DEFINITION of alpha. Zero
    # static content: it cannot fail numerically at present calibration.
    hbar_m, alpha_m = sp.symbols('hbar_m alpha_m', positive=True)
    lhs = (2 * T**2 / alpha_m)                       # kappa*a at calibration
    rhs = 4 * sp.pi**2 * eps0 * T**3 * (2 * hbar_m * c / (sp.pi * T)) / e**2
    closed = sp.simplify(sp.solve(sp.Eq(lhs, rhs), e**2)[0])
    assert sp.simplify(closed - 4 * sp.pi * eps0 * hbar_m * c * alpha_m) == 0
    print("B1b  at calibration the identity reduces to e^2 = 4 pi eps0 hbar c alpha")
    print("     -- the DEFINITION of alpha. CALIBRATION-CLOSED: zero static content,")
    print("     stated per the locked bar. The identity is live only in DRIFT.")

    # ---- B2: drift consistency, E1 branch (e^2/eps0 c drift-inert) --------------
    # Treat T, kappa, a, A as independent drift channels; equal d ln alpha for all
    # drifts iff the differential of the locking identity holds:
    dT, dK, dAa, dAmp = sp.symbols('dT dK dAa dAmp')  # d ln T, d ln kappa, d ln a, d ln A
    dln_alpha1 = 2*dT - dK - dAa
    dln_alpha2 = -dT - 2*dAmp            # from alpha2 ~ 1/(T A^2), e/eps0/c inert
    condition = sp.Eq(dK + dAa, 3*dT + 2*dAmp)
    diff_lock = sp.simplify(dln_alpha1 - dln_alpha2)      # = 3dT + 2dAmp - dK - dAa... sign
    assert sp.simplify(diff_lock - (3*dT + 2*dAmp - dK - dAa)) == 0
    print("B2   drift consistency (E1):  d ln kappa + d ln a = 3 d ln T + 2 d ln A")
    print("     -- exactly the differential of the B1 identity; under it the two")
    print("     chains give IDENTICAL d ln alpha for arbitrary drifts.")

    # ---- B3: PRED-003's channels under the joint corpus -------------------------
    G = 1 / (T * a)  # ASSUMED form, carried as such (PRED-003's own caveat)
    # Tension channel: kappa, a fixed (dK = dAa = 0) => 0 = 3dT + 2dAmp
    dAmp_T = sp.solve(condition.subs({dK: 0, dAa: 0}), dAmp)[0]
    assert dAmp_T == -sp.Rational(3, 2) * dT
    ratio_T = sp.simplify(dln_alpha1.subs({dK: 0, dAa: 0}) / (-dT))  # dlnG = -dT
    assert ratio_T == -2
    print("B3a  TENSION channel: consistency FORCES d ln A = -(3/2) d ln T")
    print("     (A ~ T^(-3/2), equivalently hbar ~ T^(-2)); the -2 ratio SURVIVES.")
    # Spacing channel: T, kappa fixed (dT = dK = 0) => dAa = 2 dAmp
    dAmp_a = sp.solve(condition.subs({dT: 0, dK: 0}), dAmp)[0]
    assert dAmp_a == sp.Rational(1, 2) * dAa
    ratio_a = sp.simplify(dln_alpha1.subs({dT: 0, dK: 0}) / (-dAa))  # dlnG = -dAa
    assert ratio_a == 1
    print("B3b  SPACING channel: consistency FORCES d ln A = (1/2) d ln a")
    print("     (A ~ a^(1/2)); the +1 ratio SURVIVES. PRED-003's scope test stands,")
    print("     each channel now carrying a derived amplitude co-drift condition.")

    # ---- B4: E2 branch, medium-borne coupling e^2 ~ T^p --------------------------
    # dln_alpha2 gains +p*dT; tension-channel condition generalizes:
    dAmp_p = sp.solve(sp.Eq(2*dT, (p*dT - dT - 2*dAmp)), dAmp)[0]
    assert sp.simplify(dAmp_p - (p - 3)/2 * dT) == 0
    print("B4   E2 branch (e^2 ~ T^p): tension channel needs d ln A = (p-3)/2 d ln T;")
    print("     E1 is the p = 0 case. p is NOT chosen: linking quantizes charge")
    print("     (GG-006) but does not derive the coupling magnitude -- flagged.")

    # ---- R4: the a-vs-w identification -------------------------------------------
    print("R4   chain 2 contains NEITHER the lattice scale a NOR the ambient spacing")
    print("     w: no conflation is possible on the hbar side. Chain 1's 'a' is the")
    print("     lattice scale; the audit introduces no dependence on w anywhere.")

    # ---- B5: verdict, mechanical --------------------------------------------------
    print("B5   VERDICT: CONSISTENT-BY-LOCKING. One identity (live in drift only),")
    print("     two channel-conditional amplitude scalings handed to ELEC-054 as")
    print("     boundary conditions. PRED-003's tier UNCHANGED per rule R1; its")
    print("     provisional list gains the amplitude co-drift condition.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
