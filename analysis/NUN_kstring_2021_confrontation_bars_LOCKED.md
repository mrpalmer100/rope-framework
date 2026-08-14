# COMMISSION NUN -- BARS, LOCKED BEFORE COMPUTING

*2026-08-13. Candidate claim FND-101. Author-directed T2 session: the
external clock named in STRATEGIC_TARGETS section D ("any continuum
SU(6) k-string determination, bands pre-registered, kill-ready") has a
candidate dataset, located this session by literature hunt.*

## The question

FND-055 registered the inverted demand: a modern continuum-limit
SU(6) k-string determination decides GRANT-N2's exclusion statistic
(the derived b_k = (k-1)/(N-1), i.e. antisymmetric-Casimir
sigma_k/sigma_1 = k(N-k)/(N-1)) against the sine law. Does the
Athenodorou-Teper 2021 determination (arXiv:2106.00364, JHEP 12
(2021) 082; 3+1d, Wilson action, N = 2..12, continuum-extrapolated
sigma_{k=2}/sigma_f) decide it?

## The dataset (fixed before computing)

The paper's own two global continuum fits, transcribed verbatim from
Section 3.4 before any comparison arithmetic was run:

- FIT-A (powers of 1/N): sigma_2/sigma_f = 2 - 1.28(19)/N - 4.78(90)/N^2,
  chi2/ndf ~ 0.5.
- FIT-B (powers of 1/N^2): sigma_2/sigma_f = 2 - 14.43(60)/N^2
  + 73.8(12.1)/N^4, chi2/ndf ~ 2.2.

Disclosure: the per-N continuum Table 14 values were not extracted
from the PDF this session; the confrontation runs at the level of the
paper's published global fits, which are the paper's own statement of
the continuum N-dependence. If Table 14 values are later obtained,
a point-level re-read is permitted but the fit-level verdict below
may not be re-graded retroactively.

Paper caveats carried at full volume: N >= 8 volumes are small
(1.9(5) percent correction applied by the authors); the large-N
crossover to the weakly-interacting-pair regime (their eqn 9) is an
acknowledged ambiguity at the largest N; SU(6) sits in the safe
volume group (l sqrt(sigma) ~ 3.1).

## The pre-registered bands (from AYIN, fixed 2026-08-11, before this
## data was ever read by the corpus)

SU(6) k=2: Casimir sigma_2/sigma_1 = 1.6000; sine = 1.7321.
Prior registered record: +8.3 percent above Casimir (on sine), ~2
percent errors, non-continuum.

## Decision statistics (locked)

S1 (LEADING-POWER TEST, primary): the sine law 2 cos(pi/N) has ZERO
1/N coefficient (expansion 2 - pi^2/N^2 - ...). The derived exclusion
statistic has leading coefficient -2/N. VERDICT RULE: if the paper
prefers FIT-A (nonzero 1/N) over FIT-B at chi2/ndf ratio > 2, the
functional form resolves AGAINST sine-class (pure 1/N^2) structure
and toward the exclusion-statistic class. This is a class statement,
not a coefficient match.

S2 (COEFFICIENT TEST): compare FIT-A's 1/N coefficient 1.28(19) to
the derived 2 (exact, no free parameter). Report the discrepancy in
sigma. VERDICT RULE: <2 sigma = consistent; 2-3 sigma = tension;
>3 sigma = the exact derived law MISSES at the coefficient level and
this is registered as a miss, not absorbed.

S3 (SU(6) POINT READ, display only): evaluate both fits at N=6 with
propagated (uncorrelated-approximation) errors and place against the
1.600 / 1.732 bands. Display only: correlations between fit
coefficients are unavailable, so no sigma verdict is taken from S3.

## Pre-committed verdict grammar

- S1 sine-class rejected AND S2 <= 2 sigma: GRANT-N2's statistic
  VINDICATED outright.
- S1 sine-class rejected AND S2 > 3 sigma: SPLIT VERDICT -- the law's
  CLASS (1/N binding, vanishing at large N) is confirmed against
  sine, the EXACT coefficient is convicted; register as
  partial-confirmation-with-registered-miss. The old sine-favoring
  record (+8.3 percent, non-continuum) is SUPERSEDED either way.
- S1 prefers sine-class: GRANT-N2's exclusion statistic FALSIFIED per
  FND-055's own clause; register Failed-and-kept.
- No post-hoc refits of the derived coefficient; no softening rescue
  (FND-040's correction is negative and may only be disclosed, it
  pushes away from data).

## House

Bars locked before any comparison arithmetic. Em dashes forbidden.
Stale tripwires honored: no n_b window quoted; photon sector not
quoted as unresolved.
