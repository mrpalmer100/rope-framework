#!/usr/bin/env python3
"""COMMISSION YOD-2 -- is the electron core's axis pinned by the mesh?

Bars: analysis/YOD2_axis_pinning_bars_LOCKED.md.
Y1 the scale r0/a; Y2 the form of the anisotropy; Y3 the confrontation.
"""
import math

J_PER_EV = 1.602176634e-19
K_ME = 2.6065e-14          # T0 a (FND-038)
S_EFF = 3.61e35
FLOORS = (50, 250)
M_E_EV = 510998.95         # electron rest energy, eV
BAR_EV = 1e-6              # conservative degeneracy bar, locked

print("=" * 72)
print("Y1 -- THE SCALE r0/a")
print("=" * 72)
print("The registered mesoscopic ratio is g = l_q/a = 82.6 (kappa=50) to")
print("108.0 (kappa=250) -- FND-044's residual, the electron's size in")
print("cells. NOT independently derived; the conditionality is inherited.")
print()
rows = []
for kap, g in ((50, 82.6), (250, 108.0)):
    a = (3 * K_ME / (kap * S_EFF)) ** (1 / 3)
    r0 = g * a
    rows.append((kap, a, g, r0))
    print(f"   kappa={kap:>3}: a = {a:.3e} m,  g = r0/a = {g},"
          f"  r0 = {r0:.3e} m")

print()
print("=" * 72)
print("Y2 -- THE FORM OF THE ANISOTROPY")
print("=" * 72)
print("MECHANISM (stated, with its assumption): an extended object of size")
print("r0 embedded in a periodic medium of spacing a couples to the")
print("lattice through its Fourier components at the reciprocal-lattice")
print("wavevectors G = 2 pi/a. The orientation-dependent energy is set by")
print("the object's form factor at G. For a SMOOTH object of size r0 the")
print("form factor is exponentially small in G r0 -- this is the standard")
print("Peierls/commensurability argument, and the ASSUMPTION it carries is")
print("SMOOTHNESS: a core with a sharp edge on the scale of a would have a")
print("power-law form factor instead. ELEC-074's core HAS a hard boundary,")
print("so BOTH readings are computed and the weaker one is used.")
print()
print(f"{'kappa':>6} {'2 pi r0/a':>12} {'exp(-2 pi r0/a)':>18} "
      f"{'power (a/r0)^4':>16}")
for kap, a, g, r0 in rows:
    x = 2 * math.pi * g
    print(f"{kap:>6} {x:>12.1f} {math.exp(-x):>18.3e} {(1/g)**4:>16.3e}")

print()
print("=" * 72)
print("Y3 -- THE CONFRONTATION (bar locked at 1e-6 eV)")
print("=" * 72)
print("Scale the suppression by the object's own energy, m_e c^2, which is")
print("the largest energy the core could plausibly modulate:")
print()
print(f"{'kappa':>6} {'suppression':>14} {'E_pin [eV]':>14}  vs 1e-6 eV")
worst = 0.0
for kap, a, g, r0 in rows:
    for label, s in (("exponential", math.exp(-2 * math.pi * g)),
                     ("power (a/r0)^4", (1 / g) ** 4)):
        E = M_E_EV * s
        worst = max(worst, E)
        print(f"{kap:>6} {label:>14} {E:>14.3e}  "
              f"{'PASS' if E < BAR_EV else 'FAIL'}")

print()
print(f"   Worst case across both floors and both readings: {worst:.3e} eV")
print(f"   Bar: {BAR_EV:.0e} eV")
if worst < BAR_EV:
    print("   => UNPINNED on both readings.")
else:
    print("   => the POWER-LAW reading FAILS the bar. Reported as such.")
    print(f"   Margin required to pass: a further factor {worst/BAR_EV:.2e}")
