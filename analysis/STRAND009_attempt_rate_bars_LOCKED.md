# FND-STRAND-009 — THE ATTEMPT RATE'S PROVENANCE: bars locked before computation

Date: 2026-08-03. Session commissioned from the standing queue (GRV-094; the
"weave-as-reservoir" residual named at QB-033 and FND-STRAND-006 as the last
generic ingredient of the measurement chain).

## The question

FND-STRAND-007/008 derived the bath: a gapped weave reservoir (omega_min = 1,
band top sqrt(1 + 4 kt)), deterministic and energy-conserving, whose only
stochastic element is a temperature. FND-STRAND-006 measured Arrhenius escape
in the channel energy. What no session has asked: WHO SETS THE PREFACTOR? The
Kramers form tau = nu^-1 exp(DeltaE_eff / T) has an attempt rate nu, and the
gapped-band structure makes a specific identification available: the weave has
no mode below the strand mass scale, so the natural attempt clock is the band
gap itself, nu = O(1) x omega_min. If true, Prediction 10's structural shape
(the gapped floor) acquires a KINETIC corollary (dark-count prefactors pinned
at the strand mass scale, feeding Prediction 11). If false, the prefactor's
provenance must be named.

Engine: the registered FND-STRAND-008 composite exactly (measured gapped
spectrum, symplectic, no injected noise; thermal initial conditions only),
kt = 0.64, coupling scale c0 = 0.35 as registered.

## B1 — the Boltzmann limb (the exponential earns its name)

At fixed drive h = 0.65, sweep T over >= 4 values spanning at least a factor
1.8. Fit ln(tau_mean) vs 1/T (>= 6 seeds per point; seeds fixed in the
benchmark before running).

- PASS: linear with r^2 >= 0.97. The slope IS DeltaE_eff (measured, not
  assumed).
- FAIL: r^2 < 0.97 -> the escape is not single-barrier Arrhenius in T on this
  composite; register the shape as found, NO prefactor extraction is valid,
  B2 is moot and says so.

## B2 — the nu-identification (pre-committed before any fit is run)

From B1's fit, nu := exp(-intercept), i.e. tau = nu^-1 exp(DeltaE_eff/T),
angular-frequency units of the engine (omega_min = 1 exactly, measured).

- PASS (identification holds): nu in [1/3, 3] x omega_min. Registered as: the
  attempt rate is the weave band gap to O(1) — the gapped bath supplies its
  own clock.
- FAIL (identification refuted): nu outside [1/3, 3]. Registered as: the
  attempt rate is NOT the gap; the measured value stands in the registry and
  its provenance (band top? coupling? collective mode?) becomes the named
  next-order. No rescue by re-fitting.

The O(1)-Boltzmann check, jointly: B1 pass AND B2 pass means the full Kramers
grammar tau = O(1) x omega_min^-1 x exp(DeltaE/T) holds on a bath the corpus
DERIVED rather than postulated.

## B3 — supply-limited vs attempt-limited (both grammars fixed now)

At fixed (h = 0.65, T = 0.4), sweep the coupling scale c0 over {0.175, 0.35,
0.70} (factor 16 in c0^2). Fit slope s of ln(tau_mean) vs ln(c0^2).

- ATTEMPT-LIMITED verdict: |s| <= 0.3. Grammar: the bath's job is
  thermalization only; the rate is set by the internal clock (consistent with
  B2's identification if it passed). Consequence: Prediction 11's latency and
  dark-count prefactors inherit the STRAND MASS SCALE, not the environment
  coupling — a sharpened, testable commitment.
- SUPPLY-LIMITED verdict: s <= -0.7. Grammar: the rate is throttled by energy
  delivery from the gapped band (energy-diffusion Kramers regime). The
  nu-identification, even if B2 numerically passed, is DEMOTED to coincidence
  at the registered c0; the prefactor belongs to the coupling and Prediction
  11's kinetic package inherits an environment dependence that must be stated
  in the predictions paper.
- NEITHER (-0.7 < s < -0.3): register UNRESOLVED-INTERMEDIATE as measured;
  no promotion of either grammar; the turnover location becomes the named
  next-order. No third-option softening of the two grammars above.

## Honesty clauses

- The engine's units are model units; nothing here touches the absolute scale
  (FND-MATTER-003 stands).
- tau_mean over censored runs (no escape within tmax) is invalid; any censored
  point at the fitted (h, T, c0) invalidates that point and is reported, not
  imputed.
- Status ceiling: Modeled (inherits FND-STRAND-007/008).
- Kill-verdict on any bar triggers the standing audit rule before any
  interpretation is written.
