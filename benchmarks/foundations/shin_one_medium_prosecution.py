"""COMMISSION SHIN -- the one-medium prosecution.

Bars: analysis/SHIN_one_medium_bars_LOCKED.md (locked first).
Instrument: FND-040's DERIVED leading coefficient
    |delta_D - delta_f| = (eps_f/2)(C_D/C_f - 1),  eps_f = 1/kappa_pack
against the registered Casimir-scaling bound (<= 5 percent at ratio 6;
adjoint 2.25(2)). Components:
    OM-D: kappa_pack = 1 (ELEC-050 B1's density identity).
    OM-S: kappa_pack from FND-073's inverted a band via FND-038's
          M-point solve, kappa = 3 K_ME / (a^3 Sigma_eff).
Constants exactly as registered in tools/scale001_seal.py.
"""

import math
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from tools.scale001_seal import K_ME, S_EFF  # spent calibration; ELEC-081

A_BAND_OMS = (6.30e-17, 8.41e-17)   # FND-073 headline band, metres
BOUND = 0.05                        # registered CS bound at ratio 6
RATIO6 = 6.0                        # Casimir ratio of the bounding rep
ADJ = 9.0 / 4.0                     # adjoint ratio
ADJ_MEAS_PREC = 0.02 / 2.25         # 2.25(2) -> ~0.9 percent
L1 = 3.0
FLOORS = (50.0, 250.0)              # FND-037/040 registered floors


def e3_verification():
    """eps_f = 1/kappa_pack must reproduce the registered inversion:
    bound 5 percent at ratio 6 with coefficient eps/2 -> eps <= 0.02
    -> kappa >= 50 (FND-040's registered arithmetic)."""
    eps_max = BOUND / ((RATIO6 - 1.0) / 2.0)
    kappa_floor = 1.0 / eps_max
    assert abs(eps_max - 0.02) < 1e-12 and abs(kappa_floor - 50.0) < 1e-9
    return True


def kappa_from_a(a):
    return 3.0 * K_ME / (a ** 3 * S_EFF)


def violation(kappa, ratio):
    return (1.0 / kappa) / 2.0 * (ratio - 1.0)


def confront(name, kappas):
    klo, khi = min(kappas), max(kappas)
    v6 = (violation(khi, RATIO6), violation(klo, RATIO6))
    excl = (v6[0] / BOUND, v6[1] / BOUND)
    vadj = (violation(khi, ADJ), violation(klo, ADJ))
    print(f"{name}: kappa_pack in [{klo:.3f}, {khi:.3f}]")
    print(f"  predicted violation at ratio 6: {v6[0]*100:.0f}-{v6[1]*100:.0f} percent "
          f"vs bound 5 percent -> EXCLUSION x{excl[0]:.0f}-x{excl[1]:.0f}")
    print(f"  predicted adjoint violation: {vadj[0]*100:.0f}-{vadj[1]*100:.0f} percent "
          f"vs measured precision ~{ADJ_MEAS_PREC*100:.1f} percent")
    verdict = "EXCLUDED beyond L1" if excl[0] > L1 else (
        "EXCLUDED within L1" if excl[0] > 1.0 else "NOT EXCLUDED")
    print(f"  -> {verdict}\n")
    return excl[0] > L1


def main():
    assert e3_verification()
    print("E3 verified: eps_f = 1/kappa_pack reproduces the registered "
          "5 percent -> kappa >= 50 inversion exactly.\n")

    d_falls = confront("OM-D (kappa_pack = 1)", (1.0, 1.0))
    ks = tuple(kappa_from_a(a) for a in A_BAND_OMS)
    s_falls = confront("OM-S (+ lattice band + spent calibration)", ks)

    # cross-checks against registered statements
    a_floor = tuple((3 * K_ME / (k * S_EFF)) ** (1 / 3) for k in FLOORS)
    excl_fac = tuple(min(A_BAND_OMS) / a for a in a_floor)
    print(f"cross-check vs FND-073's registered conflict: OM-S band excludes "
          f"floor a readings by x{excl_fac[0]:.1f} / x{excl_fac[1]:.1f} "
          f"(FND-073 face: 3.9 / 6.5)")
    m_point = (3 * K_ME / (1.0 * S_EFF)) ** (1 / 3)
    print(f"D3 coherence check: M-point a (kappa=1) = {m_point*1e17:.3f}e-17 m, "
          f"OM-S low edge {A_BAND_OMS[0]*1e17:.2f}e-17 m "
          f"({(A_BAND_OMS[0]/m_point-1)*100:+.1f} percent)\n")

    if d_falls and s_falls:
        print("VERDICT (pre-committed grammar): CONVICTED-WHOLE")
    elif d_falls != s_falls:
        print("VERDICT (pre-committed grammar): CONVICTED-SPLIT")
    else:
        print("VERDICT (pre-committed grammar): ACQUITTED")


if __name__ == "__main__":
    main()
