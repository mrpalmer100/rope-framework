#!/usr/bin/env python3
"""
build_roadmap.py — compute the sector maturity roadmap from claims.yaml.

Maturity is DERIVED, not asserted: each sector's tier follows from the status
mix and benchmark coverage of its claims. The tool then cross-checks the
sector's stated 'external_readiness' against the computed evidence and FLAGS any
sector whose readiness outruns its backing (e.g. a 'Ready' sector whose main
claims have no benchmark). This keeps the roadmap honest and in sync with the
corpus automatically.

Outputs:
  docs/roadmap.md   (the computed maturity table + flags)
  stdout            (same, for quick inspection)

Usage:  python tools/build_roadmap.py
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
import os, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load():
    """Parse claims + sectors from claims.yaml (no PyYAML dependency)."""
    claims=[]; sectors=[]; cur=None; mode="claims"; scur=None
    for raw in open(os.path.join(ROOT,"claims.yaml"),encoding="utf-8"):
        line=raw.rstrip("\n")
        if line.startswith("sectors:"): mode="sectors"; 
        if mode=="claims":
            if line.startswith("  - id:"):
                if cur: claims.append(cur)
                cur={"id":line.split("id:",1)[1].strip(),"benchmark":None,"depends_on":[]}
            elif cur is not None and line.strip().startswith(("status:","benchmark:","paper:")):
                k=line.strip().split(":",1)[0]; v=line.strip().split(":",1)[1].strip()
                cur[k]= None if v=="null" else v.strip('"')
        else:  # sectors
            if line.startswith("  - prefix:"):
                if scur: sectors.append(scur)
                scur={"prefix":line.split("prefix:",1)[1].strip(),"papers":[]}
            elif scur is not None and line.strip().startswith("name:"):
                scur["name"]=line.split("name:",1)[1].strip().strip('"')
            elif scur is not None and line.strip().startswith("external_readiness:"):
                scur["external_readiness"]=line.split("external_readiness:",1)[1].strip().strip('"')
            elif scur is not None and line.strip().startswith("papers:"):
                v=line.split("papers:",1)[1].strip()
                scur["papers"]=[x.strip() for x in v.strip("[]").split(",") if x.strip()]
    if cur and cur not in claims and "sectors:" not in str(cur): 
        # ensure last claim (only if we never entered sectors after it)
        pass
    if scur: sectors.append(scur)
    # re-collect claims cleanly (the last claim before sectors:)
    claims2=[]; cur=None; mode="claims"
    for raw in open(os.path.join(ROOT,"claims.yaml"),encoding="utf-8"):
        line=raw.rstrip("\n")
        if line.startswith("sectors:"): 
            if cur: claims2.append(cur); cur=None
            break
        if line.startswith("  - id:"):
            if cur: claims2.append(cur)
            cur={"id":line.split("id:",1)[1].strip(),"benchmark":None}
        elif cur is not None and line.strip().startswith(("status:","benchmark:")):
            k=line.strip().split(":",1)[0]; v=line.strip().split(":",1)[1].strip()
            cur[k]= None if v=="null" else v.strip('"')
    if cur: claims2.append(cur)
    return claims2, sectors

# Maturity is computed from these rules (documented so it's auditable):
def compute_maturity(cl):
    """Return (tier, rationale) from a sector's claims."""
    n=len(cl)
    if n==0: return "Empty","no claims"
    statuses=[c.get("status") for c in cl]
    benched=sum(1 for c in cl if c.get("benchmark"))
    cov=benched/n
    solid=sum(1 for s in statuses if s in ("Derived","EFT-constrained"))
    failed=sum(1 for s in statuses if s=="Failed")
    openc=sum(1 for s in statuses if s=="Open")
    conj=sum(1 for s in statuses if s=="Conjecture")
    solid_frac=solid/n

    # A sector dominated by Failed/Open with a clear documented boundary is
    # "Mature (boundary)" — a strong negative result, not immature.
    if failed+openc >= n*0.5 and solid>=1:
        return "Mature (boundary)", f"{solid} derived + {failed} failed/{openc} open, documented limit"
    # Conjecture-dominated = Exploratory regardless of prose
    if conj >= n*0.5:
        return "Exploratory", f"{conj}/{n} conjectural"
    # High maturity needs BOTH mostly-solid statuses AND real benchmark coverage
    if solid_frac>=0.66 and cov>=0.5:
        return "Mature", f"{solid}/{n} derived/EFT, {benched}/{n} benchmark-backed"
    if solid_frac>=0.5 and cov>=0.5:
        return "Mature (conditional)", f"{solid}/{n} solid, {benched}/{n} benchmarked"
    # Solid statuses but THIN benchmark coverage -> conceptually strong, evidence thin
    if solid_frac>=0.5 and cov<0.5:
        return "Conceptually strong, thin backing", f"{solid}/{n} solid but only {benched}/{n} benchmark-backed"
    return "Developing", f"{solid}/{n} solid, {benched}/{n} benchmarked"

