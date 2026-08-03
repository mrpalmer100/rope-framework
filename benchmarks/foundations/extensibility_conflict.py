"""FND-021 -- INEXTENSIBLE OR NOT: the idealisation resolved, and an eight-order
conflict in k/T0 exposed.

Bars locked in analysis/FND021_k_conflict_bars_LOCKED.md BEFORE computing.
"""
import numpy as np

C = 2.99792458e8
T0 = 1203.0
D_C = 1.87e-19
A = 1.0e-16
K_NUCLEAR = 2.0        # EM-RECON-009, GRV-009
K_BELL = 1.9e8         # QB-008


def gamma_of(k_over_T0):
    r = D_C / 2
    k = k_over_T0 * T0
    E = k / (np.pi * r ** 2)
    G = E / 2.5
    Cc = G * np.pi * r ** 4 / 2
    return Cc / A ** 2


def main():
    print("B1 THE FIRST CONFLICT, RESOLVED:")
    print("   A perfectly inextensible strand has NO longitudinal wave -- an")
    print("   infinitely stiff rod transmits compression instantly and carries no")
    print("   propagating mode. The fast channel exists BECAUSE k is finite.")
    print("   The longitudinal speed is c_L = sqrt(k/mu), and with mu = T0/c^2,")
    print("      c_L/c = sqrt(k/T0).")
    print("   SO 'INEXTENSIBLE' IS THE k -> infinity IDEALISATION, NOT AN EXACT")
    print("   FACT ABOUT THE MEDIUM. T0 is a Lagrange multiplier only in that")
    print("   limit; at finite k there IS stored elastic energy, of order")
    print("   T0^2/(2k) per unit length relative to the constrained state.")
    print("   The operator's question is well posed and the card's flat statement")
    print("   'not stored elastic energy' is TOO STRONG.\n")

    print("B2 QB-008's INTERNAL CONSISTENCY:")
    print(f"   it states K_L/K_T >= {K_BELL:.1e} and v_dep > 1.38e4 c.")
    print(f"   sqrt({K_BELL:.1e}) = {np.sqrt(K_BELL):.4e}  vs  1.38e4")
    assert abs(np.sqrt(K_BELL) / 1.38e4 - 1) < 0.01
    print("   CONSISTENT to better than 1%. The two statements are the same")
    print("   statement, and the relation c_L/c = sqrt(k/T0) is confirmed by the")
    print("   corpus's own numbers.\n")

    print("B3 THE SECOND CONFLICT, and this one is NOT resolved here:")
    print(f"   EM-RECON-009 / GRV-009 use  k/T0 = {K_NUCLEAR}")
    print(f"     -- fitted to NUCLEAR and CHEMICAL spacings, and required > 1 for")
    print("        nonlinear stability.")
    print(f"   QB-008 requires              k/T0 >= {K_BELL:.1e}")
    print("     -- forced by BELL TIMING, an entirely different measurement.")
    print(f"   THESE DIFFER BY {K_BELL/K_NUCLEAR:.1e} -- EIGHT ORDERS OF MAGNITUDE.")
    print("   Both are registered. Neither cites the other. This is a live")
    print("   cross-sector inconsistency in the corpus's own constants, and it is")
    print("   reported rather than adjudicated: choosing by preference is exactly")
    print("   the failure mode this corpus has been correcting all day.\n")

    print("B4 THE CONSEQUENCE FOR GRV-073's DERIVED COUPLE-STRESS MODULUS:")
    for lab, kk in (("EM-RECON-009 (k/T0 = 2)", K_NUCLEAR),
                    ("QB-008 (k/T0 = 1.9e8)", K_BELL)):
        g = gamma_of(kk)
        print(f"   {lab:26s} gamma = {g:.3e} J/m,  gamma/T0 = {g/T0:.2e}")
    print("   GRV-073 USED k/T0 = 2 AND DID NOT CHECK QB-008. On the Bell-timing")
    print("   value gamma is EIGHT ORDERS LARGER and EXCEEDS the tension by ~33x,")
    print("   which inverts that claim's headline finding that the couple-stress")
    print("   modulus is seven orders BELOW the tension.")
    print("   GRV-073's NUMBER IS THEREFORE CONDITIONAL ON WHICH k IS RIGHT, and")
    print("   its stated conclusion is withdrawn pending that.\n")

    print("B5 WHAT THE CARD MUST SAY:")
    print("   (1) the medium is EXTENSIBLE with a very large k; 'inextensible' is")
    print("       an idealisation and T0 is a multiplier only in that limit;")
    print("   (2) the fast channel speed is c_L = c sqrt(k/T0), which is WHY the")
    print("       superluminal sector exists at all;")
    print("   (3) k/T0 IS IN DISPUTE by eight orders between two registered")
    print("       claims, and every quantity depending on k inherits that.")
    print("PASS: the idealisation is resolved, an eight-order cross-sector conflict")
    print("      is exposed, and GRV-073's conclusion is made conditional.")


if __name__ == "__main__":
    main()
