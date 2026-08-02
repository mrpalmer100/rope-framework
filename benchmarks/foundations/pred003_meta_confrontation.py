"""PRED-003 WIDENED: EVERY INDEPENDENT DETERMINATION, COMBINED AND TESTED.

Bars locked in analysis/PRED003_META_bars_LOCKED.md BEFORE any combination.
"""
import numpy as np

# (value, sigma, label, in_combination)
ALPHA = [
    (1.0e-18, 1.1e-18, "Yb+ E3/E2 PTB 2023", True),
    (1.8e-19, 2.5e-19, "PTB 2023 supplemental fit", False),   # same data as A1
    (-1.7e-17, 2.5e-17, "Al+/Hg+ (revised)", True),
    (-5.8e-17, 6.9e-17, "Dy (Leefer et al.)", True),
    (7.2e-17, 4.7e-17, "Yb+/Cs (Godun 2014)", True),
    (-0.7e-17, 2.1e-17, "Godun 2014 combination", False),      # overlaps above
]
GDOT = [
    (7.1e-14, 7.6e-14, "LLR Hofmann & Muller 2018", True),
    (4e-13, 9e-13, "LLR Williams et al. 2004", False),         # same lineage
    (-0.6e-12, 0.55e-12, "PSR J1713 Zhu 2015", False),         # same pulsar
    (-0.1e-12, 0.45e-12, "PSR J1713 Zhu 2019", False),         # same pulsar
    (0.32e-12, 0.155e-12, "PSR J1713+J0437 2025", True),       # pulsar rep
    (-7e-12, 12e-12, "PSR J1738+0333", True),
]


def combine(rows):
    v = np.array([r[0] for r in rows]); s = np.array([r[1] for r in rows])
    w = 1 / s ** 2
    mean = (w * v).sum() / w.sum()
    err = 1 / np.sqrt(w.sum())
    chi2 = (((v - mean) / s) ** 2).sum()
    dof = max(len(rows) - 1, 1)
    return mean, err, chi2, dof


def main():
    print("B1 INTERNAL CONSISTENCY")
    for name, rows in (("alpha-dot/alpha", [r for r in ALPHA if r[3]]),
                       ("Gdot/G", [r for r in GDOT if r[3]])):
        m, e, chi2, dof = combine(rows)
        print(f"  {name}: {len(rows)} independent determinations, "
              f"chi2/dof = {chi2:.2f}/{dof} = {chi2/dof:.2f} -> "
              f"{'consistent' if chi2/dof < 2 else 'INTERNALLY INCONSISTENT'}")
        for v, s, lab, _ in rows:
            print(f"     {lab:32s} {v:+.2e} +/- {s:.1e}  ({abs(v/s):.1f} sigma from 0)")
    print()

    a_m, a_e, _, _ = combine([r for r in ALPHA if r[3]])
    g_m, g_e, _, _ = combine([r for r in GDOT if r[3]])
    print(f"B2 COMBINED: alpha-dot/alpha = {a_m:+.2e} +/- {a_e:.2e} /yr")
    print(f"             Gdot/G          = {g_m:+.2e} +/- {g_e:.2e} /yr")
    print(f"   (the alpha combination is dominated by the Yb+ clock; the G")
    print(f"    combination is dominated by LLR at {7.6e-14:.1e})\n")

    print("B3 THE TEST, per method and combined:")
    for gv, gs, lab, use in GDOT:
        if not use and "Zhu" not in lab and "Williams" not in lab:
            continue
        pred, perr = -2 * gv, 2 * gs
        sig = abs(pred - a_m) / np.hypot(perr, a_e)
        print(f"   from {lab:32s}: predicts {pred:+.2e} -> {sig:5.2f} sigma "
              f"{'CONSISTENT' if sig < 2 else ('TENSION' if sig < 3 else 'REFUTED')}")
    pred, perr = -2 * g_m, 2 * g_e
    sig = abs(pred - a_m) / np.hypot(perr, a_e)
    print(f"   COMBINED                          : predicts {pred:+.2e} -> "
          f"{sig:5.2f} sigma "
          f"{'CONSISTENT' if sig < 2 else ('TENSION' if sig < 3 else 'REFUTED')}")
    assert sig < 2

    print("\nB4 THE 2025 PULSAR CENTRAL VALUE, reported whether or not it flatters:")
    g5, s5 = 0.32e-12, 0.155e-12
    print(f"   PSR J1713+J0437 (2025) gives Gdot/G = {g5:+.2e} +/- {s5:.2e},")
    print(f"   which is {g5/s5:.1f} sigma FROM ZERO -- the only nonzero-leaning")
    print(f"   G determination in the set.")
    imp = -2 * g5
    print(f"   IF THAT CENTRAL VALUE IS REAL, the relation implies")
    print(f"   alpha-dot/alpha = {imp:+.2e} /yr, which sits "
          f"{abs(imp - a_m)/a_e:.0e} sigma from the clock combination.")
    print(f"   So the relation and a real 3e-13 G drift CANNOT BOTH HOLD.")
    print(f"   The relation currently survives only because that pulsar result is")
    print(f"   itself marginal and disagrees in SIGN with the earlier analyses of")
    print(f"   the SAME pulsar (Zhu 2015: {-0.6e-12:+.1e}, Zhu 2019: {-0.1e-12:+.1e}).")
    print(f"   LINEAGE CHECK on that pulsar: three analyses of one system give")
    print(f"   -0.60, -0.10, +0.32 (e-12) -- the sign has flipped and the spread")
    print(f"   exceeds the latest quoted error. THIS IS THE MEASUREMENT TO WATCH.")

    print("\nB5 HONESTY: the combination is still null-vs-null and the verdict is")
    print("   still survival, not confirmation. What has changed is that the test")
    print("   now has a NAMED WEAK POINT: PSR J1713+0747's G-drift determination,")
    print("   where a confirmed positive result at the 2025 central value would")
    print("   refute PRED-003 outright. That is a sharper statement than the first")
    print("   confrontation could make, and it does not depend on future instruments.")


if __name__ == "__main__":
    main()
