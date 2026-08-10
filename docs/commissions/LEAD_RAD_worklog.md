# LEAD-RAD WORKLOG (construction phase; alpha out of the room)

Run opened 2026-08-09 on operator GO. Charter:
docs/commissions/COMMISSION_LEAD_RAD_radiative_backreaction.md (read
first, per its own condition). This worklog records the construction
BLIND: no reference to the target residuals, measured couplings, or
measured g anywhere in this phase. Targets enter only at the final
confrontation, in a separate, clearly marked step.

## The committed kinematics (registered inputs only)

- The MOMENT observable (Gate 2b, registered): the terminus circulates
  at the luminal edge, Omega_e R* = c, R* = pi lambda_bar_C. The
  retardation parameter of the circulating source is beta = 1 exactly.
- The ENERGY observable (Commission W, registered): the dressing
  configuration rotates at Omega = pi/x*, domain radius x* = exp(pi^2).
  The pattern speed at the domain edge is Omega x* = pi -- the outer
  pattern is superluminal beyond r = x*/pi, which in a wave-bearing
  medium is the condition for radiative coupling of a rotating pattern.
- The medium: the committed elastic law (density eps + (1/2) k eps^2,
  eps = sqrt(1+g^2) - 1), whose linearization is a wave-bearing membrane
  with unit wave speed in solver units. The geometry is the solver's:
  2D axisymmetric with measure 2 pi r dr.
- The coupling: the corpus's own e_eff^2 (the chain's output variable,
  carried SYMBOLICALLY as alpha_bare); the recorded spin normalization
  S = hbar/2 (tether Z_2, registered). No measured value enters.

## The mechanism, stated once

A rotating source in a wave-bearing medium is dressed by its own
RETARDED field, not its static field. The static solver computes the
static dressing; the back-reaction term is the difference. For a source
circulating at angular frequency W, decompose in angular harmonics m:
each harmonic radiates/dresses at frequency m W, and the self-
interaction kernel per harmonic is the 2D Helmholtz Green's function at
wavenumber m W / c evaluated on the source circle -- Bessel structure
J_m(m beta) and Y_m(m beta) at retardation parameter beta = W R / c.
The REAL part of the kernel shifts the dressing energy (the reactive,
moment/energy-shifting piece); the IMAGINARY part is radiated power
(which for a steady state must be resupplied and enters the energy
budget). The dimensionless WEIGHTS multiplying alpha_bare are angular
mode sums of these kernels at the committed beta values (1 for the
moment; the pattern structure at Omega x* = pi for the energy) --
derived numbers, no freedom.

## Phase plan

- A2 (first, cleanest): the moment-side kernel. The m = 1 circulating
  charge at beta = 1: compute the reactive self-interaction weight
  w2 from the mode kernel, with convergence and regulator handling
  recorded (the m-sum's UV end is cut by the committed source size --
  the terminus core scale from the solver's r_min physics -- and the
  cut-dependence must be shown weak or absorbed into a registered
  structure, else the honest outcome is the quantum fence).
- A3: the energy-side kernel. The rotating dressing pattern's radiative
  zone (r > x*/pi): the dynamical correction to D_E from replacing the
  static kernel by the rotating-frame retarded kernel on the committed
  solution f(r). Weight w1 as a functional of the REGISTERED f(r), no
  re-solve of the statics (the static result is protected by charter).
- A4: the single-mechanism check: w1 and w2 must come from the SAME
  kernel construction (same Green's function, same coupling
  identification) applied to the two observables. Any per-observable
  freedom voids the run (charter bar).
- CONFRONTATION (last, separate step, clearly marked): targets enter.

## Honest hardness ledger (live)

- The 2+1D wave equation has no Huygens principle (afterglow tails);
  steady circular motion makes this tractable via the frequency-domain
  mode sum, which is why the construction goes through harmonics.
- The m-sum at beta = 1 sits exactly at the sonic/luminal boundary
  where J_m(m) decays only as m^(-1/3); convergence and the physical
  cutoff are the construction's central technical risk, recorded as
  such before computing.

## A2 session 1 record (2026-08-09)

The mode kernel at beta = 1 computed (scipy Bessel, deterministic):
- Radiative series J_m(m)^2 and reactive series J_m(m) Y_m(m) both
  decay as m^(-2/3) (measured exponents -0.666 / -0.667 over m in
  [30, 60]) -- the raw sums diverge as M^(1/3). The cutoff question
  flagged in the hardness ledger is confirmed real: a point-source
  self-interaction at the luminal edge is cutoff-sensitive at power
  1/3 in the angular cutoff M* ~ R / (core size).
