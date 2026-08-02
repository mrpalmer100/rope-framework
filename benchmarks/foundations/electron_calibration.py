"""ELEC-021 (Modeled): THE CALIBRATION -- WHAT 15.5627 BECOMES, AND THE
TWO CONFRONTATIONS IT BUYS.

THE INVARIANT (calibration-independent): Lambda = E_inf d_c / kappa =
0.4669, plus the geometry ratios (16.4:1, the clasp's 2 pi floor, the
46.3/53.7 partition). These survive any choice of units.

THE CALIBRATION (two anchors: kappa -> alpha hbar c, E_inf -> m_e c^2;
everything else becomes a prediction):
  energy unit 32.835 keV; length unit 21.93 fm
  ROPE THICKNESS d_c = 1.316 fm = 0.467 x classical electron radius
  charge-cloud width 5.26 fm (the model's second microlength, ratio 4)
  TENSION T0 = 1.50 keV/fm = 0.240 newtons
  clasp 9.1 fm around; loop 149 fm; object diameter ~ 36 fm
  MASS PARTITION: 46.3 percent tension (mass as rope length) + 53.7
  percent electrostatic -- the Abraham-Lorentz question answered by
  measurement inside the model: neither pure.
  Dominant uncertainty: the N-grid systematic (~2-3 percent); the
  ladder bar (12e-4) is negligible against it.

CONFRONTATION I -- THE FORM FACTOR PROBLEM (kept, primary): a ~36 fm
geometric object versus scattering bounds on electron structure below
~1e-3 fm: five orders. The rope ontology's defense (probes are
excitations of the same medium and may not see the geometric loop) is
NAMED AND UNEARNED. Registered as the matter sector's primary standing
obstacle.

CONFRONTATION II -- THE CROSS-SECTOR CLASH (kept): the scale branch's
hbar normalization (W = 1.80 T D^2/c, collective n_t ~ 111) evaluated
at the electron calibration gives 2.6e-3 x hbar: ~381x short. Either
vacuum strands and matter ropes are DIFFERENT OBJECTS with different
(T, D) -- a claim the framework must now make explicitly or retract --
or the two independently calibrated sectors disagree. First
inter-sector confrontation in the corpus's history.

FLAGGED COINCIDENCE (named, not leaned on, per the Schwinger-seduction
rule): the collective reconciling thickness (25.7 fm) sits within 8
percent of the electron loop's radius (23.7 fm).

NOT DELIVERED, so no one is fooled: spin one-half, the magnetic moment
and g-factor, charge quantization, m_p/m_e. The energy became a mass
by assumption. Those remain on the wall.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.elec_grad import al
from rope_solver.geometry.curve import tension_energy
from rope_solver.topology.linking import hopf_curves

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
    z = st['z_final'].astype(float); E = float(st['energy_final'])
    cs = curves16(z, al.M_ENERGY)
    ET = float(sum(tension_energy(c, al.T0) for c in cs)); EF = E - ET
    # the invariant and partition
    Lam = E*al.D_HARD/al.KAPPA
    assert 0.45 < Lam < 0.48, "Lambda = E d_c/kappa = 0.467"
    assert 0.44 < ET/E < 0.49, "mass partition ~46% tension / ~54% electrostatic"
    # the calibration
    alpha = 1/137.035999; hbarc = 197.3269804; me = 0.51099895
    E0 = me/E; L0 = (alpha*hbarc/al.KAPPA)/E0
    d_c = al.D_HARD*L0; r_e = hbarc*alpha/me
    assert 0.44 < d_c/r_e < 0.49, "rope thickness = 0.467 classical electron radii (1.32 fm)"
    T0_N = (E0/L0)*1e6*1.602176634e-19/1e-15
    assert 0.22 < T0_N < 0.26, "tension = 0.24 newtons"
    c1, c2 = curves16(z, 256)
    Ls = sorted(float(np.sum(np.linalg.norm(np.roll(np.asarray(c), -1, axis=0) - np.asarray(c), axis=1))) for c in (c1, c2))
    assert 30 < 2*0.8244*L0 < 42, "object diameter ~36 fm"
    # confrontation II numbers
    hbar = 1.054571817e-34; c_ = 2.99792458e8
    W111 = 111*1.80*T0_N*(d_c*1e-15)**2/c_
    short = hbar/W111
    assert 250 < short < 550, "cross-sector clash: ~381x short of hbar (collective)"
    D_rec = np.sqrt(hbar*c_/(1.80*T0_N))/np.sqrt(111)*1e15
    loop_r = Ls[1]*L0/(2*np.pi)
    assert 0.85 < D_rec/loop_r < 1.3, "the flagged coincidence: reconciling D ~ loop radius (8%)"
    print(f"Lambda={Lam:.4f}; d_c={d_c:.3f} fm ({d_c/r_e:.3f} r_e); T0={T0_N:.3f} N; "
          f"partition {ET/E*100:.1f}/{EF/E*100:.1f}; diameter {2*0.8244*L0:.0f} fm")
    print(f"clash: {short:.0f}x short; coincidence D_rec/loop_r = {D_rec/loop_r:.2f} (flagged)")
    print("PASS: the calibration executed; both confrontations registered as kept obstacles;")
    print("      the not-delivered list stated so no one is fooled.")


if __name__ == "__main__":
    test()
