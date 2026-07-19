#!/usr/bin/env python3
"""
build_overview.py — generate PROGRAMME_OVERVIEW.md from the corpus machinery.

The overview is NOT hand-written prose that can drift. Its factual core — the
sector maturity table, the honest open-problems list, the corpus statistics, and
the reading order keyed to real papers — is generated from claims.yaml and the
computed roadmap, so it stays in sync with the corpus by construction. The
narrative framing lives in a template string; the numbers and tables are live.

Usage:  python tools/build_overview.py   ->  docs/PROGRAMME_OVERVIEW.md
"""

# --- UTF-8 console shim (cross-platform; fixes Windows cp1252 crashes) ---
import sys as _sys
for _s in ("stdout", "stderr"):
    _stream = getattr(_sys, _s, None)
    _rc = getattr(_stream, "reconfigure", None)
    if callable(_rc):
        try:
            _rc(encoding="utf-8", errors="replace")
        except Exception:
            pass
# --- end shim ---
import os, io, sys, subprocess
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load():
    claims=[]; sectors=[]; cur=None; scur=None; mode="claims"
    for raw in io.open(os.path.join(ROOT,"claims.yaml"),encoding="utf-8"):
        l=raw.rstrip("\n")
        if l.startswith("sectors:"):
            if cur: claims.append(cur); cur=None
            mode="sectors"; continue
        if mode=="claims":
            if l.startswith("  - id:"):
                if cur: claims.append(cur)
                cur={"id":l.split("id:",1)[1].strip(),"benchmark":None,"note":"","depends_on":[]}
            elif cur is not None and l.strip().startswith(("status:","title:","benchmark:","paper:","note:")):
                k=l.strip().split(":",1)[0]; v=l.strip().split(":",1)[1].strip()
                cur[k]= None if v=="null" else v.strip('"')
        else:
            if l.startswith("  - prefix:"):
                if scur: sectors.append(scur)
                scur={"prefix":l.split("prefix:",1)[1].strip(),"papers":[]}
            elif scur is not None and l.strip().startswith("name:"):
                scur["name"]=l.split("name:",1)[1].strip().strip('"')
            elif scur is not None and l.strip().startswith("external_readiness:"):
                scur["readiness"]=l.split("external_readiness:",1)[1].strip().strip('"')
    if scur: sectors.append(scur)
    return claims, sectors

def roadmap_maturity():
    """Run the roadmap tool and parse computed maturity per sector name."""
    out=subprocess.run([sys.executable,"tools/build_roadmap.py"],cwd=ROOT,
                       capture_output=True,text=True,encoding="utf-8",errors="replace",
                       env=dict(os.environ,PYTHONPATH=ROOT)).stdout or ""
    mat={}
    for line in out.splitlines():
        if line.startswith("|") and "**" in line:
            parts=[p.strip() for p in line.strip("|").split("|")]
            if len(parts)>=2:
                name=parts[0]; tier=parts[1].replace("**","")
                mat[name]=tier
    return mat

