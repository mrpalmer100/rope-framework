"""COMMISSION TET -- the arriving-wavenumber spectrum.

Bars: analysis/TET_arriving_spectrum_bars_LOCKED.md (locked first).
Spectra S1-S4 closed at lock; granted g = [0.395, 0.460] (FND-080);
exact p form (FND-072) everywhere; sealed mesoscopic target regenerated
from the seal procedure at run time.
"""

import math
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from tools.scale001_seal import target

G_BAND = (0.395, 0.460)          # FND-080 grant
P_SEAL = (8.3e-4, 8.6e-3)        # FND-071 sealed band (D4, data-side)
KA_ROBUST = (2.19, 2.38)         # D2
KA_ANY = (1.8, 2.9)              # D3
KAPPA_A = 1.0 / 0.6272           # 1/w_vac in units of 1/a
L1 = 3.0
NMAX = 200000


def p_exact(g, ka):
    return g * g / (2.0 * (g * g + 4.0 * ka * ka))


def s1(g):
    return p_exact(g, math.pi)


def s2(g):
    num = den = 0.0
    for n in range(1, NMAX + 1):
        w = 1.0 / (n * n)
        num += w * p_exact(g, n * math.pi)
        den += w
    return num / den


def s3(g):
    return p_exact(g, 1.0)


def s4(g):
    """Lorentzian rho(k) ~ 1/(k^2 + kappa^2), closed form:
    p_eff = (1/2) q/(q + kappa), q = g/2 (in 1/a units)."""
    q = g / 2.0
    return 0.5 * q / (q + KAPPA_A)


SPECTRA = {"S1 fundamental": s1, "S2 step-kink harmonics": s2,
           "S3 transit": s3, "S4 kink continuum": s4}


def ka_eff(g, p):
    """Exact inversion of p(g, ka)."""
    x = math.sqrt(2.0 * p / (1.0 - 2.0 * p))
    return g / (2.0 * x)


def band_verdict(lo, hi, blo, bhi, label):
    if hi >= blo and lo <= bhi:
        return f"INSIDE/overlaps {label}"
    gap = blo / hi if hi < blo else lo / bhi
    return f"outside {label} x{gap:.2f}" + (" BEYOND L1" if gap > L1 else " (within L1)")


def main():
    t = target()
    print(f"granted g band {G_BAND}; sealed p band {P_SEAL}; "
          f"mesoscopic target (regenerated) {t}\n")
    d4_pass, c4_land = [], []
    for name, f in SPECTRA.items():
        p_lo, p_hi = f(G_BAND[0]), f(G_BAND[1])
        v_d4 = band_verdict(p_lo, p_hi, *P_SEAL, "sealed p band")
        ka_lo = ka_eff(G_BAND[0], p_lo)
        ka_hi = ka_eff(G_BAND[1], p_hi)
        kas = (min(ka_lo, ka_hi), max(ka_lo, ka_hi))
        g2 = (1 / (2 * p_hi), 1 / (2 * p_lo))
        g3 = (1 / (3 * p_hi), 1 / (3 * p_lo))
        print(f"{name}:")
        print(f"  p_eff = [{p_lo:.3e}, {p_hi:.3e}] -> D4: {v_d4}")
        print(f"  effective ka = [{kas[0]:.2f}, {kas[1]:.2f}] -> "
              f"D2 {KA_ROBUST}: {band_verdict(*kas, *KA_ROBUST, 'robust')} ; "
              f"D3 {KA_ANY}: {band_verdict(*kas, *KA_ANY, 'any-landing')}")
        print(f"  g_C4 linear = [{g2[0]:.1f}, {g2[1]:.1f}] -> "
              f"{band_verdict(*g2, *t, 'target')}")
        print(f"  g_C4 volume = [{g3[0]:.1f}, {g3[1]:.1f}] -> "
              f"{band_verdict(*g3, *t, 'target')}\n")
        if "INSIDE" in v_d4:
            d4_pass.append(name)
            if ("INSIDE" in band_verdict(*g2, *t, "t")
                    or "INSIDE" in band_verdict(*g3, *t, "t")):
                c4_land.append(name)

    print(f"D4-PASS spectra: {d4_pass}")
    print(f"C4-landing among D4-PASS: {c4_land}")
    if d4_pass and c4_land:
        v = "CHAIN-CLOSES + C4-LANDS"
    elif d4_pass:
        v = "CHAIN-CLOSES + C4-MISSES"
    else:
        v = "CHAIN-BREAKS (grant exposure fires)"
    print(f"\nVERDICT (pre-committed grammar): {v}")


if __name__ == "__main__":
    main()
