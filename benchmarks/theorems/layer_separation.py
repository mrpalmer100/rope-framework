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
    # Registered 2026-08-01: the pre-committed bar was enrichment > 2.0, measured
    # at ~4x when THM-006 was written. It is now 1.85x. The bar was NOT relaxed to
    # accommodate the decline -- that would be bar-shopping, which this corpus
    # refuses by rule. The claim is reclassified Failed-and-kept and this benchmark
    # now documents the falsification instead of asserting the dead threshold.
    assert enrich < 2.0, "the original >2x bar is violated (this is the kept failure)"
    assert enrich > 1.0, "the SIGN survives: failures still concentrate at Layer III"
    assert f_layer["III"] >= 4, "a real cluster of failures at Layer III, not one lucky hit"
    # the honest counterweight: NOT all failures are frontier (Layer II keeps some)
    assert f_layer["II"] >= 2, "some failures are ordinary classical falsifications (kept, not frontier)"
    print(f"KEPT FAILURE: enrichment {enrich:.2f}x against the locked bar of 2.0x. "
          f"Layer III is {100*layer_tot['III']/total:.0f}% of claims and holds "
          f"{f_layer['III']}/{n_fail} failures. The sign survives; the magnitude does not.")
    print(f"layers: I={layer_tot['I']}, II={layer_tot['II']}, III={layer_tot['III']} (III is the minority)")
    print(f"failures at Layer III: {f_layer['III']}/{n_fail}; enrichment {enrich:.1f}x over chance")
    print(f"failures at Layer II (ordinary falsifications, kept): {f_layer['II']}")
    print("VERDICT: the sign is a measured property of the registry; the 4x magnitude")
    print("      the ladder figure was built on is retired. See THM-006's note.")


if __name__ == "__main__":
    test()
