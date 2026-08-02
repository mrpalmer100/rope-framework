"""ELEC-028 (Modeled): THE CONSTRAINT-AWARE METRIC -- TANGENCY FIXED,
ELEC-027'S DIAGNOSIS REFUTED, AND THE JAMMING MEASURED. B1 passed,
B3 failed and is kept, and two corrections are filed against prior
claims including one against a hypothesis raised inside this session.

THE FIX: ELEC-027 decomposed the gradient in the Euclidean metric and
then rescaled the step by D^2, so its residual was tangent in the wrong
geometry. Doing everything in the transformed coordinates instead --
gradient D g, constraint rows A D, NNLS there, step -D r_y -- makes
the step genuinely tangent in the metric it is taken in.

(1) B1 PASSED DECISIVELY: constraint violation produced per unit step
    falls from 2.25e-4 (ELEC-027's scheme) to EXACTLY ZERO, with the
    tangency measure |A p| dropping tenfold (0.797 -> 0.082).

(2) THE MISMATCHED SCHEME NOW STALLS COMPLETELY: run from this state
    (158 active rows) ELEC-027's direction accepts ZERO steps in 80
    seconds, every trial rejected. The mismatch was real and it
    worsens as the active set grows.

(3) B3 FAILED AND IS KEPT: constraint-aware descent gives 2.25x
    against raw at equal wall-clock, best of the three schemes and far
    below the 10x bar.

(4) ELEC-027'S DIAGNOSIS IS REFUTED BY DIRECT MEASUREMENT: it
    attributed its loss to restoration cost, but instrumenting the
    loop shows rejections per accepted step of 1.57 (raw) versus 1.52
    (constraint-aware) and restorations per step of 2.57 versus 2.52
    -- statistically identical. Restoration was never the bottleneck.
    The constraint-aware scheme wins by doing 2.4x more work per step
    at the same cost per step, not by making steps cheaper.

(5) THE JAMMING MEASUREMENT, a new campaign-scale observable: the
    active-constraint Jacobian has rank 87 of 193 parameters, leaving
    a feasible tangent dimension of 106. Tracked backwards the object
    has been progressively pinning itself -- tangent 193 (ELEC-020,
    pre-wall), 120 (ELEC-024), 127 (ELEC-026), 106 (now). CORRECTION
    TO A HYPOTHESIS RAISED IN THIS SESSION: the tangent space was
    guessed at ~10 dimensions from the raw row count (158 of 193); the
    rank computation gives 106, an order of magnitude larger, so
    JAMMING IS REAL BUT DOES NOT EXPLAIN the collapse in per-step
    gains from ELEC-027's 47x to tonight's 2.4x. That collapse remains
    unexplained and is state-dependence, not geometry, until measured.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'ELEC028_state.npz')
    assert float(s['floor']) < 1e-9, "floor measured first"
    # B1: tangency fixed
    assert float(s['vC']) == 0.0 and float(s['vB']) > 1e-5, \
        "B1 PASS: zero violation vs 2.25e-4 for the mismatched scheme"
    # the mismatched scheme stalls
    assert float(s['dE_mis']) == 0.0 and int(s['n_mis']) == 0, \
        "ELEC-027's direction accepts ZERO steps at this state"
    # B3 failed and kept
    sp = float(s['speedup_ca'])
    assert 1.5 < sp < 10.0, "B3 FAILED AND KEPT: 2.25x against a 10x bar"
    assert float(s['dE_ca']) > float(s['dE_raw']), "best of the three schemes"
    # ELEC-027's diagnosis refuted: restoration cost is the SAME
    assert abs(float(s['rej_ca']) - float(s['rej_raw'])) < 0.2, \
        "restoration cost identical: ELEC-027's 'restoration eats the gain' is REFUTED"
    # the jamming measurement, and the correction to the in-session guess
    assert int(s['rank']) < int(s['m_rows']), "the active Jacobian is rank-deficient"
    assert int(s['tangent']) > 50, \
        "tangent dimension 106, NOT the ~10 guessed mid-session: jamming does not explain it"
    print(f"violation {float(s['vB']):.2e} -> {float(s['vC']):.0e}; mismatched stalls "
          f"({int(s['n_mis'])} steps); speedup {sp:.2f}x; rej/step {float(s['rej_raw']):.2f} vs "
          f"{float(s['rej_ca']):.2f}; rank {int(s['rank'])}/{int(s['n_par'])}, tangent {int(s['tangent'])}")
    print("PASS: tangency fixed and the mismatch confirmed fatal; B3 still failed; ELEC-027's")
    print("      restoration diagnosis refuted; jamming measured and explicitly NOT the cause.")


if __name__ == "__main__":
    test()
