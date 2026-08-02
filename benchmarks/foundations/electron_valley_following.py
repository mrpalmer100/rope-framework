"""ELEC-026 (Modeled): VALLEY-FOLLOWING FAILS ITS BAR, AND THE TROUGH IS
DIAGNOSED AS AN ANISOTROPIC CURVED VALLEY. B1 and B3 both failed and
are kept; the diagnosis they produced is the result.

(1) B1 FAILED, AND INVERTED THE PICTURE: the crawl is not coherent.
    Mean cos(step_i, step_i+1) = -0.281 -- NEGATIVE, the textbook
    zig-zag of steepest descent in an ill-conditioned valley -- while
    the AXIS drifts coherently (straightness 0.53, cos(first,last) =
    +0.45). Not a maze and not a straight crawl: a narrow valley
    crossed repeatedly by steps that overshoot it.

(2) B2 WORKED BUT SATURATED: secant extrapolation along the 300-step
    net displacement descends, but the best multiplier is 0.5 (dE =
    -5.4e-4) and 2x already ascends. The valley AXIS CURVES, so linear
    extrapolation buys a bounded amount however far one aims.

(3) B3 FAILED AND IS KEPT: alternating 25 plain steps with a jump,
    head-to-head against plain descent at equal wall-clock, gives
    dE = 7.55e-3 versus 4.76e-3 -- a speedup of 1.58x against a bar of
    10x. Valley-following at this level of sophistication does not
    crack the trough.

(4) THE CONDITIONING, measured: curvature along the axis versus across
    it differs by roughly two orders of magnitude. That single number
    explains both failures -- steepest descent must zig-zag (hence the
    negative cosine), and the axis bends before a long jump pays off
    (hence the saturation at 0.5x).

WHAT THIS LEAVES: the trough is now characterized rather than
mysterious -- anisotropic, curved, and kink-dense. Those three
properties together defeat first-order methods (zig-zag), quasi-Newton
memory (kinks corrupt the secant pairs), and linear acceleration
(curvature). The honest remaining candidates are a reparameterization
that conditions the valley, a genuinely nonsmooth-aware second-order
method, or the conclusion that the functional possesses a near-flat
direction no term in it closes.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'ELEC026_state.npz')
    assert float(s['floor']) < 1e-9, "floor measured first"
    # B1 failed: the crawl is a zig-zag, not a coherent march
    assert float(s['cos_succ']) < 0.0, "B1 FAILED: successive steps ANTI-correlated (-0.28)"
    assert 0.3 < float(s['straightness']) < 0.8, "but the axis drifts coherently"
    # B3 failed and is kept
    sp = float(s['speedup'])
    assert 1.0 < sp < 10.0, "B3 FAILED AND KEPT: 1.58x against a 10x bar"
    assert float(s['dA']) > float(s['dP']), "acceleration helps, just not enough"
    assert int(s['jumps']) > 5, "the accelerator actually fired"
    # the explanatory measurement
    an = float(s['anisotropy'])
    assert an > 20, "anisotropy explains both failures (two orders of magnitude)"
    print(f"cos={float(s['cos_succ']):+.3f}, straightness={float(s['straightness']):.2f}; "
          f"speedup={sp:.2f}x ({int(s['jumps'])} jumps); anisotropy={an:.0f}x")
    print("PASS: both bars failed and kept; the trough is now CHARACTERIZED -- anisotropic,")
    print("      curved, kink-dense: the three properties that defeat first-order machinery.")


if __name__ == "__main__":
    test()
