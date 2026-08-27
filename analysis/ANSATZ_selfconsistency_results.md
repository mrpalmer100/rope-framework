# COMMISSION ANSATZ -- RESULTS (2026-08-18)

Executed under analysis/ANSATZ_selfconsistency_bars_LOCKED.md.
Benchmark: benchmarks/foundations/ansatz_selfconsistency.py
(exit nonzero BY DESIGN: the bars' halt condition fired).

**VERDICT: HALTED-AT-CONTROL, DIFFERENT-OBJECTS-FOUND.** The session
never reached its chartered legs. Surface control (b2) -- the
arclength derivative of the composite tangent must reproduce the
registered composite curvature -- failed at ORDER ONE (max gap
1.506/a_f against a 1e-6 bar), while the companion controls that
validate the numerical operator passed at machine precision (level-1
limit 4e-16; tangent-in-span 2e-11). The failing object is not the
instrument. It is the registered curvature.

## 1. THE FINDING

The registered composite curvature K = k_1(a) + kappa_2(frame b) --
the object the bending machinery has carried since the substructure
sessions -- is a PER-LEVEL CURVATURE SUM. The Frenet curvature of the
actual nested curve is a different object. Empirical decomposition
(no hypothesis; the session's first guess, a pure frame-transport
story, was REFUTED by its own control and replaced):

    |(da/ds) d_a t - k_1|      up to 1.87 /a_f
    |(db/ds) d_b t - kappa_2|  up to 1.27 /a_f

BOTH pieces mismatch: the sum-form weights the level-1 curvature as
if the backbone advanced at unit rate per unit composite arc (it
advances at less), and assigns the level-2 term a straight-axis
winding rate the curved backbone does not have. Magnitudes over the
torus:

    |k| actual:      [0.295, 4.469] /a_f,  RMS 3.469
    |K| registered:  [0.213, 5.713] /a_f,  RMS 4.056
    <|k|^2> actual / registered = 0.732   (bending-energy weighting)

## 2. WHY THE COMMISSION CANNOT RUN AS CHARTERED

The self-consistency test compares the stated motion's acceleration
against the force the fibre supplies -- and the force side depends on
WHICH curvature the granted rod's bending responds to. That is now an
open adjudication, not an input. Running the test with either choice
would beg the question the control exposed.

A reading the adjudication must weigh, recorded here without being
adopted: FND-118's granted class carries no stress-free wound
reference (MAINT channel i was ruled inadmissible on exactly this),
which suggests the rod's bending references the TRUE curvature of the
actual shape -- in which case the sum-form instruments mispriced the
bending channel. The opposing reading (the per-level sum as the
constitutive object of a hierarchically wound medium) must be stated
by its defenders at the adjudication, not strawmanned here.

## 3. ON NOTICE, BY NAME (not superseded)

Every bending-channel number priced through K_registered:
- BLOCH-L's kb feasibility ceiling (the standing 0.079 bound) -- the
  bending energy entered through the sum-form k0. DIRECTION if the
  true curvature wins: <|k|^2> falls to 0.73x, bending spend per kb
  falls, the ceiling LOOSENS. Direction displayed, value owed.
- SHIN7's kappa_tot = kappa_1 + kappa_2 worst case -- LOCKED as an
  upper bound in its own bars, and the actual RMS is lower, so that
  leg was conservative in the safe direction; on notice for value.
- The energy bill's level-2 coefficient (tau_2^2 - kappa_2^2/2 =
  17.926) and the composite build's level-2 balance -- per-level
  objects of the same class; on notice.
- NOT implicated: every pure level-1 object (the neutrality theorem,
  the material-speed identity, Omega_1) -- a single helix's Frenet
  curvature IS its per-level curvature; the two objects coincide
  where there is no nesting. The DBC null-correction is also
  untouched (shift-invariance holds for whatever k0 the instrument
  carries).

## 4. CORRECTIONS OF THIS SESSION, RECORDED

The first diagnostic asserted "the gap IS the frame-transport term"
with a control that refuted it (3.68 vs a 1.51 gap) -- caught before
registration by the control's own number, replaced by the empirical
piecewise decomposition. Same-night second instance of FND-137's
lesson; the discipline held because the control was in the output.

## THE NAMED NEXT-ORDER

COMMISSION CURVE-OBJ: the curvature-object adjudication. Which object
does the granted rod's bending energy reference -- the Frenet
curvature of the actual nested curve, or the per-level sum? The
grant's own no-wound-reference clause is the first exhibit; the
bending-channel re-pricing (kb ceiling direction: looser) executes on
the verdict. The ansatz self-consistency test re-charters AFTER the
adjudication, with the force side unambiguous.
