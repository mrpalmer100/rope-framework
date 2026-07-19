#!/usr/bin/env python3
"""
build_depgraph.py — emit the claim dependency graph from claims.yaml.

Produces:
  docs/dependency_graph.dot   (Graphviz DOT; render with `dot -Tpng`)
  docs/dependency_graph.txt   (ASCII, for reading without Graphviz)

The graph shows what each result rests on, so a reviewer can see at a glance
that (for example) electromagnetism and thermodynamics both descend from the
Gamma-convergence result, which descends from the microscopic mechanics — while
gravity and the soliton spectrum sit on independent roots.

Usage:  python tools/build_depgraph.py
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
    path=os.path.join(ROOT,"claims.yaml")
    claims=[]; cur=None; in_dep=False
    for raw in open(path,encoding="utf-8"):
        line=raw.rstrip("\n")
        if line.startswith("  - id:"):
            if cur: claims.append(cur)
            cur={"id":line.split("id:",1)[1].strip(),"depends_on":[]}; in_dep=False
        elif cur is not None and line.strip().startswith("depends_on:"):
            v=line.split("depends_on:",1)[1].strip()
            if v.startswith("[") and v!="[]":
                cur["depends_on"]=[x.strip() for x in v.strip("[]").split(",") if x.strip()]
        elif cur is not None and ":" in line and line.startswith("    "):
            k=line.strip().split(":",1)[0].strip(); val=line.strip().split(":",1)[1].strip()
            if k in ("title","status","paper"): cur[k]=val.strip('"')
    if cur: claims.append(cur)
    return claims

STATUS_COLOR={"Derived":"#2E6E4F","EFT-constrained":"#2E4057","Modeled":"#1F3864",
    "Conjecture":"#B8860B","Failed":"#7B2D26","Open":"#666666"}

def emit_dot(claims):
    lines=["digraph RopeCorpus {","  rankdir=TB;","  node [shape=box style=filled fontname=Helvetica fontsize=10 fontcolor=white];","  edge [color=\"#888888\"];"]
    for c in claims:
        col=STATUS_COLOR.get(c.get("status"),"#333333")
        label=f"{c['id']}\\n{c.get('status','?')}"
        lines.append(f'  "{c["id"]}" [fillcolor="{col}" label="{label}"];')
    for c in claims:
        for d in c.get("depends_on",[]):
            lines.append(f'  "{d}" -> "{c["id"]}";')
    lines.append("}")
    return "\n".join(lines)

def emit_ascii(claims):
    by_id={c["id"]:c for c in claims}
    children=defaultdict(list)
    roots=[]
    for c in claims:
        deps=c.get("depends_on",[])
        if not deps: roots.append(c["id"])
        for d in deps: children[d].append(c["id"])
    out=["Rope Programme — claim dependency graph","="*60,
         "(roots have no dependencies; arrows = 'is required by')",""]
    seen=set()
    def walk(cid,depth):
        c=by_id[cid]
        bullet="  "*depth+("└─ " if depth>0 else "")
        tag=f"[{c.get('status','?')}]"
        out.append(f"{bullet}{cid} {tag} {c.get('title','')[:52]}")
        if cid in seen:
            if children[cid]: out.append("  "*(depth+1)+"(deps shown above)")
            return
        seen.add(cid)
        for ch in children[cid]:
            walk(ch,depth+1)
    for r in roots:
        walk(r,0); out.append("")
    # legend
    out.append("Status legend: Derived / EFT-constrained / Modeled / Conjecture / Failed / Open")
    return "\n".join(out)

def main():
    claims=load()
    dot=emit_dot(claims); ascii_=emit_ascii(claims)
    with open(os.path.join(ROOT,"docs","dependency_graph.dot"),"w") as f: f.write(dot+"\n")
    with open(os.path.join(ROOT,"docs","dependency_graph.txt"),"w") as f: f.write(ascii_+"\n")
    print(f"Wrote docs/dependency_graph.dot and docs/dependency_graph.txt ({len(claims)} nodes)")
    print("Render the graph with:  dot -Tpng docs/dependency_graph.dot -o docs/dependency_graph.png")
    print()
    print(ascii_)

if __name__=="__main__":
    main()
