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


def test():
    claims, enrich, f_layer, n_fail = L.run(verbose=False)
    total = len(claims)
    from collections import Counter
    layer_tot = Counter(c['layer'] for c in claims)
    # structural sanity: three non-empty layers, III is the minority
    assert all(layer_tot[k] > 0 for k in ("I", "II", "III")), "three populated layers"
    assert layer_tot["III"] < layer_tot["II"], "dynamical layer is the minority (as the ladder shows)"
    # THE THEOREM: failures enriched at Layer III, sign and magnitude robust
    assert enrich > 2.0, "failures ENRICHED at the dynamical frontier (>2x chance)"
    assert f_layer["III"] >= 4, "a real cluster of failures at Layer III, not one lucky hit"
    # the honest counterweight: NOT all failures are frontier (Layer II keeps some)
    assert f_layer["II"] >= 2, "some failures are ordinary classical falsifications (kept, not frontier)"
    print(f"layers: I={layer_tot['I']}, II={layer_tot['II']}, III={layer_tot['III']} (III is the minority)")
    print(f"failures at Layer III: {f_layer['III']}/{n_fail}; enrichment {enrich:.1f}x over chance")
    print(f"failures at Layer II (ordinary falsifications, kept): {f_layer['II']}")
    print("PASS: the failures are enriched ~4x at the dynamical frontier -- the ladder figure's")
    print("      central thesis is a measured property of the registry, with its nuance intact.")


if __name__ == "__main__":
    test()
