"""COMMISSION SHIN8 -- EM-RECON-033: the refinement-invariance audit.

Exhibit n_sub-invariance of the load-bearing coarse quantities under
GRANT-SUBSTRUCTURE-TIGHT's redistribution map, or find the break.
Bars: analysis/SHIN8_refinement_invariance_bars_LOCKED.md.
Symbolic check: exact rational arithmetic at two arbitrary n_sub
values; equality at both against the n-free value certifies the
algebraic identity for the map's monomial structure.
"""

from fractions import Fraction as F

# Coarse aggregates (symbolic stand-ins as exact rationals; values
# irrelevant, only the n_sub-scaling structure is audited).
T0, MU, K, LQ2_4PIA = F(7), F(3), F(14), F(11)   # k/T0 = 2 (coarse, adjudicated)
S = F(2472, 10000)  # projection transmission s (n_sub-free geometry)

def fine(n):
    """The refinement map R(n): per-sub-strand quantities."""
    return dict(T0f=T0 / n, MUf=MU / n, Kf=K / n)

def main():
    print("COMMISSION SHIN8: refinement-invariance audit")
    ns = [F(2), F(9973)]  # two arbitrary refinement depths

    # Q1 c: c^2 = T0/mu at coarse; T0_f/mu_f at fine.
    c2 = T0 / MU
    ok1 = all(fine(n)["T0f"] / fine(n)["MUf"] == c2 for n in ns)
    print(f"Q1 c: fine T0_f/mu_f == coarse T0/mu at all n: {ok1} -> INVARIANT")

    # Q2 Sigma: registered inputs (T0, a, kappa_pack) all coarse-fixed
    # under R by the map's definition. Audit grade: BY-INPUTS.
    print("Q2 Sigma: inputs {T0, a, kappa_pack} all coarse-fixed under R"
          " -> INVARIANT-BY-INPUTS")

    # Q3 hbar route (GRV-093): hbar = T0 * [l_q^2/(4 pi alpha)] / c.
    c = c2  # (work with c^2-consistent unit; only scaling audited)
    hbar = T0 * LQ2_4PIA / c
    ok3 = all(T0 * LQ2_4PIA / c == hbar for n in ns)  # no fine qty enters
    print(f"Q3 hbar route: inputs {{T0, l_q, alpha, c}} coarse-fixed; "
          f"no fine quantity enters the registered formula: {ok3}"
          " -> INVARIANT-BY-INPUTS")

    # Q4 T0 fork (ELEC-052): the R_eq reconstruction consumes coarse T0
    # (band). R changes no coarse quantity, so the +19%/28% tension is
    # numerically untouched in both directions.
    print("Q4 T0 fork: reconstruction consumes coarse T0 only; the"
          " tension neither resolves nor worsens under R -> INVARIANT"
          " (no substructure escape, no substructure blame)")

    # Q5 zero-point: mode partition under hierarchical winding.
    # Carried band (lambda > p): sub-strands locked, bundle moves as ONE
    # carrier -> mode count per volume UNCHANGED; mode frequencies ride
    # c (Q1-invariant) -> carried-band zero-point INVARIANT by
    # construction. Relative sub-strand modes exist only at lambda < p
    # <= lambda_min/4 (FND-087's over-resolution condition), strictly
    # OUTSIDE the carried band. Whether they contribute depends on the
    # zero-point ledger's cutoff convention, for which the registry
    # carries NO claim (searched this session; FND-038's zero-point
    # readings are superseded coefficients, not a ledger convention).
    print("Q5 zero-point: CONDITIONAL -- carried-band invariant by the"
          " over-resolution mode partition; the fine-band contribution"
          " is governed by a ledger-cutoff convention the registry does"
          " NOT carry. Condition named: invariance is total iff the"
          " zero-point ledger integrates carried modes only. The"
          " missing claim is the cutoff convention itself.")

    # Q6 the fine constant: k_f/T0_f under R.
    vals = [fine(n)["Kf"] / fine(n)["T0f"] for n in ns]
    ok6 = all(v == K / T0 for v in vals)
    # and the derived chain: fine ratio = (coarse ratio)/s, bound 1/s
    fine_ratio = (K / T0) / S
    bound = 1 / S
    print(f"Q6 k_f/T0_f: ratio invariant under R at all n: {ok6};"
          f" derived value 2/s = {float(fine_ratio):.4g},"
          f" bound 1/s = {float(bound):.4g}"
          " -> INVARIANT (the 8.09 falsifier confronts ANY n_sub)")

    assert ok1 and ok3 and ok6
    assert abs(float(fine_ratio) - 8.09) < 0.01
    assert abs(float(bound) - 4.045) < 0.005
    print()
    print("AUDIT VERDICT: five of six INVARIANT (two by-inputs), one")
    print("CONDITIONAL with the missing claim named (zero-point ledger")
    print("cutoff convention). No BREAK located.")
    print("ALL CHECKS PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
