# The Photon Sector Repair: Substructure, Winding, and the Derived Angles
### The 2026-08-12 arc (FND-083 through FND-088), documented for the registry
*Mark Palmer, with the session record; every number regenerates from
claims.yaml and the named benchmarks.*

## 1. The problem this arc solved

Registered openly at FND-062 (route (c), 2026-08-11): the medium as
then specified could not carry the observed 1.4 PeV Galactic photons.
Two independent walls:
- THE LENGTH WALL: transverse coherence must be sampled at
  <= hbar c / E = 1.409e-22 m, five orders below the mesh spacing.
- THE DIRECTION WALL: the three straight strand axes make the
  accessible wavevector region a slab; PeV propagation would be
  confined to ~1e-9 of the sky, against all-sky LHAASO sources and
  FND-REL-002's derived isotropy.
Four escapes had been prosecuted and closed (FND-058..060 plus the
electron-anchor block on length tuning). The failure was disclosed at
full volume in KNOWN_LIMITATIONS.

## 2. The pricing (docs/T3_PHOTON_REPAIR_PRICING.md)

Five candidates were priced. Two were closed at pricing with kill
numbers on their face: network-waveguide rerouting (point-source
pointing demands per-crossing deflection <= 1.3e-21 rad over ~1e37
crossings) and topological-excitation transport (same pointing wall;
the registered charge-carrier fence; 8.6e9 kink units per quantum
with no formation channel). The second-carrier route remained the
expensive fallback. The purchasable path was substructure plus
winding, and the pricing session found the key arithmetic error in
the standing block:

THE REDISTRIBUTION RESULT (FND-083, A1). The registered length-tuning
destruction held T0 fixed while shrinking the spacing, exploding
Sigma_vac by up to 1.5e15. The correct map for SUBSTRUCTURE divides
the tension among the sub-strands: T0_f = T0/n_sub, mu_f = mu/n_sub.
Under that map c^2 = T/mu, Sigma, and both Lorentz margins (6.1x,
10.5x at the two live kappa readings) are EXACTLY invariant. The
length wall is purchasable at zero Lorentz cost, with
n_sub ~ 4.6e9 - 1.3e10 per coarse cell at the base resolution and the
fine ceiling landing at 1.400 PeV exactly. The electron anchor
(T0 a = 2.6065e-14 J) reads the bundle envelope.

## 3. The direction wall: three commissions, two kept failures, one pass

FND-083 (SHIN2) established NECESSITY at coverage level: straight
fine strands cover 1e-9 of the sky (reproducing FND-059's number as
the instrument control); single-level helices cover 1.6e-4 -- five
orders better, five orders short; two-level winding covers the full
sky. Coverage was explicitly graded necessary-not-sufficient.

FND-084 (TAV3/TAV3B, Failed-and-kept): LOOSE winding (pitch >>
wavelength) scatters rather than carries -- the wave lives on locally
straight fiber and breaks at the turns. The time-domain instrument
was retired at its own control (INSTRUMENT-INVALID, taken not tuned);
the Bloch instrument delivered the verdict.

FND-085 (SHIN3, Failed-and-kept): PITCH-MATCHED winding (pitch ~
wavelength) is the resonant Bragg regime -- the worst case. But
SHIN3's G1 established the constructibility window (the 1/sin^2
tension compensation inside Lorentz margin) and the failure's trend
line pointed at the homogenization regime.

FND-086 (SHIN4, PASS): at pitch <= wavelength/4 the medium
homogenizes. Measured on the validated instrument: phase-speed
spread 0.36 percent (bar 5), group speed 0.86 everywhere (bar 0.3),
group aligned with k to 0.3 degrees (bar 15), plane-wave spectral
weight 0.92 -- the short wave IS an eigenmode of the wound medium,
while the straight control at the same wavelength stays obstructed at
45 percent spread. The two failures bracket the pass from above.

## 4. The adoption (FND-087)

GRANT-SUBSTRUCTURE-TIGHT, adopted by the author through the arc's
standing conditional authorization: the vacuum strand is a bundle of
finer sub-strands, tension-redistributed, over-resolved to
a_f <= lambda/4 at the highest carried photon energy, hierarchically
wound at two levels in the homogenization regime. Price on the face
at adoption: one new primitive family; four underived parameters;
sub-spacing winding radii with unpriced bending cost; the
collective-branch conditionality (light is the collective mode,
never guided -- required independently by LIV timing bounds).

## 5. The derivation (FND-088): the winding was never a choice

Isotropy of a fiber medium's homogenized response requires the
tangent distribution to satisfy exactly TWO moment conditions:
E[t_z^2] = 1/3 and E[t_z^4] = 1/5. Each winding level supplies one
angle. Therefore:

