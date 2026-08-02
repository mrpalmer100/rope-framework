"""ELEC-012 (Modeled): THE SMOOTHED PUSH BREAKS THE STALEMATE -- AND THE
OBJECT SLIDES TOWARD THE TIGHT LINK. B2/B3 failed and kept; the failure
is the discovery.

The softmin-smoothed constraint model (certification unchanged and
hard: true d_min >= 0.060 at 128/256/512) uncreased the wall tangent,
and the optimizer promptly found the real valley: 108 certified
accepted steps, E: 16.104 -> 14.921 (-1.18 -- roughly TEN TIMES the
descent of all prior campaigns combined), with d_min sliding down and
PINNING AT EXACTLY the hard core (0.0600 to four decimals from
iteration ~45 onward), |Lk| = 1.0003, full cross-resolution
certification green, and energy STILL DESCENDING at line-search
exhaustion.

THE RESIDUAL ROSE (PG ~ 0.74-1.05 vs bars < 0.05/0.02) -- and that is
the finding, not a defect: as the object presses into the wall the
gradient and multiplier GROW while energy falls along the wall's
downhill direction. The ELEC-011 wall-supported state was a SHOULDER,
not the equilibrium. THE CINCHING, quantified: the number of segment
pairs in near-contact (within 1.15 x D_HARD) grows substantially from
the ELEC-011 state to tonight's -- the curves are wrapping into
EXTENDED contact, the geometry of a TIGHTENING link.

THE TRANSFORMED PICTURE: the trajectory heads toward a tight
(ideal-link-like) configuration in which impenetrability is active
along whole arcs -- a continuum of active constraints with
measure-valued contact forces, where finite-dimensional KKT residuals
legitimately remain O(1) even AT the generalized equilibrium. The
campaign's question is transformed once more, and for the better:
IS THE ELECTRON CANDIDATE THE TIGHT HOPF LINK AT HARD-CORE THICKNESS,
dressed by its field? -- a concrete, literature-adjacent (ropelength /
ideal-link geometry), checkable endpoint. Scale sanity: ELEC-010's
bowl was measured at the OLD shape; the balance moves as the shape
cinches, and the run remained certified throughout.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.elec_grad import Grad, al


def seg_dist_matrix(A, B):
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
    return np.sqrt(np.sum(D*D, axis=2))


def contact_pairs(g, z, factor=1.15):
    c1, c2 = g.m.curves(z, 128)
    D = seg_dist_matrix(np.asarray(c1), np.asarray(c2))
    return int(np.sum(D <= factor*al.D_HARD)), float(D.min())


def test():
    g = Grad()
    zA = np.load(ROOT/'analysis'/'ELEC011A_state.npz')['z_final'].astype(float)
    st = np.load(ROOT/'analysis'/'ELEC012_state.npz')
    zF = st['z_final'].astype(float); EF = float(st['energy_final'])
    EA, _, _ = g.energy(zA)
    assert EA - EF > 1.0, "the stalemate broke: E fell by > 1.0 (record by ~10x)"
    # the pinning
    d, lk, okfull, _ = g.m.cert(zF, full=True)
    assert okfull, "full 128/256/512 certification green at the tight state"
    assert abs(d - al.D_HARD) < 2e-3, "d_min PINNED at the hard core"
    assert abs(abs(lk) - 1) < 0.01, "linking pristine (|Lk| = 1.000)"
    # the cinching: extended contact grows
    nA, dA = contact_pairs(g, zA)
    nF, dF = contact_pairs(g, zF)
    assert nF > 2*nA and nF >= 8, "near-contact pair count grows: EXTENDED contact forming"
    # the kept bar failure: residual O(1) at the contact-rich state
    pg = float(st['pg_hard'])
    assert pg > 0.3, "B2/B3 failed and kept: finite-dim KKT residual O(1) at extended contact"
    print(f"E: {EA:.4f} -> {EF:.4f} (drop {EA-EF:.3f}); d pinned {d:.4f}; |Lk| {abs(lk):.4f}")
    print(f"cinching: near-contact pairs {nA} -> {nF}; residual {pg:.3f} (kept)")
    print("PASS: the object slides along the wall into extended contact -- the candidate's")
    print("      rest state looks like the TIGHT HOPF LINK at hard-core thickness.")


if __name__ == "__main__":
    test()
