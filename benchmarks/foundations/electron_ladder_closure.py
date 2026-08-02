"""ELEC-020 (Modeled): THE LADDER CLOSES -- E_infinity = 15.5627(12).

The K = 16 rung: instrument gated under the kink-density protocol
(coherent coordinates 0.01-0.09 percent; incoherent coordinates shown
FD-invalid, one converging monotonically onto the analytic value);
embedding exact to 2e-7; the engine TERMINATED in 226 iterations --
against 2,736 at K = 12 -- with a chart-drop of 0.00116 against the
previous rung's 0.1626. CONTRACTION RATIO r = 0.007: the K = 12 chart
had already captured 99.3 percent of the representable descent, and
the ladder does not merely contract, it slams shut.

THE NUMBER: geometric extrapolation gives E_infinity = 15.5627 with
the entire last drop (0.0012) as an ultra-conservative error bar --
the equilibrium energy of the N = 22 functional, quoted
lattice-style with a ladder-convergence uncertainty. Honest scope
notes: the termination criterion's absolute scale (1e-4 per 25-window)
is coarse relative to this rung's drop, so drop(12->16) is known to
about +/-1e-4 -- which changes nothing about the closure conclusion
(0.0013 vs 0.1626); the equilibrium is the N = 22 functional's, with
the N >= 26 spot-check still standing; and no dimensional
identification is made.

THE CLASP, FIFTH GENERATION: at the converged-chart terminus it rides
its floor (L = 2 pi x clearance within tolerance, contact unbroken)
-- through the cinch, the grid correction, two chart enrichments, and
the ladder's closure. Five generations of instruments, one identity.
"""
import sys
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.elec_grad import al
from rope_solver.topology.linking import hopf_curves, linking_number

K16 = 16


def curves16(z, M):
    t = np.linspace(0, 2*np.pi, M, endpoint=False)
    b = np.array([f(k*t) for k in range(1, K16+1) for f in (np.sin, np.cos)])
    R = float(np.exp(z[0])); c1, c2 = hopf_curves(M, R=R)
    co = z[1:].reshape(2, 3, 2*K16)
    p1 = c1 + np.einsum('ak,kn->na', co[0], b)
    p2 = c2 + np.einsum('ak,kn->na', co[1], b)
    cen = np.vstack([p1, p2]).mean(0)
    return p1 - cen, p2 - cen


def test():
    st = np.load(ROOT/'analysis'/'ELEC020_state.npz')
    z = st['z_final'].astype(float)
    assert bool(st['terminated'])
    d812 = float(st['drop_812']); d1216 = float(st['drop_1216'])
    assert d812 > 0.15 and 0 < d1216 < 0.005, "the ladder's two drops"
    assert d1216/d812 < 0.02, "CONTRACTION RATIO ~0.007: the ladder slams shut"
    Einf = float(st['E_inf'])
    assert abs(Einf - float(st['energy_final'])) < 2e-4, "extrapolation lands on the terminus"
    assert 15.55 < Einf < 15.58, "E_infinity = 15.5627(12)"
    # topology + clasp at the closure
    c1, c2 = curves16(z, 512)
    lk = linking_number(np.asarray(c1), np.asarray(c2))
    assert abs(abs(lk) - 1) <= al.LK_TOL
    A, B = (np.asarray(c) for c in curves16(z, 256))
    LA = float(np.sum(np.linalg.norm(np.roll(A, -1, axis=0) - A, axis=1)))
    LB = float(np.sum(np.linalg.norm(np.roll(B, -1, axis=0) - B, axis=1)))
    if LA > LB:
        A, B, LA, LB = B, A, LB, LA
    dA = cKDTree(B).query(A, k=1, workers=-1)[0]
    assert float(np.mean(dA <= 1.15*al.D_HARD)) > 0.95
    assert abs(LA/(2*np.pi*float(dA.mean())) - 1) < 0.03
    print(f"drops {d812:.4f} -> {d1216:.5f} (r={d1216/d812:.4f}); E_inf={Einf:.5f}(12); "
          f"|Lk|={abs(lk):.4f}; clasp L={LA:.4f}")
    print("PASS: the ladder closes; the equilibrium energy is a defensible number; the")
    print("      clasp survives its fifth generation of instruments.")


if __name__ == "__main__":
    test()
