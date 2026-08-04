# FND-STRAND-010 — the promotion rerun: results against the locked bars

Bars: analysis/STRAND010_promotion_bars_LOCKED.md (h re-locked at 0.55 with
rationale; seed budget priced at S = 64/point before the threshold was
reused). Dataset archived verbatim: analysis/STRAND010_promotion_data.json
(4 x 64 escape times; generators seed0 = 11, 12 at S = 32 each, as locked).

## Execution ledger

Engine: FND-STRAND-008 composite verbatim, kt = 0.64, N = 48, K = 16,
c0 = 0.35, dt = 0.02, h = 0.55 (re-locked), tmax = 12000 time units.
The T = 0.34 batches ran chunked with exact state checkpointing (identical
trajectories to a single-shot run; the locked seed set preserved bit-for-bit).

| T    | S  | censored | mean tau | rel. SE |
|------|----|----------|----------|---------|
| 0.34 | 64 | 0        | 1052.9   | 0.225   |
| 0.40 | 64 | 0        | 457.7    | 0.148   |
| 0.47 | 64 | 0        | 209.6    | 0.173   |
| 0.56 | 64 | 0        | 90.8     | 0.109   |

Zero censoring anywhere: the raised tmax retired the exposure exactly as
intended (slowest walker escaped at ~11000 units at T = 0.34).

## B1' — the Boltzmann limb: PASS

ln(tau_mean) vs 1/T: DeltaE_eff = 2.112, r^2 = 0.9965 against the unchanged
0.97 bar. The pricing was honest: the bar was priced to pass at ~0.979 if
the shape was Arrhenius, and the data cleared it with room — the shape IS
Arrhenius over this range. DeltaE_eff sits inside STRAND-009's 1.9–2.1
stability band from every prior handling.

## B2' — the nu-identification: PROMOTED

nu = exp(-intercept) = 0.451 x omega_min, inside the locked window [1/3, 3].
Both limbs pass; per the pre-committed criterion the identification is
PROMOTED from supported to measured:

  THE ATTEMPT RATE IS THE WEAVE BAND GAP TO O(1).
  tau = O(1) x omega_min^-1 x exp(DeltaE_eff / T)

on a bath the corpus derived (STRAND-007), whose spectrum it measured
(STRAND-008), and whose regime it adjudicated attempt-limited (STRAND-009
B3). Every symbol in the Kramers form now has a corpus-internal provenance.

Consequence, conditional lifted as pre-committed: Prediction 11's latency
and dark-count prefactors inherit the STRAND MASS SCALE, not the environment
coupling — now stated unconditionally at model level (Modeled status and the
absolute-scale caveat still apply; the frequency is scale-open per
FND-MATTER-003, the SHAPE and the clock identification are the commitments).

## Hygiene

- The STRAND-009 h-deviation is discharged by re-lock, not pardon: h = 0.55
  was fixed in the bars with its rationale before any run, and the runs
  honored it.
- The seed-budget pricing lesson was executed, and the margin behaved as
  priced (expected r^2 0.979; realized 0.9965).
- Consistency across independent generators: per-batch means at each T agree
  within the exponential estimator's expected scatter; no batch was dropped.
- OUT OF SCOPE, standing open: the N-sweep (collective vs per-site nu); the
  rare-event exponent (since STRAND-006); B3 not rerun, stands as registered.
- Status: Modeled (inherits STRAND-007/008/009).
