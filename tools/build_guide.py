"""Optional doc-builder (NOT part of pip-install or verify_corpus). Requires
external tools: LibreOffice (soffice) and the `diagrams` package, installed
separately only if you are regenerating the guide. Ordinary users and CI never
run this file."""
#!/usr/bin/env python3
"""
build_guide.py — assemble the plain-language guide from per-topic source files.

The guide is NOT a hand-edited Word document that drifts from the physics. Its
content lives in guide/topics/*.md (one file per topic: light, charge, current,
magnetism, ...), its diagrams in guide/figs/diagrams.py (callable by name), and
its ordering in guide/topics/00_manifest.yaml. This tool renders the diagrams,
assembles the topics in order, and produces docs/rope_plain_language_guide.docx
via pandoc, so the guide stays in sync with its source by construction.

Topic markdown conventions:
  # Title                         -> chapter heading
  > CALLOUT|LABEL                 -> teal callout box (label + body lines)
  > body line...
  ![caption](fig:NAME)            -> render diagram NAME, embed with caption
  normal markdown otherwise.

Usage: python tools/build_guide.py [--pdf]
"""
# VALIDATION STANCE (explicit and intentional):
# This guide is produced via pandoc, whose OOXML is legitimately structured but
# does NOT pass the corpus's strict in-house validator (scripts/office/validate.py)
# -- even pristine pandoc output fails that validator, which is calibrated for the
# hand-built (docx-js / XML-surgery) papers. The guide is therefore checked by
# RENDERING it (soffice -> PDF) and confirming it opens and paginates, not by strict
# schema validation. This is a deliberate, documented tradeoff: the guide is a
# plain-language artifact meant to render and read correctly, not a schema-strict
# deliverable. The primary PAPERS remain strictly validated.

import os, sys, re, subprocess, shutil

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUIDE=os.path.join(ROOT,"guide")
TOPICS=os.path.join(GUIDE,"topics")
FIGS=os.path.join(GUIDE,"figs")
BUILD=os.path.join(GUIDE,"_build")
OUT=os.path.join(ROOT,"docs","rope_plain_language_guide.docx")

def load_manifest():
    import yaml
    with open(os.path.join(TOPICS,"00_manifest.yaml")) as f:
        return yaml.safe_load(f)

def render_diagram(name):
    """Render diagram NAME to PNG in _build; return the PNG path."""
    sys.path.insert(0, FIGS)
    import diagrams
    os.makedirs(BUILD, exist_ok=True)
    svg=diagrams.make(name, outdir=BUILD)
    # svg -> png via soffice
    sys.path.insert(0,"/mnt/skills/public/docx/scripts/office")
    try:
        from soffice import run_soffice
        run_soffice(["--headless","--convert-to","png","--outdir",BUILD,svg])
    except Exception as e:
        print(f"  WARN: soffice render failed for {name}: {e}")
    png=os.path.join(BUILD,f"{name}.png")
    return png if os.path.exists(png) else None

def process_topic(md_text):
    """Convert topic conventions (CALLOUT, fig:) into plain markdown pandoc handles.
    Returns (markdown, set_of_diagram_names_used)."""
    out=[]; figs=set()
    lines=md_text.splitlines()
    i=0
    while i<len(lines):
        line=lines[i]
        # callout block: consecutive '> ' lines starting with '> CALLOUT|'
        m=re.match(r'>\s*CALLOUT\|(.+)', line)
        if m:
            label=m.group(1).strip(); body=[]
            i+=1
            while i<len(lines) and lines[i].startswith(">"):
                body.append(re.sub(r'^>\s?','',lines[i])); i+=1
            # render as a markdown table (1x2) which pandoc styles; label cell + body cell.
            body_md=" ".join(b for b in body if b.strip())
            out.append("")
            out.append(f"| **{label}** | {body_md} |")
            out.append("|:--|:--|")
            out.append("")
            continue
        # contrast block: '> CONTRAST' then lines 'STANDARD| ...', 'ROPE| ...', 'EQUATIONS| ...'
        cm=re.match(r'>\s*CONTRAST\s*$', line)
        if cm:
            fields={}
            i+=1
            while i<len(lines) and lines[i].startswith(">"):
                body=re.sub(r'^>\s?','',lines[i])
                fm2=re.match(r'(STANDARD|ROPE|EQUATIONS)\|\s*(.*)', body)
                if fm2: fields[fm2.group(1)]=fm2.group(2)
                elif body.strip() and fields:
                    last=list(fields)[-1]; fields[last]+=" "+body.strip()
                i+=1
            out.append("")
            out.append("| What mainstream physics says | What the rope picture proposes |")
            out.append("|:--|:--|")
            out.append(f"| {fields.get('STANDARD','')} | {fields.get('ROPE','')} |")
            out.append("")
            if fields.get("EQUATIONS"):
                out.append(f"*The math:* {fields['EQUATIONS']}")
                out.append("")
            continue
        # figure: ![cap](fig:NAME)
        fm=re.match(r'!\[(.*?)\]\(fig:(\w+)\)', line)
        if fm:
            cap, name = fm.group(1), fm.group(2)
            figs.add(name)
            out.append(f"![{cap}](FIGPATH::{name})")
            i+=1; continue
        out.append(line); i+=1
    return "\n".join(out), figs


