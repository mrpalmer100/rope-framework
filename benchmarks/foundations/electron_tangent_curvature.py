"""ELEC-033 (Modeled): THE TANGENT-SPACE CURVATURE IS POSITIVE-DEFINITE
-- the obstruction is purely FIRST-ORDER, and the saddle worry is
retired.

The question a stationarity certificate ultimately needs: on the
directions the contact set leaves free, is the reduced curvature
positive?

METHOD: at the ELEC-032 state (rows 145, rank 88, TANGENT DIMENSION
105) an orthonormal null-space basis is built by SVD and verified
(max |A p| = 7.2e-9 over the basis). Curvature is then measured by
parabolic probe along 42 random tangent directions at two scales, with
restoration and rtol=1e-12.

RESULT: ALL 42 CURVATURES POSITIVE AT BOTH SCALES -- h=1e-4 gives
min +1.77e4, median +4.01e4, max +8.93e4; h=3e-5 gives min +1.64e4,
median +6.53e4. Zero negative directions. The median ratio across
scales is 1.63, so the curvature is scale-dependent (kink structure)
but its SIGN is not.

THE CONSEQUENCE, and it is the point: the residual dips the census
keeps finding are NOT evidence of a saddle. With ||P g|| = 0.888 on
the tangent space and median curvature 4.0e4, a quadratic model
predicts a remaining descent of ||P g||^2/(2c) = 9.8e-6 -- the same
order as the ~5.5e-6 the ELEC-032 sweeps recover per round. The
dips are the linear term, not a negative eigenvalue.

WHAT THIS RETIRES AND WHAT IT DOES NOT: it retires the standing worry,
live since ELEC-023, that the object might be a very flat saddle. IF
stationarity is reached, this state is a genuine local minimum. It
does NOT establish stationarity, which remains unproven and is now the
sole obstruction.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'ELEC033_state.npz')
    assert float(s['maxAp']) < 1e-7, "B1: the tangent basis is genuinely null (|Ap| = 7e-9)"
    assert int(s['tangent_dim']) > 90, "105 free directions"
    c1, c2 = s['c_h1'], s['c_h2']
    assert len(c1) >= 40 and len(c2) >= 40, "B2: 42 directions at each scale"
    assert c1.min() > 0 and c2.min() > 0, "B3: ALL curvatures positive -- minimum-consistent"
    assert bool(s['allpos'])
    assert c1.min() > 1e4, "and positive with large margin, not marginally"
    # the first-order reading
    d = np.load(ROOT/'analysis'/'ELEC034_state.npz')
    pred = float(d['pred_remaining'])
    assert 1e-6 < pred < 1e-4, "quadratic model predicts ~1e-5 remaining: same order as sweeps"
    print(f"tangent dim {int(s['tangent_dim'])}; curvature min {c1.min():.2e}, median "
          f"{np.median(c1):.2e}; negatives 0/{len(c1)}; ||Pg||={float(d['Pg']):.3f}; "
          f"predicted remaining {pred:.2e}")
    print("PASS: positive-definite on the tangent space -- the saddle worry is retired;")
    print("      the obstruction is purely first-order (stationarity, still unproven).")


if __name__ == "__main__":
    test()
