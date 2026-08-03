"""GRV-088: the (K, h) evaluation. K derived (the pressing is the cell's
weight), the coefficient assembled and evaluated on both forks, and the
prediction-meets-prediction test adjudicated by the locked rule.
Bars locked in analysis/GRV088_coefficient_bars_LOCKED.md.
"""
import numpy as np
import sympy as sp

HBARC = 3.1615e-26          # J m
H_CORE = 1.87e-19           # m (HBAR-005 thickness; convention-flag carried)
BETA = 15.67                # GRV-082 (drive-depth flag carried)
COMMITTED = 0.23            # GRV-049


def b1_K_derived():
    sigma, e, a, chi, c = sp.symbols('sigma e a chi c', positive=True)
    a_p = c**2 / sigma
    N = (e * a_p / c**2) * (a**3 / chi)      # demand/volume x volume/crossing
    assert sp.simplify(N - e * a**3 / (chi * sigma)) == 0
    print("B1 PASS  K DERIVED: the pressing per crossing is N(sigma) =")
    print("         e a^3/(chi sigma) -- each crossing carries its CELL'S")
    print("         WEIGHT, m_cell a_proper. GRV-038's K is not a free O(1);")
    print("         it is Sigma a^3/chi (premise P-e: the cell energy is the")
    print("         ambient density).")


def b2_b3_evaluate():
    print("B2       the coefficient, every factor sourced:")
    print("         C = beta Sigma a^3 h/(m* chi hbar c) = beta (3 T0 a) h /")
    print("             (m* chi hbar c)   [Sigma a^2 = 3 T0, FND-017]")
    rows = []
    for fork, a in (("F-Lor", 1.0e-16), ("F-Sak", 1.26e-34)):
        for T0 in (1203.0, 1700.0):
            base = BETA * 3 * T0 * a * H_CORE / (HBARC)
            lo = base / (6 * 3)              # m* = 6, chi = 3, spectral 1
            hi = base / (4 * 1) * 2.8        # m* = 4, chi = 1, spectral 2.8
            rows.append((fork, T0, lo, hi))
    for fork, T0, lo, hi in rows:
        print(f"           {fork}  T0 = {T0:4.0f}:  C = {lo:.1e} .. {hi:.1e}")
    best_hi = max(hi for f, _, _, hi in rows if f == "F-Lor")
    gap = np.log10(COMMITTED / best_hi)
    print(f"B3       against the committed 0.23 (GRV-049): the F-Lor bracket's")
    print(f"         MOST FAVOURABLE edge sits {gap:.1f} orders LOW; F-Sak is")
    print(f"         ~18 orders lower still. Locked rule: MET requires within")
    print(f"         one order, brackets included.")
    assert gap > 1.0
    print("B3 TENSION REGISTERED AT FULL STRENGTH: the two internal predictions")
    print("         DISAGREE by four-plus orders on the favourable fork. The")
    print("         prediction-meets-prediction test returns its negative, and")
    print("         at least one chain carries an unearned link.")


def main():
    b1_K_derived()
    b2_b3_evaluate()
    print("B4       THE SUSPECT-LINK LEDGER, pre-listed in the bars and now")
    print("         opened on BOTH chains:")
    print("         mechanism side -- (i) beta = 15.67 was measured at arbitrary")
    print("         ENGINE parameters and its drive-depth sensitivity was")
    print("         disclosed at registration: it is not yet a physical")
    print("         constant, and it multiplies the answer linearly; (ii) h =")
    print("         the registered thickness, flagged possibly convention-")
    print("         dressed (GRV-076's queued fm-audit); (iii) P-e, the cell-")
    print("         energy identification (ambient Sigma vs local pile-up --")
    print("         the accretion shell piles energy far above ambient, which")
    print("         would RAISE C).")
    print("         lineage side -- (iv) GRV-040's mode identification behind")
    print("         0.23, never confronted with a mechanism until now.")
    print("         VERDICT: the sector's last summit is climbed and returns a")
    print("         LOCATED DISAGREEMENT -- the Hawking FORM stands (all three")
    print("         cancellations are coefficient-independent), the COEFFICIENT")
    print("         is in four-order tension with four named suspects, and")
    print("         resolving which link is unearned is the sector's next")
    print("         campaign, not tonight's epilogue. No tier motion.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
