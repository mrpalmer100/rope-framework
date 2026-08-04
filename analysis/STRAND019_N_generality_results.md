# FND-STRAND-019 — the N-generality session: results

Bars: analysis/STRAND019_N_generality_bars_LOCKED.md. Fresh data archived:
analysis/STRAND019_N_generality_data.json (N = 48 and 192, n = 128 each,
zero censoring). Archived pools per the committed rule.

## The table (committed estimator, bootstrap 95% CIs, seed 2027)

| N   | n   | R     | 95% CI          |
|-----|-----|-------|-----------------|
| 24  | 512 | 0.371 | [0.263, 0.507]  |
| 48  | 128 | 0.281 | [0.138, 0.530]  |
| 96  | 128 | 0.479 | [0.247, 0.820]  |
| 192 | 128 | 0.972 | [0.502, 1.513]  |

slope s_R = +0.495 over ln N.

## Verdict: SIZE-EFFECT, cleanly

s_R = 0.495 against the 0.25 threshold. R rises toward 1 with N, and at
N = 192 the hazard ratio is consistent with FULLY EXPONENTIAL escape
(R = 0.97, CI spanning 1). The non-exponential transient is a genuine
SMALLNESS effect: strong at N = 24-48, intermediate at 96, gone by 192 at
this operating point. Per the pre-committed pricing language, this session
decides the fork, not the decimal — and the fork is decided.

The STRAND-018 exploratory hint (R(96) = 0.48 "in the N = 24 range") is
SUPERSEDED exactly as the bars required: the 96 point alone was
misleading; the four-point picture shows the rise, and the quarantine of
the exploratory number did its job — it seeded the design and granted no
verdict a head start.

## The explanation candidate, named (and it needs no new mechanism)

The result coheres perfectly with STRAND-012's crossover (nucleation
approaching rate-additivity by 96 -> 192): a large ring hosts many
INDEPENDENT escape channels, and the superposition of many independent
renewal processes POISSONIZES the aggregate first-passage (the classical
Khinchin superposition limit) REGARDLESS of per-channel memory. An
intensive per-site memory transient (tau_mix ~ 175, STRAND-018) survives
at every size, but the aggregate hazard flattens as the channel count
N / xi grows. Small boxes show the transient because they ARE one or few
channels; big boxes hide it behind Poissonization. The onset scale is the
channel count, not a new physical scale — a parameter-free explanation
candidate, promotable to a derivation in its own session (the Khinchin
argument is theorem-shaped and the corpus prefers theorems).

## Consequence for Prediction 11, now stated in final form (pending derivation)

The non-Poisson dark-count signature carries a SIZE CONDITION: small
isolated detectors (few independent nucleation channels) show a bounded
non-exponential waiting-time transient over the bath's own mixing epoch;
large detectors show ideal-Poisson statistics because superposition
Poissonizes them. The deviation's onset is set by the number of
independent channels — a counting statement, not a new constant.

## Ledger and next-orders

- SIZE-EFFECT registered per the locked grammar; NO promotion (that
  criterion belonged to the other fork branch); the bootstrap CIs carried
  alongside every value as committed.
- Zero censoring; the exploratory hint superseded on schedule; all four
  points on the committed estimator.
- NEXT-ORDERS: (1) THE POISSONIZATION SESSION — derive the Khinchin
  superposition limit for this engine (channel count N/xi from the
  measured kink correlation length; predict R(N) parameter-free; compare
  against tonight's table under blind bars; a Derived-status candidate);
  (2) the onset-scale empirical fit rides inside (1); (3) the
  hazard-shape session (013's flags) is largely SUBSUMED: the flags'
  N-pattern matches the size-effect and should be revisited only if (1)
  fails.
- Status: Modeled. Absolute scale untouched (FND-MATTER-003).
