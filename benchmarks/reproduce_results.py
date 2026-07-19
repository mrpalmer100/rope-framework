"""
benchmarks/reproduce_results.py  --  Re-run prior physics claims through the
canonical solver and check they reproduce the published numbers.

This is the harness's core purpose: any result that does NOT reproduce is a
previously-uncaught error, surfaced now instead of by a referee.
"""
import numpy as np
import sys
from rope_solver.psi.solver import grid, solve_psi, ring_source, hopf_source, field_energy
from rope_solver.relaxation.relax import relax_link
from rope_solver.topology.linking import hopf_curves, torus_link, linking_number

checks = []
def report(name, value, expected, tol, unit=""):
    ok = abs(value - expected) <= tol
    checks.append(ok)
    print(f"  [{'OK' if ok else 'XX'}] {name}: {value:.3f}{unit} "
          f"(published {expected}{unit}, tol {tol}) {'reproduced' if ok else 'MISMATCH'}")

print("="*64)
print("REPRODUCING PRIOR RESULTS THROUGH CANONICAL SOLVER")
print("="*64)

# --- 1. Stable single-ring knot: published R*~0.85, mass~12 M_Pl --------
print("\n1. Stable ring knot (rope_computational): R*~0.85, E~12")
N, L, a = 64, 10.0, 0.15
Rs = np.linspace(0.4, 2.5, 12)
Es = []
for R in Rs:
    psi = solve_psi(ring_source(N, L, R, a), L/(N-1))
    Es.append(1.0*2*np.pi*R + field_energy(psi, L/(N-1)))  # kappa=1
Es = np.array(Es); i = int(np.argmin(Es))
x = Rs[i-1:i+2]; y = Es[i-1:i+2]
d = (x[0]-x[1])*(x[0]-x[2])*(x[1]-x[2])
A = (x[2]*(y[1]-y[0])+x[1]*(y[0]-y[2])+x[0]*(y[2]-y[1]))/d
B = (x[2]**2*(y[0]-y[1])+x[1]**2*(y[2]-y[0])+x[0]**2*(y[1]-y[2]))/d
R_star = -B/(2*A)
report("ring R*", R_star, 0.85, 0.10)
report("ring E_min", Es[i], 12.0, 1.5, " M_Pl")

# --- 2. Hopf link sourced minimum: published R*~0.83 ---------------------
print("\n2. Hopf link sourced (rope_fullfield_solitons): R*~0.83")
Rs = np.linspace(0.4, 1.6, 10); Es = []
for R in Rs:
    psi = solve_psi(hopf_source(N, L, R, a), L/(N-1))
    Es.append(1.0*2*(2*np.pi*R) + 2.0*field_energy(psi, L/(N-1)))  # kappa=2
Es = np.array(Es); i = int(np.argmin(Es))
x = Rs[i-1:i+2]; y = Es[i-1:i+2]
d = (x[0]-x[1])*(x[0]-x[2])*(x[1]-x[2])
A = (x[2]*(y[1]-y[0])+x[1]*(y[0]-y[2])+x[0]*(y[2]-y[1]))/d
B = (x[2]**2*(y[0]-y[1])+x[1]**2*(y[2]-y[0])+x[0]**2*(y[1]-y[2]))/d
report("Hopf link R*", -B/(2*A), 0.83, 0.12)

# --- 3. Flexible Hopf link: Lk conserved, relaxes to symmetric ----------
print("\n3. Flexible Hopf link (rope_flexible_hopf): Lk conserved ~1")
C1, C2 = hopf_curves(40, R=0.85)
C1n, C2n, info = relax_link(C1, C2, steps=4000, core=0.16, record_every=2000)
report("Hopf |Lk| conserved", abs(info["Lk1"]), 1.0, 0.1)

# --- 4. Higher links: Lk=2,3 conserved under relaxation -----------------
print("\n4. Higher links (rope_alpha_higher_links): Lk=2,3 conserved")
for n in [2, 3]:
    A2, B2 = torus_link(60, n)
    A2n, B2n, info = relax_link(A2, B2, steps=3000, core=0.16, record_every=1500)
    report(f"torus Lk={n} conserved", abs(info["Lk1"]), n, 0.2)

print("\n" + "="*64)
np_ = sum(checks)
print(f"REPRODUCTION: {np_}/{len(checks)} prior results reproduced")
print("="*64)
sys.exit(0 if np_ == len(checks) else 1)
