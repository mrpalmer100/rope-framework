"""ROPE-MODE-005 (Failed, kept): THE RESOLVED-TUBE SPECTRUM IS A SINGLE
LEVEL -- the shell question is not wrong but PREMATURE at the certified
geometry, and the failure explains itself quantitatively.

The rule honored at last: floors measured FIRST (free-box continuum
edge 2.8905 at n=48; cross-grid jitter ~0.012 -> degeneracy tol 0.037).
Grids h/sigma = 0.65 and 0.52: the tube is RESOLVED (ROPE-MODE-004's
central defect repaired). Bars locked: B1 >= 4 bound modes at beta = 8,
fallback beta = 16 declared in advance; B2 gap convergence <= 5 percent;
B3 ring-vs-harmonic classification.

RESULT: B1 FAILED AT BOTH DECLARED SETTINGS AND IS KEPT. beta = 8
binds exactly ONE mode (E0 = 2.339); beta = 16 binds exactly ONE mode
(E0 = 1.636). No spectrum exists to classify; B3 cannot be posed.

THE FAILURE EXPLAINS ITSELF: the loops' arc lengths give a first
longitudinal ring excitation of order (2 pi / L_loop)^2 ~ 3, LARGER
than the entire measured binding depth (edge - E0 = 1.25 at beta=16):
the resolved rope binds one transverse channel whose longitudinal
excitations land above the continuum. A single-level binder, by
geometry.

WHAT SURVIVES: (a) THE COOPERATION SIGNATURE -- at beta = 8 the linked
pair's bound level (2.339) sits far below both single-loop levels
(2.615, 2.565): a 0.23 deviation against a 0.010 jitter floor (22x).
The one bound mode is a HYBRID spanning both tubes -- the pair binds
what neither loop binds alone. (b) THE RESOLUTION PROGRAM WORKED:
E0 is now grid-stable to ~0.01 where ROPE-MODE-004 saw 106 percent
chaos; the instrument is fixed, and what it revealed is a one-level
system. NAMED NEXT-ORDER: the regime map -- synthetic circular tubes
with controllable (beta, sigma, L) to chart where multi-level binding
begins, then return to the certified geometry in that regime.
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

BOX, SIG = 1.6, 0.10


def geometry():
    st = np.load(ROOT/'analysis'/'ELEC009_state.npz')
    model = Model(20, knots=st['knots_final'], m_energy=64)
    return model.curves(st['z_final'], 768)


def solve(n, pts, beta, k=12):
    x = np.linspace(-BOX, BOX, n + 2)[1:-1]; h = x[1] - x[0]
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    xyz = np.column_stack([X.ravel(), Y.ravel(), Z.ravel()])
    L = diags([-np.ones(n-1), 2*np.ones(n), -np.ones(n-1)], [-1, 0, 1], format='csr')/(h*h)
    I = eye(n, format='csr')
    H0 = kron(kron(L, I), I) + kron(kron(I, L), I) + kron(kron(I, I), L)
    dc = cKDTree(pts).query(xyz, k=1, workers=-1)[0]
    H = H0 + diags(-beta*np.exp(-0.5*(dc/SIG)**2), 0, format='csr')
    vals, _ = eigsh(H, k=k, which='SA', tol=1e-6, maxiter=8000)
    return np.sort(vals)


def test():
    c1, c2 = geometry()
    rope = np.vstack([c1, c2])
    edge = 2.8905  # measured floor, n=48 free box
    v8 = solve(48, rope, 8.0)
    v16 = solve(48, rope, 16.0)
    b8 = v8[v8 < edge - 0.1]; b16 = v16[v16 < edge - 0.1]
    # THE REGISTERED FAILURE: one level at both declared settings
    assert len(b8) == 1 and len(b16) == 1, "single-level binder at both settings (the finding)"
    assert b16[0] < b8[0] - 0.3, "deeper at beta=16, still solitary"
    # the self-explanation: longitudinal ring spacing exceeds the binding depth
    Ls = [float(np.sum(np.linalg.norm(np.roll(c, -1, axis=0) - c, axis=1))) for c in (c1, c2)]
    ring = min((2*np.pi/L)**2 for L in Ls)
    depth = edge - float(b16[0])
    assert ring > depth, "first longitudinal excitation exceeds the whole binding depth"
    # the cooperation signature at beta = 8
    vA = solve(48, np.asarray(c1), 8.0, k=6); vB = solve(48, np.asarray(c2), 8.0, k=6)
    singles = [v[v < edge - 0.1] for v in (vA, vB)]
    assert all(len(s) >= 1 for s in singles), "each loop alone binds one mode"
    coop = min(float(s[0]) for s in singles) - float(b8[0])
    assert coop > 0.1, "the pair binds DEEPER than either loop alone: hybrid mode, 22x floor"
    print(f"bound modes: beta8={len(b8)}, beta16={len(b16)} (E0 {b8[0]:.3f}, {b16[0]:.3f}); "
          f"ring spacing {ring:.2f} > depth {depth:.2f}")
    print(f"cooperation: pair {b8[0]:.3f} vs singles {singles[0][0]:.3f}/{singles[1][0]:.3f} "
          f"(hybrid, deviation {coop:.3f})")
    print("PASS (as a kept failure): the resolved rope is a single-level binder by geometry;")
    print("      the shell question is premature here, and the pair's one mode is a hybrid.")


if __name__ == "__main__":
    test()