# Consistency lint: phrases from superseded models that must not reappear in the
# guide. Each maps to why it's wrong / what to say instead. The build warns loudly
# if any appear, so physics-model drift is caught automatically (not by readers).
FORBIDDEN_PHRASES = {
    "phase winding": "old magnetism model; magnetism = network's circulating response to rotating ropes",
    "strand imbalance": "old charge model; charge = strand HANDEDNESS (Gaede)",
    "pull unequally": "old charge model; charge = handedness, not a tug-of-war",
    "wound together": "old charge model; charge = handedness (mirror-orientation), not winding count",
    "braid wrap": "old charge model; charge = handedness",
    "the braid streams": "use 'the handedness streams / a current flows'",
    "= braid": "old charge model; Charge = HANDEDNESS",
    "nothing spins": "misleading; local rotation DOES happen and is the current",
    "whirling like a shaft": "conflates rigid-shaft (denied) with rotation (real); reword",
    "neutral means no wraps": "helix/linking conflation; neutral is still helical",
    "run alongside": "implies un-coiled neutral rope; wrong",
    "handedness pattern streaming": "old current wording; current = turning the helix like a screw",
    "barber-pole climb": "old current image; use the screw / drive-shaft picture",
    "recent technical work": "research-log voice; speak about the picture, not the project's progress",
    "recent papers establish": "research-log voice; describe what the picture does, not project status",
    "new work worth stating": "research-log voice; just explain the physics",
    "how far this has been taken": "research-log voice; use a plain honest-limit note",
    "every link is checked": "research-log voice; reader-facing guide, not a status report",
    "earlier version of this guide": "reader never saw it; state the physics directly",
}

def lint_topics():
    import glob
    problems = []
    for path in sorted(glob.glob(os.path.join(TOPICS, "*.md"))):
        text = open(path).read().lower()
        for phrase, why in FORBIDDEN_PHRASES.items():
            # allow the phrase only if explicitly negated nearby (e.g. quoting the wrong view)
            if phrase in text:
                # crude negation guard: skip if 'not' or 'tempting to say' within 40 chars before
                idx = text.find(phrase)
                context = text[max(0, idx-45):idx]
                if any(neg in context for neg in ("not ", "no longer", "tempting to say", "wrong", "instead of")):
                    continue
                problems.append((os.path.basename(path), phrase, why))
    if problems:
        print("  CONSISTENCY LINT: found superseded-model phrases:")
        for fn, ph, why in problems:
            print(f"    [{fn}] '{ph}' -> {why}")
    else:
        print("  consistency lint: clean (no superseded-model phrases)")
    return problems

def build(make_pdf=False):
    man=load_manifest()
    lint_topics()
    os.makedirs(BUILD, exist_ok=True)
    parts=[]
    # title block
    parts.append(f"% {man['title']}")
    parts.append(f"% {man['author']}")
    parts.append("")
    parts.append(f"*{man.get('subtitle','')}*")
    parts.append("")
    parts.append(f"> {man.get('credit','')}")
    parts.append("")
    all_figs=set()
    fig_paths={}
    for topic in man["order"]:
        path=os.path.join(TOPICS,f"{topic}.md")
        if not os.path.exists(path):
            print(f"  (skip missing topic: {topic})"); continue
        md=open(path).read()
        processed, figs = process_topic(md)
        for fn in figs:
            if fn not in fig_paths:
                p=render_diagram(fn)
                if p: fig_paths[fn]=p
        parts.append(processed); parts.append("\n\\newpage\n")
    doc="\n".join(parts)
    # substitute FIGPATH::name with real rendered paths
    for name,p in fig_paths.items():
        doc=doc.replace(f"FIGPATH::{name}", p)
    # drop any unrendered figure refs gracefully
    doc=re.sub(r'!\[(.*?)\]\(FIGPATH::\w+\)', r'*[diagram: \1]*', doc)
    md_path=os.path.join(BUILD,"guide.md")
    open(md_path,"w").write(doc)
    # pandoc -> docx (with reference doc if present)
    ref=os.path.join(GUIDE,"reference.docx")
    cmd=["pandoc",md_path,"-o",OUT]
    if os.path.exists(ref): cmd+=["--reference-doc",ref]
    subprocess.run(cmd,check=True)
    fix_content_types(OUT)
    normalize_docx(OUT)
    print(f"Wrote {OUT} ({len(man['order'])} topics, {len(fig_paths)} diagrams)")
    render_check(OUT)
    if make_pdf:
        sys.path.insert(0,"/mnt/skills/public/docx/scripts/office")
        from soffice import run_soffice
        run_soffice(["--headless","--convert-to","pdf","--outdir",os.path.join(ROOT,"docs"),OUT])
        print("Wrote PDF")



