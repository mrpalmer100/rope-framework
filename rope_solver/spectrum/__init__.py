"""
rope_solver.spectrum  --  Canonical fluctuation-determinant tools.

The one-loop quantum correction to a soliton mass is governed by the
regularised determinant ratio  det'(-nabla^2 + V) / det(-nabla^2).  This module
provides the canonical spectral computation and the method-validation against
the analytically-solvable Poeschl-Teller potential.

KEY PRIOR RESULT (rope_fluctuation_determinant): the one-loop determinant gives
an O(1) correction, NOT the exp(-54) suppression the electron mass would need.
The one-loop mass mechanism is therefore falsified.  This module lets any future
paper recompute that determinant ratio from the same code.
"""
import numpy as np
from scipy import sparse


def poschl_teller_bound_states(ell, N=600, L=24.0):
    """Bound-state energies of V = -ell(ell+1) sech^2(x) (1D).

    Analytic result: exactly `ell` bound states for integer ell, the deepest
    at E = -ell^2.  Used to validate the spectral method.
    Returns the sorted negative eigenvalues (bound states).
    """
    x = np.linspace(-L / 2, L / 2, N)
    h = x[1] - x[0]
    V = -ell * (ell + 1) / np.cosh(x)**2
    main = 2.0 / h**2 + V
    off = -1.0 / h**2 * np.ones(N - 1)
    M = sparse.diags([off, main, off], [-1, 0, 1]).toarray()
    vals = np.linalg.eigvalsh(M)
    return np.sort(vals[vals < -1e-6])


def log_det_ratio(V_grid, h, n_modes=60):
    """Regularised log determinant ratio ln[det'(-nabla^2+V)/det(-nabla^2)].

    Computed from the low-lying spectra of M = -nabla^2 + V and M0 = -nabla^2
    on a common 3D grid.  V_grid is an (N,N,N) potential.  For a positive,
    localised V (the physical second-variation potential) this returns an O(1)
    number with no negative modes -- the result that falsified the one-loop
    mass mechanism.
    """
    from scipy.sparse.linalg import eigsh
    N = V_grid.shape[0]
    main = -2.0 * np.ones(N)
    off = np.ones(N - 1)
    L1 = sparse.diags([off, main, off], [-1, 0, 1], format="csr") / h**2
    I = sparse.identity(N, format="csr")
    lap = (sparse.kron(sparse.kron(L1, I), I)
           + sparse.kron(sparse.kron(I, L1), I)
           + sparse.kron(sparse.kron(I, I), L1)).tocsr()
    M0 = -lap
    M = -lap + sparse.diags(V_grid.flatten())
    valsM = np.sort(eigsh(M, k=n_modes, which="SA", return_eigenvectors=False))
    vals0 = np.sort(eigsh(M0, k=n_modes, which="SA", return_eigenvectors=False))
    shift = -min(valsM.min(), vals0.min()) + 0.5
    ldr = np.sum(np.log(valsM + shift) - np.log(vals0 + shift))
    n_neg = int(np.sum(valsM < -1e-3))
    return ldr, n_neg


def required_log_det_for_electron():
    """The ln[det ratio] the electron mass would need from the one-loop term.

    m_classical ~ 12 M_Pl, m_electron ~ 4e-23 M_Pl, and
    ln(m_cl/m_e) ~ 54, so the (-1/2) ln det would need ln[ratio] ~ +108.
    Returned for comparison against the computed O(1) value: the gap that
    falsifies the one-loop mechanism.
    """
    return 2 * np.log(12.0 / 4e-23)
