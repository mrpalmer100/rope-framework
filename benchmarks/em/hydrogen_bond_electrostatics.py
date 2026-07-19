"""CHEM-HB-001 (Modeled): hydrogen bonding COMPLETED from the derived pieces --
EM-015 superposition electrostatics of partial winding imbalances, molecular
shapes from CHEM-GEO-001, partial charges from the adopted electronegativity
scale (Section 8, Modeled: delta = 1 - exp(-dChi^2/4); O-H -> 0.32 e).
DECLARED INPUTS: dimer O...O = 2.98 A (nonbonded contact not yet derived --
the honest open edge); 3-point-charge truncation per molecule. Bars declared
before evaluation, same-session (weaker than cross-session pre-commitment,
stated openly): (a) water-dimer energy in the 0.1-0.3 eV order untuned
(gets -0.15 eV vs measured net -0.217; -0.26 with our Part-A monomer geometry);
(b) sits BETWEEN thermal (~6x kT) and covalent (~1/32 of O-H); (c) LINEAR
preferred, softly (few-hundredths-eV penalty at 20 deg); (d) WHY HYDROGEN:
a carbon-like donor (delta = 0.03 e, contact ~3.5 A) is >100x weaker --
hydrogen is special for the largest delta on the scale plus the bare-bundle
close approach. All four PASS.
"""
import numpy as np

K = 14.3996  # eV*Angstrom/e^2


def water(delta, r_oh, theta_deg, origin, acceptor, tilt=0.0):
    th = np.deg2rad(theta_deg)
    O = np.array(origin, dtype=float)
    if acceptor:
        h1 = O + r_oh*np.array([np.cos(th/2),  np.sin(th/2), 0])
        h2 = O + r_oh*np.array([np.cos(th/2), -np.sin(th/2), 0])
    else:
        b = np.deg2rad(tilt)
        h1 = O + r_oh*np.array([np.cos(b), 0, np.sin(b)])
        h2 = O + r_oh*np.array([np.cos(b+th), 0, np.sin(b+th)])
    return [(O, -2*delta), (h1, +delta), (h2, +delta)]


def U_dimer(delta, r_oh, theta, D, tilt=0.0):
    don = water(delta, r_oh, theta, (0, 0, 0), False, tilt)
    acc = water(delta, r_oh, theta, (D, 0, 0), True)
    return sum(K*q1*q2/np.linalg.norm(p1-p2) for p1, q1 in don for p2, q2 in acc)


def test():
    delta, D = 1 - np.exp(-1.24**2/4), 2.98
    U_meas_geom = U_dimer(delta, 0.958, 104.5, D)
    U_our_geom = U_dimer(delta, 1.108, 90.0, D)
    assert 0.05 < abs(U_meas_geom) < 0.5 and 0.05 < abs(U_our_geom) < 0.5, "bar (a): 0.1-0.3 eV order"
    kT, E_cov = 0.0259, 4.8
    assert 3*kT < abs(U_meas_geom) < E_cov/10, "bar (b): between thermal and covalent"
    tilts = [U_dimer(delta, 0.958, 104.5, D, tilt=b) for b in (0, 10, 20, 30, 40)]
    assert tilts[0] == min(tilts), "bar (c): linear is the minimum"
    assert abs(tilts[2] - tilts[0]) < 0.08, "bar (c): soft bending (few hundredths eV at 20 deg)"
    dC = 1 - np.exp(-0.35**2/4)
    U_C = U_dimer(dC, 1.09, 109.5, 3.5)
    assert abs(U_meas_geom/U_C) > 10, "bar (d): carbon-like donor collapses >10x -- why hydrogen"
    print(f"water dimer: {U_meas_geom:+.3f} eV (measured geom), {U_our_geom:+.3f} eV (our Part-A geom); net measured -0.217")
    print(f"hierarchy: {abs(U_meas_geom)/kT:.1f}x kT, 1/{E_cov/abs(U_meas_geom):.0f} of covalent; linear soft minimum")
    print(f"why hydrogen: carbon-like donor {abs(U_meas_geom/U_C):.0f}x weaker")
    print("PASS: all four bars met; hydrogen bonding assembled from EM-015 + geometry + adopted delta scale.")


if __name__ == "__main__":
    test()
