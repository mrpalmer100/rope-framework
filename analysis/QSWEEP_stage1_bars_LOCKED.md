# Q-SWEEP STAGE 1 charter and bars -- LOCKED 2026-08-22 BEFORE COMPUTING

Authorized by the author 2026-08-22, on FND-146's Rule C promotion.
PURPOSE: the q-sensitivity probe (external review step 2; the
author's stage 1). Rule C acquitted Jacobian degeneration on the
measured branch; the two survivors are the branch DIRECTION FIELD
and the RATIONALIZED CELL, and stage 1 asks the cell question first:
does the dA2/ds collapse depend on the rationalization q = 3/2, or
does it persist unchanged on neighboring rationalizations?

## THE PARAMETER, STATED HONESTLY

q = K2/K1 = N2/N1 is a RATIONALIZATION, not a knob: the cell must
hold N1 whole level-1 periods (LCELL = N1 * sqrt(3)) and N2 whole
level-2 periods (K2 = N2 * 2pi / LCELL). "Local" variation therefore
means NEIGHBORING RATIONALS ON LARGER CELLS. Stage 1 takes the two
nearest affordable neighbors:

  q = 4/3  (N1 = 3, N2 = 4, cell 3 sqrt(3))
  q = 3/2  (N1 = 2, N2 = 3, cell 2 sqrt(3))  -- the REGISTERED
           baseline; its trajectory is cited, not recomputed
  q = 5/3  (N1 = 3, N2 = 5, cell 3 sqrt(3))

Grid density is MATCHED, not grid size: 48 s-points per sqrt(3)
(the NATIVE-96 density), so the q = 4/3 and 5/3 cells run at
144 x 36 (n = 15554). The level-2 wave is physically different at
different q (K2 changes); the question is whether the SAME aligned
two-frequency construction shows the same amplitude-growth collapse
at comparable A2. R1, R2, TBAR, K1, and the level-1 sector are
q-independent by construction and shared by all three columns.

## PROTOCOL (the NATIVE protocol, replicated per q; no cross-cell
## seeding -- the FND-143 lesson binds)

Per q in {4/3, 5/3}:
  P1  NATIVE LEVEL-1 RECOVERY on the q-cell (level-1 physics is
      q-independent; this is the instrument control).
  P2  RAMP to members at the registered waypoints A2 = {0.02, 0.05,
      0.10} * R2 (= 0.00188, 0.00470, 0.00940), each solved to the
      full acceptance gates.
  P3  RATE MEASUREMENT: member-grade dA2/ds by arc-length pairs at
      matched A2 targets {0.0048, 0.0063}, the two points where the
      q = 3/2 collapse is registered (6.5e-4 -> 6.8e-5, the
      eightfold). Rates cite full-bar states only (standing rule).
      Tangent and cell variables (om1, om2, gamma, closure, wsNyq)
      recorded at every member.

## INSTRUMENT (new, validated before use; no physics changes)

QGrid: the stage-2 Grid and TGrid charts parameterized by
(N1, N2) -- identical operators, stencils, pins, and weights; only
LCELL, K2, and the grid size change, exactly as the existing
constants prescribe. VALIDATION BARS (halt-grade, before any P2/P3
computing):
  (v1) At q = 3/2, NS = 96: QGrid must REPRODUCE the registered
       instrument -- level-1 recovery at the registered grades
       (theta constant ~1e-9, Om1 rel ~1e-5) and the S1 member
       re-verified to its registered metrics at 1e-6 relative.
  (v2) At q = 4/3 and 5/3: native level-1 recovery to the same
       grades (level-1 does not know q; failure means the cell
       construction is wrong, not the physics).
  (v3) Closure remains halt-grade (< 1e-6) for every accepted
       member on every cell (the FND-143 promotion binds here too).
  (v4) The f64 true-operator check (SVD-DIAG amendment 2) is
       retained wherever a Jacobian quantity is cited.

## REGISTERED INTERPRETATION RULES (locked before results; anything
## else is NO CALL)

Let D(q) = [dA2/ds at A2 = 0.0048] / [dA2/ds at A2 = 0.0063] -- the
collapse factor (registered value at q = 3/2: ~9.6x from 6.5e-4 /
6.8e-5).

  RULE S1-CELL: the collapse is ABSENT or strongly reshaped on the
      neighbors -- D(4/3) and D(5/3) both < 3 while member-grade
      rates hold. Registered reading: the collapse is a property of
      the q = 3/2 rationalized cell. (The author's causal step 2,
      the frozen-direction/frozen-cell split, is then chartered to
      confirm mechanism.)
  RULE S1-BRANCH: the collapse REPRODUCES -- D(4/3) and D(5/3) both
      > 5. Registered reading: the collapse is intrinsic to the
      aligned-branch family (direction-field mechanism leads); the
      cell is acquitted at stage 1 grade.
  RULE S1-SPLIT: the neighbors DISAGREE with each other (one < 3,
      one > 5). Registered reading: q-asymmetric -- neither
      mechanism is confirmed; stage 2 (the split experiment) is
      REQUIRED before any interpretive grant.
  Anything else (either D in [3, 5], or a member fails its gates so
      a D cannot be formed from full-bar states): NO CALL at that
      q; report and stop.

If a ramp cannot reach a waypoint on a neighbor cell at member
grade, that is itself a REPORTED RESULT (the branch may not exist
at that q at that amplitude), not a failure to hide: the waypoint
is recorded as unreached with its best full-bar A2.

## SCHEDULING (budgets, not bars)

n = 15554 per neighbor cell: solves via the established f32-J
machinery (trf/lsmr scout phases; gnx-f32j endgame with blocked f64
normal accumulation -- the 2.4 GB budget measured at S4). Detached,
MEMORY-EXCLUSIVE, per-member checkpointing to /tmp/qsweep_ckpt.pkl;
caps are budgets and adjudicate nothing; a reaped run resumes. The
stage is expected to span multiple sessions; partial states are
exported to analysis/ at every close-out.

LOCKED before any Q-SWEEP computing. Amendments, if any, go below
this line with their reasons.

## AMENDMENT 1 (2026-08-22, recorded before any neighbor-cell
## interpretation)

WHAT WAS FOUND: the dense-J trf solver OOMs this container at
n = 15554 (measured, RSS 3.75 GB of 4), so neighbor-cell solves run
on a lean f32-J Gauss-Newton/lsmr ladder instead. On the q = 4/3
cell that ladder LOST THE m2 MODE from the injection seed three ways
(bare, basin-guarded, sub-pinned): every descent direction drives A2
to zero and the first waypoint gates FAILED at A2 = 8.5e-5 against
1.88e-3. This CANNOT be read as a branch-existence result yet,
because the registered q = 3/2 ramp was landed by trf -- a DAMPED
trust-region method -- and an undamped GN line search is known to
quench weak modes far from solution. The solver is an uncontrolled
variable.

WHAT CHANGES (both stricter; thresholds and rules untouched):
  1. The ladder gains LEVENBERG-MARQUARDT DAMPING (lsmr damp
     parameter, adaptive mu with accept/reject) -- the trust-region
     character the registered ramp solver had. Acceptance stays the
     f64 monotone residual test; the degenerate-basin guard stays.
  2. NEW VALIDATION BAR (v5), halt-grade: before ANY neighbor-cell
     ramp outcome is interpreted, the identical ladder + guard +
     sub-pin protocol must REPRODUCE the registered q = 3/2 first
     waypoint member from the injection seed at 96 x 36 (where the
     branch provably exists). If the control fails, the outcome at
     the neighbors is an INSTRUMENT statement and no branch claim of
     any kind is made. The failed q = 4/3 attempt is kept on the
     record and marked pre-(v5).
