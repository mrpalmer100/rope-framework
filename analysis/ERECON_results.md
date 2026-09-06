# COMMISSION E-RECON -- RESULTS (2026-09-05)
Charter analysis/ERECON_charter_LOCKED.md; symbolic log
analysis/casimir/erecon_symbolic.log.

## VERDICT: ** RECON-IDENTICAL **
The two registered identifications of E are ONE identification under
a single relation the registry had not written down:

      A = - rho kappa_0 (s x z)      (the orientation connection IS the
                                     rotated collective transverse
                                     displacement, not its slope)

With this A:
- E = -dA/dt = rho kappa_0 (v x z) with v = ds/dt: EM-016's Faraday
  half equals EM-RECON-026's Magnus E pointwise, for every medium
  motion (sympy: difference identically zero).
- B = curl A = -kappa_0 rho (ds/dz) in-plane and +rho kappa_0 (div_perp
  s) along z. With rho_total = rho (1 - div_perp s) this is exactly
  B_total = -kappa_0 rho_total z: EM-RECON-026's constant B' = -rho
  kappa_0 z is the unperturbed background, and its perturbation is the
  mesh compression. The in-plane part is the strand TILT: B is minus
  kappa_0 times the strand-direction flux density -- the registered
  reading "the 1/r^2 field is rest-tension FLUX GEOMETRY (rope count)"
  (EM-RECON-011) made literal.
- A transverse plane wave s_x = f(z - t) gives E = rho kappa_0 f' y:
  in-plane, perpendicular to the propagation direction -- light is
  transverse under the reconciled reading. (The alternative, A = tilt
  = ds/dz, gives a DIFFERENT E for the same motion and is not the
  Magnus field; excluded.)
- A uniform translation of s shifts A by a constant = grad of a linear
  function: pure gauge, GG-004's phase-convention arbitrariness.
All four charter conditions hold for candidate (D) and fail for (T).
EM-016's phrase "orientation-transport rate" is to be read as the rate
of the transported DISPLACEMENT (the connection's holonomy), not the
strand slope. EM-016's Derived grade is untouched; this fixes a reading
it left open.

## The conductor condition (Leg 1 of CASIMIR-PLATE, now fixed)
Perfect conductor, plate normal along z (the weave axis): tangential
E = 0 means (v x z)_{x,y} = 0, i.e. v_x = v_y = 0 at the plate: the
in-plane collective displacement is PINNED at the plate sites --
DIRICHLET on both transverse components, effective separation
d_eff = d + 1 (Amendment A1(b)). The -grad phi half gives phi constant
along the plate: the longitudinal (twist-tension) channel is
constrained in its in-plane variation (k_par != 0 longitudinal modes
meet the plate; the k_par = 0 longitudinal mode does not).
CENSUS: transverse band 1 -- constrained (Dirichlet); transverse band 2
-- constrained (Dirichlet); longitudinal carrier -- constrained at
k_par != 0 through phi. The plate is a place where strands are pinned
in-plane and the tension field is level along it.
For the (111) plate normal (D6) the same statement holds with "in-
plane" read as tangential to the plate: tangential displacement
pinned, normal displacement free.

## Draft for the author's grant
EM-023 (proposed): "The orientation connection is the rotated
collective transverse displacement, A = -rho kappa_0 (s x z);
EM-016's E and EM-RECON-026's E coincide; B is minus kappa_0 times
the strand-direction flux density (background + compression + tilt);
a perfect conductor pins the tangential displacement (Dirichlet) and
levels the tension field along the plate." Riders: EM-016 (the
reading fixed), EM-RECON-026 (its B' identified as the background of
curl A), CAS-BC-OPEN (discharged by this commission).

## Consequence
CASIMIR-PLATE Leg 1 is complete; Legs 2-5 are licensed with the plate
condition above. The piston instrument is already calibrated (A1).
