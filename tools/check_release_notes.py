#!/usr/bin/env python3
"""Release-notes completeness check (house convention guard).

Every minor release cut (X.Y.0) recorded in CHANGELOG.md must have a
matching docs/history/RELEASE_NOTES_vX.Y.0.md. Patch versions
(X.Y.Z, Z > 0) are working versions and owe no file. Exits nonzero
listing every missing file, so CI fails the build the moment a cut
lands without its notes.

Also checks the reverse direction: a notes file whose version never
appears in the CHANGELOG is flagged (stale or typo), as a warning
only (exit 0), since history files may legitimately predate the
current CHANGELOG's horizon.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FLOOR = (3, 18)   # convention enforced from v3.18.0 onward

def main():
    text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    cut = set()
    for m in re.finditer(r"^##\s+v?(\d+)\.(\d+)\.0(?:\s|$)", text, re.M):
        maj, minor = int(m.group(1)), int(m.group(2))
        if (maj, minor) >= FLOOR:
            cut.add((maj, minor))
    hist = ROOT / "docs" / "history"
    have = set()
    for p in hist.glob("RELEASE_NOTES_v*.md"):
        m = re.match(r"RELEASE_NOTES_v(\d+)\.(\d+)\.0\.md$", p.name)
        if m:
            have.add((int(m.group(1)), int(m.group(2))))
    missing = sorted(cut - have)
    def recorded_anywhere(maj, minor):
        return re.search(rf"^#{{2,4}}\s+v?{maj}\.{minor}\.0\b", text, re.M) is not None
    orphans = sorted(v for v in have
                     if v >= FLOOR and v not in cut
                     and not recorded_anywhere(*v))
    for maj, minor in orphans:
        print(f"WARNING: docs/history/RELEASE_NOTES_v{maj}.{minor}.0.md "
              f"has no CHANGELOG record at any heading level")
    if missing:
        for maj, minor in missing:
            print(f"MISSING: docs/history/RELEASE_NOTES_v{maj}.{minor}.0.md "
                  f"(CHANGELOG cuts v{maj}.{minor}.0)")
        print(f"\n{len(missing)} release cut(s) lack notes. The convention: "
              "every X.Y.0 entry in CHANGELOG.md ships with its "
              "docs/history file, written at the cut, not backfilled.")
        return 1
    print(f"release-notes check: {len(cut)} cuts since v{FLOOR[0]}.{FLOOR[1]}.0, all have notes. OK")
    return 0

if __name__ == "__main__":
    sys.exit(main())
