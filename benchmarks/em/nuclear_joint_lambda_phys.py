"""NUC-014 (Modeled): THE JOINT RE-RUN AT lambda_phys REVERSES BOTH OF
THIS SESSION'S MECHANISMS -- every refinement moves the surface/volume
ratio AWAY from the empirical value, and the simplest model is the
closest.

THE SETUP, made consistent for the first time. All variants share one
lattice, one N-ladder (55-683), the physical force range
lambda_phys = 0.4886 (from L = 1.4 fm and the saturation spacing
2.03 fm), and a contact core rc = 0.5651 chosen so the PAIR EQUILIBRIUM
SITS EXACTLY AT THE LATTICE SPACING -- without which "relaxation" merely
measures a mismatched core.

THE LADDER:
    pure contact (nearest only)      a_V 6.020  a_S 8.261  ratio 1.372
    Yukawa at lambda_phys, no core   a_V 4.003  a_S 7.542  ratio 1.884
    Yukawa + matched core            a_V 3.590  a_S 6.972  ratio 1.942
      + relaxation                   a_V 4.032  a_S 8.185  ratio 2.030
      + diffuse surface              a_V 3.462  a_S 7.635  ratio 2.206
      + both                         a_V 3.866  a_S 8.807  ratio 2.278
    EMPIRICAL                                              ratio 1.160
All fits R^2 >= 0.9986.

THE REVERSAL. NUC-011 reported relaxation closing 37 percent of the gap
and NUC-012 reported diffuseness closing 10 percent. Both were measured
against a baseline built with a force range 2.05x too long AND, in
NUC-011's case, a repulsive core whose equilibrium did not sit at the
lattice spacing -- so its "relaxation" was largely the cluster escaping
an artificial compression. Repaired, BOTH MECHANISMS RAISE THE RATIO:
1.942 -> 2.030 (relaxation), 1.942 -> 2.206 (diffuseness),
1.942 -> 2.278 (both).

WHY THE CORE HURTS, since it is counter-intuitive. B = attraction minus
repulsion, so the ratio is (A_S - R_S)/(A_V - R_V). The r^-12 core is
effectively nearest-neighbour, with its own surface/volume ratio near
1.1, well below the Yukawa attraction's 1.88. Subtracting a
lower-ratio component from both terms RAISES the combined ratio. The
sign is structural, not numerical.

THE STANDING RESULT: the model reproduces the empirical surface/volume
ratio best when it is SIMPLEST -- pure nearest-neighbour contact gives
1.372 against 1.160, and every physical elaboration the sector has
added since makes it worse.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'NUCS006_state.npz')
    tab = s['tab']            # NN, yuk, core : a_V, a_S, ratio, R^2
    joint = s['joint']        # rigid+sharp, relaxed+sharp, rigid+diffuse, relaxed+diffuse
    # the core is matched to the lattice spacing
    assert 0.5 < float(s['rc']) < 0.62, "core rc = 0.5651, pair equilibrium at NN"
    assert abs(float(s['lam']) - 0.4886) < 0.001, "lambda_phys"
    # every fit is good, so the ordering is not a fitting artifact
    assert (tab[:, 3] > 0.998).all() and (joint[:, 3] > 0.998).all(), "all R^2 >= 0.9986"
    # the ladder: simplest is closest
    nn, yuk, core = tab[0, 2], tab[1, 2], tab[2, 2]
    assert nn < yuk < core, "adding the tail and then the core RAISES the ratio"
    assert abs(nn - 1.16) < abs(yuk - 1.16) < abs(core - 1.16), "each step moves away from 1.16"
    # the reversal: both mechanisms now hurt
    rigid_sharp, relaxed_sharp, rigid_diff, both = joint[:, 2]
    assert relaxed_sharp > rigid_sharp, "relaxation RAISES the ratio (NUC-011 reversed)"
    assert rigid_diff > rigid_sharp, "diffuseness RAISES the ratio (NUC-012 reversed)"
    assert both > relaxed_sharp and both > rigid_diff, "and together they are worst"
    # the simplest model remains closest of everything tested
    allr = list(tab[:, 2]) + list(joint[:, 2])
    assert min(abs(np.array(allr) - 1.16)) == abs(nn - 1.16), \
        "pure contact is the closest of every variant tested"
    print(f"contact {nn:.3f} < Yukawa {yuk:.3f} < +core {core:.3f} < +relax "
          f"{relaxed_sharp:.3f} < +diffuse {rigid_diff:.3f} < both {both:.3f} | target 1.160")
    print("PASS: the joint re-run reverses both mechanisms -- every refinement moves the")
    print("      ratio away from empirical, and the simplest model is the closest.")


if __name__ == "__main__":
    test()
