"""Atomic masses from nucleon-knot count minus rope-mode-overlap binding.

The nuclear paper (rope_nuclear_physics) models the neutron as a COMPLETE knot
(udd, zero NET winding but full nucleon mass), so the mass-bearing rope quantity
is the nucleon-knot count A = protons + neutrons -- NOT the net winding (charge)
Z. Atomic mass is then the sum of constituent-knot masses minus the binding
energy (identified as rope mode overlap energy, peaking at Fe-56):

    M(atom) = Z*m_p + N*m_n + Z*m_e  -  BE/c^2

This benchmark verifies that, GIVEN measured binding energies, this structure
reproduces real atomic masses to <0.1% across the periodic table. It also shows
that the naive 'mass ~ net winding (charge) Z' FAILS (blind to neutrons, off by
up to ~2x), which is why the nucleon-knot count is the correct quantity.

SCOPE (honest): the binding energies are MEASURED INPUTS. The paper identifies
binding = rope mode overlap and explains the Fe-56 peak qualitatively (optimal
knot packing) but does NOT yet derive the binding curve from rope parameters
(its own open problem). So this is REPRODUCTION-given-binding + a mechanism story,
not a from-scratch prediction. Registered as NUC-001.
"""
u = 931.494          # MeV per amu
m_p, m_n, m_e = 938.272, 939.565, 0.511  # MeV

# (name, Z, N, measured atomic mass amu, total binding energy MeV)
DATA = [
    ("H-1",  1,   0,   1.007825,    0.0),
    ("He-4", 2,   2,   4.002602,   28.30),
    ("Li-7", 3,   4,   7.016004,   39.24),
    ("C-12", 6,   6,  12.000000,   92.16),
    ("O-16", 8,   8,  15.994915,  127.62),
    ("Fe-56",26, 30,  55.934936,  492.25),
    ("U-238",92,146, 238.050788, 1801.7),
]


def predicted_mass(Z, N, BE):
    return (Z * m_p + N * m_n + Z * m_e) / u - BE / u


def test():
    # (1) nucleon-knot count + binding reproduces atomic mass to <0.1%
    worst = 0.0
    for name, Z, N, meas, BE in DATA:
        pred = predicted_mass(Z, N, BE)
        err = abs(pred - meas) / meas
        worst = max(worst, err)
        assert err < 1e-3, f"{name}: {err:.4%} exceeds 0.1%"
    # (2) naive 'mass ~ net winding Z' FAILS: weight/Z is NOT constant
    ratios = [meas / Z for _, Z, N, meas, BE in DATA]
    spread = max(ratios) / min(ratios)
    assert spread > 1.8, "mass~Z should fail by ~2x (it does)"
    print(f"nucleon-knot count + binding reproduces atomic mass: worst error {worst:.4%}")
    print(f"naive mass~charge(Z) fails: weight/Z spread = {spread:.2f}x (blind to neutrons)")
    print("PASS: correct rope quantity for mass is nucleon-knot count A, not winding Z;")
    print("      reproduces masses <0.1% GIVEN measured binding (binding not yet derived).")


if __name__ == "__main__":
    test()
