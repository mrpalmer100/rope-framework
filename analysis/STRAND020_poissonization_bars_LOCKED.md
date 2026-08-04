# FND-STRAND-020 — the Poissonization session: bars locked first

Date: 2026-08-03. Commission: v3.7.0's headline debt. Target status:
DERIVED — the corpus's first Derived candidate of the strand-kinetics arc.

## D1 — the derivation (committed in full before any comparison)

ASSUMPTIONS, named: (A1) INDEPENDENCE — a ring of size N hosts escape
channels that are statistically independent; (A2) INTENSIVITY — each
channel's waiting-time law is a property of the medium (per-channel
hazard shape and its memory epoch do not depend on N); (A3) PROPORTIONAL
COUNT — the channel count scales as M(N) proportional to N.

THE LAW: if the aggregate escape is the first event among M independent
channels, the aggregate survival is the product of channel survivals:
S_N(t) = s(t)^{M(N)}. Taking the measured N = 24 ensemble as the
reference (whatever its own channel count M_24 is), A2 + A3 give

    S_N(t) = S_24(t)^{N/24}      — PARAMETER-FREE.

The unknown M_24 CANCELS: the law needs no correlation length, no channel
count, no fitted constant. Corollaries: (i) the aggregate hazard is
lambda_N(t) = (N/24) lambda_24(t) — same shape, scaled magnitude; (ii)
aggregate quantiles map exactly as q_p(N) = q_{p^{24/N}}(24) — the large
ring reads the SMALL-QUANTILE (early, locally flat) part of the reference
curve, which is WHY R(N) -> 1: window compression against an intensive
memory scale, the mechanism behind the Khinchin intuition, here exact and
finite-N. (iii) The 012 crossover marks A2's expected breakdown at SMALL
N (barrier relief changes the per-channel law below ~48): deviations at
N = 48 in the direction of LONGER measured times are consistent-with-012,
pre-named, and are not strikes against the law in its stated domain.

## The confrontation, committed

Reference: the pooled censor-free N = 24 archive (n = 512; the committed
014/015/016 pool). Predictions computed from the reference ALONE via the
quantile map, then compared to the v3.7.0 table (FND-STRAND-019, which
this session may not recompute or reweight):

- R_pred(N) for N in {48, 96, 192}: the STRAND-013 hazard-ratio estimator
  applied to the PREDICTED distribution — equivalently, hazards of the
  N = 24 sample evaluated over the MAPPED windows
  [q25(N), q50(N)] -> [q_{0.75^{24/N}}, q_{0.50^{24/N}}] etc.
- Median_pred(N) = q_{0.50^{24/N}}(24).

## B1 — the primary bar

R_pred(N) lands inside the REGISTERED bootstrap 95% CI of the measured
R(N) (from the 019 table: [0.138, 0.530] at 48; [0.247, 0.820] at 96;
[0.502, 1.513] at 192).
- CONFIRMED: 3 of 3 inside.
- PARTIAL: 2 of 3, with the miss at N = 48 AND in the 012-consistent
  direction -> the law holds in its stated domain (A2's breakdown at
  small N as pre-named); registered as CONFIRMED-IN-DOMAIN.
- REFUTED: otherwise; the independence assumption (A1) becomes the named
  suspect and the hazard-shape session revives.

## B2 — the secondary bar (medians)

Median_pred(N) within a factor 1.5 of the measured median for N = 96 and
192 (N = 48 reported, with the 012-consistent direction clause as above).
- PASS/FAIL per point, reported; B2 does not gate promotion alone but a
  double miss at 96 AND 192 demotes any B1 pass to PARTIAL.

## Promotion criterion

PROMOTE at status DERIVED iff B1 lands CONFIRMED or CONFIRMED-IN-DOMAIN
and B2 does not demote. The Derived status attaches to the LAW
(S_N = S_24^{N/24} under A1-A3, with A2's small-N domain edge on the
claim's face); the confrontation is its verification. Otherwise: register
as measured; A1 inherits the suspicion.

## Honesty clauses

- The 019 table is used as REGISTERED; nothing is recomputed from its
  underlying samples except the reference S_24, which 019 pooled under
  its own committed rule.
- The quantile map at N = 192 reads the reference's 3.5th-percentile
  region (~18 of 512 points) — priced and adequate for factor-level bars;
  stated so the tail-thinness is on the record.
- No smoothing, no interpolation beyond linear between order statistics.
- Status ceiling: Derived (conditional on A1-A3, domain edge stated).
  Absolute scale untouched (FND-MATTER-003).