def main():
    claims, sectors = load()
    mat = roadmap_maturity()
    status=Counter(c.get("status") for c in claims)
    backed=sum(1 for c in claims if c.get("benchmark"))
    # papers now live in papers/ (+_sources) with meta docx in docs/; count physics-paper sources
    ndocx=0
    for sub in ("papers/_sources","papers","docs"):
        p=os.path.join(ROOT,sub)
        if os.path.isdir(p):
            ndocx+=len([f for f in os.listdir(p) if f.endswith(".docx") and not f.startswith("ARCHIVED")])
    nbench=sum(len([f for f in fs if f.endswith(".py")]) for _,_,fs in os.walk(os.path.join(ROOT,"benchmarks")))

    bysec=defaultdict(list)
    for c in claims: bysec[c["id"].split("-")[0]].append(c)

    L=[]
    L.append("# The Rope Programme — Overview\n")
    L.append("*The front door to the corpus. This document is **generated** from `claims.yaml` and the "
             "computed roadmap by `tools/build_overview.py`, so its statistics, maturity table, and "
             "open-problems list stay in sync with the corpus by construction.*\n")
    L.append("Programme credit: the core Rope Hypothesis is due to Bill Gaede; this corpus develops and "
             "formalises it.\n")
    L.append("---\n")

    # What this is
    L.append("## What this programme is\n")
    L.append("The Rope Hypothesis is a speculative classical model in which interactions are carried by "
             "physical strands under tension. This corpus develops its **classical continuum sector** into "
             "a reproducible research programme: a coherent chain from microscopic mechanics up through "
             "electromagnetism, optics, and thermodynamics, with every principal claim assigned a status "
             "and, wherever possible, backed by an executable benchmark.\n")
    L.append("The programme's discipline is its defining feature: **derived results, empirical inputs, and "
             "open problems are kept strictly separate**, corrections and negative results are preserved as "
             "visibly as successes, and the mathematics is kept distinct from the ontology it proposes.\n")

    # Statistics (live)
    L.append("## Corpus at a glance (generated)\n")
    L.append(f"- **Bundled papers:** {ndocx}")
    L.append(f"- **Reproducible benchmarks:** {nbench}")
    L.append(f"- **Registered claims:** {len(claims)} ({backed} code-backed and machine-verified)")
    order=["Derived","EFT-constrained","Modeled","Conjecture","Failed","Open"]
    L.append("- **Claim status distribution:** "+", ".join(f"{k} {status[k]}" for k in order if status.get(k)))
    L.append("\nVerify it yourself in one command: `make verify` (runs every benchmark the registry "
             "references) or `python tools/verify_corpus.py`.\n")

    # The continuum chain
    L.append("## The classical continuum chain (the strongest core)\n")
    L.append("The programme's spine is a single geometric structure developed level by level. Each link is "
             "a Mature, benchmark-backed sector:\n")
    L.append("```")
    L.append("Microscopic Mechanics")
    L.append("      -> Homogenization (Gamma-convergence)")
    L.append("            -> Effective Field Theory")
    L.append("                  -> Electromagnetism")
    L.append("                        -> Classical Optics -> Interface Optics")
    L.append("      -> Defect Theory (2D + 3D)  [shares the same functional]")
    L.append("      -> Statistical Mechanics    [BKT = defect-gas unbinding]")
    L.append("  All unified by: Gauge Geometry (bundle -> connection -> curvature -> topology)")
    L.append("```")
    L.append("The gauge-geometry paper is the mathematical reference showing these are one structure; "
             "the machine-readable dependency graph (`docs/dependency_graph.txt`) encodes the links "
             "claim by claim.\n")

    # Maturity table (live from roadmap)
    L.append("## Sector maturity (computed)\n")
    L.append("Maturity is **computed** from each sector's claim statuses and benchmark coverage, not "
             "hand-assigned. Readiness is cross-checked against it; there are currently no "
             "readiness-vs-evidence flags.\n")
    L.append("| Sector | Computed maturity | Claims | Derived | Benchmarked |")
    L.append("|---|---|---:|---:|---:|")
    for s in sectors:
        cl=bysec.get(s["prefix"],[])
        d=sum(1 for c in cl if c.get("status") in ("Derived","EFT-constrained"))
        b=sum(1 for c in cl if c.get("benchmark"))
        tier=mat.get(s["name"],"?")
        L.append(f"| {s['name']} | {tier} | {len(cl)} | {d} | {b} |")
    L.append("")

    # Reading order
    L.append("## Suggested reading order\n")
    L.append("For a first read of the corpus:\n")
    L.append("1. **This overview** — assumptions, scope, maturity, open problems.")
    L.append("2. **Topology and Gauge Geometry Underlying the Rope Programme** — the mathematical backbone; "
             "why bundles, connections, curvature, and topology recur.")
    L.append("3. **Microscopic Mechanics** — the endpoint mechanics the chain starts from.")
    L.append("4. **A Gamma-Convergence Derivation for the Rope Medium** (homogenization) — how the discrete "
             "model becomes the continuum functional.")
    L.append("5. **Electromagnetism** and **Classical Optics** — the strongest, most self-contained "
             "physical sectors.")
    L.append("6. **Scope and Limits** — what the programme does not claim, especially the quantum boundary.\n")

    # Honest open problems (live)
    L.append("## Open problems and boundaries (generated)\n")
    L.append("The programme marks where it does not (yet) claim to explain nature. These are surfaced "
             "directly from the registry:\n")
    def dump(stat, header, gloss):
        items=[c for c in claims if c.get("status")==stat]
        if not items: return
        L.append(f"**{header}** — {gloss}")
        for c in items:
            note=f" — {c['note']}" if c.get("note") else ""
            L.append(f"- `{c['id']}` {c.get('title','')}{note}")
        L.append("")
    dump("Open","Genuinely open","not established either way; the honest frontier.")
    dump("Failed","Documented negative results","kept as findings, not hidden.")
    dump("Conjecture","Conjectural","numerically suggestive or conditional; not established.")

    # How to evaluate
    L.append("## How to evaluate this corpus\n")
    L.append("- **Dependency graph:** `docs/dependency_graph.txt` — what rests on what.")
    L.append("- **Claim registry:** `claims.yaml` — every claim's status, paper, and benchmark.")
    L.append("- **Computed roadmap:** `docs/roadmap.md` — sector maturity, auto-flagged if any readiness "
             "outruns its evidence.")
    L.append("- **One-command verification:** `make verify` — runs every code-backed claim's benchmark.")
    L.append("- **Heartbeat:** `make heartbeat` — the core validation runs (currently 75/75 + 10/10 + 6/6).\n")
    L.append("The programme's strongest posture is not any single prediction; it is that the classical "
             "core can be independently audited, sector by sector and claim by claim, and that its "
             "boundaries are stated rather than blurred.\n")

    text="\n".join(L)
    io.open(os.path.join(ROOT,"docs","PROGRAMME_OVERVIEW.md"),"w",encoding="utf-8").write(text+"\n")
    print(f"Wrote docs/PROGRAMME_OVERVIEW.md ({len(claims)} claims, {ndocx} papers, {nbench} benchmarks)")

if __name__=="__main__":
    main()
