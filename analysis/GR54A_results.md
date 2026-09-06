# GR54-A -- 4/3 CELL AT 144x54: RESULTS (2026-09-05)

## VERDICT: ** A-ABSENT **

The corpus's founding collapse column (4/3: registered COLLAPSE at
144x36, f_rise +0.3691, the strongest in the q-sweep) shows NO
collapse at 144x54 anywhere in the tested span A2 0.0048 - 0.0055:

  W36 (in-36-window rise)  = +0.0144   vs +0.15   does not fire
  WX  (full 20-point rise) = -0.0009   vs +0.15   does not fire

20/20 points gated at full bars (RMS all < 6e-9); seed pair gated
at 1.0e-9 / 9.5e-10; Om2 2.2163 -> 2.2448 smooth; arc steps at ds;
continuity verified on the same branch at every point. Points 12-19
were marched on the author's MacBook (run_local.sh, identical
driver and instrument, checkpoint returned to the session for the
single verdict computation); the seal held throughout.

## The profile (144x54)
rate 4.66e-4 -> 4.36e-4 (-6 pct over the span), V_pt flat to 0.5
pct, f_dir 0.1065 -> 0.1055 (flat to three decimals, one transient
bump at points 4-5 that point 6 erases -- the solver's long
corrector walks at those two points, not the branch). Full table
in analysis/gr54a_ckpt.pkl.

The 5/4 branch turned at 54 with every geometric marker (A2 gain
per step collapsing 22x, arc-step overshoot, predictor sliding
95.7 -> 48 pct). The 4/3 branch showed NONE: A2 gain constant at
3.6e-5 to the last point, no overshoot, predictor IMPROVING with
depth (94.2 -> 94.7 pct). The two collapse cells behave
qualitatively differently under phi-refinement.

## What this establishes, and what it does not (GR54's lesson)
1. The 4/3 collapse does not occur at 54 where the 36 grid placed
   it (W36), and does not occur displaced into the region where the
   5/4 collapse relocated (WX). Beyond A2 0.0055 its status at 54 is
   OPEN. This is NOT an artifact verdict: GR54 called 5/4 ARTIFACT on
   a 12-point span and was wrong by 0.0003 in A2; the 4/3 span here
   is 20 points, but "not found" remains "not found in the span."
2. "Collapse location is grid-dependent" is a ONE-CELL finding
   (5/4). The two-cell version is not supported.
3. The corpus now holds: 5/4 collapse at 36 (FND-163), displaced and
   sharpened at 54 (GR-DISPLACED); 4/3 collapse at 36 (FND-150..153
   lineage), absent to 0.0055 at 54; 5/3 flat at both. The refined
   grid separates the two collapse cells that the coarse grid made
   look alike. Whatever the mechanism, it is not one thing acting
   the same way in both cells.
4. The n=17 deep tangent object (grid-bound in both cells) was
   riding on a real collapse at 5/4 and on -- what, at 4/3? Its 36-
   grid collapse signature (f_rise +0.37, the corpus's strongest)
   has no 54-grid counterpart in the span the refined instrument can
   reach with 20 points. That is the sharpest open question in the
   program and it belongs to the 4/3 cell specifically.

## Consequences for the desk
- GR-DISPLACED claim: scope line fixed to ONE cell (5/4).
- FND-150..153 grid rider (draft): "at 144x54 the 4/3 branch marches
  flat to A2 0.0055 with no collapse signature under the C1 rule;
  the registered 36-grid collapse has no refined-grid counterpart in
  the tested span; status beyond it open."
- COMPOSITE-SELECT gating amendment: reads GR-DISPLACED for 5/4 and
  A-ABSENT for 4/3; Leg B at two refinements with 20-point budgets,
  as recommended in the queue doc.
- Next-order candidates (author's call): a 4/3 extension at 54 past
  0.0055 (cheap locally; the only way to close "open beyond the
  span"); the second-order coupling commission now has a two-cell
  discriminating target.

## Process
Verdict computed once under the locked charter + Amendment A1 (W36
computed once after the in-window stretch; it did not fire, so the
march continued as chartered). Local execution of points 12-19
disclosed; the driver never prints sealed quantities, so the seal is
unaffected by where it runs.
