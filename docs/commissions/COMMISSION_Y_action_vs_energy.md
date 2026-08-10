# COMMISSION Y: CANONICAL ACTION vs ENERGY DRESSING
# (chartered 2026-08-06, Mark's go-decision, on an external review that caught
# a premature closure. LEAD-2 was killed because W's solver computed a dressing
# D_E = 1.1051029 that missed the required 1.40681 by 21% -- but that miss was
# measured against 1/alpha = pi^4 D. The reviewer noted the solver value fits a
# DIFFERENT geometric prefactor, 1/alpha = 4 pi^3 D, to 179 ppm (0.018%), and
# 4 pi^3 / pi^4 = 4/pi EXACTLY. Critically, 4/pi is a LINEAR rectified-response
# factor (<|cos|+|sin|> = 4/pi) while the solver computed an ENERGY (quadratic:
# cos^2+sin^2=1, no 4/pi). So the hypothesis is not "multiply by 4/pi" -- it is
# that alpha couples to a CANONICAL ACTION (linear in the response), not the
# energy, and the two differ by exactly the 4/pi the numerology shows. Y tests
# whether that action ratio is PRODUCED mechanically from the same solver
# solution. This reopens LEAD-2 in corrected form with a blind pass/fail.)

## What was overlooked (stated plainly)
Two things, both real:
1. PREMATURE PREFACTOR LOCK. LEAD-2's death assumed 1/alpha = pi^4 D. Against
   pi^4 (=97.409) the solver's D_E=1.105 misses by 21%. Against 4 pi^3
   (=124.025) the SAME blindly-computed D_E fits to 179 ppm:
   4 pi^3 x 1.1051029 = 137.0605 vs measured 137.0360. The solver did not
   compute a wrong number; it may have been compared to the wrong prefactor.
2. ENERGY vs ACTION CONFLATION. W's solver computed D_E = (E_elastic - E_log
   + E_rot)/E_rot, an ENERGY ratio (quadratic in the field). alpha may couple
   to a CANONICAL ACTION / rectified response (linear in the field). Linear
   and quadratic rotating quantities differ generically -- and the specific
   difference between a rectified linear response and a quadratic one is
   <|cos|+|sin|> vs cos^2+sin^2, i.e. exactly 4/pi. This is why D_J (action)
   can legitimately differ from D_E (energy) by 4/pi where a naive "multiply
   the energy by 4/pi" would be unjustified.

## THE HYPOTHESIS (sharp, falsifiable, blind)
From the SAME converged W-solver solution (w_dressing_phase1c.py, D_E=1.1051029
committed, in the package), compute the CANONICAL PHASE MOMENTUM ratio
  D_J = P_chi^full / P_chi^reduced,
where P_chi = dL_eff/d(chi_dot) = I_chi chi_dot + A_chi is LINEAR in the
response (the collective-coordinate momentum of the rotating phase chi),
INCLUDING core, far-field tether deformation, geometric strain, any Berry/
gyroscopic term A_chi, and the 4pi (double-cover) closure. The test:
  DOES D_J / D_E = 4/pi = 1.27324 FALL OUT MECHANICALLY?
If yes, the 4/pi is DERIVED, not noticed, and 1/alpha = 4 pi^3 D_E holds at
179 ppm with a computable residual correction.

## THE BARS -- GENEROUS ON THE SCIENCE, STRICT ON PROVENANCE
- BLIND FIRST: compute D_J from the solver solution's canonical action BEFORE
  comparing to 4/pi or alpha. D_J is an output; 4/pi is the menu item it is
  checked against, not a target fitted to. (The solver D_E is already
  committed and frozen -- this is the strongest possible blind setup: the
  energy number exists, and Y computes an INDEPENDENT action number from the
  same solution.)
- THE LINEAR/QUADRATIC DISCIPLINE (the physics gate): the 4/pi is admissible
  ONLY if D_J is genuinely a LINEAR rectified-response / canonical-action
  quantity. Y must exhibit that P_chi is linear in the field (as a canonical
  momentum is) and that its rectification structure produces the 4/pi -- NOT
  assert 4/pi because it fits. If D_J comes out quadratic-like (= D_E, no
  4/pi), the hypothesis is FALSIFIED, cleanly.
- SUCCESS IS WIDE-BUT-SHAPED: D_J/D_E landing in ~1.24-1.31 with the RIGHT
  MECHANICAL ORIGIN (rectified linear response) counts as a hit; the exact
  4/pi with a small tether-anisotropy correction is the target. Right-origin-
  off-magnitude is a lead pursued to a second prediction.
