# COMMISSION: THE ORDERED-LIMIT D EXTRACTION (EXACT-D II)

Successor to COMMISSION_EXACT_D (outcome GRV-096, Failed and kept).
Charter written and bars locked before computation. Operator GO given
2026-08-09. Operator: Mark Palmer. Computational collaborator: Claude
(Anthropic).

## What GRV-096 taught, and what changes

GRV-096: the m-odd amplitude is protocol-dependent (12-57%) because m and
m^3 are near-collinear over a 7-point mass window at m = 0.3-1.0. The EH
regime is c q << m << 1; the old window violated the upper jaw and
undersampled. This protocol changes four things at once:

1. SCALING WINDOW: per grid size M, masses run m in [3 c q(M), 1.0] with
   q(M) = 2 pi / M and c = sqrt(kt0); the bottom descends with M -- the
   ordered joint limit, taken as a sequence.
2. DENSE SAMPLING: 15 log-spaced points in u = m^2 per M.
3. RICH BASIS: fit {1, u, u^2, u^3, u^(1/2), u^(3/2)} -- model the
   contamination instead of hoping it is absent. Condition number of the
   design matrix is a registered diagnostic.
4. SECOND EXTRACTOR: the third finite difference in u kills every
   polynomial term exactly; the residual is the sqrt(u) signal with local
   amplitude proportional to u^(-5/2). Amplitude and exponent are both
   extracted, independently of the global fit.

## Pre-committed bars

- B1 (integrity): absorption_test, absorption_verdict, and the GRV-096
  benchmark all PASS unmodified before any new computation. Hard gate.
- B2 (extractor agreement): |A_fit - A_FD3| / |A_fit| < 10% at M = 96,
  where A is the sqrt(u) amplitude (A = D_lat after per-volume and q^2
  normalization, identical to GRV-096's convention).
- B3 (window and basis universality): sub-window refits (lower 10 points,
  upper 10, middle 9) and basis variants (drop u^3; drop u^(3/2)) each
  move A_fit by < 10% at M = 96.
- B4 (M-convergence): A(64), A(96), A(128) monotone with
  |A(128) - A_extrap| / |A_extrap| < 5% under the 1/M-quadratic
  extrapolation.
- B5 (exponent): the FD3 local log-slope over the middle of the window is
  -2.5 +/- 0.3. A parameter-free structural prediction of the sqrt(u)
  hypothesis; failure means the extracted signal is not the m-odd term.

## Kill and honesty conditions

Each bar failure registers as a finding with its numbers. No bar widens,
no window or basis is added after first compute, every computed number
enters the record. If B2-B5 all pass, the resulting claim carries D_lat
with a stated uncertainty (the spread across B3 variants) at status
Modeled; propagation to a (GRV-095's substitution) and the cross-sector
check follow in the same claim only if the uncertainty supports a
narrowing of at least 3x, per the predecessor charter's B4 standard.

## Deliverables

benchmarks/gravity/exact_d_ordered.py (deterministic; CI-fast signature
test); a registered claim (proposed GRV-097); charter outcome addendum;
document propagation; release at the operator's preference.

## OUTCOME (registered 2026-08-09, GRV-097, Failed and kept)

B1 PASSED. B2 FAILED (20.8%): global-fit sqrt(u) coefficient 8.63e-5 vs
FD3 intercept 1.04e-4 at M=96. B3 FAILED (worst 104%, drop-u^1.5). B4
FAILED (A(64,96,128) = 1.081, 0.863, 0.746 x 1e-4; extrapolation
deviation 103%). B5 FAILED (log-slope -2.01 vs -2.5 +/- 0.3). THE
FINDING: the m-odd sector is two-term, A sqrt(u) + B u^(3/2), B =
4.83e-4, B/A = 5.6, verified by the machine-exact FD3 identity
dd3(u^1.5)/dd3(u^0.5) = -u (4e-14) and a linear FD3 profile (R^2 0.998
at M=96). No fitting protocol can deliver a bar-clean D at that ratio;
the named route is analytic derivation and SUBTRACTION of B. No bar was
widened; every number is in the record. Benchmark:
benchmarks/gravity/exact_d_ordered.py.
