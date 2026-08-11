#!/usr/bin/env python3
"""COMMISSION RESH -- the collective mode's cutoff, best case granted.

Bars: analysis/RESH_collective_cutoff_bars_LOCKED.md.
Granted for the test: strands continuous along their length (no cutoff
along a strand axis), discreteness transverse only at crossing spacing a.
Question: what solid angle can a PeV photon propagate into?
"""
import math

HBARC_eV_m = 197.3269804e-9
K_ME, S_EFF = 2.6065e-14, 3.61e35
FLOORS = (50, 250)
E = 1.4e15                      # eV, LHAASO Galactic photons

k_photon = E / HBARC_eV_m       # 1/m
print(f"Photon wavenumber at {E:.1e} eV: |k| = {k_photon:.3e} 1/m\n")
print(f"{'kappa':>6} {'a [m]':>11} {'pi/a [1/m]':>12} {'theta_max':>12} "
      f"{'solid-angle frac':>18}")

for kap in FLOORS:
    a = (3 * K_ME / (kap * S_EFF)) ** (1 / 3)
    k_max_perp = math.pi / a
    ratio = k_max_perp / k_photon
    if ratio >= 1:
        theta = math.pi / 2; frac = 1.0
    else:
        theta = math.asin(ratio)
        # three orthogonal strand-axis families, each a double cone
        frac = min(1.0, 3 * 2 * (1 - math.cos(theta)) / 2)
    print(f"{kap:>6} {a:>11.3e} {k_max_perp:>12.3e} {theta:>12.3e} rad "
          f"{frac:>16.3e}")

print("\nIn degrees, and in familiar units:")
for kap in FLOORS:
    a = (3 * K_ME / (kap * S_EFF)) ** (1 / 3)
    theta = math.asin(min(1.0, (math.pi / a) / k_photon))
    print(f"  kappa={kap}: PeV photons confined within {math.degrees(theta):.3e} deg "
          f"({math.degrees(theta)*3600e3:.2f} milli-arcsec) of a strand axis")

print("\nBAR (locked before computing): escape succeeds iff accessible")
print("solid-angle fraction > 10 percent.")
print("The computed fractions are ~1e-9 -- nine orders below the bar.")
print("\nWHAT KILLS IT is the corpus's own commitment: FND-REL-002 forces")
print("the wave sector to Lorentz-invariant form, i.e. ISOTROPIC")
print("propagation. A medium that carries PeV photons only within")
print("milli-arcsecond cones of three axes is maximally anisotropic at")
print("high energy. The framework's earlier success is what makes this")
print("fatal -- an anisotropic escape contradicts a Derived claim.")
