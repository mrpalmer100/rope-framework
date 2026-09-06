# SPARSE-J COMMISSION -- C3-C5 RESULTS AND VERDICT (2026-08-29)
# Under analysis/SPARSEJ_charter_LOCKED.md, continuing
# analysis/SPARSEJ_checkpoint_2026-08-29.md (C1-C2 evidence there).
# Ships in the NEXT release; v3.29.0 closed.

## VERDICT: ** SJ-CREDENTIALED ** (C1-C5 all pass)

Per the charter's locked consequence: the probe42 retry and the
stage-3 resolution replication RETURN TO THIS CONTAINER'S QUEUE,
each under its own charter; the queue-head hardware note is amended
from "capable hardware" to "capable instrument". Grants reserved to
the author; nothing here adjudicates physics.

## C3 -- RATE CREDENTIAL: ** PASS **

Two consecutive arc-rate points of the q = 4/3 profile re-marched
from the retained stage-2c states (states[0], states[1]) with the
sparse instrument (SparseJac + BandedTorusSolver via gn_sparse),
the arc-step machinery replicated verbatim from qsweep_profile.run
(tangent predictor, ds = 0.08, full gates, identical
rate/V_pt/f_dir formulas). Bar: 1 percent, point-by-point.

  point 0: rate 5.802913e-04 vs registered 5.806063e-04
           deviation 0.054 percent   PASS
  point 1: rate 5.669181e-04 vs registered 5.671585e-04
           deviation 0.042 percent   PASS

Both points gated at full bars (RMS < 1e-8 AND closure < 1e-6).
Point 1, marched on the fully corrected instrument from the start,
converged in seven consecutive full-fraction accepted rounds with
no fallbacks -- the f64 exact route's quadratic tail. Point 0's
early grind was fault-9 damage (below), not physics; all its
iterates were monotone-accepted on the true wres and remain
legitimate.

## C4 -- MEMORY CEILING: ** PASS ** (the commission's reason to exist)

Peak RSS of one FULL solve round (jacobian + factor + solve +
acceptance ladder), fresh process per grid, sampled at 50 ms from
/proc alongside ru_maxrss:

  grid     n       pattern nnz   peak RSS      round
  144x36   15554   18,920,267    1.814 GB      accepted
  144x42   18146   22,115,948    2.095 GB      accepted
  144x54   23330   28,531,449    2.674 GB      accepted   [bar 3.0]

  C4: 2.674 GB <= 3.0 GB  -- PASS, with 0.33 GB daylight under the
  bar and ~1.3 GB under the container ceiling. The phi-major design
  claim held: bandwidth does not grow with NP, so memory grows
  sub-linearly in NP (the route improves at the larger grid, as the
  checkpoint predicted).

States at 42/54: the retained 144x36 member prolongated along phi
by Fourier refinement (pt unwrapped, winding trend carried
explicitly). MEMORY MEASUREMENT ONLY -- no solve claims from
prolongated states (the charter's S3 synthetic-state rule, same
logic). At 42 and 54 the jacobian entered the measured process from
its byte-identical memo (J fully resident through factor + solve +
ladder -- the true co-residency of a round; jac-build scratch, one
residual + one probe vector, is negligible and excluded). Practical
note: with the resume memos writing (SJ_MEMO=1), transient pickle
copies add ~0.4 GB; marches at 54 in this container class should
run SJ_MEMO=jac.

Round timings at 54: pattern (one-time, cached) 46 s; jacobian
~50 s fresh / 0.5 s memo; factor 129 s; solve <1 s.

## C5 -- LEDGER HONESTY: ** PASS **

All nine construction faults annotated at their code sites before
the credential evidence above was produced: faults 1-3 (spike doc +
the superseded-solver rationale sites), 4-6 (BandedTorusSolver
header, make_instrument), 7-9 (below, at their fix sites). The
spike's pymetis to-do is MOOT: the METIS ordering served only the
fault-6-superseded BorderedSolver and was removed (identity perm
kept for the cache-format contract); pymetis is NOT added to
requirements.

## INSTRUMENT LEDGER, FAULTS 7-9 (found in the C3 march; kept)

7. HIST BOOKKEEPING NOT VERBATIM (D5 violation in the C2-session
   port): gn_sparse appended to hist on every round, uncapped;
   gn_lean appends only on ACCEPTED rounds, capped at 4. The stall
   trigger fired on every no-step and the gnx branch re-floored lam
   perpetually. Restored to verbatim.
8. CLOSURE-AWARE STOP MISSING: gn_sparse broke gate-facing solves
   on RMS alone; gn_lean's 2026-08-23 closure-aware stop (break
   only when RMS AND closure clear their bars) was not ported --
   the exact gate-racing defect that annotation records. Restored
   at both stop sites. C2's verdict is unaffected: its bars were
   measured directly post-run.
9. PATTERN REUSED ACROSS PIN MODES (the C3 stall's cause): the
   C1/C2 pattern was silently reused for the arc chart, whose arc
   row -- dense in ALL columns -- it did not contain. Measured as
   O(1) jacobian entries missing from row m-3 at the stall point
   (field converged, closure pinned at 1.01e-5: the solver could
   not see the constraint it was asked to satisfy). The cache key
   now includes pin_mode. Fault 4's lesson extends: measure the
   pattern of the residual you will actually solve -- INCLUDING its
   pin mode.

## ENGINEERING CHANGES THIS SESSION ([SJ-OPT], no logic changes)

- Band-scatter vectorized (the C2 checkpoint's annotated
  optimization candidate): precomputed fancy-index scatter per
  slice-offset; verified vs the dense reference at 48x12 to
  2.8e-11 (bar 1e-10). Residual factor cost is structural (banded
  border solves + block products).
- Cross-process memoization of J and the factor (content-hash
  keyed, byte-identical replay), env-gated (SJ_MEMO=1/jac/0):
  required because this container reaps at ~3-minute tool
  boundaries and a rejected round exceeded one window, so the lam
  escalation could never persist -- the same failure the 2026-08-22
  LAM PERSISTENCE annotation records, one level down.
- METIS ND ordering removed with the superseded BorderedSolver.

## STANDING

Registry untouched. Grants reserved to the author. Failures kept.
The credentialed instrument is benchmarks/foundations/
sparsej_instrument.py with pattern caches
analysis/sparsej_pattern_144x36.pkl (keys 144x36:arc, 144x42:arc,
144x54:arc; the un-suffixed 144x36 key is the C1/C2-era pattern,
kept for the record). Drivers: sparsej_c3.py, sparsej_c4.py.
