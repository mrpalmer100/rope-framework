"""THE J1713+0747 LINEAGE: is the Gdot/G history statistically normal, and
when does it decide PRED-003?

Bars locked in analysis/PRED003_J1713_bars_LOCKED.md BEFORE computing.
NOTE: this is an analysis of PUBLISHED results, not a re-timing of the pulsar.
"""
import numpy as np

L = [(2015, -0.6e-12, 0.55e-12, "Zhu et al. 2015, 21-yr NANOGrav"),
     (2019, -0.1e-12, 0.45e-12, "Zhu et al. 2019, MNRAS 482, 3249"),
     (2025, 0.32e-12, 0.155e-12, "2025, EPTA DR2, +J0437-4715")]
ALPHA_COMB, ALPHA_ERR = 9.89e-19, 1.10e-18


def main():
    print("B1 NESTED CONSISTENCY (each analysis uses a superset of the earlier data,")
    print("   so the expected shift is sqrt(s_old^2 - s_new^2), NOT the independent form):")
    for i in range(len(L) - 1):
        for j in range(i + 1, len(L)):
            (y0, v0, s0, _), (y1, v1, s1, _) = L[i], L[j]
            exp = np.sqrt(max(s0 ** 2 - s1 ** 2, 1e-99))
            naive = np.hypot(s0, s1)
            print(f"   {y0} -> {y1}: shift {v1-v0:+.2e}, expected sigma {exp:.2e} "
                  f"-> {abs(v1-v0)/exp:.2f} sigma   (naive independent test would say "
                  f"{abs(v1-v0)/naive:.2f})")
    worst = max(abs(L[j][1] - L[i][1]) / np.sqrt(max(L[i][2] ** 2 - L[j][2] ** 2, 1e-99))
                for i in range(len(L) - 1) for j in range(i + 1, len(L)))
    print(f"   WORST PAIRWISE: {worst:.2f} sigma -> "
          f"{'STATISTICALLY NORMAL' if worst < 2 else 'ANOMALOUS'}")
    print("   CORRECTION TO PRED-003-META: that claim described the spread as")
    print("   'exceeding the latest quoted error' with the sign 'flipping twice',")
    print("   which applied an independent-sample intuition to NESTED analyses. Under")
    print("   the correct test the lineage is unremarkable: successive analyses of one")
    print("   growing data set are EXPECTED to wander by roughly the difference in")
    print("   quoted errors, and these do. The sign changes are not evidence of a")
    print("   systematic; they are what a null measurement looks like as it sharpens.\n")

    print("B2 THE KNOWN SYSTEMATIC, which cuts the other way:")
    print("   PSR J1713+0747 underwent an abrupt pulse-profile change in April 2021")
    print("   (an earlier event occurred in 2016) that disrupted its timing stability;")
    print("   mitigation methods were still being published in July 2026. The EPTA DR2")
    print("   data underlying L3 runs up to this era, so L3's tighter error bar is")
    print("   drawn from a baseline whose late portion carries a documented, actively")
    print("   researched profile systematic. THIS IS AN ARGUMENT FOR CAUTION ABOUT L3")
    print("   independent of its statistics: the quoted 0.155e-12 assumes the profile")
    print("   event is fully absorbed by the noise model.\n")

    print("B3 THE DECISION FORECAST:")
    v3, s3 = L[-1][1], L[-1][2]
    need = abs(v3) / 3
    print(f"   a 3 sigma detection at L3's central value needs sigma = {need:.2e}")
    print(f"   (a factor {s3/need:.2f} below the present {s3:.2e})")
    # calibrate improvement: Pbdot precision ~ T^-5/2; L2 (2019, ~25 yr) -> L3 (2025, ~31 yr)
    t2, t3 = 25.0, 31.0
    predicted = (t3 / t2) ** 2.5
    observed = L[1][2] / s3
    print(f"   baseline scaling T^-5/2 predicts a {predicted:.2f}x gain from 2019->2025;")
    print(f"   the observed gain was {observed:.2f}x (extra telescopes and data volume).")
    yrs = t3 * ((s3 / need) ** (1 / 2.5)) - t3
    print(f"   on baseline growth ALONE, sigma reaches {need:.2e} after "
          f"~{yrs:.1f} more years (~{2025+yrs:.0f}).")
    yrs_fast = t3 * ((s3 / need) ** (1 / (2.5 * np.log(observed) / np.log(predicted)))) - t3
    print(f"   at the historically observed rate, ~{yrs_fast:.1f} years (~{2025+yrs_fast:.0f}).")
    print(f"   SO THE DECISION IS PLAUSIBLY WITHIN THIS DECADE, not four orders away.\n")

    print("B4 THE VERDICT FOR PRED-003:")
    imp = -2 * v3
    print(f"   If L3's central value is confirmed at 3 sigma, the relation implies")
    print(f"   alpha-dot/alpha = {imp:+.2e}/yr, which is {abs(imp-ALPHA_COMB)/ALPHA_ERR:.0e}")
    print(f"   sigma from the clock combination: PRED-003 WOULD BE REFUTED.")
    print(f"   If the central value regresses toward zero as the error tightens --")
    print(f"   which the nested analysis above says is entirely ordinary for a null --")
    print(f"   PRED-003 survives and its inverse commitment (G static to ~1e-18/yr)")
    print(f"   becomes progressively harder to evade.")
    print(f"   EITHER WAY THE CLAIM IS DECIDABLE BY ONE SYSTEM ON A KNOWN TIMESCALE,")
    print(f"   which is a better position than any other prediction in the corpus.")


if __name__ == "__main__":
    main()
