# COMMISSION NUC-D2: THE CURVATURE TERM (CLASSICAL COMPLETION)
# (chartered 2026-08-06, Mark's go-decision. THE LAST CLASSICAL BRICK. NUC-D
# recovered the table to 11.9 MeV rms and left the missing piece explicit: a
# smooth +3.1 A^(2/3) - 0.25 A - 7.1 A^(1/3) shape, dominated by the A^(1/3)
# CURVATURE term, whose removal lands the model at ~4.5 MeV rms = the quantum
# shell/pairing floor. NUC-D2 recomputes the finite-range bond kernel to next
# order in 1/R -- which naturally produces the A^(1/3) curvature energy -- to
# absorb that smooth shape and land the classical model at its floor. Same
# generous-science / bounded-scope discipline. After NUC-D2 the classical
# program is COMPLETE and only the quantum tiers remain.)

## The target (sharp, from NUC-D's residual shape)
NUC-D's best one-constant model (finite-range kernel + NUC-C Coulomb + NUC-B
asymmetry) sits at table rms 11.9 MeV, heavy-table 1.05%, with the missing
piece an EXPLICIT smooth shape: +3.1 A^(2/3) - 0.25 A - 7.1 A^(1/3), whose
removal leaves 4.47 MeV rms (the shell floor). The A^(1/3) CURVATURE term
(coefficient -7.1) is the dominant piece and the named target. NUC-D2
recomputes the bond kernel to O(1/R) and tests whether the derived curvature
+ jointly-recalibrated surface/volume absorb this smooth shape, landing the
table at ~4-5 MeV rms.

## Why this is the last classical brick, in-reach, no new constant
The finite-range coordination deficit that gave NUC-D's surface term
(~A^(2/3)) has a NEXT ORDER in the surface curvature 1/R. Since R ~ A^(1/3),
curvature ~ A^(-1/3), and curvature-energy ~ (area) x (curvature) ~
A^(2/3) x A^(-1/3) = A^(1/3) -- exactly the missing term's shape. This is
the SAME integral (same contact radius r_c = 2.40 fm from z = 12, same eps),
carried one order further in the Leptodermous (surface + curvature)
expansion. NO new constant: the volume is recalibrated once on Ca-40 as
before, and surface + curvature come from the same kernel geometry. After
this order, the smooth (liquid-drop) expansion is exhausted and what remains
is the genuinely quantum shell/pairing structure.

## THE BARS -- GENEROUS ON THE SCIENCE (unchanged)
- SUCCESS IS WIDE: the derived curvature coefficient landing in a band that
  absorbs most of the -7.1 A^(1/3) shape counts (the exact coefficient
  carries the same profile-prefactor uncertainty flagged throughout; the
  standard curvature coefficient is itself model-dependent and debated). The
  point is the right shape and scale from the kernel's next order, not an
  exact number.
- RIGHT SHAPE, PARTIAL MAGNITUDE = A LEAD: if the kernel's O(1/R) term gives
  the A^(1/3) shape but under/overshoots -7.1, it is a live lead, pursued to
  the second prediction, not killed.
- THE SECOND PREDICTION (the arbiter, ALREADY BUILT): S1 table closure in
  the NUC-A/B/C/D harness. The diagnostic PREDICTS the joint curvature +
  surface + Coulomb + asymmetry model lands ~4-5 MeV rms table-wide (the
  shell floor). A derived curvature term that closes S1 to ~4-5 MeV rms
  GRADUATES. Confirm S2 (valley) stays graduated (curvature is Z-symmetric,
  so it should not disturb the valley).
- BLIND WHERE IT MATTERS: the curvature energy is computed from the kernel's
  O(1/R) expansion BEFORE comparing its coefficient to the -7.1 target.
- JOINT, ONE CONSTANT: surface + curvature recomputed together on the same
  kernel, volume recalibrated once on Ca-40. No per-term retuning.

## THE SCOPE CAP -- HARD (cost control, unchanged)
- NUC-D2 is the CURVATURE TERM, singular (jointly with the already-derived
  surface/Coulomb/asymmetry).
- PAIRING (a_P) and SHELL structure (the ~4.5 MeV rms floor) remain OUT OF
  SCOPE -- the two quantum tiers, NOT opened here, separate future
  go-decisions. NUC-D2 is the LAST CLASSICAL PIECE; after it, the smooth
  liquid-drop expansion is exhausted and everything remaining is quantum.
- No sub-commissions. One commission.

## READY TO RUN (verified 2026-08-06)
The NUC-A/B/C/D harness runs in-package (all four scripts verified). NUC-D2
extends nuc_d_surface.py: carry the coordination-deficit integral to O(1/R)
(curvature), form the joint surface + curvature energy, recalibrate volume
on Ca-40, and rerun S1 (confirm S2 holds). The kernel, r_c, z = 12, and eps
are all registered. No rebuild.

## PHASE STRUCTURE (one session)
- PRIMARY: expand the finite-range coordination deficit to next order in the
  surface curvature 1/R, giving the A^(1/3) curvature energy from the same
  kernel. Confirm the A^(1/3) shape and extract the coefficient.
- JOINT CLOSURE: rerun S1 with curvature + surface + NUC-C Coulomb + NUC-B
  asymmetry, one Ca-40 constant. Does it land ~4-5 MeV rms?
- CONFIRM S2 holds (valley undisturbed by the Z-symmetric curvature term).
- REGISTER per the ladder below.

## Registrable outcomes (all acceptable)
1. CLASSICAL MODEL COMPLETE: the derived curvature term absorbs the smooth
   A^(1/3) shape and the joint model closes S1 to ~4-5 MeV rms with the
   valley still graduated. The classical (liquid-drop) nuclear mass model is
   COMPLETE at its natural floor, entirely derived at one Ca-40 constant
   (volume calibration) with surface, curvature, Coulomb, and symmetry energy
   all from framework structure. What remains (~4.5 MeV rms) is purely the
   quantum shell/pairing tier, cleanly separated. The 13%-gap campaign's
   classical phase is DONE.
2. COMPLETE-PARTIAL: the curvature term lands close and S1 improves toward
   4-5 but with a stated residual. Real progress, residual named.
3. LEAD: right shape, magnitude off, S1 partially improved. Registered with
   the next test named.
4. BOUNDARY: the kernel's O(1/R) term does NOT produce the A^(1/3) shape or
   does not close S1 -- the honest negative, meaning the missing smooth shape
   is not (only) the curvature term. Registered; locates the residual
   precisely (and would be a genuine surprise, since the shape argument is
   clean).

## Named for go-decision (NOT opened -- the quantum tiers, unchanged)
- PAIRING (a_P): the even-odd term, genuinely quantum. Separate go-decision.
- SHELL structure (~4.5 MeV rms): spin-orbit and shell closures (the missing
  28 in the 2,8,20,28 sequence, NUC-007's declared miss). Deepest quantum
  tier. Separate go-decision.
- Also owed (small, classical): the overlap-order (B1/B2) and hole-depth
  (C1/C2) derivations, decidable in the deuteron/He-4 sector. Tidy-up.
After NUC-D2 the classical program is complete and the natural stop-and-
decide point is reached: everything remaining is quantum-wall-risk.

## Depends on
NUC-D (the finite-range bond kernel, the 11.9 MeV model, the explicit
missing A^(1/3) shape), NUC-C (the Coulomb), NUC-B (the asymmetry), NUC-A
(the harness), NUC-006 (the surface bond-counting the curvature extends),
NUC-005 (the one Ca-40 constant). Scoped: pairing and shell are separate
quantum commissions.
