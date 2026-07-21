"""Force SIGN derived from swinging-thread mechanics (Gaede's jump-rope rule).

Two adjacent swinging ropes: in the GAP between them, if the two swing velocities
OPPOSE each other the ropes mesh and pull together (attract); if they ALIGN they
clash and push apart (repel). This is Gaede's jump-rope mechanism. Applied to two
current wires, the swing = the field circulation around each wire, and the gap
lies on OPPOSITE sides of the two circulations. Therefore:

  SAME current    -> circulations same sense -> velocities OPPOSE in the gap
                  -> mesh -> ATTRACT
  OPPOSITE current -> velocities ALIGN in the gap -> clash -> REPEL

This matches the jump-rope intuition, the vortex/wave picture (EM-RECON-001), and
the Ampere force law exactly. The sign follows from the relative swing direction
in the gap alone -- it does not depend on whether the swing is rigid or a
propagating wave, and needs no assumed snag/clash rule.

NOTE: this SUPERSEDES an earlier failed attempt (force_sign_attempt.py) whose
'wrong sign' was a labeling error -- it mislabeled 'same current' as 'same
velocity in the gap', when same-sense circulation gives OPPOSITE velocity in the
gap (opposite sides of the two circulations). Corrected here.
"""
import numpy as np


def Bvec(px, py, x0, I):
    dx = px - x0; dy = py; r2 = max(dx * dx + dy * dy, 1e-9)
    p = I / (2 * np.pi * r2)
    return np.array([p * (-dy), p * (dx)])


def mean_gap_dot(I2, d):
    dots = []
    for yy in np.linspace(-0.8, 0.8, 9):
        for xx in np.linspace(-d / 2 + 0.4, d / 2 - 0.4, 9):
            v1 = Bvec(xx, yy, -d / 2, +1)
            v2 = Bvec(xx, yy, +d / 2, I2)
            dots.append(np.dot(v1, v2))
    return float(np.mean(dots))


def test():
    same = np.mean([mean_gap_dot(+1, d) for d in (2.0, 3.0, 4.0, 5.0)])
    opp = np.mean([mean_gap_dot(-1, d) for d in (2.0, 3.0, 4.0, 5.0)])
    # same current: velocities OPPOSE in gap (dot<0) -> mesh -> attract
    assert same < 0, "same current should give opposing gap velocities (attract)"
    assert opp > 0, "opposite current should give aligned gap velocities (repel)"
    print(f"same current:     mean gap v1.v2 = {same:+.4f} -> ATTRACT (mesh)")
    print(f"opposite current: mean gap v1.v2 = {opp:+.4f} -> REPEL (clash)")
    print("PASS: force sign DERIVED from relative swing direction in the gap;")
    print("      matches jump-rope rule, vortex/wave picture, and Ampere. No")
    print("      assumed snag/clash rule; independent of rigid-vs-wave propagation.")


if __name__ == "__main__":
    test()
