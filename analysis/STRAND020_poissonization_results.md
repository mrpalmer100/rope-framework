# FND-STRAND-020 — the Poissonization session: results

Bars: analysis/STRAND020_poissonization_bars_LOCKED.md (derivation,
assumptions, quantile map, and both bars committed before any comparison).

## The law, restated

Under (A1) channel independence, (A2) intensive per-channel law, and (A3)
channel count proportional to N:

    S_N(t) = S_24(t)^{N/24}

PARAMETER-FREE — the reference channel count cancels. Corollary mechanism
for the whole arc: the aggregate hazard is (N/24) x the reference hazard
with UNCHANGED shape, so a large ring's observation window compresses onto
the early, locally flat stretch of the reference curve while the memory
epoch stays intensive — R(N) -> 1 by window compression, the finite-N
sharpening of the Khinchin intuition.

## The confrontation (predictions from the n = 512 reference alone)

| N   | R_pred | R_meas | 95% CI (registered) | inside | med_pred | med_meas | factor |
|-----|--------|--------|---------------------|--------|----------|----------|--------|
| 48  | 0.292  | 0.281  | [0.138, 0.530]      | YES    | 136.3    | 154.8    | 1.14   |
| 96  | 0.647  | 0.479  | [0.247, 0.820]      | YES    | 80.2     | 88.2     | 1.10   |
| 192 | 0.930  | 0.972  | [0.502, 1.513]      | YES    | 53.7     | 69.8     | 1.30   |

B1: CONFIRMED, 3 of 3 inside the registered intervals — including the
N = 192 prediction of near-exponentiality (0.930) landing on the measured
0.972. B2: PASS at every size (factors 1.10-1.30 against a 1.5 bar), and
the N = 48 median misses in exactly the 012-consistent direction
(measured LONGER — barrier relief at small N), as pre-named.

The tail-thinness clause honored: the N = 192 windows read the
reference's 3.5th-percentile region (24/85 events per window) — priced in
the bars, adequate for the factor-level verdicts rendered.

## PROMOTED at DERIVED

The law is registered at Derived status — the strand-kinetics arc's
cornerstone — with its assumptions and domain edge on the claim's face:
A1-A3 stated; A2's small-N breakdown (the 012 barrier-relief crossover)
marks the domain boundary, and the confrontation shows the law already
accurate at N = 48 to 14% despite sitting near that edge.

What the promotion retires and unifies:
- The size-effect fork (019) now has its mechanism DERIVED, not named.
- The hazard-shape session (013's flags) is RETIRED: non-constant hazard
  at every size is the law's direct corollary (the reference shape,
  window-compressed), no longer an anomaly needing its own session.
- Prediction 11 reaches closed form: a detector's dark-count survival is
  the per-channel curve raised to its channel count; small detectors show
  the per-channel memory transient, large ones compress onto its flat
  early stretch and read Poisson. The size condition is now an EQUATION,
  not a qualitative statement.

## Ledger and next-orders

- B1 CONFIRMED 3/3; B2 PASS 3/3; PROMOTED at Derived per the committed
  criterion. Zero new trajectories; the entire session ran on archives.
- ELEVEN SESSIONS RESOLVED: 009 (clock supported) -> 010 (clock promoted)
  -> 011/012 (scaling and crossover) -> 013 (estimator robustness) ->
  014/015/016 (three exclusions) -> 017 (dead theory, kept) -> 018
  (intensive mixing) -> 019 (the fork) -> 020 (the law). The arc is
  closed.
- REMAINING OPEN, inherited not new: the per-channel law's own shape
  (why lambda_24(t) falls as it does — the 017-successor theory question,
  now cleanly separated from the size question the law just answered);
  the direct per-N saddle (012's residual); exact-D on the 3D instrument
  (GRV-095's residual).
- Status: Derived (A1-A3 on the face; domain edge at small N stated).
  Absolute scale untouched (FND-MATTER-003).
