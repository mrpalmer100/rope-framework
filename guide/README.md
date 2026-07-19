# Plain-Language Guide — Build System

The guide is NOT a hand-edited Word document. It is assembled from source, so it
never drifts from the physics.

## Source of truth
- `topics/*.md` — one file per chapter (intro, light, electricity, magnetism,
  maxwell, gravity, chemistry, heat, closing). Plain markdown plus two conventions:
  - `> CALLOUT|LABEL` (+ following `>` lines) → a highlighted callout box
  - `![caption](fig:NAME)` → renders diagram NAME and embeds it
- `topics/00_manifest.yaml` — title/author and the chapter ORDER.
- `figs/diagrams.py` — every diagram, callable by name: `make("braid")`. Warm palette.

## Build
    python tools/build_guide.py [--pdf]
Renders diagrams → assembles topics in manifest order → pandoc → styled
`docs/rope_plain_language_guide.docx` (Georgia, teal callouts via `reference.docx`).

## Validation stance (intentional)
The guide is produced via pandoc, whose OOXML does not pass the corpus's strict
in-house validator (even pristine pandoc output fails it; that validator is
calibrated for the hand-built papers). The guide is therefore checked by RENDERING
it to PDF (`render_check`) and confirming it opens and paginates — a deliberate,
documented tradeoff. The primary PAPERS remain strictly validated.

## Papers pull from the same source
`tools/plain_language_section.py <topic>` emits a paper-ready plain-language
snippet from the SAME topic file, so a paper's "In Plain Language" section and the
guide chapter never diverge. Topic→paper mapping is declared in that tool.

## To change the physics
Edit the topic `.md` (and its diagram in `figs/diagrams.py`), then rebuild.
One edit, one source — no more stale diagrams or drifted descriptions.