# Which computed tiers legitimately support which readiness levels
READY_OK = {
 "Mature","Mature (boundary)","Mature (conditional)"
}

def main():
    claims, sectors = load()
    bysec=defaultdict(list)
    for c in claims: bysec[c["id"].split("-")[0]].append(c)

    rows=[]; flags=[]
    for s in sectors:
        cl=bysec.get(s["prefix"],[])
        tier,rat=compute_maturity(cl)
        readiness=s.get("external_readiness","?")
        # flag: readiness says "Ready..." but computed tier is not Ready-eligible
        says_ready = readiness.lower().startswith("ready")
        if says_ready and tier not in READY_OK:
            flags.append((s["name"],tier,readiness,rat))
        rows.append((s["name"],tier,readiness,len(cl),rat))

    # emit markdown
    md=["# The Rope Programme — Computed Sector Roadmap","",
        "*Maturity is computed by `tools/build_roadmap.py` from the status and benchmark",
        "coverage of each sector's claims in `claims.yaml`. It is not hand-assigned, so it",
        "cannot drift from the corpus. Readiness labels are cross-checked against computed",
        "maturity; mismatches are flagged below.*","",
        "| Sector | Computed maturity | Stated readiness | Claims | Basis |",
        "|---|---|---|---:|---|"]
    for name,tier,readiness,n,rat in rows:
        md.append(f"| {name} | **{tier}** | {readiness} | {n} | {rat} |")
    md.append("")
    if flags:
        md.append("## ⚠ Readiness-vs-evidence flags")
        md.append("")
        md.append("These sectors state an external readiness that the computed maturity does "
                  "not yet fully support. This is a prompt to either add benchmark backing or "
                  "soften the readiness label — not a claim the physics is wrong.")
        md.append("")
        for name,tier,readiness,rat in flags:
            md.append(f"- **{name}**: stated *{readiness}*, but computed *{tier}* ({rat}). "
                      "Add benchmark-backed claims or relabel.")
    else:
        md.append("## Readiness-vs-evidence flags\n\nNone — every stated readiness is supported by computed maturity.")
    md.append("")
    md.append("### How maturity is computed (auditable rules)")
    md.append("- **Mature (boundary)**: ≥half claims Failed/Open *with* ≥1 solid result — a "
              "documented limit (e.g. the Bell/quantum boundary). A strong negative result.")
    md.append("- **Mature**: ≥2/3 claims Derived/EFT-constrained *and* ≥half benchmark-backed.")
    md.append("- **Conceptually strong, thin backing**: ≥half solid statuses but <half "
              "benchmark-backed — a flag to add executable backing.")
    md.append("- **Exploratory**: ≥half claims Conjecture.")
    md.append("")

    text="\n".join(md)
    with open(os.path.join(ROOT,"docs","roadmap.md"),"w") as f: f.write(text+"\n")
    print(text)
    print("\n(written to docs/roadmap.md)")
    return 0

if __name__=="__main__":
    sys.exit(main())
