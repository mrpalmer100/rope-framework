"""ELEC-060 -- PRICING THE TWO-MEDIUM OPTION: THE ONLY UNEXPLORED BRANCH OF
THE FORK, EVALUATED IN ITS THICK/THIN INSTANTIATION.

Bars locked in analysis/ELEC060_two_medium_bars_LOCKED.md BEFORE this ran.
"""
import numpy as np

HBAR = 1.054571817e-34
C = 2.99792458e8
FM = 1e-15
T_TUBE = 1.878e5
R_TUBE = 0.407 * FM
A_LORENTZ = 1e-16
R_HE4 = 1.2 * 4 ** (1 / 3) * FM
A_G4 = 6.746e-16        # ELEC-057: hbar sector needs a >= this
A_ELECTRON = 4.726e-21  # ELEC-057: electron needs a <= this


def main():
    # P1
    print("P1 DOES SPLITTING THE MEDIUM RESCUE THE HBAR SECTOR?")
    print(f"   ELEC-057's G4 requires a >= {A_G4:.3e} m; the Lorentz bound is "
          f"{A_LORENTZ:.1e} m.")
    print(f"   The shortfall is {A_G4/A_LORENTZ:.2f}x and it is against the BOUND, not")
    print("   against the electron sector. The Lorentz bound constrains VACUUM")
    print("   structure, and the hbar-carrying medium IS the vacuum, so splitting")
    print("   off a separate matter species does not relieve it.")
    print("   VERDICT: TWO MEDIA RESCUE THE ELECTRON ONLY. The hbar sector remains")
    print("   excluded by the same 6.7x, unaided, in the two-medium world too.\n")

    # P2
    print("P2 THE FLUX-TUBE BRANCH POINT (which species composes the measured tube):")
    T0_a = T_TUBE / (3 * np.pi * (R_TUBE / A_LORENTZ) ** 2)
    L_a = np.sqrt(2 * np.pi * HBAR * C / T0_a)
    print(f"   (a) TUBE = VACUUM STRANDS: T0 = T_tube/n = {T0_a:.1f} J/m stays MEASURED,")
    print(f"       L = {L_a/FM:.2f} fm vs the {R_HE4/FM:.2f} fm needed -- ELEC-057's")
    print(f"       exclusion is inherited intact. Nothing is gained for hbar.")
    T0_need = 2 * np.pi * HBAR * C / R_HE4 ** 2
    print(f"   (b) TUBE = MATTER ROPES: the vacuum tension is FREED from measurement.")
    print(f"       The hbar sector then requires T0 = {T0_need:.3e} J/m, a factor")
    print(f"       {T0_need/T0_a:.2f} above the currently derived value.")
    print(f"       BUT: that number is now FITTED, not derived. The corpus's ONE")
    print(f"       external anchor on the medium (the hadronic tube tension) has been")
    print(f"       handed to the other species, and with it every scale the HBAR and")
    print(f"       NUCQ chains inherited. This does not solve the hbar problem; it")
    print(f"       makes the hbar sector unfalsifiable by removing its measurement.\n")

    # P3
    print("P3 THE RATIO between species:")
    ratio = A_LORENTZ / A_ELECTRON
    print(f"   thick/thin = {ratio:.2e} = {np.log10(ratio):.1f} decades.")
    print("   Nothing in the corpus supplies this number: it is set by the electron")
    print("   sector's 2e4 form-factor discrepancy on one side and the Lorentz bound")
    print("   on the other, neither of which predicts a species ratio.")
    print("   IT IS A NEW FREE PARAMETER, and it is a large unexplained one.\n")

    # P4
    print("P4 THE COUPLING CONSTRAINT:")
    print("   ELEC-040's tension matching (an electron rope must be a whole number of")
    print("   vacuum strands) was FORCED by one medium. Under two media it lapses --")
    print("   which removes a constraint the electron sector was failing, but at a")
    print("   price: the two species must still interact, since matter must couple to")
    print("   the vacuum that carries its fields. No mechanism for cross-species")
    print("   coupling is derived, and a 4.3-decade mismatch in constituent scale is")
    print("   exactly the regime where a coupling is hardest to arrange.")
    print("   NOTHING IS GAINED THAT IS NOT IMMEDIATELY OWED BACK.\n")

    # P5
    print("P5 THE LEDGER:")
    print("   SURVIVES: the electron geometry gets a scale it can use (the 2e4 closes");
    print("             at the thin scale); the standing-wave FORM S = pi T A^2/(2c);")
    print("             the QCD-anchored tube physics, under whichever species owns it.")
    print("   LOST:     the one-medium declaration and the unification that motivated")
    print("             the framework; ELEC-040's tension-matching constraint; and in")
    print("             branch (b), the corpus's only external anchor on the vacuum.")
    print("   NET FREE PARAMETERS: +1 (the species ratio, 4.3 decades = 2.1e4, underived;")
    print("             distinct from ELEC-057's 5.2-decade G4-to-G2 gap, which is the")
    print("             separation of the two sectors' REQUIREMENTS, not of the species),")
    print("             +1 more in branch (b) (the freed vacuum tension). The hbar")
    print("             sector is NOT rescued in either branch.")
    print("   CONCLUSION: the abandonment branch of ELEC-057's fork does not buy what")
    print("   the fork was posed to buy. It relieves the electron sector at the cost")
    print("   of the framework's central claim, and leaves the hbar sector excluded")
    print("   exactly as before. THE FORK IS THEREFORE NOT A CHOICE BETWEEN TWO LIVE")
    print("   OPTIONS: retiring the hbar sector is required in both branches, and the")
    print("   only question the split actually decides is whether the electron sector")
    print("   is kept at the price of the unification.")
    print("PASS: the last unexplored branch is priced, and it is dearer than it looked.")


if __name__ == "__main__":
    main()
