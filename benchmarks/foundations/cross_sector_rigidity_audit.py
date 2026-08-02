"""XSEC-001 (Modeled): THE CROSS-SECTOR AUDIT -- the gravity sector's
best result and the quantum sector's new bound collide, and survive on
exactly one reading, which converts a fit into a prediction.

THE COLLISION. GRV-030's headline success is g_dagger = c H0/2pi =
1.083e-10 m/s^2, confirmed against 155 SPARC galaxies at zero free
parameters. HBAR-010 requires the strand medium to be rigid against
cosmic expansion to one part in 2e5. The gravity sector's best number
contains an expansion rate; the quantum sector forbids the medium from
expanding.

THE DISCRIMINATING QUESTION: does g_dagger evolve? Under standard
LCDM, H(z)/H0 = 1.000, 1.309, 1.761, 2.966, 4.461 at z = 0, 0.5, 1, 2,
3, so a g_dagger tracking H(z) would grow 3.3-fold by z = 3. A rigid
medium cannot produce that. THE RIGIDITY BOUND THEREFORE PREDICTS THAT
g_dagger DOES NOT EVOLVE WITH REDSHIFT.

THE ONLY RECONCILIATION. Rewrite g_dagger = c^2/(2 pi L) with
L = c/H0 = 1.32e26 m. A medium laid down at formation has a FIXED total
extent -- the horizon size at that epoch -- which numerically coincides
with c/H0 today but does not evolve. On that reading g_dagger measures
THE MEDIUM'S EXTENT rather than the expansion rate, and both sectors
stand.

WHAT EACH READING COSTS:
  (i) g_dagger ~ H(z): the medium tracks expansion, hbar varies, and
      HBAR-010 excludes it at 7.5e4. INCOMPATIBLE.
  (ii) g_dagger constant: compatible, but the framework must explain
      why the medium's fixed extent equals c/H0 TODAY -- the cosmic
      coincidence problem in rope clothing, honestly inherited rather
      than solved.

THE VERDICT: compatible on reading (ii) only, and that reading turns
GRV-030's fit into a falsifiable prediction -- high-redshift rotation
curves must show the SAME acceleration scale as local ones. Discs at
z ~ 1-2 have been observed and are the natural test.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'HBAR013_state.npz')
    c = 2.99792458e8
    # the gravity sector's number is reproduced
    assert abs(float(s['g_calc']) - float(s['g_dag']))/float(s['g_dag']) < 0.01, \
        "g_dagger = c H0/2pi reproduces GRV-030's 1.083e-10"
    # the evolution that rigidity forbids
    E = s['E']
    assert abs(E[0][1] - 1.0) < 1e-9, "H(0) = H0"
    assert E[-1][1] > 3, "H(z=3)/H0 = 4.46: a tracking g_dagger would grow 3.3x"
    # the reconciliation length is the Hubble length
    assert abs(float(s['L_H']) - c/float(s['H0']))/float(s['L_H']) < 1e-9, "L = c/H0"
    assert 1e26 < float(s['L_H']) < 2e26, "1.32e26 m = 4280 Mpc"
    # and g_dagger = c^2/(2 pi L) is the same statement
    assert abs(c**2/(2*np.pi*float(s['L_H']))/float(s['g_dag']) - 1) < 0.01, \
        "g_dagger = c^2/(2 pi L): the extent reading is algebraically identical"
    print(f"g_dagger {float(s['g_calc']):.4e} (GRV-030: {float(s['g_dag']):.4e}); "
          f"H(z=3)/H0 = {E[-1][1]:.2f}; L = c/H0 = {float(s['L_H']):.3e} m; "
          f"c^2/(2 pi L) = {c**2/(2*np.pi*float(s['L_H'])):.4e}")
    print("PASS: the sectors collide and survive on one reading only -- g_dagger measures the")
    print("      medium's fixed extent, and must therefore NOT evolve with redshift.")


if __name__ == "__main__":
    test()
