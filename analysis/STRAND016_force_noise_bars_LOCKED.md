# FND-STRAND-016 — force-noise spectroscopy at N = 24: bars locked first

Date: 2026-08-03. Commission: STRAND-015's named next-order. The surviving
suspect for the non-thermal aging is the DRESSED DRIVE: the force the chain
feels, f_n(t) = sum_k c_k (q_nk - c_k phi_n / omega_k^2), whose variance is
set by weave-chain correlations that the initialization zeroes by
construction. If the dynamics build those correlations, the effective noise
falls at constant kinetic temperature. This session measures that force
directly. If THIS instrument also reads flat, the last natural candidate is
dead and the smallest box earns a theory session — that consequence is
committed now, in advance.

## The instrument, defined exactly

V(t) per walker := mean over the N sites of f_n(t)^2, with f_n as above —
the instantaneous dressed-drive intensity. Sampled every 10 units while the
walker is alive; undefined after escape. V0_i := walker i's mean V over its
first 50 units. Effective-temperature mapping, committed now and not
tunable later: T_eff(window) := T x V(window) / V0_pool, where T = 0.40 and
V0_pool is the pooled early reference (mean V over all walkers, t <= 50).
No other instrument or mapping may be consulted.

## Design

Engine and operating point identical to STRAND-015: N = 24, h = 0.55,
T = 0.40, c0 = 0.35, K = 16, dt = 0.02, window 36000 units. S = 128
(4 batches; generators seed0 = 101..104, fixed now). Recorded per walker:
t_esc, the alive-time V series at the 10-unit cadence, V0_i. Hazard windows
from THIS session's escape quantiles (q25/q50/q90). Censoring clause:
> 2% censoring invalidates the session. Chunked checkpointing
pre-authorized.

## B1 — does the dressed drive weaken?

V_early := pooled mean of V over alive walkers in [t_q25, t_q50]; V_late
over [t_q50, t_q90]. rho_V := V_late / V_early.
- REDUCTION: rho_V <= 0.90.
- FLAT: rho_V >= 0.97 — the mechanism is killed; B2 moot and says so; the
  pre-committed consequence fires: the smallest box is registered
  MECHANISM-OPEN and the theory session (analytic treatment of the coupled
  escape process at few-kink-width rings) is commissioned.
- WEAK: between — as measured; B2 evaluated, capped as-measured.

## B2 — quantitative closure through the committed mapping

R_meas := lambda[q50,q90]/lambda[q25,q50] on this session's walkers
(STRAND-013 estimator). T_eff_early := T x V_early/V0_pool; T_eff_late :=
T x V_late/V0_pool. R_pred(DeltaE) := exp(-DeltaE x (1/T_eff_late -
1/T_eff_early)), evaluated at both bracket ends DeltaE in {2.112, 2.634}.
- CLOSED: R_meas within factor 2 of R_pred at either bracket end.
- PARTIAL: within factor 4.
- OPEN: outside factor 4 — reduction without quantitative closure; the
  residual channel is registered and named.

## B3 — the early-drive/fate coupling (character, not gate)

Spearman rho_drive between t_esc and V0_i.
- TRACEABLE: |rho_drive| >= 0.30 — the early drive intensity carries fate
  information (whether as trivial early-kick causation or as seeded
  reshaping is for the results file to argue from the sign and the curve,
  not for this bar to prejudge).
- NOT-TRACEABLE: |rho_drive| < 0.15 — the reshaping is shared; fate is not
  written in the early drive.
- INTERMEDIATE: between; as measured.
B3 informs the MECHANISM'S CHARACTER and does not gate promotion —
stated here so no clause caps another (pairwise consistency, the
STRAND-014 lesson).

## Promotion criterion

PROMOTE the dressed-drive aging mechanism iff B1 REDUCTION and B2 CLOSED.
Any other combination: as measured, with the follow-up named by the
failing limb. Consequence grammar if promoted: the aging hazard is a
CORRELATION-DYNAMICS property of small composites; Prediction 11's
flat-temperature dark-count drift acquires its mechanism (drive screening
by developed correlations), registered at Modeled with the absolute-scale
caveat.

## Honesty clauses

- Instrument, mapping, cadence, windows, seeds, bracket, thresholds: fixed
  above. DeltaE enters only as the registered bracket; not re-fit here.
- The 015 kill is not relitigated: kinetic temperature is settled flat;
  this session measures a different observable.
- Status ceiling: Modeled. Absolute scale untouched (FND-MATTER-003).
