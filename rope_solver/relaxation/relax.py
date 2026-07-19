"""
relaxation/relax.py  --  Canonical curve relaxation with topology tracking.

Gradient descent on node positions under the correct rope-tension force
(geometry.curve.tension_force) plus field self-repulsion, with a hard-core
non-crossing constraint that preserves the linking number.

Every relaxation records the linking-number trajectory so topological
conservation can be checked, not assumed.
"""
import numpy as np
from rope_solver.geometry.curve import (tension_force, self_repulsion_force,
                            pair_repulsion_force, tension_energy,
                            curve_field_energy)
from rope_solver.topology.linking import linking_number


def relax_single(C, steps=4000, dt=0.002, T0=1.0, q2=0.04, a=0.14,
                 record_every=500):
    """Relax a single closed curve under tension + self-repulsion.

    Returns (C_final, energy_trajectory) where energy_trajectory is a list of
    (step, total_energy).
    """
    traj = []
    for s in range(steps):
        F = tension_force(C, T0) + self_repulsion_force(C, q2, a)
        C = C + dt * F
        C = C - C.mean(0)
        if s % record_every == 0 or s == steps - 1:
            E = tension_energy(C, T0) + curve_field_energy([C], q2, a)
            traj.append((s, E))
    return C, traj


def relax_link(C1, C2, steps=8000, dt=0.003, T0=1.0, q2=0.04, a=0.14,
               core=0.16, record_every=1000):
    """Relax a two-component link with hard-core non-crossing.

    Returns (C1, C2, info) where info has keys:
      'energy'  : final total energy
      'Lk0'     : initial linking number
      'Lk1'     : final linking number
      'Lk_traj' : list of (step, Lk)
      'E_traj'  : list of (step, E)
    """
    Lk0 = linking_number(C1, C2)
    Lk_traj = [(0, Lk0)]
    E_traj = []
    for s in range(steps):
        F1 = (tension_force(C1, T0) + self_repulsion_force(C1, q2, a)
              + pair_repulsion_force(C1, C2, q2, a, core))
        F2 = (tension_force(C2, T0) + self_repulsion_force(C2, q2, a)
              + pair_repulsion_force(C2, C1, q2, a, core))
        C1 = C1 + dt * F1
        C2 = C2 + dt * F2
        com = (C1.mean(0) + C2.mean(0)) / 2
        C1 = C1 - com
        C2 = C2 - com
        if s % record_every == 0 or s == steps - 1:
            E = (tension_energy(C1, T0) + tension_energy(C2, T0)
                 + curve_field_energy([C1, C2], q2, a))
            E_traj.append((s, E))
            Lk_traj.append((s, linking_number(C1, C2)))
    info = {
        "energy": E_traj[-1][1],
        "Lk0": Lk0,
        "Lk1": linking_number(C1, C2),
        "Lk_traj": Lk_traj,
        "E_traj": E_traj,
    }
    return C1, C2, info


def ring_equilibrium(solve_psi_fn, ring_source_fn, N, L_box, a,
                     T0=1.0, kappa=1.0, R_scan=None):
    """Find the equilibrium radius of a sourced ring via energy minimisation.

    solve_psi_fn, ring_source_fn are injected (from psi.solver) to keep this
    module independent of the grid solver.  Returns (R_star, E_min, stable).
    """
    from numpy.polynomial import polynomial as P
    if R_scan is None:
        R_scan = np.linspace(0.4, 2.5, 12)
    Es = []
    for R in R_scan:
        src = ring_source_fn(N, L_box, R, a)
        psi = solve_psi_fn(src, L_box / (N - 1))
        gx, gy, gz = np.gradient(psi, L_box / (N - 1))
        E_field = 0.5 * (gx**2 + gy**2 + gz**2).sum() * (L_box / (N - 1))**3
        Es.append(T0 * 2 * np.pi * R + kappa * E_field)
    Es = np.array(Es)
    i = int(np.argmin(Es))
    if 0 < i < len(R_scan) - 1:
        x = R_scan[i - 1:i + 2]
        y = Es[i - 1:i + 2]
        d = (x[0] - x[1]) * (x[0] - x[2]) * (x[1] - x[2])
        A = (x[2] * (y[1] - y[0]) + x[1] * (y[0] - y[2]) + x[0] * (y[2] - y[1])) / d
        B = (x[2]**2 * (y[0] - y[1]) + x[1]**2 * (y[2] - y[0])
             + x[0]**2 * (y[1] - y[2])) / d
        R_star = -B / (2 * A)
        stable = A > 0
    else:
        R_star = R_scan[i]
        stable = False
    return R_star, Es[i], stable
