# FND-STRAND-015 — survivor thermometry at N = 24: bars locked first

Date: 2026-08-03. Commission: STRAND-014's named next-order, designed to
break the frailty degeneracy with a STATE measurement. The hypothesis under
test (the finite-bath-cools mechanism): the composite starts with all
thermal energy in the weave; as the weave feeds the channel it COOLS; a
cooling bath is a genuinely aging hazard shared by all walkers. The
competing hypothesis (hidden frailty): walkers destined to escape late were
in a distinguishable (colder / less effective) weave state FROM THE START.
The two make opposite predictions about EARLY-TIME state vs fate, and the
same prediction about late-time state — which is exactly what the bars
below exploit.

## The thermometer, defined exactly

T_w(t) per walker := mean over all N x K weave oscillators of p^2 (the
kinetic temperature; equipartition-consistent with the initialization,
where <p^2> = T = 0.40 by construction). Sampled every 10 time units while
the walker is alive (mean-crossing not yet reached); undefined after
escape. No other thermometer may be consulted.

## Design

Engine and operating point: FND-STRAND-008 composite verbatim; N = 24,
h = 0.55, T = 0.40, c0 = 0.35, K = 16, dt = 0.02, window 36000 units.
S = 128 (4 batches of 32; generators seed0 = 91..94, fixed now). Recorded
per walker: t_esc (mean-crossing), the full alive-time T_w series at the
10-unit cadence, archived as npz. Census hazard windows recomputed on THIS
session's escape times (quantiles q25/q50/q90), so the session is
self-contained. Censoring clause: censored walkers reported; > 2% censoring
invalidates the session. Chunked exact-state checkpointing pre-authorized.

## B1 — does the bath cool?

T_early := mean of T_w over all alive walkers and all sample times in
[t_q25, t_q50]; T_late := the same over [t_q50, t_q90].
rho_T := T_late / T_early.
- COOLING: rho_T <= 0.90.
- FLAT: rho_T >= 0.97 — the mechanism is dead on arrival; B2 moot and says
  so; the falling hazard must live elsewhere (registered).
- WEAK: in between — as measured; B2 still evaluated, capped as-measured.

## B2 — quantitative closure: does the cooling PREDICT the hazard fall?

Measured hazard ratio R_meas := lambda[q50,q90] / lambda[q25,q50] on this
session's 128 walkers (STRAND-013 estimator). Predicted from thermometry
via Arrhenius: R_pred(DeltaE) := exp( -DeltaE x (1/T_late - 1/T_early) ),
evaluated at BOTH bracket ends DeltaE in {2.112, 2.634} (the
estimator-flagged bracket from STRAND-010/013, carried as a bracket, not
averaged).
- CLOSED: R_meas within a factor 2 of R_pred for at least one bracket end
  -> the cooling quantitatively accounts for the aging.
- PARTIAL: within a factor 4 -> cooling contributes but does not close;
  the residual is registered.
- OPEN: outside factor 4 -> the mechanism fails quantitatively even if B1
  found cooling; registered at full volume.

## B3 — the frailty break (the session's point)

T0_i := walker i's mean T_w over its first 50 units (all walkers alive
there). Spearman rho_frail between t_esc and T0_i.
- SHARED-AGING SUPPORTED: |rho_frail| < 0.15 — early state does NOT
  predict fate; late escapers were not distinguishable at the start.
- FRAILTY COMPONENT: |rho_frail| >= 0.30 — fate is written in the early
  state after all; the degeneracy resolves TOWARD frailty and the cooling
  story (even if B1/B2 pass) is at most partial. Registered at full
  volume.
- INTERMEDIATE: in between; as measured.

## Promotion criterion, stated in advance

PROMOTE the cooling-bath aging mechanism if and only if: B1 COOLING and
B2 CLOSED and B3 SHARED-AGING SUPPORTED. Any other combination: registered
as measured with the split quantified; the follow-up named by whichever
limb failed. (Clauses checked pairwise this time: the three limbs are
independent measurements and no clause caps another — the STRAND-014
drafting lesson applied.)

## Consequence grammar, fixed now

- If promoted: the aging hazard is a THERMODYNAMIC property of small
  composites (finite bath cools as it works), and Prediction 11 gains the
  drifting-dark-rate signature: small isolated detectors' dark-count rate
  declines over the equilibration time with the Arrhenius of the bath's
  own cooling curve. Registered at Modeled with the absolute-scale caveat.
- If frailty: the smallest box carries state classes the census covariates
  missed but the thermometer sees; the class variable becomes the named
  object.
- If cooling but not closed: a second aging channel exists beyond
  temperature (e.g., spectral reshaping of the weave); the residual is the
  named object.

## Honesty clauses

- Thermometer, cadence, windows, seeds, bracket, and all thresholds fixed
  above; no post-hoc alternatives.
- DeltaE enters only as the registered bracket; this session must not
  re-fit it.
- Status ceiling: Modeled. Absolute scale untouched (FND-MATTER-003).
