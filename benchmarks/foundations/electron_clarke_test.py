"""ELEC-035 (Modeled): NOT STATIONARY IN ANY SENSE -- the projected
gradient plateaus, the Clarke test comes back NEGATIVE with adequate
sampling, and the bundle direction is no better than random sweeping.
The landscape is not the obstruction; the search is.

(1) THE ||Pg|| FORK, resolved: across sweep rounds 5-9 the
    tangent-projected gradient reads 0.90, 0.91, 0.61, 1.31, 0.82 --
    mean 0.910, sd 0.228, trend +0.023 per round -- while E fell
    2.9e-5. IT DOES NOT FALL. The full gradient is even steadier
    (6.46, 6.68, 6.52, 6.40, 6.49). Sweep recovery per round declined
    only mildly over nine rounds (~5.5e-6 -> ~2e-6), so the descent is
    slow but persistent, not terminating.

(2) THE CLARKE TEST, and a caught methodological error: the first
    attempt sampled 8 gradients in a 107-dimensional tangent space and
    returned 'not Clarke-stationary' -- a MEANINGLESS verdict, since
    8 points span a 7-dimensional simplex that cannot contain the
    origin regardless of the truth. Generic containment needs at least
    dim+1 = 108. Re-run with 202 usable samples the hull minimum falls
    0.61, 0.39, 0.22, 0.147 and then STOPS (last increment exactly
    zero), plateauing at ratio 0.180 of the base gradient norm.
    VERDICT: NOT CLARKE-STATIONARY. Zero is not in the local
    gradient hull, so the kink structure does NOT bound the gradient
    away from zero and genuine descent remains available.

(3) THE BUNDLE DIRECTION, tested because the hull minimizer IS one:
    a single bundle step recovers -2.4e-7 against a full 16-direction
    random sweep's -3.9e-7, at roughly five times the cost. It works
    and it is not a win.

THE SYNTHESIS with ELEC-033: the tangent curvature is positive-
definite, the state is not stationary smoothly, and it is not
stationary in the Clarke sense either. A genuine local minimum
therefore lies further along, the landscape is benign in both
respects that matter, and the entire remaining obstruction is the
practical one of FINDING efficient descent directions in 107
dimensions where every method tried recovers about the same 1e-6 per
round.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'ELEC035_state.npz')
    log = s['log']
    # (1) the plateau
    assert float(s['pg_slope']) > -0.05, "||Pg|| does NOT fall across rounds"
    assert 0.5 < float(s['pg_mean']) < 1.4, "it oscillates around ~0.9"
    assert float(s['pg_sd']) > 0.1, "with real scatter, not a slow decay"
    assert log[0, 1] - log[-1, 1] > 1e-5, "while E fell 2.9e-5 over the same rounds"
    # (2) the Clarke test, adequately powered
    assert int(s['nG']) > int(s['tangent']), "202 samples > dim+1 = 108: adequately powered"
    ratio = float(s['hull'])/float(s['g0'])
    assert ratio > 0.1, "hull minimum plateaus ABOVE zero: NOT Clarke-stationary"
    assert not bool(s['clarke'])
    assert int(s['nactive']) > 10, "the plateau is supported by many active samples"
    # (3) the bundle direction: works, not a win
    assert float(s['bundle_dE']) < 0, "the bundle step does descend"
    assert abs(float(s['bundle_dE'])) < float(s['sweep_round']), \
        "but recovers less than one random sweep round, at ~5x the cost"
    print(f"||Pg|| mean {float(s['pg_mean']):.3f} sd {float(s['pg_sd']):.3f} slope "
          f"{float(s['pg_slope']):+.3f}; Clarke hull {float(s['hull']):.4f} ratio {ratio:.3f} "
          f"({int(s['nG'])} samples, dim {int(s['tangent'])}); bundle {float(s['bundle_dE']):.2e} "
          f"vs sweep {float(s['sweep_round']):.2e}")
    print("PASS: not stationary smoothly, not stationary in the Clarke sense, curvature")
    print("      positive -- the landscape is benign; finding descent is the whole problem.")


if __name__ == "__main__":
    test()
