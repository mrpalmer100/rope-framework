"""COMMISSION EM-RECON-032 -- the wound-bundle effective c4.

Executed under analysis/EMRECON032_wound_c4_bars_LOCKED.md. Inputs:
registered winding angles (FND-088), medium constant k/T0 = 2
(FND-027), stability theorem (EM-RECON-009). Stiff-helix projection
model, two-level compounding; closure re-run inherits EM-RECON-031's
locked benchmark unchanged.
"""
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

S1 = 1.0/3.0                          # sin^2 psi1 (FND-088)
S2 = (15.0 + 2.0*np.sqrt(30.0))/35.0  # sin^2 psi2 (FND-088)
KT_COARSE = 2.0                       # k/T0, FND-027 (coarse observables)

def main():
    s = S1 * S2
    print("EM-RECON-032 -- wound-bundle effective c4 (locked bars)")
    print(f"M1: s = sin^2(psi1) sin^2(psi2) = {S1:.6f} x {S2:.6f} = {s:.6f}")

    c4f = (KT_COARSE*s - 1.0)/8.0
    print(f"M2: READING-FINE coarse quartic c4_eff/T_eff = (2s-1)/8 = {c4f:+.6f}")
    print(f"    sign {'<= 0 -> READING-FINE EXCLUDED (no core, no matter)' if c4f <= 0 else '> 0 -> survives'}")

    kmin = 1.0/s
    print(f"M3: core-existence demand (lower bound): (k_f/T0_f)_min = 1/s = {kmin:.4f}")

    kf = KT_COARSE/s
    print(f"M4: READING-COARSE derived fine ratio: k_f/T0_f = 2/s = {kf:.4f}"
          f"  (margin over demand: {kf/kmin:.2f}x)")

    print("\nM5: closure re-run at the surviving reading's coarse c4 = T0/8")
    print("    (inheriting EM-RECON-031's locked benchmark unchanged):")
    import emrecon031_ba_closure as base
    r = base.d0(2.0)
    print(f"    d0/xi = {r:.4f} at g* = 2 -> vs 1.36: {abs(r-1.36)/1.36*100:.1f}%"
          f", vs 1.67: {abs(r-1.67)/1.67*100:.1f}% -> UNCHANGED-FAIL (inherited)")

    print("\nVERDICT: READING-COARSE DERIVED-BY-EXCLUSION; CLOSURE UNCHANGED-FAIL")
    print(f"BYPRODUCTS: k_f/T0_f = {kf:.4f} (derived, stiff-helix bound); "
          f"falsifier armed: any independent k_f/T0_f < {kmin:.4f} contradicts the core")

if __name__ == "__main__":
    main()
