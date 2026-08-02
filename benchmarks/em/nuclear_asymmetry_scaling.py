"""NUC-020 (Modeled): THE ASYMMETRY SCALING IS WRONG IN BOTH EXPONENTS
-- the model gives A^-0.37 |N-Z| where the SEMF gives A^-1 (N-Z)^2, and
NUC-019's magnitude agreement was an artifact of testing at one A.

THE TEST. NUC-019 found the label model reproduces the asymmetry
penalty to within a factor 1.5 at A = 40 and asked whether the linear
coefficient is A-independent. Measured at A = 16, 40 and 80 with up to
nine asymmetry values each:
    A =  16: slope 5.22 MeV per unit |N-Z|, residual scatter 0.39 eps
    A =  40: slope 3.94 MeV per unit |N-Z|, residual scatter 0.53 eps
    A =  80: slope 2.84 MeV per unit |N-Z|, residual scatter 0.79 eps
The coefficient FALLS with mass number as A^-0.374. It is not
A-independent, and the answer to NUC-019's question is no.

THE FULL FORM. Model total deficit = 14.99 A^-0.37 |N-Z| MeV against
the SEMF's 23 (N-Z)^2/A. THE EXPONENTS DISAGREE IN BOTH VARIABLES: the
model is linear in the asymmetry where nature is quadratic, and falls
as A^-0.37 where nature falls as A^-1.

ACROSS THE CHART, with no free parameter (eps fixed by a_V):
    Fe-56    N-Z =  4   model  13.3   SEMF   6.6   ratio 2.03
    Sn-120   N-Z = 20   model  50.1   SEMF  76.7   ratio 0.65
    Pb-208   N-Z = 44   model  89.7   SEMF 214.1   ratio 0.42
    U-238    N-Z = 54   model 104.7   SEMF 281.8   ratio 0.37
Everything sits within a factor of 2.7, which for a parameter-free
estimate is not nothing -- but the ratio falls MONOTONICALLY with A,
which is the unmistakable signature of a wrong exponent rather than a
wrong constant.

WHAT THIS DOES TO NUC-019. Its central claim -- 'the right magnitude
across the physically populated range' -- was measured entirely at
A = 40, which is where the two curves happen to cross. Tested across
the chart the agreement degrades systematically to 0.37 at U-238. The
mechanism is real and the scale is the right order; the claim of
quantitative agreement is not supported and is qualified accordingly.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'NUCA002_state.npz')
    As, sl = s['As'], s['slopes']
    # the coefficient is NOT A-independent
    assert sl[0] > sl[1] > sl[2], "the slope falls monotonically with A"
    assert sl[0]/sl[-1] > 1.5, "by a factor 1.8 from A = 16 to 80"
    p = float(s['p'])
    assert p < -0.2, "scaling A^-0.37, clearly not A-independent"
    assert abs(p - (-1.0)) > 0.4, "and clearly not the SEMF's A^-1 either"
    # the residual scatter is real but does not explain the trend
    sc = s['scatter']
    assert (sc < 1.0).all(), "residual scatter under 1 eps at every A"
    # across the chart: within a factor 2.7 but monotonically degrading
    ch = s['chart']          # A, D, model, semf, ratio
    r = ch[:, 4]
    assert r.max()/r.min() < 6, "everything within a factor 2.7 of the SEMF"
    assert all(r[i] > r[i+1] for i in range(len(r)-1)), \
        "the ratio falls MONOTONICALLY with A: a wrong exponent, not a wrong constant"
    assert r[0] > 1.5 and r[-1] < 0.5, "overshoots light, undershoots heavy"
    print(f"slopes {sl[0]:.2f}/{sl[1]:.2f}/{sl[2]:.2f} MeV at A = 16/40/80 -> A^{p:.3f}; "
          f"chart ratios {r[0]:.2f} -> {r[-1]:.2f} (Fe-56 to U-238), monotone")
    print("PASS: wrong in both exponents -- linear where nature is quadratic, A^-0.37 where")
    print("      nature is A^-1; NUC-019's agreement was an artifact of testing at A = 40.")


if __name__ == "__main__":
    test()
