# `rope_solver.spectrum`

Fluctuation determinant

> rope_solver.spectrum  --  Canonical fluctuation-determinant tools.

## `log_det_ratio(V_grid, h, n_modes=60)`

Regularised log determinant ratio ln[det'(-nabla^2+V)/det(-nabla^2)].

Computed from the low-lying spectra of M = -nabla^2 + V and M0 = -nabla^2
on a common 3D grid.  V_grid is an (N,N,N) potential.  For a positive,
localised V (the physical second-variation potential) this returns an O(1)
number with no negative modes -- the result that falsified the one-loop
mass mechanism.

## `poschl_teller_bound_states(ell, N=600, L=24.0)`

Bound-state energies of V = -ell(ell+1) sech^2(x) (1D).

Analytic result: exactly `ell` bound states for integer ell, the deepest
at E = -ell^2.  Used to validate the spectral method.
Returns the sorted negative eigenvalues (bound states).

## `required_log_det_for_electron()`

The ln[det ratio] the electron mass would need from the one-loop term.

m_classical ~ 12 M_Pl, m_electron ~ 4e-23 M_Pl, and
ln(m_cl/m_e) ~ 54, so the (-1/2) ln det would need ln[ratio] ~ +108.
Returned for comparison against the computed O(1) value: the gap that
falsifies the one-loop mechanism.
