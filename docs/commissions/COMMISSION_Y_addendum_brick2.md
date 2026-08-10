# COMMISSION Y ADDENDUM (BRICK 2): THE SPATIAL f4 CONSTRUCTION (2026-08-06)
# Follow-on named in COMMISSION_Y_results.md, opened on Mark's go-decision.
# Script: explorations/y2_spatial_f4.py. Blind order held: all eps_4 values
# printed before the comparison line and closure test.

## WHAT WAS BUILT
The reviewer's construction, implemented literally: 2D ansatz
f(r,theta) = f0(r) + a4(r) cos 4theta, with the exact rectified-load
harmonic m(theta) = -(2/15) cos 4theta modulating the elastic sector,
solved as a linear perturbation around the committed radial solution
(full quadratic form including the epp0 cross-stiffness, the M^2/r^2
angular stiffness, and the rotational sector; mesh-converged N=2000/3500
to 0.01%). eps_4 measured under three pre-registered weights (rotational,
plain norm, tether-load pairing) plus the m=8 harmonic audit.

## RESULT: THE SPATIAL FULL-ENERGY-MODULATION MODEL IS FALSIFIED
eps_4 = +0.0360 across all three weights (weights agree to 0.2%, so the
pairing freedom is NOT the issue here). That is 13.4x the reviewer's
required 0.00268 and drives the closure to -2220 ppm, overshooting the
target by an order of magnitude. The induced shape anisotropy is 4.5% of
the profile. Internal cross-check: an anisotropy that large would feed
back into D_E at second order at the ~0.1% level, which would have
violated W's committed 0.0000% spread. The model contradicts both the
target and the corpus's own committed number.

## WHY THIS IS PROGRESS, NOT A DEAD END
The falsification is of a specific source model: "the rectified harmonic
modulates the elastic ENERGY." That premise was already suspect after the
Y gate (the solution is purely quadratic-elastic; rectification is not a
property of its energy). Brick 2 confirms it quantitatively: if the
energy carried the rectified structure, the configuration would be far
more anisotropic than alpha permits. The audited model space now stands:
  (a) time-harmonic second-order back-reaction (Y, Part 3):
      -15 ppm (overlap pairing) / -450 ppm (energy pairing)
  (b) spatial energy-modulation (this brick): -2220 ppm -- FALSIFIED
  (c) no correction: +179 ppm
Route (a) is the only surviving realization, and it is also the one
consistent with the gate: the rectification lives in the COUPLING's time
structure, and its back-reaction on the profile is second order. The
chain's status sharpens to: 1/alpha = 4 pi^3 D_E (1 - Delta), Delta from
the 4-Omega response, currently -15 ppm, gated on the coupling derivation
that would (i) force 4 pi^3 over pi^4 and (ii) select the pairing.

## LADDER / REGISTRY
LEAD-2R updated: spatial-source branch closed (registered negative);
time-harmonic branch stands at -15 ppm. Named for go-decision, NOT
opened: the coupling derivation (the measurement-dictionary step that
makes the observable a rectified linear functional), which is now the
single remaining gate for the entire alpha chain.
