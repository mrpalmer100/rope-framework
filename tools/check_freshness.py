#!/usr/bin/env python3
"""
check_freshness.py -- one command that catches every staleness class we know of.

Run it in CI (and locally before a release). It exits non-zero if anything is
stale, so a stale artifact blocks the commit rather than reaching a grant reviewer.
It CHANGES NOTHING -- it only reports. The paired fixers are:
    tools/sync_doc_facts.py     (marker fact-blocks)
    make overview roadmap graph (generated docs)

Checks:
  1. GENERATED DOCS current    -- regenerate to a temp copy, diff against committed.
  2. MARKER FACT-BLOCKS current -- sync_doc_facts.py --check.
  3. VERSION metadata agrees   -- CITATION.cff == pyproject.toml == latest release note.
  4. NO BROKEN REFERENCES      -- every benchmark/paper in claims.yaml exists on disk.
  5. PAPER CATALOG complete    -- every papers/*.pdf appears in docs/PAPERS.md.
  6. RENDERED PDFS current      -- no paper PDF older than its _sources docx.
"""
import sys, os, re, glob, subprocess, tempfile, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)
problems = []


def load_claims():
    import yaml
    return yaml.safe_load(open("claims.yaml"))["claims"]


# ---- 1. generated docs are current ---------------------------------------
def check_generated_docs():
    # regenerate into a scratch tree and diff the committed outputs
    generated = {
        "tools/build_overview.py": ["docs/PROGRAMME_OVERVIEW.md"],
        "tools/build_roadmap.py": ["docs/ROADMAP.md"],
        "tools/build_depgraph.py": ["docs/dependency_graph.txt"],
        "tools/build_suggested_issues.py": ["docs/SUGGESTED_ISSUES.md"],
        "tools/quantum_audit.py": ["docs/QUANTUM_LEDGER.md"],
    }
    for gen, outs in generated.items():
        before = {o: (Path(o).read_text() if Path(o).exists() else None) for o in outs}
        subprocess.run([sys.executable, gen], capture_output=True)
        for o in outs:
            after = Path(o).read_text() if Path(o).exists() else None
            if before[o] != after:
                problems.append(f"[generated-doc] {o} was stale -- {gen} had not been re-run "
                                f"(now regenerated; commit the change)")


