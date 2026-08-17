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




def gen_current_release(claims):
    """One-line current-release banner: version from pyproject (single
    source of truth), claim count from the registry, date from today's
    UTC. Added 2026-08-16 after the hand-written banner went stale at
    v3.26.52 within three releases of being written -- version numbers
    never belong in hand-maintained prose."""
    import re as _re, datetime as _dt
    v = gen_version(claims)
    # date from the CHANGELOG entry for this version (the release's own
    # date), not the wall clock -- avoids UTC-midnight drift
    ch = (ROOT / "CHANGELOG.md").read_text()
    m = _re.search(_re.escape(v) + r"\s*\((\d{4})-(\d{2})-(\d{2})\)", ch)
    if m:
        d = _dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        ds = d.strftime("%-d %b %Y")
    else:
        ds = _dt.date.today().strftime("%-d %b %Y")
    return f"**Current release: v{v}** ({ds}), {len(claims)} claims."

GENERATORS = {
    "version": gen_version,
    "current_release": gen_current_release,
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

    # ---- FRONT-DOOR TRIPWIRE (added v3.26.3) -------------------------------
    # Narrative furniture (release cards, version mentions) lives OUTSIDE the
    # generated regions and went stale twice at v3.26.x. This check compares
    # every version-like reference in the front-door docs against the release
    # version in pyproject.toml. Rules:
    #   - README must reference the CURRENT version at least once.
    #   - Any vX.Y.Z reference in README/KNOWN_LIMITATIONS prose that is more
    #     than one MINOR version behind current fails, unless the line also
    #     contains a history/archival cue (docs/history, 'prior', 'archived',
    #     'superseded', 'era', 'since v', 'through v', 'from v', 'at v').
    # This is a report-and-fail check only; it never edits.
    import re as _re
    pyproject = (ROOT / "pyproject.toml").read_text()
    m = _re.search(r'version\s*=\s*"(\d+)\.(\d+)\.(\d+)"', pyproject)
    if m:
        cur = tuple(int(x) for x in m.groups())
        cur_str = f"{cur[0]}.{cur[1]}.{cur[2]}"
        # NOTE: "docs/history" is deliberately NOT a cue -- the release card
        # itself links into docs/history, and exempting the path would have
        # masked the exact v3.20.0 bug this tripwire exists to catch
        # (verified by negative test at v3.26.3).
        HISTORY_CUES = ("prior", "archived", "superseded", "-era",
                        "since v", "through v", "from v", "consolidat")
        stale_hits = []
        readme_text = (ROOT / "README.md").read_text()
        if cur_str not in readme_text:
            stale_hits.append(("README.md", 0,
                               f"current version v{cur_str} never mentioned"))
        for doc in (ROOT / "README.md", ROOT / "KNOWN_LIMITATIONS.md"):
            for i, line in enumerate(doc.read_text().splitlines(), 1):
                for vm in _re.finditer(r"v(\d+)\.(\d+)\.(\d+)", line):
                    ref = tuple(int(x) for x in vm.groups())
                    behind_minor = (cur[0] - ref[0]) * 1000 + (cur[1] - ref[1])
                    if behind_minor > 1:
                        low = line.lower()
                        if any(c in low for c in
                               (c.lower() for c in HISTORY_CUES)):
                            continue
                        stale_hits.append((doc.name, i,
                                           f"references v{'.'.join(map(str, ref))}"
                                           f" (current v{cur_str})"))
        # Badge check: the Verify badge count must equal the code-backed
        # count from claims.yaml (it sat at 411/411 for ~189 benchmarks
        # before this check existed).
        backed = sum(1 for c in claims if c.get("benchmark"))
        bm = _re.search(r"verify-(\d+)%2F(\d+)%20passing", readme_text)
        if bm and (int(bm.group(1)) != backed or int(bm.group(2)) != backed):
            stale_hits.append(("README.md", 0,
                               f"Verify badge says {bm.group(1)}/{bm.group(2)},"
                               f" registry has {backed} code-backed"))
        if stale_hits:
            any_drift = True
            for name, ln, msg in stale_hits:
                print(f"FRONTDOOR-STALE  {name}:{ln}: {msg}")
        else:
            print(f"ok     front-door version tripwire (current v{cur_str},"
                  f" badge {backed}/{backed})")
    # ------------------------------------------------------------------------

    if check and any_drift:
        sys.exit(1)


if __name__ == "__main__":
    main()
