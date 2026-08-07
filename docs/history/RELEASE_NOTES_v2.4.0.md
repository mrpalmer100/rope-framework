# v2.4.0 — The cinched link

Corpus state: **271 registered claims (102 Derived, 138 Modeled, 4 EFT-constrained, 3 Conjecture,
5 Open, 19 Failed-and-kept); 257 benchmark-backed claims, all passing; 60 papers.**

Three claims that complete the stationarity arc the electron campaign opened eight sessions ago
-- and end it holding the framework's first complete electron-candidate geometry. A minor
version, because something finished: the question "is the localized linked object stable?"
was decomposed, instrumented, and driven to a terminated, certified answer-shape, with exactly
one number left open and the tool to attack it named.

## ELEC-011 — the exact adjoint and the wall-supported state
The instrument: a calibrated-adjoint first attempt REJECTED at its held-out gate (on the
record); the true discrete adjoint -- lambda = -4 pi kappa L3^{-1}(dFE/dpsi) with the exact
gradient-stencil transpose, chained through the sample-point Jacobian -- validated to
0.001-0.02 percent against converged finite differences, at ~100x lower cost. The apparent
disagreements at FD step 2e-4 converged ONTO the analytic values as the step shrank: the FD
was lying, and THE OBJECTIVE IS PIECEWISE-SMOOTH at exactly the step prior campaigns used --
retroactively explaining four sessions of optimizer misery. The discovery: the state is
WALL-SUPPORTED -- cos(grad, grad d_min) = +0.52 with stable multiplier mu ~ 0.166. Half of
four campaigns' "non-stationarity" was a constraint at equilibrium, bearing load. The
wall-tangent push: 40 certified steps, E 16.153 -> 16.104, with the tangential residual
oscillating at ~0.29 -- and its cause identified: grad(d_min) is itself kinky.

## ELEC-012 — the smoothed push breaks the stalemate
The softmin-smoothed constraint model (certification unchanged and hard) uncreased the
tangent, and the optimizer found the real valley: 108 certified steps, E 16.104 -> 14.921 --
roughly ten times the descent of all prior campaigns combined -- with d_min sliding down and
PINNING at the hard core (0.0600), |Lk| = 1.0003, and energy still descending at exhaustion.
The residual ROSE, and that was the finding: the ELEC-011 state was a shoulder. Near-contact
pairs grew 22 -> 408: the curves wrapping into extended contact, a link cinching.

## ELEC-013 — the run to termination
The generalized-KKT test (implemented as commissioned) exposed the softmin normal's limit
(residual 0.73 with feasible descent it could not represent); the ACTIVE-SET NNLS engine --
gradient decomposed over all active pair-constraint gradients with nonnegative multipliers --
ran 103 certified iterations to the pre-locked termination criterion. THE TERMINAL STATE:
E = 14.9072; d = 0.0610, a hair off the core; |Lk| = 1.0004 with full 128/256/512
certification; the contact set saturated at 525 pairs; length flat at L = 4.5114. The
ropelength ratio L/r = 150 versus the ideal Hopf link's 8 pi ~ 25 CORRECTS v2.4.0's own
namesake extrapolation: the object does not globally tighten -- it cinches where it touches
and stays large where the field wins, an interior balance part contact-mechanical, part
electrostatic. The scale bowl holds AT the terminal shape. The generalized residual fell
0.73 -> ~0.38 and plateaued: kept open, with second-order contact-manifold steps the named
decider.

## What stands, said plainly
In analysis/ELEC013_state.npz sits the framework's first complete electron-candidate
geometry: certified, linked, localized, scale-stationary, contact-saturated, and dynamically
terminated under a pre-locked criterion. It is NOT yet a proven constrained minimum -- the
first-order residual plateau (~0.38) is stated on the claim, unvarnished, and Modeled-not-
Derived is the honest label until second-order machinery closes it. No physical-electron
identification is made: mass, charge, and spin remain unbuilt bridges, and the rope-derived
Psi remains the mountain. But the question that stood at "is it stable?" for five releases
now stands at "is the cinched, field-held Hopf link the constrained minimum?" -- one
instrument from decidable, with its geometry in hand and its size and self-energy now
computable numbers awaiting calibration.
