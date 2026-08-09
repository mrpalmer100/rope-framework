"""COMMISSION ETA -- E4: THE CONFRONTATION (marked; target loaded HERE ONLY).

Form locked before this file ran (see eta_contact_dispersion.py output and
analysis/ETA_bars_LOCKED.md):
  lever fraction of tension mass, per knot, UNIVERSAL (all L_k cancel):
    f_mech = [g''(x0) ln(kmax/kmin) / (2 pi)] * eps * rho * (a/sigma0)^3
  with eps = hbar c/(T0 a^2)  (registered ambient quantum over T0 a),
       rho = Ac sigma0/(T0 a) (the material ratio, carried symbolically),
       sigma0/a = 0.362       (EM-RECON-018, w/a from registered f_c),
       g'' in [1.000, 1.470] over the standoff band, positive throughout,
       ln in [ln 4, ln 30] (IR band, both carried).
"""
import numpy as np

HBAR, C = 1.054571817e-34, 2.99792458e8
A_M, T0_M = 6.0056e-17, 434.0            # registered (MATTER055 constants)
SIGMA_OVER_A = 0.362                      # EM-RECON-018
G_BAND = (1.000, 1.470)                   # derived, E1
LN_BAND = (np.log(4), np.log(30))         # IR readings, both carried

eps = HBAR * C / (T0_M * A_M ** 2)
print(f"eps = hbar c/(T0 a^2) = {eps:.4e}   (T0 a = "
      f"{T0_M*A_M/1.602176634e-13:.4f} MeV, quantum = "
      f"{HBAR*C/A_M/1.602176634e-13:.1f} MeV)")

# ===================== TARGET LOADED (E4 ONLY) =====================
# Demand (MATTER055, unchanged): zp share = 25% of m_tot; tension = 75%.
# So the demanded fraction of the TENSION mass is 0.25/0.75 = 1/3, per
# knot, universal -- the same normalization in which the mechanism is
# universal. (The 1.156e-5 target was the SAME demand expressed against
# the DEZP raw term; both are one number.)
F_DEMAND = 0.25 / 0.75
print(f"DEMAND: f = {F_DEMAND:.4f} of tension mass (equivalently the "
      f"registered lambda target 1.156e-5 against the DEZP raw term)")

print("\nMechanism value across the carried bands:")
inv = 1.0 / SIGMA_OVER_A
results = []
for g2 in G_BAND:
    for lnv in LN_BAND:
        pref = g2 * lnv / (2 * np.pi)
        # f_mech = pref * eps * rho * (a/sigma0)^3  -> rho needed:
        rho_needed = F_DEMAND / (pref * eps * inv ** 3)
        results.append(rho_needed)
        print(f"  g''={g2:.3f}, ln={lnv:.3f}: rho_needed = {rho_needed:.3e}")
lo, hi = min(results), max(results)
print(f"\nRHO REQUIRED BY THE LEVER: [{lo:.2e}, {hi:.2e}]")
print("RHO REQUIRED BY CORE SURVIVAL (EM-RECON-018): [0.40, 0.46]")
print("RHO BOUNDED BY NUCLEAR IMPORT (FND-029): [0.019, 87] (straddles)")
gap = 0.40 / hi
print(f"\nTHE THIRD CENSUS CONFLICTS: the lever demands rho ~ 1e-6-1e-5, "
      f"the survival band demands rho >= 0.40 -- a factor {gap:.1e} apart.")
print("At any survival-band rho the mechanism OVERSHOOTS the lever by the")
print("same ~1e4-1e5 -- the MATTER055 genericity finding reappearing from")
print("inside a founded mechanism: a mesh-cutoff zero-point effect arrives")
print("orders too large unless the material ratio is tiny, and the ratio")
print("cannot be tiny without collapsing the EM core.")
