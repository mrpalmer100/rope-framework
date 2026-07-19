#!/usr/bin/env python3
"""
plain_language_section.py — emit a paper's plain-language section from the SAME
topic source the guide uses, so paper and guide never drift.

Each primary paper can carry a short "In Plain Language" section whose content is
GENERATED from guide/topics/<topic>.md, not hand-written. This tool renders that
topic (minus its chapter title, with callouts flattened to prose) to a markdown
snippet that the paper build/insert step can embed.

Mapping topic -> paper is declared here (kept next to the guide manifest order).

Usage:
  python tools/plain_language_section.py <topic>          # -> markdown to stdout
  python tools/plain_language_section.py --list           # show topic->paper map
"""
import os, sys, re

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOPICS=os.path.join(ROOT,"guide","topics")

# topic -> paper (which primary paper embeds this topic's plain-language section)
TOPIC_PAPER={
    "light":"rope_classical_optics",
    "electricity":"rope_electricity",
    "magnetism":"rope_theory_of_magnetism",
    "maxwell":"rope_maxwell_equations",
    "gravity":"rope_gravity",
    "chemistry":"rope_chemistry",
    "heat":"rope_thermodynamics",
}

def render_snippet(topic):
    path=os.path.join(TOPICS,f"{topic}.md")
    if not os.path.exists(path): raise SystemExit(f"no topic '{topic}'")
    md=open(path).read()
    out=[]
    for line in md.splitlines():
        if line.startswith("# "): continue  # drop chapter title (paper supplies its own heading)
        m=re.match(r'>\s*CALLOUT\|(.+)', line)
        if m:
            out.append(f"**{m.group(1).strip().title()}.** "); continue
        if line.startswith(">"):
            out.append(re.sub(r'^>\s?','',line)); continue
        # flatten fig refs to a short parenthetical
        fm=re.match(r'!\[(.*?)\]\(fig:\w+\)', line)
        if fm:
            out.append(f"*(See the guide diagram: {fm.group(1)[:60]}...)*"); continue
        out.append(line)
    # collapse blank runs
    text=re.sub(r'\n{3,}','\n\n','\n'.join(out)).strip()
    return text

if __name__=="__main__":
    if "--list" in sys.argv:
        for t,p in TOPIC_PAPER.items(): print(f"  {t:14s} -> {p}")
    elif len(sys.argv)>1:
        print(render_snippet(sys.argv[1]))
    else:
        print(__doc__)
