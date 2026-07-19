"""
examples/01_stable_knot.py  --  Compute a stable rope knot from scratch.

Demonstrates the core workflow: build a source, solve the field, scan the
size, locate the energy minimum. Run:  python3 examples/01_stable_knot.py
"""
import numpy as np
from rope_solver.psi.solver import solve_psi, ring_source, field_energy

N, L, a = 56, 10.0, 0.15
print("Scanning ring radius to find the stable knot...\n")
print(f"  {'R':>6} {'E_tension':>11} {'E_field':>10} {'E_total':>10}")
best = (None, 1e9)
for R in np.linspace(0.5, 1.5, 11):
    psi = solve_psi(ring_source(N, L, R, a), L/(N-1))
    Ef = field_energy(psi, L/(N-1))
    Et = 2*np.pi*R
    E = Et + Ef
    print(f"  {R:>6.2f} {Et:>11.3f} {Ef:>10.3f} {E:>10.3f}")
    if E < best[1]:
        best = (R, E)
print(f"\nStable knot near R* = {best[0]:.2f}, mass = {best[1]:.1f} M_Pl")
print("Tension wants to shrink the loop; field self-energy wants to spread")
print("it. Their balance picks the size -- a soliton that evades Derrick's")
print("theorem because the rope is one-dimensional.")
