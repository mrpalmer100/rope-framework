# FND-STRAND-021 — the switch-on session: results

Bars: analysis/STRAND021_switch_on_bars_LOCKED.md (preparation recipe,
generators, estimator, thresholds all fixed first; the Gaussian draw
verified against its variance targets before any trajectory). Data
archived: analysis/STRAND021_switch_on_data.json (n = 128, zero
censoring).

## The experiment

Identical engine, identical operating point — the ONLY change is the
preparation: metastable-well equilibrium (chain phonons thermal in the
linearized well around phi_0 = asin(h); weave in the dressed
shifted-oscillator equilibrium at the drawn chain configuration) instead
of the product state every prior session used.

## Verdicts

B1 — FLATNESS: R_eq = 0.932 (lambda_1 = 5.09e-4, lambda_2 = 4.74e-4),
inside the [0.75, 1.33] CONSTANT window. Against the product-state
ensembles' thrice-replicated 0.33-0.43, the falling hazard is GONE. The
transient was preparation, not physics of the well.

B2 — LEVEL CLOSURE: lambda_eq = 5.46e-4 vs the registered product-state
plateau 4.06e-4 — factor 1.34 against a bar of 2. CLOSED: the plateau the
product-state ensemble decays INTO is the equilibrium rate the
equilibrium ensemble starts AT.

B3 — MEMORYLESSNESS: ln-survival r^2 = 0.956 over [q25, q90]. The
equilibrium ensemble escapes exponentially.

PROMOTED per the committed criterion.

Descriptive corroboration (reported): the equilibrium ensemble is SLOWER
overall (median 1016 vs the product-state 350; mean 1657 vs 1317) — the
product state's early epoch was escape-ENHANCED, exactly as initial slip
requires (transient extra effective forcing while correlations build).

## What is now established

THE PER-CHANNEL SHAPE QUESTION IS ANSWERED: the falling hazard is
PRODUCT-STATE SLIP — the decaying excess forcing a coordinate feels when
switched on uncorrelated with its bath — relaxing into the stationary
Kramers rate whose clock STRAND-010 promoted (attempt rate = the weave
band gap). The two flat instruments (015/016) are explained a second,
deeper way: they measured STATIONARY aggregates, and the slip lives
entirely in the non-stationary correlations those observables integrate
out.

THE COMPOSED PICTURE, closing the whole kinetics program:
- After a quench (product-state start): per-channel hazard = switch-on
  curve decaying to the plateau; aggregate at size N =
  (switch-on curve)^{N/24} by the STRAND-020 law.
- In steady state: pure exponential at the plateau rate, at EVERY size.

PREDICTION 11, final form: dark-count statistics are a TWO-REGIME
statement. After power-up, reset, or sudden isolation, a small detector
shows the non-Poisson switch-on transient for the correlation-building
epoch (and a large one compresses it away per the Poissonization law);
in steady state, all sizes click Poisson at the plateau rate with the
band-gap prefactor. Every clause of that sentence now has a registered,
audited provenance.

## Ledger and next-orders

- B1 CONSTANT, B2 CLOSED, B3 PASS; PROMOTED (Modeled). Zero censoring;
  draw variances verified pre-run.
- The strand-kinetics program (009-021, thirteen claims) is CLOSED at the
  physics level: clock, law, and shape all accounted for.
- REMAINING OPEN (inherited residuals only): the direct per-N saddle
  (STRAND-012; precision on the small-N barrier-relief number); exact-D
  on the 3D instrument (GRV-095). The quantitative slip theory (deriving
  the switch-on curve's analytic form from the coupling spectrum) is
  named as optional polish, not debt.
- Status: Modeled. Absolute scale untouched (FND-MATTER-003).
