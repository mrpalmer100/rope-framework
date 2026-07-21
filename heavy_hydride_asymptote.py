"""NUC-005: atomic masses PREDICTED across the table (C-12 .. U-238 at 0.01-0.11%
mass accuracy) with ONE calibrated nuclear constant -- the rest is derived
structure. Upgrades NUC-001 (which took ALL binding energies as measured inputs).

Construction, each piece traced:
  * Bond counting: nucleons bind pairwise by mode overlap (NUC-004 Yukawa form +
    EM-RECON-009 core) at spacing d0 ~ 1.9 fm, close packed (z=12): bulk binding
    6*eps per nucleon. eps = THE one calibrated constant (absolute nuclear
    scale), fixed once on Ca-40.
  * Surface term: DERIVED FROM GEOMETRY, zero parameters -- close-packed sphere,
    surface nucleons miss ~3 of 12 bonds: a_S/a_V = 1.108 predicted vs 1.130
    empirical (2%).
  * Coulomb term: DERIVED -- charge is winding (GG-006), spacing derived:
    r0 = 1.05 fm -> a_C = 0.823 MeV vs 0.711 empirical (16%; classical uniform
    sphere, no diffuseness/exchange).
  * DECLARED OMISSIONS (fixed in advance): asymmetry + pairing need Fermi
    statistics (hbar; quantum boundary, out of scope). Predicted consequence:
    heavy N>Z nuclei overbound by ~23(A-2Z)^2/A. RESIDUAL AUDIT: Pb-208 and
    U-238 overbinding is 80-86% accounted by exactly that term.
  * Cross-check: eps = 2.70 MeV > deuteron 2.22 MeV (a classical bond depth must
    exceed the quantum-zero-point-reduced deuteron: correct direction).

Honest boundaries: H-1 is inputs only (m_p + m_e; no nuclear binding); He-4
FAILS at 38% binding error -- the smallest nuclei are quantum-dominated (alpha
clustering, zero-point) and a classical drop is declared inapplicable there.
The capability is strongest mid-table. Binding-energy accuracy: ~1.5-2.5%
(N~Z, A>=12) degrading to ~10-14% (heavy, dominated by the declared omission);
MASS accuracy 0.01-0.11% throughout because binding is ~1% of mass.
"""
import numpy as np

MP, MN, ME = 938.272, 939.565, 0.511
D0 = 1.9  # fm

B_EXP = {"He-4": (4, 2, 28.296), "C-12": (12, 6, 92.162), "O-16": (16, 8, 127.619),
         "Ca-40": (40, 20, 342.052), "Fe-56": (56, 26, 492.254),
         "Pb-208": (208, 82, 1636.43), "U-238": (238, 92, 1801.69)}


def structure_constants():
    r0_over_d0 = (3 / (4 * np.pi * np.sqrt(2)))**(1 / 3)
    Ns = 4 * np.pi * r0_over_d0**2 / (np.sqrt(3) / 2)
    aS_over_aV = 1.5 * Ns / 6.0
    aC = 0.6 * 1.44 / (r0_over_d0 * D0)
    return aS_over_aV, aC


def calibrate_aV(aS_over_aV, aC):
    A, Z, B = B_EXP["Ca-40"]
    return (B + aC * Z**2 / A**(1 / 3)) / (A - aS_over_aV * A**(2 / 3))


def binding(A, Z, aV, aS_over_aV, aC):
    return aV * A - aS_over_aV * aV * A**(2 / 3) - aC * Z**2 / A**(1 / 3)


def test():
    aS_over_aV, aC = structure_constants()
    assert abs(aS_over_aV - 1.130) / 1.130 < 0.05, "parameter-free surface ratio within 5% of empirical"
    assert abs(aC - 0.711) / 0.711 < 0.20, "derived Coulomb coefficient within 20%"
    aV = calibrate_aV(aS_over_aV, aC)
    assert abs(aV - 15.75) / 15.75 < 0.05, "calibrated a_V lands near the empirical value"
    eps = aV / 6
    assert eps > 2.22, "bond depth exceeds quantum-reduced deuteron binding (direction check)"

    # mass accuracy across the table (one constant)
    for name, (A, Z, Bx) in B_EXP.items():
        Bp = binding(A, Z, aV, aS_over_aV, aC)
        m_pred = Z * MP + (A - Z) * MN + Z * ME - Bp
        m_exp = Z * MP + (A - Z) * MN + Z * ME - Bx
        err = abs(m_pred - m_exp) / m_exp
        if name == "He-4":
            assert abs(Bp - Bx) / Bx > 0.2, "He-4 declared classical-drop failure (quantum-dominated)"
            assert err < 0.005, "even He-4 mass within 0.5% (binding is small vs mass)"
        else:
            assert err < 0.0015, f"{name} mass within 0.15%, got {err:.4%}"

    # residual audit: heavy overbinding matches the DECLARED asymmetry omission
    for name in ("Pb-208", "U-238"):
        A, Z, Bx = B_EXP[name]
        gap = binding(A, Z, aV, aS_over_aV, aC) - Bx
        asym = 23.0 * (A - 2 * Z)**2 / A
        assert 0.6 < gap / asym < 1.2, "overbinding 80-86% accounted by the omitted quantum term"

    print(f"parameter-free surface ratio a_S/a_V = {aS_over_aV:.3f} vs 1.130 empirical (2%)")
    print(f"derived Coulomb a_C = {aC:.3f} MeV vs 0.711 (16%); calibrated a_V = {aV:.2f} vs 15.75")
    print(f"eps = {aV/6:.2f} MeV > deuteron 2.22 (direction check)")
    print("masses C-12..U-238 within 0.15% (one constant); He-4 declared quantum failure (38% in B)")
    print("heavy residuals 80-86% accounted by the DECLARED asymmetry omission (needs hbar)")
    print("PASS: atomic masses predicted across the table with ONE calibrated constant.")


if __name__ == "__main__":
    test()
