"""COMMISSION PE: the branching ratio p derived as one-crossing
inter-strand transfer, per analysis/PE_branching_ratio_bars_LOCKED.md.
The derivation is completed and checked BEFORE the sealed band is opened
for comparison (the band appears only in the final section)."""
import numpy as np
import sympy as sp

print("== COMMISSION PE: the branching ratio ==\n")

# ---------------------------------------------------------------- symmetry split
print("-- the channel split (from EM-RECON-025's registered matrix) --")
print("   Stiffness couples RELATIVE displacement: rows (T0 q^2 + s/a, -s/a).")
print("   Symmetric S = (u1+u2)/sqrt(2): the s/a terms CANCEL -> free passage,")
print("   t_S = 1 exactly (the acoustic branch's gaplessness, exhibited).")
print("   Antisymmetric A = (u1-u2)/sqrt(2): sees the crossing as a point")
print("   pinning of dimensionless contrast g (Commission G's registered")
print("   transfer relation defines g).\n")

# ---------------------------------------------------------------- exact scattering
print("-- exact antisymmetric-channel scattering (symbolic, B5) --")
g_s, ka = sp.symbols('g ka', positive=True)
# delta scatterer of dimensionless strength g on a string, wave number k:
# t_A = 1/(1 + i g/(2 ka)),  r_A = -(i g/(2 ka))/(1 + i g/(2 ka))
i = sp.I
tA = 1 / (1 + i * g_s / (2 * ka))
rA = -(i * g_s / (2 * ka)) / (1 + i * g_s / (2 * ka))
unitarity = sp.simplify(sp.Abs(tA) ** 2 + sp.Abs(rA) ** 2 - 1)
print(f"   unitarity |t_A|^2 + |r_A|^2 - 1 = {unitarity}  (exact zero required)")

# exchange probability per B1: exits on strand 2 in either direction.
# u1 = (S + A)/sqrt(2), u2 = (S - A)/sqrt(2); incident on 1 splits equally.
# far side on 2: (t_S - t_A)/2 ; near side on 2: (0 - r_A)/2.
p_expr = (sp.Abs(1 - tA) ** 2 + sp.Abs(rA) ** 2) / 4
p_simpl = sp.simplify(p_expr)
print(f"   p(g, ka) = |1 - t_A|^2/4 + |r_A|^2/4 = {p_simpl}")
x = sp.symbols('x', positive=True)          # x = g/(2 ka)
p_x = sp.simplify(p_simpl.subs(g_s, 2 * ka * x))
print(f"   in x = g/(2 ka):  p = {p_x}   (closed form: x^2/(2(1+x^2)))\n")

# ---------------------------------------------------------------- evaluate at the locked scale
print("-- evaluation at the locked encounter scale ka = 1 (B2) --")
def p_of(g, kav=1.0):
    xv = g / (2.0 * kav)
    return xv * xv / (2.0 * (1.0 + xv * xv))
print("   p(g) at ka = 1, over the registered contrast inventory (B3):")
for g in [1e-2, 3e-2, 0.1, 0.3, 1.0, 3.0, 10.0, 87.0]:
    print(f"     g = {g:6.3g}: p = {p_of(g):.3e}")
print("   sensitivity sweep (reported, not used to select), g = 0.1:")
for kav in [0.3, 0.5, 1.0, 2.0, 3.0]:
    print(f"     ka = {kav:3.1f}: p = {p_of(0.1, kav):.3e}")
print("   monotone in g, saturating at 1/2 (the topological ceiling: at")
print("   infinite contrast the crossing is a hard node and the disturbance")
print("   splits evenly). Athermal, amplitude-free, local: B6 satisfied.\n")

# ---------------------------------------------------------------- NOW open the band
print("-- confrontation with the sealed band (opened only now) --")
p_lo, p_hi = 8.3e-4, 8.6e-3
# invert p = x^2/(2(1+x^2)) -> x = sqrt(2p/(1-2p)); g = 2 ka x at ka = 1
def g_of(p):
    xv = np.sqrt(2 * p / (1 - 2 * p))
    return 2.0 * xv
g_lo, g_hi = g_of(p_lo), g_of(p_hi)
print(f"   sealed band p in [{p_lo:.1e}, {p_hi:.1e}]")
print(f"   demanded contrast window: g in [{g_lo:.3f}, {g_hi:.3f}]")
print(f"   registered inventory: floor g >= O(1e-2) (Commission G, G3);")
print(f"   material band E_x/(T0 a) in [0.019, 87] (FND-029)")
inside = (g_lo > 0.019) and (g_hi < 87) and (g_lo > 1e-2)
print(f"   window strictly inside the registered inventory: {inside}")
print(f"   window pinned by the inventory: False (the band spans 3.7 orders)")
verdict = "CONSISTENT-UNDERDETERMINED" if inside else "MISS"
print(f"\n   VERDICT (locked grammar): {verdict}")
print("   The chain does not close to a number and does not break: the")
print("   sealed p-band converts to a demanded crossing contrast")
print(f"   g in [{g_lo:.2f}, {g_hi:.2f}], sitting comfortably inside the")
print("   registered material band and above the registered floor. The")
print("   NUC-030 falsifier does NOT fire. The acquisition moves down one")
print("   rung: from p (now derived in form, exactly) to g (a material")
print("   ratio the FND-029 import already ties to the constituent width w).")
