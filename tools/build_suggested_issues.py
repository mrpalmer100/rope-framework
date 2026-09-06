#!/usr/bin/env python3
"""
build_suggested_issues.py -- generate docs/SUGGESTED_ISSUES.md from the registry.

The "suggested issues" doc is meant to mirror the programme's *current open
frontier* so a contributor can pick a real, still-open problem. Hand-maintained,
it drifts: problems get solved but stay listed, and new open problems never get
added. Listing an already-solved problem as "help wanted" makes the programme look
like it does not know its own state -- the opposite of what it is for.

The open frontier is a registry query: every claim at status Open or Conjecture.
This tool emits exactly those, in the doc's existing issue-block format, so the
list is correct by construction every time it runs.

Usage:
    python3 tools/build_suggested_issues.py
"""
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLAIMS = ROOT / "claims.yaml"
OUT = ROOT / "docs" / "SUGGESTED_ISSUES.md"

HEADER = """# Suggested GitHub Issues (open problems as research questions)

*Generated from `claims.yaml` -- do not edit by hand. Regenerate with
`python3 tools/build_suggested_issues.py` (run by `make` / checked by
`tools/check_freshness.py`).*

Every claim currently at status **Open** or **Conjecture** -- the programme's live
open frontier. Paste a block below as a new Issue. Suggested labels:
`open-problem`, `conjecture`, `derivation-wanted`, `help-wanted`.

"""

FOOTER = "*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*"


def clean(text, n=320):
    if not text:
        return ""
    text = " ".join(text.split())
    return text[:n] + ("..." if len(text) > n else "")


def block(c):
    lines = [f"### [{c['id']}] {clean(c.get('title',''), 90)}", ""]
    lines.append(f"**Status:** {c.get('status')}  ")
    if c.get("paper"):
        lines.append(f"**Paper:** {c['paper']}  ")
    if c.get("benchmark"):
        lines.append(f"**Benchmark:** `{c['benchmark']}`  ")
    if c.get("depends_on"):
        dep = ", ".join(c["depends_on"]) if isinstance(c["depends_on"], list) else str(c["depends_on"])
        lines.append(f"**Depends on:** {dep}  ")
    lines.append("")
    note = clean(c.get("note", "") or c.get("title", ""))
    if note:
        lines.append(note)
        lines.append("")
    lines.append(FOOTER)
    return "\n".join(lines)


def main():
    d = yaml.safe_load(CLAIMS.read_text())
    frontier = [c for c in d["claims"] if c.get("status") in ("Open", "Conjecture")]
    # stable, readable order: Open first, then Conjecture, each by id
    frontier.sort(key=lambda c: (c["status"] != "Open", c["id"]))

    parts = [HEADER, "\n---\n"]
    for c in frontier:
        parts.append("\n" + block(c) + "\n")
        parts.append("\n---\n")

    n_open = sum(1 for c in frontier if c["status"] == "Open")
    n_conj = len(frontier) - n_open
    parts.append(f"\n*{len(frontier)} open-frontier claims "
                 f"({n_open} Open, {n_conj} Conjecture) as of the current registry.*\n")

    OUT.write_text("".join(parts))
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(frontier)} open-frontier claims: "
          f"{n_open} Open, {n_conj} Conjecture)")


if __name__ == "__main__":
    main()
