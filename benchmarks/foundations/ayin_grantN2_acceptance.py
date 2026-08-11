#!/usr/bin/env python3
"""COMMISSION AYIN -- GRANT-N2's acceptance test.

Bars: analysis/AYIN_grantN2_acceptance_bars_LOCKED.md.
Granted primitive: strands carry one of N labels; inter-tube attraction
from label exchange. Two pre-named statistics, both computed.
"""
import sympy as sp

N, k = sp.symbols("N k", positive=True)

# --- the shared shape: b_k = C(k,2) * v(N) / k ---
def b_of(v):
    return sp.simplify(sp.binomial(k, 2) * v / k)

# STATISTIC A -- free labels.
# Two tubes exchange only if they share a label; with independent uniform
# labels that happens with probability 1/N. Exchange has 2 orientations
# (i->j and j->i), but a SHARED label is a single channel: v_A = 1/N.
v_A = 1 / N
b_A = b_of(v_A)

# STATISTIC B -- exclusion labels.
# Bundle tubes carry DISTINCT labels. For a given tube of label i, the
# partner's label j is one of the N-1 others; the exchange (i,j)->(j,i)
# is a single channel per ordered pair, so 2 orientations over the N-1
# available partners: v_B = 2/(N-1).
v_B = 2 / (N - 1)
b_B = b_of(v_B)

print("SHAPE (symbolic):")
for name, b in (("A free", b_A), ("B exclusion", b_B)):
    lead = sp.simplify(sp.limit(b * N, N, sp.oo))
    prop = sp.simplify(b / (k - 1))
    print(f"  {name:>12}: b_k = {b}   b_k/(k-1) = {prop}   "
          f"N*b_k -> {lead} (falls as 1/N: {'yes' if lead.is_finite else 'no'})")

casimir_b = (k - 1) / (N - 1)
print(f"\n  antisymmetric-Casimir demand: b_k = {casimir_b}")
print(f"  B - Casimir = {sp.simplify(b_B - casimir_b)}")
print(f"  A - Casimir = {sp.simplify(sp.together(b_A - casimir_b))}")

# --- magnitude table ---
import math
def sine_b(Nv, kv):
    return 1 - (math.sin(math.pi * kv / Nv) / math.sin(math.pi / Nv)) / kv
def cas_b(Nv, kv):
    return (kv - 1) / (Nv - 1)
print("\nMAGNITUDE (binding fraction b):")
print(f"{'N':>3} {'k':>2} {'A free':>9} {'B excl':>9} {'Casimir':>9} {'sine':>9}")
for Nv in (4, 6, 8):
    for kv in (2, 3):
        if kv >= Nv: continue
        a = float(b_A.subs({N: Nv, k: kv}))
        bb = float(b_B.subs({N: Nv, k: kv}))
        print(f"{Nv:>3} {kv:>2} {a:>9.4f} {bb:>9.4f} "
              f"{cas_b(Nv, kv):>9.4f} {sine_b(Nv, kv):>9.4f}")

print("\nDISCRIMINATION: B reproduces antisymmetric-Casimir IDENTICALLY")
print("  (difference symbolically zero). A gives the right shape at half")
print("  strength (b_A/b_Casimir = (N-1)/(2N) -> 1/2).")
print("\nSOFTENING DISCLOSURE (FND-040, mandatory): the derived single-source")
print("  softening is NEGATIVE (reduces sigma/C), i.e. it pushes the bundle")
print("  ratio DOWN, further BELOW the sine law, which sits ABOVE Casimir.")
print("  The correction moves away from the data, not toward it.")
