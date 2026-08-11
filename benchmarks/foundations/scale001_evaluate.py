#!/usr/bin/env python3
"""SCALE-001 Phase 3 -- evaluate the LOCKED laws once.

Laws frozen in analysis/SCALE001_PHASE2_laws.md (hash in
analysis/SCALE001_PHASE2.lock). Three evaluable classes: C2, C3, C8.
Five UNDERSPECIFIED: C1, C4, C5, C6, C7.

Registered inputs only; provenance on every line.
"""
import math

# Registered inputs (see the locked laws file for claim IDs).
K_ME = 2.6065e-14        # T0*a, spent calibration (FND-038)
S_EFF = 3.61e35          # Sigma_eff, pinned (FND-030 / ELEC-081)
FLOORS = (50, 250)       # kappa_pack floors (FND-040)
R_EQ = 0.402e-15         # m, flux-tube equilibrium radius (ELEC-081 median)
K_OVER_T0 = 2.0          # adjudicated stretch modulus (EM-RECON-013/017, GRV-073)

rows = []
for kap in FLOORS:
    a = (3 * K_ME / (kap * S_EFF)) ** (1 / 3)   # FND-038 solve (FND-040 corr.)
    t0 = K_ME / a                                # FND-017
    kappa_lock = 2 * t0 / a                      # PRED-003-ETA, exact
    g_c2 = (K_OVER_T0 - 1) ** -0.5               # C2, per-floor invariant
    g_c3 = R_EQ / a                              # C3
    g_c8 = math.sqrt(t0 / (2 * kappa_lock * a))  # C8
    rows.append((kap, a, g_c2, g_c3, g_c8))

print("SCALE-001 PHASE 3 -- single evaluation of the locked laws")
print(f"{'kappa':>6} {'a [m]':>10} {'g_C2':>8} {'g_C3':>8} {'g_C8':>8}")
for kap, a, c2, c3, c8 in rows:
    print(f"{kap:>6} {a:>10.3e} {c2:>8.3f} {c3:>8.3f} {c8:>8.3f}")

# Look-elsewhere convention committed in the locked laws file:
# three locked evaluable laws, log-uniform prior over 10^0..10^4 cells.
# Target log-width filled in at unseal; the per-law hit probability is
# p = ln(hi/lo) / ln(1e4); P(>=1 of 3) = 1 - (1-p)^3.
def look_elsewhere(lo, hi, n_laws=3):
    p = math.log(hi / lo) / math.log(1e4)
    return p, 1 - (1 - p) ** n_laws

if __name__ == "__main__":
    print("\nUnseal separately; then compute look_elsewhere(lo, hi).")
