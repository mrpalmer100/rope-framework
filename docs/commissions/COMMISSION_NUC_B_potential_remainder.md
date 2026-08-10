# COMMISSION NUC-B: THE POTENTIAL REMAINDER OF THE SYMMETRY ENERGY
# (chartered 2026-08-06, Mark's go-decision. NUC-A DERIVED the kinetic
# asymmetry coefficient a_A(kinetic) = 16.6 MeV from level-filling and
# closed ~87% of the 13% gap (S1: heavy-table 8.8% -> 1.17%). S2 (valley
# of stability) drifts to -10 protons at U-238, sizing a MISSING quadratic
# piece at ~2.5-3 MeV. NUC-B tests whether that remainder is the collective
# mean-field isospin dependence of mode overlap. Same GENEROUS science bars,
# same HARD scope cap as NUC-A.)

## The target (sharp, from NUC-A's S2 diagnostic)
Produce, from the framework's mode-overlap mean field, the ~2.5-3 MeV
QUADRATIC potential contribution to the symmetry energy that NUC-A's
kinetic term leaves on the table. Combined target: a_A(kinetic 16.6) +
a_A(potential) should land the effective coefficient in the empirical
19-23 range AND fix S2's heavy-A valley drift (the -10 at U-238 -> near 0).

## The critical distinction (why this is NOT the excluded channel)
NUC-A already confronted a potential asymmetry channel and it FAILED
twice, so NUC-B must be a DIFFERENT object:
- The EXCLUDED channel (V4, dead): LOCAL per-nucleon capacity (NUC-021
  theorem) gives a LINEAR |N-Z| deficit -- wrong shape -- and the data
  bounded it to 0.45 +/- 0.13 MeV, <~11% of naive. NUC-B must NOT be this.
- The V3 channel (dead): full-a_V isospin bonds gave 32.8, overshooting,
  and WORSENED S1 (rms 58.3). NUC-B must NOT be this either.
- NUC-B's channel: the COLLECTIVE MEAN-FIELD isospin dependence -- the
  mode-overlap integrals differ for like vs unlike nucleon pairs at the
  MEAN-FIELD (not local-count) level, which is collective and therefore
  QUADRATIC-shaped ((N-Z)^2/A), the right shape, and expected small
  (~2.5-3, not ~a_V). This is the mean-field average of the overlap
  asymmetry, distinct from both the local capacity count and the full-bond
  channel.

## THE BARS -- GENEROUS ON THE SCIENCE (unchanged from NUC-A)
- SUCCESS IS WIDE: a_A(potential) landing in ~1.5-4 MeV counts (the S2
  diagnostic sized it ~2.5-3, but the mean-field estimate carries
  profile-prefactor uncertainty, so a band is honest). The COMBINED
  coefficient landing in the empirical 19-23 is the real target.
- RIGHT SHAPE, OFF MAGNITUDE = A LEAD: if the mean-field overlap gives the
  quadratic shape but a coefficient outside the band, it is a live lead,
  pursued to a second prediction, not killed.
- THE SECOND PREDICTIONS (the arbiters, ALREADY BUILT in nuc_a_asymmetry.py):
  S1 (279-nuclide table closure) and S2 (valley of stability). The
  combined kinetic+potential coefficient must IMPROVE S1 toward the
  audit's fitted-19.26 closure (~0.6% heavy-table) AND flatten S2's heavy-A
  drift. A potential term that closes S1 further AND fixes the U-238 drift
  GRADUATES. One that worsens either (as V3 did) DIES.
- LOOK HARD, KEEP CANDIDATES: variants of the mean-field overlap
  (profile choices, the like/unlike overlap ratio's derivation) may be
  explored, each owing a second prediction.
- BLIND WHERE IT MATTERS: the overlap-asymmetry ratio is derived from the
  mode structure BEFORE its coefficient is compared to the 2.5-3 target.

## THE SCOPE CAP -- HARD (cost control, unchanged)
- NUC-B is the POTENTIAL REMAINDER of the symmetry energy, singular.
- PAIRING (a_P) and SHELL structure (~6 MeV rms magic-number residual)
  remain OUT OF SCOPE -- the already-scoped separate tiers, NOT opened here.
- No sub-commissions. Follow-ons are NAMED for Mark's go-decision.
- One commission. Generous exploration WITHIN the potential term, hard wall
  around it.

## READY TO RUN (verified 2026-08-06)
nuc_a_asymmetry.py runs against the package (deps present: periodictable,
atomic_mass_predictor with structure_constants/calibrate_aV/binding/D0;
results reproduce: a_A=16.6, r^2=0.85, S1 8.8%->1.17%, S2 drift to -10).
NUC-B EXTENDS this script: add the mean-field overlap-asymmetry term as a
new candidate a_A(potential), form the combined coefficient, and rerun the
EXISTING S1/S2 harness. No rebuild needed -- the setup, ladders, geometry,
and both second-prediction functions are already in place.

## PHASE STRUCTURE (one session)
- PRIMARY: derive the like-vs-unlike mode-overlap integral ratio from the
  framework's mode structure (NUC-004 Yukawa overlap + EM-RECON-009 core);
  take its MEAN-FIELD (collective) average to get the quadratic asymmetry
  coefficient a_A(potential); confirm the (N-Z)^2/A shape.
- COMBINE: a_A(total) = 16.6 (kinetic, NUC-A) + a_A(potential); check it
  lands 19-23.
- SECOND PREDICTIONS: rerun S1 (does the combined coefficient close the
  table toward 0.6%?) and S2 (does it flatten the U-238 drift from -10?).
- REGISTER the outcome per the ladder below.

## Registrable outcomes (all acceptable)
1. DERIVED: mean-field overlap gives a_A(potential) ~2.5-3 with the right
   shape, combined coefficient lands 19-23, S1 closes toward 0.6% AND S2's
   heavy drift flattens. The symmetry energy is now FULLY derived (kinetic
   + potential), and essentially all of the 13% gap is derived physics.
   The nuclear mass sector's classical program reaches its natural
   completion (only pairing + shell remain, both quantum-kinetic).
2. DERIVED-PARTIAL: the potential term lands and improves S1/S2 but leaves
   a stated residual (e.g. S2 better but not flat). Real progress, residual
   named.
3. LEAD: right shape, magnitude off, one second prediction partial.
   Registered as a lead with its next test named. Not a failure.
4. BOUNDARY: the mean-field overlap does NOT produce a quadratic term of
   the right size, or worsens S1/S2 -- the honest negative locating where
   the remainder actually lives (possibly the quantum-kinetic layer).
   Registered; the ~2.5-3 stays a declared omission, boundary sharpened.

## Depends on
NUC-A (a_A kinetic = 16.6, the S1/S2 harness, the well setup -- NUC-B
extends its script), NUC-021 (the local-capacity exclusion theorem -- NUC-B
must be the COLLECTIVE channel, not this), NUC-022 (the kinetic/potential
apportionment, now revised to ~85% kinetic), NUC-004 (Yukawa mode overlap),
EM-RECON-009 (the core), NUC-005 (the binding model and a_V). Scoped:
pairing and shell structure are separate future commissions.
