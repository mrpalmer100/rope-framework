# COMMISSION NATIVE-96 -- THE NATIVE FINE-GRID CONTINUATION -- BARS (LOCKED)

*Locked 2026-08-20 before computing, on the author's instruction
("Let's run it"), from the draft below with ZERO amendments; the
draft is preserved as analysis/NATIVE96_bars_DRAFT.md. The FND-143
grant was issued in the same instruction and the claim is registered
(v3.27.3) before this run's first computation.
Successor chartered in analysis/TRAVERSE96_results.md. Inherits
analysis/TRAVERSE_bars_LOCKED.md in FULL -- equations, tangent-sphere
chart, pins, gauge, cell and rationalization, pseudo-arclength path,
clean room, and outcome sheet -- with only the deltas below. Inherits
NOTHING from the 64 x 24 branch data: no member of the 64-grid path
seeds, pins, or targets any part of this run.*

## THE DIAGNOSIS THIS COMMISSION ANSWERS

TRAVERSE-96 (SCOUT) measured that the 64 x 24 steepened-regime members
are aliasing artifacts at the 2-7% level, and localized the mechanism:
their CONTINUOUS-LEVEL transverse closure violation reaches 8e-3 while
their own-grid field RMS sat under the 1e-8 acceptance bar. The
acceptance bar never saw it, because control (v) printed the closure
residuals and did not gate on them. The scout's own diagnostic table
makes the point sharply: own-grid closure 1.9e-9 on the mild member,
3.9e-4 at gamma = 0.558, 8.3e-3 at the endpoint. THE TELL WAS ON THE
FACE OF EVERY ACCEPTED POINT AND WAS NOT A BAR. That is the single
structural change here.

## DELTAS FROM THE INHERITED BARS

1. GRID: 96 x 36 throughout and NATIVE. Level-1 is constructed in
   closed form at 96 x 36; the A2 ramp, the tangent, and the walk all
   run on that grid. FFT interpolation of 64-grid states appears
   NOWHERE in the path. Level-1 discrete values shift with the grid;
   control (i)'s value bars stay at 1e-3 and its constancy bar at
   1e-6, both inherited unchanged.

2. CONTROL (v) IS PROMOTED FROM PRINTED TO HALT-GRADE (the charter
   item). At EVERY accepted point: max |transverse closure| and
   max |axial closure| < 1e-6, evaluated UNWEIGHTED on the same
   residual vector as bar (ii). HALT if exceeded, with the last
   clean member registered. Rationale for the value, on the face: the
   mild converged member measures 1.9e-9, so 1e-6 carries roughly
   500x headroom against a correct solve while firing three orders
   before the contamination the scout measured. This bar, applied to
   the 64 x 24 run, would have halted it at member 5.

3. CONTROL (0) IS NOT AVAILABLE AND IS REPLACED BY (0*), THE MILD-
   REGIME CROSS-CHECK. There is no 64-grid re-solve in a native run,
   so representation equivalence is demonstrated instead against the
   REGISTERED FND-142 members at the shared A2 pins of the converged
   ramp (RAMP_CONV = [0.02, 0.05, 0.10] x R2), regenerated inside
   this run by stage 2's OWN code at 64 x 24. Bar: gamma and Om2
   agree within 5e-3 RELATIVE. This is a resolution-consistency bar,
   not an equivalence bar, and it is looser than control (0)'s 1e-6
   for the reason TRAVERSE-96 stated: two grids are two instruments
   and the drift is itself a measurement. The scout measured
   1e-4-grade drift in this regime, so 5e-3 fires only on real
   trouble. HALT. Without (0*) nothing else in the run is reportable.

4. TAIL DIAGNOSTIC AND ITS TRIGGER. The s-Nyquist amplitude of w_s
   (already printed by the inherited reporter) is recorded at every
   accepted point as a trajectory. It is NOT a halt bar. If it rises
   above 1e-8, or if closure crosses 1e-8 while still under the
   halt bar, the run performs the CROSS-RESOLUTION CONFIRMATION: the
   current member is FFT-interpolated to 112 x 42 and re-solved, and
   gamma / Om2 / A2 drift must stay under 5e-3. HALT if exceeded.
   112 x 42 rather than 128 x 48 for a stated instrument reason, not
   a physics one: at n = 14114 the dense float64 normal matrix is
   1.59 GB and the float32 Jacobian 0.80 GB, which fits the 3 GB
   container with the scout's memory ladder; 128 x 48 (n = 18434)
   does not fit and would have to be run on CI.

5. SOLVER: the TRAVERSE-96 ladder imported verbatim from
   benchmarks/foundations/traverse96_scout.py (float32 Jacobian store,
   float64 criteria, damped GN with the measured damping floor, f64
   dsyrk normal equations in the endgame, exact-GN with line search at
   the bottom, x_scale = 1). No solver change is proposed. Every
   forcing incident is annotated in place, as before.

6. BUDGET AS A FIRST-CLASS OUTCOME (inherited from TRAVERSE-96 delta
   4, restated). The walk proceeds until (a) a bars halt, or (b) the
   session budget ends, in which case the registered content is the
   MEASURED TRAJECTORIES -- A2(s), gamma(s), Om2(s), min z'(s),
   closure(s), Nyquist(s) -- with the walk resumable from its
   checkpoint. Outcome (b) is reported as RATES-REGISTERED, not as
   failure.

7. Everything else -- pins, gauge, arc geometry (ds cap 0.08, growth
   1.2, floor 1e-4), acceptance field RMS < 1e-8, chart-validity floor
   min sin theta > 0.05, the W0 resonance margin printed, min z'
   printed with sign, inextensibility printed as a tautology and not
   as evidence, clean room, outcome sheet -- inherited verbatim.

## WHAT THIS COMMISSION IS ALLOWED TO CONCLUDE

The question is the one the 64 x 24 halt left and the scout could not
answer without a walk: past the mild regime, does dA2/ds continue to
decay (asymptote, and the registered R2 = 0.09396 is unreachable on
this family at q = 3/2) or recover (transition, and the pin is live)?
A run that halts on the closure bar early answers NEITHER and must say
so: it registers the reachable extent of the honest branch and the
resolution at which the next attempt must start. The steepening rates
measured past gamma = 0.558 at 64 x 24 are superseded-not-erased and
are NOT a comparison target for this run; the clean room extends to
them.

## COST NOTE (measured, not a bar)

Calibrated in this container before drafting (instrument timing only,
no physics evaluated): at 96 x 36, n = 10370 and m = 10481. One
residual 8 ms; one forward-difference Jacobian ~30 s; the f64 dsyrk
normal equations ~16 s; the Cholesky ~20 s. A full exact-GN round is
therefore ~70 s on this one core, and a converged member is ~15-30
minutes. Level-1 plus the five-pin ramp is a few hours of chunked
wall time before the walk begins. This is chunk-scale in-session work
with --budget resumption, not the CI-only run the scout assumed.
