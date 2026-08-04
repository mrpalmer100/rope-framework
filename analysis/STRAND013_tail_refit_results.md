# FND-STRAND-013 — the tail-robust refit: results

Bars: analysis/STRAND013_tail_refit_bars_LOCKED.md (estimators fixed to the
letter before touching the archives; no new trajectories; no alternative
estimators reported). Inputs: the three archived datasets, untouched.

## B1 — shape: the escape process is NOT exponential-with-delay in general

The r^2 >= 0.95 constant-hazard bar over [q25, q90], per point:

PASS: S10 T=0.47 (0.963); S12 N=24 mean (0.971), N=48 first (0.951),
N=96 mean (0.955), N=96 first (0.968); S11 N=24 (0.966), N=96 (0.952).
FAIL (shape-flagged): S10 T=0.34 (0.914), T=0.40 (0.945), T=0.56 (0.949 —
fails by the letter); S12 N=24 first (0.861), N=48 mean (0.837),
N=192 mean (0.925), N=192 first (0.891).

Seven of fourteen points carry the flag: the mid-distribution hazard is
non-constant at half the archive. The kinetics are richer than a single
Kramers rate — this is the session's structural finding, and every
downstream number below inherits the flags of its inputs as the bars
require.

## B2 — the STRAND-010 promotion: CONFIRMED-ROBUST, with shape flags

Robust Arrhenius on the four-T archive: tau_rate = 1466 / 545 / 193 / 70,
DeltaE_rob = 2.634 at r^2 = 0.9958, nu_rob = 1.467 — inside [1/3, 3].
Verdict per the locked bar: CONFIRMED-ROBUST. The identification (attempt
rate = band gap to O(1)) holds on BOTH estimators: nu = 0.451 (mean-based)
and 1.467 (rate-based), window [1/3, 3] containing both.

Stated with equal volume: the BARRIER VALUE is estimator-sensitive —
DeltaE 2.112 (mean) vs 2.634 (rate), a 25% spread — and three of the four
input points are shape-flagged, so the flag rides B2 on its face. The
identification is robust; the barrier's decimal is not yet a constant.

## B3 — the crossover: ESTIMATOR-INDEPENDENT

Nucleation-channel robust pairwise slopes: -2.04 / -1.80 / -0.81. The 012
signature (both small-N legs <= -1.15, the 96->192 leg >= -1.0) is
RETAINED: the crossover — steep small boxes flattening toward
rate-additivity — is registered estimator-independent. The robust curves
are wilder in the flagged channels (conversion pairwise -0.04 / -3.41 /
-1.05 with the N=48 point shape-flagged at 0.837), reported as-is with
their flags; the crossover verdict rests on the nucleation channel, whose
flags sit at the endpoints, not the signature-carrying legs' shared
mid-structure.

## B3 — the N = 24 fragility adjudication: the convenient answer REFUSED

Per-batch tau_rate at N = 24: S12 batches 598 / 1521 (ratio 2.54); S11
batches 1451 / 3005 (ratio 2.07) — both far beyond the 1.35 bar, and NO
BETTER than the mean-based ratios (1.86, 2.29). Verdict per the locked
grammar: the factor-2 swings are NOT mean-specific tail artifacts — RATE
HETEROGENEITY AT THE SMALLEST BOX IS PHYSICAL (or at minimum lives below
the estimator, in the hazard's own shape): different thermal initial
conditions produce persistently different escape rates at N = 24.

Confound stated in advance of the census: non-constant hazard (B1's
finding) itself inflates batch dispersion, so "seed-level heterogeneity"
and "aging hazard" are not yet separated — the pre-named next-order (the
per-seed hazard census) is designed to separate exactly these.

## B4 — STRAND-011's exponent, robust reading (reported, not asserted)

Robust three-point slope: -2.447 (vs the retired mean-based -1.661). The
two estimators disagree wildly on a quantity 012 already showed is
malformed — recorded as further confirmation that no single exponent
exists, nothing more.

## Ledger

- The identification survives its severest available test: two estimators
  with opposite failure modes both land nu in the O(1) window.
- The barrier value, the exponent, and half the shape ledger do NOT
  survive unflagged — kept at full volume.
- The smallest box now carries a physical question, not a statistical one.
- NEXT-ORDERS: (1) the per-seed hazard census at N = 24 (separate
  heterogeneity from aging; archived data may partially serve, new
  long-window runs likely needed); (2) hazard-shape characterization under
  blind bars (the B1 flags earn their own session); (3) the {192, 384}
  asymptote pair, unchanged.
- No new runs; no estimator shopping; STRAND-012's registered mean-based
  numbers untouched. Status: Modeled.
