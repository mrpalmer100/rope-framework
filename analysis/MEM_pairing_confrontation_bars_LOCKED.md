# COMMISSION MEM -- NUC-024'S PAIRING vs THE TABLE: BARS (LOCKED BEFORE COMPUTING)

*Locked 2026-08-11, before any binned coefficient is evaluated. The
confrontation NUC-026 delivered the number for: the derived A-independent
parity cost against the out-of-sample pairing channel of the full table.*

## The two hypotheses, fixed with zero free parameters

- H1 (NUC-024 as registered): even-even vs odd-odd staggering
  S(A) = 6.11 MeV, A-INDEPENDENT (the fixed cross-sublattice cost of one
  misplaced label, NUC-021).
- H2 (empirical law): S(A) = 24 / sqrt(A) MeV (twice the SEMF 12/sqrt(A)).

Neither may be rescaled, shifted, or refit.

## Measurement (pre-committed)

Round-2 LAMED residual (registry-best baseline, unchanged). A-bins fixed:
[12,40), [40,80), [80,120), [120,160), [160,200), [200,260). Within each
bin, OLS of R on the locked descriptor set [1, D1, D2, D3, D4, D5, D6];
the measured staggering is S_hat = 2 x coef(D2) with 2 x SE. Sign
stability checked per bin on the seed-3141 train/test halves.

## Bars (pre-committed)

- MAGNITUDE: a hypothesis is consistent with a bin if it lies within
  2 sigma of that bin's S_hat. H1 CONFIRMED-IN-MAGNITUDE only if
  consistent in the lightest bin (its home regime, A <= 40 adjacent).
- SCALING: the A-trend of S_hat adjudicated by weighted least squares of
  S_hat on A^(-1/2) vs on a constant; the better chi^2 wins, and a
  falling trend at > 2 sigma REFUTES the A-independent form at table
  scale (upgrading the standing defect from noted to measured).
- Verdict grammar: CONFIRMED-BOTH / MAGNITUDE-ONLY (scaling refuted) /
  REFUTED (neither magnitude nor scaling) / INCONCLUSIVE (bins too noisy
  to separate the laws at 2 sigma). Full bin table reported either way.
