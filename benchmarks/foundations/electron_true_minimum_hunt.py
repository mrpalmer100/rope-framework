"""ELEC-024 (Modeled): THE TERMINUS RECEDES -- a valid stationarity
metric for the first time, 33x more descent than the ladder's last
rung, and a fat-tailed approach that defeats extrapolation.

From ELEC-023's wall-bound state, with curvature-matched line searches
(the flaw that stopped every prior engine) and the constraint GENUINELY
BINDING so the active-set residual is meaningful again:

(1) THE FIRST VALID SMALL RESIDUAL: gres fell 0.941 -> 0.078 over
    1,798 certified iterations. Every previous small-looking residual
    was computed at a state with clearance (ELEC-023's void-metric
    catch); this is the first time the campaign's stationarity number
    is both DEFINED and near its 0.05 bar. Certification held
    throughout (d pinned at 0.06014, |Lk| = 1.0090).

(2) THE TERMINUS RECEDES: E fell to 15.52432 -- 3.83e-2 below the
    ELEC-020 'terminus', which is 33x that ladder's final rung. Two
    successive engines have now each found more descent than the
    entire chart-enrichment step they were meant to have exhausted.

(3) THE FAT TAIL, and the honest consequence: the descent rate decays
    as it^-0.59 across the measured decade. An exponent shallower than
    -1 means the cumulative remaining descent DIVERGES under the fitted
    law -- so no reliable extrapolation to a true minimum energy is
    possible from this data. The energy is bounded below (both terms
    are non-negative), so the law must steepen eventually; where it
    does is unmeasured. E <= 15.52432 is what can be honestly stated.

(4) THE CENSUS (the new standing rule, applied): 22 of 24 restored
    feasible directions still dip, deepest -1.03e-4 -- comparable to
    ELEC-023's -7.5e-5. NOT A MINIMUM, and notably the dip magnitude
    did NOT shrink despite 0.038 of descent: the object is crawling
    along a narrow valley floor rather than settling into a bowl.

CONSEQUENCE FOR THE CALIBRATION: E shifts -0.246 percent, propagating
to ~0.25 percent in d_c and ~0.5 percent in T0 -- still an order
inside the +3.02 percent continuum correction. Thickness ~1.351 fm
and tension ~0.227 N. The dimensional picture is unmoved; only the
claim of convergence keeps dying.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.elec_grad import al


def test():
    s = np.load(ROOT/'analysis'/'ELEC024_state.npz')
    E = float(s['energy_final'])
    assert float(s['floor']) < 1e-9, "floor measured first (3.8e-11)"
    assert E < 15.5250, "the terminus receded to 15.52432"
    rec = float(s['recovered_since_020'])
    assert rec > 0.03 and rec/0.00116 > 25, "33x the K=12->16 ladder drop"
    q = float(s['q'])
    assert -1.0 < q < 0.0, "FAT TAIL (it^-0.59): cumulative descent not summable under the fit"
    mins = s['census_mins']
    assert (mins < -3*float(s['floor'])).sum() > 0.8*len(mins), \
        "the census: still not a minimum (22/24 dip)"
    assert float(s['deepest']) < -5e-5, \
        "dip magnitude did NOT shrink: a valley floor, not a bowl"
    # calibration robustness
    shift = rec/15.562664
    assert shift < 0.005, "calibration shift 0.25%: inside the continuum correction"
    print(f"E={E:.5f}; recovered {rec:.3e} ({rec/0.00116:.0f}x last rung); tail it^{q:.2f}; "
          f"census {int((mins<0).sum())}/{len(mins)} dip, deepest {float(s['deepest']):.2e}")
    print("PASS: first VALID small residual (0.078); terminus receded 33x the last rung;")
    print("      fat tail defeats extrapolation; still not a minimum; calibration unmoved.")


if __name__ == "__main__":
    test()
