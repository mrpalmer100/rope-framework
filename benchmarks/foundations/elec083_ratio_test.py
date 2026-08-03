"""ELEC-083: the A-to-l_q ratio test — the commissioned scale-set vote proven
vacuous, and the non-tautological residue extracted: under the shared-origin
hypothesis, 1/alpha = 2 pi^2 rho^2.

Bars locked in analysis/ELEC083_ratio_test_bars_LOCKED.md BEFORE computation,
with the suspected vacuity recorded in the commission and the numerology guard
armed maximally (rule R2: no candidate constants tested).
"""
import sympy as sp

ALPHA = sp.Rational(72973525693, 10**13)   # 7.2973525693e-3 exact decimal


def b1_vacuity():
    T, a, hbar, c, alpha = sp.symbols('T a hbar c alpha', positive=True)
    A = sp.sqrt(2 * hbar * c / (sp.pi * T))            # ELEC-054's readback
    lq_bound = sp.sqrt(4 * sp.pi * alpha * hbar * c / T)   # ETA: g_min * a
    ratio = sp.simplify(A / lq_bound)
    expected = 1 / sp.sqrt(2 * sp.pi**2 * alpha)
    assert sp.simplify(ratio - expected) == 0
    assert not ratio.has(T) and not ratio.has(a) and not ratio.has(hbar)
    print("B1 PASS  VACUITY CONFIRMED: A/(g_min a) = 1/sqrt(2 pi^2 alpha) exactly --")
    print("         T, a, and hbar c cancel identically. The scale-set vote is DEAD:")
    print("         invariance of the ratio-at-bound is algebra, not evidence.")
    print("         (The calibration-closure trap, caught in the commission.)")


def b2_reframing():
    rho, alpha = sp.symbols('rho alpha', positive=True)
    # Shared origin: A/l_q = rho pure. With A = sqrt(2 hbar c/(pi T)) and
    # alpha = l_q^2 T/(4 pi hbar c) (DICT reduction, eta = 1):
    T, hbar, c = sp.symbols('T hbar c', positive=True)
    A = sp.sqrt(2 * hbar * c / (sp.pi * T))
    lq = A / rho
    alpha_expr = sp.simplify(lq**2 * T / (4 * sp.pi * hbar * c))
    assert sp.simplify(alpha_expr - 1 / (2 * sp.pi**2 * rho**2)) == 0
    print("B2 PASS  THE REFRAMING THEOREM: under the shared-origin hypothesis,")
    print("         alpha = 1/(2 pi^2 rho^2), i.e.  1/alpha = 2 pi^2 rho^2, EXACTLY,")
    print("         independent of T, a, hbar. The fine-structure constant collapses")
    print("         to ONE pure geometric ratio between the corpus's two mesoscopic")
    print("         lengths.")
    rho_req = 1 / sp.sqrt(2 * sp.pi**2 * ALPHA)
    print(f"         rho required by measured alpha: {sp.N(rho_req, 12)}")
    return rho_req


def b3_consistency():
    # Under the hypothesis the two mesoscopic demands are one: g = (A/a)/rho for any
    # a, so ELEC-054's A ~ 60-71 w and ETA's g >= 13-16 are a single statement.
    rho = sp.N(1 / sp.sqrt(2 * sp.pi**2 * ALPHA), 10)
    for name, A_over_w in (("Sigma-route", 59.60), ("lattice-anchored", 70.85)):
        A_over_a = A_over_w / sp.sqrt(3)          # w = a/sqrt(3)
        g = sp.N(A_over_a / rho, 6)
        print(f"B3       [{name}] A/a = {sp.N(A_over_a,5)}  =>  g = {g}")
        # cross-check against ETA's independently computed bounds (13.1 / 15.5):
        target = {"Sigma-route": 13.1, "lattice-anchored": 15.5}[name]
        assert abs(float(g) - target) / target < 0.01, (name, g)
    print("B3 PASS  the hypothesis TIES the two scales (one number rho) without")
    print("         fixing a: ELEC-054's amplitude and ETA's source bound collapse")
    print("         to one demand, mutually consistent at both scale sets by")
    print("         construction (which is B1's algebra seen from the other side).")


def b4_guard(rho_req):
    print("B4       RULE R2 APPLIED: rho_required = %s. NO candidate constants" %
          sp.N(rho_req, 10))
    print("         are tested against it; a mechanism must produce rho BLIND, and")
    print("         only then may 2 pi^2 rho^2 be compared with 137.036. What breaks")
    print("         the degeneracy: any independent determination of a (fixes A/a,")
    print("         hence g) or of the locking kappa (tests kappa = 2T/a).")


def b5_branch():
    print("B5       THE OTHER BRANCH, carried without prejudice: if A and l_q have")
    print("         independent origins, rho is meaningless, alpha is not reducible")
    print("         to one ratio, and the corpus holds two separate mesoscopic")
    print("         mechanisms to find. Nothing in today's algebra selects a branch.")


def main():
    b1_vacuity()
    rho = b2_reframing()
    b3_consistency()
    b4_guard(rho)
    b5_branch()
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
