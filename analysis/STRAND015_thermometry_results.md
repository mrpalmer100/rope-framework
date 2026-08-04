# FND-STRAND-015 — survivor thermometry: results

Bars: analysis/STRAND015_thermometry_bars_LOCKED.md (blind: thermometer,
cadence, windows, seeds, bracket, thresholds all fixed first; clauses
checked pairwise per the STRAND-014 lesson). Lean archived dataset:
analysis/STRAND015_thermometry_data.json (128 walkers: escape times,
early-state T0, pooled cooling curve, window means).

## Execution

N = 24, 4 batches (seed0 = 91..94), n = 128, ZERO censoring. Escape
statistics reproduce the census (median 366 vs 350; hazard ratio 0.429 vs
0.326 — same falling-hazard structure, independent seeds).

## B1 — does the bath cool? FLAT. The mechanism is dead on arrival.

T_early = 0.3837, T_late = 0.3835: rho_T = 0.9995 against a COOLING bar of
0.90. The weave's kinetic temperature over the entire hazard-relevant range
is constant to five parts in ten thousand.

KILL-VERDICT AUDIT (standing rule, run before interpretation): the
thermometer reads the initialization exactly (T_w(0) = 0.3990 vs 0.400
built in), resolves the genuine early equilibration dip (0.399 -> 0.386
within the first 100 units as the weave dresses the cold channel — a 3.5%
effect cleanly measured), and then reads flat drift of only ~0.2% per
several thousand units. The instrument works; the FLAT verdict is real.
The finite bath does NOT meaningfully cool at this size and coupling: the
channel's energy uptake (~one barrier's worth) is small against the weave's
total thermal budget (N x K modes), and the arithmetic agrees.

## B2 — MOOT, per the locked grammar (descriptives reported)

With B1 FLAT, B2 is moot by its own clause. The descriptive numbers make
the kill quantitative: the measured temperature difference predicts
R_pred = 0.998 (both bracket ends of DeltaE), against R_meas = 0.429 — the
thermal channel accounts for essentially NONE of the hazard fall.

## B3 — the frailty break: SHARED-AGING SUPPORTED

rho_frail = -0.051 (p = 0.57): a walker's early thermal state carries NO
information about its fate. Frailty-along-early-kinetic-temperature is
excluded at the committed threshold. (Hidden frailty in other state
variables remains logically open — the grammar committed to this
covariate, and says so.)

## The finding: NON-THERMAL AGING

Assembling the three limbs: the hazard falls 2-3x (twice measured,
independent seed sets) while the bath's kinetic temperature is flat to
0.05% and the early thermal state carries no fate information. The aging
is real and it is NOT thermodynamic cooling and NOT early-thermal
frailty. Per the pre-committed consequence grammar, a second aging channel
beyond temperature must exist, and the physics points at a specific one:
the DRESSED DRIVE. The force the weave exerts on the chain is
sum_k c_k (q - c phi / omega^2); its variance is set not by the kinetic
temperature alone but by the weave-chain CORRELATIONS, which start at zero
(independent draw) and develop as the composite couples. A weave that
becomes correlated with the chain it drives can deliver less effective
noise at CONSTANT kinetic temperature — aging by spectral reshaping, not
by cooling.

## Consequence for Prediction 11, sharpened by the kill

The drifting-dark-rate signature SURVIVES and becomes more distinctive:
small isolated detectors should show dark-count rates that decline over an
equilibration time WHILE the bath temperature holds constant — a
correlation-driven drift that no thermal-drift model reproduces. An
experimenter who measures both the click rate and the stage temperature
and finds the first falling with the second flat is seeing exactly this
engine's behavior.

## Ledger and next-orders

- B1 FLAT (mechanism killed; audit confirms the instrument); B2 MOOT with
  the kill made quantitative; B3 SHARED-AGING SUPPORTED; PROMOTION: NO,
  by the pre-committed criterion.
- The census arc's score so far: cooling killed, early-thermal frailty
  excluded, measured-covariate frailty excluded (014) — the aging is
  non-thermal and the dressed drive is the named suspect.
- NEXT-ORDERS: (1) FORCE-NOISE SPECTROSCOPY — track the variance of the
  dressed drive along trajectories (the same census design, thermometer
  replaced by the force-variance instrument, one level closer to the
  escape coordinate); (2) the hazard-shape blind session, unchanged;
  (3) the {192, 384} asymptote pair, unchanged.
- Status: Modeled. Absolute scale untouched (FND-MATTER-003).
