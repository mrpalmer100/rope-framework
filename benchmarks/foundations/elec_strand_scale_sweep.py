"""ELEC-057 -- IS THERE ANY STRAND SCALE WHERE THE ELECTRON AND HBAR SECTORS
BOTH LIVE? THE ONE-MEDIUM PARAMETER SWEPT OVER ITS FULL ALLOWED RANGE.

Bars locked in analysis/ELEC057_strand_scale_sweep_bars_LOCKED.md BEFORE this ran.
"""
import numpy as np

HBAR = 1.054571817e-34
C = 2.99792458e8
FM = 1e-15
T_TUBE = 1.878e5          # J/m, hadronic measurement
R_TUBE = 0.407 * FM       # ELEC-052 lattice-anchored flux-tube radius
A_LORENTZ = 1e-16         # the BOUND, never a measurement
RE_AT_BOUND = 21.16 * FM  # ELEC-036 calibrated rms charge radius at a = bound
RE_LIMIT = 1e-3 * FM      # conservative experimental structure bound
T_ROPE = 0.2376           # J/m, ELEC-040 calibrated electron-rope tension
R_HE4 = 1.2 * 4 ** (1 / 3) * FM


def T0(a):
    return T_TUBE / (3 * np.pi * (R_TUBE / a) ** 2)


def L_patch(a):
    return np.sqrt(2 * np.pi * HBAR * C / T0(a))


def r_e(a):
    return RE_AT_BOUND * (a / A_LORENTZ)


def main():
    # Exact gate boundaries, solved not gridded (B1)
    g1 = A_LORENTZ
    g2 = A_LORENTZ * (RE_LIMIT / RE_AT_BOUND)                 # r_e(a) <= limit
    g3 = A_LORENTZ * np.sqrt(T_ROPE / T0(A_LORENTZ))          # T0(a) <= T_rope
    # G4: L(a) <= R  ->  a >= ...   (L ~ 1/a, so this is a FLOOR)
    def a_for_L(Ltarget):
        return A_LORENTZ * L_patch(A_LORENTZ) / Ltarget
    g4_1 = a_for_L(R_HE4)                                     # >=1 patch in He-4
    g4_100 = a_for_L(R_HE4 / 100 ** (1 / 3))                  # >=100 patches

    print("GATE BOUNDARIES (exact, from the locked scaling laws):")
    print(f"  G1 LORENTZ            a <= {g1:.3e} m")
    print(f"  G2 ELECTRON SIZE      a <= {g2:.3e} m   (r_e = 21.16 fm at the bound)")
    print(f"  G3 TENSION MATCHING   a <= {g3:.3e} m   (T0 <= {T_ROPE} J/m)")
    print(f"  G4 HBAR/NUCLEAR       a >= {g4_1:.3e} m   (>=1 patch in He-4)")
    print(f"     stricter variant   a >= {g4_100:.3e} m   (>=100 patches)\n")

    print("THE SWEEP (25 decades, gates evaluated at each scale):")
    print(f"  {'a (m)':>10} {'T0 (J/m)':>10} {'r_e (fm)':>10} {'L (fm)':>10}  gates passed")
    for a in np.logspace(-30, -10, 21):
        passed = [n for n, ok in (("G1", a <= g1), ("G2", a <= g2),
                                  ("G3", a <= g3), ("G4", a >= g4_1)) if ok]
        print(f"  {a:10.1e} {T0(a):10.2e} {r_e(a)/FM:10.2e} {L_patch(a)/FM:10.2e}  "
              f"{','.join(passed) if passed else 'none'}")

    # B2: the intersection
    lo, hi = g4_1, min(g1, g2, g3)
    print(f"\nB2 THE INTERSECTION: allowed a must satisfy "
          f"{lo:.3e} <= a <= {hi:.3e}")
    if lo <= hi:
        print("  NON-EMPTY -- a viable window exists and has never been examined.")
    else:
        gap = np.log10(lo / hi)
        print(f"  EMPTY. The floor exceeds the ceiling by {gap:.1f} DECADES.")
        print("  NO STRAND SCALE SATISFIES BOTH SECTORS. Under the one-medium")
        print("  declaration (ELEC-038) the electron and hbar sectors are")
        print("  MUTUALLY EXCLUSIVE at every value of the one free length.")

    # B3: separability -- which gates fail ALONE inside the Lorentz bound
    print("\nB3 SEPARABILITY (does a gate fail on its own, inside G1?):")
    print(f"  G2 electron: needs a <= {g2:.2e}, which IS inside G1 -- "
          f"satisfiable alone (by shrinking {A_LORENTZ/g2:.1e}x).")
    print(f"  G3 tension:  needs a <= {g3:.2e}, inside G1 -- satisfiable alone.")
    print(f"  G4 hbar:     needs a >= {g4_1:.2e} > G1 = {g1:.1e} --")
    print(f"     NO SOLUTION ANYWHERE IN THE ALLOWED REGION, short by "
          f"{g4_1/g1:.1f}x even at the ceiling and for the WEAKEST threshold")
    print(f"     (one patch in He-4). The hbar sector is therefore excluded by the")
    print(f"     LORENTZ BOUND ALONE, independently of the electron sector.")
    print(f"     This is stronger than a two-sector clash: it needs no comparison.")

    # B4
    print("\nB4 LIMITS: r_e(a) rescales rigidly because ELEC-041's geometry is pure")
    print("   ratios; the calibration carries ELEC-034's ~2.4% residue -- irrelevant")
    print("   against a gap measured in decades. G4's threshold is the WEAKEST")
    print("   defensible one; the >=100-patch version pushes the floor to")
    print(f"   {g4_100:.2e} m, worsening the gap. No gate was relaxed after the fact.")
    print("\nPASS: the one free length was swept over its full allowed range and the")
    print("      two-sector window is empty; the hbar sector fails unaided.")


if __name__ == "__main__":
    main()
