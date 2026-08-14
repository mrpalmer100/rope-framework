# COMMISSION NUN -- RESULTS (FND-101, 2026-08-13)

*Bars: analysis/NUN_kstring_2021_confrontation_bars_LOCKED.md.
Benchmark: benchmarks/foundations/nun_kstring_2021_confrontation.py.*

## What fired

The external clock FND-055 armed on 2026-08-11 ("a modern
continuum-limit SU(6) k-string determination decides GRANT-N2's
exclusion statistic outright") has a dataset: Athenodorou-Teper,
JHEP 12 (2021) 082 (arXiv:2106.00364). 3+1d, Wilson action,
N = 2..12, sigma_{k=2}/sigma_f continuum-extrapolated per N, with the
N-dependence fitted globally. The measurement existed BEFORE the
derivation (2021 vs 2026-08-11) and was never read by the corpus; the
bands were pre-registered blind to it.

## The numbers (paper side, verbatim)

- FIT-A: sigma_2/sigma_f = 2 - 1.28(19)/N - 4.78(90)/N^2,
  chi2/ndf ~ 0.5 (paper's preferred fit).
- FIT-B: 2 - 14.43(60)/N^2 + 73.8(12.1)/N^4, chi2/ndf ~ 2.2
  ("cannot be entirely excluded", paper's words).
- N >= 8 volumes carry the authors' 1.9(5) percent correction; the
  large-N pair-regime crossover is their acknowledged residual
  ambiguity. SU(6) is in the safe volume group.

## S1: the leading-power test (primary) -- SINE-CLASS REJECTED

The sine law 2 cos(pi/N) has IDENTICALLY ZERO 1/N coefficient. The
derived exclusion statistic b_k = (k-1)/(N-1) has leading term -2/N.
The data prefers the nonzero-1/N fit at chi2/ndf 0.5 vs 2.2 (ratio
4.4, rule was > 2). The FUNCTIONAL CLASS the corpus derived -- binding
with a leading 1/N falloff, i.e. pairwise label-exchange structure --
is what the continuum data exhibits. Sine's pure-1/N^2 structure is
what it disfavors. Independent corroboration: the same group's 2+1d
companion (arXiv:1609.03873) reports leading 1/N and explicitly
pairwise binding.

## S2: the coefficient test -- THE EXACT LAW MISSES AT 3.8 SIGMA

Measured 1/N coefficient: 1.28(19). Derived: 2, exactly, no freedom.
Discrepancy 3.8 sigma, i.e. the measured binding is ~64 percent of
the derived strength. Per the locked rule this is a MISS, registered,
not absorbed. FND-040's softening disclosure is mandatory and cuts
the wrong way as always (negative, pushing below Casimir; the data
sits ABOVE Casimir).

## S3 (display only): SU(6)

Casimir 1.6000, sine 1.7321. FIT-A at N=6: 1.654 +/- 0.040 (uncorr.
approx). The continuum value sits BETWEEN the laws, ~+3.4 percent
above Casimir and ~-4.5 percent below sine. The old registered
record (+8.3 percent, on sine, non-continuum, ~2 percent errors) is
SUPERSEDED by this continuum determination.

## VERDICT (pre-committed grammar): SPLIT

- The CLASS is confirmed against sine: binding exists, falls as 1/N,
  vanishes at large N -- everything KAF's inverted demand asked for
  qualitatively, and the structure only GRANT-N2's label counting
  could express (FND-053).
- The EXACT coefficient is convicted: (k-1)/(N-1) predicts -2/N and
  the data says -1.28(19)/N. The exclusion statistic's normalization
  (two exchange orientations over N-1 partners, v = 2/(N-1)) is
  measured ~36 percent strong.
- Sine is NOT the escape: the corpus does not get to lose to sine
  here, because sine lost the class test outright.

## What this buys and owes

BUYS: the FND-055 demand is DISCHARGED -- the corpus no longer waits
on this clock. The sine-favoring record that has hung over the sector
since FND-047 is superseded. GRANT-N2's qualitative purchase (the 1/N
carrier) is CONFIRMED by continuum data.

OWES: the coefficient. Either (i) the exchange-orientation count is
wrong by a derivable factor (candidates must be named blind, not
fitted: e.g. orientation weighting, partial-overlap suppression), or
(ii) the ~0.64 ratio is a genuine dynamical correction the label
combinatorics cannot supply, in which case the statistic stands as
class-right/normalization-incomplete. Naming that mechanism is the
sector's next brick and any candidate must predict 1.28(19)/2 = 0.64
blind.

LIMITATION, on the face: this confrontation ran at the level of the
paper's global fits, not per-N Table 14 points (not extracted this
session); a point-level re-read is permitted per the locked bars and
is the cheap follow-up. The paper's own large-N caveats (small
volumes, pair-regime crossover) soften the coefficient conviction's
edges but cannot rescue exactness: SU(4..6), the safe-volume group,
drives the 1/N fit.
