# COMMISSION PEV-IDENT (F2) -- RESULTS (2026-09-05)
Executed under analysis/PEV_IDENT_charter_LOCKED.md (locked before any
ratio was evaluated). Legs 0-2: analysis/pev_ident/ (controls logs,
legs12_symbolic.py). Numbers attached in this Leg 3 only.

## VERDICTS (locked grammar)
  Q1  ** IDENT-IDENTITY **
  Q2  ** BAND-ABOVE ** (rotation frequency)  |  ** BAND-ABOVE ** (wave)
  Q3  ** P33-DEMOTE **

## Leg 0 -- controls (all pass)
v1 R_1: symbolic R_1 = sqrt(2) a_f / (2 pi) = 0.22507908 a_f (registered
   0.22508; |err| 9.2e-7 < 1e-6).
v2 Band ceiling: the C1/FND-089 instrument re-run on the adjudicating
   f = 1/5 member, 13^3 grid: S = 3.3575 exactly (stable vs 9^3 at
   0.01 pct); c_eff = 0.7615 c.
v3 Rotating helix: maint_equilibrium.py re-run; v_1 = sqrt(3/2) c from
   registered inputs, level-1 control 0.000 pct.
v4 Clean room: grep-verified before and after Legs 1-2.

## Leg 1 -- Q1, the ratio (symbolic, sympy)
E_rot = hbar c / R_1 with R_1 = a_f sqrt2 / (2 pi) (pitch p = a_f,
sin^2 psi_1 = 1/3, convention A). E_ceiling(a_f) = h c / (4 a_f) (the
lambda/4 rule read as the photon energy whose quarter-wavelength is
a_f). Then
      E_rot / E_ceiling = 2 sqrt 2      (free symbols: none)
and equivalently, at the ceiling itself, E_rot(a_f,ceil) / E_max =
2 sqrt 2 with m cancelling. The two scales are ONE scale, a_f,
appearing twice; the pure number 2 sqrt 2 = 4 / (2 pi R_1/a_f) is
fixed by the pitch-to-radius relation, the magic angle, and the
lambda/4 rule. No a_f determination can separate them.
(Numerical check, Leg 3: 2 sqrt 2 x 1.4 PeV = 3.960 PeV, Prediction
33's stated value at m = 1 -- the "coincidence" was the identity.)

## Leg 2 -- Q2, the fine frequency ladder (units c / a_f)
  omega_homog (lambda/4 ceiling)         pi/2      = 1.5708
  omega_band  (instrument, S c_eff/a_f)  3.3575 x 0.7615 = 2.5567
  omega_band  (charter-literal, S c/a_f) 3.3575
  omega_wave  (FND-130 rotating helix)   sqrt2 pi  = 4.4429
  omega_rot   (material orbit c / R_1)   sqrt2 pi  = 4.4429
  level-2 torus spectrum (FND-142): OMITTED -- its unit conversion
    to c/a_f is not registered; the charter admits it for display
    only after that conversion is recorded, so it is not placed.
Two findings: (i) omega_rot = omega_wave IDENTICALLY (the rotating-
helix wave's temporal frequency is the material orbit frequency --
fibre length per turn is sqrt3 a_f, and sqrt(3/2) c / sqrt3 a_f x
2 pi = sqrt2 pi c/a_f); (ii) omega_rot sits ABOVE the band ceiling by
32 pct (charter-literal) or 74 pct (instrument units) -- far outside
the 5 pct BAND-EDGE window under either normalization, so D2's
normalization caveat does not change the placement. No transverse
normal mode exists at omega_rot; the FND-089 lookup is therefore not
licensed (D4: "reported as above, with the statement that no
transverse normal mode exists there").

## Leg 3 -- Q3, disposition of Prediction 33
IDENT-IDENTITY x BAND-ABOVE -> P33-DEMOTE under the locked grammar.
Prediction 33 as written ("the SAME class ... locked to move with
it under any a_f determination"; test: "a future a_f determination
that separates the two scales") commits to a separation that the
registered constructions make impossible (the ratio is 2 sqrt 2
identically) and to a "vacuum spectral structure in the PeV window"
that has no transverse carrier (the rotation lies above the band the
mesh carries; it is a relative-equilibrium state, consistent with
KBSAT's "forced, not adopted"). Its stated test is vacuous and its
observable has no channel.

DISPOSITION (draft for the author's grant; paper-sync after):
  Prediction 33 is DEMOTED from Structural to a registered identity of
  the ceiling construction: "E_rot = 2 sqrt 2 x E_ceiling(a_f)
  identically; the winding rotation frequency equals the level-1 wave
  frequency, sqrt2 pi c/a_f, and lies above the medium's transverse
  band (S c_eff/a_f = 2.56 c/a_f)." Removed from the live prediction
  inventory; the count in docs/WHERE_IT_STANDS.md is adjusted by one.
  The identity itself is kept at full weight (a demotion by the
  corpus's own reduction is a result).

## Consequences for the queue
- FINE-GATE Q2 inventory: the "rotation quantum" relation is NOT an
  independent equation in a_f; it is the lambda/4 relation times
  2 sqrt 2. One fewer candidate pair (recorded for FINE-GATE by
  amendment when it locks).
- The identity omega_rot = omega_wave is a new registrable
  consistency statement (FND-130 x FND-132), offered with the
  demotion.
- No new scale, no new coupling introduced; the resemblance rule was
  not needed (the identification is a derivation, not a resemblance).

## Process
One session, as budgeted. Controls, symbolic legs, and the ladder
were complete before any Prediction-33 number was read; the numbers
3.96 and 2.83 first appear in this document.
