# COMMISSION EM-RECON-036 -- THE REGISTERED-CLASS CLOSURE -- BARS LOCKED (2026-08-15)

Locked BEFORE any integral is evaluated. This is EM-RECON-035's named
successor: the core closure run, for the first time in the arc, on the
profile the registry itself wrote. Zero profile freedom.

## THE PROFILE, quoted from registered structure (B1)
MODE_OVERLAP_DERIVATION.md Sec 2 / harness line 13:
    psi(r) = w(rho_perp/xi) e^(-rho/xi) e^(i s phi),
    w(u) = u/sqrt(1 + u^2),
where rho = |r - center| (SPHERICAL envelope at the healing length)
and rho_perp = distance from the mode's winding axis m (CYLINDRICAL
core factor, vanishing on the axis). The strain amplitude entering
the quartic energy is the scalar magnitude
    f(r) = w(rho_perp/xi) e^(-rho/xi),
matching the prior closures' use of scalar profiles. The mode is a
3D object; the closure integrals are 3D. All lengths in xi units.

## AMPLITUDE MAPPING (B2)
The registered amplitude meaning in this arc is PEAK STRAIN = g (the
1D benchmark's g e^(-|x|/xi) peaks at g). The registered profile
vanishes on its axis, so the peak is interior:
    g(r) = g* f(r)/f_max,  f_max = max over space of f,
computed once analytically/numerically at lock quality. Operating
amplitude policy unchanged: verdict at g* = 2; sweep over g in
[1, 3] displayed, never used.

## ORIENTATION (B3)
The registered mode has an axis; two modes at separation d have a
relative geometry. NO orientation is chosen by hand. Three canonical
configurations are computed at every d: (a) COAXIAL, both axes along
the separation vector; (b) PARALLEL-TRANSVERSE, axes parallel to each
other, perpendicular to the separation; (c) CROSSED, axes mutually
perpendicular, both perpendicular to the separation. The physical
equilibrium is the (d, configuration) minimizing the energy; the
verdict is read at that minimum. All three curves displayed.

## ENERGY, METHOD, ANCHORS (B4)
E(d) = -(T0/2) I2 + c4 (4 I31 + 6 I22 + 4 I13), c4 = T0/8, with
I_mn = Int f1^m f2^n d^3x, both f at amplitude per B2. Numerics: 3D
grid; convergence by grid doubling with the equilibrium stable to
better than 1 percent; integrator anchored on an analytic 3D
Gaussian-overlap identity to 0.1 percent before any profile number
is read. The 1D regression anchor (6.1566) stands re-verified this
session already (EM-RECON-034's run).

## TARGETS, BANDS, VERDICT GRAMMAR (B5)
Targets and bands unchanged: nuclear d0/xi in [1.02, 1.70]; chemical
in [1.2525, 2.0875]; joint [1.2525, 1.70]. Zero free parameters, so:
- PASS: equilibrium d0/xi inside the JOINT band at g* = 2.
- PARTIAL: inside exactly one band; the band is named; registered as
  partial, not spun, and nothing downstream consumes it.
- FAIL: outside both bands, or NO-MINIMUM at g* = 2. Kept.
No idealization window exists to argue with; the number is the
number.

## REFUSALS (B6)
- No profile modification, no envelope swap, no core-factor
  amendment after any number is seen.
- No orientation invented beyond the three canonical ones; no
  intermediate-angle scan bolted on after seeing results.
- No amplitude off-policy; no touching c4 = T0/8 or k/T0 = 2.
- No consumption by downstream claims this session regardless of
  verdict.

## DELIVERABLE (B7)
Benchmark benchmarks/em/emrecon036_registered_class_closure.py; one
registered claim EM-RECON-036 with the verdict, all three orientation
curves' equilibria, the convergence and anchor records, and the
amplitude sweep on its face; chain annotations; CHANGELOG;
verify_corpus --quick green; re-zip.

## FAILURE MODES NAMED IN ADVANCE
- Orientation-shopping (defended at B3: the energy chooses).
- Reading PARTIAL as PASS in prose (the day's known surface).
- Trusting an unanchored 3D integrator (defended at B4).
- Any whisper of profile adjustment: the entire point of this
  commission is that the profile is not ours to touch.
