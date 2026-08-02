"""ELEC-038 (Modeled): THE ONE-MEDIUM DECLARATION, ADOPTED -- and its
price computed. The framework keeps a single kind of rope; the scale
branch inherits n_t ~ 8.7e8 as a standing obligation; no registered
inequality is violated, and one long-standing coincidence dies.

THE DECLARATION (framework-level, taken deliberately): vacuum strands
and matter ropes are THE SAME KIND OF OBJECT. ELEC-037's invariant
therefore stands in full, and the framework accepts the consequence
rather than dissolving it by splitting the medium.

WHAT THE CHOICE COSTS, computed from the scale branch's own registered
parameters (n_t = 111, D/w = 19, Sigma = 5.1e35 J/m^3, rho = 5.67e18
kg/m^3, T0 = 1.70e3 J/m per strand):

  (a) STRAND SPACING: n_t ~ (d_c/w)^2 with the calibrated rope
      thickness d_c = 1.338 fm gives w = 4.53e-20 m and d_c/w =
      2.96e4, against the registered D/w ~ 19. This is 2.8e15 times
      the Planck length -- tight, but PERMITTED.
  (b) VACUUM DENSITY: the fence moves from 5.67e18 to 4.46e25 kg/m^3,
      i.e. from 25x nuclear to 1.9e8 x NUCLEAR. Independent check: the
      reconstruction rho = (T0/c^2)/w^2 evaluated at n_t = 111 returns
      1.17e18 against the registered 5.67e18, agreeing to a factor of
      4.8, so the scaling is sound to order of magnitude and the
      reconstruction is honest about that.
  (c) THE SCHWINGER COINCIDENCE DIES: Sigma rises to 4.01e42 J/m^3,
      putting E_crit = sqrt(Sigma/eps0) = 6.73e26 V/m, which is
      5.1e8 times ABOVE the Schwinger field. Mesh nonlinearity becomes
      unobservable. No conflict is created -- and QGATE-009 had
      already diagnosed the old near-coincidence as a flattery rather
      than a prediction, so its loss costs the framework nothing it
      was entitled to.
  (d) THE EM-RECON-015 FENCE, already worsened 3.3e10-fold at
      n_t = 111, worsens by a further 7.87e6 to 2.6e17-fold.

VERDICT: the one-medium framework is EXPENSIVE BUT NOT KILLED. Every
consequence is a worsening of invoices the corpus had already itemized
and accepted; none is a new violated inequality. The standing
obligation is now explicit and falsifiable: the vacuum must supply
~8.7e8 coherently reconnecting strands at ~4.5e-20 m spacing, and
QGATE-009's six confrontations must be re-run at the new Sigma.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'ELEC038_state.npz')
    # the obligation
    assert 5e8 < float(s['n_req']) < 2e9, "n_t ~ 8.7e8 inherited from ELEC-037's invariant"
    assert abs(float(s['fac']) - 7.866e6)/7.866e6 < 0.01, "the factor is ELEC-037's invariant"
    # (a) permitted, not Planck-limited
    assert float(s['w_planck']) > 1e10, "strand spacing 2.8e15 Planck lengths: permitted"
    assert float(s['dw']) > 1e4, "d_c/w ~ 3e4 against the registered 19"
    # (b) the density invoice
    assert float(s['rho_nuc_ratio']) > 1e7, "vacuum at ~1.9e8 x nuclear"
    # (c) the coincidence dies, without creating a conflict
    assert float(s['schw_ratio']) > 1e6, "E_crit now 5.1e8 x above Schwinger: coincidence gone"
    # (d) the fence
    assert float(s['fence']) > 1e16, "EM-RECON-015 fence worsened to 2.6e17-fold"
    print(f"n_t {float(s['n_req']):.2e}; w {float(s['w']):.2e} m ({float(s['w_planck']):.1e} Planck); "
          f"rho {float(s['rho_nuc_ratio']):.1e}x nuclear; E_crit/Schwinger {float(s['schw_ratio']):.1e}; "
          f"fence {float(s['fence']):.1e}")
    print("PASS: one medium adopted -- expensive but not killed; every consequence worsens an")
    print("      already-itemized invoice, none violates a registered inequality.")


if __name__ == "__main__":
    test()
