# COMMISSION NUC-D: THE SURFACE TERM ON THE DIFFUSE PROFILE
# (chartered 2026-08-06, Mark's go-decision. THE CLASSICAL COMPLETION --
# and, unusually, NOT optional: NUC-C corrected the Coulomb term and in
# doing so BROKE a hidden cancellation, leaving the model temporarily worse
# on table closure (S1 rms 6.3 -> 63.8) even as it derived the Coulomb
# sector and graduated the valley of stability. The regression is 97.8% a
# single smooth volume+surface shape; the +16% Coulomb error had been
# silently compensating the SHARP-SPHERE surface term. NUC-D recomputes the
# surface term on the SAME diffuse profile, jointly with the corrected
# Coulomb, ONE Ca-40 constant. This is the commission that turns NUC-C from
# "made the table worse" into "completed the classical model at better-than-
# ever accuracy." Pairing and shell remain the scoped quantum tiers.)

## The target (sharp, from NUC-C's regression diagnostic)
The current surface term is a_S/a_V = 1.108, derived from SHARP-SPHERE
bond-counting (surface nucleons miss ~3 of 12 bonds; NUC-006). After the
NUC-C Coulomb correction, the data prefer a_S/a_V ~ 1.25 -- and the
diagnostic showed 97.8% of NUC-C's S1 regression is exactly this
smooth volume+surface shape, with residual 3.4 MeV rms once removed.
NUC-D recomputes the surface term on the DIFFUSE density profile and
tests whether it lands ~1.25 and closes the table to ~3-4 MeV rms.

## Why this is classical, in-reach, and uses no new constant
The surface energy counts under-coordinated nucleons near the boundary. A
SHARP sphere has a monolayer surface; a DIFFUSE surface (the same Fermi
profile NUC-C used, width a_d = xi/2 = 0.70 fm from the registered xi)
spreads the boundary over a finite shell, so MORE nucleons are partially
coordinated -- raising the effective surface energy. This is the SAME
classical bond-counting the corpus already does (NUC-006), now evaluated
on the diffuse density instead of a step. Verified: the correction goes
the RIGHT DIRECTION (up, toward 1.25) and the right ballpark. The width is
the registered xi -- NO new constant.

## THE BARS -- GENEROUS ON THE SCIENCE (unchanged)
- SUCCESS IS WIDE: a_S/a_V landing in ~1.18-1.32 counts (the data prefer
  ~1.25; the diffuse-broadening prefactor carries the same profile-shape
  uncertainty flagged throughout). The point is the right scale from the
  corpus's own profile, not hitting 1.25 exactly.
- RIGHT DIRECTION, PARTIAL MAGNITUDE = A LEAD: if the diffuse surface
  raises a_S/a_V toward 1.25 but under/overshoots, that is a live lead,
  pursued to the second prediction, not killed.
- THE SECOND PREDICTION (the arbiter, ALREADY BUILT): S1 table closure in
  the NUC-A/B/C harness. The diagnostic PREDICTS the joint diffuse-surface +
  corrected-Coulomb model lands ~3-4 MeV rms table-wide. A recomputed
  surface term that closes S1 to ~3-4 MeV rms (recovering and surpassing
  NUC-B's 6.3) GRADUATES. Also confirm S2 (valley) stays graduated (it
  should -- the surface term is Z-symmetric, so it does not disturb the
  valley the Coulomb+asymmetry fixed).
- BLIND WHERE IT MATTERS: the diffuse surface energy is computed from the
  corpus's own xi / density profile BEFORE comparing a_S/a_V to 1.25.
- JOINT, ONE CONSTANT: surface and Coulomb are recomputed TOGETHER on the
  same diffuse profile, with the single Ca-40 calibration (a_V) unchanged.
  No per-term retuning.

## THE SCOPE CAP -- HARD (cost control, unchanged)
- NUC-D is the SURFACE TERM on the diffuse profile, singular (jointly with
  the already-derived Coulomb).
- PAIRING (a_P) and SHELL structure remain OUT OF SCOPE -- the two quantum
  tiers, NOT opened here, separate future go-decisions.
- No sub-commissions. One commission. NUC-D is the LAST CLASSICAL PIECE:
  after it, the model is at its classical completion (~3-4 MeV rms floor),
  and what remains is genuinely quantum.

## READY TO RUN (verified 2026-08-06)
The NUC-A/B/C harness runs in-package. NUC-D extends it: recompute the
surface energy on the diffuse density (same xi, same Fermi profile as
NUC-C's Coulomb), form a_S/a_V, and rerun S1 (and confirm S2 holds) with
the joint diffuse surface + corrected Coulomb at NUC-B's a_A. The profile,
xi, and bond-counting geometry are all registered. No rebuild.

## PHASE STRUCTURE (one session)
- PRIMARY: recompute the surface energy by counting under-coordinated
  nucleons on the diffuse Fermi density profile (width a_d = xi/2), giving
  a_S/a_V. Compare to ~1.25.
- JOINT CLOSURE: rerun S1 with the diffuse surface + NUC-C corrected
  Coulomb + NUC-B asymmetry, one Ca-40 constant. Does it land ~3-4 MeV rms?
- CONFIRM S2 holds (valley should be undisturbed by the Z-symmetric surface
  term).
- REGISTER per the ladder below.

## Registrable outcomes (all acceptable)
1. CLASSICAL MODEL COMPLETE: diffuse surface gives a_S/a_V ~1.25, and the
   joint model closes S1 to ~3-4 MeV rms with the valley still graduated.
   The classical nuclear mass model is COMPLETE at its natural floor, with
   the broken cancellation resolved (both surface and Coulomb now diffuse,
   one constant). What remains (~3-4 MeV rms) is the shell/pairing quantum
   structure, cleanly separated. NUC-C's regression is RESOLVED.
2. COMPLETE-PARTIAL: the surface term lands close and S1 improves toward
   3-4 but with a stated residual. Real progress, residual named.
3. LEAD: right direction, magnitude off, S1 partially recovered. Registered
   with next test named.
4. BOUNDARY: the diffuse surface does NOT produce a_S/a_V ~1.25 or does not
   recover S1 -- the honest negative, meaning the regression was not (only)
   the surface term. Registered; locates the residual precisely. (Note: this
   would leave the model in NUC-C's temporarily-worse state, so a boundary
   here specifically flags that the classical completion is not where the
   diagnostic predicted, an important finding.)

## Named for go-decision (NOT opened -- the two quantum tiers, unchanged)
- PAIRING (a_P): the even-odd term, genuinely quantum. Separate go-decision.
- SHELL structure (~6 MeV rms of the remaining ~3-4, the magic-number and
  spin-orbit residual): deepest quantum tier. Separate go-decision.
After NUC-D the classical program is complete and BOTH remaining tiers are
quantum -- the natural stop-and-decide point.

## Depends on
NUC-C (the diffuse Fermi profile, a_d = xi/2, the corrected Coulomb, the
regression diagnostic identifying the surface term as the residual), NUC-B
(the a_A asymmetry, the harness), NUC-A (the harness and geometry), NUC-006
(the sharp-sphere surface bond-counting a_S/a_V = 1.108 that NUC-D
generalizes to the diffuse profile), NUC-005 (a_V, the one Ca-40 constant),
EM-RECON-009 / two-mode equilibrium (xi, the profile width). Scoped:
pairing and shell are separate commissions.
