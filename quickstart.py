#!/usr/bin/env python3
"""
quickstart.py  --  60-second orientation for rope_solver.

  python3 quickstart.py

Prints what the toolkit is (and is NOT), then runs a single end-to-end
calculation so a new reader sees a real number come out of the canonical
solver immediately.

   THIS TOOLKIT ESTABLISHES NUMERICAL REPRODUCIBILITY, NOT PHYSICAL TRUTH.
"""
import numpy as np
from rope_solver.psi.solver import solve_psi, ring_source, field_energy
from rope_solver.topology.linking import hopf_curves, linking_number

BANNER = """
================================================================
 rope_solver  --  quickstart
================================================================
 WHAT THIS IS:
   A tested toolkit for computing rope-soliton configurations:
   a 3D Poisson solver for the field psi, linking-number topology,
   curve relaxation, plus validation and reproduction harnesses.

 WHAT THIS IS NOT:
   It does NOT prove the rope theory or any physical claim.
   It establishes numerical REPRODUCIBILITY, not physical truth.

 To verify the foundation yourself:
   python3 validation/run_validation.py     # 10 ground-truth tests
   python3 benchmarks/reproduce_results.py  # 6 prior results re-run
   python3 benchmarks/convergence.py        # grid refinement series
================================================================
"""

def main():
    print(BANNER)
    print("Running one end-to-end calculation (stable ring knot)...\n")
    N, L, a = 56, 10.0, 0.15
    Rs = np.linspace(0.5, 1.3, 9)
    Es = []
    for R in Rs:
        psi = solve_psi(ring_source(N, L, R, a), L/(N-1))
        Es.append(2*np.pi*R + field_energy(psi, L/(N-1)))
    i = int(np.argmin(Es))
    print(f"  Stable ring knot: R* ~ {Rs[i]:.2f} lambda_c, "
          f"mass ~ {Es[i]:.1f} M_Pl")
    C1, C2 = hopf_curves(60, R=1.0)
    print(f"  Hopf link charge: Lk = {linking_number(C1, C2):.3f}  (= 1, the unit charge)")
    print("\n  Both came from the canonical solver. "
          "See validation/ and benchmarks/ to check them.\n")

if __name__ == "__main__":
    main()
