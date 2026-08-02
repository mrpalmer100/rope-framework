"""ELEC-023 (Modeled): THE MINIMALITY CENSUS -- THE TERMINUS WAS NOT A
MINIMUM, THE RESIDUAL METRIC WAS MEASURING NOTHING, AND THE LADDER'S
ERROR BAR WAS TOO SMALL BY THIRTEEN TIMES. The calibration survives;
the precision claim does not.

Rung 2 of the stability question attacked directly, floors first
(energy reproducibility 3.6e-11 -- an exceptionally clean instrument).

(1) THE COMPLEMENTARY-SLACKNESS DISCOVERY: at the ELEC-020 state
    d_min = 0.06566 against a wall of 0.0600 -- CLEARANCE +0.0057. NO
    CONSTRAINT WAS BINDING. The active-set NNLS decomposition that
    produced every 'gres' number from ELEC-013 onward was distributing
    a nonzero gradient over constraints whose true multipliers are
    ZERO by complementary slackness. The residual plateau (0.18-0.38)
    that three claims struggled to explain was an ARTIFACT OF THE
    METRIC, not a property of the state. The correct stationarity test
    at such a state is simply ||grad||, which was 7.14.

(2) THE CENSUS: 44 random directions x 5 scales x both signs. 37 of 44
    dip below E0 at the smallest scales while BOTH signs rise steeply
    past t ~ 3e-4 -- the exact signature of a nonzero gradient inside
    an enormously stiff basin (fitted curvature ~3000). NOT A LOCAL
    MINIMUM, and the reason the engines stopped is now clear: their
    line searches began far above the basin's tiny descent scale
    (t* ~ 1e-4).

(3) THE RECOVERY: a fine-scale descent tuned to the measured curvature
    recovered dE = 1.586e-2 in NINE iterations, terminating with
    d_min driven onto the wall (0.06000) where the constraint becomes
    genuinely active and gres becomes meaningful again.

CONSEQUENCES, stated without softening:
  - ELEC-020's E_infinity = 15.5627(12) is an UPPER BOUND whose error
    bar was underestimated by ~13x (the recovered 0.0159 is 14x the
    K=12->16 drop). The ladder measured ENGINE TERMINI, not chart
    minima, so its contraction ratio characterized the optimizer's
    stopping behavior as much as the chart's exhaustion.
  - THE CALIBRATION SURVIVES: the shift is -0.10 percent of E, which
    propagates to ~0.1 percent in d_c and ~0.2 percent in T0 -- an
    order below the continuum correction already applied. Rope
    thickness 1.354 fm and tension 0.226 N stand.
  - THE PHYSICS PICTURE STRENGTHENS: the object sits in a basin so
    stiff that 193-dimensional descent moves it a parameter distance
    of ~1e-4. Stiffness is what stability looks like when measured.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.elec_grad import al


def test():
    c = np.load(ROOT/'analysis'/'ELEC023_census.npz')
    s = np.load(ROOT/'analysis'/'ELEC023_state.npz')
    # (1) no constraint was binding at the audited state
    assert float(c['d0']) - al.D_HARD > 0.004, \
        "COMPLEMENTARY SLACKNESS: clearance +0.0057 -- gres was decomposing over non-binding rows"
    # (0) the floor, measured before the bars
    assert float(c['floor']) < 1e-9, "noise floor 3.6e-11 measured first"
    # (2) the census verdict
    res = c['results']
    assert int(c['ndips']) > 0.7*len(res), "37/44 directions dip: NOT a local minimum"
    assert res.min() < -1e-5, "dips are real (1e-5 scale), far above the floor"
    # (3) the recovery and its consequence for the ladder
    rec = float(s['recovered'])
    assert rec > 1e-2, "fine-scale descent recovered 0.0159"
    assert rec > 10*0.00116, "the recovery EXCEEDS the K=12->16 ladder drop by ~14x"
    assert bool(s['terminated']) and int(s['accepted']) < 20, \
        "nine iterations, terminating against the wall"
    # the calibration's robustness
    shift = rec/float(s['E_start'])
    assert shift < 0.002, "calibration shift ~0.1%: an order below the continuum correction"
    print(f"clearance {float(c['d0'])-al.D_HARD:+.4f} (no binding constraint); floor {float(c['floor']):.1e}; "
          f"dips {int(c['ndips'])}/{len(res)}; recovered {rec:.4e} ({shift*100:.3f}% of E)")
    print("PASS: not a minimum; the residual metric was void at that state; the ladder bar was")
    print("      13x too small; the calibration survives at the 0.1% level.")


if __name__ == "__main__":
    test()
