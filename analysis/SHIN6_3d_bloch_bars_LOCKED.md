# COMMISSION SHIN6 -- THE 3D TWO-POLARIZATION BLOCH INSTRUMENT (bars LOCKED)

Locked 2026-08-12, author authorization (Mark Palmer): clear the debt
register. Tier T3, GRANT-SUBSTRUCTURE-TIGHT debts 3 then 1. Bars fixed
BEFORE any computation. Adverse outcomes pre-authorized: a failure is
registered Failed-and-kept, no rescue, KNOWN_LIMITATIONS unchanged.

## The medium (fixed at lock)

3D cubic supercell, vector displacements, local tangent field t(x)
from the DERIVED two-level winding (FND-088, no free angles):
  psi_1 = arcsin(1/sqrt(3)) = 35.2644 deg
  psi_2 = arcsin(sqrt((15 + 2 sqrt(30))/35)) = 59.4444 deg
Level-1 tangent: polar tilt psi_1 from transverse plane, azimuth
phi_1(x); level-2: the same construction expressed in the level-1
local frame with pitch angle psi_2, azimuth phi_2(x). Phases advance
linearly across the supercell (SHIN3's construction lifted to 3D):
  phi_1 = 2 pi x / P1,  phi_2 = 2 pi (y / P2 + z / P3)
with all pitches <= lambda/4 (the FND-086 homogenization regime).
Probe wavelength lambda = 6 lattice units (|k| = 2 pi / 6), matching
the validated 2D instrument's ratio. Pitch set to be scanned, fixed
at lock: (P1,P2,P3) in {(3,4,4), (4,4,4), (3,3,4)} -- p <= lambda/4
throughout... wait, lambda/4 = 1.5; the pitch condition in FND-086 is
p = lambda/8 to lambda/6 in the PASSING member with the regime bar
p <= lambda/4 stated on the modulation period seen by the wave. The
periods above are the supercell phase periods; the modulation period
along a propagation direction is min over the phase gradients. LOCKED
CONDITION restated precisely: for every scanned pitch set, the
modulation wavelength along each probe direction must be <= lambda/4;
any set violating this is out of regime and skipped, not failed.
Correction at lock (no computation performed yet): the sets above give
modulation periods 3-4 units against lambda/4 = 1.5; to sit in the
regime the phase must advance faster. Locked pitch sets:
  (P1,P2,P3) in {(1,1,1) is degenerate -- excluded}
  phi advance per lattice step in {2pi/1.5 equivalent: use
  phi_1 = 2 pi x * (2/3), phi_2 = 2 pi (y + z) * (2/3)} i.e.
  fractional advance f in {2/3, 1/2, 1/3} per step, supercell taken
  as the minimal integer period of f (3, 2, 3 respectively).
The f = 1/3 member has modulation period 3 units > lambda/4 = 1.5:
OUT OF REGIME, retained as the loose-side control expected to degrade
(bracketing per FND-084). In-regime members: f = 2/3 (period 1.5 =
lambda/4 exactly) and f = 1/2 (period 2 -- boundary case, marginal;
its verdict is reported but only the in-regime member bears the bars).

## Inextensibility (fixed at lock)

Longitudinal displacement along t(x) is constrained out by projector
P_t = I - t t^T applied symmetrically at each site (FND-REL-002's own
mode-counting: rope inextensibility removes the material longitudinal
mode). The two lowest bands with transverse character are the
physical polarization pair.

## Bond model (fixed at lock)

Nearest and next-nearest neighbor bonds (the 3D lift of TAV3B's
8-neighbor stencil: 6 + 12 = 18 neighbors), scalar bond stiffness
  w(b, x) = (KX + (b_hat . t(x))^2) / |b|^2,  KX = 0.08
(TAV3B/SHIN3's validated form, unchanged), acting on the projected
vector displacement.

## Probe directions (fixed at lock)

13 directions: the 3 axes, 6 face diagonals, 4 body diagonals
(normalized). Full-sky proxy at supercell-affordable cost.

## THE BARS (SHIN4 precedent numbers where they exist)

B1  min group speed over all directions and both polarizations >= 0.3
B2  phase-speed spread (max-min)/mean, pooled over directions AND both
    polarizations, <= 0.05
B3  group-velocity vs k misalignment <= 15 deg, every direction, both
    polarizations
B4  plane-wave spectral weight of each of the two transverse bands
    >= 0.5 (summed transverse-projected plane-wave weight per band)
B5  polarization degeneracy: |omega_+ - omega_-| / mean <= 0.05 at
    every probe direction
CTRL  the straight medium (phi_1 = phi_2 = 0, t = z_hat everywhere)
    at the same wavelength must FAIL B2 with spread >= 0.20
    (obstruction visible; TAV3B's 2D control showed 0.45). If the
    control passes, INSTRUMENT-INVALID is declared and taken, not
    tuned.
BLIND  the instrument code computes wound and straight through the
    same path; no branch may inspect which case it is serving beyond
    the tangent field itself.

## Speed normalization (fixed at lock)

Long-wavelength phase speed of the straight medium's transverse
branch along z (the fiber axis: the fast, unobstructed direction)
defines v = 1, as in TAV3B. The direction-averaged stiffness factor
of the wound medium (SHIN4 measured 0.790 in 2D) is expected < 1 and
is absorbed by the SHIN3 G1 tension compensation; it is REPORTED, not
barred.

## Verdict rule (fixed at lock)

PASS = B1..B5 all met on at least one in-regime pitch member with
CTRL failed by the straight medium. PASS clears debt 3 and the
session proceeds to the FND-REL-002 re-derivation (debt 1) with SHIN6
as machine verification. FAIL on any bar = Failed-and-kept, debts
stand, no rescue.

## ADDENDUM AT FIRST RUN (2026-08-12, before any verdict accepted)

Two instrument facts, disclosed:
(1) LATTICE ALIASING: phase advance f and 1-f are identical on
integer sites; the locked f = 2/3 member IS the f = 1/3 member
(modulation period 3). By the locked regime rule it is skipped.
(2) WAVELENGTH ERROR AT LOCK: lambda = 6 was locked citing "the
validated 2D ratio"; SHIN4's validated passing regime is lambda = 24
with pitch 3-4 (p = lambda/8 to lambda/6). At lambda = 6 no integer
lattice can reach p <= lambda/4. The first run is declared
INSTRUMENT-PARAMETERIZATION-INVALID at its own terms (TAV3
precedent), not a wound-medium failure.

CORRECTED PROBE (SHIN6B): lambda = 24 (|k| = 2 pi / 24), members
f = 1/3 (p = 3 = lambda/8) and f = 1/4 (p = 4 = lambda/6), both
inside SHIN4's passing window; loose control f = 1/12 (p = 12 =
lambda/2, out of regime, expected degraded). Bars B1-B5, CTRL
threshold, blindness guard, verdict rule ALL UNCHANGED.

## SECOND ADDENDUM (2026-08-12): INSTRUMENT-INVALID, replaced

The projector-based dynamical matrix violates the acoustic sum rule
(P_i P_j couplings with site-varying projectors do not annihilate
uniform translation), producing a spurious k -> 0 gap: straight
control returned mean v = 3.42x normalization with zero group
speeds. Declared INSTRUMENT-INVALID at its own control, taken not
tuned (TAV3 precedent). REPLACEMENT INSTRUMENT (SHIN6C): central-
spring vector lattice -- pairwise blocks w * (bh bh^T) with Bloch
phases, sum rule holds by construction; same bond stiffness law
w = (KX + (bh.t)^2)/r^2 averaged over the bond's two ends;
longitudinal branch is naturally stiff, transverse pair identified
by transverse plane-wave weight. Bars B1-B5, CTRL, probe set,
verdict rule ALL UNCHANGED.

## THIRD ADDENDUM (2026-08-12): the fourth-moment sampling requirement

FND-088's isotropy is a FOURTH-moment condition; fourth harmonics of
the winding azimuth require >= 5 discrete phase samples per level to
average without aliasing. Verified a priori on the tangent statistics:
P = 5 realizes the derived fourth-order orientation tensor to machine
zero; P = 3 and P = 4 carry aliased residuals (7.4e-3, 4.6e-3) and
CANNOT express the derived isotropy in principle. The f = 1/3 and
f = 1/4 members are therefore out of the instrument's validity class
for B2/B5 (retained as reported context); the adjudicating member is
f = 1/5 (p = lambda/5 <= lambda/4, in regime, isotropy-capable).
Bars unchanged. Sampling requirement derived before the member ran.

## FOURTH ADDENDUM (2026-08-12): engine calibration at the null

The isotropic-stiffness null medium (w with (bh.t)^2 replaced by its
isotropic average 1/3) on the uncalibrated stencil shows spread
0.206 and polarization split 0.202 -- ABOVE the wound medium's own
numbers and above the bars: raw B2/B5 were unpassable in principle
(central-force cubic anisotropy, a Cauchy artifact of the engine,
not the medium). Correction per TAV3 precedent, instrument fixed at
its own control: NNN spring shell weighted by g relative to NN,
calibrated ON THE NULL ONLY (blind to the wound medium); the
calibration lands on g = 2 EXACTLY (the closed-form isotropy
condition for NN+NNN central-spring cubic lattices, not a fitted
number), null spread 0.0014, null split 0.0000. g = 2 frozen and
applied identically to straight control and wound members. Bars
B1-B5, CTRL, probe set, verdict rule ALL UNCHANGED.
