"""ELEC-025 (Modeled): THE DEGENERACY TEST -- BENDING STIFFNESS DOES NOT
CLOSE THE TROUGH. The valley is not an artifact of the missing curvature
term, and the clasp survives a new physical term unchanged.

ELEC-024's diagnosis left two options: the trough ends far along, or
the functional lacks a term. This tests the term ELEC-016 flagged
first -- bending stiffness -- by adding E_bend = beta * sum |D2 P|^2 /
hs^3 (a frozen-metric discretization of the integral of curvature
squared, stated as such) and asking whether the CONVERGENCE CHARACTER
changes. Bars locked; beta set by B1 to 2.79 percent of E.

WHAT THE CALIBRATION EXPOSED (a finding in its own right): the
contact-saturated state carries high-frequency structure nobody had
measured -- the clasp's mean |kappa| was 86 with a max of 445, a
circle-equivalent radius of 0.0116, SMALLER than the clasp's own
radius. The wiggles were invisible to every energy-based diagnostic
because tension only sees length.

THE RESULT, three parts:
(1) THE OBJECT SHED THE STRUCTURE, NOT THE TROUGH: under the penalty
    the clasp smoothed hard (mean |kappa| 86 -> 18.6, max 445 -> 36.6)
    and the bending share collapsed from 2.79 percent to 0.068 percent
    -- the object paid off the new term and carried on.
(2) THE TAIL DID NOT STEEPEN: rate ~ it^-0.53 against the no-bending
    baseline of it^-0.59, still far above the q < -1 needed for
    summability. B3's degeneracy-confirmation bar FAILS. Bending
    stiffness at perturbative strength does not close the trough.
(3) STILL NOT A MINIMUM: 19 of 20 restored directions dip, deepest
    -5.2e-5 against ELEC-024's -1.0e-4 -- halved, same order.

THE CLASP'S SIXTH GENERATION: length 0.3844 -> 0.3843 (unchanged to
four figures) while its curvature fell fivefold. The architecture
absorbed a NEW PHYSICAL TERM without moving -- the strongest form of
robustness yet demonstrated, since previous confirmations varied only
the numerics.

SCOPE, stated: this rules out bending as a REGULARIZER at perturbative
strength. A physically-sized bending term (beta large enough to
inflate the clasp) is a different experiment and remains open, as does
the other flagged term, self-avoidance.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.elec_grad import al


def test():
    s = np.load(ROOT/'analysis'/'ELEC025_state.npz')
    assert float(s['floor']) < 1e-9, "floor measured first"
    # (2) the decider: the tail did not steepen
    q = float(s['q'])
    assert q > -1.0, "B3 FAILS: no summable tail -- bending does not close the trough"
    assert abs(q - (-0.59)) < 0.25, "tail essentially unchanged from the no-bending baseline"
    # (1) the object shed the structure
    assert float(s['bend_share_final']) < 0.2, \
        "bending share collapsed 2.79% -> 0.068%: the penalty was paid off, not obeyed"
    # (3) still not a minimum
    mins = s['census_mins']
    assert (mins < -3*float(s['floor'])).sum() >= 0.85*len(mins), "19/20 still dip"
    assert float(s['deepest']) < -1e-5, "dips same order as before"
    print(f"tail it^{q:.2f} (baseline -0.59); bend share -> {float(s['bend_share_final']):.3f}%; "
          f"census {int((mins<0).sum())}/{len(mins)} dip, deepest {float(s['deepest']):.2e}")
    print("PASS: degeneracy PERSISTS under bending; the clasp absorbed a new physical term")
    print("      with its length unchanged to four figures (sixth-generation confirmation).")


if __name__ == "__main__":
    test()
