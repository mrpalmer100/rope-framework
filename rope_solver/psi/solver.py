"""
psi/solver.py  --  Canonical 3D Poisson solver for the rope psi-field.

The rope gravitational/field potential psi satisfies  nabla^2 psi = -4 pi rho
in vacuum (linear field equation; the nonlinearity of the rope theory lives in
the metric-field relation, not here).  This module provides the single canonical
implementation used by every benchmark and physics calculation.

Validated against:
  - analytic 1/r Green's function (test_psi.py)
  - Brill-Lindquist conformal factor / Schwarzschild (benchmarks)
"""
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import cg


def laplacian_3d(N, h):
    """Sparse 3D finite-difference Laplacian on an N^3 grid, spacing h.

    Returns a (N^3, N^3) CSR matrix.  Dirichlet (psi->0) boundaries are
    implicit in the stencil truncation at the grid edge.
    """
    main = -2.0 * np.ones(N)
    off = np.ones(N - 1)
    L1 = sparse.diags([off, main, off], [-1, 0, 1], format="csr") / h**2
    I = sparse.identity(N, format="csr")
    L3 = (sparse.kron(sparse.kron(L1, I), I)
          + sparse.kron(sparse.kron(I, L1), I)
          + sparse.kron(sparse.kron(I, I), L1))
    return L3.tocsr()


def grid(N, L_box):
    """Return (coords, X, Y, Z, h) for an N^3 cube spanning [-L/2, L/2]^3."""
    coords = np.linspace(-L_box / 2, L_box / 2, N)
    X, Y, Z = np.meshgrid(coords, coords, coords, indexing="ij")
    h = L_box / (N - 1)
    return coords, X, Y, Z, h


def solve_psi(source, h, L3=None, rtol=1e-8, maxiter=3000):
    """Solve nabla^2 (psi-1) = -4 pi source on the grid.

    Parameters
    ----------
    source : (N,N,N) array, normalised so sum(source)*h^3 = total charge
    h      : grid spacing
    L3     : optional pre-built Laplacian (saves rebuild in scans)

    Returns
    -------
    psi : (N,N,N) array  =  1 + perturbation
    """
    N = source.shape[0]
    if L3 is None:
        L3 = laplacian_3d(N, h)
    rhs = -4.0 * np.pi * source.flatten()
    psi_pert, info = cg(L3, rhs, rtol=rtol, maxiter=maxiter)
    return 1.0 + psi_pert.reshape(N, N, N)


def field_energy(psi, h):
    """Field gradient energy  E = (1/2) integral (grad psi)^2 d^3x."""
    gx, gy, gz = np.gradient(psi, h)
    return 0.5 * (gx**2 + gy**2 + gz**2).sum() * h**3


def ring_source(N, L_box, R, a_thick):
    """Gaussian-tube source for a circular ring of radius R in the z=0 plane.

    Normalised to unit total charge.
    """
    _, X, Y, Z, h = grid(N, L_box)
    rho_cyl = np.sqrt(X**2 + Y**2)
    dist = np.sqrt((rho_cyl - R)**2 + Z**2)
    src = np.exp(-(dist / a_thick)**2 / 2)
    return src / (src.sum() * h**3)


def hopf_source(N, L_box, R, a_thick):
    """Two interlocked rings (Hopf link, Lk=1), radius R each.

    Ring 1 in the xy-plane at origin; ring 2 in the xz-plane centred at
    (R,0,0) so it threads ring 1.  Normalised to unit total charge.
    """
    _, X, Y, Z, h = grid(N, L_box)
    d1 = np.sqrt((np.sqrt(X**2 + Y**2) - R)**2 + Z**2)
    d2 = np.sqrt((np.sqrt((X - R)**2 + Z**2) - R)**2 + Y**2)
    src = np.exp(-(d1 / a_thick)**2 / 2) + np.exp(-(d2 / a_thick)**2 / 2)
    return src / (src.sum() * h**3)
