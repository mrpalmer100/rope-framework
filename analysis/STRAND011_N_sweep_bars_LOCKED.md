# FND-STRAND-011 — the N-sweep: bars locked before computation

Date: 2026-08-03. Commission: the standing open item on FND-STRAND-009/010 —
is the promoted attempt rate nu = 0.451 x omega_min a property of the MEDIUM
(intensive: a collective escape clock) or of the BOX (extensive: per-site
nucleation summing to a system-size-dependent rate)? The promoted
identification's reach depends on the answer, and both directions are
registrable.

## Design

Engine: FND-STRAND-008 composite verbatim; h = 0.55, T = 0.40, c0 = 0.35,
kt = 0.64, K = 16, dt = 0.02, tmax = 12000 units. N in {24, 48, 96}.

THE N = 48 POINT IS THE ARCHIVED STRAND-010 DATASET (T = 0.40, 64 seeds,
generators 11/12), reused verbatim — pre-committed here, not decided after
seeing new data. New points: N = 24 with generators seed0 = {21, 22} at
S = 32 each; N = 96 with seed0 = {31, 32} at S = 32 each. Budget S = 64 per
point throughout, priced per the STRAND-010 rule: per-point scatter of
ln(tau_mean) ~ 1/sqrt(64) = 0.125, giving slope standard error ~0.13 over
the ln N span of 1.386 — adequate to separate grammars 0.4 apart at their
boundaries.

## B1 — the scaling limb

Fit slope s of ln(tau_mean) vs ln(N) over the three points.

- INTENSIVE verdict: |s| <= 0.3. The escape clock is a property of the
  medium; nu is N-independent; the STRAND-010 promotion EXTENDS — the
  identification (attempt rate = band gap to O(1)) holds as stated, box-free.
- EXTENSIVE verdict: s in [-1.3, -0.7]. Nucleation is per-site and rates
  add; the collective nu scales ~N, so the promoted O(1) window membership
  at N = 48 was PARTLY COINCIDENTAL. Grammar, fixed now: the promotion is
  NARROWED, not revoked — the surviving statement is the per-site form
  nu_site = nu/N with the barrier unchanged, and the identification must be
  restated at the per-site level, where nu_site << omega_min and the clock
  question REOPENS. This outcome is registrable at full volume.
- NEITHER (-0.7 < s < -0.3): UNRESOLVED-INTERMEDIATE as measured; named
  suspect (pre-stated): the registered observable convolves nucleation with
  kink-pair GROWTH to the mean-crossing, and the growth time scales with N —
  partial cancellation can produce intermediate slopes. No promotion of
  either grammar; the deconvolution becomes the next-order.

## Honesty clauses

- OBSERVABLE CONTINUITY: escape is mean(phi) > pi, the registered
  STRAND-006..010 observable, kept for comparability. Its convolution of
  nucleation + growth is named ABOVE, in advance, as the intermediate
  outcome's suspect — not invoked after the fact to rescue a preferred
  verdict.
- DIAGNOSTIC, reported not asserted: the first-passage time of the maximum
  local phase (max_i phi_i > pi), a growth-light proxy, recorded on the new
  runs for the deconvolution's benefit. No bar rides on it.
- Censoring clause unchanged: any censored run invalidates its point; two
  valid points cannot fit a slope bar — NO-VERDICT with censoring reported.
- Chunked exact-state checkpointing is pre-authorized (bit-identical
  trajectories; the STRAND-010 execution note).
- B2/B3 of prior claims are untouched; DeltaE_eff is not re-fit here.
- Status ceiling: Modeled. Absolute scale untouched (FND-MATTER-003).
