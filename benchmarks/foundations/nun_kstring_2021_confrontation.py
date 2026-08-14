"""COMMISSION NUN -- FND-101: the FND-055 external clock fires.

Confront the derived exclusion statistic b_k = (k-1)/(N-1)
(antisymmetric-Casimir sigma_k/sigma_1 = k(N-k)/(N-1)) and the sine
law against the Athenodorou-Teper 2021 continuum determination
(arXiv:2106.00364, Section 3.4 global fits), per the locked bars in
analysis/NUN_kstring_2021_confrontation_bars_LOCKED.md.

No fitted parameters on the corpus side. Data side is transcribed
from the paper verbatim.
"""

import math

# Paper's global continuum fits (Section 3.4), transcribed verbatim.
FIT_A = dict(c1=1.28, c1_err=0.19, c2=4.78, c2_err=0.90, chi2ndf=0.5)
FIT_B = dict(c2=14.43, c2_err=0.60, c4=73.8, c4_err=12.1, chi2ndf=2.2)

# Derived laws, k = 2 (no free parameters).
def casimir(N):
    return 2.0 * (N - 2) / (N - 1)  # k(N-k)/(N-1), k=2

def sine(N):
    return math.sin(2 * math.pi / N) / math.sin(math.pi / N)  # = 2 cos(pi/N)

def fit_a(N):
    v = 2.0 - FIT_A["c1"] / N - FIT_A["c2"] / N ** 2
    e = math.hypot(FIT_A["c1_err"] / N, FIT_A["c2_err"] / N ** 2)
    return v, e

def fit_b(N):
    v = 2.0 - FIT_B["c2"] / N ** 2 + FIT_B["c4"] / N ** 4
    e = math.hypot(FIT_B["c2_err"] / N ** 2, FIT_B["c4_err"] / N ** 4)
    return v, e

def main():
    print("COMMISSION NUN: k-string continuum confrontation (AT 2021)")
    print()

    # S1: leading-power test. Sine expansion has zero 1/N coefficient;
    # exclusion statistic has -2/N. Paper prefers FIT_A (nonzero 1/N).
    ratio = FIT_B["chi2ndf"] / FIT_A["chi2ndf"]
    s1_sine_rejected = ratio > 2.0
    print(f"S1 leading-power: chi2/ndf FIT_B / FIT_A = {ratio:.1f} "
          f"(rule: > 2 rejects pure-1/N^2 sine class)")
    print(f"S1 verdict: sine-class {'REJECTED' if s1_sine_rejected else 'not rejected'}")
    print()

    # S2: coefficient test. Derived leading coefficient is exactly 2.
    dev = (2.0 - FIT_A["c1"]) / FIT_A["c1_err"]
    print(f"S2 coefficient: measured 1/N coeff {FIT_A['c1']}({FIT_A['c1_err']}) "
          f"vs derived 2 exactly -> {dev:.1f} sigma")
    s2_miss = dev > 3.0
    print(f"S2 verdict: {'MISS (>3 sigma)' if s2_miss else 'within tolerance'}")
    print()

    # S3: SU(6) point read, display only.
    N = 6
    va, ea = fit_a(N)
    vb, eb = fit_b(N)
    print("S3 (display only), SU(6) k=2:")
    print(f"  Casimir band: {casimir(N):.4f}   sine band: {sine(N):.4f}")
    print(f"  FIT_A value:  {va:.4f} +/- {ea:.4f} (uncorr. approx)")
    print(f"  FIT_B value:  {vb:.4f} +/- {eb:.4f} (uncorr. approx)")
    print(f"  Prior registered record (non-continuum): 1.733 (~sine, +8.3%)")
    print()

    # Pre-committed verdict grammar.
    if s1_sine_rejected and not s2_miss:
        verdict = "VINDICATED"
    elif s1_sine_rejected and s2_miss:
        verdict = "SPLIT: class confirmed against sine, exact coefficient convicted"
    else:
        verdict = "FALSIFIED per FND-055 clause"
    print(f"VERDICT (per locked grammar): {verdict}")

    # Machine checks.
    assert abs(casimir(6) - 1.6) < 1e-12
    assert abs(sine(6) - math.sqrt(3)) < 1e-12
    assert s1_sine_rejected
    assert abs(dev - 3.789) < 0.01
    assert s2_miss
    assert 1.60 < va < 1.7321  # SU(6) fit value lies between the bands
    print("ALL CHECKS PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
