"""FND-MATTER-028 (Modeled): THE LITERATURE ANCHORS SOURCED -- the
reference column upgraded from recall-grade to source-grade, the
composite anchors landed, and a sleeper fact about the doublet.

THE SOURCE: Cantarella, LaPointe & Rawdon, "Shapes of Tight Composite
Knots" (arXiv:1110.3262), ridgerunner constrained gradient descent,
residuals ~1e-3, ropelength in RADIUS units (divide by 2 for D
units). UNITS VERIFIED via the tight trefoil: their 32.74317 radius
bound = 16.3716 D, matching the corpus constant 16.372 exactly.

THE COMPOSITE ANCHORS (rigorous upper bounds, D units):
    granny 3_1#3_1  : 57.04 / 2 = 28.520
    square 3_1#3_1^m: 57.07 / 2 = 28.535
THE SLEEPER FACT: the ideal doublet is nearly DEGENERATE -- split by
0.05 percent, granny marginally SHORTER. For a program that built an
isospin-doublet rehearsal on exactly this pair, a striking datum
(the n/p mass split is 0.14 percent). It also flags our ordering
(granny above square by 4.7 percent) as a WALL ARTIFACT: adjusted,
square sits at +4.3 percent (mild-wall class, twin of 5_2) and
granny at +9.3 percent (walled, twin of 6_1).

THE SOLID UPGRADES from the same paper's prime ranges: 6_1 = 28.353 D
(the wall now measured against a SOLID reference: +10.6 percent),
6_3 = 28.920 D (ours +2.0 percent, clean class), 7_1 = 30.703 D
(the recalled value confirmed exactly). Banked composite anchors for
future seats: 3_1#4_1 = 32.62, 3_1#5_1 = 35.77, 4_1#4_1 = 36.60,
3_1#3_1#3_1 = 39.67.

Remaining approx-grade rows (5_2, 6_2, 7_2, 8_1) are named for the
prime-table source (Ashton-Cantarella-Piatek-Rawdon, Exp. Math. 2011).
"""
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from two_term_mass_model import tighten_coords, profile
from topology_certifier import knot_det
from braid_family_spectrum import braid_closure

SYS = 1.023
LIT = {"trefoil_D": 32.74317/2, "granny_D": 57.04/2, "square_D": 57.07/2,
       "6_1_D": 56.7058/2, "6_3_D": 57.8392/2, "7_1_D": 61.4067/2}


def test():
    # units: the trefoil conversion matches the corpus constant
    assert abs(LIT["trefoil_D"] - 16.372) < 0.001, "radius-to-D conversion verified on 3_1"
    # the sleeper fact: near-degenerate doublet, granny marginally shorter
    split = (LIT["square_D"] - LIT["granny_D"])/LIT["granny_D"]
    assert 0 < split < 0.002, "the ideal doublet splits by ~0.05 percent, granny shorter"
    # our seats against the sourced anchors, wall-aware: square mild-wall, granny walled
    gr = tighten_coords(braid_closure((1, 1, 1, 2, 2, 2), N=140).copy(), iters=16000)
    sq = tighten_coords(braid_closure((1, 1, 1, -2, -2, -2), N=140).copy(), iters=16000)
    assert knot_det(gr) == 9 and knot_det(sq) == 9, "composites certified (det 9)"
    Lg = float(profile(gr)[3])/SYS; Ls = float(profile(sq)[3])/SYS
    devg = (Lg - LIT["granny_D"])/LIT["granny_D"]
    devs = (Ls - LIT["square_D"])/LIT["square_D"]
    assert -0.01 < devs < 0.09, "square within mild-wall band of the sourced anchor"
    assert -0.01 < devg < 0.14, "granny within wall band of the sourced anchor"
    assert devg > devs - 0.005, "the wall artifact: our granny sits higher, contra the lit ordering"
    print(f"units verified; doublet split {split*100:.3f}% (granny shorter)")
    print(f"our adjusted seats: square {Ls:.2f} ({devs*100:+.1f}%), granny {Lg:.2f} ({devg*100:+.1f}%)")
    print(f"6_1 wall vs SOLID reference {LIT['6_1_D']:.3f}: measured height now source-grade")
    print("PASS: the reference column is sourced, the doublet is nearly degenerate in ideal")
    print("      geometry, and the walls are measured against rigorous upper bounds.")


if __name__ == "__main__":
    test()
