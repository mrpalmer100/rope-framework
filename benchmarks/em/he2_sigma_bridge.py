#!/usr/bin/env python3
"""COMMISSION HE-2 -- the Sigma_EM <-> Sigma_eff bridge.

Bars: analysis/HE2_sigma_bridge_bars_LOCKED.md.
H1 definitional identity; H2 provenance of the 1e25; H3 consistency.
"""
import math

EPS0 = 8.854187817e-12
E_S = 1.32e18                 # Schwinger field, V/m
K_ME = 2.6065e-14             # T0 a (FND-038)
S_EFF = 3.61e35               # FND-030 pinned
FLOORS = (50, 250)

print("=" * 70)
print("H1 -- DEFINITIONAL IDENTITY (definitions, not quoted values)")
print("=" * 70)
print("EM-RECON-014: SIGMA = T0 * n_L, 'the network's vacuum TENSION")
print("DENSITY' -- a tension per unit area, i.e. tension x line density.")
print("The registered mesh HAS a line density: spacing a, three strand")
print("families, so n_L = 1/a^2 per family and 3/a^2 in total.")
print("Both readings computed; neither is chosen by hand.\n")
print(f"{'kappa':>6} {'a [m]':>11} {'T0 [J/m]':>10} "
      f"{'T0/a^2':>12} {'3T0/a^2':>12}")
vals = {}
for kap in FLOORS:
    a = (3 * K_ME / (kap * S_EFF)) ** (1 / 3)
    t0 = K_ME / a
    vals[kap] = (a, t0, t0 / a**2, 3 * t0 / a**2)
    print(f"{kap:>6} {a:>11.3e} {t0:>10.4g} {t0/a**2:>12.3e} {3*t0/a**2:>12.3e}")
print("\n   => n_L IS registered. Sigma_EM's own definition, evaluated on")
print("      the registered mesh, gives 6.0e36 - 9.0e37 J/m^3.")

print()
print("=" * 70)
print("H2 -- WHAT KIND OF NUMBER IS THE 1e25?")
print("=" * 70)
print("From EM-RECON-014's own source text (benchmarks/em/")
print("field_strain_calibration.py), quoted in substance:")
print("   'ATLAS light-by-light is consistent with QED => any classical")
print("    rope quartic must have onset >= the Schwinger scale, so")
print("    SIGMA >= eps0 E_S^2/g*^2 ~ 4e24 - 1.5e25 J/m^3 (strong bound;")
print("    EQUALITY = the identification, in which case ATLAS has")
print("    MEASURED SIGMA).'")
sigma_bound_lo = EPS0 * E_S**2 / 2.0**2
sigma_bound_hi = EPS0 * E_S**2 / 1.0**2
print(f"\n   recomputed bound: eps0 E_S^2/g*^2 for g* in [1,2] = "
      f"{sigma_bound_lo:.2e} to {sigma_bound_hi:.2e} J/m^3")
print("\n   => THE 1e25 IS A LOWER BOUND, saturated by an ASSUMED equality.")
print("      It was never a measurement. And the assumption behind the")
print("      equality -- that ATLAS measures SIGMA -- is exactly what")
print("      QGATE-007 WITHDREW (unpolarized light-by-light carries no")
print("      structure information; the rate is degenerate with")
print("      normalization).")
print("\n   CONSEQUENCE: the '10.6-order gap' is not a discrepancy between")
print("   two quantities. It is the distance between a LOWER BOUND and the")
print("   actual value. A value 11 orders ABOVE a lower bound SATISFIES it.")

print()
print("=" * 70)
print("H3 -- CONSISTENCY UNDER SUBSTITUTION")
print("=" * 70)
print(f"{'kappa':>6} {'Sigma used':>12} {'g*':>4} {'E* [V/m]':>12} "
      f"{'E*/E_Schwinger':>16}  bound ok?")
for kap in FLOORS:
    a, t0, s1, s3 = vals[kap]
    for label, sig in (("T0/a^2", s1), ("3T0/a^2", s3)):
        for gstar in (1.0, 2.0):
            Estar = gstar * math.sqrt(sig / EPS0)
            ok = Estar >= E_S
            print(f"{kap:>6} {sig:>12.2e} {gstar:>4.1f} {Estar:>12.3e} "
                  f"{Estar/E_S:>16.2e}  {'YES' if ok else 'NO'}")
print("\n   Every combination clears the Schwinger requirement by 5-6")
print("   orders, so the ATLAS consistency bound is satisfied with room.")
print("   The weaker laser bound (SIGMA > ~1e15) is satisfied by 21 orders.")
print("\n   CROSS-CHECK against an independently registered number:")
print("   FND-031 computed E_crit = 2.0e23 V/m under the PINNED Sigma and")
print("   recorded it as 1.5e5x above Schwinger -- the same order as the")
print("   values above. The corpus had ALREADY, in the FND-031 sweep, run")
print("   the EM nonlinearity confrontation on the pinned Sigma family.")

print()
print("VERDICT: BRIDGE-LANDS. Sigma_EM is not a free constant -- it is")
print("T0 n_L on the registered mesh, and the 1e25 was a saturated lower")
print("bound whose saturating assumption has been withdrawn.")
