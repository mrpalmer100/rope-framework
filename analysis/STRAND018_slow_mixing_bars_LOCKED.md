# FND-STRAND-018 — the slow-mixing session: bars locked first

Date: 2026-08-03. Commission: FND-STRAND-017's refined candidate.
Hypothesis under test: SLOW-MIXING MEMORY — the weave is an internally
mixing thermal network; on times shorter than its mixing time it is a
non-Markovian bath; the escape hazard falls while the bath remembers its
initial microstate and plateaus once mixing completes; and the mixing time
shrinks with N, making the non-exponential structure a small-box
phenomenon. Three predictions, each with grammar fixed below.

## The mixing clock, defined exactly

Per walker, the per-mode energy vector E(t) (N x K entries, shifted-
oscillator energies as in the STRAND-017 check: E_nk = 0.5 p^2 +
0.5 omega^2 (q - c phi/omega^2)^2), sampled every 10 units while alive.
Memory overlap O(t) := mean over alive walkers of the Pearson correlation
between the vectors E(t) and E(0). tau_mix := the earliest sampled t at
which the pooled O(t) <= 1/e, linearly interpolated between samples. No
other clock may be consulted.

## Design

Operating point: the standard one (h = 0.55, T = 0.40, c0 = 0.35, K = 16,
dt = 0.02). Mixing runs: N = 24 with S = 32 (generator 131) to t = 6000;
N = 96 with S = 32 (generator 132) to t = 3000. POOLING RULE, committed:
the archived N = 24 escape samples of STRAND-014 (n = 256), -015
(n = 128), and -016 (n = 128) were generated at the IDENTICAL operating
point and window (36000) with disjoint generators, and are pooled
(n = 512) for P2; no other data enters.

## P1 — the timescale coincidence

Bar: tau_mix(24) lies within [q25, q90] of the pooled 512-walker escape
distribution (the hazard-fall window).
- IN-WINDOW: the mixing clock and the hazard fall share a timescale.
- OUT: registered as found; the candidate loses its central coincidence.

## P2 — the plateau

On the pooled n = 512: lambda_1 over [q25, q50], lambda_2 over [q50, q90],
lambda_3 over [q90, q98] (STRAND-013 estimator; the [q90, q98] slice holds
~41 events — priced, adequate for a factor-level bar).
- PLATEAU-CONSISTENT: lambda_2/lambda_1 <= 0.7 (the known fall) AND
  lambda_3/lambda_2 in [0.6, 1.5] (the fall stops or decelerates to
  within noise beyond the mixing epoch).
- STILL-FALLING: lambda_3/lambda_2 < 0.6 — the hazard keeps falling past
  the candidate's plateau horizon; the memory picture in its simple form
  is refuted at this horizon; registered.
- REVERSAL: lambda_3/lambda_2 > 1.5 — registered as found.

## P3 — the size scaling

r_N := tau_mix(96)/tau_mix(24).
- SHRINKS: r_N <= 0.5 — more chain channels mix the weave faster; the
  small-box exclusivity is explained and the STRAND-012 crossover is
  reconnected from this side.
- DOES-NOT-SHRINK: r_N >= 0.8 — refuted; registered.
- INTERMEDIATE: as measured.

## Promotion criterion

PROMOTE slow-mixing memory as the mechanism of the small-box
non-exponential escape iff P1 IN-WINDOW and P2 PLATEAU-CONSISTENT and P3
SHRINKS. Any other combination: as measured, follow-up named by the
failing limb. Consequence grammar if promoted: the smallest box's escape
is Markovian-with-memory-transient — Prediction 11's fork resolves toward
a FINITE-MEMORY statement (non-exponential waiting times over the bath's
own equilibration epoch, exponential beyond), which is a testable,
bounded deviation from ideal Poisson rather than an open-ended one.

## Honesty clauses

- Clock, cadence, generators, pooling rule, windows, and thresholds fixed
  above. Clauses checked pairwise; no clause caps another.
- Censoring: the pooled archives are censor-free as registered; the
  mixing runs measure overlap, not escape, and walkers escaping during a
  mixing run simply leave the alive-average (reported).
- Status ceiling: Modeled. Absolute scale untouched (FND-MATTER-003).
