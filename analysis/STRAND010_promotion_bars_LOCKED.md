# FND-STRAND-010 — the promotion rerun: bars locked before computation

Date: 2026-08-03. Commission: FND-STRAND-009's named next-order. Purpose:
promote (or refuse to promote) the nu-identification on a run whose bar is
priced to its own estimator and whose drive value is adjudicated rather than
deviated.

## The two open items, adjudicated NOW, before any run

H-ADJUDICATION (the STRAND-009 deviation discharged by re-lock, not by
pardon): the promotion runs at h = 0.55. Rationale on the record: the
original lock at h = 0.65 was made before the probing that showed escape
there is near-ballistic (mean tau ~25-30 across T = 0.28-0.46, no Arrhenius
regime to measure); h = 0.55 is the FND-STRAND-008 registered operating
point and sits in the activated regime. This is a RE-LOCK: the value is
fixed here, in advance, and a deviation from it in the runs below would be
a fresh violation, not a continuation of the old one.

SEED-BUDGET PRICING (the STRAND-009 lesson executed): for exponential
waiting times, the sample mean of S runs has relative error 1/sqrt(S), so
the per-point scatter of ln(tau_mean) is ~1/sqrt(S). With four T points at
{0.34, 0.40, 0.47, 0.56} and DeltaE_eff ~ 2 (STRAND-009's measured value),
the fit ordinate spans ~2.3 and carries variance ~0.74. Expected
r^2 ~ 1 - (1/S)/0.74: S = 48 prices to 0.972 (no margin); S = 64 prices to
0.979. THE BUDGET IS S = 64 PER POINT, fixed here. If the bar fails at a
budget priced to pass it with margin, the failure is informative about the
physics (non-Arrhenius shape), not the statistics — which is exactly what
a bar is for.

## The runs

Engine: FND-STRAND-008 composite verbatim (measured gapped spectrum,
symplectic, thermal ICs only), kt = 0.64, N = 48, K = 16, c0 = 0.35,
dt = 0.02. h = 0.55 (re-locked above). T in {0.34, 0.40, 0.47, 0.56}.
S = 64 seeds/point, generators seed0 in {11, 12} at S = 32 each, fixed here.
tmax = 12000 time units (600k steps), raised from STRAND-009's 8000
specifically to retire the censoring exposure at T = 0.34.

## B1' — the Boltzmann limb, same bar, priced budget

Fit ln(tau_mean) vs 1/T over the four points.
- PASS: r^2 >= 0.97 (unchanged threshold — the point of the pricing is to
  reuse the bar honestly, not to soften it).
- FAIL: r^2 < 0.97 at S = 64 -> the shape itself is in question; register
  the measured curvature, NO promotion, and the named next-order becomes
  the functional form (finite-barrier corrections), not more seeds.
- Censoring clause unchanged: any censored run invalidates its point; three
  valid points are insufficient for this bar (pre-stated this time) and
  yield NO-PROMOTION with the censoring reported.

## B2' — the nu-identification, promotion criterion

nu := exp(-intercept) from B1's fit, angular units (omega_min = 1).
- PROMOTE: B1' passes AND nu in [1/3, 3]. Registered as: the attempt rate
  IS the weave band gap to O(1) — promoted from supported to measured, and
  Prediction 11's prefactor corollary (dark-count/latency prefactors at the
  strand mass scale) loses its conditional.
- REFUSE: either limb fails. The supported-not-promoted status of
  FND-STRAND-009 stands unchanged; whichever limb failed names the
  next-order. No third outcome.

## Honesty clauses

- B3 (attempt-limited) is NOT rerun; its clean pass stands and is not
  retroactively strengthened by this session.
- The N-sweep (collective vs per-site nu) is explicitly OUT OF SCOPE here
  and remains a named open item regardless of outcome.
- Units are model units; the absolute scale is untouched (FND-MATTER-003).
- Status ceiling: Modeled (inherits FND-STRAND-007/008/009).
