#!/usr/bin/env python3
"""Insert a claim into claims.yaml STRUCTURALLY, not by regex.

History (why this file was rewritten, 2026-08-01):
  v1 located the insertion point with a regex over the raw text
  (`    note: "[^"]*"`). That worked only for one exact serialization. When
  claims.yaml was rewritten by a structured load/dump during the misfiled-claims
  repair, the regex stopped matching and the tool failed on every call. Worse,
  a sibling failure in the same reformat left tools/verify_corpus.py parsing ZERO
  claims while still reporting ALL CHECKS PASS.

  The lesson is recorded in docs/STANDING_RULE_SOURCE_BEFORE_INSTRUMENT.md's
  spirit: tooling that depends on incidental formatting will break silently.
  This version parses YAML, inserts into the list, and re-serializes with the
  canonical style, so it is immune to whitespace and quoting changes.

Usage (programmatic):
    from tools.add_claim import insert_after
    insert_after("PRIOR-ID", block)      # block: YAML text OR a dict

Usage (CLI):
    python tools/add_claim.py --after PRIOR-ID --file new_claim.yaml
"""
import argparse
import sys

import yaml

PATH = "claims.yaml"
FIELDS = ("id", "title", "status", "paper", "benchmark", "depends_on", "note")


class Canonical(yaml.SafeDumper):
    """The corpus's canonical serialization: sequences indented under their key
    (so entries read '  - id: X'), long strings double-quoted, no aliases."""

    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)

    def ignore_aliases(self, *args):
        return True


Canonical.add_representer(str, lambda dp, dt: dp.represent_scalar(
    "tag:yaml.org,2002:str", dt, style='"' if ("\n" in dt or len(dt) > 80) else None))


def _as_claim(block):
    """Accept a dict or a YAML block (with or without the leading '  - ')."""
    if isinstance(block, dict):
        return block
    text = block.strip()
    if text.startswith("- "):
        parsed = yaml.safe_load(text)
        return parsed[0] if isinstance(parsed, list) else parsed
    parsed = yaml.safe_load(text)
    if isinstance(parsed, list):
        return parsed[0]
    return parsed


def _check_structure(doc, path):
    """Guards against the two corruptions actually seen in this corpus."""
    misfiled = [e["id"] for e in doc.get("sectors", []) if isinstance(e, dict) and "id" in e]
    if misfiled:
        raise SystemExit(
            f"REFUSING TO WRITE {path}: claims misfiled into the sectors block: "
            f"{misfiled}. (This corruption hid six claims from every registry tool.)")
    ids = [c["id"] for c in doc["claims"]]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        raise SystemExit(f"REFUSING TO WRITE {path}: duplicate ids {sorted(dupes)}")
    if not doc["claims"]:
        raise SystemExit(f"REFUSING TO WRITE {path}: zero claims")


def insert_after(prior_id, block, path=PATH):
    doc = yaml.safe_load(open(path, encoding="utf-8"))
    claims = doc["claims"]
    claim = _as_claim(block)
    if "id" not in claim:
        raise SystemExit("block has no 'id'")
    if any(c["id"] == claim["id"] for c in claims):
        raise SystemExit(f"id {claim['id']} already present")
    idx = next((k for k, c in enumerate(claims) if c["id"] == prior_id), None)
    if idx is None:
        raise SystemExit(f"prior id {prior_id} not found")
    ordered = {k: claim[k] for k in FIELDS if k in claim}
    ordered.update({k: v for k, v in claim.items() if k not in ordered})
    claims.insert(idx + 1, ordered)
    _check_structure(doc, path)
    text = yaml.dump(doc, Dumper=Canonical, sort_keys=False, width=100000,
                     allow_unicode=True)
    yaml.safe_load(text)  # strict parse BEFORE writing
    open(path, "w", encoding="utf-8").write(text)
    print(f"inserted {claim['id']} after {prior_id}; "
          f"{len(claims)} claims, strict YAML OK")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--after", required=True)
    ap.add_argument("--file", required=True, help="YAML file holding the new claim")
    ap.add_argument("--path", default=PATH)
    a = ap.parse_args()
    insert_after(a.after, open(a.file, encoding="utf-8").read(), a.path)


if __name__ == "__main__":
    main()
