# COMMISSION DBC -- RESULTS (2026-08-18)

Executed under analysis/DBC_background_correction_bars_LOCKED.md.
Benchmark: benchmarks/foundations/dbc_background_correction.py.
Instrument: the BLOCH-L build imported verbatim (no re-implementation).
Clean room held: no derive-point family value appears in any leg; the
solve was not rerun; kb entered symbolically and at its standing value
only in the delta-dependence check.

**VERDICT: NULL-CORRECTION.** The dynamical matrix of the perturbation
problem on the registered rotating-wave background is time-independent
at the production instrument (m = 6), to machine precision (spreads
1e-13-class against a 1e-6 bar), in both read directions, with the
bending channel on, and for arbitrary independent rotation rates at both
winding levels. The Floquet problem the rotating background poses
degenerates exactly to the static one; the BLOCH-L anchors carry ZERO
background-rotation correction at every order; the handoff's named gap
on the standing kb bound is DISCHARGED.

## 1. WHY THE CORRECTION IS EXACTLY ZERO (the mechanism, in three steps)

(i) MATERIAL FRAME: in material coordinates the perturbation kinetic
form is (mu/2)|d_t u|^2 with no convective and no Coriolis term; the
linear cross term cancels against the linear potential term by the
background's own equation of motion -- the centripetal balance MAINT
channel iii exhibited, kb-free at level 1 by the neutrality theorem and
kb-arbitrary at level 2. All background dependence sits in Q(t).

(ii) ROTATION = SHIFT: the rotating state at time t is the static
configuration with all level-1 phases advanced by delta = Omega t
(rigid rotation about the winding axis is an isometry carrying tangents
and curvature vectors; verified 2.7e-15). So Q(t) depends on t only
through a COMMON phase shift.

(iii) ALIAS-FREE AVERAGING: the instrument carries the phase ensemble
at every site; a common shift moves the sample points, and the m-point
average is exactly shift-invariant once the sampling out-resolves the
energy form's phase-harmonic content. At m = 6 (production) the spread
over delta is 1e-13-class: the shift-invariance is EXACT at the
instrument, not merely in the ensemble limit.

## 2. THE SWEEP (lambda = 24p, directions (001) and (111))

    m=1   spread c_L up to 2.0e+00      (single-orientation: wildly
                                         delta-dependent, as the
                                         rank-deficiency catch predicted)
    m=2   spread 1e-3 -- 1e-2 class
    m=4   spread 1e-13 class            (see sec. 3)
    m=6   spread 1e-13 class            NULL at the production instrument
    level-2 independent shifts (m=6):   1e-13 class
    bending on at the standing bound:   1e-13 class

## 3. DEVIATION FROM THE PRE-REGISTRATION, recorded not smoothed

The bars predicted delta-dependence at m = 1, 2, AND 4 (degree-<=4
harmonic counting: alias-free only for m >= 5). The instrument returned
NULL already at m = 4. The prediction was an UPPER BOUND on harmonic
content; the observed nullity at m = 4 means the harmonic-4 amplitude of
the site-averaged energy form, in the projections the two read branches
take, is zero. The prediction's direction of error is the safe one (the
production read at m = 6 is alias-free a fortiori), but the vanishing
itself is unexplained and is left OPEN as a small named question: which
symmetry of the nested two-level form kills the fourth harmonic?

## 4. WHAT MOVES, AND WHAT DOES NOT

MOVES (annotation only): the standing kb bound loses its
static-background conditionality. It now reads: kb <= 0.07909 T0_f a_f^2,
CONDITIONAL on the Kirchhoff-only bending treatment (pre-stress gap,
contact-gated, FND-126 sec. 5 -- UNTOUCHED by this session), and
UNCONDITIONAL with respect to the background's rotation state.
r_s <= 0.1874 and the FND-122 ceiling inherit the same annotation
upgrade and nothing else.

DOES NOT MOVE: every registered number. The anchors, the mapping, the
reverting set, both tripwires (FND-132 tension tripwire; FND-129 class-A
re-opener) all stand exactly as at the close of the prior release.

## REFUSALS

The solve was not rerun (a time-independent D implies it unchanged
exactly; rerunning would only have re-imported the target values into a
session that did not need them). No claim is made about the pre-stress
gap. The m = 4 surprise is registered as open, not explained after the
fact. Level-2 rotation RATE remains unregistered; the theorem was proved
rate-free precisely so the composite build owes nothing to this session.
