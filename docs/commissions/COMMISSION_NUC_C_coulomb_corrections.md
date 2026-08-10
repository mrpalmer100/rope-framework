# COMMISSION NUC-C: THE COULOMB DIFFUSENESS AND EXCHANGE CORRECTIONS
# (chartered 2026-08-06, Mark's go-decision, option one of the three named
# residuals. This is the CLASSICAL one -- the cheap, low-risk, in-reach
# residual, done first. NUC-B's valley-of-stability analysis showed the
# remaining drift is dominated by the corpus's own registered Coulomb miss:
# a_C = 0.823 (derived, uniform sphere) vs 0.711 empirical, +16%, and the
# predictor's own comment names the cause: "no diffuseness/exchange." Both
# are CLASSICAL corrections. NUC-C derives them. Pairing and shell remain
# separate go-decisions, NOT opened here.)

## The target (sharp, from the corpus's own registered miss)
The framework's Coulomb coefficient a_C = 0.823 MeV comes from a CLASSICAL
UNIFORM CHARGED SPHERE (charge = winding, GG-006; spacing r0 = 1.05 fm
derived). The empirical value is 0.711 MeV. The +16% is the corpus's own
declared omission, named in atomic_mass_predictor.py line 14: "classical
uniform sphere, no diffuseness/exchange." NUC-C derives the two missing
CLASSICAL corrections and tests whether they close the 16%:
  a_C(uniform 0.823) - diffuseness - exchange  ->  ~0.711 target.

## Why this is classical and in-reach (low quantum-wall risk)
Neither correction requires the quantum sector the framework has walled off:
- DIFFUSENESS: real nuclei have a surface thickness (~0.5-0.55 fm), so the
  charge is not a hard sphere. A diffuse (Fermi) charge distribution softens
  the 1/R Coulomb energy. This is classical electrostatics of a smooth
  charge profile -- and the framework ALREADY HAS the profile: the same
  healing-tail / surface structure (xi, the two-mode equilibrium) that
  NUC-B used for the mode overlap. The surface thickness is not a new input;
  it is the corpus's own xi.
- EXCHANGE: the Fermi-hole (exchange) term, standard SEMF form
  -0.36 Z^(4/3)/A^(1/3), reduces the Coulomb energy because like-charge
  nucleons avoid each other. In the framework this is the winding-winding
  correlation already implied by the exclusion structure NUC-B used; it is
  a classical correlation correction, not a quantum-field effect.
Both corrections REDUCE a_C (verified: correct sign, moving 0.823 toward
0.711), and their combined leading magnitude (~10-16%) is the right size.

## THE BARS -- GENEROUS ON THE SCIENCE (unchanged from NUC-A/B)
- SUCCESS IS WIDE: a_C landing anywhere in 0.68-0.75 MeV counts (empirical
  0.711 +/- ~5%), because the diffuseness prefactor carries the same
  profile-shape uncertainty flagged throughout the corpus. The point is to
  derive the reduction at the right scale from the corpus's own surface
  structure, not to hit 0.711 exactly.
- RIGHT SIGN, PARTIAL MAGNITUDE = A LEAD: if diffuseness + exchange reduce
  a_C in the right direction but under/overshoot, that is a live lead,
  pursued to the second prediction, not killed.
- THE SECOND PREDICTION (the arbiter, ALREADY BUILT): S2, the valley of
  stability in the NUC-A/B harness. NUC-B showed that swapping the empirical
  a_C into S2 collapses the U-238 drift from -8 to -3/-4. So the test is:
  does the DERIVED corrected a_C reproduce that S2 improvement? A derived
  a_C that flattens the valley drift the way the empirical value does
  GRADUATES. Also rerun S1 (table closure) to confirm nothing worsens.
- BLIND WHERE IT MATTERS: the diffuseness reduction is computed from the
  corpus's own xi / surface profile BEFORE comparing the result to 0.711.
  The surface thickness is the registered xi, not a fitted width.

## THE SCOPE CAP -- HARD (cost control, unchanged)
- NUC-C is the COULOMB CORRECTIONS, singular (diffuseness + exchange).
- PAIRING (a_P) and SHELL structure remain OUT OF SCOPE -- the two quantum
  tiers, explicitly NOT opened here, separate future go-decisions Mark makes
  with NUC-C's result in hand.
- No sub-commissions. One commission. Generous exploration within the
  Coulomb corrections, hard wall around it.

## READY TO RUN (verified 2026-08-06)
The predictor (atomic_mass_predictor.py) exposes the Coulomb term and the
S1/S2 harness runs in-package (NUC-A/B verified). NUC-C extends the same
harness: replace the uniform-sphere a_C with the diffuseness+exchange-
corrected derivation, rerun S1 and S2. The surface profile (xi) and the
winding-charge structure are already registered. No rebuild needed.

## PHASE STRUCTURE (one session)
- PRIMARY: derive the diffuseness reduction to the uniform-sphere Coulomb
  energy from the corpus's own surface profile (xi / two-mode healing
  length), and the exchange reduction from the winding-correlation / SEMF
  Fermi-hole form. Compute the corrected a_C.
- WINDOW CHECK: does corrected a_C land 0.68-0.75?
- SECOND PREDICTION: rerun S2 with the derived corrected a_C -- does the
  U-238 valley drift flatten toward the empirical-a_C result (-3/-4)? Rerun
  S1 to confirm no regression.
- REGISTER per the ladder below.

## Registrable outcomes (all acceptable)
1. DERIVED: diffuseness + exchange from the corpus's own surface structure
   give a_C in 0.68-0.75, and S2's valley drift flattens toward the
   empirical-a_C benchmark. The Coulomb sector's 16% miss is closed with no
   new constant, and the valley-of-stability prediction is now derived. The
   dominant NUC-B residual is resolved.
2. DERIVED-PARTIAL: the corrections land a_C closer but with a stated
   residual (e.g. diffuseness closes most, exchange prefactor uncertain).
   Real progress, residual named.
3. LEAD: right sign, magnitude off, S2 partially improved. Registered with
   the next test named.
4. BOUNDARY: the corpus's surface structure does NOT produce the right
   diffuseness reduction -- the honest negative, locating whether the
   Coulomb miss needs structure the framework lacks. Registered.

## Named for go-decision (NOT opened -- the two quantum tiers)
- PAIRING (a_P): the even-odd term, genuinely quantum (pairing correlation).
  Separate go-decision, honest quantum-wall risk.
- SHELL structure (~6 MeV rms): spin-orbit and shell closures (the missing
  28 in the 2,8,20,28 sequence). Deepest quantum tier. Separate go-decision.

## Depends on
NUC-B (the valley-drift residual attributed to Coulomb, the S1/S2 harness),
NUC-A (the harness and geometry), NUC-005 (a_C = 0.823, the uniform-sphere
derivation, the a_C assertion at 20%), GG-006 (charge = winding, the charge
source), EM-RECON-009 / the two-mode equilibrium (xi, the surface profile
the diffuseness uses). Scoped: pairing and shell are separate commissions.
