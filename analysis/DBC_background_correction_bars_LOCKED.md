# COMMISSION DBC -- THE DYNAMICAL-BACKGROUND CORRECTION -- BARS (LOCKED)

*Locked 2026-08-18, before any result leg is computed. Session opened as
the v3.26.77 handoff's designated one job: BLOCH-L's anchors (and
therefore the standing kb bound) were computed on a STATIC winding; the
rotating-wave background's corrections are the named gap on the fine
sector's sharpest number. Instrument: FND-089-class supercell Bloch
machinery, exactly as built in benchmarks/foundations/blochl_longitudinal.py.*

## SCOPE

The question, precisely: does the registered rotating-wave background
(FND-131/132: level-1 rigid phase rotation, material orbit at c) change
the dynamical matrix from which BLOCH-L's anchors were read, and if so
by how much at the production reading window?

NOT in scope, named so no one mistakes a pass here for more than it is:
- The Kirchhoff-only conditionality on kb (the second-order geometric
  pre-stress terms, gated on contact machinery, FND-126 sec. 5). That
  gap is SEPARATE and this session cannot touch it.
- Any re-pricing of kb, r_s, or the anchors themselves. Whatever the
  verdict, no registered number moves in this session; only the
  static-background conditionality annotation is adjudicated.
- The level-2 rotation RATE (unregistered; composite build owns it).
  The session's arguments must hold for ARBITRARY common phase-shift
  rates at both levels or declare themselves level-1-only.

## THE LEGS

1. THE BACKGROUND KINEMATICS CONTROL. The level-1 rotating state must be
   reconstructed from registered inputs alone (reading-A geometry from
   the BLOCH-L file's own helix(), T_fibre = 3/2 T0_f, mu_f = T0_f/c^2)
   and must reproduce, as numeric controls: (a) the centripetal balance
   mu Omega^2 R = kappa_1 T_fibre; (b) the material-speed identity
   v_m = Omega R = c to 1e-6 (FND-132's jewel, recomputed not quoted);
   (c) kappa_1 R = sin^2 theta = 2/3. A failed control halts the session
   (Thirteenth-Catch rule: the convention layer is exactly where this
   class of session dies).

2. THE MASS-MATRIX LEG (derivation, displayed not assumed). In material
   coordinates the perturbation kinetic form is (mu/2)|d_t u|^2 with no
   convective or Coriolis term; the linear cross term integrates against
   the background acceleration and cancels by the background equation of
   motion (MAINT channel iii, FND-130). The cancellation must be stated
   with its condition (background equilibrated) and the level-2 case
   covered (equilibrated at any kb per MAINT sec. 4).

3. THE SHIFT LEG. The rotating background at time t is the static
   configuration with all level-1 phases advanced by delta = Omega t
   (rigid rotation about the winding axis is an isometry carrying
   tangents and curvature vectors with it). Therefore the entire
   time dependence of the perturbation problem enters through a COMMON
   phase shift in the instrument's local_set. The leg must verify the
   rotation/shift identity numerically (rotated tensors vs shifted-phase
   tensors, machine precision bar 1e-12).

4. THE INSTRUMENT SWEEP (the decisive leg). Branch speeds c_L, c_T at
   the production window (lambda = 24p, directions (001) and (111)),
   swept over common shifts delta in [0, 2pi), at multiplicities
   m = 1, 2, 4, 6, with independent level-2 common shifts included at
   m = 6. Pre-registered harmonic-counting prediction, stated BEFORE the
   sweep runs: the fibre energy form is degree <= 4 in the phase
   trigonometrics, so an m-point phase average is alias-free for m >= 5;
   the sweep should show delta-dependence at m = 1, 2, 4 and NONE at
   m = 6 (the production multiplicity) to the instrument's precision.

## THE OUTCOME SHEET (pre-registered)

- Spread at m = 6 below 1e-6 relative, at both directions, both levels'
  shifts -> NULL-CORRECTION: the dynamical matrix on the rotating
  background is time-independent AT THE PRODUCTION INSTRUMENT, the
  Floquet problem degenerates to the static one, the anchors carry ZERO
  background-rotation correction at every order, and the
  static-background conditionality on kb <= 0.079 is DISCHARGED (the
  Kirchhoff-only conditionality stands untouched).
- Spread at m = 6 above 1e-6 but below the 0.5% convergence bar ->
  CORRECTION-BOUNDED: report the bound, conditionality stands, no
  number moves.
- Spread above the convergence bar, or any Leg-1/Leg-3 control fails ->
  INSTRUMENT-LIMITED or HALT respectively. No verdict beyond that.

## CLEAN ROOM

The derive-point family (the coarse ratio's derive value, the r_s
derive-point, the c_L derive read) appears in NO leg of this session.
kb enters as a symbol only; no solve is rerun (a time-independent D
implies the BLOCH-L solve unchanged EXACTLY, which is the point).
Version numbers do not appear in prose. Bars may not be edited after
this lock; a failed bar is reported failed.
