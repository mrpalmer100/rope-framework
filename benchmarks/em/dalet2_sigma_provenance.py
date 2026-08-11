#!/usr/bin/env python3
"""COMMISSION DALET-2 -- is EM-016's SIGMA the corpus's pinned Sigma_eff?

Bars: analysis/DALET2_sigma_provenance_bars_LOCKED.md.
"""
import math

K_ME = 2.6065e-14          # T0 * a (FND-038)
S_EFF = 3.61e35            # J/m^3, pinned by FND-030, re-scoped by FND-034
SIGMA_EM = 1e25            # J/m^3, EM-RECON-014's SIGMA (ATLAS-era, pin snapped)

print("Q1 -- ARE THEY THE SAME OBJECT?\n")
print(f"   EM-RECON-014's SIGMA (EM-016 blocker (i)):  {SIGMA_EM:.2e} J/m^3")
print(f"   FND-030's pinned Sigma_eff (FND-034 scope): {S_EFF:.2e} J/m^3")
print(f"   ratio: {S_EFF/SIGMA_EM:.2e}  ({math.log10(S_EFF/SIGMA_EM):.1f} orders apart)\n")

for kap in (50, 250):
    a = (3 * K_ME / (kap * S_EFF)) ** (1 / 3)
    t0 = K_ME / a
    sigma_vac = 3 * t0 / a**2
    n_L_from_mesh = 1 / a**2                 # one strand per cell face
    sigma_if_mesh = t0 * n_L_from_mesh
    n_L_required = SIGMA_EM / t0
    print(f"   kappa={kap}: a={a:.3e} m, T0={t0:.4g} J/m")
    print(f"      Sigma_vac = 3 T0/a^2            = {sigma_vac:.3e} J/m^3")
    print(f"      T0 * n_L with n_L = 1/a^2       = {sigma_if_mesh:.3e} J/m^3")
    print(f"      n_L required to give SIGMA_EM   = {n_L_required:.3e} /m^2")
    print(f"         vs mesh 1/a^2                = {n_L_from_mesh:.3e} /m^2"
          f"   (ratio {n_L_from_mesh/n_L_required:.2e})")

print("\n   READING: the vacuum-mesh construction T0/a^2 lands within a small")
print("   factor of the pinned Sigma_eff scale (both ~1e36-1e37), while")
print("   EM-RECON-014's SIGMA sits ~11 orders BELOW it. No registered")
print("   conversion spans 11 orders. These are NOT the same quantity.")

print("\nQ2 -- WHAT IS EM-016's SIGMA, THEN?\n")
print("   EM-RECON-014 defines it as SIGMA = T0 * n_L, calibrated by ATLAS")
print("   light-by-light -- an EFFECTIVE optical-nonlinearity scale read off")
print("   a photon-photon measurement, NOT the vacuum stiffness the FND-030")
print("   series pinned from lattice tube data. Its ATLAS pin was moreover")
print("   SUPERSEDED as unsound (QGATE-007: unpolarized light-by-light")
print("   carries no structure information; the rate is degenerate with")
print("   normalization).")
print("\n   => EM-016's blocker (i) concerns an EFFECTIVE EM-sector scale")
print("      whose only quoted determination has been withdrawn, and which")
print("      is DISTINCT from the corpus's pinned Sigma_eff. Two different")
print("      quantities wear the letter Sigma.")
