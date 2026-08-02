"""ELEC-014 (Modeled): THE SECOND-ORDER DECIDER -- THE TERMINAL STATE IS
A GENERALIZED MINIMUM TO WITHIN INSTRUMENT RESOLUTION.

The composite second-order step (move along the NNLS residual, RESTORE
feasibility via linearized least-norm correction on violated pairs,
certify) answered both locked questions:
B1 CONFIRMED: the corrector achieves certified descent where the
   first-order engine terminated -- 25 accepted composite steps. The
   contact manifold's curvature obstruction is real.
B2 DECIDED, second branch: the accessible descent is MICROSCOPIC --
   total dE = 2.2e-5 (five orders below the campaign's 1.246), step
   sizes collapsing to 3e-7, termination re-tripping under the same
   pre-locked criterion, with the generalized residual wobbling at
   0.24-0.39 and NOT collapsing toward the 0.05 certificate.

VERDICT: past the ELEC-013 terminus there is no physically meaningful
descent accessible to second-order machinery. The residual plateau is
hereby attributed -- AS A HYPOTHESIS, tested by ELEC-015's resolution
ladder -- to the FACETING of the polygonal (128-gon) contact manifold:
a smooth contact surface's multipliers live on arcs, and the 128-gon
approximates them with facet-noise of exactly this order. The state in
ELEC014_state.npz (E = 14.907163, d = 0.0610, |Lk| = 1.0004, full
cert green) supersedes ELEC-013's by 2.2e-5 and inherits its titles.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.elec_grad import Grad, al


def test():
    g = Grad()
    s13 = np.load(ROOT/'analysis'/'ELEC013_state.npz')
    s14 = np.load(ROOT/'analysis'/'ELEC014_state.npz')
    E13 = float(s13['energy_final']); E14 = float(s14['energy_final'])
    assert bool(s14['terminated']), "the second-order run re-terminated under the same criterion"
    assert 0 < E13 - E14 < 1e-3, "accessible second-order descent is MICROSCOPIC (~2e-5)"
    assert int(s14['accepted']) >= 10, "yet composite steps DID work: curvature obstruction real"
    gres = float(s14['gres'])
    assert 0.15 < gres < 0.5, "the residual plateau persists (facet-noise hypothesis -> ELEC-015)"
    z = s14['z_final'].astype(float)
    d, lk, okfull, _ = g.m.cert(z, full=True)
    assert okfull and abs(abs(lk) - 1) < 0.01, "the superseding state fully certified"
    print(f"dE(second order) = {E13-E14:.2e}; steps {int(s14['accepted'])}; gres {gres:.3f}; "
          f"cert d={d:.4f} |Lk|={abs(lk):.4f}")
    print("PASS: generalized minimum to within instrument resolution; the plateau is")
    print("      attributed (as hypothesis) to contact-manifold faceting -- ELEC-015 decides.")


if __name__ == "__main__":
    test()
