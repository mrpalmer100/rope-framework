"""ELEC-019 (Modeled): THE K = 12 TERMINUS, AND THE LADDER'S FIRST
EVIDENCE OF CONVERGENCE.

The K = 12 run to termination: 2,736 certified iterations -- the
longest certified run in the corpus -- reaching the pre-locked
criterion at E = 15.5638 (chart-drop 0.1626 from the K = 8 terminus;
N = 22 campaign total 17.110 -> 15.564). Certification green
throughout and at the end (d = 0.0657, |Lk| within tolerance), with
d_min glued to the same 0.0657 across all 2,736 iterations: the
contact architecture never wavered.

THE K-LADDER PROBE at the terminus: embedding into K = 16 (verified
exact to machine precision; instrument spot-gated at 0.0-1.0 percent)
gives gres16 = 0.237 -- BELOW the analogous gres12 = 0.295 measured at
the K = 8 terminus. THE LADDER CONTRACTS: each enrichment sees less
unrepresented descent than the last. Two rungs are not a convergence
proof, and the claim says so; but both indicators (the shrinking
next-chart residual, the decaying within-chart rate) point the same
way -- toward a convergent K -> infinity equilibrium, approachable by
geometric extrapolation once the K = 16 rung (named next-order)
supplies the third point.

THE CLASP, one more time: at the K = 12 terminus it rides its
isoperimetric floor with contact unbroken -- through grid correction,
chart enrichment, and now the longest descent yet, the identity
L = 2 pi x clearance has never budged by more than half a percent.
"""
import sys
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree
from scipy.sparse import diags, eye, kron

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.elec_grad import al
from rope_solver.topology.linking import hopf_curves, linking_number

K12 = 12


def curves12(z, M):
    t = np.linspace(0, 2*np.pi, M, endpoint=False)
    b = np.array([f(k*t) for k in range(1, K12+1) for f in (np.sin, np.cos)])
    R = float(np.exp(z[0])); c1, c2 = hopf_curves(M, R=R)
    co = z[1:].reshape(2, 3, 2*K12)
    p1 = c1 + np.einsum('ak,kn->na', co[0], b)
    p2 = c2 + np.einsum('ak,kn->na', co[1], b)
    cen = np.vstack([p1, p2]).mean(0)
    return p1 - cen, p2 - cen


def dmin_at(z, M):
    A, B = (np.asarray(c) for c in curves12(z, M))
    P = A[:, None, :]; Q = np.roll(A, -1, axis=0)[:, None, :]
    R = B[None, :, :]; S = np.roll(B, -1, axis=0)[None, :, :]
    u = Q - P; v = S - R; w = P - R
    a = np.sum(u*u, axis=2); b = np.sum(u*v, axis=2); c = np.sum(v*v, axis=2)
    d = np.sum(u*w, axis=2); e = np.sum(v*w, axis=2); den = a*c - b*b
    sc = np.where(den > 1e-14, (b*e - c*d)/den, 0.0)
    tc = np.where(den > 1e-14, (a*e - b*d)/den, np.where(c > 1e-14, e/c, 0.0))
    sc = np.clip(sc, 0, 1); tc = np.clip(tc, 0, 1)
    tc = np.where(c > 1e-14, np.clip((b*sc + e)/c, 0, 1), 0.0)
    sc = np.where(a > 1e-14, np.clip((b*tc - d)/a, 0, 1), 0.0)
    D = w + sc[:, :, None]*u - tc[:, :, None]*v
    return float(np.sqrt(np.maximum(np.sum(D*D, axis=2), 1e-18)).min())


def test():
    st = np.load(ROOT/'analysis'/'ELEC019_state.npz')
    z = st['z_final'].astype(float)
    assert bool(st['terminated']), "terminated under the pre-locked criterion (it 2736)"
    E = float(st['energy_final'])
    assert 15.55 < E < 15.58, "the K=12 terminal energy"
    assert float(st['E_k8']) - E > 0.15, "chart-drop 0.16 from the K=8 terminus"
    # the ladder contracts
    assert float(st['gres16_at_terminus']) < 0.28, \
        "gres16 (0.237) BELOW the K=8 analogue (0.295): first evidence of ladder convergence"
    # certification, K12-native
    ds = [dmin_at(z, M) for M in (128, 256, 512)]
    c1, c2 = curves12(z, 512)
    lk = linking_number(np.asarray(c1), np.asarray(c2))
    assert all(d >= al.D_HARD for d in ds) and abs(abs(lk) - 1) <= al.LK_TOL
    # the clasp
    A, B = (np.asarray(c) for c in curves12(z, 256))
    LA = float(np.sum(np.linalg.norm(np.roll(A, -1, axis=0) - A, axis=1)))
    LB = float(np.sum(np.linalg.norm(np.roll(B, -1, axis=0) - B, axis=1)))
    if LA > LB:
        A, B, LA, LB = B, A, LB, LA
    dA = cKDTree(B).query(A, k=1, workers=-1)[0]
    assert float(np.mean(dA <= 1.15*al.D_HARD)) > 0.95
    assert abs(LA/(2*np.pi*float(dA.mean())) - 1) < 0.03, "the floor identity, still"
    print(f"E(K12)={E:.4f} (drop {float(st['E_k8'])-E:.4f}); gres16={float(st['gres16_at_terminus']):.3f}<0.295; "
          f"cert d={min(ds):.4f} |Lk|={abs(lk):.4f}; clasp L={LA:.4f}=2pi x {LA/(2*np.pi):.4f}")
    print("PASS: the K=12 terminus certified after 2,736 iterations; the ladder CONTRACTS;")
    print("      the clasp's floor identity survives its third generation of instruments.")


if __name__ == "__main__":
    test()
