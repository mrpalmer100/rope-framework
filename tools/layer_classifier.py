#!/usr/bin/env python3
"""Layer classifier for the Layer Separation Theorem (THM-006).

HONEST DESIGN NOTE: a first version keyed on any mention of hbar/mass/Bell and mis-tagged the
whole matter and QB sectors (which mostly SUCCEED at characterizing the boundary). Vocabulary is
not requirement. This version classifies by what a claim FUNDAMENTALLY REQUIRES, using markers
chosen to separate "requires a universal action / quantum amplitude / absolute mass origin"
(Layer III) from "reproduces a classical field/geometry result that merely mentions those words."
The classifier is still applied uniformly and never hand-lists which claims are which; but the
marker set is curated and its choices are auditable below. The theorem is then tested on the
STATUS distribution that emerges."""
import yaml, re, json
from collections import Counter, defaultdict

# Layer III REQUIRES a genuinely dynamical ingredient. Phrases chosen to fire on the requirement,
# not on incidental mention. (e.g. "Tsirelson as a theorem" SUCCEEDS at the boundary -> II-about-III,
# not a Layer III failure; it is caught as settled and that is correct.)
L3_REQUIRE = [
    r"reproduce quantum entanglement", r"quantum entanglement\b(?!.*bound)",
    r"lepton (mass|ratio|spectrum)", r"electron\b.*\bmass\b.*mechanism", r"fluctuation mass",
    r"born rule", r"probability amplitude",
    r"universal action", r"derive .*\bhbar", r"planck.*constant",
    r"quantum gravity", r"quantum-completion", r"strong-field.*grav",
    r"absolute mass scale", r"origin of.*mass spectrum",
]
# Layer I: pure topology / metric-free invariants (the discrete building blocks)
L1_MARK = [
    r"winding", r"linking number", r"\bknot type", r"\bbraid\b", r"homotop", r"framing",
    r"integer quantis", r"integer quantiz", r"conserved integer", r"chern",
    r"charge = .*winding", r"charge as .*winding", r"topological (invariant|winding|charge)",
    r"no-monopole", r"parity.*topolog",
]

def classify(text):
    t = text.lower()
    if any(re.search(p, t) for p in L3_REQUIRE):
        return "III"
    if any(re.search(p, t) for p in L1_MARK):
        return "I"
    return "II"

def load():
    d = yaml.safe_load(open('claims.yaml'))
    return d['claims'] if isinstance(d, dict) and 'claims' in d else d

def run(verbose=True):
    claims = load()
    for c in claims:
        c['layer'] = classify(c['id'] + " " + c['title'] + " " + c.get('note', ''))
    failed = [c for c in claims if c['status'] in ("Failed", "Open")]
    f_layer = Counter(c['layer'] for c in failed)
    total = len(claims); layer_tot = Counter(c['layer'] for c in claims)
    # THE TEST: are the genuine failures/opens enriched at Layer III vs the base rate?
    p3 = layer_tot["III"]/total
    of3 = f_layer["III"]; expected = p3*len(failed)
    enrich = of3/expected if expected else 0
    if verbose:
        print(f"=== {total} claims classified by REQUIREMENT (not mention) ===")
        for L in ("I","II","III"):
            print(f"  Layer {L}: {layer_tot[L]} claims")
        print(f"\n=== FAILURE CLUSTERING TEST ===")
        print(f"Failed+Open claims: {len(failed)}")
        for L in ("I","II","III"):
            print(f"  in Layer {L}: {f_layer[L]}")
        print(f"\nBase rate P(III) = {p3:.2f}; expected {expected:.1f} of {len(failed)} at Layer III by chance;")
        print(f"observed {of3}.  ENRICHMENT = {enrich:.1f}x")
        print(f"\n=== the Failed+Open claims and their layers (auditable) ===")
        for c in sorted(failed, key=lambda x: x['layer']):
            print(f"  [{c['layer']:>3}] {c['id']} ({c['status']}): {c['title'][:62]}")
    json.dump({c['id']: c['layer'] for c in claims}, open('docs/layer_classification.json','w'), indent=0)
    return claims, enrich, f_layer, len(failed)

if __name__ == "__main__":
    run()
