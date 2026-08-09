"""ZPE BAR RE-AUDIT: the MATTER041 inverted pipeline re-run under both
branches of the dissolved 25% share. Bars locked in
analysis/ZPE_reaudit_bars_LOCKED.md BEFORE this file was written.
Constants and code path IDENTICAL to matter041_two_scale_fork.py; only
the T0 band varies per branch. Nothing adopted.
"""
import numpy as np

HBAR, C, G = 1.054571817e-34, 2.99792458e8, 6.67430e-11
ALPHA, ME = 1 / 137.036, 9.1093837015e-31
L_RING, A_MESH = 3.141, 1.0e-16
T0_ANCHORS = {"R1 quantum-area": 119.3, "lattice": 1203.0,
              "Sigma-route": 1700.0, "GRV-074 rigidity": 5847.0}
BETA, RINGF, H_CORE = 35.4, 0.23, 1.87e-19
NQ_BAND = (1.1e-4, 4.6e-4)
L_Q_REGISTERED = 1.39e-15
WINDOW = (1.0, 100.0)

BRANCHES = {
    # name: (share band s in [s_lo, s_hi], provenance note)
    "OLD (25% reading, for reference)": (0.0, 2.0 / 3.0),
    "A (lambda open)": (0.0, 0.999),
    "B (pi(r/a)^2 prediction, 057 levers)": (0.064, 0.093),
}


def pipeline(s_lo, s_hi):
    """T0 = (1-s) m_e c^2/(L a); l_q = sqrt(4 pi alpha hbar c / T0)."""
    t0_max = (1 - s_lo) * ME * C**2 / (L_RING * A_MESH)
    t0_min = (1 - s_hi) * ME * C**2 / (L_RING * A_MESH)
    lq = lambda t0: np.sqrt(4 * np.pi * ALPHA * HBAR * C / t0)
    lq_lo, lq_hi = lq(t0_max), lq(t0_min)          # l_q ~ T0^-1/2
    return (t0_min, t0_max), (lq_lo, lq_hi)


print("=" * 72)
print("ZPE BAR RE-AUDIT -- MATTER041 pipeline under three T0 bands")
print("=" * 72)
verdicts = {}
for name, (s_lo, s_hi) in BRANCHES.items():
    (t0_min, t0_max), (lq_lo, lq_hi) = pipeline(s_lo, s_hi)
    r_lo, r_hi = lq_lo / A_MESH, lq_hi / A_MESH
    width = lq_hi / lq_lo
    print(f"\n--- BRANCH {name} ---")
    print(f"share s in [{s_lo:.3f}, {s_hi:.3f}] -> T0 in "
          f"[{t0_min:.1f}, {t0_max:.1f}] J/m; l_q band width x{width:.3f}")
    print(f"C1  l_q/a band: [{r_lo:.1f}, {r_hi:.1f}] vs window {WINDOW}")
    c1 = "INSIDE" if r_hi <= WINDOW[1] else (
        "EXITS ABOVE" if r_lo <= WINDOW[1] else "OUTSIDE")
    # share at which the band exits the window:
    s_exit = 1 - (r_lo / WINDOW[1]) ** 2
    print(f"    verdict: {c1}; window exit at share s > {s_exit:.3f}")
    # C2/C3: coherence tags. Old tag rule: excused if factor <= sqrt-carried
    # band... MATTER041 used 'inside ZPE bar' at factor <= 3 on T0-space
    # factors. Re-evaluate: excusable slack = t0_max/t0_min on T0, and
    # sqrt of that on l_q.
    slack_t0 = t0_max / t0_min
    slack_lq = np.sqrt(slack_t0)
    print(f"C2  T0 anchors (excusable T0 slack x{slack_t0:.2f}):")
    for k, v in T0_ANCHORS.items():
        f = max(t0_max, v) / min(t0_max, v)  # vs calibration top, as 041 did
        tag = "excused by band" if f <= slack_t0 else "NAKED TENSION"
        print(f"      vs {k} ({v:.0f}): factor {f:.1f}  [{tag}]")
    f_lq = L_Q_REGISTERED and (max(lq_lo, L_Q_REGISTERED)
                               / min(lq_lo, L_Q_REGISTERED))
    tag = "excused by band" if f_lq <= slack_lq else "NAKED TENSION"
    print(f"C3  l_q vs registered 1.39e-15: factor {f_lq:.2f} vs slack "
          f"x{slack_lq:.2f}  [{tag}]")
    # C4: n_q, computed at both l_q edges, chi in (3,1) as registered
    nq = lambda l, chi: 4 * np.pi * ALPHA * (3 * BETA / (RINGF * chi)) \
        * (A_MESH * H_CORE / l**2)
    nq_max = nq(lq_lo, 1.0)   # smallest l_q, chi=1 -> largest n_q
    nq_min = nq(lq_hi, 3.0)
    print(f"C4  n_q range [{nq_min:.2e}, {nq_max:.2e}] vs snap band "
          f"[{NQ_BAND[0]:.1e}, {NQ_BAND[1]:.1e}]")
    c4 = ("OVERLAPS" if nq_max >= NQ_BAND[0] and nq_min <= NQ_BAND[1]
          else "BELOW" if nq_max < NQ_BAND[0] else "ABOVE")
    print(f"    verdict: {c4} (miss at nearest edge: "
          f"{NQ_BAND[0]/nq_max:.2f}x)" if c4 == "BELOW" else
          f"    verdict: {c4}")
    # DIRECTIONAL CHECK of MATTER041's recovery sentence:
    # n_q ~ 1/l_q^2 and ZPE can only LOWER T0 -> RAISE l_q -> LOWER n_q.
    verdicts[name] = (c1, c4, width)

print()
print("=" * 72)
print("C4 DIRECTIONAL CHECK (MATTER041's 'recoverable within the same ZPE")
print("band' sentence): the ZPE bar moves T0 DOWNWARD only (share >= 0),")
print("so l_q moves UP only and n_q = k/l_q^2 moves DOWN only -- AWAY from")
print("the snap band it sits below. The registered recovery sentence is")
print("DIRECTIONALLY WRONG under the bar's own mechanics. CATCH, logged.")
print("=" * 72)

# C6: nuclear import sensitivity
print("\nC6  FND-029 nuclear import: T0 a enters E_x/(T0 a).")
for name, (s_lo, s_hi) in BRANCHES.items():
    t0a_lo = (1 - s_hi) * ME * C**2 / L_RING / 1.602176634e-13
    t0a_hi = (1 - s_lo) * ME * C**2 / L_RING / 1.602176634e-13
    print(f"    {name}: T0 a in [{t0a_lo:.4f}, {t0a_hi:.4f}] MeV "
          f"(x{t0a_hi/t0a_lo:.2f} width vs FND-029's straddling band "
          f"[0.019, 87] in the ratio -- verdict UNCHANGED at any width)")
