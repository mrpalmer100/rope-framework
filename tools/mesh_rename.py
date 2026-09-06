"""Programme rename (2026-09-05): 'the rope framework/programme' -> 'the mesh framework/programme'.
Surgical: the OBJECT 'rope' (two-strand rope, rope count, rope tension, Rope Hypothesis), the
identifiers (rope_solver, rope-framework slug/URLs, file names, ROPE_PARAMETERS, claim IDs) and
paper TITLES are untouched. Case-preserving phrase list."""
import re
PAIRS = [
    (r'\bthe ROPE framework\b', 'the mesh framework'), (r'\bROPE framework\b', 'mesh framework'),
    (r'\bthe Rope Framework\b', 'the Mesh Framework'), (r'\bRope Framework\b', 'Mesh Framework'),
    (r'\bthe rope framework\b', 'the mesh framework'), (r'\brope framework\b', 'mesh framework'),
    (r'\bthe Rope Programme\b', 'the Mesh Programme'), (r'\bRope Programme\b', 'Mesh Programme'),
    (r'\bthe rope programme\b', 'the mesh programme'), (r'\brope programme\b', 'mesh programme'),
    (r'\bthe rope program\b', 'the mesh programme'), (r'\bthe ROPE programme\b', 'the mesh programme'),
    (r'\bthe ROPE program\b', 'the mesh programme'), (r'\bROPE programme\b', 'mesh programme'),
    (r'\bthe rope-framework programme\b', 'the mesh programme'),
    (r'\bTHE ROPE FRAMEWORK\b', 'THE MESH FRAMEWORK'), (r'\bROPE FRAMEWORK\b', 'MESH FRAMEWORK'),
    (r'\bTHE ROPE PROGRAMME\b', 'THE MESH PROGRAMME'), (r'\bROPE PROGRAMME\b', 'MESH PROGRAMME'),
    (r'\bRope Programme\u2019s\b', 'Mesh Programme\u2019s'), (r"\bRope Programme's\b", "Mesh Programme's"),
]
PROTECT = re.compile(r'(rope-framework|rope_framework|rope_solver|ROPE_PARAMETERS|github\.com/[^\s)]*|https?://\S+)')
def rename(text):
    """apply PAIRS outside protected identifier/URL spans; return (new_text, count)."""
    out=[]; n=0; pos=0
    for m in PROTECT.finditer(text):
        seg=text[pos:m.start()]
        for pat,rep in PAIRS:
            seg,k=re.subn(pat,rep,seg); n+=k
        out.append(seg); out.append(m.group(0)); pos=m.end()
    seg=text[pos:]
    for pat,rep in PAIRS:
        seg,k=re.subn(pat,rep,seg); n+=k
    out.append(seg)
    return ''.join(out), n
if __name__=='__main__':
    import sys, pathlib
    tot=0
    for f in sys.argv[1:]:
        p=pathlib.Path(f); s=p.read_text(encoding='utf-8'); t,n=rename(s)
        if n: p.write_text(t,encoding='utf-8')
        tot+=n; print(f'{n:4d}  {f}')
    print('total', tot)
