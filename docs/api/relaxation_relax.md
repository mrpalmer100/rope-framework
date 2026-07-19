# `rope_solver.relaxation.relax`

Curve relaxation with topology tracking

> relaxation/relax.py  --  Canonical curve relaxation with topology tracking.

## `relax_link(C1, C2, steps=8000, dt=0.003, T0=1.0, q2=0.04, a=0.14, core=0.16, record_every=1000)`

Relax a two-component link with hard-core non-crossing.

Returns (C1, C2, info) where info has keys:
  'energy'  : final total energy
  'Lk0'     : initial linking number
  'Lk1'     : final linking number
  'Lk_traj' : list of (step, Lk)
  'E_traj'  : list of (step, E)

## `relax_single(C, steps=4000, dt=0.002, T0=1.0, q2=0.04, a=0.14, record_every=500)`

Relax a single closed curve under tension + self-repulsion.

Returns (C_final, energy_trajectory) where energy_trajectory is a list of
(step, total_energy).

## `ring_equilibrium(solve_psi_fn, ring_source_fn, N, L_box, a, T0=1.0, kappa=1.0, R_scan=None)`

Find the equilibrium radius of a sourced ring via energy minimisation.

solve_psi_fn, ring_source_fn are injected (from psi.solver) to keep this
module independent of the grid solver.  Returns (R_star, E_min, stable).
