"""ELEC-054 -- STANDING-WAVE SCALE SELECTION: FIVE CANDIDATES, THE HONEST
ACCOUNTING, AND A RELATIVISTIC BOUND NOBODY HAD CHECKED.

Bars locked in analysis/ELEC054_scale_selection_bars_LOCKED.md BEFORE this ran.
"""
import numpy as np

HBAR = 1.054571817e-34
C = 2.99792458e8
A_LORENTZ = 1e-16
W = A_LORENTZ / np.sqrt(3)          # ELEC-053 invariance theorem
FM = 1e-15
SETS = {"Sigma-route": 1.70e3, "lattice-anchored": 1203.0}
D_C = 3.2e-3 * W                     # registered thickness ratio


def amp(T0):
    return np.sqrt(2 * HBAR * C / (np.pi * T0))


def main():
    print("THE TARGET (what any mechanism must produce, from medium properties alone):")
    for tag, T0 in SETS.items():
        A = amp(T0)
        print(f"   {tag:17s} T0={T0:6.0f} J/m -> A_hbar = {A/FM:.3f} fm = {A/W:.2f} w")
    r = amp(1203.0) / amp(1.70e3)
    print(f"   NOT INVARIANT ({r-1:+.0%} between sets): a mechanism giving a PURE NUMBER")
    print(f"   would SELECT the scale set -- deciding Sigma from theory rather than")
    print(f"   waiting on polarimetry. That is this problem's payoff structure.\n")

    # M1: relativistic ceiling
    print("M1 RELATIVISTIC CEILING: v_max = A omega, omega = pi c/L, demand v_max <= c")
    print("   -> A <= L/pi. This contains no scale for A (L is free, it cancelled in S),")
    print("   so it DOES NOT SELECT. But inverted it BINDS THE PATCH:")
    for tag, T0 in SETS.items():
        A = amp(T0)
        L_min = np.pi * A
        L_hbar = np.sqrt(HBAR * C / T0)
        print(f"   {tag:17s} L >= pi A = {L_min/FM:.2f} fm, i.e. {L_min/L_hbar:.2f}x the "
              f"quoted L_hbar = {L_hbar/FM:.2f} fm ({L_min/W:.0f} spacings)")
    print("   FINDING (byproduct, B3): the coherent segment carrying one hbar cannot be")
    print("   the 4.3 fm patch HBAR-005 quotes -- at that length the fundamental mode's")
    print("   transverse speed would be 2.51c. The patch is >= 10.8 fm (Sigma-route) or")
    print("   >= 12.9 fm (lattice). Annotations owed on HBAR-005 and NUCQ-001.\n")

    # M2 / M4: the medium's own lengths
    print("M2 AMPLITUDE = SPACING and M4 ANHARMONIC TURNING POINT (~w, the scale at which")
    print("   U = C/w^2 departs harmonic): both give A ~ w, hence")
    for tag, T0 in SETS.items():
        print(f"   {tag:17s} S(A=w)/hbar = {np.pi*T0*W**2/(2*C)/HBAR:.2e} "
              f"-- short by {amp(T0)/W:.0f}x in amplitude, {(amp(T0)/W)**2:.0f}x in action")
    print(f"   Also checked, the only other registered length: thickness d_c = {D_C:.2e} m")
    print(f"   gives S/hbar = {np.pi*1.70e3*D_C**2/(2*C)/HBAR:.1e}. ALL FAIL. The medium's")
    print("   intrinsic lengths are the WRONG SIZE by ~60x; the selected amplitude is")
    print("   mesoscopic, which is the same wall HBAR-005's dimensional audit hit.\n")

    # M3: thermal
    print("M3 THERMAL/EQUIPARTITION: selecting A needs an energy scale; the corpus")
    print("   registers no vacuum temperature, and importing one imports the answer.")
    print("   NOT A SELECTION (external input), consistent with HBAR-002's verdict that")
    print("   the coherence mechanism supplies capability, not occupation.\n")

    # M5: integer collective count
    print("M5 COLLECTIVE COUNT hbar = n S_1, S_1 = pi T w^2/(2c):")
    for tag, T0 in SETS.items():
        S1 = np.pi * T0 * W ** 2 / (2 * C)
        n = HBAR / S1
        dev = abs(n - round(n)) / n
        print(f"   {tag:17s} n = {n:.1f}, nearest integer {round(n)}, deviation {dev:.1e}")
    print("   RESTATEMENT, not selection (B1): n = (A/w)^2 identically, so this is the")
    print("   target rewritten, and it takes hbar as input.")
    print("   THE INTEGRALITY TEST IS PRECISION-BLOCKED: deciding whether n is an exact")
    print("   integer needs T0 to ~1e-4 relative; the corpus has it to 7% (and the two")
    print("   scale sets differ by 19%). Registered as untestable-at-present with the")
    print("   precision requirement named -- NOT as a success.\n")

    print("VERDICT: SCALE SELECTION REMAINS OPEN. Five candidates, no selection.")
    print("SHARPENED TARGET for any future mechanism, per B4:")
    print("   (i) produce A/w = 59.6 (or 70.8) from T0, w, c and structure alone;")
    print("   (ii) take no hbar as input;")
    print("   (iii) be compatible with L >= pi A (M1's bound);")
    print("   (iv) if it yields a pure number, it thereby SELECTS the scale set --")
    print("        the single highest-value outcome available to this sector.")
    print("PASS: the negative is registered, the target is sharpened, and one new")
    print("      derived bound (M1) falls out of the failure.")


if __name__ == "__main__":
    main()
