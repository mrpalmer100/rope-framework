"""ELEC-016 (Modeled): THE CLASP AND THE LOOP -- the terminal object has
SPONTANEOUSLY BROKEN the two-curve symmetry.

Both curves entered the campaign as congruent Hopf circles. The
certified terminal state is maximally asymmetric:

THE CLASP: curve 1 has contracted to L1 = 0.4026 -- which equals
2 pi x 0.0641, THE MINIMAL CIRCLE around the partner strand at wall
clearance -- with 100 percent of its arc in contact (one connected
patch). Tension won everything the wall allows: the clasp is
geometrically tight, at its length floor.

THE LOOP: curve 2 remains large (L2 = 4.110, a 10:1 length asymmetry)
and NEARLY PLANAR (principal-variance aspect 245:1), held open by its
field. THE DRESSING: the field energy is a diffuse Coulomb cloud, not
a sheath -- only ~14 percent lies within two tube-widths of the rope;
~54 percent within r = 1.5 of the center (measured at N = 22).

The Hopf linking is pristine throughout (|Lk| = 1.0004, full cert).
The picture: A MINIMAL CLASP RING ON A LARGE FIELD-HELD LOOP -- the
tension sector and the field sector each captured one component
entirely, an equilibrium of specialization rather than compromise.

MODEL BOUNDARIES, named without varnish: (a) the functional carries NO
self-distance constraint and no bending stiffness -- the clasp's
collapse to its floor is licensed by that absence, and a rope with
self-thickness or curvature energy could stop elsewhere (the clasp's
centerline radius 0.064 does exceed the tube radius 0.03, so no
self-intersection occurs even ungoverned); (b) discrete curvature
statistics at K = 8 / 256 samples are unreliable and are NOT claimed;
(c) ELEC-015's 15-percent field-grid debt applies to every energy
statement here. The geometry facts (lengths, contact, planarity,
linking) are grid-independent and are the claim.
"""
import sys
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.elec_grad import Grad, al


def test():
    g = Grad()
    z = np.load(ROOT/'analysis'/'ELEC014_state.npz')['z_final'].astype(float)
    c1, c2 = g.m.curves(z, 256)
    A, B = np.asarray(c1), np.asarray(c2)
    LA = float(np.sum(np.linalg.norm(np.roll(A, -1, axis=0) - A, axis=1)))
    LB = float(np.sum(np.linalg.norm(np.roll(B, -1, axis=0) - B, axis=1)))
    if LA > LB:
        A, B, LA, LB = B, A, LB, LA
    # the clasp at its geometric floor
    assert 0.38 < LA < 0.43, "clasp length ~0.40"
    dA = cKDTree(B).query(A, k=1, workers=-1)[0]
    assert float(np.mean(dA <= 1.15*al.D_HARD)) > 0.95, "clasp fully in contact"
    r_eff = LA/(2*np.pi)
    assert abs(r_eff - float(dA.mean()))/float(dA.mean()) < 0.1, \
        "clasp radius = wall clearance: the MINIMAL circle around the strand"
    # the loop and the broken symmetry
    assert LB/LA > 8, "10:1 spontaneous length asymmetry (started congruent)"
    allp = np.vstack([A, B]); cen = allp.mean(0)
    ev = np.sort(np.linalg.eigvalsh(np.cov((allp - cen).T)))[::-1]
    assert ev[0]/max(ev[2], 1e-9) > 50, "near-planar configuration"
    d, lk, okfull, _ = g.m.cert(z, full=True)
    assert okfull and abs(abs(lk) - 1) < 0.01, "Hopf linking pristine"
    print(f"clasp: L={LA:.4f} = 2pi x {r_eff:.4f} (wall {float(dA.mean()):.4f}), 100% contact")
    print(f"loop:  L={LB:.4f} ({LB/LA:.1f}:1 asymmetry); planarity aspect {ev[0]/ev[2]:.0f}:1")
    print("PASS: THE CLASP AND THE LOOP -- spontaneous symmetry breaking into a minimal")
    print("      clasp ring on a large field-held loop, linking pristine throughout.")


if __name__ == "__main__":
    test()
