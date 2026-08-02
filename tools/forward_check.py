#!/usr/bin/env python3
"""Forward check: before relying on a claim, list every LATER claim in its
sector that may have revised it.

WHY THIS EXISTS (2026-08-01). Twice in one day the corpus built on a superseded
result:
  - HBAR-010 was classified as surviving a sector retirement because it did not
    use the retired LENGTH -- but it used the retired RELATION (ELEC-064).
  - GRV-049 and GRV-052 used GRV-040's supply-limited luminosity law without
    checking GRV-047, three claims later in the same sector, titled 'THE
    LUMINOSITY LAW REVISED TO A SWITCH'. The resulting number was wrong by 63
    orders of magnitude (GRV-053).
Both were caught by a human reading, not by any tool. tools/verify_corpus.py's
dependency guard and ELEC-065's sweep both look DOWNSTREAM of claims whose
standing changed; nothing looked FORWARD from a claim about to be used.

Usage:
    python tools/forward_check.py GRV-040
    python tools/forward_check.py GRV-040 ELEC-053 --quiet
    python tools/forward_check.py --audit          # every claim with revisers
"""
import argparse
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Words that, in this corpus's house style, announce that a claim changes the
# standing of an earlier one. Drawn from the actual annotation vocabulary.
REVISION_WORDS = (
    "revised", "revision", "supersede", "superseded", "supersedes",
    "corrected", "correction", "retired", "retracted", "withdrawn",
    "amended", "amendment", "narrowed", "restated", "overturned",
    "falsified", "closed", "demoted", "kill", "killed", "no-go",
    "artifact", "error", "mistaken", "unsound", "wrong", "replaced",
)


def load(path=None):
    p = path or os.path.join(ROOT, "claims.yaml")
    d = yaml.safe_load(open(p, encoding="utf-8"))
    return d["claims"]


def sector_of(cid):
    """Sector prefix: everything before the trailing numeric field."""
    parts = cid.split("-")
    return "-".join(parts[:-1]) if len(parts) > 1 else cid


def revisers(cid, claims):
    """Later claims that may revise `cid`, by three independent routes."""
    by_pos = {c["id"]: i for i, c in enumerate(claims)}
    if cid not in by_pos:
        return None
    here = by_pos[cid]
    sect = sector_of(cid)
    out = []
    for c in claims[here + 1:]:
        text = (c["title"] + " " + (c.get("note") or ""))
        low = text.lower()
        reasons = []
        # 1. names it explicitly anywhere
        if re.search(r"\b" + re.escape(cid) + r"\b", text):
            reasons.append("names it")
        # 2. same sector AND uses revision vocabulary
        if sector_of(c["id"]) == sect and any(w in low for w in REVISION_WORDS):
            reasons.append("same sector + revision language")
        # 3. depends on it
        if cid in (c.get("depends_on") or []):
            reasons.append("depends on it")
        if reasons:
            out.append((c["id"], c.get("status"), reasons, c["title"][:100]))
    return out


def report(cid, claims, quiet=False):
    r = revisers(cid, claims)
    if r is None:
        print(f"{cid}: NOT FOUND in the registry")
        return 1
    named = [x for x in r if "names it" in x[2]]
    print(f"\n=== {cid}: {len(r)} later claim(s) may bear on it "
          f"({len(named)} name it explicitly)")
    if not r:
        print("    none -- safe to rely on as written")
        return 0
    for cid2, st, reasons, title in r:
        if quiet and "names it" not in reasons:
            continue
        print(f"    {cid2:16s} [{st or '?':14s}] {'; '.join(reasons)}")
        print(f"        {title}")
    print("    READ THESE BEFORE RELYING ON THE CLAIM ABOVE.")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="*", help="claim IDs about to be relied upon")
    ap.add_argument("--quiet", action="store_true",
                    help="show only claims that name the target explicitly")
    ap.add_argument("--audit", action="store_true",
                    help="summarise every claim that has potential revisers")
    a = ap.parse_args()
    claims = load()

    if a.audit:
        rows = []
        for c in claims:
            r = revisers(c["id"], claims)
            named = [x for x in r if "names it" in x[2]]
            if named:
                rows.append((c["id"], len(named)))
        rows.sort(key=lambda t: -t[1])
        print(f"claims with later claims naming them: {len(rows)} of {len(claims)}")
        for cid, n in rows[:25]:
            print(f"   {cid:18s} named by {n} later claim(s)")
        return 0

    if not a.ids:
        ap.print_help()
        return 2
    rc = 0
    for cid in a.ids:
        rc |= report(cid, claims, a.quiet)
    return rc


if __name__ == "__main__":
    sys.exit(main())
