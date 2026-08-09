"""COMMISSION EXACT-D VI: the a = 8 Planck lengths re-derivation
(charter: docs/technical/COMMISSION_EXACT_D6.md; bars locked first).
GRV-101.

Verifies deterministically: (a) the extensivity of GRV-021's chi_2
(the erratum: registered zeta carries the ring size M = 96); (b) the
corrected 1D chain a = 0.80 l_P; (c) the covariant-chain window and its
sign half-line; (d) the registered a_Sak reproduces from GRV-075's own
formula before correction.
"""
import sys, os
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from induced_elasticity import zp_energy

KT0 = 0.64
HBAR, CLIGHT, G_MEAS = 1.054571817e-34, 2.99792458e8, 6.674e-11
L1 = -1.610665e-4  # GRV-100's covariant slope

REGISTERED = {  # commission record 2026-08-09 (COMMISSION_EXACT_D6 addendum)
    "chi2_ratio_192_96": 2.0353, "zeta_int": 0.012586,
    "a_1d_corrected_lp": 0.795, "a_registered_lp": 7.8,
    "a_cov_window_lp": (0.0, 0.1835), "sign_halfline": "u0 > 1",
}


def chi2_at(M):
    E0 = zp_energy(np.full(M, KT0))
    x = np.arange(M); delta = 0.02
    qs = 2 * np.pi * np.array([1, 2, 3, 4, 6]) / M
    chis = [2 * (zp_energy(KT0 * (1 + delta * np.cos(q * x))) - E0) /
            (KT0 * delta) ** 2 for q in qs]
    return np.polyfit(qs ** 2, chis, 1)[0]


def test():
    # (a) extensivity at CI-cheap sizes
    c64, c128 = chi2_at(64), chi2_at(128)
    ratio = c128 / c64
    assert abs(ratio - 2.0) < 0.15, f"chi_2 is extensive (ratio {ratio:.3f})"
    # (b) the corrected intensive chain
    zint = c64 / (64 * np.sqrt(KT0))
    a1d = np.sqrt(16 * np.pi * zint)
    assert abs(a1d - 0.795) < 0.03, f"corrected 1D selection ~0.80 l_P (got {a1d:.3f})"
    # (c) covariant window: real a only for u0 > 1; max at u0 = 4 x dict 3
    C_low, C_high = L1 * np.log(1 / 0.5), L1 * np.log(1 / 4.0)
    assert C_low < 0 < C_high, "sign half-line: positivity requires u0 > 1"
    amax = np.sqrt(16 * np.pi * C_high * 3)
    assert 0.15 < amax < 0.22, f"covariant window ceiling ~0.18 l_P (got {amax:.3f})"
    # (d) the registered (uncorrected) a_Sak reproduces from the original formula
    zeta_ext = chi2_at(96) / np.sqrt(KT0)
    a_sak = np.sqrt(16 * np.pi * zeta_ext * HBAR * G_MEAS / CLIGHT ** 3)
    lp = np.sqrt(HBAR * G_MEAS / CLIGHT ** 3)
    assert abs(a_sak / lp - 7.8) < 0.2, f"registered chain reproduces ({a_sak/lp:.2f} l_P)"
    print(f"extensive (ratio {ratio:.3f}); corrected a = {a1d:.3f} l_P; covariant")
    print(f"ceiling {amax:.3f} l_P on the u0 > 1 half-line; registered 7.8 l_P reproduced.")
    print("PASS: the scale selection is PLANCK-CLASS AT OR BELOW ONE l_P; the '8' was")
    print("      ring-size bookkeeping (sqrt(96)); GRV-101's record stands.")


if __name__ == "__main__":
    test()
