"""HBAR-005 (Modeled): THE DIMENSIONAL AUDIT -- no combination of the
medium's constants gives hbar, and the reason is informative: hbar is
MESOSCOPIC in this framework, the action of a patch ~75 strand
spacings across.

THE AUDIT. The strand medium has exactly two independent lengths (the
spacing w = 0.0578 fm and the thickness d_c = 1.87e-4 fm) plus T and
c; the vacuum density is not independent, since rho = T/(c^2 w^2)
reproduces the registered 5.670e18 exactly. Any action built from T,
c and a length must take the form S ~ T L^2/c, the only dimensionally
consistent combination, so the whole question is WHICH LENGTH.

THE ANSWER hbar demands: L_hbar = sqrt(hbar c/T) = 4.312 fm.

THE MEDIUM'S OWN ACTIONS, all of them:
    spacing w           -> 1.79e-4 hbar
    thickness d_c       -> 1.88e-9 hbar
    sqrt(w d_c)         -> 5.81e-7 hbar
    w^2/d_c             -> 1.71e+1 hbar
NONE is hbar. The closest, the strand spacing, is short by 5575x, and
L_hbar = w^1.752 d_c^-0.752 has no simple exponent, so there is no
natural combination either. THE FIVE-MINUTE CHECK COMES BACK NEGATIVE.

WHAT IT ESTABLISHES POSITIVELY, and this is the substantive part:
L_hbar/w = 74.7, so hbar corresponds to a coherent patch of ~5575
strands (HBAR-001's 3549 differs only by the pi/2 convention). HBAR IS
NOT A MICROSCOPIC QUANTITY IN THIS FRAMEWORK. It is mesoscopic -- the
action of a region 75 spacings across -- which means the framework
predicts genuine SUB-QUANTUM structure below 4.3 fm, where actions
smaller than hbar exist and are ordinary. That is a substantive
prediction and it connects this family directly to the corpus's
pilot-wave work (QGATE-011/012/013), which assumed sub-quantum
dynamics without a scale; this supplies the scale.

THE QUESTION IT SHARPENS TO: why 75 spacings? Nothing in T, w, d_c or
c supplies that number. It must come from dynamics -- or hbar is an
input to this framework rather than an output.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'HBAR007_state.npz')
    hbar = 1.054571817e-34; c = 2.99792458e8
    T = float(s['T']); w = float(s['w']); d_c = float(s['d_c'])
    # the density is not independent
    assert abs(T/(c**2*w**2)/5.670e18 - 1) < 1e-3, "rho = T/(c^2 w^2): not an independent constant"
    # the length hbar demands
    assert abs(float(s['L_h']) - np.sqrt(hbar*c/T))/float(s['L_h']) < 1e-9, "L_hbar = sqrt(hbar c/T)"
    assert 4e-15 < float(s['L_h']) < 5e-15, "4.312 fm"
    # no medium action is hbar
    assert float(s['S_w'])/hbar < 1e-3, "spacing gives 1.8e-4 hbar"
    assert float(s['S_d'])/hbar < 1e-8, "thickness gives 1.9e-9 hbar"
    assert float(s['short']) > 1e3, "short by 5575x"
    # and no simple exponent connects them
    a = float(s['expo'])
    assert min(abs(a - r) for r in (0.0, 0.5, 1.0, 1.5, 2.0)) > 0.2, \
        "L_hbar = w^1.752 d_c^-0.752: no natural combination"
    # the positive: hbar is mesoscopic
    assert 50 < float(s['ratio_w']) < 100, "L_hbar is ~75 strand spacings"
    assert 3000 < float(s['n_w']) < 8000, "a patch of ~5575 strands"
    print(f"L_hbar {float(s['L_h'])*1e15:.3f} fm = {float(s['ratio_w']):.1f} w; medium actions "
          f"{float(s['S_w'])/hbar:.2e}, {float(s['S_d'])/hbar:.2e} hbar; short by "
          f"{float(s['short']):.0f}x; patch {float(s['n_w']):.0f} strands")
    print("PASS: no medium constant gives hbar -- and hbar is MESOSCOPIC here, ~75 spacings,")
    print("      so the framework predicts real sub-quantum structure below 4.3 fm.")


if __name__ == "__main__":
    test()
