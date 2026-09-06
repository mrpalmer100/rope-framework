#!/usr/bin/env python3
"""
build_claim_status_registry.py -- generate the reviewer-facing Master Claim-Status
Registry (docs/rope_claim_status_registry.docx + .pdf) from claims.yaml.

Why generated: this table is item #2 in the external-review package -- the curated
one-page status map a reviewer reads to navigate the eleven-paper set. Hand-
maintained, its Status column drifts as the corpus advances (e.g. Tsirelson moved
Modeled -> Derived when QB-020 landed; the gravity metric likewise). Deleting it
would break the review package and remove a genuinely useful view; so instead the
CURATION stays human (which claims, their reviewer-friendly phrasing, the external
test) and the volatile STATUS is pulled live from the registry by claim id.

Each ROW is (label, claim_id | None, paper, dependency, corrected, ext_test):
  - claim_id set  -> Status is read live from claims.yaml (never drifts)
  - claim_id None -> Status is an editorial summary, given inline (rare)

Run: python3 tools/build_claim_status_registry.py
"""
import sys, yaml, subprocess, shutil
from pathlib import Path
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

ROOT = Path(__file__).resolve().parent.parent
CLAIMS = ROOT / "claims.yaml"
OUT_DOCX = ROOT / "docs" / "rope_claim_status_registry.docx"
OUT_PDF = ROOT / "docs" / "rope_claim_status_registry.pdf"

NAVY = RGBColor(0x1F, 0x38, 0x64)

# ---- CURATED ROW SET (editorial; the human decisions) --------------------
# (label, claim_id_or_status, paper, dependency, corrected, ext_test)
# If field 2 is a known status word it is used verbatim (editorial summary row);
# otherwise it is treated as a claim id and the live status is looked up.
TIER1 = ("Tier 1 -- In-Domain (Classical) Claims", [
    ("Rope effective metric = isotropic Schwarzschild (weak field)", "GRV-026", "Gravity", "Rope static config", "No", "GR-equiv"),
    ("PPN gamma = beta = 1", "GRV-002", "Gravity", "Effective metric", "No", "Cassini"),
    ("Light deflection 1.751\u2033; Mercury 43.0\u2033/cy", "GRV-026", "Gravity", "gamma, beta", "No", "VLBI, obs"),
    ("Shapiro gamma = 1; Nordtvedt eta = 0", "GRV-002", "Gravity", "Effective metric", "No", "Cassini, LLR"),
    ("Two-slit intensity law I \u221d 1+cos(2\u03c0\u0394/\u03bb)", "OPT-001", "Optics", "Light = rope wave", "No", "Classic optics"),
    ("Classical diffraction (obstacle / needle)", "OPT-002", "Optics", "Wave superposition", "No", "Classic optics"),
    ("Maxwell structure from rope tension/twist", "EM-003", "Electromagnetism", "Rope kinematics", "No", "EM equiv"),
    ("Magnetism: field near/far from one rope set", "EM-012", "Magnetism", "Rope geometry", "No", "Oersted-type"),
    ("Stiffness K = T\u00b2/(\u03ba a) scalar; 2T\u00b2/(\u03ba a) director", "EM-RECON-009", "Microscopic Mechanics", "Coarse-graining", "YES (was 3T\u00b2)", "\u2014"),
    ("Coarse-grained action S = (K/2)\u222b(\u2207\u03b8)\u00b2 at leading order", "EM-RECON-011", "Renormalization/EFT", "Power-counting", "No", "\u2014"),
    ("Thermodynamic coarse-graining & coefficients", "THM-001", "Thermodynamics", "Rope statistics", "No", "\u2014"),
    ("Condensed-matter analogues (vortex/phase)", "Modeled", "Condensed Matter", "Rope order params", "No", "Lab analogue"),
])
TIER2 = ("Tier 2 -- The Quantum Boundary (Findings & Open)", [
    ("Local rope model gives triangle wave, CHSH \u2264 2", "QB-001", "Non-Local Dynamics", "Counting rule", "No", "Bell tests"),
    ("Tsirelson bound derived as a theorem; corpus-native singlet saturates it", "QB-020", "Non-Local Dynamics", "Hopf/spinor structure", "No", "Bell tests"),
    ("Bell violation demonstrated from a nucleated pair (CHSH = 2.039)", "QB-030", "Non-Local Dynamics", "Guidance imported", "No", "Bell tests"),
    ("No-signalling holds for the update rule", "Derived", "Non-Local Dynamics", "Update structure", "No", "\u2014"),
    ("Local configuration-counting reading does not reproduce entanglement", "QB-003", "Measurement/Born; Scope", "Bell caps local at 2", "No", "Bell, g\u00b2"),
    ("Single-photon self-interference (counting form)", "QB-005", "Optics; Scope", "Amplitude interference", "No", "g\u00b2, single-photon"),
    ("Detector couples to Bloch angle (gamma = 1)", "QB-011", "Non-Local Dynamics", "Measurement dynamics", "No", "\u2014"),
    ("Rope-native derivation of configuration-space guidance (future)", "Open", "Scope and Limits", "New structure needed", "No", "\u2014"),
])
TIER3 = ("Tier 3 -- Ontology & Scope", [
    ("Interactions mediated by physical two-strand ropes", "Modeled", "Ontology/Foundations", "Core premise", "No", "\u2014"),
    ("Programme is a classical model w/ documented quantum boundary", "Derived", "Scope and Limits", "Whole corpus", "No", "\u2014"),
    ("Boundary generalises to any local counting ontology", "EFT-constrained", "Scope and Limits", "Consistent w/ Bell", "No", "Bell"),
])
TIERS = [TIER1, TIER2, TIER3]

