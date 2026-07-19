"""
topology/linking.py  --  Canonical linking-number and curve topology tools.

The electric charge of a rope soliton is the Gauss linking number between its
two strands (q = Lk).  This module is the single canonical implementation;
every relaxation tracks Lk through it to verify topological conservation.
"""
import numpy as np


def linking_number(A, B):
    """Discrete Gauss linking integral between two closed curves A, B.

    A, B : (M,3) and (K,3) arrays of node positions (closed: last connects
    to first).  Returns a float that should be close to an integer for a
    well-resolved link.
    """
    A = np.asarray(A)
    B = np.asarray(B)
    nA, nB = len(A), len(B)
    dA = np.roll(A, -1, axis=0) - A          # (nA,3) segment vectors
    dB = np.roll(B, -1, axis=0) - B          # (nB,3)
    total = 0.0
    for i in range(nA):
        r = A[i] - B                          # (nB,3)
        rn = np.linalg.norm(r, axis=1) + 1e-12
        cross = np.cross(np.broadcast_to(dA[i], (nB, 3)), dB)   # (nB,3)
        total += np.sum(np.einsum("ij,ij->i", cross, r) / rn**3)
    return total / (4 * np.pi)


def writhe(C):
    """Self-writhe of a single closed curve C (M,3) via the Gauss double sum.

    Diagonal (i==j) and adjacent terms are skipped to avoid the self-singularity.
    """
    C = np.asarray(C)
    n = len(C)
    dC = np.roll(C, -1, axis=0) - C
    total = 0.0
    for i in range(n):
        for j in range(n):
            if abs(i - j) <= 1 or abs(i - j) >= n - 1:
                continue
            r = C[i] - C[j]
            rn = np.linalg.norm(r) + 1e-12
            total += np.dot(np.cross(dC[i], dC[j]), r) / rn**3
    return total / (4 * np.pi)


def torus_link(M, n, R=2.5, r=0.9):
    """Construct a (2,2n) torus link: two components with linking number n.

    Returns (C1, C2), each an (M,3) array.  The constructed linking number
    should verify as approximately n via linking_number(C1, C2).
    """
    phi = np.linspace(0, 2 * np.pi, M, endpoint=False)

    def comp(offset):
        ang = n * phi + offset
        return np.stack([(R + r * np.cos(ang)) * np.cos(phi),
                         (R + r * np.cos(ang)) * np.sin(phi),
                         r * np.sin(ang)], axis=1)

    return comp(0.0), comp(np.pi)


def hopf_curves(M, R=1.0, sep=None):
    """Two interlocked circles forming a Hopf link (Lk=1), as node arrays."""
    if sep is None:
        sep = R
    t = np.linspace(0, 2 * np.pi, M, endpoint=False)
    C1 = np.stack([R * np.cos(t), R * np.sin(t), np.zeros(M)], axis=1)
    C2 = np.stack([sep + R * np.cos(t), np.zeros(M), R * np.sin(t)], axis=1)
    return C1, C2
