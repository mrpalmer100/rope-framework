# SPARSE-J INSTRUMENT COMMISSION -- CHARTER (LOCKED 2026-08-29)
# Authorized by the author 2026-08-29 ("Yes let's charter it"), in the
# handoff-review session, after v3.29.0 was cut. Locked BEFORE any
# sparsity measurement, construction, or solve.

## THE QUESTION
The queue-head work (the FND-159 probe retry and the full stage-3
resolution replication) is blocked on "hardware where 144x54+ is
feasible." The block is a REPRESENTATION choice, not physics: the
instrument's Jacobian is dense finite-difference (TGrid96.jac,
column-chunked) and the solve accumulates a dense n x n normal
matrix -- ~4.3 GB f64 at 144x54 (n ~ 23,300), over this container
class's ceiling. The registered operator is LOCAL; its true
Jacobian is sparse. COMMISSION: build and credential a sparse-f64
re-instrument such that 144x54+ full-bar gating is feasible in the
~4 GB container class.

## SCOPE (hard boundary)
This is an INSTRUMENT commission: engineering, credential, and a
measured memory ceiling. It adjudicates NO physics. The probe42
retry and the stage-3 replication remain separately chartered
adjudications that may run on this instrument ONLY if it
credentials. A refusal reproduced under this instrument's full-f64
exact solve would be evidence-bearing for state-intrinsic
fragility, but that reading belongs to the retry's charter, not
this one.

## DESIGN COMMITMENTS (locked)
D1. The residual is REUSED UNCHANGED: the instrument calls the
    registered wres of the stage-1/2 chart byte-identically. No
    physics code is rewritten.
D2. The Jacobian is assembled SPARSE by finite-difference GRAPH
    COLORING over the residual's measured dependency pattern
    (columns probed in non-overlapping groups, scattered into
    CSR). Same h = 1e-8 * (1 + |x|) probe steps as the dense jac.
D3. FULL f64 END-TO-END in the solve path. The f32-J rule was a
    memory workaround (three mapped OOM incidents); this
    instrument retires it. No mixed precision.
D4. The linear solve is a sparse bordered factorization: sparse
    core (stencil rows) + dense border (pin/phase/global rows,
    identified by measured row density), solved exactly
    (factor + Schur complement on the border). No iterative
    approximation in the acceptance path.
D5. Solver logic above the linear algebra (acceptance ladder,
    trust cap |dx| <= 0.05, rejection-abort persistence, gates,
    bars) is carried over UNCHANGED from the registered
    instrument.

## THE SPIKE (pre-credential engineering measurements; adjudicate
## nothing; reported in the results doc)
S1. Empirical dependency pattern of wres at a retained 144x36
    gated member (qsweep_stage2c_ckpt.pkl, read-only): perturb
    single components, record which residuals move; report
    nnz/row distribution and any dense rows.
S2. Coloring count for the measured pattern (number of residual
    sweeps per Jacobian assembly).
S3. Measured sparse-factor fill and peak memory of one bordered
    factorization at 144x36, 144x42, 144x54 (synthetic state at
    the larger grids is acceptable for the FILL measurement only;
    no solve claims from synthetic states).

## CREDENTIAL BARS (all locked now; ALL must pass for the verdict
## SJ-CREDENTIALED; any miss is SJ-F-INSTRUMENT, kept)
C1. OPERATOR IDENTITY: sparse J agrees with the dense jac
    column-by-column on 64 randomly chosen columns at a retained
    144x36 member, max abs deviation <= 5e-6 (f32-store tolerance
    of the reference), AND J @ v agrees on 16 random unit vectors
    to the same tolerance.
C2. ANCHOR: from the retained 144x36 member perturbed by 1e-4
    relative Gaussian noise, the instrument re-converges to the
    SAME member: RMS <= 1e-9, |A2 - A2_reg|/A2_reg <= 1e-6,
    |om2 - om2_reg|/om2_reg <= 1e-6.
C3. RATE CREDENTIAL: two consecutive arc-rate points re-marched
    from retained states reproduce the registered FND-147-profile
    rates within 1 percent, point-by-point.
C4. MEMORY CEILING (the commission's reason to exist): peak RSS
    of a full solve round at 144x54 <= 3.0 GB, measured, leaving
    daylight under the container ceiling. Reported alongside:
    the same measurement at 144x36 and 144x42.
C5. HONESTY OF THE LEDGER: every fault found during construction
    is annotated at its code site before the credential runs are
    trusted (house instrument-ledger rule).

## VERDICT FORMS (exactly three)
  SJ-CREDENTIALED: C1-C5 all pass. CONSEQUENCE: the probe42 retry
      and stage-3 replication return to THIS container's queue,
      each under its own charter; the queue-head hardware note is
      amended from "capable hardware" to "capable instrument".
  SJ-F-INSTRUMENT: any of C1-C3/C5 fails. Fault kept; the
      hardware note stands; the dense instrument remains the
      instrument of record.
  SJ-INFEASIBLE: C1-C3/C5 pass but C4 fails (the sparse route is
      correct but does not fit). Measured ceiling recorded; the
      hardware note stands with the measured number.

## NO-RESCUE RULE
No per-state or per-grid tuning of the coloring, border
identification, or factorization ordering after the spike numbers
are seen. One instrument, all grids. Failures kept on the record.

## STANDING
Registered claims untouched by this commission. Grants reserved to
the author. This charter and its results ship in the NEXT release;
v3.29.0 is already cut and closed.
