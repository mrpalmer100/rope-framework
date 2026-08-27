# COMMISSION TRUE-STATE (STAGE 1) -- THE TRUE COMPOSITE STATE -- BARS (LOCKED)

*Locked 2026-08-18 before computing. The author's desk chose option
(b) at FND-139: commission the true composite state -- variational,
arclength-preserving, on the adjudicated force law -- and re-price
Sigma_wave from its solution.*

## FAMILY DECLARATION (the honesty clause)

The solve runs in the RELATIVE-EQUILIBRIUM family: rigid rotation at a
single Omega about the winding axis, r(s,t) = R_z(Omega t) rho(s),
inextensible (arclength exactly preserved by construction), tension
the constraint field. This family contains the VERIFIED level-1 state
as a member and is the variational class (critical points of E -
Omega J). Screw/traveling composite classes are NAMED OPEN; a stage-2
charter covers them if stage 1's state is contested.

## THE FORCE LAW (adjudicated, FND-139)

At kb = 0: (T that)' = mu rddot, i.e. in the co-rotating frame
    (T w')' + mu Omega^2 w = 0,     T = F / z',    z' = sqrt(1 - |w'|^2),
w the complex transverse position, F the constant axial force flux
(the z-equation integrates exactly). DERIVE on the face; CONTROL: the
single-mode member must return the registered level-1 state
identically (Omega = k1 sqrt(T) = 4.4429 at T = 1.5; halt on fail).

## THE OBSTRUCTION LEG (structure, before the solve)

Show on the face: a pure two-mode w makes |w'|^2 oscillate at the
difference wavenumber, so z' and hence T oscillate, and (T w')'
generates harmonics outside the two modes -- NO pure two-mode member
exists; the true state carries a full harmonic tail. This is the
structural explanation of FND-139's order-one off-shell finding and
is pre-registered as the reason the ansatz failed.

## THE SOLVE (Galerkin/collocation)

Fourier in s on the rationalized cell (level-2:level-1 winding ratio
q = 3/2, the nearest small rational to the registered 1.492 --
INSTRUMENT CHOICE, sensitivity at the registered irrational ratio
displayed via a second rationalization 149/100 NOT required at stage
1 but the choice is on the face). Pins, all declared: level-1 mode
amplitude at the registered R1; level-2 mode amplitude at the
registered R2 (shape content held to the registered geometry);
arc-mean tension <T> = 3/2 (the tripwire quantity preserved as the
mean; F floats to satisfy it); gauge fixed by real-positive mode
phases. Unknowns: harmonic coefficients, Omega, F. Both handedness
signs solved (level-2 mode at +q and -q).

Controls: (i) residual of the full nonlinear system < 1e-9; (ii)
|w'| < 1 everywhere (the parametrization's validity); (iii) removing
the level-2 pin amplitude -> 0 recovers the level-1 member (seed
continuation control); (iv) harmonic-tail convergence: doubling N
moves Sigma by < 0.5%.

## THE RE-PRICING

Sigma_wave (kb = 0 corners, both signs) = [booked 1.0 per unit arc +
KE per unit arc] x (arc per axial), from the SOLUTION. Comparison to
the registered box and to the refit display appears in the final leg
only. The kb-at-bound corners are NOT re-priced (bending under
kappa_true belongs to TRUE-SOLVE, chartered separately).

## OUTCOME SHEET

- Both signs converge, controls pass -> STATE-FOUND: Sigma_wave's
  kb = 0 corners re-priced FROM A SOLUTION, displayed against the
  box; adoption is the author's (the registry rider updates to cite
  the solution; the box moves only on the author's confirmation,
  which option (b) implies but the claim requests explicitly).
- One sign fails to converge -> the converged sign is registered,
  the failure reported with its diagnostics.
- Obstruction leg fails (a pure two-mode member exists) -> the
  structural story of FND-139 is WRONG and the session halts to
  report that instead.

## CLEAN ROOM

The registered box and refit numbers appear in the final leg only.
T_fibre enters as the pinned mean 3/2 and is not re-priced. Verdict
prose after the run; controls print; bars locked.
