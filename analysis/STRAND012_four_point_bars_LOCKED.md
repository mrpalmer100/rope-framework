# FND-STRAND-012 — the blind four-point sweep: bars locked before computation

Date: 2026-08-03. Commission: STRAND-011's named next-order, run BLIND: all
grammar below is committed before any new trajectory exists; no archived
point is reused (the decomposition needs the two-channel observable on every
box, which the archives lack). This session is promotion-eligible by
construction — the 011 addendum's informed-status ceiling does not apply
here because nothing here is written informed.

## The question, decomposed

STRAND-011 measured super-extensive scaling of the mean-crossing time
(s = -1.66) and named the suspects. This session separates them with two
channels recorded PER RUN, aligned:

- t_first: first local passage (max_i phi_i > pi) — first-event statistics,
  the nucleation channel.
- t_mean: mean-field crossing (mean phi > pi) — the registered legacy
  observable.
- t_conv := t_mean - t_first per run — the conversion (growth/spread)
  channel.

If nucleation is per-site Poisson with an N-independent barrier, t_first
scales exactly as 1/N (slope -1): rate-additivity is the null. Barrier
relief with N (suspect i) steepens t_first below -1. Parallel multi-seed
conversion (suspect iii) shrinks t_conv with N without touching t_first.

## Design

Engine: FND-STRAND-008 composite verbatim; h = 0.55, T = 0.40, c0 = 0.35,
kt = 0.64, K = 16, dt = 0.02. N in {24, 48, 96, 192}. S = 64 per point,
generators fixed now: seed0 = {41, 42} (N=24), {51, 52} (N=48), {61, 62}
(N=96), {71, 72} (N=72 -> typo guard: N=192), S = 32 each.

WINDOWS PRICED PER-N (the 011 lesson executed): the 011 straggler reached
17015 at N = 24 (mean 1569), i.e. ~11x the mean — tails are heavier than
exponential. Windows set at >= 20x the extrapolated mean:
tmax(24) = 36000; tmax(48) = 24000; tmax(96) = 12000; tmax(192) = 8000.
Censoring clause unchanged: a censored run invalidates its point; a slope
bar needs >= 3 valid points on its channel or NO-VERDICT for that channel.
Chunked exact-state checkpointing pre-authorized.

## B1 — the nucleation channel (t_first slope s_f over four points)

- RATE-ADDITIVE: s_f in [-1.15, -0.85]. Per-site Poisson with an
  N-independent barrier is CONFIRMED; the entire super-extensive excess in
  t_mean is assigned to conversion, and B2 must corroborate or the session
  fails its own closure (B3).
- BARRIER-RELIEF: s_f <= -1.3. The barrier itself falls with N over this
  range (suspect i dominant); registrable at full volume, with the
  finite-size mechanism (ring-periodic pair interaction) named for the
  follow-up.
- INTERMEDIATE: s_f in (-1.3, -1.15) or (-0.85, -0.3): mixed; both
  mechanisms contribute; register the split as measured.
- ANOMALOUS: s_f > -0.3 or non-monotone ordering of the four means:
  register as found; no promotion; instrument audit becomes the next-order.
- Fit-quality gate for any promotion: r^2 >= 0.97 on the priced budget
  (per-point scatter 1/sqrt(64) = 0.125; expected r^2 >= 0.98 for any
  power law in the committed range).

## B2 — the conversion channel (t_conv slope s_c over four points)

- PARALLEL CONVERSION: s_c <= -0.5 (t_conv shrinks with N; suspect iii
  active).
- N-FLAT CONVERSION: |s_c| <= 0.3 (conversion does not drive the excess).
- INTERMEDIATE: (-0.5, -0.3): as measured.
- POSITIVE: s_c >= +0.3 is admissible physics (a bigger ring takes longer
  to convert at fixed seed count) and is registered as found.

## B3 — closure (the check that keeps B1/B2 honest)

The direct t_mean four-point slope must be reproduced by the two-channel
decomposition: recompose <t_mean>(N) = <t_first>(N) + <t_conv>(N)
identically (it is a per-run identity, so this is an accounting check that
the channels were recorded aligned, bar: exact to numerical roundoff), and
the t_mean slope must land within 0.15 of STRAND-011's -1.661 (continuity
with the registered measurement at the overlapping boxes; a larger shift is
registered as a finding about the 192 extension, not smoothed).

## Promotion criteria, stated in advance

- If B1 lands RATE-ADDITIVE and B2 lands PARALLEL CONVERSION and B3 closes:
  PROMOTE the decomposition "clock = band gap per event; excess = parallel
  conversion; barrier N-free" — and STRAND-010's scope note simplifies (the
  per-event identification becomes box-free at the nucleation level).
- If B1 lands BARRIER-RELIEF and B3 closes: PROMOTE "the barrier is
  N-dependent over 24..192" — STRAND-010's scope note stands and sharpens
  (the Arrhenius slope itself needs an N-tag; the earlier DeltaE_eff = 2.1
  becomes the N = 48 value).
- Mixed/intermediate outcomes: registered as measured, split quantified, no
  promotion; the next lever is a direct barrier measurement per N
  (constrained saddle search), pre-named.

## Honesty clauses

- Windows, seeds, grammar, and promotion criteria are all fixed above
  before any run; any deviation is a fresh violation.
- t_first depends on the local threshold choice (pi); this is the same
  threshold as the legacy observable, kept for comparability, and the
  arbitrariness is priced: slopes, not absolute times, carry the bars.
- Status ceiling: Modeled (inherits STRAND-007/008). Absolute scale
  untouched (FND-MATTER-003).