- HIERARCHY DEPTH TWO, BY THEOREM: one level gives constant
  t_z = sin psi, forcing E[t^4] = (E[t^2])^2 = 1/9 != 1/5. One line.
- THE FIRST ANGLE IS THE MAGIC ANGLE: sin^2(psi_1) = 1/3
  (psi_1 = 35.2644 deg) makes the second-moment condition hold
  identically -- the same 1/3 of NMR magic-angle spinning and
  isotropic fiber composites, arriving unforced.
- THE SECOND ANGLE IS ONE QUADRATIC: 35 u^2 - 30 u + 3 = 0 for
  u = sin^2(psi_2), roots (15 +- 2 sqrt 30)/35.
- THE LORENTZ FLOORS SELECT THE ROOT: the minus root spends 25.9x
  margin (excluded by both floors); the plus root spends 4.05x
  (inside 6.1x and 10.5x). Unique physical solution:
      psi_1 = 35.2644 deg,  psi_2 = 59.4444 deg.
- VERIFIED: the full fourth-order orientation tensor at these angles
  is isotropic to 2.9e-13. FND-REL-002's isotropy is recovered as a
  theorem of the derived winding at homogenized level.

The grant's underived parameters drop from four to two -- m and
n_sub, the absolute-scale class, where the corpus's standing position
(FND-MATTER-003 lineage) already locates the irreducible bottom.

## 6. The plain-English statement

The vacuum's strands are cables of far finer sub-strands. Splitting
the tension among them changes nothing measurable at ordinary
energies -- the speed of light, the vacuum energy, and every Lorentz
margin are exactly preserved -- but lets the medium carry wavelengths
the coarse cable cannot. The sub-strands wind helically, and the
winding winds again, turning several times within each wavelength of
the shortest light carried, so the wave sees only the average of all
directions: a perfectly isotropic medium. The two twist angles are
not adjustable: isotropy fixes them in closed form and the
framework's own Lorentz bound selects between the two mathematical
solutions. What remains free are two absolute scales -- how fine and
how many -- which is where physical theories normally bottom out.

## 7. The debt register (enforcement order)

1. FND-REL-002 re-derived on wound carriers at Derived grade -- the
   grant's return-to-adjudication trigger (the homogenized-level
   recovery in FND-088 is Modeled).
2. The analytic necessity proof that level one sits at the magic
   angle (the sweep found no magic-free solutions; exhaustiveness is
   quadrature, not proof).
3. The 3D two-polarization Bloch instrument.
4. The bending-cost pricing (kb, unscaled).
5. Predictions-paper and KNOWN_LIMITATIONS sync at the next release
   cut, including the candidate new entry below.

## 8. Candidate prediction (drafted, NOT yet registered)

A medium isotropic BY winding has structure at the winding scales.
Two directions worth chartering before any registration: (i) whether
the derived chirality hierarchy supplies PRED-002's owed
nineteen-order suppression of the structural scale in optical
observables (the T3 double-duty flag, now with derived angles);
(ii) whether photons approaching the over-resolved ceiling
m x 1.4 PeV acquire any winding-scale signature -- noting the soft
falsifier already on the grant (a confirmed photon above the ceiling
forces m upward).

## Appendix: claim and artifact index

FND-083 (SHIN2, coverage necessity); FND-084 (TAV3/TAV3B, loose
winding excluded); FND-085 (SHIN3, resonant winding excluded + the
G1 window); FND-086 (SHIN4, homogenized pass); FND-087 (the grant);
FND-088 (SHIN5, the derivation). Pricing:
docs/T3_PHOTON_REPAIR_PRICING.md. Bars and results under analysis/
with the commission names; benchmarks under benchmarks/foundations/.
Releases v3.21.2 through v3.22.1.

## 9. SUPPLEMENT (2026-08-12, same day, FND-089/090): debts 1-3 discharged

The debt register of section 7 is superseded: (1) FND-REL-002 is
re-derived on wound carriers at Derived grade, homogenized scope
(FND-090) -- the trigger delivered, not fired; (2) the necessity
question resolved SHARPENED -- the magic angle is forced at exactly
one level, not specifically level one, and the winding is unique up
to level relabeling (exhaustive exact solve); (3) the 3D
two-polarization Bloch instrument exists and PASSES at the derived
angles (FND-089, triply controlled, g = 2 closed-form calibration).
Remaining: the bending-cost pricing (kb) and the release-cut sync.
KNOWN_LIMITATIONS' photon entry is softened per the grant's own gate.
