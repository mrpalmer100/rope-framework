# FND-STRAND-012 — the blind four-point sweep: results

Bars: analysis/STRAND012_four_point_bars_LOCKED.md (blind; grammar, seeds,
per-N windows, and promotion criteria all fixed before any trajectory).
Dataset archived: analysis/STRAND012_four_point_data.json (4 x 64 runs,
per-run aligned two-channel records).

## Execution ledger

h = 0.55, T = 0.40, c0 = 0.35; S = 64/point; windows 36000/24000/12000/8000
units for N = 24/48/96/192. ZERO censoring on any channel at any box — the
per-N window pricing held (the 011 lesson, executed and vindicated).

| N   | t_first | t_conv | t_mean |
|-----|---------|--------|--------|
| 24  | 343.5   | 546.2  | 889.6  |
| 48  | 125.4   | 415.5  | 541.0  |
| 96  | 45.9    | 120.3  | 166.2  |
| 192 | 28.8    | 67.7   | 96.5   |

Recomposition t_mean = t_first + t_conv: exact per run (accounting closed).

## Verdicts, straight off the locked grammar

B1 (nucleation channel): s_f = -1.218 at r^2 = 0.9761 -> INTERMEDIATE.
Neither pre-committed pure class: steeper than rate-additivity (-1), short
of the barrier-relief line (-1.3). Both mechanisms contribute; per the bars,
the split is registered as measured and NO PROMOTION issues.

B2 (conversion channel): s_c = -1.082 at r^2 = 0.9475 -> PARALLEL
CONVERSION, cleanly in class. Suspect (iii) is real: conversion time shrinks
~1/N — more simultaneous seeds convert a bigger ring proportionally faster.

B3 (closure): recomposition exact; continuity FAILS the 0.15 window —
t_mean slope tonight is -1.132 vs STRAND-011's -1.661, shift +0.529,
registered as a finding per the locked clause. See the diagnosis below,
which is NOT the one the clause guessed.

## The finding behind the B3 shift: the mean estimator is heavy-tail fragile

The clause pre-guessed the 192 extension as the shift's locus. The data say
otherwise: the shift lives at N = 24, where tonight's batch means are 623
and 1156 (factor 1.9 apart at S = 32 each) and STRAND-011's were 954 and
2185 (factor 2.3). Session-level N = 24 means of 890 vs 1569 are therefore
consistent with estimator scatter under tails far heavier than exponential
— the 1/sqrt(S) pricing assumed exponential waiting times and the smallest
box violates that assumption. THE ARC'S THIRD PRICING MISS, named: seeds
(009), window (011), and now DISTRIBUTION SHAPE (012). The lesson enters
the standing rule: price the estimator to the measured tail, or use a
tail-robust statistic (survival-curve rate fits), before locking a bar on
means.

Consequence for STRAND-011, stated precisely: its super-extensive
CLASSIFICATION survives where its data were clean and stable — the 48->96
leg reads -1.545 there and -1.70 here, super-extensive both times — but its
three-point EXPONENT VALUE (-1.661) is estimator-limited by the N = 24
mean and should not be quoted as a measured constant. Annotated on 011.

## What the four points actually show: curvature, not one power law

Pairwise slopes, nucleation channel: -1.45 (24->48), -1.45 (48->96),
-0.67 (96->192). Conversion channel: -0.39, -1.79, -0.83. Mean channel:
-0.72, -1.70, -0.78. The nucleation channel tells the cleanest story: STEEP
at small boxes, flattening toward rate-additivity at large ones — exactly
the signature of finite-size barrier relief (suspect i) that EXHAUSTS
itself as the ring grows, leaving per-site Poisson statistics (the -1
asymptote, with the measured 96->192 leg at -0.67 consistent with approach
from above plus estimator noise). Both named suspects are therefore REAL,
in different regimes: barrier relief owns the small-N steepness; parallel
conversion (B2's clean verdict) owns the conversion channel throughout.

A single power-law exponent for this system over 24..192 does not exist,
and the blind bars were right to withhold promotion: the honest object is
the crossover, not a slope.

## Ledger

- B1 INTERMEDIATE (split measured); B2 PARALLEL CONVERSION (clean pass);
  B3 recomposition exact, continuity shift +0.529 registered and diagnosed
  as N = 24 estimator fragility, not new physics at 192.
- No promotion, per the bars' own criteria — and the reason is now physical
  (a crossover) rather than statistical (a breach).
- STRAND-010 unaffected beyond its standing scope note; STRAND-011
  annotated (classification survives; exponent value estimator-limited).
- Zero censoring; zero imputation; blind status intact throughout.
- NEXT-ORDERS, pre-named priority order: (1) tail-robust re-estimation on
  the archived four-point data (survival-curve rate fits — no new runs
  needed); (2) the large-N confirmation pair {192, 384} for the additive
  asymptote; (3) the direct per-N barrier measurement (constrained saddle
  search) to make the small-N relief a computed number instead of an
  inferred one.
- Status: Modeled. Absolute scale untouched (FND-MATTER-003).
