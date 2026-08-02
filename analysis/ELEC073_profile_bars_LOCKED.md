# ELEC-073 — The 3D radial profile, solved. Locked bars

## Commission
ELEC-072 declared the scaling analysis exhausted and named the first step beyond
it: solve the Euler-Lagrange equation for the 3D radial profile with the derived
quartic and sextic, and check whether the assumed sech-like shape is anywhere
near the true one.

## The system, fixed before computing
From the lab-parametrization expansion (ELEC-070/071), E/T0 = p^2/2 - p^4/8 +
p^6/16 with p = psi'(r), integrated over 4 pi r^2 dr. The Euler-Lagrange
equation is d/dr [r^2 F(p)] = 0 with F(p) = p - p^3/2 + 3 p^5/8, giving the FIRST
INTEGRAL r^2 F(p) = C.

## Locked bars
B1 MONOTONICITY: F must be invertible for the first integral to define p(r)
   uniquely. Check min F' over the relevant range. If F is non-monotone the
   solution is multivalued and the analysis stops.
B2 THE PROFILE, and this is the question ELEC-072 asked: determine p(r) near the
   origin and compare with the sech family assumed in ELEC-069. Report the
   comparison whether or not it invalidates the earlier work.
B3 FINITENESS: the excursion and the energy integrals must converge. Report both.
B4 WHAT FIXES THE SCALE: the equation contains no length, so the solution is a
   one-parameter family in C. Determine what the size and energy scale as, and
   identify what in the corpus could fix the free parameter.
B5 HONESTY: this is a radial scalar model with the transverse field as a
   stand-in, no topology imposed, no time dependence, no charge. State it.