- THE SECOND PREDICTION (the arbiter): if D_J = (4/pi) D_E holds, then
  1/alpha = 4 pi^3 D_E predicts 137.0605, 179 ppm high. The reviewer's
  mechanical prediction is that a computable angular harmonic of the tether
  configuration, eps_4 ~ 0.00268, supplies the (1 - eps_4/15) correction that
  closes the 179 ppm. Y's SECOND prediction: compute eps_4 from the tether's
  f_4 perturbation (linear perturbation around the radial solution f_0) and
  test whether it lands ~0.00268, closing 1/alpha to <ppm. A derived eps_4
  that closes the residual GRADUATES the whole chain; a wrong eps_4 leaves the
  4/pi as a 179 ppm near-miss (still a real result, honestly bounded).
- LOOK HARD, KEEP CANDIDATES: if the exact 4/pi does not fall out but a
  related rectification factor does, keep it as a lead with its own second
  prediction. Do not kill on one number.

## THE SCOPE CAP -- HARD
- Y is the ACTION-vs-ENERGY ratio D_J and (if it holds) the eps_4 correction.
  Two computations on ONE existing solver solution.
- No new solver, no new commission spawned. If D_J confirms and eps_4 closes,
  that is the result; if not, the boundary is registered. Follow-ons NAMED
  for Mark's go-decision, not opened.
- One commission.

## READY TO RUN (verified 2026-08-06)
w_dressing_phase1c.py is in the package (explorations/), runs, and commits
D_E = 1.1051029 to 7 digits. Y extends it: from the SAME converged f(r)
solution, compute the canonical phase momentum P_chi (linear in the field,
with the gyroscopic/Berry term and 4pi closure) and form D_J; compare
D_J/D_E to 4/pi; then compute eps_4 from the f_4 tether perturbation and test
1/alpha = 4 pi^3 D_E (1 - eps_4/15). No rebuild -- the solver solution exists.

## PHASE STRUCTURE (one session)
- PRIMARY: derive the effective collective-coordinate Lagrangian L_eff for the
  phase chi from the solver's functional; compute P_chi^full and P_chi^reduced
  (the canonical momentum, linear in the response) on the converged solution;
  form D_J = P_chi^full/P_chi^reduced. Compare D_J/D_E to 4/pi BLIND.
- LINEAR/QUADRATIC CHECK: exhibit that D_J is linear-response (why the 4/pi is
  legitimate) or find it is not (falsification).
- SECOND PREDICTION: compute eps_4 from the f_4 perturbation; test
  1/alpha = 4 pi^3 D_E (1 - eps_4/15) against 137.0360.
- REGISTER per the ladder below.

## Registrable outcomes
1. ALPHA CRACKED (the summit): D_J = (4/pi) D_E falls out mechanically from
   the canonical action (linear-response origin exhibited), AND eps_4 ~ 0.00268
   computed from the tether closes 1/alpha to <ppm. alpha is DERIVED:
   1/alpha = 4 pi^3 D_E (1 - eps_4/15), every factor mechanical. The last
   constant falls. (Prior: uncertain -- but this is a real, blind, geometrically
   -grounded route, and the energy number is already committed.)
2. 4/pi DERIVED, RESIDUAL OPEN: D_J = (4/pi) D_E holds mechanically, so
   1/alpha = 4 pi^3 D_E at 179 ppm is a DERIVED near-prediction, but eps_4 does
   not close the last 179 ppm. Still a major result: alpha reduced to a derived
   4 pi^3 D_E with a sharply-located 179 ppm residual.
3. RECTIFICATION LEAD: a related linear-response factor (not exactly 4/pi)
   falls out; registered as a lead with its second prediction named.
4. FALSIFIED: D_J = D_E (no 4/pi -- the action ratio equals the energy ratio),
   or D_J is not a linear-response quantity. The 4/pi is a 179 ppm coincidence;
   LEAD-2 stays dead; the pi^4 framing stands. Clean, honest negative -- and
   valuable, because it closes the action-dressing route the review opened.

## Named for go-decision (NOT opened)
- If Y confirms, the full eps_4 angular-harmonic computation as its own
  refinement; the provenance of 4 pi^3 vs pi^4 as the geometric prefactor
  (which one the construction actually forces).

## What this is
The honest reopening of LEAD-2 in corrected form. The external review caught
two premature closures: locking pi^4 as the prefactor, and reading the solver's
ENERGY dressing as the quantity alpha couples to. Y tests whether the CANONICAL
ACTION (linear response) differs from the energy by exactly the 4/pi that makes
the already-committed solver number fit alpha to 179 ppm -- computed BLIND from
the existing solution, with a sharp linear-vs-quadratic physics gate that can
falsify it cleanly. The most promising alpha thread of the campaign, because
the number was computed before the target was proposed.

## Depends on
Commission W (the solver, D_E=1.1051029, w_dressing_phase1c.py), Commission V
(J=J0, the circulation the action ratio is taken of), Commission U (the
two-constraint closure, the rotating solution), Commission T (the pi^2 anchor,
the geometry), Commission R (the tether whose f_4 perturbation gives eps_4).
The external review (alpha_idea.txt) that caught the premature closure.
