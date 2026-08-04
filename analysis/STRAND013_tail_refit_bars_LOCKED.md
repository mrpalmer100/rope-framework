# FND-STRAND-013 — the tail-robust refit: bars locked before computation

Date: 2026-08-03. Commission: STRAND-012's first-priority next-order. NO new
trajectories: every number below is computed from the three archived
datasets (STRAND010_promotion_data.json, STRAND011_N_sweep_data.json,
STRAND012_four_point_data.json). The refit hazard for a session like this is
estimator shopping, so the estimators are fixed here to the letter and no
alternative estimator may be reported alongside them.

## The estimators, exact definitions

RATE (primary): for a sample of n escape times, sort ascending t_(1)..t_(n);
empirical survival S(t_(i)) = 1 - i/(n+1). Fit ordinary least squares of
ln S vs t over the points with q25 <= t_(i) <= q90 (sample quantiles,
linear interpolation). lambda := -slope; tau_rate := 1/lambda. The [q25,q90]
window excises both the early transient (deterministic growth delay) and
the extreme tail (the region that wrecked the mean); its choice is committed
here, not tuned.

SHAPE DIAGNOSTIC: r^2 of that ln S fit (reported per point; a bar rides on
it only in B1). MEDIAN SCALE (secondary diagnostic only, no bars):
tau_med := median / ln 2, biased upward by any escape delay, reported for
cross-checks and never substituted where a bar names tau_rate.

## B1 — shape: is the escape exponential beyond the transient?

For every archived point (STRAND-010's four T at N = 48; STRAND-012's four
N; STRAND-011's N = 24 and 96): report the ln S fit r^2 over [q25, q90].
- PASS per point: r^2 >= 0.95 — the inter-quantile hazard is constant; the
  process is exponential-with-delay and tau_rate is its honest scale.
- FAIL per point: r^2 < 0.95 — hazard non-constant even mid-distribution;
  that point's tau_rate is reported with a shape flag and any downstream
  bar consuming it inherits the flag.

## B2 — does the STRAND-010 promotion survive the robust estimator?

Refit the Arrhenius line on STRAND-010's archived four-T dataset using
tau_rate per point: DeltaE_rob (slope) and nu_rob := exp(-intercept).
- CONFIRMED-ROBUST: r^2 >= 0.97 AND nu_rob in [1/3, 3]. The promoted
  identification is estimator-independent; annotate 010 accordingly.
- ESTIMATOR-DEPENDENT: either limb fails -> the promotion acquires an
  estimator flag on its face (registered at full volume; the mean-based and
  rate-based readings both stated). No softening of either.

## B3 — the STRAND-012 structure under the robust estimator

Recompute the four-point channel slopes (t_first and t_mean; t_conv is a
per-run difference of times, not a waiting process, so its robust treatment
is tau_rate applied to the per-run t_conv sample — same estimator, stated).
- CROSSOVER ROBUST: nucleation-channel pairwise slopes retain the 012
  signature (both small-N legs <= -1.15 AND the 96->192 leg >= -1.0) ->
  the crossover is registered ESTIMATOR-INDEPENDENT.
- CROSSOVER FRAGILE: signature not retained -> registered as found; the
  crossover reverts to single-session status pending the {192, 384} pair.
- N = 24 FRAGILITY ADJUDICATION: compute tau_rate separately on each
  32-seed batch at N = 24 (012's two batches; 011's two batches). Bar: all
  batch-pair ratios <= 1.35 -> the factor-2 swings were MEAN-SPECIFIC
  (tail-driven), the estimator lesson closes, and 011/012's N = 24 robust
  scales become quotable. Any ratio > 1.35 -> RATE HETEROGENEITY is
  physical (seed-level), registered as a finding, and the smallest box gets
  a named next-order (per-seed hazard census).

## B4 — STRAND-011's exponent, revisited (reported, not asserted)

The three-point robust slope on 011's archived boxes, stated for the
record next to the retired mean-based -1.661. No bar; 012's four-point
structure supersedes any single exponent regardless.

## Honesty clauses

- No new runs; no estimator beyond the two defined; the [q25, q90] window
  is fixed and appears in every fit identically.
- STRAND-012's mean-based registered numbers stand untouched; this session
  ADDS the robust reading, it does not overwrite.
- Status ceiling: Modeled.
