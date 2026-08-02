"""ELEC-027 (Modeled): THE REPARAMETERIZATION LEVER -- THE ZIG-ZAG IS
CURED AND PER-STEP PROGRESS RISES 47x, BUT THE CONSTRAINT EATS THE
GAIN. B2 passed, B3 failed and is kept, and the split between them is
the finding.

(1) B1, THE CURVATURE SPECTRUM (a new measurement): probing all 193
    coordinates gives H_ii from 1.10e1 to 1.68e4 -- a RAW-CHART
    CONDITIONING OF 1535x. Sorted by Fourier mode order the medians
    scale as roughly k^1.33 (k=1: 7.6e1, k=16: 3.1e3, a ratio of 40x),
    far milder than the k^2 or k^4 one might guess. MODE ORDER
    EXPLAINS ONLY 40 OF THE 1535: most of the spread is WITHIN mode
    order, set by which curve and which spatial direction a
    coefficient moves -- the clasp and the loop have wildly different
    stiffnesses, and no mode-order preconditioner can see that.

(2) B2 PASSED: with the diagonal coordinate change y = z/sqrt(H_ii),
    the valley anisotropy falls from 108.6x to 14.5x -- a 7.5x
    improvement, so a substantial part of ELEC-026's ill-conditioning
    IS a chart artifact, and the untried lever does move.

(3) B3 FAILED AND IS KEPT: head-to-head at equal wall-clock, the best
    clamped preconditioner gives 1.90x against a bar of 10x --
    essentially ELEC-026's 1.58x, from a completely different
    mechanism.

(4) THE SPLIT, which is the real result: per STEP the preconditioned
    descent is transformed -- dE/step rises from 7.7e-6 to 3.7e-4
    (47x) and the zig-zag is CURED (mean cos(step_i, step_i+1) goes
    from -0.284 to +0.887, i.e. from anti-correlated to coherent).
    The wall-clock gain evaporates because each preconditioned step
    pushes harder into the contact manifold, and the restoration
    projection needed to stay feasible costs an order of magnitude
    more than the step it rescues.

DIAGNOSIS AND CURE, named: the preconditioner conditions the ENERGY
but ignores the CONSTRAINT, so it aims steps into the wall. The
matching instrument is a constraint-aware metric -- the preconditioner
projected onto the active tangent space, or an SQP whose quadratic
model and constraint linearization share the same metric.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'ELEC027_state.npz')
    assert float(s['floor']) < 1e-9, "floor measured first"
    # B1: the spectrum
    H = s['H']; mode = s['mode']
    assert float(s['cond_raw']) > 1000, "raw-chart conditioning 1535x"
    r_mode = np.median(H[mode == 16])/np.median(H[mode == 1])
    assert 20 < r_mode < 80, "mode-order scaling ~k^1.33 explains only 40x of 1535x"
    # B2 passed: the lever moves
    assert float(s['a_raw']) > 80 and float(s['a_pre']) < 25, \
        "B2 PASS: anisotropy 108.6 -> 14.5 (7.5x): partly a chart artifact"
    # B3 failed and kept
    sp = float(s['best_speedup'])
    assert 1.0 < sp < 10.0, "B3 FAILED AND KEPT: 1.90x against a 10x bar"
    # the split: per-step transformed, zig-zag cured
    assert float(s['dE_step_pre'])/float(s['dE_step_raw']) > 20, "47x more descent PER STEP"
    assert float(s['cos_raw2']) < 0 < float(s['cos_pre2']), \
        "the zig-zag is CURED: cos goes from -0.284 to +0.887"
    print(f"cond {float(s['cond_raw']):.0f}x (mode order only {r_mode:.0f}x); anisotropy "
          f"{float(s['a_raw']):.0f}->{float(s['a_pre']):.1f}; speedup {sp:.2f}x; "
          f"per-step {float(s['dE_step_pre'])/float(s['dE_step_raw']):.0f}x; "
          f"cos {float(s['cos_raw2']):+.2f}->{float(s['cos_pre2']):+.2f}")
    print("PASS: the lever moves (B2) but does not pay (B3) -- the coordinate change conditions")
    print("      the energy and ignores the constraint, aiming its better steps into the wall.")


if __name__ == "__main__":
    test()
