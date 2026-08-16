"""GRV-105 -- COMMISSION NUN-GRV2: THE beta_J PIN AUDIT.

Bars locked in analysis/NUNGRV2_betaJ_pin_bars_LOCKED.md BEFORE this
script was written. Clean-room rule B3 in force: no LARES-2 or GR
Lense-Thirring numerical value appears anywhere in this file.
"""
import numpy as np

# Registered inputs only (charter's permitted list)
GAMMA = 4.21e-4          # J/m, K_0, GRV-073 (coarse-effective, EM-RECON-032)
T0 = 1203.0              # J/m, lattice-anchored tension (GRV-073 benchmark)


def main():
    print("B1 THE CHAIN, FACTOR BY FACTOR:")
    print("   Step 1  FIELD EQUATION. GRV-066: the co-rotation mode phi obeys")
    print("           gamma * laplacian(phi) = -s(x), POISSON -- no screening,")
    print("           because the locking mass term is FORBIDDEN (EM-RECON-012")
    print("           derived: no material points -> gradient-order penalty only).")
    print("           Propagation coefficient = gamma, DERIVED (GRV-073).")
    print()
    print("   Step 2  SOURCE UNDER THE GRANT. GRV-104 grants: mechanical J")
    print("           LIVES in topological-geometric twist -- the totality")
    print("           reading, no partition. Conservation bookkeeping then")
    print("           fixes the source: the twist sector carries ALL of the")
    print("           body's J, so s(x) integrates to J exactly.")
    print("               s = beta_J * j_matter(x),   beta_J = 1")
    print("           Any beta_J != 1 would mean a fraction of J living")
    print("           outside twist, contradicting the grant as worded.")
    print("           This is a PIN BY THE GRANT'S OWN TOTALITY, not by a")
    print("           new assumption: the coefficient slot is closed by the")
    print("           identification's wording plus J-conservation.")
    print()
    print("   Step 3  FAR FIELD, closed form, no open slot at medium level:")
    print("           phi(r) ~ J_source / (8 pi gamma r^3) x angular structure")
    print("           (the GRV-066 session verified falloff + angular form")
    print("           match the Lense-Thirring PATTERN with no free parameter;")
    print("           the pattern match is registered, the RATE is not quoted")
    print("           here per B3).")
    gamma_check = GAMMA / T0
    print(f"           gamma/T0 = {gamma_check:.2e} (seven orders, GRV-073)")
    assert gamma_check < 1e-5
    print()
    print("B2 WHERE THE CHAIN STOPS -- THE HONEST PART:")
    print("   The medium-level chain terminates closed. But the chain to an")
    print("   OBSERVABLE does not. Converting phi (microrotation of the")
    print("   medium) into a gyroscope precession requires the dictionary's")
    print("   SHIFT SLOT, and the registry states it does not exist:")
    print("     GRV-055 (Modeled): the one-metric bijection extends to time")
    print("       dependence ONLY onto zero-shift metrics -- 'the medium can")
    print("       ring and cannot spin' through the current operator.")
    print("     GRV-071 (Modeled): coefficients c and d ABSENT; the GRV-029")
    print("       bijection has no shift and the current operator cannot")
    print("       carry one.")
    print("   Bars clause B2(c) therefore FIRES for the confrontation chain:")
    print("   the route to a LARES-2 number requires the open shift-slot")
    print("   structure. The block is NOT in beta_J. It is in the dictionary.")
    print()
    print("B3 CLEAN-ROOM ATTESTATION: no target value was consulted,")
    print("   computed, or compared at any step above. The only numbers in")
    print("   this file are gamma and T0, both registered before the grant.")
    print()
    print("VERDICT (per bars B4, split, stated plainly):")
    print("   beta_J: PINNED. beta_J = 1 by the grant's totality reading plus")
    print("     J-conservation; propagation fixed by derived gamma; the")
    print("     medium-level closed form has no open slot, no new constant,")
    print("     no O(1) factor introduced.")
    print("   LARES-2 CONFRONTATION: REMAINS BLOCKED under B2(c) -- the")
    print("     shift-slot dictionary (GRV-071 c/d, GRV-055's registered")
    print("     restriction) is the missing structure, exactly as GRV-103")
    print("     already named it a separate owed item regardless of grant.")
    print("   The pin audit found the freedom does NOT hide in the coupling.")
    print("   It never got the chance to: the observable map is absent, and")
    print("   until the dictionary carries a shift, no confrontation can be")
    print("   run clean-room at any beta_J.")


if __name__ == "__main__":
    main()
