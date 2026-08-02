"""XSEC-005 (Modeled): THE PHOTOMETRIC RE-RUN CONFIRMS THE CIRCULARITY
AND DESTROYS THE RESULT -- XSEC-003's clean trend does not survive
replacing fitted baryonic masses with photometric ones, and no clean
trend replaces it.

THE FIX ATTEMPTED. RC100's Table B1 lists log M* separately from
log M_baryon, and the stellar masses are photometric (3D-HST SED fits)
rather than fitted to the kinematics. Re-running XSEC-003's estimator
on M* (plus a Tacconi-type gas scaling) removes the circularity
XSEC-004 identified, using data already in hand.

THE SMOKING GUN. The fitted-to-photometric mass ratio has median 1.549
-- plausible as a gas correction -- but a 16th-84th range of
0.83-2.34, and in 22 percent of galaxies THE FIT DEMANDS LESS BARYONIC
MASS THAN THE OBSERVED STARS. A gas correction can only add mass. A
parameter that goes both ways is not measuring baryons; it is
absorbing kinematic residuals, which is precisely the circularity.

THE PHYSICALITY PROBLEM. Under the Tacconi-scaled budget, 51 of 100
galaxies have g_bar > g_obs -- baryons alone exceeding the observed
acceleration, which is unphysical. Even at half that gas, 35 fail.
Only the stars-only budget keeps most of the sample (86 usable), and
that budget UNDERSTATES the baryons by construction. Either the gas
prescription is wrong, or the enclosed fraction is, or RC100's
photometric masses and kinematics are mutually inconsistent at this
level. Any of the three defeats the test.

THE RESULT. Under stars-only -- the only budget that keeps the sample
physical -- the three redshift bins give 5.56e-10, 2.82e-10 and
3.71e-10: non-monotonic, mutually inconsistent, and all far above both
hypotheses (+10.1, +4.1, +5.1 sigma against A). XSEC-003's clean
monotone trend was an artifact of the fitted masses. No trend replaces
it.

VERDICT: the photometric re-analysis supports NEITHER hypothesis. It
does not rescue the prediction and it does not refute it. Combined
with XSEC-004's KROSS attempt, the corpus now has two independent
demonstrations that the high-redshift acceleration scale is not
measurable with the data available to it.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'XSEC006_state.npz')
    # the smoking gun: the fitted mass goes BOTH ways against the stellar mass
    assert float(s['frac_below']) > 0.15, \
        "22% of fits demand LESS baryonic mass than the observed stars: not a gas correction"
    assert 1.3 < float(s['ratio_fit_phot']) < 1.9, "median ratio 1.55 looks plausible in isolation"
    # the physicality problem
    bad = s['grid_bad']; n = s['grid_n']
    assert bad[2] > 45, "Tacconi gas makes 51/100 unphysical (g_bar > g_obs)"
    assert bad[0] < 20, "stars-only keeps 86 usable"
    assert n[0] > n[1] > n[2], "usable sample shrinks monotonically as gas is added"
    # the result: no coherent trend
    rows = s['rows']          # zz, med, err, dA_sigma, dB_sigma, n
    meds = rows[:, 1]
    assert not (meds[0] > meds[1] > meds[2] or meds[0] < meds[1] < meds[2]), \
        "the three bins are NON-MONOTONIC: no coherent trend"
    assert all(abs(rows[i, 3]) > 3 for i in range(3)), \
        "and all three sit >3 sigma from hypothesis A"
    assert meds.max()/meds.min() > 1.5, "bins mutually inconsistent by a factor 2"
    print(f"fitted/stellar median {float(s['ratio_fit_phot']):.3f} but {float(s['frac_below'])*100:.0f}% below 1; "
          f"unphysical {bad[0]}/{bad[2]} (stars/gas); bins {meds[0]:.2e}, {meds[1]:.2e}, {meds[2]:.2e}")
    print("PASS: the circularity is confirmed, XSEC-003's trend does not survive, and the")
    print("      photometric re-analysis supports neither hypothesis.")


if __name__ == "__main__":
    test()
