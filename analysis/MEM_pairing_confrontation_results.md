# COMMISSION MEM -- RESULTS: NUC-024'S A-INDEPENDENT PAIRING REFUTED AT TABLE SCALE

*Evaluated 2026-08-11 after bar lock
(analysis/MEM_pairing_confrontation_bars_LOCKED.md). Benchmark:
benchmarks/nuclear/mem_pairing_confrontation.py. Data: AME2012, round-2
LAMED residual, 2389 nuclides in six pre-committed A-bins.*

## The bin table (full disclosure)

| A-bin | n | S_hat +/- 2SE [MeV] | H1 = 6.11 | H2 = 24/sqrt(A) |
|---|---|---|---|---|
| [12,40) | 197 | +3.63 +/- 0.52 | NO | NO (4.68) |
| [40,80) | 344 | +2.54 +/- 0.40 | NO | NO (3.10) |
| [80,120) | 464 | +2.44 +/- 0.23 | NO | yes (2.40) |
| [120,160) | 493 | +2.24 +/- 0.22 | NO | yes (2.03) |
| [160,200) | 464 | +2.02 +/- 0.15 | NO | NO (1.79) |
| [200,260) | 427 | +1.97 +/- 0.33 | NO | NO (1.60) |

Sign-stable positive in every bin on the seed-3141 halves: the pairing
channel is real everywhere. Zero-parameter chi-squared over six bins:
H1 (A-independent 6.11) = 6326; H2 (24/sqrt(A)) = 42. The falling trend
is +6.6 sigma on A^(-1/2) -- the 1/sqrt(A) shape is the table's shape.

## VERDICT: REFUTED (per the pre-committed grammar)

- MAGNITUDE: H1 fails even in its home regime -- the lightest bin measures
  3.63 +/- 0.26 (1SE) against 6.11, a ~9 sigma overshoot. Not
  CONFIRMED-IN-MAGNITUDE, so MAGNITUDE-ONLY is unavailable.
- SCALING: the A-independence is refuted at 6.6 sigma. The standing defect
  NUC-024 registered as a noted property of the model class (the third
  appearance of the linear-law signature) is upgraded to MEASURED, at
  table scale, out of sample.

H2 is not the winner so much as the survivor: chi2/dof ~ 7 means the pure
24/sqrt(A) also strains (slightly high at light A, low at heavy A through
this estimator), but it is 150x closer than the derived form and carries
the correct trend.

## Measurement-condition disclosure (on the face)

NUC-024's 6.11 came from the N = Z chain, A = 8-40, against its own
recalibrated baseline -- a different estimator with different exposure.
This confrontation measures the table-wide staggering controlling for the
locked descriptor set against the registry-best chain. The two estimators
disagree even in the overlap region (3.63 vs 6.11 at light A), so part of
the gap is estimator-sensitivity -- reported, and it does not rescue H1:
no reading of either estimator produces an A-independent trend.

## The inverted demand (constructive, registered)

The framework's parity cost is the fixed cross-sublattice price of one
misplaced label (NUC-021). The table says that price DILUTES as
1/sqrt(A). A rescue must derive the dilution: the unpaired label's cost
spread over a growing structure -- delocalization of the odd nucleon --
which is precisely the collective/quantum structure the sector's other
misses (asymmetry exponents, NUC-020) already demand. One mechanism,
three registered misses, one demand: derive the 1/sqrt(A) dilution of the
NUC-021 cost blind, and all three channels are confronted at once.
