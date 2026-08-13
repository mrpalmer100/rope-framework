#!/usr/bin/env python3
"""COMMISSION NUN-2 -- does the three-family weave break rotational symmetry?

Bars: analysis/NUN2_rotational_symmetry_bars_LOCKED.md.
N1 point group; N2 lowest allowed anisotropy; N3 the dynamical average.
Symmetry only -- no coupling model, no fitted normalization.
"""
import numpy as np
import sympy as sp

print("=" * 70)
print("N1 -- THE POINT GROUP OF THE REGISTERED WEAVE")
print("=" * 70)
print("Three strand families along x, y, z at spacing a (EM-RECON-025,")
print("FND-038/040). The set of directions {x, y, z} is invariant under")
print("the octahedral group O_h -- 48 elements: permutations of axes and")
print("sign flips. It is NOT the full rotation group SO(3).")
print()
print("=> an orientation-dependent energy E(n) is GENERICALLY ALLOWED.")
print("   Exact cancellation (mechanism A) would require an identity")
print("   BEYOND the lattice symmetry, not the symmetry itself.")

print()
print("=" * 70)
print("N2 -- THE LOWEST ALLOWED ANISOTROPY (group theory alone)")
print("=" * 70)
nx, ny, nz = sp.symbols("n_x n_y n_z", real=True)
n = sp.Matrix([nx, ny, nz])
# cubic invariants of a unit vector under O_h
I2 = nx**2 + ny**2 + nz**2                      # = 1, trivial
I4 = nx**4 + ny**4 + nz**4
I6 = nx**6 + ny**6 + nz**6
print("Invariants of a unit axis under O_h, by order:")
print(f"   order 2: {I2}  -- equals 1 on the unit sphere: NO anisotropy")
print(f"   order 4: {I4}  -- the FIRST nontrivial cubic harmonic")
print(f"   order 6: {I6}")
print()
print("The axis n is also defined only up to sign (n and -n are the same")
print("axis, since the two poles are equivalent), which kills all ODD")
print("orders independently. So the leading anisotropy is ORDER 4.")
print()
vals = {"[100]": (1, 0, 0), "[110]": (1, 1, 0), "[111]": (1, 1, 1)}
print("   the order-4 invariant on the symmetry axes:")
for k, v in vals.items():
    u = np.array(v, float); u /= np.linalg.norm(u)
    print(f"      {k:>6}:  sum n_i^4 = {np.sum(u**4):.4f}")
print("   spread = 1.0000 - 0.3333 = 0.6667 -- NONZERO, so the harmonic")
print("   genuinely distinguishes orientations. It does not vanish.")
print()
print("=> VERDICT N2: SYMMETRY-ALLOWED AT ORDER 4.")
print("   The pinning is not forbidden. Mechanism (A) is EXCLUDED unless")
print("   a further, non-symmetry identity is produced.")

print()
print("=" * 70)
print("N3 -- THE DYNAMICAL AVERAGE (mechanism C)")
print("=" * 70)
print("ELEC-068 (registered): the electron has NO static branch; it exists")
print("only as a rotating configuration. If the core rotates about its own")
print("axis n, does that average the order-4 harmonic away?")
print()
print("   The order-4 invariant depends on n ALONE, not on the phase of")
print("   rotation about n. Rotating the configuration about its OWN axis")
print("   leaves n fixed, so sum n_i^4 is UNCHANGED by that motion.")
print("   => rotation about the axis does NOT average the pinning away.")
print()
print("   Averaging would require the AXIS ITSELF to precess or tumble")
print("   through many orientations on the timescale of a measurement.")
print("   ELEC-068 registers rotation of the winding pattern; it does NOT")
print("   register axis tumbling, and no claim supplies a precession rate.")
print()
print("=> VERDICT N3: NOT AVERAGED by the registered dynamics.")
print("   Mechanism (C) is available in principle but UNREGISTERED: it")
print("   would need a tumbling rate the corpus does not have.")

print()
print("=" * 70)
print("CONSEQUENCE FOR THE NEXT COMMISSION")
print("=" * 70)
print("Mechanism (A) excluded by symmetry; (C) unregistered. Only (B)")
print("remains: a strong DERIVED suppression, whose coefficient must come")
print("from the registered mechanics. The prefactor commission is")
print("therefore DECISIVE and its target is now known in advance:")
print("   E_pin(n) = C_pin * s^(-3/2) * [sum_i n_i^4 - 3/5] * E_core")
print("with the bracket the normalized order-4 cubic harmonic and C_pin")
print("the one number left. The 3/2 scaling is FIXED INPUT, per the bar.")
