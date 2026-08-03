"""ELEC-082: ELEC-054's five dead candidates re-graded against the three derived
amplitude boundary conditions (HBAR-011; PRED-003-XCHAIN, E1 branch).

  BC1  |d ln A/dt| < 1.6e-18 /yr (expansion decoupling)
  BC2  tension channel:  A ~ T^(-3/2)
  BC3  spacing channel:  A ~ a^(1/2)

Bars locked in analysis/ELEC082_candidate_regrade_bars_LOCKED.md. Candidate list
CLOSED (the five of ELEC-054); exponent grading exact-match; every kill conditional
on the E1 branch and said so.
"""
import sympy as sp

T, a, L, Theta = sp.symbols('T a L Theta', positive=True)
w = a / sp.sqrt(3)                      # exact, ELEC-053

REQ_T, REQ_A = sp.Rational(-3, 2), sp.Rational(1, 2)   # BC2, BC3 exponents


def exponents(A_expr):
    """Return (d ln A/d ln T, d ln A/d ln a) for a candidate's A(T, a)."""
    eT = sp.simplify(sp.diff(sp.log(A_expr), T) * T)
    ea = sp.simplify(sp.diff(sp.log(A_expr), a) * a)
    return eT, ea


def main():
    verdicts = {}

    # M1 RELATIVISTIC CEILING: v_max = A*omega <= c, omega = pi c/L  =>  A <= L/pi.
    # A bound on A in terms of the FREE length L; no mechanism fixes A(T, a).
    eT, ea = exponents(L / sp.pi)
    assert (eT, ea) == (0, 0)
    verdicts['M1'] = ("NOT-A-MECHANISM (rule R4). The ceiling constrains, it does "
                      "not select; for the bound to remain saturable under tension "
                      "drift, L itself would have to run as T^(-3/2).")

    # M2 AMPLITUDE = SPACING: A = w = a/sqrt(3).
    eT, ea = exponents(w)
    assert (eT, ea) == (0, 1)
    verdicts['M2'] = (f"FAILS BC2 (T-exponent {eT} vs {REQ_T}) and BC3 (a-exponent "
                      f"{ea} vs {REQ_A}); FAILS BC1 if the spacing comoves. Dead on "
                      "magnitude (60x, ELEC-054) AND now on scaling: overdetermined.")

    # M4 ANHARMONIC TURNING POINT of U = C/w^2 with |C| = T w^2/2 (HBAR-007):
    # departure from harmonic at excursion ~ w, so A ~ w. The T in C cancels
    # against the T in the equilibrium condition; the turning point carries no
    # residual T-dependence.
    eT, ea = exponents(w)   # same scaling as M2 by its own mechanism
    assert (eT, ea) == (0, 1)
    verdicts['M4'] = ("FAILS BC2 (0 vs -3/2) and BC3 (1 vs 1/2), same wall as M2: "
                      "the turning point is pinned to the spacing.")

    # M5 COLLECTIVE COUNT: hbar = n S_1, S_1 = pi T w^2/(2c), n a FIXED integer
    # => A^2 = n w^2 => A = sqrt(n) w. An integer cannot drift continuously.
    n = sp.Symbol('n', positive=True)   # constant
    eT, ea = exponents(sp.sqrt(n) * w)
    assert (eT, ea) == (0, 1)
    # Sharper: under the tension channel M5 forces d ln hbar = +1 d ln T while the
    # joint corpus requires -2 — incompatible outright, not merely untestable.
    hbar_M5 = sp.pi * T * (sp.sqrt(n) * w) ** 2 / 2   # /c omitted; constants inert
    e_hbar_T = sp.simplify(sp.diff(sp.log(hbar_M5), T) * T)
    assert e_hbar_T == 1
    verdicts['M5'] = ("FAILS BC2/BC3 as M2 does, and SHARPER: fixed integer n gives "
                      "d ln hbar = +1 d ln T against the required -2 — the "
                      "collective-count reading is structurally incompatible with "
                      "PRED-003's tension channel (E1). ELEC-054 filed M5 as "
                      "precision-blocked (needs T0 to 1e-4); it is now killed "
                      "conditionally WITHOUT that precision.")

    # M3 THERMAL/EQUIPARTITION: A^2 ~ Theta L / T for a string mode of length L
    # at energy scale Theta (mode stiffness ~ T/L). Free structure: Theta and L
    # are imports. Convert BC2/BC3 into a specification (bar B5):
    A_M3 = sp.sqrt(Theta * L / T)
    # hbar ~ T A^2 ~ Theta L. BC2 (hbar ~ T^-2) => Theta*L ~ T^-2.
    # BC3 (A ~ a^(1/2) at fixed T) => Theta*L ~ a.
    hbar_M3 = sp.simplify(T * A_M3 ** 2)
    assert sp.simplify(hbar_M3 - Theta * L) == 0
    verdicts['M3'] = ("SURVIVES AS A SPECIFICATION, not a pass: hbar ~ Theta*L "
                      "identically, so the imported product must run as T^(-2) "
                      "under tension drift and as a under spacing drift. The "
                      "thermal reading's vagueness is converted into two exact "
                      "requirements on its import; importing hbar-like structure "
                      "remains importing the answer (ELEC-054's own rule).")

    for k in sorted(verdicts):
        print(f"{k}: {verdicts[k]}\n")

    # B4 THE CLASS RESULT: any mechanism A = (pure number) x w has a-exponent 1.
    kpure = sp.Symbol('k_pure', positive=True)
    eT, ea = exponents(kpure * w)
    assert (eT, ea) == (0, 1) and ea != REQ_A
    print("B4 CLASS RESULT: every mechanism of the form A = (pure number) x w")
    print("   fails BC3 (a-exponent 1 vs 1/2) and BC2 (0 vs -3/2). CONSEQUENCE,")
    print("   reported per rule R5 and it cuts AGAINST the corpus: ELEC-054's")
    print("   registered payoff structure -- 'a mechanism yielding a pure number")
    print("   for A/w would select Sigma from theory' -- is CLOSED on the E1")
    print("   branch. The route to selecting Sigma without polarimetry narrows to")
    print("   mechanisms with genuine T-dependence, none of which are on the list.")

    # Reviewer round (2026-08-02), accepted: verify the GENERALIZED spacing
    # exponent under e^2 ~ T^p * a^q before stating any p-robustness. Spacing
    # channel (dT = 0): chain 1 gives d ln alpha = -d ln a; chain 2 gives
    # q d ln a - 2 d ln A; consistency => d ln A = ((1+q)/2) d ln a.
    q = sp.Symbol('q')
    dAa_gen = sp.solve(sp.Eq(-1, q - 2*sp.Symbol('x')), sp.Symbol('x'))[0]
    assert sp.simplify(dAa_gen - (1 + q)/2) == 0
    print("\nCONDITIONALITY (rule R2, reviewer-sharpened): all BC2 kills hold on")
    print("the E1 branch; a derived p != 0 reopens them (BC2 -> A ~ T^((p-3)/2)).")
    print("BC3 is independent of p WITHIN THE REGISTERED E2 ANSATZ e^2 = e^2(T);")
    print("under a generalized e^2 ~ T^p a^q the spacing exponent becomes (1+q)/2")
    print("(verified above), so an a-dependent coupling shifts BC3 rather than")
    print("removing it -- the M2/M4/M5 spacing failures and the B4 class closure")
    print("hold for q = 0 and must be re-graded if q != 0 is ever derived.")
    print("SCOPE OF THE KILLS: 'no magnitude refinement can resurrect a candidate")
    print("wrong in exponent' holds for the mechanisms AS REGISTERED; adding a")
    print("T-dependent population, a changing coherence domain, a coupling-")
    print("dependent w, or another dynamical scale is a NEW mechanism, not a")
    print("refinement of M2/M4/M5, and enters the corpus by its own bars.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
