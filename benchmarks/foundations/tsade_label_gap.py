#!/usr/bin/env python3
"""COMMISSION TSADE -- the label gap, derived or not.

Bars: analysis/TSADE_label_gap_bars_LOCKED.md.
Bar: E_gap > 1.4e15 eV (LHAASO, the corpus's registered photon anchor).
"""
import math

HBARC = 197.3269804e-9      # eV*m
J_PER_EV = 1.602176634e-19
K_ME = 2.6065e-14           # T0*a, spent calibration (FND-038)
S_EFF = 3.61e35             # ELEC-081
FLOORS = (50, 250)
D_C = 1.87e-19              # m, strand thickness (HBAR-005)
A_DISP = 9.3e-28            # m, registered dispersive bound (FND-REL-004)
BAR = 1.4e15                # eV

print(f"BAR (locked): E_gap > {BAR:.1e} eV\n")
print(f"{'candidate':>42} {'kappa=50':>12} {'kappa=250':>12}  clears?")

def show(name, f):
    vals = []
    for kap in FLOORS:
        a = (3 * K_ME / (kap * S_EFF)) ** (1 / 3)
        t0 = K_ME / a
        vals.append(f(a, t0))
    ok = all(v > BAR for v in vals)
    marginal = any(v > BAR for v in vals) and not ok
    tag = "YES" if ok else ("SPLIT" if marginal else "no")
    print(f"{name:>42} {vals[0]:>12.3e} {vals[1]:>12.3e}  {tag}")
    return vals, ok

show("G1  T0*a  (locking/calibration energy)", lambda a, t0: K_ME / J_PER_EV)
show("G2  hbar*c/a  (mesh spacing quantum)", lambda a, t0: HBARC / a)
show("G3  hbar*c/d_c  (strand thickness)", lambda a, t0: HBARC / D_C)
show("G4  hbar*c/a_disp  (dispersive scale)", lambda a, t0: HBARC / A_DISP)
show("G5  sqrt(T0*hbar*c)  (confinement scale)",
     lambda a, t0: math.sqrt(t0 * HBARC / J_PER_EV * J_PER_EV) / J_PER_EV
     if False else math.sqrt(t0 / J_PER_EV * HBARC))

print("\nThe split is not noise -- it is the corpus's registered THREE-PIN")
print("FORK (FND-MATTER-068, FND-REL-004 Amendment 3, EM-RECON-025 cost 1):")
print(f"  coverage/cell-face reading of a  -> {HBARC/((3*K_ME/(50*S_EFF))**(1/3)):.2e} eV  (BELOW bar)")
print(f"  dispersive reading a_disp        -> {HBARC/A_DISP:.2e} eV  (ABOVE bar by "
      f"{HBARC/A_DISP/BAR:.0e}x)")
print("\nThe label gap does not need a new grant. It needs the fork the")
print("corpus already owes -- the same fork EM-RECON-025 already carries")
print("as a MANDATORY condition of the light carrier.")
