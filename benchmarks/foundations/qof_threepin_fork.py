#!/usr/bin/env python3
"""COMMISSION QOF -- the three-pin fork, adjudicated.

Bars: analysis/QOF_threepin_fork_bars_LOCKED.md.
Anchor: LHAASO Galactic PeV photons, 1.4e15 eV (the same anchor
FND-REL-004's existence kill and FND-057's gap bar used).
"""
import math

HBARC = 197.3269804e-9      # eV*m
K_ME = 2.6065e-14
S_EFF = 3.61e35
FLOORS = (50, 250)
D_C = 1.87e-19              # m, strand thickness (HBAR-005, measured)
A_DISP = 9.33e-28           # m, the dispersive requirement (FND-REL-004)
PEV = 1.4e15                # eV

print("Band ceiling E_max = 2 hbar c / L for every registered material length")
print(f"Anchor: observed Galactic photons at {PEV:.1e} eV\n")
print(f"{'length':>34} {'L [m]':>12} {'E_max [eV]':>12}  holds PeV?")

def row(name, L):
    E = 2 * HBARC / L
    print(f"{name:>34} {L:>12.3e} {E:>12.3e}  {'YES' if E > PEV else 'no'}")
    return E

lengths = []
for kap in FLOORS:
    a = (3 * K_ME / (kap * S_EFF)) ** (1 / 3)
    lengths.append((f"mesh spacing a (kappa={kap})", a))
lengths.append(("strand thickness d_c (measured)", D_C))
Es = [row(n, L) for n, L in lengths]

print()
E_req = row("REQUIRED by dispersion (a_disp)", A_DISP)

smallest = min(L for _, L in lengths)
print(f"\nSmallest registered material length: {smallest:.3e} m")
print(f"Dispersive requirement:              {A_DISP:.3e} m")
print(f"GAP: the dispersion bound demands a length "
      f"{smallest/A_DISP:.1e}x SMALLER than anything the corpus registers")
print(f"     ({math.log10(smallest/A_DISP):.1f} orders below the strand thickness).")

print("\nCONSISTENCY VERDICT: no registered material length holds the")
print("observed photons. The loaded-continuum escape removes the")
print("Brillouin ZONE but cannot remove the CARRIERS -- a wave on a")
print("medium of strands of thickness d_c still has no structure finer")
print(f"than d_c, whose ceiling is {2*HBARC/D_C:.2e} eV, "
      f"{PEV/(2*HBARC/D_C):.0f}x below the observed photons.")
