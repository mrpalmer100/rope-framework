"""NUC-018 (Modeled): NUC-005 RE-DERIVED WITH BOTH CORRECTIONS -- the
Coulomb term improves, the volume term degrades from 3 to 13 percent,
and the headline mass accuracy roughly doubles.

TWO CORRECTIONS WERE OWED. NUC-017 showed the spacing input d0 = 1.9 fm
is 6 percent below the observed saturation spacing 2.026 fm. NUC-016
showed the parameter-free surface ratio 1.108 is an ideal-facet value,
and the sphere value derived in NUC-015 is 1.34. Both feed NUC-005's
calibration, which fixes a_V on Ca-40 given the surface ratio and the
derived Coulomb coefficient.

APPLIED SEPARATELY AND TOGETHER:
    variant                          a_S/a_V  d0     a_C     a_V    err
    NUC-005 as registered              1.108  1.900  0.823  16.21  +2.9%
    + corrected spacing                1.108  2.026  0.772  15.99  +1.5%
    + corrected surface ratio          1.340  1.900  0.823  18.02 +14.4%
    BOTH                               1.340  2.026  0.772  17.77 +12.8%
    EMPIRICAL                       1.13-1.16 2.026  0.711  15.75

THE SPACING CORRECTION HELPS. a_C moves from 0.823 to 0.772 against an
empirical 0.711, improving from +16 to +9 percent, and a_V improves
slightly to +1.5 percent. Using the right density makes the derived
Coulomb term better.

THE SURFACE CORRECTION HURTS, and it is the larger effect. A bigger
surface term means Ca-40's measured binding demands a bigger volume
coefficient: a_V rises to 17.77, and the agreement with the empirical
15.75 degrades from 3 percent to 13 percent. NUC-005'S HEADLINE
THREE-PERCENT VOLUME RESULT WAS PARTLY SUPPORTED BY THE FACET ERROR.

MASS PREDICTIONS. The worst error across C-12 to U-238 goes from
0.289 to 0.514 percent, and NUC-005's registered range '0.01-0.11
percent' becomes '0.00-0.51 percent'. Ca-40 remains exact by
construction (it is the calibration point).

WHAT STANDS. The model still reproduces an absolute nuclear energy
scale to 13 percent from one constant, with the surface term
parameter-free and the Coulomb term derived. That is a real if weaker
result than the sector believed, and it is now built on corrected
inputs rather than compensating errors.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'NUCV002_state.npz')
    c = s['cases']            # ratio, d0, a_C, a_V, a_V err%
    reg, sp, surf, both = c
    # the registered baseline
    assert abs(reg[3] - 16.21) < 0.05 and abs(reg[4] - 2.9) < 0.3, "NUC-005 as registered"
    # the spacing correction improves both a_C and a_V
    assert sp[2] < reg[2], "corrected spacing lowers a_C toward 0.711"
    assert abs(sp[2] - 0.711)/0.711 < abs(reg[2] - 0.711)/0.711, "Coulomb improves 16% -> 9%"
    assert abs(sp[4]) < abs(reg[4]), "and a_V improves slightly"
    # the surface correction degrades a_V, and dominates
    assert surf[3] > reg[3], "a bigger surface term demands a bigger a_V"
    assert surf[4] > 12, "a_V error rises to +14.4 percent"
    assert abs(surf[4] - reg[4]) > abs(sp[4] - reg[4]), "the surface effect dominates the spacing one"
    # both together
    assert 17 < both[3] < 18.5 and 10 < both[4] < 16, "combined a_V = 17.77, +12.8 percent"
    # mass accuracy roughly doubles
    eo, en = s['errs_old'], s['errs_new']
    assert en.max() > eo.max(), "worst mass error grows"
    assert 1.5 < en.max()/eo.max() < 2.5, "roughly doubling, 0.289 -> 0.514 percent"
    assert en.max() < 0.01, "still under one percent on mass throughout"
    print(f"a_C {reg[2]:.3f} -> {both[2]:.3f} (empirical 0.711); a_V {reg[3]:.2f} -> {both[3]:.2f} "
          f"({reg[4]:+.1f}% -> {both[4]:+.1f}%); worst mass error {100*eo.max():.3f}% -> {100*en.max():.3f}%")
    print("PASS: spacing helps the Coulomb term, the facet correction costs the volume term,")
    print("      and NUC-005's 3 percent was partly supported by the error.")


if __name__ == "__main__":
    test()
