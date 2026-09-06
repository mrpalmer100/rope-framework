# GR54-A -- 4/3 CELL AT 144x54: DISPLACEMENT REPLICATION (CHARTER,
# LOCKED 2026-09-03; authorized by the author: "Let's do it")

## Question
Does the corpus's founding collapse column (4/3, FND-150..153
lineage, registered COLLAPSE at 144x36 with f_rise +0.3691) show
the same GRID-DISPLACED behavior as 5/4: no collapse in the 36
window at 54, collapse deeper with the full signature?

## Protocol (identical to GR54 + GR54-X, cell 4/3, N1=3 N2=4)
Phi-continue the registered 4/3 stage-2c profile points s0, s1 to
144x54 (S3R rule, a2 pins, full bars, 60-round budgets); arc
profile at 54, ds = 0.08, BUDGET 20 POINTS from the start; fresh
'144x54:arc:n2=4' pattern at the gated s1; per-point measurements
SEALED; verdict computed ONCE after 20 gated points or a refusal.

## Locked statistics (C1 rule, DISC)
W36 = f_dir rise over the points whose A2 lies within the 36-grid
      profile's A2 span (last 3 in-span - first 3) vs +0.15.
WX  = f_dir rise over the full 20-point profile (last 3 - first 3)
      vs +0.15.

## Verdict forms (LOCKED)
A-DISPLACED:  W36 < 0.15 AND WX >= 0.15 -> 4/3 replicates the 5/4
  displacement; "collapse location is grid-dependent" becomes a
  two-cell finding and a claim is drafted at corpus scope.
A-ROBUST:     W36 >= 0.15 -> 4/3 collapses in the SAME window at
  54; displacement is cell-specific; reported as a split between
  the two collapse cells.
A-ABSENT:     W36 < 0.15 AND WX < 0.15 -> no collapse to A2 ~
  0.0055 at 54; the 4/3 collapse's status at 54 is open beyond
  the tested span; no artifact claim is made (GR54's lesson).
A-REFUSED:    < 14 gated -> recorded with the trace; a refusal near
  the branch's turn is reported as evidence, not scored.
Solve-behavior leading indicators (predictor slide, capped
corrector steps, arc-step overshoot) logged alongside, unscored.

## Deliverables
benchmarks/foundations/gr54a_43.py; analysis/gr54a_ckpt.pkl;
analysis/GR54A_results.md; claim drafts.

## AMENDMENT A1 (pre-data, 2026-09-04; cost): A-ROBUST is decided by
W36 alone under the locked forms; WX cannot alter it. Therefore:
after the last point whose A2 lies within the 36-grid profile's
span (~0.0051), compute W36 ONCE. If W36 >= 0.15, render A-ROBUST
and stop the march. If not, continue to 20 points as chartered
(DISPLACED vs ABSENT needs WX). No sealed statistic had been
computed when this was recorded.
