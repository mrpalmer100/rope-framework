# FND-STRAND-016 — force-noise spectroscopy: results

Bars: analysis/STRAND016_force_noise_bars_LOCKED.md (blind; instrument,
effective-temperature mapping, cadence, windows, seeds, bracket, thresholds
all fixed first; the FLAT consequence — theory session commissioned — was
committed in advance). Lean archived dataset:
analysis/STRAND016_force_noise_data.json.

## Execution

n = 128 at N = 24 (generators 101..104), ZERO censoring. The falling-hazard
structure reproduces a THIRD time on independent seeds: R_meas = 0.428
(census 0.326, thermometry 0.429).

## B1 — does the dressed drive weaken? FLAT. The last candidate is dead.

V_early = 0.02982, V_late = 0.02980: rho_V = 0.9994 against a 0.90
reduction bar. The dressed-drive intensity is constant to six parts in ten
thousand across the hazard-relevant range — the weave-chain correlations
either do not develop or do not screen the drive at any measurable level.

KILL-VERDICT AUDIT (standing rule, before interpretation): the instrument
reads the FDT-level initialization within 5% of the closed-form value
(theory V(0) = T c0^2 (2/pi) = 0.0312; measured 0.0296, the offset
consistent with the K = 16 band sub-sampling), and its time series is
smooth and self-consistent across all four generators. The instrument
works; the FLAT is real.

## B2 — MOOT by its own clause

Descriptively: the committed mapping predicts R_pred = 0.997 at both
bracket ends against R_meas = 0.428 — the drive channel accounts for
essentially none of the hazard fall, quantitatively mirroring the thermal
kill.

## B3 — early drive vs fate: NOT-TRACEABLE (boundary noted)

rho_drive = -0.1497 (p = 0.092): classified NOT-TRACEABLE by the letter,
sitting AT the 0.15 boundary and reported so. The sign is the trivial one
(larger early kicks, slightly earlier escape) and the effect, if real, is
weak and not significant at n = 128.

## The registered state: MECHANISM-OPEN, and the pre-committed consequence fires

Three sessions, three instruments, one reproducible phenomenon:

- The population hazard falls 2-3x across the distribution (three
  independent seed sets: 0.33, 0.43, 0.43).
- The bath's kinetic temperature is flat to 5e-4 (STRAND-015).
- The dressed-drive intensity is flat to 6e-4 (here).
- Early state — thermal, drive, or energy-covariate — carries no fate
  information beyond a few percent (014, 015, here).

The smallest box's non-exponential escape is now measured to be invisible
to every natural state variable of the noise channel. Per the bars, the
THEORY SESSION is commissioned, with its brief written by the exclusions:
the composite is a DETERMINISTIC, finite-dimensional system; "hazard" and
"aging" are stochastic-process language imported from the Langevin limit,
and the exclusion triangle suggests that language may itself be the error
at N = 24. Candidate framings for the theory session, named without
prejudice: (a) static hidden frailty in the weave's PHASE PATTERN (not its
energy or intensity — a configurational variable the census covariates and
both intensity instruments are blind to by construction); (b) intrinsically
non-exponential first-passage of a quasi-integrable deterministic system
(recurrence-structured escape, where waiting-time tails come from phase-
space geometry, not from state evolution); (c) a genuinely time-dependent
correlation SPECTRUM (the drive's total intensity is flat but its frequency
content reshapes — testable, and the theory session should say whether it
matters before another instrument is built).

## Consequence for Prediction 11, stated with the new honesty

The mechanism-conditional "drift" language of 015 is RETIRED along with its
mechanism. What stands, three-times-replicated and instrument-independent:
small isolated detectors should show NON-EXPONENTIAL dark-count waiting
times (falling population hazard) — and whether an individual detector
DRIFTS or an ensemble shows static rate DIVERSITY is exactly the open
question the theory session must answer, because the two make different
experimental signatures and the engine currently supports either reading.

## Ledger and next-orders

- B1 FLAT (killed; audited); B2 MOOT (kill quantitative); B3
  NOT-TRACEABLE at the boundary (reported); PROMOTION: NO.
- Exclusion triangle complete: temperature, drive intensity, and all
  measured early-state covariates are innocent.
- NEXT-ORDERS: (1) THE THEORY SESSION (commissioned by the bars):
  deterministic finite-N escape — decide between phase-pattern frailty,
  recurrence-structured first-passage, and spectral reshaping; derive the
  discriminating observable BEFORE building another instrument; (2) the
  hazard-shape blind session (may merge into the theory session's
  empirical arm); (3) the {192, 384} asymptote pair, unchanged.
- Status: Modeled. Absolute scale untouched (FND-MATTER-003).
