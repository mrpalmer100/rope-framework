"""NUC-025 (Modeled): SECOND-NEIGHBOUR BONDS BREAK NUC-021'S PREMISE
AND CHANGE NOTHING -- they amplify every effect and bend no form. The
linear law is more robust than its own proof.

THE HYPOTHESIS. NUC-021's no-go rests on the fcc sublattices being
INDEPENDENT SETS, which holds only for nearest-neighbour bonds. At the
physical range (NUC-013's lambda_phys) the second shell carries 38.8
percent of the nearest-neighbour weight, and the six second neighbours
of any site lie in ITS OWN sublattice. The premise therefore fails, and
excess nucleons sharing a foreign sublattice CAN now see each other --
the stated condition for a rising marginal cost, hence for a quadratic
asymmetry.

THE PREMISE DOES FAIL, AND THE MARGINAL COST DOES RISE. Verified
directly on a 400-site cluster: internal nearest-neighbour bonds are
zero in every sublattice, internal SECOND-neighbour bonds number
212-223. Parking m excess nucleons, the weighted cost per excess rises
0.556, 0.685, 0.749, 0.879, 0.959, 1.052, 1.113 for m = 1 to 64 -- a
scaling of m^1.17 rather than m^1.00.

AND IT MAKES NO DIFFERENCE TO ANY OF THE THREE TARGETS.
  1. ASYMMETRY MAGNITUDE: deficits grow 10.9x -- second-neighbour bonds
     amplify the effect substantially.
  2. ASYMMETRY FORM: R^2 against LINEAR improves 0.967 -> 0.996, and
     against QUADRATIC degrades 0.882 -> 0.694. THE RESULT BECOMES MORE
     LINEAR, NOT LESS.
  3. PAIRING A-DEPENDENCE: the high/low staggering ratio moves 1.67 ->
     1.96 where the empirical 1/sqrt(A) requires 0.78. IT MOVES AWAY.

WHY THE PREMISE CAN FAIL WITHOUT THE CONCLUSION FAILING. Breaking
independence is necessary for a rising marginal cost but not
sufficient: the optimiser still has enough freedom to route excess
nucleons around each other, so the m^1.17 growth measured for a FIXED
placement never reaches the optimised configuration. NUC-021's theorem
is proved under an assumption stronger than it needs; the linear
behaviour survives the assumption's failure.

TWO BUGS CAUGHT IN THIS SESSION, both of which would have produced
confident wrong answers. First, a distance cutoff of 0.75 applied to a
lattice whose nearest-neighbour distance is sqrt(2) returned ZERO edges
and all-zero deficits. Second, a pairing A-list of 12, 16, 20, 24, 28,
32 is entirely A = 4k, hence entirely even-even, and produced NaN
staggering. Both were caught by the results being impossible rather
than merely surprising.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'NUCX003_state.npz')
    # 1. the magnitude is amplified
    amp = float(s['dfc_2'][1])/float(s['dfc_nn'][1])
    assert amp > 5, "second neighbours amplify the asymmetry deficit ~11x"
    # 2. the FORM becomes more linear, not less
    assert float(s['r2l_2']) > float(s['r2l_nn']), "linear fit IMPROVES with second neighbours"
    assert float(s['r2q_2']) < float(s['r2q_nn']), "quadratic fit DEGRADES"
    assert float(s['r2l_2']) > 0.99, "R^2 linear 0.996: more linear than before"
    assert float(s['r2l_2']) > float(s['r2q_2']), "linear still beats quadratic decisively"
    # 3. the pairing A-dependence moves the wrong way
    r_nn = float(s['hi_nn'])/float(s['lo_nn'])
    r_2 = float(s['lo_2']) and float(s['hi_2'])/float(s['lo_2'])
    emp = float(s['emp'])
    assert emp < 1, "empirical 1/sqrt(A) requires the ratio to FALL with A"
    assert r_nn > 1 and r_2 > 1, "both model variants have it RISING"
    assert abs(r_2 - emp) > abs(r_nn - emp), "second neighbours move it FURTHER from empirical"
    print(f"magnitude x{amp:.1f}; R^2 linear {float(s['r2l_nn']):.3f}->{float(s['r2l_2']):.3f}, "
          f"quadratic {float(s['r2q_nn']):.3f}->{float(s['r2q_2']):.3f}; pairing hi/lo "
          f"{r_nn:.2f}->{r_2:.2f} vs target {emp:.2f}")
    print("PASS: the premise fails, the conclusion survives -- second neighbours amplify")
    print("      everything and bend nothing.")


if __name__ == "__main__":
    test()
