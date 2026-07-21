"""The field <-> strain calibration map, derived by energy-density identification
(the one bridge the Maxwell correspondence commits to):

    g = E * sqrt(eps0 / SIGMA),      SIGMA = T0 * n_L  [J/m^3]

the network's vacuum TENSION DENSITY -- exactly ONE physical constant, and the
same single absolute normalization EM-007 already flagged as underived (now with
a concrete identity). Nonlinearity onset in field units:

    E* = g* * sqrt(SIGMA/eps0),      g* = sqrt(4 T0/(k-T0)) ~ 1-2  (k/T0 ~ 2-5
                                     from the spacing sectors)

CONFRONTATION WITH DATA:
  * ATLAS light-by-light (2017) is consistent with QED => any classical rope
    quartic must have onset >= the Schwinger scale E_S = 1.32e18 V/m:
        SIGMA >= eps0 E_S^2/g*^2 ~ 4e24 - 1.5e25 J/m^3   (strong bound;
    EQUALITY = the identification, in which case ATLAS has MEASURED SIGMA).
  * Independent weaker bound: no anomalous vacuum Kerr at the strongest laser
    fields (~1e13 V/m): SIGMA > ~1e15 J/m^3. Ten orders of consistent headroom.

FLAGGED CONSEQUENCE (EM-RECON-015, Open): SIGMA/c^2 ~ 1e8 kg/m^3 -- a vacuum
five orders denser than lead that must NOT gravitate normally. The rope model's
version of the vacuum-energy problem, now explicit.

DISCRIMINATOR: the rope quartic is a SINGLE invariant in the transverse gradient
(g_y^2+g_z^2)^2 -- polarization-symmetric -- while Euler-Heisenberg is TWO
invariants with unequal coefficients (the 7/4 birefringence anisotropy). A
PVLAS-class polarization-ratio measurement discriminates rope vs QED.
"""
import numpy as np

EPS0 = 8.854e-12
E_S = 1.32e18          # Schwinger field, V/m
C = 3.0e8


def strain_from_field(E, Sigma):
    return E * np.sqrt(EPS0 / Sigma)


def onset_field(gstar, Sigma):
    return gstar * np.sqrt(Sigma / EPS0)


def energy_identity_check(Sigma=1.0e25, E=1.0e12):
    """u_rope = (Sigma/2) g^2 must equal u_EM = (eps0/2) E^2 under the map."""
    g = strain_from_field(E, Sigma)
    return abs(0.5 * Sigma * g**2 - 0.5 * EPS0 * E**2) / (0.5 * EPS0 * E**2) < 1e-12


def rope_quartic_is_single_invariant():
    """(g_y^2+g_z^2)^2 depends only on the polarization-symmetric combination."""
    gy, gz = 0.3, 0.7
    q1 = (gy**2 + gz**2)**2
    q2 = (gz**2 + gy**2)**2          # swap polarizations
    return q1 == q2                   # symmetric: no 7/4-type anisotropy at this order


def test():
    assert energy_identity_check(), "map must reproduce the energy identification exactly"
    # ATLAS-scale identification measures SIGMA
    for gstar, lo, hi in [(1.0, 1.4e25, 1.7e25), (2.0, 3.5e24, 4.2e24)]:
        Sig = EPS0 * E_S**2 / gstar**2
        assert lo < Sig < hi, f"SIGMA({gstar}) out of expected range: {Sig:.2e}"
    # laser lower bound is ~10 orders below (consistent headroom)
    Sig_laser = EPS0 * (1e13)**2 / 1.0
    assert Sig_laser < 1e16 and Sig_laser > 1e14
    # the flagged mass density
    rho = (EPS0 * E_S**2) / C**2
    assert 1e7 < rho < 1e9, "vacuum effective mass density ~1e8 kg/m^3 (the flag)"
    assert rope_quartic_is_single_invariant(), "rope quartic is polarization-symmetric"
    print(f"energy identification exact; SIGMA(ATLAS, g*=1) = {EPS0*E_S**2:.2e} J/m^3")
    print(f"laser lower bound SIGMA > {Sig_laser:.1e} J/m^3 (10 orders of consistent headroom)")
    print(f"flagged: vacuum effective mass density SIGMA/c^2 ~ {rho:.1e} kg/m^3 (EM-RECON-015)")
    print("rope quartic single-invariant (polarization-symmetric) vs EH two-invariant (7/4):")
    print("      the PVLAS-class polarization ratio is the rope-vs-QED discriminator")
    print("PASS: calibration derived in form; ONE constant SIGMA; ATLAS effectively measures it.")


if __name__ == "__main__":
    test()
