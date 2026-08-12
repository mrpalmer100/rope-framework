"""THM-006 (Modeled): THE LAYER SEPARATION THEOREM -- the programme's
failures are enriched at the dynamical frontier, not scattered.

Classifies all registered claims into Layer I (Topological), II
(Geometric), III (Dynamical) by REQUIREMENT (not vocabulary; see
tools/layer_classifier.py for the marker set and its audit trail),
then tests whether Failed+Open claims concentrate at Layer III.

RESULT (this corpus): Layer III is ~10 percent of claims, yet holds
5 of 12 Failed+Open claims -- a ~4x enrichment over the chance
expectation of ~1. The enriched failures are the deep ones (lepton
masses PM-002/004, quantum entanglement QB-003, the electron-mass
mechanism QB-004); the Layer II failures are ordinary classical
falsifications (cosmological alpha-variation EM-011, the two gravity-
conditioning candidates GRV-009/010), kept but NOT frontier-clustered.

HONEST HISTORY, kept: a first classifier keyed on any MENTION of
hbar/mass/Bell and mis-tagged the whole matter and QB sectors,
returning 0.5x (anti-clustering). That adverse result was registered
in the development notes, the classifier corrected to key on
requirement, and only then did the 4x signal appear. The theorem is
Modeled, not Derived: it depends on a curated (auditable) marker set,
and a different reasonable marker set could shift the enrichment. What
is robust is the SIGN and rough magnitude: genuine failures cluster
toward the dynamical layer.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
import layer_classifier as L


def _exclude_self(claims):
    """SELF-REFERENCE EXCLUSION (added 2026-08-01, and it decided the verdict).

    THM-006 is itself classified Layer III. When the claim was reclassified
    Failed-and-kept, it entered its own statistic as a Layer III failure and
    pushed the enrichment from 1.85x back up to 2.14x -- i.e. the theorem about
    where failures cluster became evidence for itself BY FAILING. A claim may
    not count itself as evidence for itself, so it is excluded here and the
    enrichment recomputed on the remaining corpus.
    """
    return [c for c in claims if c["id"] != "THM-006"]


def test():
    claims, _, _, _ = L.run(verbose=False)
    claims = _exclude_self(claims)
    total = len(claims)
    from collections import Counter as _C
    layer_all = _C(c["layer"] for c in claims)
    fails = [c for c in claims if c.get("status") in ("Failed", "Open")]
    f_layer = _C(c["layer"] for c in fails)
    n_fail = len(fails)
    enrich = (f_layer["III"] / n_fail) / (layer_all["III"] / total)
    from collections import Counter
    layer_tot = Counter(c['layer'] for c in claims)
    # structural sanity: three non-empty layers, III is the minority
    assert all(layer_tot[k] > 0 for k in ("I", "II", "III")), "three populated layers"
    assert layer_tot["III"] < layer_tot["II"], "dynamical layer is the minority (as the ladder shows)"
    # THE THEOREM AS ORIGINALLY STATED IS FALSIFIED BY THE CORPUS'S OWN GROWTH.
    # HISTORY OF THE STATISTIC (all bars locked, none relaxed, all kept):
    #   ~4x    at writing            -- the theorem's original observation
    #   1.85x  2026-08-01            -- FIRST kept failure: magnitude bar (>2x)
    #   <1x    2026-08-09            -- SECOND kept failure: sign bar (>1x),
    #          the review-arc recovery drove failures to the GEOMETRIC layer
    #   (live) recomputed each run   -- the registry keeps growing and the
    #          statistic keeps moving (observed back at ~1.1x, 2026-08-12,
    #          after the BET and NUN/SAMEKH/AYIN arcs shifted the census)
    #
    # HARDENED 2026-08-12: a KEPT-FAILURE benchmark must REPRODUCE THE RECORD,
    # not gate CI on a live registry statistic. The claim's grade is Failed and
    # stays Failed; both locked bars remain violated in the record. The dead
    # bars are now DOCUMENTED (printed with the live value) instead of asserted,
    # so registry growth cannot turn a kept failure into a spurious CI crash.
    # The structural sanity asserts above ARE genuine invariants and remain.
    print(f"THM-006 (Failed-and-kept, twice): live enrichment {enrich:.2f}x on")
    print(f"  today's registry ({total} claims, {n_fail} Failed/Open).")
    print(f"  layers: I={layer_tot['I']}, II={layer_tot['II']}, III={layer_tot['III']}"
          f" (III the minority at {100*layer_tot['III']/total:.0f}%).")
    print(f"  failures: I={f_layer['I']}, II={f_layer['II']}, III={f_layer['III']}.")
    print("  RECORD: magnitude bar (>2x) violated 2026-08-01; sign bar (>1x)")
    print("  violated 2026-08-09; both kept locked. The theorem is dead on its")
    print("  own terms regardless of where the live value drifts -- a statistic")
    print("  that has crossed its bar in both directions is not a law.")

if __name__ == "__main__":
    test()
