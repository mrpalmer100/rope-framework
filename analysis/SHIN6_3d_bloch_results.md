# COMMISSION SHIN6 -- RESULTS (2026-08-12)

Executed under analysis/SHIN6_3d_bloch_bars_LOCKED.md (four addenda,
each disclosed before the run it governed).

## Instrument history, on the record
1. First parameterization (lambda = 6): lock error -- SHIN4's
   validated regime is lambda = 24; plus lattice aliasing (f and 1-f
   identical on integer sites). INSTRUMENT-PARAMETERIZATION-INVALID.
2. Projector engine: violates the acoustic sum rule (spurious k->0
   gap, straight control mean v = 3.42x, zero group speeds).
   INSTRUMENT-INVALID at its own control, taken not tuned.
3. Central-spring engine, uncalibrated: the ISOTROPIC NULL medium
   returns spread 0.206 / split 0.202 -- above the bars: raw B2/B5
   unpassable in principle (cubic Cauchy artifact). Calibration on
   the null only lands g = 2 EXACTLY (closed-form NN/NNN isotropy
   condition, not a fit): null spread 0.0014, split 0.0000. Frozen.
4. Fourth-moment sampling: >= 5 phases per level required to express
   FND-088's isotropy; P = 5 realizes the derived orientation tensor
   to machine zero; adjudicating member f = 1/5.

## Verdict (calibrated engine, derived angles, no free parameters)
CTRL straight: spread 0.816, split 0.917, angles to 89.9 deg --
obstruction fully visible, instrument VALID.
Adjudicating member f = 1/5 (p = lambda/5):
  B1 min group speed 0.791 (bar 0.3)   PASS
  B2 phase spread 0.0476 (bar 0.05)    PASS (thin margin, disclosed)
  B3 max group angle 3.3 deg (bar 15)  PASS
  B4 min pw weight 0.86 (bar 0.5)      PASS
  B5 max pol split 0.0330 (bar 0.05)   PASS
Context members f = 1/3, 1/4 (aliased 4th moment) pass B2 marginally
and B5 within bar as well after calibration; reported, not leaned on.
PASS. Debt 3 of GRANT-SUBSTRUCTURE-TIGHT discharged: the 3D
two-polarization check exists, is validated at three controls
(straight, isotropic null, sampling), and the wound medium at the
DERIVED angles carries both polarizations isotropically.
Benchmark: benchmarks/foundations/shin6_3d_bloch.py
