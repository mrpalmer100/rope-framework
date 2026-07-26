#!/usr/bin/env python3
"""Generate the Roadmap of Knowledge from claims.yaml:
docs/roadmap.png (wall chart), docs/roadmap.html (interactive explorer),
docs/ROADMAP.md (textual map). Run from repo root."""
import yaml, re, json, html
from collections import defaultdict, Counter

SECTORS = [
    ("Foundations",        ["FND","FND-KIN","FND-STRAND","FND-REL","FND-BOUND","THM","EFT","CM","SOL"]),
    ("Electromagnetism",   ["EM","EM-RECON","EW"]),
    ("Optics",             ["OPT"]),
    ("Matter & Particles", ["FND-MATTER","PM","NUC"]),
    ("Chemistry",          ["CHEM-HB","CHEM-DYN","CHEM-GEO","CHEM-STRUCT","CHEM-MET"]),
    ("Gravity & Galaxies", ["GRV","GG"]),
    ("Quantum Boundary",   ["QB"]),
]
COLORS = {"Derived":"#2e8b57","Modeled":"#2b6cb0","EFT-constrained":"#6b46c1",
          "Conjecture":"#d69e2e","Open":"#ecc94b","Failed":"#c53030"}

def sector_of(cid):
    pre = re.match(r'([A-Z\-]+?)-\d', cid)
    p = pre.group(1) if pre else cid
    for name, pres in SECTORS:
        if p in pres:
            return name
    return "Foundations"

def load():
    d = yaml.safe_load(open('claims.yaml'))
    return d['claims'] if isinstance(d, dict) and 'claims' in d else d

