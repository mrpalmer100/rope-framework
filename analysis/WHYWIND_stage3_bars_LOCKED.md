# WHY-WINDING STAGE 3 (TARGETED) -- RESOLUTION REPLICATION OF THE
# COLLAPSE MODE: CHARTER (LOCKED 2026-08-28, before any solve)
# Authorized by the author 2026-08-28 ("Charter stage 3"). Discharges,
# in targeted form, the resolution-replication debt registered by the
# stage-1 charter, aimed at Finding 3 of
# analysis/WHYWIND_rotation_results.md: is the 4/3 collapse mode
# (n, m) = +-(17, 19) physical, or phi-grid-scale content?

## DESIGN (fixed by container feasibility, measured this session:
## ~3 GB available; 144 x 72 and 96 x 72 infeasible at f64-normal)
Grids:
  BASELINE  96 x 36  (s at the REGISTERED 96 control resolution,
                      phi unchanged; dof 10370, stage-2b size)
  PROBE     96 x 54  (phi Nyquist 18 -> 27; dof 15554, EXACTLY the
                      stage-1 size -- all solver lessons carry)
The s-reduction 144 -> 96 is common to both, so the baseline
controls it; the probe isolates the phi question, which is the
flagged axis.

## OBJECTS
- Deep arc pair per cell: states[11], states[12] of prof-4/3 and
  prof-5/3 (2c ckpt, read-only) -- the pair under tangent 10, where
  the (17, 19) mode carries 74 percent.
- Seeds: spectral transfer of each retained state -- FFT truncation
  in s (144 -> 96), FFT zero-pad in phi (36 -> 54), per field
  (th, pt, T); om1, om2 carried. (Precedent: the stage-2
  harmonic-tail control's FFT-interpolated re-solve.)
- Pins: each member re-solved under ITS OWN registered A2 (a2 pin
  mode), values taken from the member's measured A2 at load.
- Gates: the stage-1 full bars unchanged -- RMS < RMS_BAR, closure
  < 1e-6, geometry floors, pin tol. A member that cannot gate is a
  recorded failure of the solve, not a verdict.
- Solver: the stage-1 QTGrid f32-J machinery at its native dof;
  per-round checkpoint /tmp/s3_ckpt.pkl; lock-file rotation and
  worker-RSS verification per the stage-2 ledger; budgeted
  resumable runs.

## LOCKED STATISTIC
For each gated pair: t = (x_deep - x_prev)/||.||; P = |FFT2(t_pt)|^2
normalized to the pt total. BAND(n0, m0) = sum of P over
|n| in [n0-1, n0+1], |m| in [m0-1, m0+1] (and the conjugate pair).
  F17(grid) = BAND(17, 19) on the 4/3 tangent.
  HIBAND    = mass at |n| >= 21 (the new headroom band, probe only).
Display (non-verdict): full top-mode tables both cells; 5/3 beat
spectrum; pt_share.

## LOCKED VERDICT LINES
  S3-CRED (must pass before any verdict): at 96 x 36 the 4/3
      tangent shows F17 >= 0.20 and the 5/3 tangent's top mode is
      on its beat ladder (n=k, m=-2k). Failure: S3-F-INSTRUMENT
      (the s-reduction changed the story; no adjudication).
  S3-PHYSICAL: at 96 x 54, F17 >= 0.5 x F17(96x36) AND the 4/3
      dominant pt mode remains at (|n|, |m|) = (17, 19) within the
      band AND HIBAND < 0.10.
  S3-ARTIFACT: at 96 x 54, F17 < 0.05.
  Anything between: S3-OPEN, kept. No salvage; no post-hoc lines.

## CONSEQUENCES (stated in advance, per house practice)
  S3-PHYSICAL: FND-150..153 stand as registered; the mechanism
      question sharpens to why the 4/3 cell demands THIS mode.
  S3-ARTIFACT: FND-150..153 are NOT amended by this stage (out of
      its scope), but a re-pricing commission over their
      interpretation becomes OWED and is registered as such; the
      full stage-3 resolution replication of the Q-SWEEP columns
      becomes the queue head.
  Either way the q = 5/4 committed prediction stands as committed.

## COST AND EXECUTION
Six solves total (2 cells x 2 members at 96 x 54; 2 cells x 2
members at 96 x 36 -- baseline pairs must BOTH gate for a tangent).
Estimate: hours at stage-1 per-member rates. Runs in-session on the
author's go, or packages for Opus 5 per the author's standing
instruction (runbook: analysis/WHYWIND_stage3_runbook.md).
Grants reserved to the author. Failures kept.
