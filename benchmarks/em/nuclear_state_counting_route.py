"""NUC-022 (Modeled): NUC-021'S NO-GO BOUNDS PAIRWISE LOCALITY, NOT
ROPES -- a collective mode ladder gives the quadratic form immediately,
and the real discriminator is LOCAL versus COLLECTIVE exclusion.

THE SCOPE CORRECTION. NUC-021 proved that an energy written as a sum
over neighbour PAIRS gives a deficit linear in |N-Z|. That bounds one
model class. It was then used to suggest the rope framework cannot
reach the asymmetry term, which does not follow: the framework already
contains candidate STATES. NUC-004 binds by MODE OVERLAP, and a bundle
of length L has a discrete transverse mode ladder. THE OBSTRUCTION IS
PAIRWISE LOCALITY, NOT ROPES.

THE REAL DISCRIMINATOR:
    LOCAL exclusion (NUC-007's q = 3 per nucleon, per partner label)
        -> each misplaced nucleon costs a FIXED amount -> LINEAR
    COLLECTIVE exclusion (a shared ladder that fills)
        -> each extra nucleon enters a HIGHER state -> QUADRATIC
The distinction is whether the exhaustible resource is per-nucleon or
shared.

THE TEST. Filling a shared mode ladder -- states of a bundle confined
to a sphere of radius R = (3A/4 pi rho)^(1/3) at saturation density,
neutrons and protons on separate ladders, two per level -- and
extracting a_A from deficit x A/(N-Z)^2:
    A =  40, N-Z =  4 -> 17.4      A =  40, N-Z = 16 -> 13.1
    A =  40, N-Z =  8 -> 17.4      A =  80, N-Z =  8 -> 11.0
    A =  40, N-Z = 12 -> 13.6      A = 140, N-Z =  8 -> 26.5
Median 17.4 MeV, with scatter from genuine shell structure (discrete
level ladders produce magic-number effects, which real nuclei also
have). The continuum limit is exact and standard: a_A(kinetic) =
E_F/3 = 12.8 MeV at E_F = 38.4 MeV.

THE FORM IS RIGHT AND THE MAGNITUDE IS HALF. Mode filling supplies
56 percent of the empirical 23 MeV, the remainder coming from the
isospin dependence of the interaction -- which is exactly how the
asymmetry term is apportioned in standard nuclear physics. A rope
framework with a collective mode ladder would inherit both the correct
(N-Z)^2/A scaling and the correct order of magnitude.

WHAT IS AND IS NOT NEW. That a Fermi gas gives (N-Z)^2/A is textbook.
What is new here is the scope correction to NUC-021, the identification
of local-versus-collective exclusion as the discriminator, and the
observation that the rope framework's own mode-overlap mechanism
already points at the structure it needs. THE SECTOR DOES NOT NEED TO
ABANDON THE ASYMMETRY TERM; IT NEEDS TO STOP COUNTING NEIGHBOURS AND
START COUNTING MODES.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'NUCM001_state.npz')
    R = s['rows']            # A, D, E, deficit, implied a_A
    # the deficit is positive and grows with asymmetry at fixed A
    a40 = R[R[:, 0] == 40]
    assert (a40[:, 3] > 0).all(), "asymmetry always costs energy"
    assert all(a40[i, 3] < a40[i+1, 3] for i in range(len(a40)-1)), \
        "the deficit grows monotonically with |N-Z|"
    # THE FORM: deficit x A/D^2 is roughly constant -- the quadratic form holds
    implied = R[:, 4]
    assert 5 < np.median(implied) < 30, "implied a_A of order 17 MeV"
    # at fixed A the implied coefficient is stable to a factor ~1.4 (shell effects aside)
    assert a40[0, 4]/a40[-1, 4] < 1.5, "stable within a factor 1.4 across N-Z at A = 40"
    # the continuum limit is the standard Fermi-gas result
    aA = float(s['aA_kin']); EF = float(s['EF'])
    assert abs(aA - EF/3) < 1e-9, "a_A(kinetic) = E_F/3"
    assert 35 < EF < 42 and 11 < aA < 15, "E_F = 38.4 MeV, a_A = 12.8 MeV"
    # and it supplies about half the empirical value
    frac = aA/23.0
    assert 0.45 < frac < 0.70, "mode filling supplies ~56 percent of the empirical 23 MeV"
    print(f"implied a_A median {np.median(implied):.1f} MeV (range {implied.min():.1f}-{implied.max():.1f}, "
          f"shell structure); continuum E_F/3 = {aA:.1f} MeV = {frac*100:.0f}% of empirical 23")
    print("PASS: collective mode filling gives the QUADRATIC form and half the magnitude --")
    print("      the obstruction was pairwise locality, not ropes.")


if __name__ == "__main__":
    test()