STATUS_WORDS = {"Derived", "Modeled", "EFT-constrained", "Failed", "Open", "Conjecture"}

INTRO = (
    "This registry exists so the corpus can be evaluated without reading all of it at "
    "once. Every principal claim in the eleven-paper external set is listed once, with "
    "its status, the paper that carries it, what it depends on, whether it has needed "
    "correction, and whether an external test exists. Status is drawn live from the "
    "claim registry, so it cannot drift from the corpus."
)
LEGEND = (
    "Derived -- follows by calculation from stated premises. EFT-constrained -- fixed by "
    "effective-field-theory / symmetry reasoning. Modeled -- reproduced by an explicit "
    "construction consistent with data. Failed -- shown not to hold as formulated (kept "
    "as a finding). Open -- not yet established either way."
)
BYLINE = ("Mark Palmer \u00b7 with computational collaboration by Claude (Anthropic) \u00b7 "
          "palmer100@gmail.com")


def status_for(field, byid):
    if field in STATUS_WORDS:
        return field
    c = byid.get(field)
    return c.get("status") if c else "?"


def build():
    d = yaml.safe_load(CLAIMS.read_text())
    byid = {c["id"]: c for c in d["claims"]}

    doc = Document()
    title = doc.add_paragraph()
    r = title.add_run("The Mesh Programme \u2014 Master Claim-Status Registry")
    r.bold = True; r.font.size = Pt(16); r.font.color.rgb = NAVY
    sub = doc.add_paragraph()
    rs = sub.add_run("One canonical source for the status of every principal claim in the external review set")
    rs.italic = True; rs.font.size = Pt(10)
    by = doc.add_paragraph(); by.add_run(BYLINE).font.size = Pt(9)
    doc.add_paragraph(INTRO)
    lg = doc.add_paragraph(); lg.add_run(LEGEND).font.size = Pt(9)

    cols = ["Claim", "Status", "Paper", "Dependency", "Corrected?", "Ext. test?"]
    for tier_title, rows in TIERS:
        h = doc.add_paragraph()
        rh = h.add_run(tier_title); rh.bold = True; rh.font.color.rgb = NAVY; rh.font.size = Pt(12)
        table = doc.add_table(rows=1, cols=6)
        table.style = "Light Grid Accent 1"
        for i, cn in enumerate(cols):
            cell = table.rows[0].cells[i]
            cell.text = cn
            for p in cell.paragraphs:
                for rr in p.runs:
                    rr.bold = True; rr.font.size = Pt(9)
        for (label, field, paper, dep, corr, ext) in rows:
            st = status_for(field, byid)
            cells = table.add_row().cells
            vals = [label, st, paper, dep, corr, ext]
            for i, v in enumerate(vals):
                cells[i].text = v
                for p in cells[i].paragraphs:
                    for rr in p.runs:
                        rr.font.size = Pt(9)

    doc.save(str(OUT_DOCX))
    n = sum(len(rows) for _, rows in TIERS)
    print(f"Wrote {OUT_DOCX.relative_to(ROOT)} ({n} curated rows, status live from registry)")


def render_pdf():
    soffice = "/mnt/skills/public/docx/scripts/office/soffice.py"
    subprocess.run([sys.executable, soffice, "--headless", "--convert-to", "pdf",
                    str(OUT_DOCX), "--outdir", "/tmp/"], capture_output=True)
    tmp = Path("/tmp") / (OUT_DOCX.stem + ".pdf")
    if tmp.exists():
        shutil.move(str(tmp), str(OUT_PDF))
        print(f"Wrote {OUT_PDF.relative_to(ROOT)}")


if __name__ == "__main__":
    build()
    render_pdf()
