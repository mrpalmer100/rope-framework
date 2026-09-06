# COMPOSITE-SELECT -- LEG A RESULTS (QA, the selection question) 2026-09-05
Charter analysis/COMPOSITE_SELECT_charter_LOCKED.md (gating amendment +
lock line). Logs analysis/composite_select/. R2 = 0.09396 loaded ONLY in
the consequence step at the end of this document.

## Controls (Leg 0, on existing states)
v6 MOMENT CONTROL: the level-1 seed gives E[t_z^2] = 1/3 to 2e-16 on
   4/3, 5/3, 5/4 (after a first extraction used the wrong field --
   0.868 -- and was corrected: t_z = zp, |t|^2 = 1 to 1e-10).
v5 ENERGY CONTROL: the stage-2 price() transplanted to the QTGrid state
   round-trips a packed stage-2 state to 2.2e-5 relative (bar 1e-4).
   AMENDMENT: the 2.62 T0 anchor at A2 = 0.0108 on the q = 3/2 member
   is NOT reproducible -- the 3/2 states predate this release's exports
   (as FINE-GATE and BRICK2 found); the formula, not the number, is
   the control. Recorded.
v1/v3/v4/v7: existing states; the sparse instrument's reproduction and
   closure grades stand from Q54/GR54; clean room held (R2 absent from
   the Leg A scripts).

## QA -- the three principles on every gated member (4/3, 5/3, 5/4;
## 14 members each, A2 0.0019 - 0.0052; torus average = time average)

S-a ISOTROPY ON THE WAVE -> ** SEL-NONE ** (with an extrapolated crossing
    far outside): the fourth-moment deviator D4 = E[t_z^4] - 1/5 sits at
    -0.0889 (= 1/9 - 1/5, the level-1 helix alone) and moves by only
    0.0002-0.0006 across each family (slopes +0.04 to +0.18 per unit
    A2, cell-dependent). No crossing on the family; the linear
    extrapolation to D4 = 0 lands at A2* ~ 0.5-2.3 (display), two
    orders beyond A2_max. The principle that produced the static R2
    does not select any amplitude the wave family approaches: the
    static helix-on-helix reached its fourth-moment isotropy with an
    angular content the rotating wave state does not have.

S-b ENERGY -> ** SEL-NONE **: Sigma_wave(A2) rises MONOTONICALLY on
    every family, from 2.5981-2.5992 T0 at A2 = 0.0019 to 2.6055-2.6089
    at A2_max (dSigma/dA2 +1.9 to +11.4, never zero). No stationary
    point. Note for QC: the price is level-1-dominated -- the level-2
    contribution at reachable amplitudes is +0.3 pct -- and starts at
    the level-1-exact 2.598.

S-c LORENTZ SATURATION AT LEVEL 2 -> ** SEL-OUTSIDE **: the level-2
    pattern-rotation speed v_2 = RMS|om2 dW/dphi| runs 0.013-0.066 c on
    the gated states; extrapolated linearly to v_2 = c it selects
    A2* = 0.089 (4/3), 0.076 (5/3), 0.094 (5/4) -- an order of
    magnitude beyond every A2_max (0.0050-0.0052), and cell-dependent
    at the 20 pct level (0.076 vs 0.094: 21 pct; D1's cell-dependence
    rule applies at the margin). Also recorded: max|v_total| on the
    gated states already EXCEEDS c -- 1.002 at A2 = 0.0019 rising to
    1.026-1.028 at A2_max -- because level 1 sits at exactly c
    (FND-132) and level 2 adds to it. The composite state is
    superluminal in its material speed by up to 2.8 pct at the
    reachable amplitudes; the family's fold is where that excess is
    growing fastest. Reported, not adjudicated (S-c's locked statistic
    is v_2 alone).

JOINT (QA): no principle returns SEL-INSIDE; one selecting principle
    (S-c) returns SEL-OUTSIDE; two return SEL-NONE. Under the locked
    rules this is ** COMP-PIN-UNREACHABLE ** (every principle that
    selects returns SEL-OUTSIDE): the two-level rotating-wave state
    does not exist at its own selected amplitude under the registered
    protocol.

## Consequence step (R2 loaded once)
R2 = 0.09396 (static provenance, FND-125/126). S-c's A2* = 0.076-0.094
brackets it; the 5/4 value 0.094 coincides to 0.1 pct. Under the
resemblance rule this is REPORTED AS A NUMBER: the level-2 Lorentz
saturation on the dynamic state selects an amplitude of the static
R2's size, which is where the static hierarchy put it and where the
family cannot go. No identification is drafted from the coincidence
(the dependency path, if any, runs through KBSAT's forced-not-adopted
reading and is its own question).

## What COMP-PIN-UNREACHABLE means for the desk (Leg C prices it)
- Sigma_wave RETREATS to the level-1-exact 2.598 with a rider; on the
  reachable family the honest price is 2.598-2.609 T0 (S-b), against
  the ansatz bracket [3.222, 4.313] -- the bracket was the ansatz's,
  not the state's.
- Prediction 32's upper edge is re-priced to the level-1 value; the
  two-sided band collapses to its lower edge plus a rider.
- R2 stays registered as the static-provenance value; it is not the
  level-2 amplitude of any existing wave state.
- The superluminal excess is a new fact about the family that the
  charter did not anticipate; named for the author.

## Not yet run
Leg B (the rational ladder at two densities, 20-point budgets) -- a
local-execution item; its D4 order test is QB. Leg C's table follows
Leg B. No claim is drafted before the author reads.
