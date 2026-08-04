# FND-STRAND-014 — the per-seed hazard census at N = 24: results

Bars: analysis/STRAND014_hazard_census_bars_LOCKED.md (blind; covariates,
stratifier rule, windows, census size, seeds, bootstrap protocol all fixed
first). Dataset archived: analysis/STRAND014_hazard_census_data.json
(256 walkers, per-walker aligned t_mean / t_first / three IC covariates).

## Execution

N = 24, window 36000 units, 8 batches (seed0 = 81..88), n = 256, ZERO
censoring (slowest walker: 32319). Pooled: mean 1317, median 350 — the
mean/median ratio of 3.8 is the heavy tail in one number.

## B1 — traceability: INTERMEDIATE

Spearman rho against t_mean: E_w0 -0.165 (p = 0.008), E_soft0 -0.166
(p = 0.008), F0 -0.019 (n.s.). Sign is physical (more initial weave energy
-> faster escape) and significance is real, but magnitude sits far below
the 0.30 traceable bar: the measured weave functionals carry only a few
percent of the dispersion. Stratifier for B3 per the locked rule: E_soft0.

## B2 — pooled hazard: DECREASING, strongly

lambda_early = 1.60e-3, lambda_late = 5.2e-4, R = 0.326. The escape rate
for survivors falls ~3x from the [q25,q50] window to the [q50,q90] window.

## B3 — the separation: AGING-CLASS, registered AS MEASURED

Within-tercile hazard ratios: 0.514 / 0.319 / 0.580 — ALL THREE terciles
show falling hazard; stratifying on the best available covariate flattens
nothing. The locked grammar's AGING clause (>= 2 terciles with R <= 0.7)
is met in full.

TWO HONESTY ITEMS, adjudicated conservatively and on the record:

1. CLAUSE CONFLICT in the locked bars: B1-INTERMEDIATE "caps B3 at
   as-measured," while the promotion clause makes the aging verdict
   "promotable under any B1 outcome." The conflict is real, it is ours,
   and it resolves CONSERVATIVE: no promotion tonight. Logged as a
   bar-drafting lesson (clauses must be checked pairwise for consistency
   before locking).
2. FRAILTY EQUIVALENCE, stated at full volume: falling within-tercile
   hazard is observationally equivalent to heterogeneity along an
   UNMEASURED covariate (the classic frailty degeneracy). The census rules
   out heterogeneity along the three measured functionals; it cannot, by
   design, rule out hidden frailty. The bars' AGING grammar was too
   permissive on this point — a second drafting lesson, logged.

What IS registrable at full strength: the falling hazard is NOT
attributable to the measured weave functionals, and the smallest box's
escape process is non-memoryless at the population level with R = 0.33.

## B4 — batch-dispersion closure: EXPLAINED (a real closure)

Bootstrap 95% band for 32-walker batch-pair tau_rate ratios from the pooled
census: [1.02, 3.39]. The historical STRAND-011/012 ratios (2.07, 2.54) sit
comfortably inside. VERDICT: no generator-level anomaly ever existed — the
"batch swings" are exactly what this distribution does at n = 32. This
refines STRAND-013's finding with precision: the dispersion is PHYSICAL and
DISTRIBUTIONAL (the falling-hazard/heavy-tail structure itself), not
generator artifacts and not (so far) traceable IC classes.

## The physical picture this points at

The composite starts with all thermal energy in the weave and none in the
channel; early escapes ride the initial fluctuation spectrum; survivors
inhabit a composite that has partially equilibrated — energy spread into
the chain, the weave's effective temperature relaxed. A finite bath COOLS
as it works, and a cooling bath is a genuinely aging hazard shared by all
walkers. This mechanism is testable directly and cheaply: measure the
instantaneous weave temperature among survivors as a function of time and
compare against the hazard trace.

## Ledger and next-orders

- B1 INTERMEDIATE; B2 DECREASING (R = 0.326); B3 AGING-CLASS as measured
  (conservative resolution of the clause conflict; frailty degeneracy
  named); B4 EXPLAINED (batch-swing question CLOSED).
- Two bar-drafting lessons logged (pairwise clause consistency; frailty
  degeneracy in aging grammars).
- NEXT-ORDERS: (1) SURVIVOR THERMOMETRY — track the weave's instantaneous
  temperature along trajectories and test the cooling-bath mechanism
  against the hazard trace (designed to break the frailty degeneracy with
  a state measurement rather than a covariate); (2) the hazard-shape blind
  session (013's flags), now informed by R = 0.33 at N = 24; (3) the
  {192, 384} asymptote pair, unchanged.
- Status: Modeled. Absolute scale untouched (FND-MATTER-003).
