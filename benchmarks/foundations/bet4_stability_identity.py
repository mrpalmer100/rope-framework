"""
COMMISSION BET4 -- is the localised quartic's SIGN condition the same
inequality as EM-RECON-013's CORE-SURVIVAL condition?

Bars: analysis/BET4_stability_identity_bars_LOCKED.md (locked first).

B1 identity, B2 the FND-040 mapping, B3 limit hygiene.
"""
import sympy as sp

T0, k, K_c, f, g = sp.symbols('T0 k K_c f g', positive=True)

# ---- BET3 master result (FND-063), re-derived here rather than quoted
a = sp.symbols('alpha')
rc, ro = 1 + a, 1 - f*a/(1 - f)
S = sp.sqrt(1 + g**2)
ec, eo = S/rc - 1, 1/ro - 1
den = lambda r, e: r*(T0*e + sp.Rational(1, 2)*k*e**2) \
                   + sp.Rational(1, 2)*K_c*(r - 1)**2
E = f*den(rc, ec) + (1 - f)*den(ro, eo)
a2 = sp.symbols('a2')
Es = sp.series(E.subs(a, a2*g**2), g, 0, 6).removeO().expand()
sol = sp.solve(sp.Eq(sp.diff(Es.coeff(g, 4), a2), 0), a2, dict=True)[0]
c4 = sp.simplify(sp.expand(sp.simplify(Es.subs(sol))).coeff(g, 4)/f)

c4_loc = sp.simplify(sp.limit(c4, f, 0))          # localised branch
c4_uni = sp.simplify(sp.limit(c4, f, 1))          # uniform branch

k_eff = k*K_c/(k + K_c)                            # EM-RECON-013, registered

print("=" * 72)
print("B1  IDENTITY TEST")
print("=" * 72)
print("BET3 localised quartic      c4_loc =", sp.factor(c4_loc))
print("EM-RECON-013 survival form  (k_eff - T0)/8 =",
      sp.factor(sp.simplify((k_eff - T0)/8)))
print("DIFFERENCE (must be 0):",
      sp.simplify(c4_loc - (k_eff - T0)/8))

# the two INEQUALITIES, reduced by clearing positive denominators
num_sign = sp.simplify(sp.numer(sp.together(c4_loc)))          # denom 8(K_c+k) > 0
num_surv = sp.simplify(sp.numer(sp.together((k_eff - T0)/8)))  # same denom > 0
print()
print("sign  condition numerator (denom > 0):", sp.factor(sp.expand(num_sign)))
print("surv  condition numerator (denom > 0):", sp.factor(sp.expand(num_surv)))
print("IDENTICAL AS INEQUALITIES:",
      sp.simplify(sp.expand(num_sign) - sp.expand(num_surv)) == 0)
print("both reduce to:  K_c*(k - T0) > T0*k      i.e.  K_c > T0*k/(k - T0)")
print("   at k = 2*T0  ->  K_c > 2*T0 = k")

print()
print("=" * 72)
print("B2  THE FND-040 MAPPING")
print("=" * 72)
sol_keff = sp.solve(sp.Eq((sp.Symbol('keff') - T0)/8, -T0/8), sp.Symbol('keff'))
print("FND-040 registers c4 = -T0/8  ->  implied k_eff =", sol_keff)
print("k_eff = 0 requires K_c = 0 :",
      sp.solve(sp.Eq(k_eff, 0), K_c), " (k > 0 fixed)")
print("READING: c4 = -T0/8 is the NO-CONTACT-STIFFNESS corner, i.e. the")
print("         relaxed core stiffness vanishes -> NO REPULSIVE CORE.")

print()
print("=" * 72)
print("B3  LIMIT HYGIENE -- is the uniform branch governed by stability?")
print("=" * 72)
print("uniform branch c4_uni =", sp.factor(c4_uni), " (K_c absent:",
      sp.simplify(sp.diff(c4_uni, K_c)) == 0, ")")
print("at k = 2*T0 :", sp.simplify(c4_uni.subs(k, 2*T0)))
print("The uniform branch carries NO core and NO K_c; its positivity at")
print("k = 2T0 follows from k > T0 alone. Stability governs the LOCALISED")
print("branch only. Not extended.")

print()
print("=" * 72)
print("REGISTERED BAND (EM-RECON-018) -- carried, NOT adopted (B4)")
print("=" * 72)
print("survival iff Ac/(T0 a) > 2/C, band [0.40, 0.46]")
print("equivalently bundle contact multiplicity m_b < ~63-73 at L1 = 1")
print("geometries: single-pair SURVIVE, surface-line ~22 SURVIVE,")
print("            contact-patch ~63 SURVIVE, full-cross-section ~498 FAILS")
print("STATUS: EM-RECON-018 is Modeled; its plausible-geometry prior is")
print("        displayed-and-not-adopted on its own face. NOT SETTLED.")
