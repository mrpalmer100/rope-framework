# COMMISSION SHIN2 -- THE HELICAL-SUBSTRUCTURE ACCEPTANCE TEST: RESULTS

Executed 2026-08-12 under analysis/SHIN2_helical_substructure_bars_LOCKED.md.
Benchmark: benchmarks/foundations/shin2_helical_substructure.py.

## Verdict: ALL FOUR BARS PASS -- GRANT-CANDIDATE-SUBSTRUCTURE to the desk

A1 REDISTRIBUTION INVARIANCE: exact. c^2 = T/mu, Sigma, and both
Lorentz margins (6.1x, 10.5x) invariant to 1e-12 under the
redistribution map at both live readings. The registered length-tuning
destruction (Sigma x 3e14-1.5e15) does not fire because it priced the
wrong map: it held T0 fixed; redistribution divides it.

A2 THE CEILING: a_f = 1.409e-22 m at n_sub = 4.57e9 (kappa250) /
1.34e10 (kappa50); E_max = 1.400 PeV at both readings, meeting the
LHAASO demand exactly at the priced counts.

A3 DIRECTION COVERAGE (the decisive test, exact spherical geometry
after the Monte Carlo estimator was replaced -- it undercounted
continuous tangent bands at theta = 2.7e-5; estimator change,
locked bars untouched):
- W0 control: 1.09e-9, reproducing FND-059's ~1e-9. Instrument valid.
- W1 single-level helices: best 1.6e-4 -- five orders above straight,
  five orders below the bar. SINGLE-LEVEL WINDING FAILS, kept.
- W2 two-level winding: the tangent image is an annulus per family,
  [|A1-A2|, A1+A2] in polar angle with A_i = arccos(sin psi_i);
  near-transverse pairs compose to FULL-SKY coverage -- best member
  (psi1 = psi2 = 5 deg) covers 1.0000, and the >= 10 percent bar is
  passed with orders to spare. HIERARCHICAL WINDING IS REQUIRED AND
  SUFFICIENT for the direction axis, at coverage-geometry level.

A4b THE GUIDED-PATH TENSION, displayed as locked: the A3-passing
geometry has guided axial speed sin(psi1)sin(psi2) = 0.008c. The
candidate therefore REQUIRES the coarse light mode to be the
collective medium branch (EM-RECON-025's registered assignment),
never a guided single-carrier mode. Named escape, on the face,
unresolved by this commission.

## Honest scope

Coverage geometry is NECESSARY, not sufficient: this commission shows
the direction obstruction (the slab) dissolves under hierarchical
winding, not that the wound medium's actual dispersion delivers
isotropic Lorentz-invariant propagation at PeV. The owed successor is
the wound-carrier dispersion computation with FND-REL-002 as the
acceptance test. n_sub, both pitch angles, and the hierarchy depth
remain UNDERIVED parameters on the price sheet.
