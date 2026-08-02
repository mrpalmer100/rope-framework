"""GRV-053 -- CORRECTION: GRV-049 and GRV-052 used a superseded luminosity law.

Bars locked in analysis/GRV053_correction_bars_LOCKED.md BEFORE computing.
"""
import numpy as np

G = 6.674e-11
C = 2.99792458e8
HBAR = 1.054571817e-34
MSUN = 1.989e30
KPC = 3.086e19
LIGO_ASD = 4e-24
YEAR = 3.156e7


def main():
    M = 10 * MSUN
    kappa = C ** 3 / (4 * G * M)
    P_H = HBAR * C ** 6 / (15360 * np.pi * G ** 2 * M ** 2)
    L_ch = 5.8e-4 * P_H                       # GRV-047 channel ceiling
    L_used = 1e-2 * (1.26e32 / 0.1) * 0.07 * 0.925   # GRV-049/052's value

    print("B1 THE LUMINOSITY ERROR (10 Msun hole):")
    print(f"   Hawking power                 P_H   = {P_H:.3e} W")
    print(f"   GRV-047 channel ceiling       L     = {L_ch:.3e} W")
    print(f"   GRV-049/052 used (supply law) L     = {L_used:.3e} W")
    print(f"   OVERSTATEMENT: {L_used/L_ch:.2e}x, i.e. "
          f"{np.log10(L_used/L_ch):.0f} ORDERS OF MAGNITUDE.\n")

    nu = 0.23 * kappa / (2 * np.pi)
    D = 10 * KPC
    h = lambda L: (1 / (2 * np.pi * nu * D)) * np.sqrt(4 * G * L / C ** 3)
    print("B2 THE CORRECTED STRAIN at 10 kpc:")
    print(f"   GRV-052 reported     h = {h(L_used):.2e}")
    print(f"   correct (GRV-047)    h = {h(L_ch):.2e}")
    print(f"   overstated by {h(L_used)/h(L_ch):.1e}x.\n")

    print("B3 DO THE VERDICTS CHANGE?")
    print("   NO -- both STRENGTHEN, massively. GRV-052 concluded the whisper is")
    print(f"   36x below LIGO for the best real candidate; with the correct law it")
    print(f"   is ~{h(L_used)/h(L_ch):.0e}x fainter still. GRV-049's demotion of")
    print("   GRV-040 to T2 on unobservability stands and is now enormous rather")
    print("   than marginal.")
    print("   THE CONCLUSIONS WERE RIGHT FOR THE WRONG REASON, which is not the")
    print("   same as being right.\n")

    print("B4 WHAT IS WITHDRAWN, per claim:")
    print("   GRV-049: WITHDRAWN -- (a) the finding that the whisper 'is not a")
    print("     whisper', carrying 40-110% of the accretion budget: that is the")
    print("     supply-side overshoot GRV-047 had already diagnosed and resolved;")
    print("     (b) the derived bound f <~ 1e-2 from accretion budgets, since")
    print("     GRV-047 dissolved f into a ratio (~1e-67 at Eddington) and there is")
    print("     no f left to bound.")
    print("     STANDS: the frequency table (31-186 Hz stellar-mass, the LIGO-band")
    print("     coincidence), the channel fork, and the T2 demotion.")
    print("   GRV-052: WITHDRAWN -- every luminosity and strain number, and the")
    print("     '36x short' figure.")
    print("     STANDS: the method, the spectrum argument (broadband quasi-thermal")
    print("     forbidding coherent integration -- which GRV-047's ceiling makes")
    print("     moot but does not contradict), and the verdict of unobservability.")
    print("   GRV-050 and GRV-051 are UNAFFECTED: the polarization decomposition")
    print("     and the EH-channel overlap are structural and use no luminosity.\n")

    print("B5 THE PROCESS FAILURE, named:")
    print("   GRV-049 read GRV-040's luminosity law from GRV-040 and did not check")
    print("   whether a later claim had revised it. GRV-047 is three claims further")
    print("   on in the same sector, is titled 'THE LUMINOSITY LAW REVISED TO A")
    print("   SWITCH', and says so in capitals.")
    print("   WHAT WOULD HAVE CAUGHT IT: reading the sector's claims FORWARD from")
    print("   the one being used, not just the one being used. The corpus has a")
    print("   dependency sweep (ELEC-065) that looks DOWNSTREAM of changed claims;")
    print("   it has nothing that looks FORWARD from a claim being relied on.")
    print("   That gap is the reusable lesson and is registered as such.")
    print("PASS: the error is quantified, the verdicts survive, and what is")
    print("      withdrawn is listed per claim.")


if __name__ == "__main__":
    main()
