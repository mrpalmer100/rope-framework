"""Apply the mesh rename to a paper source (.docx): rename phrases inside <w:t> text (runs merged
first), insert the naming note before the first Heading1, rebuild, convert to PDF."""
import sys, re, pathlib, zipfile, tempfile, shutil, subprocess
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import paper_edit as PE, mesh_rename as MR
from xml.sax.saxutils import escape, unescape
NOTE = ("Naming note (5 September 2026). This programme is now the Mesh Programme and the theory it develops the mesh framework; "
        "'the rope framework' in earlier revisions reads 'the mesh framework'. 'Rope' remains the name of the two-strand wound "
        "object, and the Rope Hypothesis credited to Bill Gaede keeps its name. Identifiers (repository, rope_solver, file names, "
        "claim IDs) are unchanged.")
def process(src, out_docx, pdf_dir):
    d=pathlib.Path(tempfile.mkdtemp())
    with zipfile.ZipFile(src) as z: z.extractall(d)
    for p in d.rglob('*'):
        if p.is_symlink(): p.unlink()
    subprocess.run([sys.executable,'/mnt/skills/public/docx/scripts/merge_runs.py',str(d)],capture_output=True)
    n_total=0
    for xml in [d/'word'/'document.xml'] + list((d/'word').glob('header*.xml')) + list((d/'word').glob('footer*.xml')):
        x=xml.read_text(encoding='utf-8')
        def rep(m):
            nonlocal n_total
            t,k=MR.rename(unescape(m.group(2))); n_total+=k
            return m.group(1)+escape(t)+m.group(3)
        x=re.sub(r'(<w:t(?: [^>]*)?(?<!/)>)(.*?)(</w:t>)', rep, x, flags=re.S)
        if xml.name=='document.xml':
            i=x.find('<w:pStyle w:val="Heading1"/>'); i=x.rfind('<w:p>',0,i) if i>=0 else x.rfind('<w:sectPr')
            x=x[:i]+PE.para(NOTE)+x[i:]
        xml.write_text(x,encoding='utf-8')
    out=pathlib.Path(out_docx); out.unlink(missing_ok=True)
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(d.rglob('*')):
            if p.is_file(): z.write(p,p.relative_to(d).as_posix())
    shutil.rmtree(d)
    rc,_=PE.convert_pdf(out,pdf_dir)
    return n_total, rc
if __name__=='__main__':
    S=pathlib.Path('papers/_sources'); O=pathlib.Path('/tmp/mesh_papers'); O.mkdir(exist_ok=True)
    done={p.stem for p in O.glob('*.pdf')}
    todo=[p for p in sorted(S.glob('*.docx')) if p.stem not in done]
    import time; t0=time.time()
    for p in todo:
        if time.time()-t0>140: break
        n,rc=process(p, O/p.name, O); print(f"{p.stem:40s} renames {n:3d}  pdf {'ok' if rc==0 else 'FAIL'}", flush=True)
    print(f"remaining {len([p for p in S.glob('*.docx') if p.stem not in {q.stem for q in O.glob('*.pdf')}])}")
