# FND-STRAND-014 — the per-seed hazard census at N = 24: bars locked first

Date: 2026-08-03. Commission: STRAND-013's first named next-order. The
question: at the smallest box, escape statistics disperse far beyond
estimator error. Two mechanisms are on the table and STRAND-013 stated
their confound in advance: HETEROGENEITY (the thermal initial condition
partitions into faster and slower classes — the waiting process is a
mixture) versus AGING (one shared, genuinely time-dependent hazard). This
session is designed to separate them. Blind: all grammar below precedes any
new trajectory.

## A structural fact the census must respect

In this engine the CHANNEL initial conditions are identical across walkers
(phi = pphi = 0); all walker-to-walker variation enters through the WEAVE's
thermal draw (q, p). So "IC classes," if real, are weave-configuration
classes, and the covariates must be weave functionals. Also: prior "batch"
labels were generator labels over iid draws — two batches sample the SAME
IC distribution, so persistent batch differences can only reflect the
distribution's own dispersion (mixture-induced) or a generator-level
anomaly. B4 closes that loop explicitly.

## Design

Engine: FND-STRAND-008 composite verbatim; N = 24, h = 0.55, T = 0.40,
c0 = 0.35, K = 16, dt = 0.02, window 36000 units (the 012-priced N = 24
window). CENSUS SIZE S = 256 (8 batches of 32; generators seed0 = 81..88,
fixed now). Recorded per walker, aligned: t_mean, t_first, and three IC
covariates computed at t = 0 BEFORE any evolution:

- C1: total weave energy, E_w0 = sum over sites and modes of
  0.5 p^2 + 0.5 omega^2 q^2.
- C2: soft-mode weave energy, E_soft0 = the same sum restricted to the
  softest quartile of the K modes (the band-gap-adjacent quartile).
- C3: peak initial drive, F0 = max over sites n of |sum_k c_k q_{n,k}| —
  the largest random force the weave exerts on the chain at t = 0.

No other covariate may be examined. Censoring clause: censored walkers are
reported and excluded pairwise from rank statistics; > 2% censoring
invalidates the census.

## B1 — traceability: does the IC predict the fate?

Spearman rho between t_mean and each covariate over the census.
- TRACEABLE: any |rho| >= 0.30 (with n = 256 this is overwhelming
  significance) -> heterogeneity has a measurable handle; the LARGEST-|rho|
  covariate is B3's stratifier, committed now.
- NOT-TRACEABLE: all |rho| < 0.15 -> these covariates do not carry the
  dispersion; B3 is moot and says so.
- INTERMEDIATE: otherwise; B3 proceeds with the largest-|rho| covariate,
  verdicts capped at as-measured.

## B2 — the pooled hazard trend

From the pooled census survival curve: lambda_early over [q25, q50],
lambda_late over [q50, q90] (same estimator as STRAND-013, windows
committed here). R := lambda_late / lambda_early.
- DECREASING hazard: R <= 0.7 (the mixture-or-aging signature).
- CONSTANT: 0.7 < R < 1.3 (prior shape flags were small-sample; register).
- INCREASING: R >= 1.3 (registered as found).

## B3 — the separation (the session's point)

Stratify the census into terciles by the B1 stratifier. Within each
tercile compute R_t as in B2.
- HETEROGENEITY VERDICT: pooled R <= 0.7 AND the median within-tercile R
  in (0.7, 1.3): the falling pooled hazard is composition (fast classes
  exit first); within a class the process is memoryless. Promotable.
- AGING VERDICT: within-tercile R <= 0.7 in at least two terciles: the
  hazard falls even at fixed IC class — genuine memory in the escape
  process. Promotable.
- MIXED: both effects present (pooled R <= 0.7, terciles split): as
  measured, split quantified.
- Promotion requires B1 TRACEABLE for the heterogeneity verdict; the aging
  verdict is promotable under any B1 outcome (it does not need the
  covariate).

## B4 — batch-dispersion closure

Bootstrap (1000 resamples, size 32, from the pooled census; RNG seed 2026)
the distribution of per-batch tau_rate pair ratios. If the observed
STRAND-011/012 batch ratios (2.07, 2.54) fall inside the bootstrap 95%
band, the historical "batch swings" are FULLY EXPLAINED by the measured
distribution (no generator anomaly); outside -> generator-level anomaly
registered and audited.

## Honesty clauses

- Covariates, stratifier rule, windows, census size, seeds, bootstrap
  protocol: all fixed above. No post-hoc covariates, no alternative
  stratifications.
- t_first recorded for the archive and future deconvolution; no bar rides
  on it tonight.
- Status ceiling: Modeled. Absolute scale untouched (FND-MATTER-003).
