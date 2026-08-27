# COMMISSION TRAVERSE-96 (SCOUT) -- BARS (LOCKED)

*Locked 2026-08-20 before computing, on the author's instruction.
Successor to COMMISSION TRAVERSE; inherits analysis/
TRAVERSE_bars_LOCKED.md in FULL -- equations, chart, pins, gauge,
pseudo-arclength path, controls (0)-(ix), clean room, and outcome
sheet -- with only the deltas below. The 64 x 24 run registered its
halt by control (v): resolution exhaustion, chart healthy. This
commission asks the ONE question that halt left: with resolution
96 x 36 FROM THE START, does the closure/Nyquist tail stay controlled
past the old halt point, and does dA2/ds continue to decay (asymptote)
or recover (transition)?*

## DELTAS FROM THE INHERITED BARS

1. GRID: 96 x 36 throughout. Level-1 discrete values shift accordingly
   (control (i) value bars unchanged at 1e-3; the constancy bar 1e-6
   unchanged).
2. SEED: the 64 x 24 run's accepted step-0 member (arc +0.020, RMS
   7.57e-9) and its seed (the c0-re-solved FND-142 endpoint),
   FFT-interpolated to 96 x 36 and re-solved at their own A2 pins.
   CONTROL (0''): both re-solves must land < 1e-8 field RMS with
   Om2 and gamma within 5e-3 RELATIVE of the 64-grid values --
   a resolution-consistency bar, looser than control (0)'s 1e-6
   because the two grids are DIFFERENT instruments and the drift IS
   a measurement (it doubles as the inherited tail control (iv),
   applied at the frontier instead of at R2). HALT if exceeded.
3. SOLVER (instrument, on the face): Jacobian stored in float32 to fit
   the container (dense float64 at 96 x 36 is ~870 MB and risks the
   OOM reaper). Forward-difference J error (~1e-7 relative) already
   exceeds float32 quantization; the step and convergence CRITERIA
   remain float64, and the acceptance bar (ii) is evaluated on the
   float64 residual. x_scale = 1 (measured equivalent at 64 x 24).
4. BUDGET AS A FIRST-CLASS OUTCOME: this is a SCOUT on a shared
   container. The walk proceeds until (a) a bars halt, or (b) the
   session budget ends -- in which case the registered content is the
   MEASURED RATES: dA2/ds trajectory, closure/Nyquist tail trajectory,
   and min z' trajectory at 96 x 36, with the walk resumable from its
   checkpoint on CI. Outcome (b) is reported as SCOUT-RATES-REGISTERED,
   not as failure.
5. Everything else -- pins, gauge, arc geometry (ds cap 0.08, growth
   1.2), acceptance RMS < 1e-8, controls printed per accepted point,
   clean room, outcome sheet -- inherited verbatim.
