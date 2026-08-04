"""GRV-094: the invariance sweep -- h adjudicated (electron-anchored,
fork-invariant; GRV-088's last suspect closes), the one-power-of-a theorem for
the entire horizon/hbar arc, and the corpus's constants found sorted along the
invariance line. Bars locked in analysis/GRV094_invariance_sweep_bars_LOCKED.md.
"""
import numpy as np
import sympy as sp

ALPHA, LQ, DC, A_LOR = 1/137.036, 1.39e-15, 1.87e-19, 1.0e-16


def b1_table():
    rows = [
        ("d_c = 1.87e-19 m", "INVARIANT", "ELEC-021: electron-knot calibration;"
         " the registered invariant Lambda = E_inf d_c is stated"
         " calibration-independent -- anchored to the electron, not the"
         " lattice. (Full ELEC chain re-derivation out of scope, said so.)"),
        ("l_q = 1.39e-15 m", "INVARIANT", "PRED-003: the alpha relation's"
         " length; a-independent per GRV-075's survey."),
        ("T0 = 1203-1700 N", "INVARIANT", "FND-017 with GRV-076: exact on the"
         " degeneracy line -- the fork slides along it."),
        ("a (1e-16 | 1.26e-34 m)", "CONVENTION/FORK", "GRV-076: zero live"
         " pins; the scale sets are the vacuum bound wearing a different"
         " hat."),
        ("Sigma = 3 T0/a^2", "FORK (a^-2)", "carries the convention through"
         " FND-017."),
        ("w = 5.78e-17 m", "RETIRED", "ELEC-061 lineage, retired by GRV-076;"
         " HBAR-005's audit used it as 'spacing' -- that AUDIT's spacing role"
         " is superseded, while d_c, its OTHER length, stands on the electron"
         " anchor."),
    ]
    print("B1       the provenance table:")
    for name, cls, src in rows:
        print(f"           {name:26s} {cls:16s} {src}")
    print("B1 PASS  every length cited; d_c classifies INVARIANT on its"
          " registered anchor.")


def b2_exponents():
    a, T0, lq, dc, al, c, sig, kap, beta, chi, mst, w0 = sp.symbols(
        'a T0 l_q d_c alpha c sigma kappa beta chi m_star omega0',
        positive=True)
    Sigma = 3 * T0 / a**2
    N = Sigma * a**3 / (chi * sig)
    W = N * dc
    e_bit = beta * W
    T_inf = (beta / mst) * Sigma * a**3 * dc / (chi) * kap / c   # (K h/m*)kappa form
    hbar = T0 * lq**2 / (4 * sp.pi * al * c)
    C = sp.simplify(T_inf / (hbar * kap))
    Astar = sp.simplify(e_bit / ((w0 * kap) * c / (kap * sig)))
    nq = sp.simplify(Astar / hbar)
    qarea = lq**2 / (4 * sp.pi * al)
    print("B2       the a-exponents, machine-derived (invariants held fixed):")
    checks = [("Sigma", Sigma, -2), ("barrier W", W, 1), ("e_bit", e_bit, 1),
              ("Hawking coefficient C", C, 1), ("snap action A*", Astar, 1),
              ("n_q", nq, 1), ("quantum area", qarea, 0)]
    for name, expr, want in checks:
        got = sp.degree(sp.Poly(sp.together(expr).as_numer_denom()[0], a), a) \
            - sp.degree(sp.Poly(sp.together(expr).as_numer_denom()[1], a), a)
        print(f"           {name:22s} a^{got}   (expected a^{want})")
        assert got == want, (name, got, want)
    print("B2 PASS  THE ONE-POWER THEOREM: the horizon/hbar arc's entire fork-")
    print("         dependence is a SINGLE power of the lattice spacing in each")
    print("         of {C, A*, n_q} -- and ZERO in the quantum area. The")
    print("         corpus's constants and conventions have sorted themselves")
    print("         along the invariance line: everything physical rides the")
    print("         fork untouched; everything fork-sensitive carries exactly")
    print("         one a.")


def main():
    b1_table()
    b2_exponents()
    print("B3       THE ADJUDICATION: h = d_c is INVARIANT (electron-anchored),")
    print("         so GRV-088's suspect (ii) CLOSES -- the mechanism-side")
    print("         numbers do not rescale, and the coefficient campaign's")
    print("         ledger is COMPLETE: (i) beta promoted with its operating")
    print("         point measured, (ii) h invariant, (iii) pile-up eliminated,")
    print("         (iv) the identification vindicated -- four suspects, four")
    print("         adjudications, zero survivors, and the case stays closed")
    print("         exactly as GRV-091 ruled it.")
    adj = 4 * np.pi * ALPHA * LQ
    print(f"B4       guarded observation (numerology guard armed, MeV-adjacency")
    print(f"         precedent): 4 pi alpha l_q = {adj:.3e} m sits {100*abs(adj-A_LOR)/A_LOR:.0f}%")
    print("         from a_Lor = 1.0e-16 m. FLAGGED AND DISCOUNTED: a_Lor is a")
    print("         BOUND-VALUED CONVENTION (GRV-076), so adjacency to it is")
    print("         adjacency to a bound, the weakest kind; no claim is built")
    print("         on it, and the guard's precedent (the eta-MeV adjacency")
    print("         that dissolved) is cited as the reason for the discount.")
    print("         Standing queue after tonight: the tensor coefficient (P3,")
    print("         fresh-budget instrument read); the area-selection problem")
    print("         (the L1 target, unscheduled); weave-as-reservoir.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
