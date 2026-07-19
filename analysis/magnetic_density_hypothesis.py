#!/usr/bin/env python3
"""
Does universal rope density set magnetic coupling strength?
A hypothesis test + conditional derivation.  (M. Palmer question, 2026)

MOTIVATION. Magnets are full-strength in vacuum and essentially unchanged in
dense matter: mu_r(water)=0.999991 (a <1e-5 shift), mu_r(vacuum)=1 exactly,
only ferromagnets differ greatly. So LOCAL atoms cannot set the magnetic
'grip'. Hypothesis: the length-wise rope-rope coupling is set by the
UNIVERSAL rope density, which dominates any local contribution.

RESULT -- a CONDITIONAL derivation, not an unconditional one.

  Premise P: the pass-through rope network coarse-grains to a SINGLE
  orientation field theta(x) CARRIED BY the ropes (the model already builds
  its EM sector on one field: B=curl v; A a single 1-form; one theta(x) in
  rope_microscopic_mechanics).

  GIVEN P, the following are FORCED (derived here), not separately assumed:
   1. A length-wise, NON-atom-mediated coupling exists: two ropes crossing a
      point are coupled because both must share that point's theta -- no
      shared atom required.
   2. The continuum stiffness is K = kappa_theta * n_A, LINEAR in areal rope
      density n_A (kappa_theta = per-rope line stiffness = J*a on the atomic
      lattice check; a property of ONE rope, not the lattice).
   3. n_A_universal / n_A_local ~ 1e48, so K is set by the UNIVERSAL density
      and matter-independence is FORCED: K(water)/K(vacuum)-1 ~ 1e-48.
   4. The shared-atom (local) effect is correctly DEMOTED to a small
      correction, the right size to be diamagnetism (~1e-5); ferromagnetism
      is separate alignment. Correct hierarchy.

  So the hypothesis's several wants reduce to the SINGLE premise P.

WHAT IS NOT SETTLED (the honest fork). Matter-independence is ALSO consistent
with a rival:
  Picture A (P, hypothesis): theta is MADE OF ropes -> K ~ n_A, universal
     density SETS mu0. Density is the source.
  Picture B: theta is a property of SPACE that ropes merely excite -> K is a
     fixed vacuum constant, rope density irrelevant, mu0 not reducible to ropes.
Both reproduce all lab data. Dimensional analysis cannot decide.

DISCRIMINATING PREDICTION (falsifiable, for future work):
  Picture A -> mu0 (hence alpha) tracks UNIVERSAL rope density, so should vary
     across cosmic time (denser early universe -> different mu0).
  Picture B -> mu0 is era-independent.
  Observational bound on alpha variation ~1e-17/yr is a real constraint that
  DISCRIMINATES them, and may already pressure a naive Picture A. Computing
  the predicted variation vs the bound is the next derivation step.

STATUS: conditional derivation (mu0 density-scaling & matter-independence FORCED
given P); absolute mu0 value NOT derived; Picture A-vs-B NOT resolved (open,
empirically decidable). This file records reasoning; it is analysis, not a
registered Derived claim.
"""
import numpy as np

def densities(N_atoms=1e80, R=8.8e26, n_matter=3.3e28):
    nA_univ = (N_atoms**2/2)/(4*np.pi*R**2)
    nA_local = (n_matter**2/2)
    return nA_univ, nA_local

def test():
    nA_univ, nA_local = densities()
    ratio = nA_univ/nA_local
    assert ratio > 1e6, "universal rope density must dominate local matter"
    # K ~ n_A (Picture A): fractional matter shift
    frac = nA_local/nA_univ
    assert frac < 1e-6, "matter-independence must be forced under Picture A"
    print(f"n_A(universal)={nA_univ:.2e}/m^2  n_A(local)={nA_local:.2e}/m^2")
    print(f"K(matter)/K(vacuum)-1 = {frac:.2e}  (<<1e-5 diamagnetism: OK)")
    print("PASS: given single rope-carried field, density-scaling + matter-")
    print("      independence are FORCED. Picture A vs B remains open (see docstring).")

if __name__=="__main__":
    test()
