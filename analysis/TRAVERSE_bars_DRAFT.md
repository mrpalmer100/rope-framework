# COMMISSION TRAVERSE -- THE STEEPENED-REGIME TRAVERSAL -- BARS (DRAFT)

*Drafted 2026-08-18, NOT YET LOCKED. Chartered at FND-142 as the named
one job: a general-position representation to follow the aligned
two-frequency branch past the min z' -> 0 steepening and decide whether
it reaches the registered amplitude R2 = 0.09396. Sigma_wave's
re-pricing waits on this and on nothing else. Nothing is computed until
the author locks.*

## THE DIAGNOSIS (the reason for a new instrument, on the face)

FND-142's failure is NOT that the target is unrepresentable -- the
registered nested geometry has pointwise min z' ~ 0.08 > 0 and IS a
z-graph. The failure is in the CLOSURE, in two places:

1. The pointwise constraint row |w_s|^2 + z'^2 - 1 = 0 has
   d/dz' = 2 z'. As z' -> 0 that row stops determining z' at first
   order and the multiplier field T loses its determining direction:
   the Jacobian degrades toward rank deficiency along exactly the
   coordinate the branch is driving to zero. The observed near-vertical
   tangents in BOTH gamma(A2) and the gamma-parametrized path are the
   signature of a conditioning collapse in the representation, not
   necessarily of a physical fold.
2. Both continuation parameters tried (the A2 pin, then gamma) are
   COORDINATES on the branch. A branch that turns in both cannot be
   followed by pinning either; the general-position path parameter is
   pseudo-arclength.

## THE FORMULATION (the one change, and its cost)

