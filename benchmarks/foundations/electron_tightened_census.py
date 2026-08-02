"""ELEC-031 (Modeled): THE CRITERION TIGHTENED 1126x, AND THE CENSUS
CAUGHT ITSELF BEING SCALE-BLIND. Still not a minimum; ELEC-030's
verdict is corrected; the census gains a protocol rule.

(1) THE FLOOR, MEASURED PROPERLY FIRST: repeated evaluations are
    bit-identical (CG is deterministic), so the campaign's previous
    'floor' of ~1e-10 was solver TRUNCATION across different
    tolerances, not noise. Against a converged reference the
    differential truncation between nearby states is 6.7e-13 at
    rtol=1e-8 and 3.6e-15 at rtol=1e-12 -- working tighter lowers the
    census floor 188-fold and licenses a termination criterion of
    8.88e-12 on the 25-step window, 1126x tighter than the 1e-8 in
    force since ELEC-013.

(2) TERMINATION AT THE NEW CRITERION: 228 iterations to
    E = 15.447560780074, certification intact (d = 0.06001,
    |Lk| = 1.0099), confirming ELEC-030's post-dip state was already
    within 5e-12 of this point.

(3) THE CENSUS CORRECTED ITSELF: at the 188x tighter threshold, 15 of
    26 directions dip with a deepest of -8.6e-7 -- against ELEC-030's
    reported 1 of 26. Replication at fixed state isolates the cause,
    and it is NOT the seed: ELEC-030's own protocol reproduces 0 of 14
    here, while adding a single finer probe scale (t = 1e-6) yields 6
    to 9 of 14 across three seeds with deepest dips of -3.6e-7 to
    -9.8e-7. THE CENSUS WAS BLIND BELOW t = 1e-5, AND THE RESIDUAL
    DESCENT LIVES AT t ~ 1e-6.

(4) THE PROTOCOL RULE, adopted: dip COUNTS are protocol-sensitive
    (0 to 9 of 14 at one fixed state) and must not be quoted as a
    convergence statistic; the DEEPEST DIP is stable across seeds
    (-3.6e-7 to -9.8e-7) and is the number to report. Censuses must
    probe down to the step scale at which the terminating engine is
    actually moving, or they certify their own blindness.

VERDICT: still not a minimum. The honest gap is ~1e-6 in E, about
6e-8 relative -- a genuine ~100x improvement on ELEC-024's -1.0e-4,
but not the 41x-collapse-to-near-certification that ELEC-030 reported.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'ELEC031_state.npz')
    # (1) the floor and the tightened criterion
    assert float(s['floor']) < 1e-14, "differential truncation 3.6e-15 at rtol=1e-12"
    assert float(s['crit']) < 1e-11, "criterion 8.88e-12: 1126x tighter than 1e-8"
    # (2) terminated there
    assert bool(s['terminated']) and int(s['iters']) < 400, "228 iterations to the new criterion"
    # (3) the correction: still not a minimum, and the count is protocol-sensitive
    assert int(s['ndips']) > 5, "15/26 dip at the tightened threshold: NOT a minimum"
    nd = s['var_nd']; deep = s['var_deep']
    assert nd.min() == 0 and nd.max() >= 6, \
        "dip COUNT ranges 0-9 of 14 at ONE fixed state: protocol-sensitive"
    fine = deep[deep < 0]
    assert fine.max()/fine.min() < 4, "deepest dip is STABLE across seeds (-3.6e-7..-9.8e-7)"
    assert float(s['deepest']) > -1e-5, "the gap is ~1e-6: a real ~100x gain on ELEC-024"
    print(f"floor {float(s['floor']):.1e}; crit {float(s['crit']):.1e}; {int(s['iters'])} its; "
          f"census {int(s['ndips'])}/26 dip, deepest {float(s['deepest']):.2e}; "
          f"counts across protocols {nd.min()}-{nd.max()}/14")
    print("PASS: criterion tightened 1126x; the census caught its own scale-blindness;")
    print("      deepest dip is the stable statistic; still not a minimum.")


if __name__ == "__main__":
    test()
