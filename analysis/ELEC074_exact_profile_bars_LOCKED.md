# ELEC-074 — The exact profile: is the cusp an artifact? Locked bars

## Commission
ELEC-073 solved the sixth-order truncation and found a profile cusped at the
origin (p ~ x^(-2/5)), then flagged it as possibly the truncation announcing its
own failure, naming an eighth-order re-solve as the test.

## The better test, and why it replaces the named one
The lab-parametrization density is known in CLOSED FORM: E/T0 = sqrt(1+p^2) - 1.
There is no need to go to eighth order -- the ALL-ORDERS problem can be solved
directly, and doing so is strictly stronger than the named next-order.
Then F(p) = dE/dp = p/sqrt(1+p^2), which is BOUNDED with sup F = 1, where the
truncation's F(p) = p - p^3/2 + 3p^5/8 was UNBOUNDED. That difference is not a
detail: the first integral r^2 F(p) = C is solvable for all r > 0 in the
truncation but only for r^2 >= C exactly.

## Locked bars
B1 Confirm the boundedness and state what it does to the domain.
B2 THE PROFILE: solve exactly and compare with ELEC-073's cusp. Report whether
   the cusp survives, and if not, say plainly that ELEC-073's profile was an
   artifact.
B3 CONVERGENCE: the excursion and energy integrals must still converge, now
   with the singularity at a finite radius rather than at the origin.
B4 THE SCALING RELATIONS: recompute size vs excursion and energy vs excursion.
   Report whether ELEC-073's r ~ Delta and E ~ Delta^3 survive the correction,
   and with what coefficients.
B5 HONESTY: an exact solution of the LAB-parametrization density is still a
   solution of a scalar toy. It inherits every scope limit of ELEC-073 and adds
   nothing about charge, spin, or the measured electron.
