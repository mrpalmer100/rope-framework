"""
geometry/curve.py  --  Canonical discrete-curve forces.

CRITICAL CORRECTNESS NOTE
-------------------------
Rope tension energy is the TOTAL LENGTH:  E_tension = T0 * sum |C_{i+1} - C_i|.
Its gradient pulls each node along the UNIT vectors to its neighbours:

    F_i = T0 * ( unit(C_{i+1}-C_i) + unit(C_{i-1}-C_i) )

An earlier implementation used  F_i = T0*((C_prev - C_i) + (C_next - C_i)),
which is the force for a SPRING energy (1/2 sum |dC|^2), NOT rope tension.
With equal-length segments (a rigid circle) the two agree, which is why the
bug was invisible until nodes were given full freedom.  This module uses the
correct unit-vector tension force, verified against finite differences in
tests/test_geometry.py.
"""
import numpy as np


def _unit(v):
    n = np.linalg.norm(v, axis=-1, keepdims=True)
    return v / (n + 1e-12)


def tension_force(C, T0=1.0):
    """Rope tension force on each node of closed curve C (M,3).

    Gradient of E = T0 * sum |segment length|.
    """
    to_next = _unit(np.roll(C, -1, axis=0) - C)
    to_prev = _unit(np.roll(C, 1, axis=0) - C)
    return T0 * (to_next + to_prev)


def tension_energy(C, T0=1.0):
    """E_tension = T0 * total length of closed curve C."""
    seg = np.roll(C, -1, axis=0) - C
    return T0 * np.sum(np.linalg.norm(seg, axis=1))


def self_repulsion_force(C, q2=1.0, a=0.14):
    """Softened Coulomb self-repulsion within a single curve.

    For the linear psi equation the pairwise 1/r kernel IS the field force
    (the Green's function), so this is the genuine field force, not only a
    proxy, for inter-node interactions.
    """
    F = np.zeros_like(C)
    for i in range(len(C)):
        d = C - C[i]
        r2 = (d**2).sum(1) + a**2
        r2[i] = np.inf
        F[i] -= q2 * (d / r2[:, None]**1.5).sum(0)
    return F


def pair_repulsion_force(C, other, q2=1.0, a=0.14, core=None, core_k=60.0):
    """Field repulsion on nodes of C from another curve `other`.

    If `core` is given, adds a HARD short-range repulsion for separations
    below `core`, enforcing non-crossing so the linking number is preserved.
    A purely soft potential is finite at r=0 and lets ropes pass through one
    another (silently changing Lk) -- the hard core prevents that.
    """
    F = np.zeros_like(C)
    for i in range(len(C)):
        d = C[i] - other
        rr = np.sqrt((d**2).sum(1))
        r2 = rr**2 + a**2
        F[i] += q2 * (d / r2[:, None]**1.5).sum(0)
        if core is not None:
            close = rr < core
            if close.any():
                push = (d[close] / (rr[close, None] + 1e-9)
                        ) * (core - rr[close, None]) * core_k
                F[i] += push.sum(0)
    return F


def curve_field_energy(curves, q2=1.0, a=0.14):
    """Total softened-Coulomb field energy of a list of curves (proxy field).

    Sums over all node pairs across all curves with a single 1/r kernel.
    """
    allC = np.vstack(curves)
    E = 0.0
    for i in range(len(allC)):
        d = allC - allC[i]
        r = np.sqrt((d**2).sum(1) + a**2)
        r[i] = np.inf
        E += q2 * (1.0 / r).sum()
    return E / 2.0


def planarity(C):
    """0 for a perfectly planar curve; grows as it leaves a plane.

    Ratio of smallest to largest singular value of the centred node cloud.
    """
    Cc = C - C.mean(0)
    _, sv, _ = np.linalg.svd(Cc)
    return sv[2] / sv[0]


def rms_radius(C):
    """RMS distance of nodes from their centroid."""
    return np.sqrt(((C - C.mean(0))**2).sum(1).mean())
