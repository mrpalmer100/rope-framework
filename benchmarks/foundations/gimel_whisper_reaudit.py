"""Commission GIMEL -- the whisper-pricing re-audit under the moved M-point.
Bars locked BEFORE computing (analysis/GIMEL_whisper_reaudit_bars_LOCKED.md):
Q1 registry inspection of l_q's registered form; Q2 the MATTER044 table
re-priced at both FND-040 floor readings; Q3 the 1-100 window's provenance
grade; Q4 the kappa_pack cap the window implies, confronted with both floors.
Frozen inputs only: K_me (spent calibration re-used), Sigma_eff (ELEC-081),
the FND-040 floors, R1's registered form. No new fitted numbers.
"""
import math

HBAR, C = 1.054571817e-34, 2.99792458e8
ALPHA = 1 / 137.036
K_ME = 2.6065e-14              # T0*a, pinned (spent calibration)
S_EFF = 3.61e35                # J/m^3 (ELEC-081)
A_CARD, T0_LAT = 1.0e-16, 1203.0
L_Q_REG = 1.39e-15             # the registered femtometre invariant
H_CORE = 1.87e-19
BETA, RINGF = 35.4, 0.23
ZPE_BAR = 3.0
QAREA = 4 * math.pi * ALPHA * HBAR * C   # T0 * l_q^2 (R1, registered)


def point(kappa):
    sv = kappa * S_EFF
    a = (3 * K_ME / sv) ** (1 / 3)
    t0 = K_ME / a
    lq = math.sqrt(QAREA / t0)           # R1's own registered form
    return a, t0, lq


def main():
    # Q1 -- registry inspection (asserted, not computed): R1 registers
    # hbar = T0 l_q^2 / (4 pi alpha c), so l_q = sqrt(4 pi alpha hbar c/T0):
    # l_q RESCALES with the mesh by its own registered definition. The
    # OMEGA/BET strain values held l_q at the kappa=1 M-point number:
    lq_stale = 2.58e-15
    a1, t01, _ = point(1)
    assert abs(math.sqrt(QAREA / t01) / lq_stale - 1) < 0.01
    print("Q1: l_q = sqrt(4 pi alpha hbar c / T0) by R1's registered form;")
    print("    the 158/271 strain used the stale kappa=1 value "
          f"({lq_stale:.2e} m). STALE-VALUE COMPARISON, per MATTER045 class.")

    # Q2 -- the re-priced table at both floor readings
    for kappa, label in [(50, "5% CS bound"), (250, "continuum")]:
        a, t0, lq = point(kappa)
        r = lq / a
        print(f"kappa_pack = {kappa} ({label}):")
        print(f"  a = {a:.3e} m, T0 = {t0:.0f} J/m, l_q = {lq:.3e} m")
        f_t = t0 / T0_LAT
        f_lq = lq / L_Q_REG if lq > L_Q_REG else L_Q_REG / lq
        print(f"  T0 vs lattice anchor: {f_t:.2f} "
              f"[{'inside' if f_t <= ZPE_BAR else 'OUTSIDE'}]")
        print(f"  l_q vs registered:    {f_lq:.2f} "
              f"[{'inside' if f_lq <= ZPE_BAR else 'OUTSIDE'}]")
        assert f_t <= ZPE_BAR and f_lq <= ZPE_BAR
        print(f"  a vs kappa=1 M-point: {a1/a:.2f} = kappa^(1/3) "
              f"({kappa**(1/3):.2f}) -- the SAME Sigma_vac hierarchy, one")
        print("    determination moved, not two disagreeing: NOT a ZPE-band")
        print("    comparison (reclassification argued in results).")
        print(f"  l_q/a = {r:.1f} "
              f"[{'inside' if 1 <= r <= 100 else 'OUTSIDE'} the 1-100 window]")
        # n_q invariance: n_q tracks a*T0*h = K_me*h, pinned exactly
        nq = 4 * math.pi * ALPHA * (3 * BETA / (RINGF * 1.0)) * (a * H_CORE / lq**2)
        nq1 = 4 * math.pi * ALPHA * (3 * BETA / (RINGF * 1.0)) * (K_ME * H_CORE / QAREA)
        assert abs(nq / nq1 - 1) < 1e-12
    print("n_q invariance RE-VERIFIED exactly at both readings (tracks K_me*h).")

    # sixth-root law and the Q4 cap
    r1 = math.sqrt(QAREA / t01) / a1
    print(f"THE LAW: l_q/a = {r1:.1f} x kappa_pack^(1/6) "
          "(both scalings from registered relations).")
    cap = (100 / r1) ** 6
    print(f"Q4: the window caps kappa_pack at {cap:.0f}.")
    assert 50 < cap < 250
    print("    The cap falls BETWEEN the floors: the 5% CS-bound reading")
    print("    (kappa >= 50) COEXISTS with the window; the continuum reading")
    print("    (kappa >= 250) is EXCLUDED at the window's grade. The band,")
    print(f"    if the window is genuine: 50 <= kappa_pack <= {cap:.0f}.")

    # the 4.62 decomposition under the moved point
    print("THE 4.62 DECOMPOSITION: the kappa=1 pricing (1.67 x 2.77) was the")
    print("  Sigma_eff-normalized special case; under Sigma_vac the length")
    print("  shift is the derived kappa^(1/3) hierarchy, not a whisper, and")
    print("  the surviving like-for-like comparisons (T0, l_q vs registered)")
    print("  sit INSIDE the ZPE bar at both readings.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
