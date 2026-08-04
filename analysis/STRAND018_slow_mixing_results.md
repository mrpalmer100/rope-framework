# FND-STRAND-018 — the slow-mixing session: results

Bars: analysis/STRAND018_slow_mixing_bars_LOCKED.md (blind; clock, cadence,
generators, pooling rule, thresholds fixed first). Mixing curves archived:
analysis/STRAND018_mixing_curves.json.

## The mixing clock

O(t) := pooled Pearson overlap of the per-mode energy vector with its
initial value, among alive walkers. tau_mix at 1/e:
- N = 24: tau_mix = 177.3
- N = 96: tau_mix = 172.2

## Verdicts, off the locked grammar

P1 — TIMESCALE COINCIDENCE: IN-WINDOW. tau_mix(24) = 177 lies inside the
pooled (n = 512) hazard-fall window [q25, q90] = [114, 3378]. Honesty
note, at full volume: it sits at the EARLY edge — mixing is essentially
complete by ~3 tau_mix ~ 530, while the hazard continues falling to
~3000. The coincidence bar passes as written, but the simple reading
("hazard falls while memory persists, stops when it fades") is strained
by the geometry, and P2's deceleration carries the surviving version.

P2 — THE PLATEAU: PLATEAU-CONSISTENT. On the pooled 512:
lambda_1 = 1.41e-3 (128 events), lambda_2 = 5.2e-4 (204),
lambda_3 = 4.06e-4 (41). l2/l1 = 0.371 (the known fall);
l3/l2 = 0.778, inside [0.6, 1.5]: the fall decelerates strongly in the
far tail, consistent with an approach to a constant floor.

P3 — SIZE SCALING: DOES-NOT-SHRINK, decisively. r_N = 172.2/177.3 =
0.971 against a shrink bar of 0.5. tau_mix is INTENSIVE — and in
hindsight it must be: each site's K modes mix through that site's own
chain coordinate; the mixing network is local, so its clock cannot know
the ring's size. The prediction's premise (small-box exclusivity
explained by N-dependent mixing) was misdrawn.

PROMOTION: NO (P3 failed). Registered as measured: two limbs pass, the
size limb fails, and the failure is the informative part.

## What P3's failure exposes, plus one exploratory check (labeled)

If tau_mix is intensive, the memory picture — whatever its final form —
should operate at EVERY N, which prompts the question the arc never asked
directly: is the falling hazard actually a small-box phenomenon at all?
EXPLORATORY (post-hoc, no verdict rides on it; it feeds the next bars):
pooling the archived N = 96 escapes (STRAND-011 + -012, n = 128, identical
operating point), R(96) = 0.479 — the hazard falls at N = 96 essentially
as it does at N = 24 (0.33-0.43).

THE REFRAMING: the non-exponential escape is plausibly N-GENERAL. The
"smallest-box anomaly" framing that launched this arc was partly an
artifact of where the estimator drama happened (the heavy-tail mean at
N = 24), not of where the physics lives. STRAND-013's shape flags at
N = 192 said this quietly; tonight's intensive tau_mix and the
exploratory R(96) say it loudly.

## Ledger and next-orders

- P1 IN-WINDOW (edge geometry noted); P2 PLATEAU-CONSISTENT; P3
  DOES-NOT-SHRINK; no promotion. tau_mix ~ 175, intensive, now a
  measured constant of the composite at this operating point.
- The slow-mixing candidate survives in weakened form (deceleration
  toward a floor is consistent; the timescale geometry is strained) and
  must now be N-general or nothing.
- NEXT-ORDER, fully specified: the N-GENERALITY SESSION under blind
  bars — hazard ratio R(N) across {24, 48, 96, 192} with per-N priced
  sample sizes (archived data partially serve: 24 and 96 are rich; 48
  and 192 need fresh walkers at matched windows), grammar committed for
  R flat-in-N (general finite-bath transient) vs R rising toward 1 with
  N (genuine small-box effect) — the fork that decides whether
  Prediction 11's non-Poisson statement carries a size condition.
- Status: Modeled. Absolute scale untouched (FND-MATTER-003).
