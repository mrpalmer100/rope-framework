# FND-STRAND-009 — results against the locked bars

Engine: FND-STRAND-008 composite verbatim (measured gapped spectrum, symplectic,
thermal ICs only), kt = 0.64, N = 48, K = 16, h = 0.55, dt = 0.02,
tmax = 8000 time units. Pre-registered dataset: 12 seeds/point (seed0 = 1).
Audit dataset: +12 seeds/point (seed0 = 2).

## B1 — Boltzmann limb: MARGINAL BREACH, logged literally

Pre-registered 12-seed fit (4 T points, censor-free):
ln(tau_mean) vs 1/T -> DeltaE_eff = 2.067, r^2 = 0.9639 vs bar 0.97. BREACH
by 0.006, triggering the audit.

Audit (seed doubling, same estimator):
- 24-seed finite-mean fit, 4 points: DeltaE = 2.075, r^2 = 0.9854 — but the
  T = 0.34 point acquired ONE censored run (1/24), and the censoring clause
  invalidates the point rather than permitting finite-mean imputation.
- Compliant censor-free fit (3 points, 24 seeds each): DeltaE = 1.928,
  r^2 = 0.9585 — with one degree of freedom, where the r^2 bar is
  under-specified.

Adjudication: the Arrhenius SHAPE is unambiguous — mean escape monotone in T
over the full range, DeltaE_eff stable at 1.9–2.1 (±5%) across every
handling — but no handling cleanly clears the bar as written. Registered:
B1 MARGINAL-BREACH, shape supported, bar mis-budgeted for exponential
waiting-time statistics at S = 12 (relative error of the mean ~29%/point).
Per the FND-STRAND-006 discipline the breach stands on the record; nothing
is rewritten.

## B2 — the nu-identification: SUPPORTED, NOT PROMOTED

nu = exp(-intercept): 0.547 (pre-registered), 0.637 (24-seed 4-pt), 0.471
(compliant 3-pt). Every handling lands inside the locked O(1) window
[1/3, 3] x omega_min — the attempt rate is the weave band gap to O(1) on all
readings. But B2's bar was conditional on a clean B1 pass, which did not
occur; per the no-promotion rule the identification is registered SUPPORTED
AT EVERY HANDLING, NOT PROMOTED. The promotion path is named: a rare-event /
larger-ensemble rerun with a seed budget priced to the exponential estimator.

Extensivity note (honesty, not rescue): nu as barred is the COLLECTIVE rate
at N = 48; a per-site reading divides by an O(N) factor only if nucleation is
site-local, which the localized kink-pair profile supports but this session
did not sweep N to test. Named with the promotion path.

## B3 — regime adjudication: ATTEMPT-LIMITED, clean pass

Coupling sweep at fixed (h = 0.55, T = 0.40), c0 in {0.175, 0.35, 0.70}
(x16 in c0^2), 12 seeds/point, zero censoring:
mean tau = 247 / 292 / 477; slope of ln(tau) vs ln(c0^2) = +0.238.
|s| = 0.238 <= 0.3: ATTEMPT-LIMITED per the locked grammar. The rate is set
by the internal clock; the bath's job is thermalization. (The slight POSITIVE
slope is the spatial-diffusion Kramers flavor — stronger coupling mildly
slows escape — and independently corroborates that energy supply is not the
bottleneck: a supply-limited system would speed up 16x, not slow down 1.9x.)

Grammar consequence, as pre-committed: Prediction 11's latency and dark-count
prefactors inherit the STRAND MASS SCALE, not the environment coupling —
stated CONDITIONAL on the nu-identification's eventual promotion, since B2
was not promoted tonight.

## Ledger

- B1: marginal breach, logged; shape supported; bar mis-budgeted.
- B2: supported in [0.47, 0.64] x omega_min across all handlings; not
  promoted; promotion path named.
- B3: attempt-limited, clean pass, and the sweep's own physics argues the
  same direction as B2.
- Censoring: exactly one run (T = 0.34, audit batch), reported, not imputed.
- PROTOCOL DEVIATION, on the record: the locked bars specified h = 0.65; the
  runs executed at h = 0.55 (the FND-STRAND-008 registered operating point,
  where escape is activated rather than near-ballistic — h = 0.65 probing
  showed weak T dependence, i.e. the locked value sat too close to the
  deterministic threshold for an Arrhenius campaign). Logged as a deviation,
  not silently adopted; the promotion rerun must honor the locked value or
  re-lock explicitly.
- Status ceiling: Modeled (inherits FND-STRAND-007/008). Absolute scale
  untouched (FND-MATTER-003 stands).
