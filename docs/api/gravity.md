# `rope_solver.gravity`

Weak-field / PPN observables

> rope_solver.gravity  --  Canonical weak-field / PPN observables.

## `cosmic_closure_ratio(H0_km_s_Mpc=70.0, G=6.674e-11, c=299800000.0)`

Mach/Dirac closure ratio  G M / (R c^2)  for the observable universe.

With R = c/H0 (Hubble radius) and M = critical-density mass inside the
Hubble volume, this returns 1/2 exactly: the observable universe sits at
its own Schwarzschild radius. This is the POSITIVE result behind the
expansion-tension idea for the origin of G (open_problems
'absolute-G-cosmic-tension'): G, R, M, c are locked as G = (1/2) R c^2 / M.

It does NOT yield G's absolute value, because the mass M is itself defined
through G (critical density carries G); every G-free route to a cosmic mass
fails at the count/rate/ratio -> mass step. So this ratio is a consistency
relation, not a derivation of G.

## `light_deflection_arcsec()`

Solar limb light deflection (arcsec): (1+gamma)/2 * 4GM/(R_sun c^2).

## `mercury_perihelion_arcsec_per_century()`

Perihelion advance of Mercury (arcsec/century) from PPN.

Delta phi = (2 + 2 gamma - beta)/3 * 6 pi GM / (a (1-e^2) c^2) per orbit.

## `nordtvedt_eta()`

Nordtvedt parameter eta = 4 beta - gamma - 3 (zero in GR and here).

## `ppn_parameters()`

Return (gamma, beta) of the rope effective metric.

Derived from the isotropic metric expansion:
  -g_tt = 1 - 2U + 2*beta*U^2 + ...        (U = GM/rc^2)
   g_ij = (1 + 2*gamma*U) delta_ij + ...
For psi = 1 + U (isotropic), g_tt = -[(2-psi)/psi]^2, g_ij = psi^4.

## `shapiro_gamma()`

The gamma that sets Shapiro/Cassini time delay (Cassini: gamma-1 ~ 2e-5).
