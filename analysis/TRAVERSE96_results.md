# COMMISSION TRAVERSE-96 (SCOUT) -- RESULTS (2026-08-20)

Executed under analysis/TRAVERSE96_bars_LOCKED.md (inheriting
TRAVERSE_bars_LOCKED.md in full). Benchmark:
benchmarks/foundations/traverse96_scout.py, chunk-driven. Verdict
prose written AFTER the run. Outcome: CONTROL (0'') HALT, REGISTERED
AND KEPT -- and the halt, localized by the post-halt diagnostic, is
the scout's finding. No walk was taken; none was needed for the
question the commission asked.

## THE HALT

Control (0'') required the two 64-grid members (the FND-142 endpoint
and the 64-run's accepted step 0) to re-solve at 96 x 36 below the
1e-8 field bar with gamma/Om2/A2 drift under 5e-3. The endpoint
re-solve terminated at a genuine least-squares stationary point
(exact-Newton direction with full line search: no descending step) at
field RMS 2.2e-5, transverse-closure residual 1.9e-2, and drift
gamma 2.0e-2, Om2 5.7e-2, A2 7.4e-2 -- HALT on every gate.

One deviation is registered inside the halted control, with the code
annotation at its site: the locked delta-2 sentence prescribed
re-solving "at their own A2 pins"; at 96 x 36 the a2-pin Jacobian
exhibits the registered near-singularity (the 64-run's own dA2/ds ~
1.5e-5 makes the branch direction near-null to the pin, and the
pinned solve crawled at ~x1.25/round -- the steepening mechanism
reproduced at finer resolution). The re-solve therefore anchored the
branch direction with the commission's own arc instrument at ds = 0
against the interpolated tangent, with A2 moved into the drift gate
at the same 5e-3 -- strictly stronger than the pinned form.

## THE LOCALIZING DIAGNOSTIC (post-halt; the discriminating table)

Three 64-grid branch members, FFT-interpolated and re-solved at
96 x 36 by the same instrument:

  member                64-closure  interp-RMS  converged-to  gamma-drift  Om2-drift
  A2=0.0047 (mild)        1.9e-9      1.4e-3      7.1e-12       7.7e-5      1.4e-4
  A2=0.0103, g=0.558      3.9e-4      1.69        2.5e-4 *      1.8e-2      4.1e-2
  A2=0.0108 (endpoint)    8.3e-3      3.58        2.2e-5 **     2.0e-2      5.7e-2

  * stalled   ** stationary point (no descending exact-Newton step)

The mild member re-solves to machine grade in three rounds, thirty-
fold inside every gate: THE INSTRUMENT IS SOUND. The failure grows
monotonically along the branch, tracking the 64-grid closure residual
-- which is the aliasing measurement: the 64-grid steepened members
satisfied the transverse closure only DISCRETELY, while their
continuous-level (fine-grid) closure violation reaches 8e-3.

## FINDING -- THE 64-GRID STEEPENED MEMBERS ARE RESOLUTION ARTIFACTS
## AT THE SEVERAL-PERCENT LEVEL

On the honest grid, the steepened-regime members (gamma <= 0.558 on
the aligned branch) have no counterparts within the gates: the states
the 64-grid registered in that regime exist BY ALIASING, and their
physical outputs (gamma, Om2, A2) carry 2-7% resolution error. Three
independent corroborations from this scout: the O(1) interpolation
residual against 2e-4 for level-1 and 1.4e-3 for the mild member; the
closure/aliasing gradient in the table; and the reproduction of the
a2-pin near-singularity at the finer resolution.

## RETRO-IMPACT (for the author's adjudication; nothing registered)

1. FND-142's converged-member LIST survives in the mild regime
   (verified here at both resolutions to 1e-4 grade) and its verdict
   (PIN-UNREACHED, Sigma_wave not re-priced, FND-139 rider standing)
   is UNAFFECTED -- it claimed a search failure, which stands.
   Its steepened-regime display quantities inherit the several-
   percent caveat.
2. The 64-grid TRAVERSE findings measured IN the steepened regime --
   the continuation points beyond the endpoint, the dA2/ds = 1.5e-5
   rate and its decay, the "no fold" statement as a quantitative
   record -- are built on contaminated members. The PROPOSED FND-143
   text (never granted, never registered) SHOULD NOT BE GRANTED AS
   WRITTEN. A revised proposal is below.
3. The 64-run's control-(v) halt and its resolution-exhaustion
   diagnosis are STRENGTHENED: the exhaustion begins earlier on the
   branch than that run could see.

## REVISED PROPOSED CLAIM TEXT (author's grant required)

FND-143-r (Modeled): THE STEEPENED REGIME OF THE ALIGNED BRANCH IS
RESOLUTION-LIMITED AT 64 x 24: ITS REGISTERED MEMBERS ARE ALIASING
ARTIFACTS AT THE SEVERAL-PERCENT LEVEL. A tangent-sphere instrument
proven at both resolutions (control-(0) equivalence at 64; mild-
member re-solve at 96 x 36 to 7.1e-12 with 1e-4-grade drift)
demonstrates: (a) mild aligned-branch members are resolution-
converged; (b) steepened members (gamma <= 0.558) fail their fine-
grid re-solve with monotonically growing drift (to 2-7% in
gamma/Om2/A2) tracking their continuous-level transverse-closure
violation (to 8e-3), terminating in a least-squares stationary point
with no descending exact-Newton direction; (c) the a2-pin
near-singularity of the steepened regime reproduces at 96 x 36. The
steepening's quantitative record, including all rates measured past
gamma = 0.558 at 64 x 24, is superseded-not-erased pending a native
fine-grid continuation from the verified mild territory. Sigma_wave
remains un-re-priced; the FND-139 rider stands. Benchmarks:
traverse_steepened.py, traverse96_scout.py; bars:
TRAVERSE_bars_LOCKED.md, TRAVERSE96_bars_LOCKED.md.

## THE SUCCESSOR (chartered here, not begun)

NATIVE-96 CONTINUATION: re-run the aligned-branch continuation
natively at 96 x 36 from level-1 (not by interpolation of 64-grid
members), through the mild regime (cross-checking the verified
members) and INTO the steepened regime, with the closure residual
promoted to a HALT-grade tail bar so aliasing cannot silently carry
the branch again. The full solver ladder for n = 10370 on modest
memory is built and annotated in traverse96_scout.py (loose float32
LM -> f64 dsyrk-GN -> exact-GN line search; the dtype-promotion tax,
the kappa^2 float32 floor, the near-null period-2 and its damping
floor, and the graded-spectrum Krylov failure are all on the record
with measurements). This is a CI-scale run; every piece transfers.
