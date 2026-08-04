# FND-STRAND-019 — the N-generality session: bars locked first

Date: 2026-08-03. Commission: FND-STRAND-018's fork. Question: is the
falling hazard size-free (an intensive finite-bath transient every
detector inherits) or does it fade with N (a genuine smallness effect with
an onset scale)? This decides whether Prediction 11's non-Poisson
statement carries a size condition.

## Data, committed

Operating point everywhere: h = 0.55, T = 0.40, c0 = 0.35, K = 16,
dt = 0.02. R(N) := lambda[q50,q90] / lambda[q25,q50] per size
(STRAND-013 estimator; quantiles per-size).
- N = 24: the pooled censor-free archive, n = 512 (014 + 015 + 016).
- N = 96: the pooled censor-free archive, n = 128 (011 + 012).
- N = 48: FRESH, n = 128 (generators 141-144, 32 each), window 24000.
- N = 192: FRESH, n = 128 (generators 151-154, 32 each), window 8000.
Censoring clause: a censored run invalidates its point; a slope bar needs
all four points or NO-VERDICT with the partial table reported.
Uncertainty: per-point bootstrap 95% CI on R (1000 resamples, RNG seed
2027), reported alongside every value.

## Pricing, honest

SE of ln R at n = 128 is roughly 0.2, giving slope SE ~ 0.14 over the
ln N span of 2.08. The FLAT and RISING thresholds below are separated by
~1.5-2 of that SE: adequate for a factor-level fork, NOT for a precision
exponent — and the verdict language is committed accordingly (this
session decides the FORK, not the decimal).

## The grammar

Fit s_R := slope of ln R(N) vs ln N over the four points.
- N-GENERAL (size-free): |s_R| <= 0.15 AND every R(N) <= 0.7. The
  transient is intensive; PROMOTE: every finite detector inherits a
  bounded non-Poisson transient set by the bath's own mixing epoch, with
  NO size condition on Prediction 11's statement.
- SIZE-EFFECT: s_R >= 0.25 (R rising toward 1 with N). The deviation
  fades with size; the onset-scale fit becomes the named next-order;
  Prediction 11's statement acquires a size condition. Registered at full
  volume.
- PARTIAL: any single R(N) > 0.7 (the hazard does not fall at that size)
  — generality fails pointwise regardless of slope; as measured.
- INTERMEDIATE: 0.15 < s_R < 0.25 or s_R < -0.15 — as measured; the
  bootstrap CIs carry the discussion; no promotion.

## Honesty clauses

- The exploratory R(96) = 0.479 from STRAND-018 seeded this design and is
  SUPERSEDED by tonight's committed recomputation on the same archive
  under these bars; it grants no head start to any verdict.
- Windows differ by size (as archived/priced); R over interior quantiles
  is window-safe given censor-free samples, and censor-freedom is the
  clause above.
- Chunked exact-state checkpointing pre-authorized.
- Status ceiling: Modeled. Absolute scale untouched (FND-MATTER-003).
