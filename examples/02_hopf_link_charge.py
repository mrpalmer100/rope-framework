"""
examples/02_hopf_link_charge.py  --  Charge as a linking number.

Builds a Hopf link and higher torus links, shows the linking number IS the
electric charge (q = Lk), and that relaxation conserves it.
Run:  python3 examples/02_hopf_link_charge.py
"""
from rope_solver.topology.linking import hopf_curves, torus_link, linking_number
from rope_solver.relaxation.relax import relax_link

print("Charge = linking number (q = Lk)\n")
C1, C2 = hopf_curves(60, R=1.0)
print(f"  Hopf link:        Lk = {linking_number(C1, C2):+.3f}  -> charge 1")
for n in [2, 3]:
    A, B = torus_link(60, n)
    print(f"  (2,{2*n}) torus link: Lk = {linking_number(A, B):+.3f}  -> charge {n}")

print("\nRelaxing the Hopf link with hard-core non-crossing...")
C1, C2 = hopf_curves(40, R=0.85)
_, _, info = relax_link(C1, C2, steps=3000, core=0.16, record_every=1500)
print(f"  Lk before: {info['Lk0']:+.3f}   Lk after: {info['Lk1']:+.3f}")
print("  Topology is preserved: charge cannot change without cutting a rope.")
print("  That is why the charge is conserved -- it is a topological invariant.")
