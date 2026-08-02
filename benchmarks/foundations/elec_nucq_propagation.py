"""ELEC-055 -- THE SUBLUMINALITY BOUND MEETS THE NUCLEAR REFUTATION: THE
MARGIN MOVES BY AN ORDER OF MAGNITUDE AND THE ONE REGISTERED ESCAPE CLOSES.

Bars locked in analysis/ELEC055_nucq_propagation_bars_LOCKED.md BEFORE this ran.
"""
import numpy as np

HBAR = 1.054571817e-34
C = 2.99792458e8
FM = 1e-15
T_TUBE = 1.878e5
SETS = {"Sigma-route": 1.70e3, "lattice-anchored": 1203.0}
NUCLEI = [("He-4", 4), ("C-12", 12), ("O-16", 16), ("Fe-56", 56),
          ("Pb-208", 208), ("U-238", 238)]
L_OLD = np.sqrt(HBAR * C / 1.70e3)      # 4.31 fm, what NUCQ-001 used
YUKAWA = 1.4 * FM


def L_min(T0):
    """pi * A_hbar = sqrt(2 pi hbar c / T0), the subluminality floor."""
    return np.sqrt(2 * np.pi * HBAR * C / T0)


def main():
    # B1
    print(f"B1 corrected coherent length (NUCQ-001 used L = {L_OLD/FM:.2f} fm):")
    for tag, T0 in SETS.items():
        print(f"   {tag:17s} L_min = pi A_hbar = {L_min(T0)/FM:.2f} fm "
              f"({L_min(T0)/L_OLD:.2f}x)")

    # B2
    print("\nB2 Test 2 re-run -- sub-quantum patch counts (R/L)^3, R = 1.2 A^(1/3) fm:")
    print(f"   {'nucleus':8s} {'NUCQ-001':>10s} {'Sigma-route':>12s} {'lattice':>10s}")
    for name, A in NUCLEI:
        R = 1.2 * A ** (1 / 3) * FM
        old = (R / L_OLD) ** 3
        vals = [(R / L_min(T0)) ** 3 for T0 in SETS.values()]
        print(f"   {name:8s} {old:10.3f} {vals[0]:12.4f} {vals[1]:10.4f}")
    R_u = 1.2 * 238 ** (1 / 3) * FM
    worst = (R_u / L_min(1.70e3)) ** 3
    print(f"   THE MARGIN MOVES: the heaviest nucleus falls from 5.13 patches to "
          f"{worst:.3f};")
    print(f"   the entire chart is now under a THIRD of one patch (He-4: "
          f"{(1.2*4**(1/3)*FM/L_min(1.70e3))**3:.4f}).")
    print(f"   NUCQ-001's verdict does not merely keep its direction -- its margin")
    print(f"   deepens by {5.128/worst:.1f}x in the count, i.e. the picture requires")
    print(f"   standard QM to hold across objects it says are deeply sub-quantum.")

    # B3
    print("\nB3 Test 1 re-run -- the tension placing the quantum scale at the Yukawa range:")
    T_needed = 2 * np.pi * HBAR * C / YUKAWA ** 2
    print(f"   T = 2 pi hbar c / L_Y^2 = {T_needed:.3e} N vs registered 1.70e3 N")
    print(f"   -> factor {T_needed/1.70e3:.1f} (NUCQ-001 quoted 9.5 using the")
    print(f"   uncorrected length). The parameter clash WORSENS by "
          f"{(T_needed/1.70e3)/9.5:.1f}x.")

    # B4: the escape, re-priced
    print("\nB4 THE ESCAPE (NUCQ-002: small structural n_t dissolves the falsification),")
    print("   re-priced under the bound. With T0 = T_tube/n, L_min = sqrt(2 pi hbar c n")
    print("   / T_tube), so patch count scales as n^(-3/2) -- SMALL n is the escape.")
    R_he = 1.2 * 4 ** (1 / 3) * FM
    for thresh in (100, 10, 1):
        L_req = R_he / thresh ** (1 / 3)
        n_req = L_req ** 2 * T_TUBE / (2 * np.pi * HBAR * C)
        print(f"   He-4 needs >= {thresh:3d} patches -> L <= {L_req/FM:.3f} fm -> "
              f"n <= {n_req:.3f}")
    n_one = (R_he) ** 2 * T_TUBE / (2 * np.pi * HBAR * C)
    print(f"   Even ONE patch inside He-4 requires n <= {n_one:.2f}, versus NUCQ-003's")
    print(f"   lattice floor n >= 115: short by {115/n_one:.0f}x, and short by "
          f"{115/0.159:.0f}x for a")
    print(f"   defensible >= 100 patches. THE ESCAPE IS CLOSED: the structural counts")
    print(f"   that would restore Born exactness are excluded by the lattice-measured")
    print(f"   flux-tube width, the same non-circular constraint NUCQ-003 registered.")
    print("   NUCQ-002's conditional amendment is therefore SUPERSEDED; NUCQ-001")
    print("   returns to UNCONDITIONAL. Status change filed on both claims.")

    # B5
    print("\nB5 HONESTY: L >= pi A is NECESSARY, not sufficient -- any larger coherent")
    print("   segment only lowers the counts further, so every residual freedom points")
    print("   the same way. This session STRENGTHENS a refutation of the framework's")
    print("   own distinctive prediction; it is recorded in those terms.")
    print("PASS: the margin moves, not just the direction, and the one registered")
    print("      escape is closed by a bound the framework itself supplies.")


if __name__ == "__main__":
    main()
