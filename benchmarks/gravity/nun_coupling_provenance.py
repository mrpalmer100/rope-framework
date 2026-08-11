#!/usr/bin/env python3
"""COMMISSION NUN -- the coupling-provenance audit's computable parts.

Bars: analysis/NUN_coupling_provenance_bars_LOCKED.md.
1) Symbolic check: rigid rotation of an axisymmetric displacement pattern
   is time-independent (d_t u = 0), so stationary spin sources nothing
   through the displacement sector.
2) The registered channel-inventory table for angular-momentum-shaped
   carriers (the elimination statement's arithmetic).
"""
import sympy as sp

# --- 1) the symbolic check ---
r, phi, t, Omega = sp.symbols("r phi t Omega", real=True)
F = sp.Function("F")  # arbitrary axisymmetric radial profile
# axisymmetric displacement field (radial component F(r), azimuthal G(r)):
G = sp.Function("G")
# under rigid rotation by Omega*t, the pattern maps phi -> phi - Omega*t;
# axisymmetric means no phi dependence, so the rotated field is unchanged:
u_r = F(r)              # independent of phi by axisymmetry
u_phi = G(r)
u_r_rot = u_r.subs(phi, phi - Omega * t)
u_phi_rot = u_phi.subs(phi, phi - Omega * t)
check_r = sp.simplify(sp.diff(u_r_rot, t))
check_p = sp.simplify(sp.diff(u_phi_rot, t))
print("Symbolic check -- rigid rotation of an axisymmetric pattern:")
print(f"  d_t u_r  = {check_r}")
print(f"  d_t u_phi = {check_p}")
assert check_r == 0 and check_p == 0
print("  => identically zero: stationary spin is INVISIBLE to the")
print("     displacement sector; R1 and R4 have nothing to couple to.")

# --- 2) the elimination table ---
print("\nRegistered angular-momentum-shaped carriers (closed inventory):")
rows = [
    ("medium momentum density mu d_t u", "FND-REL-002 (Derived)",
     "EXCLUDED: no material velocity exists; convective term forbidden"),
    ("charge current (winding x velocity)", "EM-RECON-026 (derived Magnus)",
     "DISQUALIFIED: scales with q, vanishes for neutral matter;"
     " frame dragging is mass-proportional"),
    ("nonlinearity-generated shift", "GRV-058 (registered null)",
     "EXCLUDED: vanishes for exactly the stationary rotating source"),
    ("strand twist density tau", "FND-STRAND-002/003, GRV-061/064/066",
     "VIABLE CHANNEL, SOURCE UNMAPPED: conserved, transported,"
     " micropolar-independent, gapless, LT-form far field --"
     " and NO claim maps knot angular momentum J to tau"),
]
for carrier, lic, verdict in rows:
    print(f"  - {carrier}\n      license: {lic}\n      {verdict}")
print("\nElimination arithmetic: 4 carriers, 3 excluded/disqualified by")
print("registered claims, 1 viable and unsourced. If matter carries J at")
print("all in this ontology, twist is the only registered place it can live.")
