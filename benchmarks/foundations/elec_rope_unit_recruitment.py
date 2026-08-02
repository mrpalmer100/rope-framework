"""ELEC-059 -- WHICH LENGTH SETS THE CAUSAL REACH: THE ROPE-WIDTH ESCAPE
EVALUATED, AND THE DIAMETER FOUND TO CANCEL EXACTLY.

Bars locked in analysis/ELEC059_rope_unit_bars_LOCKED.md BEFORE this ran.
"""
import numpy as np

HBAR = 1.054571817e-34
C = 2.99792458e8
FM = 1e-15
T_TUBE = 1.878e5
R_TUBE = 0.407 * FM
A_LORENTZ = 1e-16
W = A_LORENTZ / np.sqrt(3)
R_HE4 = 1.2 * 4 ** (1 / 3) * FM
TAU0 = 1.95              # ELEC-047, in units of (unit separation)/c


def main():
    T0 = T_TUBE / (3 * np.pi * (R_TUBE / A_LORENTZ) ** 2)
    T_need = 2 * np.pi * HBAR * C / R_HE4 ** 2
    N = T_need / T0
    print(f"B1 PROVENANCE OF tau0: ELEC-047's barrier coordinate s is the SEPARATION")
    print(f"   between the two reconnecting strands, with the segment length l = 4")
    print(f"   and the threshold d_c/w both expressed in w. tau0 = {TAU0} is therefore")
    print(f"   tied to the separation of the COHERENT UNITS by construction, not to an")
    print(f"   incidental unit. Rope width can only enter if the MEDIUM's units are")
    print(f"   ropes -- a different hypothesis, not a reinterpretation.\n")

    print("B2 THE GENERAL UNIT MODEL: medium unit = rope of k strands, diameter D = f w,")
    print("   tension k T0. Then the number of units needed is N_u = T_need/(k T0),")
    print("   the coherence radius is R_c = D sqrt(N_u), and the causal reach is")
    print("   c tau0 = 1.95 D. Therefore")
    print("       shortfall = R_c/(c tau0) = D sqrt(N_u) / (1.95 D) = sqrt(N_u)/1.95")
    print("   THE DIAMETER CANCELS EXACTLY. The premise that a wider unit helps is")
    print("   WRONG: widening the unit lengthens the reach and enlarges the required")
    print("   radius in the same proportion. Only the STRAND COUNT per unit matters.\n")
    print(f"   {'k':>4} {'N_u':>10} {'shortfall':>11}  (f is irrelevant; checked below)")
    for k in (1, 2, 4, 8, 12, 16):
        Nu = N / k
        print(f"   {k:4d} {Nu:10.2f} {np.sqrt(Nu)/TAU0:11.3f}")
    # explicit cancellation check across diameters
    for f in (1.0, 2.0, 2.2, 5.0):
        Nu = N / 2
        s = (f * W * np.sqrt(Nu)) / (TAU0 * f * W)
        assert abs(s - np.sqrt(Nu) / TAU0) < 1e-12
    print(f"   cancellation verified at f = 1.0, 2.0, 2.2, 5.0 (k = 2): "
          f"shortfall {np.sqrt(N/2)/TAU0:.3f} in every case.\n")

    k_close = N / TAU0 ** 2
    print(f"B3 THE THRESHOLD: closing requires sqrt(N/k)/1.95 <= 1, i.e.")
    print(f"   k >= N/1.95^2 = {k_close:.1f} strands per coherent unit.")
    print(f"   THE CORPUS'S ELECTRON IS TWO STRANDS (ELEC-041, clasp-and-loop), giving")
    print(f"   shortfall {np.sqrt(N/2)/TAU0:.3f} -- short by a factor "
          f"{k_close/2:.1f} IN CONSTITUENT COUNT, not in width.")
    print(f"   The gap has moved from a length question to a counting question.\n")

    print("B4 SCOPE, stated plainly: none of this touches the electron sector's")
    print("   5.2-decade gap (ELEC-057) or the 1/a degradation at small scale")
    print("   (ELEC-058) -- a factor of six in k is nothing against 1e4. It concerns")
    print("   ONLY the Lorentz ceiling, where ELEC-057 already excludes the hbar")
    print("   sector by 6.7x on the bound alone. Closing this gap would not reopen")
    print("   the fork.\n")

    print("B5 HONESTY: a medium whose coherent units are k-strand ropes is a DIFFERENT")
    print("   MEDIUM HYPOTHESIS from ELEC-038's one-medium declaration, in which the")
    print("   vacuum's constituents are strands. Any k >= 12 that closed this gap")
    print("   would be a new postulate about what the vacuum is made of, and would owe")
    print("   its own derivation of why k takes that value.")
    print("PASS: the width escape is closed by an exact cancellation; what survives")
    print("      is a sharper and smaller question about constituent count.")


if __name__ == "__main__":
    main()
