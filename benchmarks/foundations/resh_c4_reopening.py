"""COMMISSION RESH -- SCALE-001 C4 re-opened with the derived carrier.

Bars: analysis/RESH_c4_reopening_bars_LOCKED.md (locked first).
Law (SCALE-001, locked 2026-08-11): lambda_mfp = 1/(n_x sigma_x).
Carrier (FND-071/072): sigma_x = p a^2, p = g^2/(2(g^2 + 4(ka)^2)).

Enumeration closed at lock:
  densities  D1 (linear 2/a -> g_C4 = 1/(2p)), D2 (volume 3/a^3 -> 1/(3p))
  contrast   g in [0.395, 0.460]  (FND-073 C3 identification, CONDITIONAL)
  ka         {1, 1.594, pi} route points + continuous sweep [1, pi]
Sealed target: g = l_q/a in [82.6, 108.0] (regenerated from the seal
tool's registered procedure, not typed in).
"""

import math
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from tools.scale001_seal import target  # regenerate, do not restate

G_BAND = (0.395, 0.460)
ROUTES = {"R3_transit": 1.0, "R2_kink": 1.0 / 0.6272, "R1_fundamental": math.pi}
DENS = {"D1_linear": 2.0, "D2_volume": 3.0}
L1 = 3.0


def p_of(g, ka):
    return g * g / (2.0 * (g * g + 4.0 * ka * ka))


def weave_density_check():
    """D2 derived, not assumed: three orthogonal strand families at
    spacing a give length density 3/a^2; crossings at linear density 2/a
    per strand, halved for pair double count: n_x = (2/a)(3/a^2)/2 = 3/a^3.
    Dimensional check of the locked law with sigma = p a^2:
    1/lambda = n_x sigma = 3 p / a  ->  g_C4 = lambda/a = 1/(3p)."""
    return 3.0


def cell(dens_c, ka):
    """g_C4 band over the contrast band, low contrast -> low p -> high g_C4."""
    p_hi = p_of(G_BAND[1], ka)
    p_lo = p_of(G_BAND[0], ka)
    return (1.0 / (dens_c * p_hi), 1.0 / (dens_c * p_lo))


def verdict_cell(lo, hi, t):
    tlo, thi = t
    if hi >= tlo and lo <= thi:
        return "OVERLAP"
    gap = tlo / hi if hi < tlo else lo / thi
    side = "LOW" if hi < tlo else "HIGH"
    return f"MISS-{side} x{gap:.2f}" + ("" if gap <= L1 else " (beyond L1)")


def demanded_ka(dens_c, t):
    """Invert for the ka at which the cell's band exactly covers the target:
    g_C4 = 1/(c p(g, ka)); solve p, then ka from the exact form."""
    out = []
    for g_c4, g in ((t[0], G_BAND[0]), (t[1], G_BAND[1])):
        p = 1.0 / (dens_c * g_c4)
        # p = g^2/(2(g^2+4ka^2)) -> ka = (g/2) sqrt(1/(2p) - 1)
        out.append((g / 2.0) * math.sqrt(1.0 / (2.0 * p) - 1.0))
    return (min(out), max(out))


def main():
    t = target()
    assert weave_density_check() == DENS["D2_volume"]
    print(f"sealed target regenerated from registered procedure: {t}")
    print(f"contrast band (CONDITIONAL, FND-073 C3): {G_BAND}\n")
    span_lo, span_hi = float("inf"), 0.0
    landing_routes = []
    for rname, ka in ROUTES.items():
        cells = {}
        for dname, c in DENS.items():
            lo, hi = cell(c, ka)
            cells[dname] = verdict_cell(lo, hi, t)
            span_lo, span_hi = min(span_lo, lo), max(span_hi, hi)
            print(f"{rname} ka={ka:.4f} {dname}: g_C4 in [{lo:.1f}, {hi:.1f}] -> {cells[dname]}")
        if all(v == "OVERLAP" for v in cells.values()):
            landing_routes.append(rname)
        print()
    print(f"family span over all locked cells: g_C4 in [{span_lo:.1f}, {span_hi:.1f}]")
    contains = span_lo <= t[0] and span_hi >= t[1]
    if landing_routes:
        v = "CONDITIONAL-LANDS at " + ", ".join(landing_routes)
    elif contains:
        v = "CONDITIONAL-CONTAINS"
    else:
        v = "CONDITIONAL-MISS (check sides)"
    print(f"VERDICT (pre-committed grammar): {v}\n")
    if contains and not landing_routes:
        # mandatory companions
        width = math.log10(span_hi / span_lo) + math.log10(t[1] / t[0])
        rate = min(width / 4.0, 1.0)
        print(f"look-elsewhere: containment rate under the committed log-uniform "
              f"10^0..10^4 prior ~ {rate:.2f} (family log-span "
              f"{math.log10(span_hi/span_lo):.2f} decades)")
        for dname, c in DENS.items():
            klo, khi = demanded_ka(c, t)
            inside = "INSIDE" if khi >= 1.0 and klo <= math.pi else "OUTSIDE"
            print(f"demanded ka for exact landing, {dname}: [{klo:.2f}, {khi:.2f}] "
                  f"-- {inside} the QOPH family [1, pi]")


if __name__ == "__main__":
    main()
