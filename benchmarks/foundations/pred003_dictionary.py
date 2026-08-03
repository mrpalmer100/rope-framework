"""PRED-003-DICT: the Maxwell-sector dictionary evaluated by impedance reduction.

Registered inputs only: OPT-006 (Z_med = sqrt(T mu) = T/c, Derived), EM-002
(Z0 = sqrt(mu0/eps0), c^2 = 1/(mu0 eps0), Derived), plus exact Maxwell algebra.
Bars locked in analysis/PRED003_DICT_bars_LOCKED.md BEFORE computation.
Rule R1: nothing chosen to hit the CONST target; rule R2: contradictions with
CONST's triple registered at full volume.
"""
import sympy as sp

T, kappa, a, c, hbar, q, Z, eps, lam, mu = sp.symbols(
    'T kappa a c hbar q Z eps lam mu', positive=True)


def b1_permittivity():
    # Maxwell identity: alpha = q^2/(4 pi eps hbar c); with eps = 1/(Z c):
    alpha_def = q**2 / (4 * sp.pi * eps * hbar * c)
    alpha_Z = q**2 * Z / (4 * sp.pi * hbar)
    assert sp.simplify(alpha_def.subs(eps, 1 / (Z * c)) - alpha_Z) == 0
    # Medium: Z_med = sqrt(T mu) with mu = T/c^2 (OPT-006) => Z_med = T/c
    Z_med = sp.sqrt(T * (T / c**2))
    assert sp.simplify(Z_med - T / c) == 0
    eps_med = sp.simplify(1 / (Z_med * c))
    assert sp.simplify(eps_med - 1 / T) == 0
    print("B1 PASS  alpha = q^2 Z/(4 pi hbar) verified against the definition;")
    print("         Z_med = T/c (OPT-006, Derived)  =>  eps_med = 1/T:")
    print("         THE MEDIUM'S PERMITTIVITY IS THE INVERSE TENSION.")


def b2_reduction():
    l_q, l_lock = sp.symbols('l_q l_lock', positive=True)
    # alpha in the medium: source strength carries LENGTH units (CHAIN B1's
    # dimensional structure): alpha = l_q^2 * (T/c) / (4 pi hbar) = l_q^2 T/(4 pi hbar c)
    alpha_med = l_q**2 * T / (4 * sp.pi * hbar * c)
    # CHAIN's target: e^2/(4 pi eps0) = 2 lam J a  <=>  alpha = 2 lam J a/(hbar c),
    # J = T^2/kappa. Equate:
    J = T**2 / kappa
    sol = sp.solve(sp.Eq(alpha_med, 2 * lam * J * a / (hbar * c)), l_q**2)[0]
    assert sp.simplify(sol - 8 * sp.pi * lam * (T / kappa) * a) == 0
    # l_lock = T/kappa is a LENGTH: [T/kappa] = (J/m)/(J/m^2) = m. Verified:
    Junit, m = sp.symbols('Junit m', positive=True)
    assert sp.simplify((Junit / m) / (Junit / m**2) - m) == 0
    print("B2 PASS  reduction theorem: alpha = l_q^2 T/(4 pi hbar c), and the CHAIN")
    print("         target collapses to  l_q^2 = 8 pi lam * l_lock * a,  with")
    print("         l_lock = T/kappa the LOCKING LENGTH (units verified). The")
    print("         two-form evaluation reduces to ONE geometric question: what")
    print("         length does a unit winding present as a source?")


def b3_candidates():
    l_lock = T / kappa
    table = [
        ("l_q ~ a",                 a,                     (1, 2, 0),  -1),
        ("l_q ~ sqrt(l_lock * a)",  sp.sqrt(l_lock * a),   (2, 1, -1), -2),
        ("l_q ~ l_lock",            l_lock,                (3, 0, -2), -3),
    ]
    print("B3       corpus-native candidate table (hbar external, G ~ 1/(Ta)):")
    for name, lq, triple, ratio in table:
        alpha_c = sp.simplify(lq**2 * T)          # /(4 pi hbar c) inert for exponents
        pT = sp.simplify(sp.diff(sp.log(alpha_c), T) * T)
        pa = sp.simplify(sp.diff(sp.log(alpha_c), a) * a)
        pk = sp.simplify(sp.diff(sp.log(alpha_c), kappa) * kappa)
        assert (pT, pa, pk) == triple, (name, pT, pa, pk)
        # tension-channel drift ratio with d ln G = -d ln T:
        r = sp.simplify(pT / (-1))
        assert r == ratio
        print(f"         {name:24s} triple {triple}   drift ratio {ratio}")
    print("B3 PASS  three candidates, three fixed scale-free ratios: -1, -2, -3.")
    print("         PRED-003's -2 is the MIDDLE candidate (the geometric-mean source")
    print("         length, l_q^2 = l_lock * a), not the framework's unique value.")


def b4_consequence():
    print("B4       WHAT SURVIVES UNCONDITIONALLY: every candidate gives a FIXED,")
    print("         scale-free alpha-G drift ratio -- the paper's own stated")
    print("         framework-forced content -- and a measured nonzero ratio in")
    print("         {-1, -2, -3} SELECTS the source length: the geometric unknown")
    print("         is an OBSERVABLE. What does not survive: -2 as the unique value.")
    print("         Registered at full volume per rule R2.")


def b5_decision():
    print("B5       THE INTERNAL DECISION, named (rule R3, not answered): the")
    print("         candidate is picked by which registered modulus curves the")
    print("         on-site locking potential -- a J-based curvature gives healing")
    print("         length ~ a (candidate 1); a kappa-based curvature gives ~ l_lock")
    print("         (candidate 3); the mixed normalization gives the geometric mean")
    print("         (candidate 2, the CONST form). Registered claims do not force")
    print("         the choice; the microscopic-mechanics paper's machinery is the")
    print("         bounded venue. No candidate is selected today.")


def main():
    b1_permittivity()
    b2_reduction()
    b3_candidates()
    b4_consequence()
    b5_decision()
    print("B6       PROPAGATION: PRED-003 gains the candidate-dependence of its")
    print("         ratio; CONST's triple is identified as candidate 2; CHAIN's")
    print("         specification is REDUCED (field theory -> one length). No tier")
    print("         motion (rule R4).")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
