# GR54-B -- 5/3 FLAT-CELL CONTROL AT 144x54 (CHARTER, LOCKED
# 2026-09-02; the GR54 charter's extension clause, exercised by the
# author: "Let's do B then A")

## Question (control, not discovery)
Does the 54-grid instrument+protocol REPRODUCE FLAT on a cell that
is registered FLAT at 36? Forecloses the objection that GR-ARTIFACT
is an instrument/grid artifact that flattens every branch.

## Protocol
Identical to GR54 in every respect, cell 5/3 (N1=3, N2=5):
phi-continue the registered 5/3 stage-2c profile points s0, s1 to
144x54 (S3R rule, a2 pins at each member's own A2, full bars,
60-round budgets); then the stage-2c arc protocol verbatim at 54 --
ds = 0.08, 12 points, full gates, fresh '144x54:arc:n2=5' pattern
measured at the gated s1 continuation (fault 9/10/11 rules);
measurements SEALED, discriminators computed ONCE at the end.

## Verdict forms (LOCKED)
CTRL-PASS: >= 8 gated points, NEITHER line fires (r < 0.8 AND rise
  < +0.15) -> the 54 protocol reproduces FLAT where FLAT is
  registered; GR-ARTIFACT survives the instrument objection.
CTRL-FAIL: >= 8 gated points, EITHER line fires -> the 54 protocol
  does not reproduce the registered 36 verdict on a control cell;
  GR-ARTIFACT is suspended pending an instrument commission, and
  this becomes the priority finding.
CTRL-OPEN: < 8 gated points -> recorded with the refusal trace.

NOTE (pre-registered, honest): a CTRL-PASS is WEAK evidence -- a
flattening instrument would also produce it. Its value is
asymmetric: only CTRL-FAIL is decisive, and it would invalidate
GR-ARTIFACT. Recorded before the run so the asymmetry cannot be
overclaimed afterward.

## Deliverables
Driver benchmarks/foundations/gr54b_control.py (GR54 driver
parameterized by cell); analysis/gr54b_ckpt.pkl;
analysis/GR54B_results.md.
