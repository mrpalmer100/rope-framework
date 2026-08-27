# Q-SWEEP STAGE 2 -- REPORT: F-INSTRUMENT (per the charter's own
# clause), WITH A MEASURED FINDING: THE WINDING FIELD IS
# LOAD-BEARING ALONG THE ALIGNED BRANCH
# Executed and closed 2026-08-26 under
# analysis/QSWEEP_stage2_charter_LOCKED.md (+amendments 1-3, all
# pre-computation or single-repair-cycle daylight). Instrument:
# benchmarks/foundations/qsweep_stage2.py. State:
# analysis/qsweep_stage2_ckpt.pkl.

## VERDICT

** F-INSTRUMENT. ** The X3a self-control (q = 4/3 cell, its OWN
winding field frozen) is gate-INFEASIBLE under the arc march at
both the chartered ds = 0.08 and the single-repair-cycle
ds = 0.02. By the charter's rule (X3 controls failing after one
daylight repair cycle), stage 2 as chartered STOPS AND REPORTS.
No transplant (X1/X2) was run; no transplant number exists to
mislead.

## THE MEASUREMENT THE CONTROL DELIVERED

1. ANCHOR CREDENTIAL (machinery exact): with pt frozen and the
   free sector (th, T, om1, om2) solved at the fixed anchor
   A2 = 0.0046979, the native member is recovered at RMS 1.7e-10,
   closure at stage-1 grade -- the compose/reduce/solve chain is
   correct. The infeasibility below is therefore PHYSICS of the
   marched system, not instrument error.

2. LOAD-BEARING WINDING FIELD: marching the arc with pt frozen
   reaches a constrained optimum that cannot gate:
     ds = 0.08: wres floor 2.457e-2 (field block only 3.9e-3;
       the arc row itself carries 2.31e-2 -- the solve sits 29
       percent short of the commanded arclength); RMS floor
       3.1e-5 vs the 1e-8 bar.
     ds = 0.02: wres floor 6.142e-3, RMS floor 7.9e-6.
   The floors scale LINEARLY with ds (2.46e-2 x 0.25 = 6.1e-3,
   measured 6.14e-3): the frozen-field misfit is first order in
   arclength, so no ds large enough to measure a rate can gate.
   CONCLUSION: the winding field pt EVOLVES NECESSARILY with
   amplitude along the branch -- direction and amplitude
   co-evolve inseparably at gate grade. The factorization premise
   of the chartered experiment (freeze one sector, march the
   other) fails physically.

## WHAT THIS MEANS FOR THE S1-SPLIT QUESTION

The stage-1 verdict left "the collapse rides the direction field"
vs "rides the cell" to be separated by transplant. This stage
shows the direction field is not a transplantable boundary
condition: it is dynamically coupled to amplitude on every cell.
Any viable stage-2b must compare the direction field's EVOLUTION
between cells rather than freeze it. Candidate redesigns
(recorded for the author, none chartered):
  (a) pt-velocity comparison: measure d(pt)/ds along each native
      branch at matched A2; ask whether the collapsing cells
      (3/2, 4/3) share a pt-evolution signature the flat cell
      (5/3) lacks.
  (b) increment transplant: march cell A while ADDING cell B's
      measured pt-increments per step (transplanting the motion,
      not the state).
  (c) mixed-sector arc: include pt in the march but penalize its
      deviation from the foreign pattern with a pre-registered
      weight ladder; measure the rate as the weight is released.

## INSTRUMENT LEDGER (three faults found and fixed BEFORE the
## physics floor was trusted; all annotated at their code sites)

- Zombie lock-holders: reaped setsid wrapper shells held the
  flock with no python behind them, silently refusing launches
  (lesson: rotate lock files; verify worker RSS before trusting a
  "running" pid).
- OOM: Jr.T.astype(f64) materialized a 1.3 GB Jacobian copy per
  gradient refresh; fixed with f32 gemv + lower-triangle-only
  Cholesky (no symmetrization transient).
- Chord Cholesky: the chord loop refactored the 10370^3/3
  Cholesky per chord step, blowing the reap window; fixed by
  factor reuse (a triangular solve per chord step). Post-fix the
  solver ran 16x faster (wres 4.0e-1 -> 2.5e-2 in four windows)
  and reached both floors cleanly -- which is why the floors are
  trusted as physics.

## STANDING

Stage 2 as chartered: CLOSED, F-INSTRUMENT, with the load-bearing
winding-field finding as its product. Stage-2b: candidate designs
above, unchartered, awaiting the author. The S1-SPLIT interpretive
freeze from FND-147 REMAINS IN FORCE (the mandate was stage 2 or
equivalent before interpretive grants; F-INSTRUMENT does not lift
it). Draft registration of the finding:
analysis/QSWEEP_stage2_draft_registration.md, AWAITING THE AUTHOR.
