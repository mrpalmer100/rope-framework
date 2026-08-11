#!/usr/bin/env python3
"""
sync_doc_facts.py -- refresh registry-derived FACTS inside hand-maintained docs,
without touching their editorial prose.

The problem this solves: docs like STATE_OF_THE_PROGRAMME.md and KNOWN_LIMITATIONS.md
are persuasive because a human wrote their narrative. But they carry factual
fragments -- claim counts, status distributions, the failed-and-kept ledger,
sector maturity -- that go stale as the corpus grows, and a stale fact reads as
undersell (a smaller, less mature, more failure-heavy programme than exists).

The fix: wrap ONLY the factual fragments in marker comments. This tool regenerates
what is between the markers from claims.yaml and leaves everything else untouched.

    <!-- BEGIN GENERATED: corpus_stats -->
    ...(this region is overwritten by the tool)...
    <!-- END GENERATED: corpus_stats -->

Editorial prose lives outside the markers and is never touched. Run this after any
registry change (or in CI) so wins propagate automatically.

Usage:
    python3 tools/sync_doc_facts.py            # update all docs with markers
    python3 tools/sync_doc_facts.py --check     # report drift, change nothing (CI)
"""
import sys, re, yaml
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLAIMS = ROOT / "claims.yaml"

# Files that may carry generated fact-blocks. Add to this list as markers spread.
TARGET_DOCS = [
    ROOT / "README.md",
    ROOT / "KNOWN_LIMITATIONS.md",
    ROOT / "docs" / "STATE_OF_THE_PROGRAMME.md",
]

SECTOR_PREFIXES = {
    "Electromagnetism": {"EM", "EM-RECON", "EW"},
    "Gravity & Galaxies": {"GRV", "GG"},
}


def load_claims():
    d = yaml.safe_load(CLAIMS.read_text())
    return d["claims"]


def sector_of(cid):
    m = re.match(r"([A-Z-]+?)-?\d", cid)
    return m.group(1) if m else cid


# ---- block generators. each returns the markdown body for a named region ----

def gen_version(claims):
    """Release version, read from pyproject.toml so it cannot drift from the
    packaged version. Added 2026-08-11 after the README was found stale at
    3.15.0 against a 3.18.x corpus: the README carried no markers and was not
    a sync target, so no tool could have caught it."""
    txt = (ROOT / "pyproject.toml").read_text()
    m = re.search(r'^version\s*=\s*"([^"]+)"', txt, re.M)
    return m.group(1) if m else "unknown"


def gen_status_breakdown(claims):
    stat = Counter(c.get("status") for c in claims)
    order = ["Derived", "Modeled", "EFT-constrained", "Conjecture", "Open", "Failed"]
    parts = []
    for k in order:
        if stat.get(k):
            label = "Failed-and-kept" if k == "Failed" else k
            parts.append(f"{stat[k]} {label}")
    for k in sorted(set(stat) - set(order)):
        parts.append(f"{stat[k]} {k}")
    backed = sum(1 for c in claims if c.get("benchmark"))
    return (f"{len(claims)} registered claims ({', '.join(parts)}); "
            f"{backed} code-backed.")


def gen_corpus_stats(claims):
    total = len(claims)
    backed = sum(1 for c in claims if c.get("benchmark"))
    stat = Counter(c.get("status") for c in claims)
    derived = stat.get("Derived", 0)
    failed = stat.get("Failed", 0)
    # one plain line, safe to drop into any prose context
    return (
        f"*{total} registered claims, {backed} code-backed and passing, "
        f"{derived} Derived, {failed} registered Failed and kept.*"
    )


def gen_failed_ledger(claims):
    """The complete failed-and-kept ledger -- the exact thing that went stale at 7-of-25."""
    failed = sorted([c for c in claims if c.get("status") == "Failed"], key=lambda c: c["id"])
    lines = [f"*The complete ledger: all {len(failed)} claims registered Failed and kept.*", ""]
    for c in failed:
        # clean the title to its first clause
        t = c.get("title", "").split("(")[0].split(" -- ")[0].strip()
        lines.append(f"- **{c['id']}**: {t}")
    return "\n".join(lines)


def gen_sector_maturity(claims):
    rows = []
    for name, prefixes in SECTOR_PREFIXES.items():
        sel = [c for c in claims if sector_of(c["id"]) in prefixes]
        der = sum(1 for c in sel if c.get("status") == "Derived")
        rows.append(f"- **{name}:** {der} of {len(sel)} Derived")
    return "\n".join(rows)


GENERATORS = {
    "version": gen_version,
    "status_breakdown": gen_status_breakdown,
    "corpus_stats": gen_corpus_stats,
    "failed_ledger": gen_failed_ledger,
    "sector_maturity": gen_sector_maturity,
}

MARKER = re.compile(
    r"(<!-- BEGIN GENERATED: (?P<name>[a-z_]+) -->\n)(?P<body>.*?)(\n<!-- END GENERATED: (?P=name) -->)",
    re.DOTALL,
)


def sync_text(text, claims):
    changed = []

    def repl(m):
        name = m.group("name")
        gen = GENERATORS.get(name)
        if gen is None:
            return m.group(0)  # unknown region, leave untouched
        new_body = gen(claims)
        if new_body != m.group("body"):
            changed.append(name)
        return m.group(1) + new_body + m.group(4)

    new_text = MARKER.sub(repl, text)
    return new_text, changed


def main():
    check = "--check" in sys.argv
    claims = load_claims()
    any_drift = False
    for path in TARGET_DOCS:
        if not path.exists():
            continue
        text = path.read_text()
        if "<!-- BEGIN GENERATED:" not in text:
            continue  # no markers yet
        new_text, changed = sync_text(text, claims)
        if changed:
            any_drift = True
            rel = path.relative_to(ROOT)
            if check:
                print(f"DRIFT  {rel}: regions out of date -> {', '.join(changed)}")
            else:
                path.write_text(new_text)
                print(f"synced {rel}: {', '.join(changed)}")
        else:
            print(f"ok     {path.relative_to(ROOT)}")
    if check and any_drift:
        sys.exit(1)


if __name__ == "__main__":
    main()
