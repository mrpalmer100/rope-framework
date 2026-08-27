# COMMISSION TRUE-STATE, STAGE 2 -- THE TWO-FREQUENCY SOLVE -- BARS (LOCKED)

*Locked 2026-08-18 before computing. Chartered at FND-140: the
invariant-torus composite state r(s,t) = R_z(Omega_1 t) q(s, Omega_2 t)
on the adjudicated force law, Fourier/collocation in s AND the internal
phase, unknowns including BOTH frequencies; the FND-135 ansatz is the
seed and the FND-139 refit display brackets the search. Sigma_wave
re-prices from THIS solution and nowhere else -- the author's option
(b), executing through this stage. Full benchmark suite verified green
by the author (GitHub CI) before this session: the base is paid.*

## THE FORMULATION (on the face)

Rotating frame q(s, phi), phi = Omega_2 t, q = (w, gamma s + zeta)
with w complex transverse, zeta doubly periodic, mu = 1:

  transverse:  -Om1^2 w + 2i Om1 Om2 w_phi + Om2^2 w_phiphi = (T w_s)_s
  axial:       Om2^2 zeta_phiphi = (T (gamma + zeta_s))_s
  constraint:  |w_s|^2 + (gamma + zeta_s)^2 = 1   (inextensible,
               pointwise on the torus; T is the multiplier field)

Level-1 member in closed form (the recovery control): w = R1 e^{i k1 s},
zeta = 0, T = 3/2, gamma = 1/sqrt(3), Om1 = k1 sqrt(T) = 4.4429; the
pricing formula Sigma = (1 + KE/arc) / gamma returns 2.598 exactly
(Om1 R1 = 1, the material-speed identity, visible on the face).

## PINS AND GAUGE (all declared)

Cell and rationalization inherited from stage 1: Lcell = 2 sqrt(3),
q = 3/2 (n1 = 2, n2 = 3; INSTRUMENT CHOICE, on the face). Pins:
level-1 content Re c_{n1,0} = R1 (registered), Im c_{n1,0} = 0
(gauge); level-2 content |c_{n2,m2}| = A2 pin ramped by continuation
to the registered R2, Im c_{n2,m2} = 0 (gauge); torus-mean tension
<T> = 3/2 (the tripwire quantity as the mean); <zeta> = 0 (z-origin).
Handedness: m2 = -sigma for sigma = +1 (aligned) and m2 = +sigma for
sigma = -1 (anti-aligned), the traveling-phase convention k2 s - sigma
phi inherited from the composite build; the labeling is a convention
and is stated, not adjudicated. THREE continuous symmetries
(s-translation, z-rotation, phi-translation) against TWO gauge
conditions leave ONE gauge null direction on the solution manifold --
tolerated by the trust-region solver and irrelevant to every priced
quantity (all gauge-invariant); stated here so the rank deficiency is
not mistaken for marginality.

## DISCRETIZATION AND SOLVER

Physical-grid collocation Ns x Nphi with 4th-order periodic finite
differences in both directions; unknowns are the grid fields (w, zeta,
T) plus (gamma, Omega_1, Omega_2); scipy least_squares (trf) with the
declared Jacobian sparsity. CONTINUATION from the level-1 member: the
A2 pin ramps 0 -> R2 in steps, previous solution seeding the next --
the stage-1 method, now in the family stage 1 proved the state
requires. Seed frequencies: Om1 at 4.4429; Om2 at the FND-139 refit
display (0.43x the build's 6.626 for aligned, 0.20x for anti-aligned;
DISPLAY-derived seeds, not bars -- landing outside the bracket is
reported, not penalized).

## CONTROLS (printed; halt semantics as marked)

(i)   LEVEL-1 RECOVERY: the solve at A2 pin = 0-limit (smallest ramp
      step continued back) must return Om1 = 4.4429 (rel 1e-3),
      T uniform 3/2 (max dev 1e-3), gamma = 0.57735 (1e-4). HALT.
(ii)  DISCRETE RESIDUAL: full nonlinear system residual RMS < 1e-8 at
      every accepted continuation step. HALT at the final step.
(iii) PARAMETRIZATION VALIDITY: min (gamma + zeta_s) > 0 (the curve
      advances axially everywhere). HALT.
(iv)  HARMONIC-TAIL CONVERGENCE: at the registered R2, re-solve at
      (3/2 Ns, 3/2 Nphi); Sigma moves < 0.5%. HALT -> the coarse
      value registers as DISPLAY ONLY with the drift on the face.
(v)   OBSTRUCTION CONSISTENCY: the solution's harmonic content beyond
      the two pinned modes is DISPLAYED (stage 1 proved the tail
      mandatory; a solution with a negligible tail would contradict
      FND-140 and is a SURPRISE to flag, not a pass).
(vi)  BOTH SIGNS solved; per-sign convergence independent.
(vii) STRETCH CONTROL: the constraint residual max displayed
      separately from (ii) -- arclength preservation is exact by
      construction here, the very property FND-139 measured the
      ansatz to violate (0.15 Omega_2); the contrast is the point.

## THE RE-PRICING (the deliverable)

Sigma_wave, kb = 0, per sign: Sigma = [1.0 booked + KE per unit arc]
x (arc per axial) with KE/arc = (1/2) <|i Om1 w + Om2 w_phi|^2 +
Om2^2 zeta_phi^2> over the torus and arc/axial = 1/gamma, all from
the SOLUTION. The kb > 0 corner of the old box is NOT re-priced
tonight: the bending force law on the torus state is a separate
construction (kappa_true machinery on the solved geometry), NAMED as
the follow-on, with the ceiling context now FND-141's 0.09332.

## CLEAN ROOM

The registered box [3.222, 4.313], the level-1-exact 2.598, and the
FND-139 refit corners (3.335 / 3.089) appear ONLY in the comparison
leg after both signs have converged and priced. T_fibre tripwire
(<T> = 3/2) is a pin, not an output. Verdict prose written AFTER the
run. Bars not edited after lock.

## PRE-REGISTERED OUTCOME SHEET

- BOTH SIGNS CONVERGED, controls pass: TRUE-STATE-SOLVED. Sigma_wave
  re-prices to the solution's kb = 0 corners [min, max over signs];
  the FND-135 box is SUPERSEDED-NOT-ERASED (exact averages of a
  non-solution, kept as the record); the FND-139 rider DISCHARGES
  into the re-priced value; the kb-increment is a named open item.
  If a corner lands below the old box's lower edge 3.222, that is the
  FND-139 conflict CONFIRMED and RESOLVED in the same stroke -- the
  registered number simply moves.
- ONE SIGN CONVERGES: the converged sign prices; the other registers
  NOT-FOUND-IN-SEARCH with the search declared; the box restates
  one-sided with the open side named.
- NEITHER CONVERGES: Failed-and-kept -- the two-frequency family
  refuses the pins as posed; the resonant-k2 window and the pin set
  become the named suspects; interim options (hold-with-rider /
  retreat to 2.598) return to the desk intact.
- Omega_2 outside the refit bracket: reported on the face; the
  bracket was a display, not a bar.