- Structural constant found: the reactive/radiative ratio per mode
  approaches -sqrt(3) (measured -1.732 at m = 60) -- the transition-
  region Bessel relation Y_nu(nu) -> -sqrt(3) J_nu(nu). Recorded as a
  derived invariant of the luminal boundary.

## The construction's next fork (posed before computing it)

The observables are not the bare kernel sums. The moment correction is
the field ANGULAR MOMENTUM of the retarded self-field per recorded
spin; the energy correction is the REACTIVE self-energy per dressing
energy. Both are combinations (weighted sums, differences against the
static kernel) in which the M^(1/3) divergence either cancels --
leaving a derived finite weight -- or does not, in which case the
charter's outcome 4 (the quantum fence: the back-reaction requires
quantized occupancy to regulate) is the registered endpoint. Next
session: construct both functionals explicitly, subtract the static
(W-committed) kernel, and adjudicate cancellation BEFORE any
confrontation. Alpha remains out of the room.

## A2/A3 session 2 record (2026-08-09, construction completed blind)

Script: explorations/lead_rad_a2a3_construction.py (deterministic).

A2 (moment side, point terminus at beta = 1):
- The static-subtracted reactive sum sum_m [-(1/4)J_m(m)Y_m(m) - 1/(4 pi m)]
  DIVERGES: measured growth exponent M^0.28 (approaching the analytic 1/3
  from below; subleading terms slow the approach). Values 0.58 (M=100) ->
  7.00 (M=30000). The static kernel removes only the log-class piece; the
  m^(-2/3) transition-region tail survives subtraction. Cutoff sensitivity
  34% per half-decade: the moment-side weight is CUTOFF-DEFINED, power 1/3.
- Derived structural identity recorded: the RADIATIVE rotating-frame budget
  E - Omega L vanishes mode-by-mode (omega_m = m Omega exactly), so radiated
  power cannot carry the correction; the correction lives entirely in the
  REACTIVE stored piece, which is the divergent object.
- The one registered regulator candidate (a finite terminus core scale) is
  unavailable inside the bars: the corpus's numerical core value descends
  from V Phase 2 LEAD-2, whose chain loaded CODATA alpha; admitting it
  during construction puts alpha in the room. The W-solver core scale is
  ruled out separately: D-E-COMPLETE A2 exhibited r_min -> 0 on the actual
  solutions. No registered alpha-independent cutoff exists.

A3 (energy side, committed f(r), m = 1 winding at k = Omega):
- Finite. w1 = (W_dyn - W_stat)/E_rot = -6.76e15, spread 0.52% across
  r_min/tol variations. No cutoff issue (extended source). Sign negative.
- Caveat on the face: the normalization of the winding-channel source to
  the medium coupling is NOT a registered identification; the raw magnitude
  therefore carries an unfixed conversion. w1 is machinery, not a landing.

## CONFRONTATION DECISION (the marked step; targets stay unloaded)

The charter's arbiter requires ONE mechanism producing BOTH P1 and P2 with
derived coefficients. P2 (moment) is not derivable classically: the weight
exists only relative to a UV cutoff the corpus cannot supply without
importing quantized structure or an alpha-contaminated scale. This is
precisely the charter's named outcome 4. No confrontation is licensed:
loading targets against A3's w1 alone, with its normalization unfixed and
its partner dead at the fence, would be target-hunting. Targets were never
loaded; alpha remained out of the room for the entire run.

## OUTCOME REGISTERED: 4 -- THE QUANTUM FENCE

The radiative back-reaction of the luminal terminus requires a physical UV
regulator (finite core / quantized occupancy) that the classical corpus
demonstrably lacks. The +178.8 ppm residual and the Schwinger-class moment
gap are FENCED as quantum-radiative, not derived and not refuted. The
classical arc's endpoint is now audited from every side: statics complete
(D-E-COMPLETE), boundary closed (V-A), rates/branches/continuum/q^2 closed
(Z bricks), and the dynamical correction shown to be cutoff-defined at
power 1/3 (this run). This is the publishable boundary V-A outcome 4
named, now reached constructively rather than by elimination.

NAMED FOR A FUTURE GO-DECISION (not opened): if a core scale is ever
registered by an alpha-independent route, the A2 sum at M* = R*/r_core is
a zero-freedom computation and the fence re-opens at exactly one number.