THE EQUATIONS ARE UNCHANGED -- the same adjudicated force law, same
rotating frame q(s, phi), phi = Omega_2 t, mu = 1, same pins. THE ONE
CHANGE is the representation: put the tangent on the sphere and let
the constraint hold identically.

    w_s = sin(theta) e^{i psi},    z_s = cos(theta)
    unknown fields: theta(s, phi), psi(s, phi), T(s, phi)
    unknown scalars: Omega_1, Omega_2   [gamma becomes an OUTPUT,
                                         gamma = <cos theta>]

    transverse:  -Om1^2 w + 2i Om1 Om2 w_phi + Om2^2 w_phiphi = (T w_s)_s
    axial:       Om2^2 z_phiphi = (T z_s)_s
    constraint:  IDENTICALLY SATISFIED (|w_s|^2 + z_s^2 = 1 by
                 construction; the algebraic row and its 2 z' factor
                 are GONE, and with them the z' -> 0 degeneracy)

theta = pi/2 (i.e. z' = 0) is an ORDINARY point of this chart, and
z' < 0 is now REPRESENTABLE -- if the branch leaves the graph class,
this instrument can see it and the old one could not.

THE COST, stated: w is recovered by s-integration of w_s (Fourier: the
nonzero s-modes divide by i k_n), so periodicity becomes EXPLICIT
closure conditions rather than a property of the unknowns --
<sin(theta) e^{i psi}>_s = 0 per phi (transverse closure) and
<cos(theta)>_s constant in phi (axial closure, its value = gamma). The
s-mean W0(phi) is a genuine unknown, fixed by the s-mean of the
transverse equation (whose right side vanishes by periodicity):
-Om1^2 W0 + 2i Om1 Om2 W0' + Om2^2 W0'' = 0 with periodic BC -- the
generic solution is W0 = 0, and the exceptional case is a resonance
whose condition is PRINTED as a control, not assumed away.

Level-1 in the new variables (the recovery control, closed form):
theta = arccos(1/sqrt(3)) = 0.955317 CONSTANT -- exactly pi/2 minus the
registered magic angle arcsin(1/sqrt(3)) -- with psi = k1 s + pi/2,
T = 3/2, Om1 = 4.44288. That theta is constant on the level-1 member is
a face fact of this chart and makes the control sharp.

## PATH: PSEUDO-ARCLENGTH (the second half of the fix)

Continuation by pseudo-arclength in the full unknown vector: the step
condition is a declared inner product against the previous tangent, so
folds in A2 AND in gamma are both traversable and neither is a
continuation coordinate. Predictor: tangent from the previous solve.
Step control: halve on non-convergence, floor declared at 1e-4 in the
path parameter; the floor being hit is a REPORTED outcome, not a
failure to hide.

## SEEDS AND PINS

SEED: the last converged FND-142 member (A2 = 0.0108), converted into
the new representation by theta = arccos(z'), psi = arg(w_s). Pins are
the STAGE-2 PINS UNCHANGED, evaluated on the reconstructed w so that
every registered quantity is comparable claim to claim: Re c_{n1,0} =
R1, Im c_{n1,0} = 0 (gauge), |c_{n2,m2}| = A2 where pinned,
Im c_{n2,m2} = 0 (gauge), <T> = 3/2 (the T_fibre tripwire quantity, a
pin not an output), <zeta> = 0. Cell and rationalization inherited:
Lcell = 2 sqrt(3), q = 3/2 -- INSTRUMENT CHOICE, on the face, and named
in FND-142's competing job as itself suspect. Base grid 64 x 24 to
match stage 2; aligned sector (m2 = -1) only -- the anti-aligned root
is resonance-locked and belongs to the OTHER commission.

## CONTROLS (printed; halt semantics as marked)

(0) REPRESENTATION EQUIVALENCE -- the instrument-unchanged proof.
    Re-solve TWO registered FND-142 members (the A2 = 0.0108 endpoint
    and one mid-branch converged point) in the new representation and
    reproduce Omega_2, gamma and A2 to 1e-6 relative. HALT. Without
    this control nothing else in the run is reportable.
(i) LEVEL-1 RECOVERY: continued to the A2 -> 0 limit, theta must be
    constant at 0.955317 (max deviation 1e-6), Om1 = 4.44288 (rel
    1e-3), T uniform 3/2 (max dev 1e-3). HALT.
(ii) DISCRETE RESIDUAL: full nonlinear residual RMS < 1e-8 at every
    ACCEPTED point, reported UNWEIGHTED (path weighting, if used, is
    path only -- the stage-2 discipline carried forward). HALT at the
    final registered point.
(iii) CHART VALIDITY (the new one): min sin(theta) > 0.05 -- the
    tangent-sphere's own singularity is at the POLES (theta -> 0, pi:
    a purely axial tangent, psi undefined), NOT at theta = pi/2. HALT
    if approached; a chart traded for another chart's singularity is
    not a general-position representation and the run says so.
(iv) HARMONIC-TAIL CONVERGENCE: at the registered R2 (if reached),
    re-solve at 96 x 36 from the FFT-interpolated solution; Omega_2 and
    Sigma move < 0.5%. HALT -> the value registers DISPLAY ONLY with
    the drift on the face.
(v) CLOSURE RESIDUALS: transverse and axial closure printed at every
    accepted point (they are equations here, not identities).
(vi) W0 RESONANCE CONDITION: the zero-mode ODE's resonance condition
    evaluated and PRINTED at every accepted point; W0 = 0 is asserted
    only where the condition says it may be.
(vii) SPARSITY PATTERN: the stage-2 permanent pattern control, re-run
    on the new stencil. HALT. (Stage 2 earned this one the hard way.)
(viii) INEXTENSIBILITY: identically zero BY CONSTRUCTION -- printed as
    such, and explicitly NOT counted as a measurement. Stage 2's exact
    satisfaction was a result; here it is a tautology and must not be
    re-registered as evidence.
(ix) Z-GRAPH DEPARTURE: min z' printed at every accepted point, sign
    included. A traversal that carries z' through zero is a FINDING to
    register, not an error.

## CLEAN ROOM

The registered Sigma_wave box [3.222, 4.313], the level-1-exact 2.598,
FND-139's refit corners, and FND-142's price DISPLAY 2.62 appear ONLY
in the final comparison leg, after the traversal has terminated by one
of the outcomes below. Verdict prose written AFTER the run. Bars not
edited after lock.

## PRE-REGISTERED OUTCOME SHEET

- BRANCH REACHES R2, controls pass: TRUE-STATE-SOLVED-AT-PINS.
  Sigma_wave re-prices from the solution's kb = 0 corner; the FND-139
  rider DISCHARGES; FND-142's PIN-UNREACHED is SUPERSEDED-NOT-ERASED
  (it was correct for its declared search, and the steepening
  measurement stands as the reason a new instrument was needed).
- FOLD REGISTERED BEFORE R2: the branch turns in pseudo-arclength and
  the maximum attainable A2 is measured. Then the obstruction is the
  FAMILY, not the path, and the registered R2 is unreachable on this
  branch -- a structural finding that puts the question back on the
  PINS (and on q = 3/2). Sigma_wave does not re-price; the rider
  stands; the desk gets a sharper choice than it has now.
- CHART OR TAIL HALT: Failed-and-kept, with the halting control named
  and the last accepted member registered.
- REACHES R2 WITH z' < 0 PATCHES: registered as a finding in its own
  right -- the composite at the registered amplitude is not a z-graph,
  which RETRO-EXPLAINS stage 2 completely; pricing proceeds normally
  (Sigma is chart-independent).
- CONTROL (0) FAILS: the instrument is wrong. Nothing else from the
  run is reported, and the failure itself is the registered content.

## COST NOTE (not a bar)

Stage 2 was a ~20 min single run; this build is a new instrument on a
comparable grid with a heavier reconstruction step, and the full
benchmark suite is running concurrently. A first end-to-end pass should
be budgeted well above stage 2's, and control (0) is cheap and comes
first precisely so a wrong instrument is caught before the expensive
traversal.
