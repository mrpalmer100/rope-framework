"""NUC-016 (Modeled): NUC-005'S PARAMETER-FREE SURFACE RESULT IS AN
IDEAL-FACET VALUE APPLIED TO A SPHERE -- the agreement is 18 percent,
not 2, and the empirical target is itself uncertain to 7 percent.

THE CLAIM AUDITED. NUC-005 registers 'surface term DERIVED FROM
GEOMETRY, zero parameters -- close-packed sphere, surface nucleons miss
~3 of 12 bonds: a_S/a_V = 1.108 predicted vs 1.130 empirical (2%)'.
This is the sector's strongest parameter-free result and it does not
survive.

THE CENSUS. Missing 3 of 12 is the (111) FACET value. On an actual
spherical droplet the surface coordination is measured directly:
    N = 201: 127 surface atoms, mean z = 7.56, mean deficit 4.44
    N = 459: 241 surface atoms, mean z = 7.99, mean deficit 4.01
    N = 923: 395 surface atoms, mean z = 8.12, mean deficit 3.88
with broad distributions running from z = 3 to z = 11. Surface atoms on
a sphere miss 3.9-4.4 bonds, not 3, because a sphere presents every
orientation and only a minority of its surface is (111)-like.

THE CONSEQUENCE. NUC-015 derived the sphere value analytically and
confirmed it on four lattices: 1.34, not 1.108. NUC-005's
parameter-free prediction therefore misses experiment by ABOUT 18
PERCENT, not the 2 percent registered. The 1.108 figure is correct only
for a perfectly (111)-faceted crystal, which a liquid-drop nucleus is
not.

AND THE TARGET IS NOT ONE NUMBER. Standard SEMF parameter sets give
a_S/a_V = 1.084 (Krane), 1.127 (original Bethe-Weizsacker), 1.130
(Wapstra), 1.158 (common) -- a 7 percent spread. The corpus has quoted
1.130 in NUC-005 and 1.16 in NUC-006 and NUC-015 without noting they
are different fits of the same data. Against the full range the model's
1.34 is 16-24 percent high.

WHAT SURVIVES OF NUC-005. Its VOLUME coefficient is a real result and
is untouched: eps calibrated once on Ca-40 gives a_V = 16.21 against
15.75 empirical, a 3 percent agreement on an absolute energy scale.
That is the sector's genuine parameter-light success, and it should
carry the weight the surface ratio was carrying.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'NUCS009_state.npz')
    cen = s['census']          # N, n_surface, mean z, mean deficit
    # the facet assumption fails on a sphere
    assert (cen[:, 3] > 3.5).all(), "mean surface deficit 3.9-4.4, not the facet's 3"
    assert (cen[:, 2] < 9.0).all(), "mean surface coordination below the facet value of 9"
    # and it converges toward ~3.9, not 3
    assert cen[-1, 3] > 3.7, "still 3.88 at N = 923: not approaching 3"
    # the model value is the sphere value, not the facet value
    assert abs(float(s['model']) - 1.34) < 0.02, "NUC-015's derived sphere value"
    assert abs(float(s['facet']) - 1.108) < 0.01, "NUC-005's facet value"
    assert float(s['model']) > float(s['facet'])*1.15, "they differ by over 20 percent"
    # the empirical target is a range
    t = s['targets']
    assert t.max()/t.min() > 1.05, "SEMF parameter sets span 7 percent"
    assert t.min() < 1.108 < t.max(), "the facet value sits INSIDE the empirical spread"
    # against the whole range the model is 16-24 percent high
    lo = 100*(float(s['model'])/t.max()-1); hi = 100*(float(s['model'])/t.min()-1)
    assert 10 < lo < 20 and 20 < hi < 30, "16-24 percent high across the target range"
    print(f"surface deficit {cen[0,3]:.2f}/{cen[1,3]:.2f}/{cen[2,3]:.2f} (facet assumes 3); "
          f"model 1.34 vs facet 1.108; targets {t.min():.3f}-{t.max():.3f}; "
          f"discrepancy {lo:.0f}-{hi:.0f}%")
    print("PASS: the parameter-free surface result was an ideal-facet value applied to a")
    print("      sphere -- 18 percent, not 2; the volume coefficient is untouched.")


if __name__ == "__main__":
    test()
