"""ELEC-075 -- THE CORE MEETS THE STRAND SPACING: the size-mass incompatibility.

Bars locked in analysis/ELEC075_core_scale_bars_LOCKED.md BEFORE computing.
"""
import numpy as np

W = 5.774e-17          # ELEC-053, strand spacing
FM = 1e-15
ME_C2 = 8.1871e-14     # J
R_BOUND = 1e-3 * FM    # ELEC-036 conservative structure bound
T0S = {"Sigma-route": 1.70e3, "lattice-anchored": 1203.0}
K_R, K_E = 0.7642, 4.3136   # ELEC-074: r0 = K_R Delta, E = K_E T0 Delta^3


def main():
    print(f"INPUTS: w = {W:.3e} m = {W/FM:.4f} fm; r_bound = {R_BOUND/FM:.0e} fm;")
    print(f"        m_e c^2 = {ME_C2:.4e} J; r0 = {K_R} Delta; E = {K_E} T0 Delta^3\n")
    worst = 0.0
    for lab, T0 in T0S.items():
        print(f"=== T0 = {T0:.0f} J/m ({lab})")
        # B1
        D1 = R_BOUND / K_R
        E1 = K_E * T0 * D1 ** 3
        print(f"  B1 impose the SIZE bound: Delta = {D1:.3e} m = {D1/W:.4f} w")
        print(f"     -> E = {E1:.3e} J against m_e c^2 = {ME_C2:.3e} J")
        print(f"     -> the object is {ME_C2/E1:.2e} times TOO LIGHT")
        # B2
        D2 = (ME_C2 / (K_E * T0)) ** (1 / 3)
        r2 = K_R * D2
        print(f"  B2 impose the ELECTRON MASS: Delta = {D2:.3e} m, r0 = {r2:.3e} m")
        print(f"     -> r0 = {r2/FM:.3e} fm = {r2/W:.2e} strand spacings")
        print(f"     -> the object is {r2/R_BOUND:.2e} times TOO LARGE")
        # B3
        r1 = K_R * D1
        print(f"  B3 CONTINUUM CHECK: under B1, r0/w = {r1/W:.4f}")
        print(f"     the core sits {'INSIDE' if r1 < W else 'outside'} one strand spacing")
        worst = max(worst, ME_C2 / E1)
        print()

    print("B4 THE COMBINED VERDICT, unsoftened:")
    print("   The two constraints cannot be met together. Sized to respect the")
    print("   scattering bound, the object is ~1e37 times too light. Massed to be")
    print("   an electron, it is ~1e12 times too large -- a MICRON-SCALE object.")
    print("   E ~ T0 Delta^3 with a hadronic T0 simply cannot deliver an electron")
    print("   mass in an electron-sized volume; the cubic law is the problem, since")
    print("   it makes energy fall far too fast as the object shrinks.")
    print("   THIS IS A QUANTITATIVE FAILURE OF THE SOLITON PICTURE AS BUILT, and")
    print("   it is independent of which registered T0 is used.\n")

    print("B3/B4 THE CONTINUUM VERDICT, which decides ELEC-074's question:")
    print(f"   at the size bound the core radius is {K_R*R_BOUND/K_R/W:.4f} w --")
    print("   i.e. r0 sits at about 1.7 PERCENT of one strand spacing, deep inside")
    print("   the medium's own granularity. THE HARD CORE IS THE CONTINUUM FAILING,")
    print("   not a physical interior boundary. ELEC-074's hollow object is a")
    print("   feature of a description applied where it does not apply.\n")

    print("B5 BOTH REGISTERED T0 VALUES give the same verdict within a factor of")
    print("   1.4 on the mass and 1.1 on the size. The scale-chain fork (ELEC-053)")
    print("   is irrelevant here: the failure is 37 orders deep and the fork moves")
    print("   things by less than one.\n")

    assert worst > 1e30
    print("WHAT SURVIVES: the exact profile (ELEC-074), the scaling relations, and")
    print("the structural result that a stable localized solution EXISTS in this")
    print("medium. What fails is the identification of that solution with the")
    print("electron. The soliton is real in the model and it is not an electron.")
    print("PASS: the deciding test was run and it returned a clean negative.")


if __name__ == "__main__":
    main()
