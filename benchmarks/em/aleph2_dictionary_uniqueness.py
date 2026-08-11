#!/usr/bin/env python3
"""COMMISSION ALEPH-2 -- EM-016 blocker (iv): uniqueness of the dictionary.

Bars: analysis/ALEPH2_dictionary_uniqueness_bars_LOCKED.md.
Registered inputs only: q = winding (integer, Z, no monopoles),
E = force per winding, Lorentz force q(E + v x B).

S1: velocity-separation -- do forces at finitely many velocities
    determine (E, B) pointwise? (Constructive, not asserted.)
S2: duality -- is the E/B rotation a symmetry of the observables?
    (Checked, not assumed.)
"""
import numpy as np
import sympy as sp

rng = np.random.default_rng(16)

print("=" * 70)
print("S1 -- VELOCITY SEPARATION: is (E, B) recoverable from forces?")
print("=" * 70)
# Ground-truth fields at a point (arbitrary; the test is the inversion)
E = np.array([0.7, -1.3, 2.1])
B = np.array([-0.4, 0.9, 0.25])
def force(q, v):            # EM-013's registered law
    return q * (E + np.cross(v, B))

# Four measurements suffice: one static (v=0) gives E directly; three
# with independent velocities give B by inverting the cross product.
q = 1.0
E_rec = force(q, np.zeros(3)) / q
print(f"   static probe (v=0) -> E recovered exactly: {np.allclose(E_rec, E)}")

V = np.eye(3)                                   # three independent velocities
M = np.zeros((9, 3)); y = np.zeros(9)
for i, v in enumerate(V):
    # F/q - E = v x B = [v]_x B ; build the 3x3 cross-product matrix
    vx = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    M[3*i:3*i+3] = vx
    y[3*i:3*i+3] = force(q, v) / q - E_rec
B_rec, *_ = np.linalg.lstsq(M, y, rcond=None)
print(f"   three moving probes -> B recovered exactly: {np.allclose(B_rec, B)}")
print(f"   residual |B_rec - B| = {np.linalg.norm(B_rec - B):.2e}")
print("   => (E, B) are pointwise DETERMINED by forces on test windings.")
print("      No velocity-degeneracy exists. Any two assignments agreeing on")
print("      all forces agree on (E, B) pointwise, hence on F_munu, hence")
print("      on the potentials up to gauge (Poincare, EM-003's dF = 0).")

print()
print("=" * 70)
print("S2 -- DUALITY: is the E/B rotation an unobservable freedom?")
print("=" * 70)
t = sp.symbols("theta", real=True)
Ex, Bx, vy, vz, qq = sp.symbols("E_x B_x v_y v_z q", real=True)
# Rotated fields
E2 = sp.Matrix([Ex, 0, 0]) * sp.cos(t) + sp.Matrix([Bx, 0, 0]) * sp.sin(t)
B2 = sp.Matrix([Bx, 0, 0]) * sp.cos(t) - sp.Matrix([Ex, 0, 0]) * sp.sin(t)
v = sp.Matrix([0, vy, 0])
F_orig = qq * (sp.Matrix([Ex, 0, 0]) + v.cross(sp.Matrix([Bx, 0, 0])))
F_rot = qq * (E2 + v.cross(B2))
diff = sp.simplify(F_rot - F_orig)
print("   force difference under duality rotation:")
sp.pprint(sp.simplify(diff.T))
print("\n   Non-zero for theta != 0 (e.g. the static piece q E_x picks up")
print("   q(E_x cos t + B_x sin t) != q E_x).")
print("   THE REGISTERED FACT THAT BREAKS DUALITY: charge is WINDING")
print("   (GG-006/EM-001) and windings are the ONLY registered charge --")
print("   the corpus has no magnetic monopole. A duality rotation maps")
print("   electric sources into magnetic ones, which the registry cannot")
print("   represent. So the rotation is not available, and the static")
print("   force above already detects it in any case.")

print()
print("=" * 70)
print("CONCLUSION")
print("=" * 70)
print("   Any mechanical assignment predicting the same forces on all test")
print("   windings at all velocities yields the SAME (E, B) pointwise, and")
print("   hence the same F_munu; potentials follow up to gauge. The only")
print("   surviving freedom is the global calibration constant already")
print("   registered as an input (SIGMA, blocker (i)).")
print("   => Blocker (iv) DISCHARGED. Blockers (i), (ii), (iii) STAND.")
