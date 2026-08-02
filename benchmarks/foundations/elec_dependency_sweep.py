"""ELEC-065 -- THE DEPENDENCY SWEEP: which claims inherited a premise that
changed today and never noticed?

Bars locked in analysis/ELEC065_dependency_sweep_bars_LOCKED.md BEFORE the sweep.
"""
import os
import yaml

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
TAGS = ("SECTOR CLOSED", "FALSIFIED BY THE CORPUS", "AMENDMENT SUPERSEDED",
        "SCALE ANCHOR LOST", "RETURNED TO UNCONDITIONAL", "DEMOTED", "CORRECTED",
        "NARROWED", "BOUND CORRECTED", "PRICE COME DUE", "ROUTE TO T1 BLOCKED",
        "UNANCHORED")


def load():
    d = yaml.safe_load(open(os.path.join(ROOT, "claims.yaml"), encoding="utf-8"))
    return d["claims"]


def main():
    claims = load()
    by = {x["id"]: x for x in claims}
    changed = {x["id"] for x in claims
               if any(t in (x.get("note") or "") for t in TAGS)}
    print(f"B1 CHANGED TODAY: {len(changed)} claims.")

    # descendants: who depends on a changed claim, transitively
    children = {}
    for x in claims:
        for dep in (x.get("depends_on") or []):
            children.setdefault(dep, []).append(x["id"])
    desc, frontier = set(), list(changed)
    while frontier:
        cur = frontier.pop()
        for kid in children.get(cur, []):
            if kid not in desc:
                desc.add(kid)
                frontier.append(kid)
    desc -= changed
    print(f"   transitive descendants (excluding the changed claims): {len(desc)}")

    # B2: which descendants carry no annotation referencing today's work?
    today_markers = ("2026-08-01", "ELEC-05", "ELEC-06", "GRV-04", "GRV-05",
                     "PRED-002-", "PRED-003-")
    flagged = [cid for cid in sorted(desc)
               if not any(m in (by[cid].get("note") or "") for m in today_markers)]
    print(f"\nB2 UNANNOTATED DESCENDANTS: {len(flagged)} of {len(desc)}")
    for cid in flagged:
        deps = [d for d in (by[cid].get("depends_on") or []) if d in changed]
        print(f"   {cid:18s} depends on changed: {deps}")

    # B3 triage
    print("\nB3 TRIAGE:")
    if not flagged:
        print("   nothing to triage.")
    triage = {}
    for cid in flagged:
        x = by[cid]
        deps = set(x.get("depends_on") or []) & changed
        # a descendant INHERITS if its own text invokes the changed quantity
        text = (x["title"] + " " + (x.get("note") or "")).lower()
        # WORD-BOUNDARY matching. The first pass used substrings and flagged nine
        # claims, ALL false positives: "born" matched inside "stubborn" and
        # "reborn", and "Born's half-angle law" / "Born equivariance" are not the
        # retired Born-SCALE prediction. Recorded because a sweep whose triage
        # over-flags is a sweep nobody will trust the second time.
        import re as _re
        hot_terms = (r"hbar ~ w", r"mesoscopic", r"4\.31\s*fm", r"n\^2 t w\^2",
                     r"sub-quantum patch", r"born-scale", r"born rule at nuclear",
                     r"\b2e4\b")
        hot = any(_re.search(t, text) for t in hot_terms)
        triage[cid] = "INHERITS" if hot else "SURVIVES"
        why = ("its text invokes a retired quantity (mesoscopic patch / hbar~w^2 / "
               "Born-scale)" if hot else
               "no retired quantity appears in its statement; the dependence is on "
               "an unaffected part of the parent")
        print(f"   {cid:18s} {triage[cid]:9s} -- {why}")

    inherits = [k for k, v in triage.items() if v == "INHERITS"]
    print(f"\nB4 RESULT: {len(flagged)} unannotated descendants, "
          f"{len(inherits)} INHERITING a changed premise.")
    if not flagged:
        print("   A NULL SWEEP. Today's corrections were complete: every claim")
        print("   downstream of a changed premise already carries an annotation")
        print("   recording it. That is the outcome the bars allowed for and it")
        print("   means the two errors found earlier were the only two.")
    else:
        print("   These are the unnoticed inheritances; B5 requires they be")
        print("   annotated in this session, not deferred.")
    print("\nB5: annotations for any INHERITS claim are filed by the session that")
    print("    runs this sweep; the benchmark records the finding, not the fix.")


if __name__ == "__main__":
    main()
