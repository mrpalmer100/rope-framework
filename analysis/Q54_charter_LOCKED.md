# Q = 5/4 COLUMN (Q54) -- CHARTER (LOCKED 2026-08-30, before any
# fourth-cell computation exists in the corpus)
# Authorized by the author ("5/4 please"), queue item 3 of
# WHYWIND_queue_action_approved.md. PRIOR: artifact-final on the
# winding-band interpretation (FND-161/162). THE COMMITTED
# PREDICTION OF RECORD (WHYWIND_dispersion_results.md, registered
# before any fourth-cell computation): ** q = 5/4 MARCHES FLAT **.
# The two hypotheses SPLIT on this cell by design: naive
# line-proximity predicts COLLAPSE (interpolated om2 ~ 1.664 lands
# 0.12 percent from an order-4 line); refinement (b) (j = n class
# only) predicts FLAT. This column adjudicates between them.

## AMENDMENT 1 (2026-08-30, PRE-DATA -- recorded before any
## waypoint, rate, or profile number exists for this cell; only
## level-1 metrics and early-ramp residuals had been seen)
The dense instrument's f64 endgame at 144x36 (dense J + dense
normal matrix, ~3.8 GB) exceeds THIS container's ceiling and was
OOM-reaped on every ramp round. This is the exact regime SPARSE-J
was commissioned and credentialed for. SUBSTITUTION: all Q54
solves at 144x36 run on the SJ-CREDENTIALED instrument (SparseJac
+ BandedTorusSolver + gn_sparse), under the standing credentials
C2 (anchor equivalence at 144x36: same member to RMS 3.2e-10,
A2/om2 within 1.5e-7) and C3 (arc marching, rates within 0.06
percent of the dense-registered profile). EVERYTHING ELSE IS
UNTOUCHED AND VERBATIM: seeds, sub-pin ladder fractions, rung
persistence, waypoint amplitudes, fine pin, arc-rate targets and
budgets, gates, bars, statistics, and verdict lines. SPOT-BAR (v2, corrected 2026-08-30 before the ramp proceeds; v1 --
re-gating the level-1 state -- proved ILL-POSED: the a2 pin is
blind at A2 ~ 0 and permits om2 slide along the branch, the
registered 2026-08-25 syndrome; the slide measured 4.6e-3 with
gam bit-identical and level-1 checks passing on both states, an
instrument-independent property of the pin, recorded): the
sparse instrument must pass the C1a column-identity check ON THIS
CELL'S OPERATOR -- >= 20 randomly probed Jacobian columns at the
level-1 state agree with direct finite differences to the C1
tolerance, with no dependency missing from the measured pattern.
Instrument equivalence at member grade rides on the standing C2
credential. The pattern for (144x36, a2, n2=5) is built fresh per
the fault-9/10 rule.

## OBJECTS AND PROTOCOL (locked; the registered column protocol,
## same instrument as the FND-150..153 columns)
- Cell: q = 5/4 (N1 = 4, N2 = 5), grid 144x36, the DENSE registered
  instrument (gn_lean) -- the instrument of record at 36. The
  sparse instrument appears ONLY in the grid rider below.
- INSTRUMENT RE-VALIDATION BAR (v-bar, this container): before the
  ramp, the dense instrument must reproduce a RETAINED 144x36
  stage-2c member's metrics (A2, om2, gam) to rel 1e-6 with RMS and
  closure inside bars, and the v5 ramp control (q = 3/2 injection
  seed at 96x36 through the identical ladder) must gate. Failure:
  HALT, no column.
- Stage 1: run_q(N1=4, N2=5, 144, 36) VERBATIM -- level-1 seed,
  sub-pin ladder, waypoints, rates at the registered lo/hi
  amplitudes (~0.0048, ~0.0063). Refusals recorded, kept,
  evidence-bearing.
- Stage 2c: the registered 12-point arc profile (ds = 0.08,
  identical rate / V_pt / f_dir formulas, full gates per point)
  marched from the stage-1 pair, deep-ward, exactly as for the
  registered columns.

## LOCKED VERDICT LINES (the REGISTERED discriminators of the
## FND-153-era control, applied verbatim to the 5/4 profile)
  r      = corr(log V_pt, -log rate) over the profile
  f_rise = f_dir(end) - f_dir(start)
  Q54-FLAT     : r < 0.8 AND f_rise < +0.15.
      The committed prediction of record is VINDICATED on its
      designed test; naive line-proximity is FALSIFIED on its own
      chosen ground (0.12 percent from an order-4 line, no
      collapse). The j = n class selection (refinement (b))
      advances to grant-proposable.
  Q54-COLLAPSE : r >= 0.8 AND f_rise >= +0.15.
      The committed prediction is FALSIFIED AND KEPT (the standing
      rule); naive proximity is revived; refinement (b) dies at
      this cell.
  Q54-OPEN     : one line fires and the other nulls, or the
      profile cannot complete >= 8 gated points within budget.
      Kept; no interpretive grant either way.
  DISPLAY (non-verdict): om2 vs the interpolation 1.664; D-factor
  per the stage-1 rules; per-point table as registered.

## GRID RIDER (out-of-sample grid question; runs AFTER the column
## verdict renders, whatever it is)
  The profile's deep pair is phi-continued to 144x54 (the S3R
  protocol verbatim: registered seed rule, a2 pins at each
  member's own A2, the SJ-CREDENTIALED instrument, full bars).
  Pre-committed statistic, defined cell-blind: let B36 = the
  maximum single-band pt mass of the 36-grid deep-pair tangent
  over bands (|n_phi| = c +- 1, both conjugates), c in [5, 17];
  B54 = the same band's mass at 54; H54 = mass at
  19 <= |n_phi| <= 27.
  Q54-GRID-NA      : B36 < 0.30 (no concentrated band to test;
                     rider moot, recorded).
  Q54-GRID-BOUND   : B36 >= 0.30 AND B54 < 0.5 x B36 AND
                     H54 < 0.10 (the 4/3 pattern out-of-sample).
  Q54-GRID-STABLE  : B36 >= 0.30 AND B54 >= 0.5 x B36
                     (a band that SURVIVES refinement -- would be
                     the first, and would demand its own record).
  Anything else: Q54-GRID-OPEN, kept.

## BUDGET AND NO-RESCUE
Stage-1 solves 60 rounds each; profile points 60 rounds each; the
rider solves 60 rounds each. Reap-window chunked with per-round
persistence throughout; durable exports to analysis/ at every
gate/refusal and at each stage boundary. NO tuning of seeds,
pins, ladders, budgets, statistics, or lines after any 5/4 number
is seen. Grants reserved to the author. Failures kept. Ships in
the NEXT release.
