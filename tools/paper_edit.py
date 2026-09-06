"""Paper source editor for papers/_sources/*.docx (house layout: Heading1 sections,
Times New Roman body, shaded 'Scope of this paper' / 'Status' boxes as one-cell tables).
Usage from Python: edit(docx_in, docx_out, replacements=[(old,new),...], sections=[(heading,[para,...]), ...],
insert_before='Status')  -- sections are inserted before the box whose first cell text == insert_before
(or appended before the final Status box). Then convert_pdf(docx_out, pdf_dir)."""
import re, shutil, subprocess, sys, pathlib, tempfile, zipfile
from xml.sax.saxutils import escape

RPR_BODY = ('<w:rPr><w:rFonts w:ascii="Times New Roman" w:cs="Times New Roman" w:eastAsia="Times New Roman" '
            'w:hAnsi="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>')
RPR_HEAD = ('<w:rPr><w:rFonts w:ascii="Times New Roman" w:cs="Times New Roman" w:eastAsia="Times New Roman" '
            'w:hAnsi="Times New Roman"/><w:b/><w:bCs/><w:color w:val="1F3864"/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr>')


def para(text, bold_lead=None):
    t = escape(text)
    runs = ''
    if bold_lead:
        runs += (f'<w:r>{RPR_BODY.replace("<w:sz", "<w:b/><w:bCs/><w:sz", 1)}<w:t xml:space="preserve">{escape(bold_lead)}</w:t></w:r>')
    runs += f'<w:r>{RPR_BODY}<w:t xml:space="preserve">{t}</w:t></w:r>'
    return f'<w:p><w:pPr><w:spacing w:after="160" w:before="0" w:line="276"/><w:jc w:val="both"/></w:pPr>{runs}</w:p>'


def heading(text):
    return (f'<w:p><w:pPr><w:pStyle w:val="Heading1"/><w:spacing w:after="140" w:before="320"/></w:pPr>'
            f'<w:r>{RPR_HEAD}<w:t xml:space="preserve">{escape(text)}</w:t></w:r></w:p>')


def _find_box(x, label):
    """index of the <w:tbl> whose first <w:t> equals label; -1 if none."""
    for m in re.finditer(r'<w:tbl>', x):
        j = x.find('<w:t', m.end()); k = x.find('</w:t>', j)
        first = re.sub(r'<[^>]+>', '', x[j:k + 6])
        if first.strip() == label:
            return m.start()
    return -1


def edit(docx_in, docx_out, replacements=(), sections=(), insert_before='Status', status_replace=None, extra=()):
    d = pathlib.Path(tempfile.mkdtemp())
    with zipfile.ZipFile(docx_in) as z: z.extractall(d)
    for p in d.rglob('*'):
        if p.is_symlink(): p.unlink()
    subprocess.run([sys.executable, '/mnt/skills/public/docx/scripts/merge_runs.py', str(d)], capture_output=True)
    xp = d / 'word' / 'document.xml'; x = xp.read_text(encoding='utf-8')
    for old, new in replacements:
        o, n = escape(old), escape(new)
        if o not in x:
            print(f"  [warn] not found: {old[:60]!r}")
        x = x.replace(o, n)
    if sections:
        block = ''.join(heading(h) + ''.join(para(p) if isinstance(p, str) else para(p[1], p[0]) for p in ps) for h, ps in sections)
        i = _find_box(x, insert_before)
        if i < 0:
            j = x.find(escape(insert_before))
            i = x.rfind('<w:p>', 0, j) if j >= 0 else x.rfind('<w:sectPr')
        x = x[:i] + block + x[i:]
    for anchor, paras in extra:            # plain paragraphs inserted before the paragraph containing `anchor`
        j = x.find(escape(anchor)); i = x.rfind('<w:p>', 0, j) if j >= 0 else x.rfind('<w:sectPr')
        x = x[:i] + ''.join(para(p) if isinstance(p, str) else para(p[1], p[0]) for p in paras) + x[i:]
    xp.write_text(x, encoding='utf-8')
    out = pathlib.Path(docx_out); out.unlink(missing_ok=True)
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in sorted(d.rglob('*')):
            if p.is_file(): z.write(p, p.relative_to(d).as_posix())
    shutil.rmtree(d)
    return out


def convert_pdf(docx_path, pdf_dir):
    r = subprocess.run([sys.executable, '/mnt/skills/public/docx/scripts/office/soffice.py', '--headless', '--convert-to', 'pdf',
                        '--outdir', str(pdf_dir), str(docx_path)], capture_output=True, text=True, timeout=170)
    return r.returncode, (r.stdout + r.stderr)[-300:]
