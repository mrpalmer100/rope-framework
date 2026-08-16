# COMMISSION EM-RECON-034 -- THE 2D PROFILE COMPUTATION -- BARS LOCKED (2026-08-15)

Locked BEFORE any integral is evaluated. This is EM-RECON-031's named
successor route 2 (a 2D/3D profile computation of the same
cross-terms), authorized by the author this session. Suspect (ii)'s
wound-bundle half was eliminated at EM-RECON-032; its DIMENSIONAL half
is what stands trial here. Verbatim-verdict discipline applied per the
GRV-117 lesson: EM-RECON-031's mechanism, quoted from its face, is
that in 1D the g1^3 g2 cross-terms decay at the same exponential rate
as the attraction and renormalize it downward, demolishing the compact
model at saturation amplitude.

## QUESTION
Does the same zero-free-parameter quartic closure, with the SAME
registered inputs (c4 = T0/8 from the adjudicated k/T0 = 2; operating
amplitude locked at the Kerr saturation strain g* = 2; the same
targets and bands), produce an equilibrium standoff d0/xi inside the
registered bands when the mode profile is the honest 2D transverse
one -- ropes are line objects, bound modes decay in the two
transverse dimensions -- instead of the 1D exponential idealization?

## THE PROFILE CLASS, fixed at lock (B1)
The 2D evanescent bound-mode profile around a line source with decay
length xi is K0(r/xi). K0 diverges logarithmically on the axis, so a
core regularization is REQUIRED and is physical (the field cannot
exceed its rope-surface value): the profile is
    g(r) = g* K0(max(r, r_w)/xi) / K0(r_w/xi),
capped flat inside the rope radius r_w and normalized so the SURFACE
STRAIN equals the operating amplitude, matching the 1D benchmark's
amplitude meaning (peak strain = g).

## THE IDEALIZATION WINDOW, fixed at lock (B2)
r_w/xi is UNREGISTERED (the rope radius hangs on n_rs per FND-110's
ladder; the healing length is the medium's). It is therefore swept,
not chosen: r_w/xi in [0.05, 0.5], eleven log-spaced points, all
displayed. It is an idealization parameter and the grammar below
prevents it from becoming a fit.

## ENERGY AND METHOD, fixed at lock (B3)
Identical structure to the failed benchmark, upgraded in dimension
only: E(d) = -(T0/2) I2 + c4 (4 I31 + 6 I22 + 4 I13) per unit rope
length, with I_mn = Int g1^m g2^n d^2x over the transverse plane,
centers separated by d. Equilibrium d0 = interior minimum of E(d),
none = NO-MINIMUM. Numerics: 2D grid, convergence checked by grid
doubling; the 1D benchmark re-run first as a regression anchor (must
reproduce 6.16 at g* = 2 before any 2D number is read).

## TARGETS AND BANDS, unchanged from EM-RECON-031 (B4)
Nuclear d0/L = 1.36; chemical bond/healing = 1.67; bands +-25
percent, the registered log-weak honesty level. Amplitude policy
unchanged: verdict at g* = 2; sensitivity over g in [1, 3] displayed,
never used for the verdict.

## OUTCOMES, pre-committed (B5)
- PASS: d0/xi inside BOTH bands at g* = 2 across the ENTIRE r_w/xi
  window. Consequence: the 1D idealization is convicted as
  EM-RECON-031's failure mechanism, suspect (i) (the saturation
  identification) is exonerated at this order, and EM-RECON-008's
  missing input collapses to the remaining profile question.
- INDICATED: inside both bands on a SUB-INTERVAL of the window; the
  sub-interval is named, the result is registered as an indication
  conditional on the unregistered r_w/xi, and EM-RECON-008 stays
  Open with the gap narrowed to that one ratio. NOT a pass; nothing
  downstream may consume it.
- FAIL: inside both bands nowhere in the window (or NO-MINIMUM
  across it). Registered and kept; the dimensional suspect dies
  alongside the wound-bundle one, and suspect (i) or the compact
  model's truncation inherit the residual.
- Mixed per-target outcomes resolve to the WORST of the two targets.

## REFUSALS (B6)
- No amplitude chosen off-policy; no r_w/xi cherry-picked; no 3D run
  bolted on after seeing 2D numbers (3D is a separate cut if ever).
- No touching c4 = T0/8, k/T0 = 2, or the adjudication that fixed
  them.
- No consumption of a PASS by bond-length or nuclear-spacing claims
  this session: consequence registration only, one step at a time.
- No softening of FAIL. The house keeps failures.

## DELIVERABLE (B7)
Benchmark benchmarks/em/emrecon034_2d_profile_closure.py; one
registered claim EM-RECON-034 with the verdict, the full window
table, the regression anchor, and the amplitude sweep on its face;
EM-RECON-008 and EM-RECON-031 annotated per outcome; CHANGELOG;
verify_corpus --quick green; re-zip.

## FAILURE MODES NAMED IN ADVANCE
- The window becoming a knob: the grammar above is the whole defense,
  fixed before any number exists.
- Reading INDICATED as PASS in the prose layer (the day's known
  failure surface).
- Skipping the 1D regression anchor and trusting a fresh integrator.
