# Q-SWEEP STAGE 1 -- RESULTS
# Completed 2026-08-24. Charter: analysis/QSWEEP_stage1_bars_LOCKED.md
# (+amendment 1). Benchmark: benchmarks/foundations/qsweep_stage1.py.
# State: analysis/qsweep_stage1_ckpt.pkl (exported from /tmp).
# Verdict rendered MECHANICALLY by the locked rules block.

## THE QUESTION

Is the dA2/ds collapse measured on the registered q = 3/2 branch
(6.5e-4 -> 6.8e-5, D ~ 9.6x, the wall blocking the road to the
registered R2 = 0.09396 composite geometry) a property of (a) the
rationalized q = 3/2 CELL, or (b) the aligned-branch FAMILY?
Instrument: run the identical NATIVE protocol on the neighboring
rationalizations q = 4/3 and q = 5/3 at 144 x 36 (n = 15554) and
measure each branch's rate profile between the matched targets
A2 = 0.0048 and 0.0063.

## HEADLINE

** RULE S1-SPLIT FIRED: THE NEIGHBORS DISAGREE. **

    q4/3:  5.555e-04 @ 0.00481  ->  1.045e-04 @ 0.00504   D = 5.31x
           (hi march CLOSED under the unreached-target clause at
            best full-bar A2 = 0.005042; the rate was declining
            monotonically ~25-32%/step, so the matched-target D is
            BOUNDED BELOW by 5.31x)
    q5/3:  5.670e-04 @ 0.00481  ->  5.090e-04 @ 0.00631   D = 1.11x
           (0.0063 target REACHED at member grade; final gated
            member A2 = 0.0063336, RMS 2.97e-9, clos 1.6e-10)

One neighbor reproduces the q = 3/2 collapse (D above the S1-BRANCH
line of 5); the other walks the entire span essentially flat (D far
below the S1-CELL line of 3). The collapse is therefore NEITHER a
universal family property NOR a q = 3/2 cell artifact: it DEPENDS ON
THE RATIONALIZATION. Per the locked rule, stage 2 (the
frozen-direction / frozen-cell factorization experiment) is REQUIRED
before any interpretive grant.

## THE MEASURED PROFILES (all points from full-bar members)

q = 4/3 (11 points; steps compound into collapse):
  A2       dA2/ds     step
  0.004721 5.806e-4   --
  0.004767 5.672e-4   -2.3%
  0.004812 5.555e-4   -2.1%
  0.004856 5.495e-4   -1.1%
  0.004899 5.328e-4   -3.0%
  0.004940 4.808e-4   -9.8%
  0.004975 3.859e-4   -19.7%
  0.005001 2.737e-4   -29.1%
  0.005019 1.860e-4   -32.0%
  0.005032 1.403e-4   -24.6%
  0.005042 1.045e-4   -25.5%   [march closed: asymptotic squeeze]

q = 5/3 (38 points; ruler-flat ~0.3%/step throughout; abridged):
  0.004721 5.789e-4 | 0.004812 5.670e-4 | 0.004948 5.608e-4
  0.005082 5.550e-4 | 0.005302 5.462e-4 | 0.005519 5.376e-4
  0.005732 5.294e-4 | 0.005900 5.233e-4 | 0.006067 5.174e-4
  0.006191 5.132e-4 | 0.006272 5.104e-4 | 0.006313 5.090e-4
  (full table in the exported checkpoint; cumulative decline over
   the whole span: 12.1%)

The two branches are kinematic twins at the low target (5.806 vs
5.789e-4, 0.3% apart) and then part company completely: q4/3 shed
82% within delta-A2 = 3.2e-4; q5/3 walked 5x that span shedding 12%.

## BRANCH EXISTENCE AND CELL VARIABLES (first off-3/2 branches ever)

  q4/3 member 1: A2 0.0018792  RMS 1.89e-9   clos 1.5e-7   om2 2.14842
  q4/3 member 2: A2 0.0046979  RMS 1.74e-10  clos 1.5e-8   om2 2.21540
  q5/3 member 1: A2 0.0018792  RMS 2.76e-10  clos 4.4e-11  om2 4.23408
  q5/3 member 2: A2 0.0046979  RMS 5.90e-11  clos 2.5e-11  om2 4.30871
  q5/3 final:    A2 0.0063336  RMS 2.97e-9   clos 1.6e-10  om2 4.38221

om2 is strongly q-dependent (2.15 vs 4.23 at matched amplitude,
nearly 2x across the neighbors bracketing 3/2) while drifting only
1.8-3.1% within each branch: the cell variable responds to the
rationalization, not the amplitude. Registered q = 3/2 sits between
(3.20 -> 3.27).

## WHAT S1-SPLIT MEANS FOR THE PROGRAMME

- The q = 3/2 cell is NOT acquitted (the q4/3 collapse killed the
  clean cell-artifact story), and the family is NOT convicted (the
  q5/3 flat line killed the universal-wall story). The wall is
  rationalization-selective.
- The road to the registered R2 = 0.09396 geometry is therefore not
  closed in principle: at least one neighboring rationalization
  reaches the 0.0063 amplitude regime effortlessly. Whether the
  PHYSICAL composite requires the 3/2 cell or can live on a 5/3-type
  cell is exactly a stage-2 question.
- Sigma_wave consequences remain open pending stage 2; no
  registered claim changes in this stage.
- Stage 2 (mandatory per the rule): the frozen-direction /
  frozen-cell factorization experiment -- transplant the direction
  field between cells to separate what collapses.

## INSTRUMENT RECORD (annotated at their code sites)

- Closure-aware stop (gate-facing solves satisfy RMS AND closure).
- TRUST CAP |dx| <= 0.05 before the acceptance ladder: broke the
  q5/3 member-1 deterministic limit cycle (descend, poison
  floor-leap, rejection cascade, rung replay -- measured twice,
  digit-identical) and carried every subsequent solve without one
  rejection cascade.
- Rejection-abort persistence (aborts keep their solve key; retries
  resume instead of replaying).
- Arc march with sub-target steps; a2 pins left abandoned on both
  columns (blind where dA2/ds shrinks), consistent with the
  registered q = 3/2 record.
- FORCING escalation: fired throughout as designed post-cap.

## PROVENANCE

Every rate point above derives from a member passing ALL locked
gates (RMS < 1e-8, closure < 1e-6, geometry floors, wsNyq). No
confirmation debt outstanding. The q4/3 fine-pin abandonment, the
q4/3 unreached-target closure, and the q5/3 reached-target closure
are recorded in the checkpoint with reasons. Draft registration:
analysis/QSWEEP_stage1_draft_registration.md -- NOT registered;
awaiting the author's grant.
