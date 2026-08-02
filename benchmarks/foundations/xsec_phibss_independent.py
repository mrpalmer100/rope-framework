"""XSEC-006 (Modeled): PHIBSS REMOVES THE CIRCULARITY AND THE QUESTION
STILL WILL NOT CLOSE -- with genuinely independent baryonic masses the
systematics alone span both hypotheses, and XSEC-005's diagnosis of the
super-criticality is corrected.

THE DATA. PHIBSS (Tacconi et al. 2013, ApJ 768, 74; VizieR
J/ApJ/768/74): CO(3-2) observations of z = 1.0-2.4 main-sequence
galaxies, giving MEASURED molecular gas masses from CO luminosity
alongside photometric stellar masses, rotation velocities and
half-light radii. NEITHER MASS IS FITTED TO THE KINEMATICS -- the
first sample in this investigation for which that is true. 34 rotating
disks survive the cuts (28 quality-A), median gas fraction 0.47.

WHAT IT DELIVERS, AND WHAT IT CANNOT:
  1. The circularity that voided XSEC-003 is gone.
  2. But only 7 galaxies lie at z > 1.7, so THERE IS NO USABLE HIGH-z
     BIN and PHIBSS cannot test evolution on its own.
  3. At z ~ 1.19 the four defensible conventions (radius = Rh or 2Rh,
     pressure correction 0 or 30 percent) give 1.68e-10, 3.07e-10,
     9.77e-11 and 2.10e-10 -- SPLITTING 2-2 between hypothesis A
     (constant) and hypothesis B (H(z)-tracking).
Removing the circularity does not produce an answer; it reveals that
the remaining systematics alone span the effect.

A CORRECTION TO XSEC-005. That claim attributed RC100's
baryon-super-critical epidemic (51 percent of galaxies with
g_bar > g_obs) to the Tacconi gas prescription. THAT ATTRIBUTION WAS
WRONG. PHIBSS, with gas masses MEASURED from CO rather than scaled,
gives 41-68 percent depending only on the radius convention and
pressure correction:
    R=Rh,  no p-corr : 68%      R=2Rh, no p-corr : 56%
    R=Rh,  +30%      : 53%      R=2Rh, +30%      : 47%
                                R=2Rh, +70%      : 41%
The fraction is driven by the RADIUS/ENCLOSED-FRACTION and PRESSURE
choices, not by the gas. It is an artifact of applying a single-point
estimator to baryon-dominated high-z discs.

THE STANDING CONCLUSION after three samples. RC100: circular baryons,
void. KROSS: independent but stellar-only, spread 8x against a signal
of 1.6x. PHIBSS: independent and gas-measured, but no high-z lever and
conventions that split. THE HIGH-REDSHIFT ACCELERATION SCALE REMAINS
UNMEASURED -- and it is now clear WHY. The single-point method needs a
radius convention and a pressure correction, and at high redshift
those choices move g_dagger by more than the effect being sought. A
curve-FIT on resolved rotation curves, as used locally on SPARC, is
what the test actually requires.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'XSEC007_state.npz')
    # the sample exists and is independent, but has no high-z lever
    assert int(s['n']) > 25, "34 rotating disks with complete independent data"
    assert int(s['nhi']) < 10, "only 7 at z > 1.7: no usable high-redshift bin"
    assert 1.0 < float(s['zm']) < 1.4, "the one usable bin sits at z ~ 1.19"
    # the conventions split
    assert int(s['favA']) == 2 and int(s['favB']) == 2, \
        "four conventions split 2-2: PHIBSS does not discriminate"
    # the correction to XSEC-005: super-criticality is convention-driven, not gas-driven
    sc = s['supercrit']          # rows: rfac, f_enc, p_corr, fraction
    fr = sc[:, 3]
    assert fr.min() > 0.35 and fr.max() > 0.6, \
        "41-68% super-critical with MEASURED gas: the gas was not the cause"
    assert fr.max() - fr.min() > 0.2, \
        "the fraction varies by 27 points across conventions alone"
    # and it brackets RC100's 51%, showing the samples behave alike
    assert fr.min() < 0.51 < fr.max(), "RC100's 51% lies inside PHIBSS's convention range"
    print(f"n={int(s['n'])} ({int(s['nhi'])} at z>1.7); conventions split "
          f"{int(s['favA'])}-{int(s['favB'])}; super-critical {fr.min()*100:.0f}-{fr.max()*100:.0f}% "
          f"with MEASURED gas (RC100 scaled: 51%)")
    print("PASS: circularity removed and the question still will not close -- systematics")
    print("      span the effect, and XSEC-005's gas-prescription diagnosis is corrected.")


if __name__ == "__main__":
    test()