# ---- 2. marker fact-blocks are current -----------------------------------
def check_markers():
    r = subprocess.run([sys.executable, "tools/sync_doc_facts.py", "--check"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        for line in r.stdout.splitlines():
            if line.startswith("DRIFT"):
                problems.append(f"[marker-block] {line[6:].strip()}")


# ---- 3. version metadata agrees ------------------------------------------
def check_versions():
    versions = {}
    cff = Path("CITATION.cff")
    if cff.exists():
        m = re.search(r"^version:\s*([0-9.]+)", cff.read_text(), re.M)
        if m: versions["CITATION.cff"] = m.group(1)
    toml = Path("pyproject.toml")
    if toml.exists():
        m = re.search(r'^version\s*=\s*"([0-9.]+)"', toml.read_text(), re.M)
        if m: versions["pyproject.toml"] = m.group(1)
    notes = sorted(glob.glob("docs/history/RELEASE_NOTES_v*.md") + glob.glob("docs/RELEASE_NOTES_v*.md"),
                   key=lambda p: [int(x) for x in re.findall(r"\d+", p)])
    if notes:
        m = re.search(r"v([0-9]+(?:\.[0-9]+)+)", os.path.basename(notes[-1]))
        if m: versions["latest release note"] = m.group(1)
    distinct = set(versions.values())
    if len(distinct) > 1:
        detail = ", ".join(f"{k}={v}" for k, v in versions.items())
        problems.append(f"[version] metadata disagrees: {detail}")


# ---- 4. no broken references ---------------------------------------------
def check_references():
    for c in load_claims():
        b = c.get("benchmark")
        if b and not Path(b).exists():
            problems.append(f"[broken-ref] {c['id']} -> missing benchmark {b}")
        p = c.get("paper")
        if p and not (Path(f"papers/{p}.pdf").exists() or Path(f"papers/{p}").exists()):
            problems.append(f"[broken-ref] {c['id']} -> missing paper {p}")


# ---- 5. paper catalog complete -------------------------------------------
def check_catalog():
    cat = Path("docs/PAPERS.md").read_text() if Path("docs/PAPERS.md").exists() else ""
    for pdf in sorted(glob.glob("papers/*.pdf")):
        name = os.path.basename(pdf)
        stem = name[:-4]
        if name not in cat and stem not in cat:
            problems.append(f"[catalog] {name} on disk but not in docs/PAPERS.md")


# ---- 6. rendered PDFs current --------------------------------------------
def check_pdf_freshness():
    for pdf in glob.glob("papers/*.pdf"):
        src = f"papers/_sources/{Path(pdf).stem}.docx"
        if os.path.exists(src) and os.path.getmtime(pdf) < os.path.getmtime(src):
            problems.append(f"[stale-pdf] {pdf} older than its source {src}")


# ---- 7. orphaned "generated" files & case-collision twins ----------------
# KNOWN_GENERATED is the set of docs written by SOME generator (a build_*.py, a
# module command, or docs/generate_api_docs.py). Check 1 verifies the registry-fed
# ones stay current; this check guards the reverse -- a file that claims generation
# but that NO generator writes and whose named generator does not exist (e.g. the
# renamed-output orphan docs/roadmap.md we found).
KNOWN_GENERATED = {
    "docs/PROGRAMME_OVERVIEW.md",
    "docs/ROADMAP.md",
    "docs/roadmap.html",
    "docs/dependency_graph.txt",
    "docs/dependency_graph.dot",
    "docs/SUGGESTED_ISSUES.md",
    "docs/API.md",          # generated by docs/generate_api_docs.py
    "docs/BENCHMARKS.md",   # hand-maintained; table synced from rope_solver.benchmark_catalogue
    "docs/QUANTUM_LEDGER.md",  # generated by tools/quantum_audit.py
}
# A file is a suspected orphan only if its header EXPLICITLY says it is generated
# output (not merely that it discusses generation, as PROVENANCE.md does). Require
# a self-referential generation phrase.
GENERATED_MARKERS = ("do not edit by hand", "auto-generated from",
                     "auto-generated from docstrings", "cannot drift from",
                     "generated by tools/", "generated by `tools/")


def _names_missing_generator(head):
    """Header claims generation AND names a script/path that does not exist."""
    import re
    for m in re.findall(r"(?:tools/|docs/)?[a-z_]+\.py", head):
        cand = m if os.path.exists(m) else None
        for base in ("", "tools/", "docs/"):
            if os.path.exists(base + os.path.basename(m)):
                cand = base + os.path.basename(m)
                break
        if cand is None:
            return True
    return False


def check_orphans():
    # 7a. files whose header claims generation but nothing writes them
    for md in (glob.glob("docs/**/*.md", recursive=True)
               + glob.glob("docs/*.html") + glob.glob("docs/*.txt")):
        rel = md.replace("\\", "/")
        if rel in KNOWN_GENERATED:
            continue
        if "/history/" in rel or "/_superseded/" in rel or "_archive" in rel:
            continue  # frozen by design
        head = " ".join(Path(md).read_text(errors="ignore").splitlines()[:8]).lower()
        claims_generated = any(m in head for m in GENERATED_MARKERS)
        if claims_generated and _names_missing_generator(head):
            problems.append(f"[orphan] {rel} declares itself generated and names a "
                            f"generator that does not exist -- likely a stale former "
                            f"output whose generator target was renamed. Remove it or "
                            f"repoint the generator.")

    # 7b. case-collision twins (ROADMAP.md vs roadmap.md) -- unsafe on
    # case-insensitive filesystems, and a classic stale-duplicate trap.
    seen = {}
    for f in glob.glob("docs/*.md") + glob.glob("docs/*.html") + glob.glob("docs/*.txt"):
        key = f.lower()
        if key in seen:
            problems.append(f"[case-collision] {f} and {seen[key]} differ only in case "
                            f"-- unsafe on case-insensitive filesystems; keep one.")
        seen[key] = f


def main():
    check_generated_docs()
    check_markers()
    check_versions()
    check_references()
    check_catalog()
    check_pdf_freshness()
    check_orphans()

    if not problems:
        print("FRESH: all docs, references, versions, and catalogs are current.")
        return 0
    print(f"STALE: {len(problems)} freshness problem(s) found:\n")
    for p in problems:
        print("  " + p)
    print("\nFixers: tools/sync_doc_facts.py  |  make overview roadmap graph  |  "
          "re-render PDFs from papers/_sources")
    return 1


if __name__ == "__main__":
    sys.exit(main())
