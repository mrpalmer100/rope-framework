"""ROPE-MODE-004 (Modeled): THE ROPE-ONLY BINDING TEST -- THE TUBE ALONE
BINDS; THE STRENGTH IS NOT YET MEASURED; AND THE BAR-SETTING RULE WAS
VIOLATED A THIRD TIME, BY THE AUDITOR.

The review's second commission: remove the imported central attraction
entirely (alpha = 0) and ask whether the certified ELEC-009 linked
tube (Gaussian width sigma = 0.10) binds anything by itself.

RESULT, four parts:
(1) BINDING EXISTS: sweeping beta = 1..16 on the 23^3 grid, a mode
    drops below the free-box continuum from beta ~ 4 and deepens
    monotonically (E0: 0.821 free -> 0.345 at beta = 16). The beta = 0
    control is clean.
(2) THE ROPE SIGNATURE HOLDS (B4): the bound mode HUGS THE TUBE --
    probability-weighted distance to the curve falls monotonically
    (1.235 free -> 0.869 at beta = 16, against a box mean of 2.19) and
    localization rises (0.745 -> 0.881). The binding is the rope's,
    not a generic well's.
(3) BAR MISSED AND KEPT -- CONVERGENCE (B2): between 23^3 and 29^3 the
    worst low-lying gap shifts 106 percent and E0 shifts 24 percent of
    its depth. The sigma = 0.10 tube at h ~ 0.21-0.25 is severely
    under-resolved: binding EXISTENCE is established at resolved
    depths, but the threshold and spectrum are NOT measured. (Physics
    note: an attractive tube is transversally quasi-2D and should bind
    at ANY beta; the numerical onset at beta ~ 4 is a resolution
    floor, consistent with under-resolution.)
(4) BAR VACUOUS AND KEPT -- THE CATCH-28 RECURRENCE (B1): the locked
    localization bar (0.70) sits BELOW the beta = 0 control's own
    baseline (0.745), making it vacuous as locked. This is the third
    violation of the measure-the-floor-first rule, committed by the
    session that registered the rule. Filed; the discriminating
    metrics are the below-continuum count and the tube-distance trend,
    and the corrected localization statement is the RISE (0.745 ->
    0.881), not the absolute value.

WHAT THIS DOES AND DOES NOT ESTABLISH: the binding prerequisite that
ROPE-MODE-003 lacked exists natively -- a surrounding 3-D field bound
to the rope alone is possible. Nothing here produces atomic
multiplets; the path to shell structure now runs through a properly
resolved tube (finer grids or adapted coordinates) before any
spectroscopy claim.
"""
import sys
from pathlib import Path
import numpy as np
from scipy.sparse import diags, eye, kron
from scipy.sparse.linalg import eigsh
from scipy.spatial import cKDTree

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from benchmarks.foundations.electron_variational_remesh import Model

BOX, EPS, SIG = 3.0, 0.12, 0.10


def rope_points():
    st = np.load(ROOT/'analysis'/'ELEC009_state.npz')
    model = Model(20, knots=st['knots_final'], m_energy=64)
    return np.vstack(model.curves(st['z_final'], 768))


def solve(n, beta, rope):
    x = np.linspace(-BOX, BOX, n + 2)[1:-1]; h = x[1] - x[0]
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    xyz = np.column_stack([X.ravel(), Y.ravel(), Z.ravel()])
    L = diags([-np.ones(n-1), 2*np.ones(n), -np.ones(n-1)], [-1, 0, 1], format='csr')/(h*h)
    I = eye(n, format='csr')
    H0 = kron(kron(L, I), I) + kron(kron(I, L), I) + kron(kron(I, I), L)
    r = np.linalg.norm(xyz, axis=1)
    dc = cKDTree(rope).query(xyz, k=1, workers=-1)[0]
    H = H0 + diags(-beta*np.exp(-0.5*(dc/SIG)**2), 0, format='csr')
    vals, vecs = eigsh(H, k=8, which='SA', tol=2e-7, maxiter=5000)
    o = np.argsort(vals); vals, vecs = vals[o], vecs[:, o]
    prob = vecs*vecs; prob /= prob.sum(0)
    return vals, float(np.sum(prob[r < 2.2, 0])), float(prob[:, 0] @ dc)


def test():
    rope = rope_points()
    v0, l0, d0 = solve(23, 0.0, rope)
    v4, l4, d4 = solve(23, 4.0, rope)
    v16, l16, d16 = solve(23, 16.0, rope)
    # (1) binding exists, monotone deepening
    assert v4[0] < v0[0] - 0.05, "onset by beta ~ 4 (numerical floor)"
    assert v16[0] < v0[0] - 0.3, "deep depression at beta = 16"
    # (2) the rope signature: tube-hugging trend + localization RISE
    assert d16 < d4 < d0, "probability-weighted tube distance falls monotonically"
    assert l16 > l0 + 0.1, "localization RISES with binding (the corrected B1 statement)"
    # (3) the kept convergence failure IS the registered finding
    v29, _, _ = solve(29, 16.0, rope)
    g23, g29 = np.diff(v16[:5]), np.diff(v29[:5])
    conv = float(np.max(np.abs(g29 - g23)/np.maximum(np.abs(g29), 1e-9)))
    assert conv > 0.2, "NON-CONVERGENCE registered: tube under-resolved, strength unmeasured"
    # (4) the vacuous-bar record
    assert l0 > 0.70, "the original B1 bar sits below the control baseline: vacuous, filed"
    print(f"E0: free {v0[0]:.3f} -> beta16 {v16[0]:.3f}; d_tube {d0:.3f}->{d4:.3f}->{d16:.3f}; "
          f"loc {l0:.3f}->{l16:.3f}; gap drift {conv*100:.0f}%")
    print("PASS: the rope alone BINDS (existence, with control and tube signature); the strength")
    print("      is unmeasured (kept); and the bar-setting rule violation is on the record.")


if __name__ == "__main__":
    test()
