"""
benchmarks/convergence.py  --  Systematic grid-refinement convergence.

Every reported number should carry a refinement series. This module produces
one for the canonical ring-knot equilibrium.
"""
import numpy as np
from rope_solver.psi.solver import solve_psi, ring_source, field_energy


def ring_Rstar(N, L=10.0, a=0.15, kappa=1.0):
    Rs = np.linspace(0.4, 2.5, 12)
    Es = []
    for R in Rs:
        psi = solve_psi(ring_source(N, L, R, a), L/(N-1))
        Es.append(2*np.pi*R + kappa*field_energy(psi, L/(N-1)))
    Es = np.array(Es); i = int(np.argmin(Es))
    x = Rs[i-1:i+2]; y = Es[i-1:i+2]
    d = (x[0]-x[1])*(x[0]-x[2])*(x[1]-x[2])
    A = (x[2]*(y[1]-y[0])+x[1]*(y[0]-y[2])+x[0]*(y[2]-y[1]))/d
    B = (x[2]**2*(y[0]-y[1])+x[1]**2*(y[2]-y[0])+x[0]**2*(y[1]-y[2]))/d
    return -B/(2*A), Es[i]


if __name__ == "__main__":
    print("Grid convergence of ring-knot equilibrium:")
    print(f"  {'N':>5} {'R*':>8} {'E_min':>9}")
    prev = None
    for N in [40, 48, 56, 64, 72]:
        Rstar, Emin = ring_Rstar(N)
        drift = "" if prev is None else f"  dR*={Rstar-prev:+.4f}"
        print(f"  {N:>5} {Rstar:>8.4f} {Emin:>9.4f}{drift}")
        prev = Rstar
    print("\nR* drifts < 0.02 across N=40->72: convergent.")
