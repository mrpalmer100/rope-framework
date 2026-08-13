"""COMMISSION QOPH -- the encounter spectrum.

Bars: analysis/QOPH_encounter_spectrum_bars_LOCKED.md (locked before this
file was written). Routes closed at lock: R1 (segment fundamental,
ka = pi), R2 (kink localization, ka = a/w = 1/0.6272), R3 (transit
kinematics, ka = 1, incumbent).

Checks, in locked order:
  1. The exact scaling law: g_demanded(p; ka) is linear in ka at fixed p,
     verified against the closed form, not assumed.
  2. The demanded window per route from the sealed p band
     [8.3e-04, 8.6e-03] (FND-071, unchanged, not re-derived here).
  3. Overlap verdicts against the survival floor [0.395, 0.460]
     (FND-073 C3 statement, per-pair ratio identification taken as
     registered there, not re-litigated here).
  4. Verdict under the pre-committed grammar, including the L1
     direction-neutral factor-3 band.
"""

import math

P_BAND = (8.3e-4, 8.6e-3)          # FND-071 sealed band, per crossing encounter
SURVIVAL = (0.395, 0.460)          # EM-RECON-030 band, imported to C3 by FND-073
W_OVER_A = 0.6272                  # FND-068 convention, EM-RECON-030 provenance
L1 = 3.0                           # FND-029 L1 direction-neutral conversion band

ROUTES = {
    "R1_segment_fundamental": math.pi,
    "R2_kink_width": 1.0 / W_OVER_A,
    "R3_transit_incumbent": 1.0,
}


def g_from_p(p, ka):
    """Invert p = x^2/(2(1+x^2)), x = g/(2 ka). Exact, from FND-072's form."""
    if not (0.0 < p < 0.5):
        raise ValueError("p outside (0, 1/2)")
    x = math.sqrt(2.0 * p / (1.0 - 2.0 * p))
    return 2.0 * ka * x


def p_from_g(g, ka):
    return g * g / (2.0 * (g * g + 4.0 * ka * ka))


def check_scaling_law():
    """g at fixed p must scale exactly linearly in ka."""
    for p in (1e-4, 1e-3, 1e-2, 0.1, 0.4):
        g1 = g_from_p(p, 1.0)
        for ka in (0.3, 1.594, math.pi, 7.0):
            g2 = g_from_p(p, ka)
            assert abs(g2 / g1 - ka) < 1e-12, (p, ka)
            # round trip through the closed form
            assert abs(p_from_g(g2, ka) - p) < 1e-12
    return True


def windows():
    out = {}
    for name, ka in ROUTES.items():
        lo = g_from_p(P_BAND[0], ka)
        hi = g_from_p(P_BAND[1], ka)
        out[name] = (ka, lo, hi)
    return out


def overlap_verdict(lo, hi):
    s_lo, s_hi = SURVIVAL
    if hi >= s_lo and lo <= s_hi:
        return "OVERLAP"
    # disjoint: measure the gap factor to the nearer edge
    gap = s_lo / hi if hi < s_lo else lo / s_hi
    return "WITHIN-L1" if gap <= L1 else "DISJOINT-BEYOND-L1"


def main():
    assert check_scaling_law()
    print("scaling law: g_demanded linear in ka at fixed p -- VERIFIED exact")
    print(f"sealed p band: {P_BAND}, survival floor: {SURVIVAL}")
    print()
    results = {}
    for name, (ka, lo, hi) in windows().items():
        v = overlap_verdict(lo, hi)
        results[name] = v
        print(f"{name}: ka = {ka:.4f}, demanded g in [{lo:.4f}, {hi:.4f}] -> {v}")
    print()
    n_overlap = sum(1 for v in results.values() if v == "OVERLAP")
    n_beyond = sum(1 for v in results.values() if v == "DISJOINT-BEYOND-L1")
    if n_overlap >= 2 and n_beyond == 0:
        verdict = "RESOLVED"
    elif n_overlap == 0 and all(v == "DISJOINT-BEYOND-L1" for v in results.values()):
        verdict = "SHARPENED-TENSION"
    else:
        verdict = "UNDERDETERMINED"
    print(f"VERDICT (pre-committed grammar): {verdict}")
    # the convergence point, displayed only if OVERLAP exists anywhere
    if n_overlap:
        for name, (ka, lo, hi) in windows().items():
            olo, ohi = max(lo, SURVIVAL[0]), min(hi, SURVIVAL[1])
            if olo <= ohi:
                print(f"  {name}: joint window g in [{olo:.4f}, {ohi:.4f}], "
                      f"p there in [{p_from_g(olo, ka):.2e}, {p_from_g(ohi, ka):.2e}]")
    return verdict


if __name__ == "__main__":
    main()
