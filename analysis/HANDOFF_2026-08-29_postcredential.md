# SESSION HANDOFF -- POST-CREDENTIAL QUEUE STATE (2026-08-29)
# Written at the close of the SPARSE-J C3-C5 session. Read this
# FIRST in any session picking up the queue. Ships in the NEXT
# release; v3.29.0 closed.

## WHAT IS NOW TRUE

1. SPARSE-J is ** SJ-CREDENTIALED ** (C1-C5 all passed;
   analysis/SPARSEJ_credential_results.md). The dense instrument's
   hardware note is AMENDED: 144x54 full-bar gating is feasible IN
   THIS CONTAINER CLASS (measured 2.674 GB round peak vs the
   3.0 GB bar). "Capable hardware" reads "capable instrument";
   prerequisite 1 of WHYWIND_queue_action_approved.md is SATISFIED
   by instrument, and the approved work order is executable here.
2. Registry prerequisite (item 3 of the approved action) HOLDS:
   FND-154..161 and the FND-152/153 hardened riders are in
   claims.yaml. New work cites registered numbers.
3. The instrument of record for large-grid solves is
   benchmarks/foundations/sparsej_instrument.py (SparseJac +
   BandedTorusSolver + gn_sparse). The dense gn_lean remains the
   instrument of record at 144x36 and below.

## HOW TO RUN THE SPARSE INSTRUMENT (operator notes)

- PATTERN CACHE: analysis/sparsej_pattern_144x36.pkl, keyed
  '<NS>x<NP>:<pin_mode>'. FAULT-9 RULE: a pattern is valid ONLY for
  the pin mode it was measured under. Cached: 144x36:arc,
  144x42:arc, 144x54:arc. Any new (grid, pin_mode) builds fresh
  (~45-90 s, one probe per column) and caches.
- MEMO MODE: env SJ_MEMO. '1' = full memos (J + factor; adds
  ~0.4 GB transient at 54), 'jac' = J only (USE THIS at 144x54),
  '0' = none (measurement runs). Memos live in /tmp/sjjac_*,
  /tmp/sjfac_*, content-hash keyed; prune to newest 2-3 between
  chunks (each pair up to ~0.9 GB).
- REAP-WINDOW CHUNKING: this container kills work at ~3-minute
  tool boundaries. Drivers must persist EVERY solver round (see
  the PersistDict pattern in sparsej_c3.py -- pickle dict(st), the
  subclass itself does not pickle) and be rerun until done. With
  memos, a killed chunk resumes at full speed.
- COSTS (144x54): pattern 46 s once; jacobian ~50 s fresh / 0.5 s
  memo; factor 129 s; solve <1 s. A clean quadratic march is
  5-10 rounds; budget ~2-4 chunks per gated member.
- KNOWN GOOD: arc marching (C3), anchor re-convergence (C2).
  NOT YET EXERCISED: 'a2'-pinned solves under gn_sparse (the p42
  retry below is the first; its pattern will be the first a2-mode
  build).

## THE QUEUE (work order of WHYWIND_queue_action_approved.md,
## unchanged in order, hardware condition now met)

1. ** p42|4/3|deep RETRY: DONE. GATED, then P42-ARTIFACT ** (see
   analysis/WHYWIND_p42_retry_results.md -- the refusal was
   instrument-intrinsic; the n=17 winding demand is a 144x36
   discretization object; FND-160/161 GRANTED and REGISTERED (registry at 161);
   the stage-3 replication charter should be written with
   P42-ARTIFACT as the prior). Original entry follows for the
   record:
   (was: IN PROGRESS as of this handoff --
   driver benchmarks/foundations/whywind_p42_retry.py, checkpoint
   /tmp/p42r_ckpt.pkl, durable export
   analysis/whywind_p42_retry_ckpt.pkl on any gate/refusal).
   One retry, per the WHYWIND-F clause. Charter: the LOCKED
   WHYWIND_probe42_bars_LOCKED.md, unchanged -- seed is the
   charter's phi-only FFT zero-pad of 2c states[12] (NOT the
   refusal session's endgame state, which slid off its
   constraints), pin 'a2' at the member's own A2, stage-1 full
   bars. IF IT GATES: run the locked P42 verdict lines (F17
   credential on retained 144x36 states first, then the 144x42
   band statistic; lines and consequences are in the charter --
   nothing post-hoc). IF IT REFUSES on this instrument's full-f64
   exact solve: that refusal is evidence-bearing for
   state-intrinsic fragility PER THE RETRY'S CHARTER (the
   SJ charter's scope clause), and registers per the WHYWIND-F
   clause. Either way the outcome is a deliverable.
2. ** DONE: S3R-ARTIFACT-CONFIRMED ** (analysis/S3R_results.md --
   all four members gated, S3R-CRED passed, F17_54 = 0.0000 and
   HIBAND54 = 0.0000; FND-162 GRANTED with scope rider (registry at 753); the
   FND-150..153 interpretation re-pricing commission has ripened;
   fault 10 caught latent). Original entry:
   (was) Full stage-3 resolution replication of the Q-SWEEP columns at
   144x54+ (both cells). NEEDS A FRESH BARS-LOCKED CHARTER before
   any computation (prerequisite 4 -- not yet written; the stage-3
   runbook is the operator base; the F17 >= 0.20 credential line
   refused at 96x36 and must be re-derived for the larger grids
   IN THE CHARTER, not after numbers are seen).
3. The q = 5/4 fourth-cell column (bundled by the author's
   standing instruction): adjudicates the committed FLAT
   dispersion prediction AND, independently, the grid question of
   WHYWIND-D/E/F. Also needs its own charter.

## HOUSE RULES THAT BIT THIS SESSION (so they do not bite yours)

- D5 means VERBATIM: two solver-schedule defects (faults 7-8) came
  from an almost-right port. Diff against gn_lean line-by-line
  when touching gn_sparse.
- Fault 4/9: measure the pattern of the residual you will actually
  solve -- grid AND pin mode.
- Monotone acceptance on the true wres is what made the fault-9
  recovery legitimate mid-march; never weaken it.
- Durable exports to analysis/ at close-out; /tmp is not a record.

## STANDING
Registry untouched by this handoff. Grants reserved to the author.
Failures kept.
