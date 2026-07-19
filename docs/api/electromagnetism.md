# `rope_solver.electromagnetism`

EM sector and cross-sector locks

> rope_solver.electromagnetism  --  Canonical EM sector of the rope theory.

## `alpha_from_impedance()`

Fine-structure constant from EM constants: alpha = e^2 Z0 / (2 h).

Equivalent to alpha = e^2/(4 pi eps0 hbar c).  This is the EM-sector
expression for alpha; it MUST equal the soliton-coupling alpha used in
rope_solver.particles (kappa = alpha/2pi).  See consistency_with_particles.

## `charge(C1, C2)`

Quantized electric charge q = Lk (topological).

Integer charge is a linking number, not an imposed quantum number.
Delegates to the canonical linking-number implementation.

## `consistency_with_chemistry(rel_tol=0.001)`

Check the atomic-mode equation uses the SAME eps0 as the EM sector.

The rope chemistry paper builds the hydrogen mode equation on the Coulomb
tension field V(r) = -e^2/(4 pi eps0 r).  That eps0 must be identical to
the EM sector's, or the two papers would quote inconsistent atomic energies.
Returns (E1_eV, consistent): the hydrogen ground-state energy computed from
THIS module's eps0, and whether it matches the standard -13.6 eV.

NOTE: -13.6 eV is standard quantum chemistry, NOT a rope-specific result.
This is a cross-sector CONSISTENCY check (one eps0 across sectors), not a
claim that the rope theory derives the hydrogen spectrum.

## `consistency_with_gravity(rel_tol=1e-09)`

Check c_EM equals c used in the gravity sector (one rope, one speed).

Returns (c_em, c_gravity, consistent).

## `consistency_with_particles(rel_tol=0.001)`

Check the EM-sector alpha equals the particle-sector soliton alpha.

alpha_from_impedance() (EM) must match the alpha behind kappa=alpha/2pi
(particles).  Returns (alpha_em, alpha_particles, consistent).

## `d3_is_essential()`

Why d=3 is required (Helmholtz: div-free field = curl only in d=3).

Returns a short structural statement; the Ampere-Maxwell law fails to
follow in d=2 (div-free = gradient) or d=4 (needs extra topology).

## `dirac_quantization_n(e_charge, g_charge)`

Dirac integer n = e*g/(2*pi*hbar) for electric e and magnetic g charges.

Follows from identifying the EM U(1) bundle with the Hopf bundle
(first Chern number 1) and requiring bundle consistency over S^2.
INHERITED from the bundle identification, not an independent rope result.
Returns n; bundle consistency requires n to be an integer.

## `eps0_from_structure()`

Vacuum permittivity from the structural identity eps0 = 1/(mu0 c^2).

In the rope model c^2 = T0/mu_rope and the EM constants satisfy
eps0 mu0 = 1/c^2, so eps0 is fixed once mu0 and c are.  Returns the SI
value as a consistency check against 8.854e-12 F/m.

## `impedance_of_free_space()`

Vacuum impedance Z0 = sqrt(mu0/eps0) = mu0 c.

A structural consequence of c^2 = 1/(eps0 mu0): the rope model predicts
Z0 = mu0 c with no extra input.  Returns ohms (SI: 376.730).

## `maxwell_structure()`

Return the derivation chain of the four Maxwell equations (as recorded).

Structural/topological derivation (rope_topological_maxwell), not a grid
solve.  Each entry: (equation, origin).

## `wave_speed_squared(T0, mu_rope)`

EM (and gravitational) wave speed squared c^2 = T0/mu_rope.

One rope carries both EM and gravitational waves, so this single speed
serves both sectors -- the origin of c_EM = c_GW.
