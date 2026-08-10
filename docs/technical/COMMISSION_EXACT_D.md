# COMMISSION: THE EXACT-D EXTRACTION

Charter written before computation. Bars locked at sign-off; no bar may be
widened after the first compute. Operator: Mark Palmer. Computational
collaborator: Claude (Anthropic). Drafted 2026-08-09.

## Standing

GRV-095 names this as the thread's live precision task: "the exact-D
extraction on GRV-024/025's three-dimensional instrument (refines a within
its last factor of ten -- precision now, not decision)." The instrument is
the absorption exam (benchmarks/gravity/absorption_test.py, GRV-024,
Derived) and its verdict (benchmarks/gravity/absorption_verdict.py,
GRV-025, Derived): the m-odd, IR-universal, regulator-independent part of
the weave band's induced q^2 action is Einstein-Hilbert in pattern,
validated against exact diagonalization at 0.5%, with the EH-pattern bars
at 20%.

What this commission adds: the pattern verdict becomes a NUMBER. D is the
dimensionless coefficient of the IR-universal EH remainder in the induced
tension zeta D hbar c / a^2 (GRV-095). Extracting D in the continuum limit
with quantified error, then substituting once (the one-power theorem,
GRV-094: A* and n_q carry exactly a^1), refines the spacing a within its
final factor of ten and tightens the ring-quantum arc's endpoints,
including the Hawking-form coefficient's final bracketed value.

## Objective

Extract D from the GRV-024/025 instrument: continuum-extrapolated, with a
stated numerical uncertainty, and demonstrated IR-universal. Propagate the
number through GRV-095's substitution. Target status for the resulting
claim: Modeled (a measured extraction with error bars); Derived only if a
closed form emerges and survives the same bars.

## Plan

- P1 (integrity): run the existing GRV-024 and GRV-025 benchmarks
  unmodified and record PASS before touching anything.
- P2 (extraction): finite-size sweep in lattice size M beyond the verdict's
  grid; extract the EH-remainder coefficient per M; extrapolate to
  continuum (polynomial in 1/M; Richardson as cross-check).
- P3 (universality): repeat the extraction across a mass-regulator sweep
  (m^2 over at least one decade) and any epsilon/regulator freedom the
  instrument exposes; the IR-universal part's coefficient must not move
  beyond bar B3.
- P4 (propagation): substitute D into zeta D hbar c / a^2; restate a and
  the ring-quantum arc's dependent brackets (A*, n_q, the coefficient's
  final bracket) via the one-power theorem. One substitution, no retuning.
- P5 (pre-installed second check): the refined a must land consistent with
  the standing cross-sector bounds it never saw during extraction --
  ELEC-057's two-sector strand-scale clash window and NUCQ-002's inherited
  n_t. Consistency is a free second prediction; inconsistency is a
  registrable finding, not a tuning license.

## Pre-committed bars

- B1 (integrity): GRV-024 and GRV-025 benchmarks PASS unmodified before
  any new computation. Hard gate.
- B2 (convergence): the extrapolated D is stable -- the largest-grid value
  and the continuum extrapolation differ by < 5%, with a monotone
  finite-size tail over the final three grid sizes.
- B3 (universality): D moves by < 10% across the full regulator sweep
  (m-odd part only, per the instrument's own decomposition).
- B4 (refinement): the propagated a-window narrows by at least a factor of
  3 relative to its current final factor of ten. If the extraction
  converges but the window narrows less, register "converged, refinement
  short of target" with the number anyway.
- B5 (cross-sector): the P5 consistency check is computed and registered
  whichever way it lands.

## Kill and honesty conditions

- Non-convergence (B2 fails): register the failure with the finite-size
  data and the diagnosis. The instrument's pattern verdict (GRV-025) is
  NOT thereby impugned; the failure attaches to the extraction only.
- Regulator dependence (B3 fails): register as "the coefficient is not
  IR-universal at extraction precision" -- a finding about the
  decomposition's reach, kept at full strength.
- No bar widening, no post-hoc grid selection, no dropping of regulator
  points after first compute. Every computed number enters the record.

## Deliverables

The extraction script (benchmarks/gravity/exact_d_extraction.py) with
deterministic seeds; a registered claim (proposed ID GRV-096) carrying the
number, the bars' outcomes, and the propagation; document propagation per
the standing queue; release cut at the operator's preference.

## Sign-off

Bars lock at the operator's GO. Execution begins only after.

## OUTCOME (registered 2026-08-09, GRV-096, Failed and kept)

Executed same day as sign-off. B1 PASSED (instrument reproduces GRV-025's
+286.8 at M=96 exactly). B2 PASSED at fixed protocol: D_lat monotone over
M = 48..160, extrapolating to 3.179e-4 at 0.9% deviation, Richardson
agreeing at 0.5%. B3 FAILED: mass-window shifts move the amplitude
12-29%, basis augmentation 51-57%, against the locked 10% bar. Diagnosis:
m and m^3 near-collinear over the instrument's mass window; the m-linear
IR amplitude is not separable at extraction precision. The pattern
verdict (GRV-025) is unaffected. B4/B5 not reached, gated per charter.
No bar was widened; no protocol was added after the bars fired. Named
next-order: an ordered-limit (scaling-window, m tied to q) extraction,
to be chartered separately. Benchmark: benchmarks/gravity/exact_d_extraction.py.
