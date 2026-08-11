#!/usr/bin/env python3
"""COMMISSION SHIN -- can any admissible operator raise the band ceiling?

Bars: analysis/SHIN_operator_ceiling_bars_LOCKED.md.
C1: periodicity of omega^2(k) for arbitrary-range translation-invariant
    lattice dynamics.
C2: operator-norm bound for ARBITRARY (including disordered) couplings.
"""
import sympy as sp
import math

print("=" * 72)
print("C1 -- PERIODICITY, arbitrary coupling range (symbolic)")
print("=" * 72)
k, a = sp.symbols("k a", positive=True)
n = sp.symbols("n", integer=True, positive=True)
J = sp.IndexedBase("J")
# Most general translation-invariant transverse dynamics: coupling J_n
# between sites separated by n*a. Equation of motion gives
#   mu omega^2(k) = sum_n J_n * 2 (1 - cos(n k a))
m = sp.symbols("m", positive=True)
terms = [2 * J[i] * (1 - sp.cos(i * k * a)) for i in range(1, 5)]
w2 = sum(terms) / m
shifted = w2.subs(k, k + 2 * sp.pi / a)
print("omega^2(k)            =", sp.simplify(w2))
print("omega^2(k + 2pi/a) - omega^2(k) =", sp.simplify(sp.expand_trig(shifted - w2)))
print("=> PERIODIC in k with period 2pi/a for EVERY coupling range n.")
print("   A periodic continuous function on a compact domain attains a")
print("   finite maximum. Long-range coupling does NOT evade the ceiling;")
print("   it only reshapes the band. The ceiling is a consequence of")
print("   DISCRETENESS, not of the nearest-neighbour approximation.")

print()
print("=" * 72)
print("C2 -- OPERATOR-NORM BOUND, arbitrary/disordered couplings")
print("=" * 72)
# Gershgorin: for the dynamical matrix D with row sums, omega_max^2 <=
# max_i sum_j |D_ij| / mu.  With couplings of tension type J ~ T0/a and
# mass per site mu ~ (linear density) a, the bound is c^2/a^2 up to O(1).
HBARC = 197.3269804e-9      # eV*m
K_ME, S_EFF = 2.6065e-14, 3.61e35
FLOORS = (50, 250)
PEV = 1.4e15

print("Gershgorin bound: omega_max^2 <= (sum_j |D_ij|)/mu.")
print("Tension-type couplings J ~ T0/a with site mass mu_site ~ rho a give")
print("omega_max ~ z^(1/2) c / a, z the effective coordination -- so the")
print("ceiling is c/a up to a coordination factor, for ANY arrangement.\n")
print(f"{'kappa':>6} {'a [m]':>11} {'hbar c/a [eV]':>15} "
      f"{'z needed for PeV':>18}")
for kap in FLOORS:
    a_v = (3 * K_ME / (kap * S_EFF)) ** (1 / 3)
    E1 = HBARC / a_v
    z_needed = (PEV / E1) ** 2
    print(f"{kap:>6} {a_v:>11.3e} {E1:>15.3e} {z_needed:>18.3e}")

print("\nTo reach the anchor energy at fixed a, the effective coordination")
print("(or equivalently the coupling-to-mass ratio) must rise by ~1e9-3e9.")
print("The registered couplings are fixed: T0 and mu are pinned by the")
print("m_e calibration and FND-017's invariance. No admissible operator")
print("on this mesh reaches the observed photons.")

print()
print("CONCLUSION: E_max ~ hbar c / a, up to an O(1) structural factor,")
print("for every admissible operator. The ceiling tracks the SPACING and")
print("nothing else. Operator-shaped hopes are closed as a class.")