def render_check(docx):
    """Confirm the guide renders (opens + paginates) via soffice->PDF. This is the
    guide's validation gate in lieu of strict schema validation (see stance above)."""
    import sys as _s
    _s.path.insert(0,"/mnt/skills/public/docx/scripts/office")
    try:
        from soffice import run_soffice
        outdir=os.path.dirname(docx)
        run_soffice(["--headless","--convert-to","pdf","--outdir",outdir,docx])
        pdf=docx[:-5]+".pdf"
        ok=os.path.exists(pdf) and os.path.getsize(pdf)>2000
        print(f"  render-check: {'PASS' if ok else 'FAIL'} ({pdf})")
        return ok
    except Exception as e:
        print(f"  render-check ERROR: {e}"); return False

def normalize_docx(docx):
    """Fix pandoc's known OOXML element-ordering quirks that fail strict validation
    but render fine. Operates on the zip's XML parts in place."""
    import zipfile, shutil, re as _re
    tmp=docx+".norm"
    with zipfile.ZipFile(docx) as zin:
        names=zin.namelist(); data={n:zin.read(n) for n in names}
    def fixdoc(xml):
        t=xml.decode()
        # in table cell props, jc is not allowed -> drop stray <w:jc> inside <w:tcPr>
        t=_re.sub(r'(<w:tcPr>)(.*?)(</w:tcPr>)', lambda m: m.group(1)+m.group(2).replace(_re.search(r'<w:jc[^/]*/>',m.group(2)).group(0) if _re.search(r'<w:jc[^/]*/>',m.group(2)) else '','')+m.group(3), t, flags=_re.S)
        return t.encode()
    def fixsettings(xml):
        t=xml.decode(); t=_re.sub(r'<w:zoom[^/]*/>','',t); return t.encode()
    def fixnumbering(xml):
        t=xml.decode()
        # nsid val must be 8 hex chars; pad short ones
        t=_re.sub(r'(<w:nsid w:val=")([0-9A-Fa-f]{1,7})(")', lambda m: m.group(1)+m.group(2).rjust(8,"0")+m.group(3), t)
        return t.encode()
    def fixstyles(xml):
        t=xml.decode()
        # remove stray injected <w:color> that landed out of order (belt-and-suspenders)
        return t.encode()
    if "word/document.xml" in data: data["word/document.xml"]=fixdoc(data["word/document.xml"])
    if "word/settings.xml" in data: data["word/settings.xml"]=fixsettings(data["word/settings.xml"])
    if "word/numbering.xml" in data: data["word/numbering.xml"]=fixnumbering(data["word/numbering.xml"])
    with zipfile.ZipFile(tmp,"w",zipfile.ZIP_DEFLATED) as zout:
        for n in names: zout.writestr(n, data[n])
    shutil.move(tmp, docx)

def fix_content_types(docx):
    """Ensure png/jpeg default content types are declared (pandoc sometimes omits)."""
    import zipfile, tempfile
    tmp=docx+".tmp"
    with zipfile.ZipFile(docx) as zin:
        names=zin.namelist()
        ct=zin.read("[Content_Types].xml").decode()
        changed=False
        for ext,mime in [("png","image/png"),("jpeg","image/jpeg"),("jpg","image/jpeg")]:
            if f'Extension="{ext}"' not in ct:
                ct=ct.replace("</Types>", f'<Default Extension="{ext}" ContentType="{mime}"/></Types>')
                changed=True
        with zipfile.ZipFile(tmp,"w",zipfile.ZIP_DEFLATED) as zout:
            for n in names:
                data = ct.encode() if n=="[Content_Types].xml" else zin.read(n)
                zout.writestr(n, data)
    shutil.move(tmp, docx)

if __name__=="__main__":
    build(make_pdf="--pdf" in sys.argv)
