"""HBAR-004 (Modeled): THE TWIST ROUTE FAILS, FOR A REASON THAT
GENERALIZES -- topology is scale-invariant and hbar is not.

THE HYPOTHESIS TESTED: a rope carries a material frame, so a closed
loop obeys Calugareanu, Lk = Tw + Wr with Lk an integer. If writhe
grew as amplitude squared -- the same way the mode action does -- then
an integer Lk would quantize the amplitude and hence the action.

STEP 1, THE PROMISING PART: writhe IS quadratic in amplitude. For a
helically perturbed circle, doubling A multiplies Wr by 3.98, 3.92
(n = 3) and 3.89, 3.59 (n = 6), converging on 4 as A shrinks and the
higher-order terms drop away. Wr and S share the same A^2 scaling, so
the mechanism is at least well-posed.

STEP 2, THE FIRST FAILURE: Calugareanu constrains the SUM. Lk is an
integer, but Wr is not -- the TWIST absorbs the remainder,
Tw = Lk - Wr, and Wr varies continuously with amplitude while Tw
compensates. Twist does not quantize the amplitude at all unless it
is separately locked by some energetic mechanism the framework has
not supplied.

STEP 3, THE DECISIVE FAILURE. Even granting a locked twist, writhe is
DIMENSIONLESS: computed at (A, R) = (0.04, 1), (0.08, 2) and
(0.40, 10) it returns -0.019051 identically -- it depends only on the
ratio A/R. So Wr = 1 fixes A/R = 0.2891, and the resulting action is
    S = pi T (A/R)^2 R^2/(2c) = 7.44e-7 x R^2
which scales with the loop size: 7.1e-9 hbar at R = 1e-18 m,
7.1e-3 hbar at 1e-15 m, 7.1e3 hbar at 1e-12 m. A loop twice as large
would carry a quantum four times bigger.

THE REASON IT GENERALIZES: hbar is a dimensionful constant and every
topological invariant is dimensionless. A condition on an invariant
can fix a RATIO but never a SCALE. HBAR-001's attraction was precisely
that its action formula had no length in it; imposing a topological
condition puts the length back. No topological route can supply a
universal quantum of action, and this closes the family of attempts
rather than one member of it.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from rope_solver.topology.linking import writhe


def helical(A, n, M, R):
    t = np.linspace(0, 2*np.pi, M, endpoint=False)
    nrm = np.column_stack([np.cos(t), np.sin(t), np.zeros_like(t)])
    binm = np.column_stack([np.zeros_like(t), np.zeros_like(t), np.ones_like(t)])
    base = R*np.column_stack([np.cos(t), np.sin(t), np.zeros_like(t)])
    return base + A*(np.cos(n*t)[:, None]*nrm + np.sin(n*t)[:, None]*binm)


def test():
    s = np.load(ROOT/'analysis'/'HBAR006_state.npz')
    # step 1: quadratic in amplitude
    w1 = writhe(helical(0.02, 3, 400, 1.0))
    w2 = writhe(helical(0.04, 3, 400, 1.0))
    assert 3.7 < w2/w1 < 4.3, "writhe is quadratic in amplitude, like the action"
    # step 3: and scale-invariant, which is fatal
    inv = s['Wr_scaleinv']
    assert abs(inv[0] - inv[1])/abs(inv[0]) < 1e-6, \
        "writhe identical at (A,R) and (2A,2R): DIMENSIONLESS"
    # the consequence: the quantized action scales as R^2
    coeff = float(s['S_coeff'])
    hbar = 1.054571817e-34
    S_small = coeff*(1e-18)**2; S_big = coeff*(1e-12)**2
    assert S_big/S_small > 1e11, "the resulting quantum scales as R^2: NOT universal"
    assert S_small/hbar < 1e-6 and S_big/hbar > 1e2, \
        "spanning 1e-9 to 1e4 hbar across plausible loop sizes"
    assert 0.2 < float(s['A_over_R']) < 0.4, "Wr = 1 fixes only the RATIO A/R = 0.289"
    print(f"Wr quadratic (ratio {w2/w1:.2f}); scale-invariant ({inv[0]:.6f} = {inv[1]:.6f}); "
          f"Wr=1 fixes A/R={float(s['A_over_R']):.4f}; S = {coeff:.2e} R^2 -> "
          f"{S_small/hbar:.1e} to {S_big/hbar:.1e} hbar")
    print("PASS: the twist route fails twice -- twist absorbs the remainder, and topology is")
    print("      dimensionless while hbar is not. A ratio can be fixed; a scale cannot.")


if __name__ == "__main__":
    test()
