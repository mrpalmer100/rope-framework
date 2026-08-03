"""GRV-073 -- K_0 DERIVED from registered constants: the strands are rods, the
corpus said so, and gamma is SEVEN ORDERS below the tension.

Bars locked in analysis/GRV073_K0_derived_bars_LOCKED.md BEFORE computing.
"""
import numpy as np

T0_SETS = {"lattice-anchored": 1203.0, "Sigma-route": 1.70e3}
K_OVER_T0 = 2.0          # EM-RECON-009 stability + GRV-009's evaluation point
D_C = 1.87e-4 * 1e-15    # HBAR-005 strand thickness, metres
A = 1.0e-16              # Lorentz-bound spacing
POISSON_FACTOR = 2.5     # G ~ E/2(1+nu), nu ~ 0.25


def main():
    print("B1 THE CORRECTION TO GRV-072, plainly:")
    print("   That claim said the corpus 'has never registered strand torsional")
    print("   rigidity' and had 'never said which its strands are'. BOTH ARE")
    print("   FALSE, and a full-corpus search found it:")
    print("     GRV-009 (Failed) specifies its primitives as (k, P-VOL,")
    print("     TORSION~r^4) 'with ZERO FREEDOM'. An r^4 torsion law IS the")
    print("     polar-moment law of a ROD. THE STRANDS ARE RODS AND THE CORPUS")
    print("     SAID SO -- in a claim registered Failed for an unrelated reason")
    print("     (it gave the wrong sign of spatial curvature), whose PRIMITIVES")
    print("     were never in question.")
    print("     GRV-005 states outright that the corpus possesses the FULL elastic")
    print("     constants (T0, mu, lambda, k, P-VOL).")
    print("   GRV-072's estimate was offered because I had not looked.\n")

    print("B2 THE DERIVATION, every relation named:")
    r = D_C / 2
    print(f"   strand radius r = d_c/2 = {r:.3e} m       (HBAR-005)")
    print(f"   stretch modulus k = {K_OVER_T0} T0           (EM-RECON-009, GRV-009)")
    print("   axial stiffness of a rod:  k = E A = E pi r^2   =>  E = k/(pi r^2)")
    print("   torsional rigidity:        C = G I_p = G pi r^4 / 2")
    print(f"   isotropic shear:           G = E/2(1+nu) ~ E/{POISSON_FACTOR}")
    out = {}
    for lab, T0 in T0_SETS.items():
        k = K_OVER_T0 * T0
        E = k / (np.pi * r ** 2)
        G = E / POISSON_FACTOR
        C = G * np.pi * r ** 4 / 2
        out[lab] = (T0, C)
        print(f"   {lab:18s} T0={T0:7.1f} J/m -> E={E:.3e} Pa, "
              f"G={G:.3e} Pa, C={C:.3e} J.m")
    print()

    print("B3 THE MEDIUM'S COUPLE-STRESS MODULUS:")
    print("   gamma = C x (strands per unit area) = C / a^2")
    for lab, (T0, C) in out.items():
        gam = C / A ** 2
        print(f"   {lab:18s} gamma = K_0 = {gam:.3e} J/m")
    print()

    print("B4 THE RATIO, and GRV-072's estimate does NOT survive:")
    for lab, (T0, C) in out.items():
        gam = C / A ** 2
        print(f"   {lab:18s} gamma/T0 = {gam/T0:.3e}")
    ratio = (out['lattice-anchored'][1] / A ** 2) / T0_SETS['lattice-anchored']
    assert ratio < 1e-5
    print("   GRV-072 estimated gamma ~ T0 at O(1). THE TRUTH IS SEVEN ORDERS")
    print("   SMALLER, and the reason is structural rather than accidental:")
    print("   the axial stiffness carries r^2 (a cross-sectional area) while the")
    print("   torsional rigidity carries r^4 (a polar moment). Their ratio leaves")
    print(f"   one factor of (r/a)^2 = {(r/A)**2:.2e}, and the strand is THIN.")
    print("   A DIMENSIONAL ESTIMATE COULD NOT HAVE FOUND THIS, because the")
    print("   suppression comes from a second length the estimate did not use.\n")

    print("B5 HONEST SCOPE:")
    print("   CORPUS-SPECIFIC: the r^4 torsion law (GRV-009), the stretch modulus")
    print("     and its k > T0 stability bound (EM-RECON-009), the thickness")
    print("     (HBAR-005), the spacing (ELEC-053), and the tension.")
    print("   STANDARD ROD MECHANICS, imported: E = k/(pi r^2), C = G pi r^4/2,")
    print("     and G ~ E/2.5 for an isotropic material. The last is the weakest")
    print("     link -- a strand's Poisson ratio is not registered, and G/E could")
    print("     move the answer by a factor of a few. IT CANNOT MOVE SEVEN ORDERS.")
    print("   WHAT WOULD CHANGE THE NUMBER MATERIALLY: a different strand")
    print("     thickness. gamma goes as r^2 at fixed k, so d_c is the sensitive")
    print("     input and it enters squared.")
    print("   K_0 IS NOW DERIVED, not estimated. GRV-071's count becomes FOUR")
    print("   ABSENT AND ONE DERIVED.")
    print("PASS: the corpus had the constants, GRV-072's estimate is replaced by a")
    print("      derivation, and the answer is seven orders from the guess.")


if __name__ == "__main__":
    main()
