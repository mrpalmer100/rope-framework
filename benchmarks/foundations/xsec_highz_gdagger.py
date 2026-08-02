"""XSEC-003 (Modeled): THE HIGH-REDSHIFT TEST RUNS, AND THE JOINT
PREDICTION SURVIVES -- g_dagger does NOT track H(z). Hypothesis B is
excluded at 7.4 sigma in the highest redshift bin.

THE DATA. RC100 (Nestor Shachar et al. 2023, ApJ 944:78), Table B1:
100 massive star-forming discs at z = 0.6-2.5 with forward-modelled
kinematics, giving per galaxy the redshift, effective radius,
circular velocity at Re, and dark-matter fraction fDM(Re).

THE ESTIMATOR. Since fDM = V_DM^2/V_circ^2, the baryonic acceleration
follows directly: g_bar = g_obs (1 - fDM) with g_obs = V_circ^2/Re.
Inverting the simple interpolation function used locally,
g_obs = g_bar/(1 - exp(-sqrt(g_bar/g_dagger))), gives the closed form
    g_dagger = g_bar / [ln fDM]^2
so each galaxy yields one estimate with no fitting.

THE CONTROL, run before the result was read. The same single-point
estimator applied to the 2597 usable SPARC points returns a median of
1.225e-10 against the full-curve value of 1.09e-10: THE ESTIMATOR IS
BIASED HIGH BY 1.13x (+0.053 dex). The comparison is therefore made
against 1.225e-10, the local value measured the SAME WAY, not against
the published 1.083e-10.

THE RESULT:
  z = 0.6-1.2 (n=32, <z>=0.83): g_dagger = 1.878e-10
      vs A (constant): +0.186 dex = +2.5 sigma
      vs B (~H(z))   : -0.017 dex = -0.2 sigma
  z = 1.2-2.0 (n=27, <z>=1.50): g_dagger = 1.384e-10
      vs A: +0.053 dex = +0.7 sigma ;  vs B: -0.313 dex = -4.2 sigma
  z = 2.0-2.6 (n=41, <z>=2.22): g_dagger = 1.284e-10
      vs A: +0.021 dex = +0.3 sigma ;  vs B: -0.494 dex = -7.4 sigma

THE TREND: d log g_dagger/d log(1+z) = -0.381 +/- 0.392, against
0.000 predicted by A (-1.0 sigma) and +1.111 predicted by B
(-3.8 sigma).

VERDICT: the acceleration scale does NOT grow with H(z). The
medium-extent reading forced by XSEC-001 -- that g_dagger measures a
FIXED extent laid down at formation rather than the current expansion
rate -- is what the data show. Hypothesis B is excluded decisively in
the two higher bins.

THE ONE DISCREPANT POINT, kept: the lowest redshift bin sits +2.5
sigma above the constant prediction, and is the only bin where B fits
better. With three bins this is not a trend (the global slope is
negative), but it is not noise-free either, and the corpus records it
rather than smoothing it.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'XSEC004_state.npz')
    z, gd, ok = s['z'], s['gd'], s['ok']
    assert len(z) == 100, "RC100: 100 galaxies"
    assert 0.6 <= z.min() and z.max() <= 2.6, "z = 0.61-2.52"
    assert int(ok.sum()) > 90, "essentially all usable"
    # the control: the estimator is biased and the bias was measured
    assert 1.05 < float(s['bias']) < 1.25, "single-point estimator biased high by 1.13x"
    assert abs(float(s['base']) - 1.225e-10)/1.225e-10 < 0.05, \
        "the comparison baseline is the LOCAL value measured the same way"
    # the result: B is excluded in the two high bins
    res = s['res']   # rows: z, med, err, dA, dB, n
    for zz, med, err, dA, dB, n in res:
        if zz > 1.2:
            assert dB/err < -3, f"z={zz:.2f}: hypothesis B excluded at >3 sigma"
            assert abs(dA/err) < 1.5, f"z={zz:.2f}: hypothesis A consistent"
    hi = res[-1]
    assert hi[4]/hi[2] < -6, "highest bin excludes B at 7.4 sigma"
    # the trend
    sl, se, slB = float(s['slope']), float(s['se']), float(s['slopeB'])
    assert abs(sl - 0)/se < 2, "slope consistent with zero (hypothesis A)"
    assert abs(sl - slB)/se > 3, "slope inconsistent with H(z) tracking (hypothesis B)"
    print(f"bias {float(s['bias']):.3f}x; base {float(s['base']):.3e}; "
          f"z=2.22 bin: A {hi[3]/hi[2]:+.1f} sigma, B {hi[4]/hi[2]:+.1f} sigma; "
          f"slope {sl:+.3f}+/-{se:.3f} vs A 0.000, B {slB:+.3f}")
    print("PASS: g_dagger does NOT track H(z) -- the medium-extent reading survives, and")
    print("      hypothesis B is excluded at 7.4 sigma in the highest redshift bin.")


if __name__ == "__main__":
    test()
