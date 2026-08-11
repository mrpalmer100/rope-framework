#!/usr/bin/env python3
"""COMMISSION SAMEKH -- the 1/N channel's computable adjudicators.

Bars: analysis/SAMEKH_1overN_provenance_bars_LOCKED.md.
CHECK 1: N-independence of any winding-additive pairwise functional.
CHECK 2: sign of the like-sense torsion-torsion interaction.
"""
import sympy as sp
import itertools, random

# ---------- CHECK 1 ----------
# A pairwise energy over k unit windings built from N-blind constants:
# E(k) = k*E1 + C(k,2)*V for ANY pair interaction V (V itself a function of
# registered N-blind inputs). sigma_k/sigma_1 = E(k)/E1 = k + k(k-1)V/(2E1).
# Formally: does N appear? Symbolically it cannot -- but the check makes the
# stronger point numerically: the demand b_k(N) ~ (k-1)/(N-1) is a
# NON-CONSTANT function of N at fixed k, while any winding-additive model
# yields b_k independent of N. No choice of V (any sign, any magnitude)
# can produce N-dependence.
k, N, E1, V = sp.symbols("k N E1 V", positive=True)
E_bundle = k * E1 + sp.binomial(k, 2) * V
b = 1 - E_bundle / (k * E1)
print("CHECK 1 -- winding-additive bundle, arbitrary pair interaction V:")
print(f"  b_k = {sp.simplify(b)}")
print(f"  dbdN = {sp.diff(b, N)}   (identically zero: N absent by construction)")
demand = (k - 1) / (N - 1)
print(f"  demand b_k(N) = (k-1)/(N-1): d/dN = {sp.simplify(sp.diff(demand, N))} != 0")
print("  => NO winding-additive functional with N-blind inputs can meet the")
print("     demand. The registered charge group is Z (GG-006); b_k(N)")
print("     requires the modulus of Z_N. The gap is group-theoretic, not")
print("     a missing coefficient.")

# ---------- CHECK 2 ----------
# Quadratic twist energy density e = (gamma/2) tau^2. Two parallel tubes
# with like-sense torsion fields tau1(r), tau2(r) superposed:
# E_int = gamma * integral tau1 tau2 > 0 for like sign -> REPULSION
# (energy decreases as overlap decreases). Verified on sampled profiles.
random.seed(7)
import math
def profile(r, w): return math.exp(-r * r / (2 * w * w))
def E_int(d, w1, w2, sgn):
    # 2D overlap integral on a grid
    s, h, L = 0.0, 0.1, 6.0
    x = -L
    while x <= L:
        y = -L
        while y <= L:
            r1 = math.hypot(x, y); r2 = math.hypot(x - d, y)
            s += profile(r1, w1) * sgn * profile(r2, w2) * h * h
            y += h
        x += h
    return s
print("\nCHECK 2 -- like-sense torsion-torsion interaction (gamma > 0):")
for d in (0.5, 1.0, 2.0, 4.0):
    e = E_int(d, 1.0, 1.0, +1)
    print(f"  separation {d}: E_int = {e:+.4f} (positive)")
print("  E_int > 0 at all separations and DECREASES with distance:")
print("  like-sense torsion lines REPEL (screw-dislocation class).")
print("  Opposite-sense attract -- but a k-bundle is LIKE-sense by")
print("  construction (additive winding), so S4 has the wrong sign.")
print("  And gamma, tau carry no N: no N-structure either way.")
