"""NUC-012 (Modeled; partial, weak): THE DIFFUSE SURFACE HELPS BY ONLY
TEN PERCENT -- the right sign, a measured parameter, and far too small
to close NUC-006's gap.

THE PARAMETER IS MEASURED, NOT FITTED. Nuclear saturation density
0.17 fm^-3 gives 5.88 fm^3 per nucleon and an fcc nearest-neighbour
spacing of 2.03 fm. The measured surface diffuseness of 0.54 fm is
therefore 0.267 of a spacing, which in the model's lattice units
(NN = 0.7071) is a_diff = 0.1884. Nothing was tuned.

THE IMPLEMENTATION. Each lattice site is occupied with probability
p(r) = 1/(1 + exp((r-R)/a_diff)), with R set so the occupations sum to
N, and the energy evaluated in mean field as E = (1/2) p^T V p with V
the same Yukawa-plus-contact-core potential. The sharp-edge case is the
same expression with a_diff = 0, where p is 0/1 and the mean field is
exact.

THE RESULT:
    SHARP   a_V = 9.169, a_S = 26.018, ratio = 2.837, R^2 = 0.9139
    DIFFUSE a_V = 8.092, a_S = 21.655, ratio = 2.676, R^2 = 0.9373
The diffuse surface lowers BOTH coefficients, lowers the surface one
proportionally more, improves the fit, and moves the ratio toward the
empirical 1.16 -- but closes only 10 PERCENT of the gap, against
37 percent from NUC-011's relaxation.

COMBINED ESTIMATE, flagged as an estimate. Applying the diffuse factor
(0.943 on the ratio) to NUC-011's relaxed 2.007 gives 1.893, still
63 percent above 1.16. THE TWO MECHANISMS WERE NOT RUN JOINTLY, so this
multiplicative combination is an approximation and not a computed
result.

A METHOD CAVEAT, recorded. The per-N energies are not monotone (N = 43
and 55 invert), because an fcc droplet has geometric shell closures
that a smooth N^(-1/3) fit cannot follow. R^2 sits at 0.91-0.94, which
is adequate for a ratio but not for precision work; a larger and denser
N-ladder would be needed before quoting these coefficients as
measurements.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'NUCS002_state.npz')
    # the parameter is a conversion of a measurement
    sp = float(s['spacing']); al = float(s['a_lat'])
    assert 1.9 < sp < 2.2, "fcc spacing 2.03 fm from saturation density"
    assert abs(al - 0.54/sp*0.70710678) < 1e-6, "a_diff is 0.54 fm converted, not fitted"
    assert 0.15 < al < 0.25, "a_diff = 0.188 lattice units"
    # the effect: right sign, small size
    r0, r1 = float(s['rat0']), float(s['rat1'])
    assert r1 < r0, "the diffuse surface LOWERS the ratio"
    assert abs(r1 - 1.16) < abs(r0 - 1.16), "toward the empirical value"
    closed = (r0 - r1)/(r0 - 1.16)
    assert 0.05 < closed < 0.20, "but only ~10 percent of the gap"
    assert closed < 0.37, "weaker than NUC-011's relaxation"
    # both coefficients fall, surface proportionally more
    assert float(s['aS1']) < float(s['aS0']) and float(s['aV1']) < float(s['aV0'])
    assert float(s['q1']) > float(s['q0']), "and the fit improves"
    # the combined estimate does not solve it
    assert float(s['combined']) > 1.5, "combined estimate 1.893 still far above 1.16"
    print(f"a_diff {al:.4f} (from 0.54 fm / {sp:.2f} fm); ratio {r0:.3f} -> {r1:.3f} "
          f"({closed*100:.0f}% of gap); R^2 {float(s['q0']):.4f} -> {float(s['q1']):.4f}; "
          f"combined estimate {float(s['combined']):.3f} vs target 1.16")
    print("PASS: the diffuse surface is the right sign with a measured parameter, and is")
    print("      far too weak -- 10 percent against relaxation's 37, and 63 percent remains.")


if __name__ == "__main__":
    test()