def build():
    claims = load()
    for c in claims:
        c['sector'] = sector_of(c['id'])
    by_sector = defaultdict(list)
    for c in claims:
        by_sector[c['sector']].append(c)
    ids = {c['id']: c for c in claims}
    downstream = defaultdict(list)
    for c in claims:
        for dep in (c.get('depends_on') or []):
            downstream[dep].append(c['id'])

    # ---------- PNG wall chart ----------
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.patches as mp
    ncols = 26
    rowh = 0.62
    heights = {name: (len(by_sector[name]) + ncols - 1)//ncols for name, _ in SECTORS}
    total_rows = sum(heights[n] for n, _ in SECTORS)
    fig_h = 2.2 + total_rows*rowh*0.42 + len(SECTORS)*0.66
    fig, ax = plt.subplots(figsize=(15, fig_h))
    ax.set_xlim(0, ncols + 6.5); ax.axis('off')
    y = 0.0
    sector_edges = Counter()
    for c in claims:
        for dep in (c.get('depends_on') or []):
            s1, s2 = ids[dep]['sector'], c['sector']
            if s1 != s2:
                sector_edges[(s1, s2)] += 1
    for name, _ in SECTORS[::-1]:
        cs = sorted(by_sector[name], key=lambda c: c['id'])
        rows = heights[name]
        stat = Counter(c['status'] for c in cs)
        for k, c in enumerate(cs):
            cx, cy = k % ncols, y + (rows - 1 - k//ncols)*rowh
            ax.add_patch(mp.FancyBboxPatch((cx, cy), 0.88, 0.5,
                boxstyle="round,pad=0.02,rounding_size=0.06",
                fc=COLORS[c['status']], ec='white', lw=0.6))
        label = f"{name}  ({len(cs)})"
        sub = "  ".join(f"{s}:{n}" for s, n in stat.most_common())
        ax.text(ncols + 0.4, y + rows*rowh/2 + 0.16, label, fontsize=12.5,
                fontweight='bold', va='center')
        ax.text(ncols + 0.4, y + rows*rowh/2 - 0.28, sub, fontsize=8.2,
                va='center', color='#444444')
        y += rows*rowh + 0.62
    total = len(claims); stat = Counter(c['status'] for c in claims)
    ax.set_ylim(-1.6, y + 1.2)
    ax.text(0, y + 0.55, "THE ROPE PROGRAMME — ROADMAP OF KNOWLEDGE",
            fontsize=17, fontweight='bold')
    ax.text(0, y + 0.1,
            f"{total} registered claims · " + " · ".join(f"{s} {n}" for s, n in stat.most_common())
            + "   (generated from claims.yaml)", fontsize=10, color='#333333')
    lx = 0
    for s, col in COLORS.items():
        ax.add_patch(mp.FancyBboxPatch((lx, -1.25), 0.7, 0.42,
            boxstyle="round,pad=0.02,rounding_size=0.06", fc=col, ec='white'))
        ax.text(lx + 0.85, -1.04, s, fontsize=9, va='center')
        lx += 0.95 + 0.16*len(s)
    fig.savefig('docs/roadmap.png', dpi=150, bbox_inches='tight')
    plt.close(fig)

    # ---------- interactive HTML ----------
    data = [{"id": c['id'], "t": c['title'][:400], "s": c['status'],
             "sec": c['sector'], "b": c.get('benchmark') or "",
             "d": c.get('depends_on') or [], "dn": downstream.get(c['id'], [])}
            for c in claims]
    payload = json.dumps(data)
    colors_js = json.dumps(COLORS)
    sectors_js = json.dumps([n for n, _ in SECTORS])
    page = """<!DOCTYPE html><html><head><meta charset="utf-8">
<title>Rope Programme — Roadmap of Knowledge</title>
<style>
body{font-family:Georgia,serif;margin:0;display:flex;height:100vh}
#map{flex:1;overflow:auto;padding:18px;background:#fafaf7}
#panel{width:390px;border-left:1px solid #ddd;padding:16px;overflow:auto;background:#fff}
h1{font-size:19px;margin:2px 0 4px}
.meta{color:#555;font-size:12px;margin-bottom:10px}
.sector{margin:14px 0 4px;font-weight:bold;font-size:14px}
.dot{display:inline-block;width:15px;height:15px;margin:1.5px;border-radius:3px;cursor:pointer;border:1.5px solid transparent}
.dot.up{border-color:#000}
.dot.down{border-color:#c53030;border-style:dashed}
.dot.sel{outline:2.5px solid #000}
#panel h2{font-size:14px;margin:4px 0}
#panel .st{display:inline-block;padding:1px 8px;border-radius:9px;color:#fff;font-size:11px}
#panel .tt{font-size:12.5px;line-height:1.45;margin:8px 0}
#panel .lk{font-size:12px;color:#2b6cb0;cursor:pointer;text-decoration:underline}
#panel code{font-size:11px;background:#f2f2ee;padding:1px 4px}
.legend span{display:inline-block;margin-right:10px;font-size:11px}
.legend i{display:inline-block;width:11px;height:11px;border-radius:2px;margin-right:3px;vertical-align:-1px}
</style></head><body>
<div id="map"><h1>The Rope Programme — Roadmap of Knowledge</h1>
<div class="meta" id="meta"></div><div class="legend" id="legend"></div><div id="grid"></div></div>
<div id="panel"><em>Click any claim. Solid outline = its dependencies (upstream); dashed red = everything built on it (direct downstream).</em></div>
<script>
const DATA=__DATA__;const COLORS=__COLORS__;const SECTORS=__SECTORS__;
const byId={};DATA.forEach(c=>byId[c.id]=c);
const counts={};DATA.forEach(c=>counts[c.s]=(counts[c.s]||0)+1);
document.getElementById('meta').textContent=DATA.length+" registered claims — generated from claims.yaml";
document.getElementById('legend').innerHTML=Object.entries(COLORS).map(([s,c])=>`<span><i style="background:${c}"></i>${s} (${counts[s]||0})</span>`).join('');
const grid=document.getElementById('grid');
SECTORS.forEach(sec=>{
 const cs=DATA.filter(c=>c.sec===sec).sort((a,b)=>a.id<b.id?-1:1);
 const h=document.createElement('div');h.className='sector';h.textContent=sec+"  ("+cs.length+")";grid.appendChild(h);
 const row=document.createElement('div');
 cs.forEach(c=>{const d=document.createElement('span');d.className='dot';d.id='n-'+c.id;
  d.style.background=COLORS[c.s];d.title=c.id;d.onclick=()=>select(c.id);row.appendChild(d);});
 grid.appendChild(row);
});
function transDown(id){const seen=new Set();const q=[id];while(q.length){const x=q.pop();
 (byId[x]?byId[x].dn:[]).forEach(y=>{if(!seen.has(y)){seen.add(y);q.push(y);}});}return seen;}
function select(id){
 document.querySelectorAll('.dot').forEach(d=>d.className='dot');
 const c=byId[id];const el=document.getElementById('n-'+id);el.className='dot sel';
 c.d.forEach(u=>{const e=document.getElementById('n-'+u);if(e)e.className='dot up';});
 c.dn.forEach(u=>{const e=document.getElementById('n-'+u);if(e)e.className='dot down';});
 const td=transDown(id);
 const p=document.getElementById('panel');
 p.innerHTML=`<h2>${c.id}</h2><span class="st" style="background:${COLORS[c.s]}">${c.s}</span>
 <div class="tt">${c.t.replace(/&/g,'&amp;').replace(/</g,'&lt;')}${c.t.length>=400?'…':''}</div>
 ${c.b?`<div>benchmark: <code>${c.b}</code></div>`:''}
 <div style="margin-top:8px"><b>depends on (${c.d.length}):</b> ${c.d.map(u=>`<span class="lk" onclick="select('${u}')">${u}</span>`).join(', ')||'—'}</div>
 <div style="margin-top:6px"><b>direct dependents (${c.dn.length}):</b> ${c.dn.map(u=>`<span class="lk" onclick="select('${u}')">${u}</span>`).join(', ')||'—'}</div>
 <div style="margin-top:6px"><b>total downstream (transitive):</b> ${td.size} claims</div>`;
}
</script></body></html>"""
    page = page.replace("__DATA__", payload).replace("__COLORS__", colors_js).replace("__SECTORS__", sectors_js)
    open('docs/roadmap.html', 'w').write(page)

    # ---------- ROADMAP.md ----------
    lines = ["# The Rope Programme — Roadmap of Knowledge\n",
             f"*Generated from claims.yaml — {len(claims)} registered claims.*\n",
             "**The ladder** (each sector builds on those above it; the interactive explorer is",
             "[docs/roadmap.html](roadmap.html), the wall chart [docs/roadmap.png](roadmap.png)):\n"]
    for name, _ in SECTORS:
        cs = by_sector[name]; st = Counter(c['status'] for c in cs)
        lines.append(f"- **{name}** — {len(cs)} claims ("
                     + ", ".join(f"{s} {n}" for s, n in st.most_common()) + ")")
    lines.append("\n**Status colors:** Derived (green) — proved/computed within the model; "
                 "Modeled (blue) — quantitative model with stated assumptions; EFT-constrained "
                 "(purple); Conjecture (orange); Open (yellow); Failed (red) — kept, with its lesson.\n")
    top = sorted(claims, key=lambda c: -len(transitive(downstream, c['id'])))[:10]
    lines.append("**Ten most load-bearing claims** (by transitive downstream count):\n")
    for c in top:
        lines.append(f"- `{c['id']}` ({c['status']}) — {len(transitive(downstream, c['id']))} downstream")
    open('docs/ROADMAP.md', 'w').write("\n".join(lines) + "\n")
    print(f"roadmap built: png + html + md ({len(claims)} claims, {len(SECTORS)} sectors)")

def transitive(downstream, cid):
    seen = set(); q = [cid]
    while q:
        x = q.pop()
        for y in downstream.get(x, []):
            if y not in seen:
                seen.add(y); q.append(y)
    return seen

if __name__ == "__main__":
    build()
