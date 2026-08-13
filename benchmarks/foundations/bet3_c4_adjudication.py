"""
COMMISSION BET3 -- the C6 adjudication (SCALE-001 / FND-051).

Bars: analysis/BET3_c4_sign_adjudication_bars_LOCKED.md (locked first).

ONE functional, two material conditions.

Strand with material coordinate s, lab coordinate z, transverse shape
Y(z) with slope g = Y'(z).  Let rho(z) = ds/dz be the material density
per unit lab length.  An element of lab length dz has arc length
dz*sqrt(1+g^2) and carries material rho*dz, so the stretch is

    lambda = sqrt(1+g^2)/rho,      e = lambda - 1.

Energy (EM-RECON-009's elastic strand, the only registered form):

    E = int dz  rho(z) [ T0 e + (k/2) e^2 ]

CONDITION A (fixed material, "no flow"):  rho == 1 pinned locally.
CONDITION B (material free to flow along the strand, total conserved):
    minimise E over rho(z) subject to  int rho dz = L.
    FND-017: T0 IS the Lagrange multiplier of that constraint.

Two-region model: core of lab length l = f*L carries slope g,
outer region (1-f)*L is straight.  f is the localisation fraction.
"""

import sympy as sp

T0, k, g, f = sp.symbols('T0 k g f', positive=True)
a = sp.symbols('alpha')          # rho_core  = 1 + alpha

# ---- constraint: f*rho_c + (1-f)*rho_o = 1  (total material conserved)
rho_c = 1 + a
rho_o = 1 - f*a/(1 - f)

S = sp.sqrt(1 + g**2)
e_c = S/rho_c - 1
e_o = 1/rho_o - 1

def dens(rho, e):
    return rho*(T0*e + sp.Rational(1, 2)*k*e**2)

# energy per unit lab length, whole strand
E = f*dens(rho_c, e_c) + (1 - f)*dens(rho_o, e_o)

# ---------------------------------------------------------------
# CONDITION A : no flow  (alpha = 0)
# ---------------------------------------------------------------
E_A = sp.series(E.subs(a, 0), g, 0, 6).removeO().expand()
c2_A = sp.simplify(E_A.coeff(g, 2)/f)
c4_A = sp.simplify(E_A.coeff(g, 4)/f)

# ---------------------------------------------------------------
# CONDITION B : material flows, minimise over alpha
# ---------------------------------------------------------------
# alpha is O(g^2); expand to the order needed for the quartic
a2, a4 = sp.symbols('a2 a4')
a_ser = a2*g**2 + a4*g**4
E_B = sp.series(E.subs(a, a_ser), g, 0, 6).removeO().expand()

# stationarity order by order
sol2 = sp.solve(sp.Eq(sp.diff(E_B.coeff(g, 4), a2), 0), a2, dict=True)[0]
E_B2 = sp.simplify(E_B.subs(sol2))

c2_B = sp.simplify(sp.expand(E_B2).coeff(g, 2)/f)
c4_B = sp.simplify(sp.expand(E_B2).coeff(g, 4)/f)

print("=" * 70)
print("B1  REDUCTION TEST")
print("=" * 70)
print("CONDITION A (no flow):")
print("   c2 =", sp.simplify(c2_A))
print("   c4 =", sp.factor(sp.simplify(c4_A)))
print("CONDITION B (flow, minimised):")
print("   c2 =", sp.simplify(c2_B))
print("   c4 =", sp.factor(sp.simplify(c4_B)))
print("   alpha_2 =", sp.simplify(sol2[a2]))

print()
print("Limits of CONDITION B:")
c4_B_f1 = sp.simplify(sp.limit(c4_B, f, 1))
c4_B_f0 = sp.simplify(sp.limit(c4_B, f, 0))
print("   f -> 1 (uniform, no room to flow) :", sp.factor(c4_B_f1))
print("   f -> 0 (localised in a long span) :", sp.factor(c4_B_f0))

print()
print("TARGETS:")
print("   EM-RECON-009 : (k - T0)/8")
print("   FND-040      : -T0/8")
print("   match A / B(f->1) vs EM-RECON-009 :",
      sp.simplify(c4_A - (k - T0)/8) == 0,
      sp.simplify(c4_B_f1 - (k - T0)/8) == 0)
print("   match B(f->0) vs FND-040          :",
      sp.simplify(c4_B_f0 + T0/8) == 0)

# ---------------------------------------------------------------
# B3 : monotonicity in the control parameter f
# ---------------------------------------------------------------
print()
print("=" * 70)
print("B3  MONOTONICITY IN f   (k = 2*T0, the adjudicated value, B5)")
print("=" * 70)
c4_num = sp.simplify(c4_B.subs(k, 2*T0)/T0)
print("   c4_eff/T0 =", sp.simplify(c4_num))
d = sp.simplify(sp.diff(c4_num, f))
print("   d(c4_eff/T0)/df =", sp.factor(d))
for fv in [sp.Rational(i, 20) for i in range(1, 20)]:
    print("     f = %5.2f   c4_eff/T0 = %+.6f" %
          (float(fv), float(c4_num.subs(f, fv))))

# crossover: where does the effective quartic change sign?
root = sp.solve(sp.Eq(c4_num, 0), f)
print()
print("   SIGN CROSSOVER at f =", [sp.nsimplify(r) for r in root],
      "->", [float(r) for r in root if r.is_real])
