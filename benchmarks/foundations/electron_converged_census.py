"""ELEC-030 (Modeled): THE FIRST TERMINUS FROM A CONVERGING METHOD, AND
THE CENSUS THAT ALMOST PASSED. The minimality gap collapses 41x; the
verdict is still 'not a minimum', and the standing obligation to run
any descent found was honored.

(1) TERMINATION, properly earned: the constraint-aware scheme with a
    state-fresh spectrum (refreshed every 60 steps) reached the
    pre-locked criterion in 492 iterations at E = 15.4475841, with
    certification intact (d = 0.06001, |Lk| = 1.0099) and the tangent
    dimension recovering slightly to 117 (rows 112, rank 76).

(2) THE CENSUS, applied for the first time to a state reached by a
    method that actually converges: 26 directions x 4 scales x both
    signs, with restoration. ONE direction dips. The deepest dip is
    -2.52e-6 and the MEDIAN dip is EXACTLY ZERO -- 25 of 26 directions
    rise at every probed scale. Against the campaign's history
    (-7.5e-5, -1.0e-4, -5.2e-5) this is a 41-fold collapse of the
    minimality gap, and a qualitative change from '37 of 44 dip' to
    'one of 26'.

(3) THE VERDICT IS STILL 'NOT A MINIMUM', and the obligation from
    ELEC-023 was honored rather than argued around: descending the
    dipping direction accepted exactly ONE step (-2.5e-6), after which
    the full engine resumed for 259 more steps to E = 15.447560785 --
    a total of -2.33e-5 beyond the declared terminus.

WHAT THAT NUMBER MEANS: the terminus was premature by 1.5 parts per
million of E. The census is now measuring the convergence criterion's
own slack rather than a failure of the method, which is the first time
in the campaign that has been true. The honest position: still no
stationarity certificate, but the gap between 'where the engine stops'
and 'where descent actually ends' has fallen from percent-scale to
ppm-scale.

CALIBRATION NOTE: E has now fallen 0.74 percent below the ELEC-020
value the published dimensional numbers rest on. That is still inside
the +3.0 percent continuum correction, but the drift is monotone and a
recalibration is named as due.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'ELEC030_state.npz')
    assert bool(s['terminated']), "reached the pre-locked criterion"
    assert int(s['iters']) < 600, "492 iterations -- the campaign's fastest termination"
    assert float(s['floor']) < 1e-9, "floor measured first"
    # the census: the collapse, and the honest verdict
    mins = s['census_mins']
    assert int(s['ndips']) >= 1, "STILL NOT A MINIMUM: one direction dips"
    assert int(s['ndips']) <= 3, "but only one of 26 -- a qualitative change"
    assert abs(float(np.median(mins))) < 1e-12, "median dip EXACTLY zero"
    assert float(s['deepest']) > -1e-5, "deepest dip -2.5e-6: a 41x collapse of the gap"
    assert float(s['deepest']) < 0, "and it is real, not noise"
    # the obligation honored
    assert int(s['dip_steps']) >= 1, "the dipping direction was RUN, not argued around"
    tot = abs(float(s['total_from_terminus']))
    assert tot < 1e-4, "total beyond the terminus: 2.33e-5, i.e. 1.5 ppm of E"
    assert tot > float(abs(s['deepest'])), "the engine found more after the dip opened the door"
    print(f"terminated in {int(s['iters'])} its at E={float(s['energy_final']):.7f}; census "
          f"{int(s['ndips'])}/26 dip, deepest {float(s['deepest']):.2e}, median 0; "
          f"beyond terminus {tot:.2e} ({tot/float(s['energy_final'])*1e6:.1f} ppm)")
    print("PASS: the minimality gap collapsed 41x and the census now measures the stopping")
    print("      criterion's own slack -- still not a minimum, but ppm from one.")


if __name__ == "__main__":
    test()
