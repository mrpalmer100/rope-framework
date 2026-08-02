# ELEC-052 — The ancillary-data computation: locked bars (before parsing any values)

## Commission
ELEC-051 adjudicated on a RECONSTRUCTED profile (prose parameters) and found a
28% one-sign tension, naming the definitive version: the same integrals on the
paper's actual lattice points. The data arrived (arXiv 2409.20168v1 source
tarball, uploaded 2026-07-31): anc/Ex_NP_d{0.7,0.9,1.0}fm_scaling_normfact.agr,
midplane nonperturbative field E_x^NP(x_t) [GeV^2] vs x_t [fm], multiple
lattice setups per distance, with errors; anc/width_from_integral.agr, the
paper's own integrated w values.

## Method, fixed before parsing
- Each Grace set = one lattice setup. Fold the signed cut to radius r = |x_t|
  (average both sides where present). Azimuthal symmetry as in the paper.
- Integrals by trapezoid over the FULL available r range of each set (no
  truncation choices allowed post hoc); one pre-registered sensitivity
  variant: clip E < 0 tail points to 0 (noise floor), reported alongside.
- Per set compute: w_E = sqrt(int r^3 E dr / int r E dr) and
  R_eq = sqrt(2 * int r^3 E^2 dr / int r E^2 dr).
- Errors: 200-draw Monte Carlo over the quoted point errors, per set.
- Aggregate: median across sets per distance; cross-distance spread quoted.

## Locked bars
B1 (instrument validation, now on the SAME data): the per-distance median w_E
   must agree with the paper's own width_from_integral value at that distance
   within 10%, else the parse is wrong and the adjudication is VOID.
B2 (THE ADJUDICATION): compare the aggregate R_eq to R_pred = 0.342 fm.
   SUPPORTS if within 15%; TENSION otherwise, with size and sign quoted.
   The ELEC-051 estimate (0.404 fm, +18%) is also confronted: does the real
   data confirm the reconstruction or overturn it?
B3 (propagation): restate n, T0, Sigma_eq at the data-derived R_eq.
B4 (honesty): 1D cut + azimuthal symmetry assumed (as in the paper); negative
   tail noise handled only by the two pre-registered variants; d-dependence
   reported, not averaged away if the spread exceeds the MC errors.

## AMENDMENT 1 (locked 2026-07-31, after B1 diagnosis, before recomputation)
The full-range rule FAILED B1 at d = 0.9 and 1.0 (parse validated at d = 0.7,
-0.7%): the r^3-weighted integrand amplifies far-tail points with SNR <~ 1
(diagnosed: mean |E|/dE = 0.7-2.2 beyond r = 1.2 fm). Those two full-range
verdicts are VOID as locked. Amended integration rule, fixed without reference
to any resulting R_eq: per set, truncate at the first radius where |E|/dE < 2
for two consecutive points (signal termination); if never, use full range.
B1 re-applies unchanged: all three distances must now match the paper's own
w within 10% or the adjudication is void. Both the void full-range numbers
and the amended numbers are reported.

## RESOLUTION (locked 2026-07-31, no further amendments permitted)
Amendment 1 ALSO failed B1 at d = 0.9/1.0 (overshoot: -13%, -37%): the paper's
w there is tail-dominated (their own stated uncertainties grow by two orders
with d) and no answer-blind cut reproduces it. NO THIRD RULE will be tried;
that would be bar-shopping. Standing resolution under the original B1: a
distance is verdict-bearing only where the instrument validates against the
paper's own integral. That is d = 0.7 fm ONLY, which passed under BOTH rules
(-0.7% full-range, -0.3% truncated) with R_eq stable to 0.001 fm across all
four handling variants. d = 0.9/1.0 are reported as exploratory bounds. The
E^2 weighting is tail-insensitive by construction, which is why R_eq is
stable where w_E is not.
