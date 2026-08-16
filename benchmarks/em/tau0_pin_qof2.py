"""THE tau0 PIN SESSION (QOF2, 2026-08-16).

Bars: analysis/QOF2_tau0_pin_bars_LOCKED.md (locked first).
Registered inputs: gamma = 1 + 1/(r tau0)^2 (EM-RECON-012, Derived,
bracket ~2-4); v_t/c = 1/sqrt(5) (FND-MATTER-047); k/T0 = 2
(registered use, grade carried); c^2 = T0/mu. beta = sqrt(I/mu)/r
carried SYMBOLIC (unregistered O(1) geometry; named gate).
"""

import sympy as sp

gamma, r, tau0, beta, c, vt, kT = sp.symbols(
    "gamma r tau_0 beta c v_t kappa_T", positive=True
)

# ---------------------------------------------------------------
# 1. Invert the Derived relation.
rel = sp.Eq(gamma, 1 + 1 / (r * tau0) ** 2)
sol = sp.solve(rel, tau0)
tau0_of_gamma = [s for s in sol if s.is_positive or True][0]
tau0_of_gamma = sp.simplify(sp.Abs(tau0_of_gamma))
print("1. tau0 = ", tau0_of_gamma, "  i.e.  r tau0 = 1/sqrt(gamma-1)  [exact inversion]")
rt = 1 / sp.sqrt(gamma - 1)
assert sp.simplify(rel.rhs.subs(tau0, rt / r) - gamma) == 0
for gv in [2, 4]:
    print(f"   gamma = {gv}: r tau0 = {sp.nsimplify(rt.subs(gamma, gv))} = {float(rt.subs(gamma, gv)):.4f}")

# ---------------------------------------------------------------
# 2. Reduce tan(2 chi_d) to registered dimensionless ratios.
# tan(2 chi_d) = 2 sqrt(I mu) lambda gamma tau0 / (I k_s - lambda mu)
# Divide top and bottom by I mu:
#   top: 2 (lambda/I) gamma tau0 sqrt(I/mu) = 2 v_t^2 gamma tau0 (beta r)
#   bottom: k_s/mu - lambda/I = (k/T0) c^2 - v_t^2
lam, I_rot, mu, k_s = sp.symbols("lambda I mu k_s", positive=True)
tan2chi_raw = 2 * sp.sqrt(I_rot * mu) * lam * gamma * tau0 / (I_rot * k_s - lam * mu)
subs_ratios = {lam: vt**2 * I_rot, k_s: kT * c**2 * mu}
tan2chi = sp.simplify(tan2chi_raw.subs(subs_ratios))
tan2chi = sp.simplify(tan2chi.subs(sp.sqrt(I_rot * mu), beta * r * mu).subs(I_rot, (beta * r) ** 2 * mu))
tan2chi = sp.simplify(tan2chi)
print("\n2. tan(2 chi_d) reduced:", tan2chi)
target = 2 * (vt**2 / c**2) * beta * (gamma * tau0 * r) / (kT - vt**2 / c**2)
assert sp.simplify(tan2chi - target) == 0
print("   = 2 (v_t/c)^2 beta gamma (r tau0) / (k/T0 - (v_t/c)^2)   [verified]")

# Registered ratios in: (v_t/c)^2 = 1/5, k/T0 = 2, r tau0 = 1/sqrt(gamma-1)
tan2chi_reg = target.subs([(vt, c / sp.sqrt(5)), (kT, 2), (tau0, rt / r)])
tan2chi_reg = sp.simplify(tan2chi_reg)
print("   at registered ratios: tan(2 chi_d) =", tan2chi_reg)
coeff = sp.Rational(2, 9)
assert sp.simplify(tan2chi_reg - coeff * beta * gamma / sp.sqrt(gamma - 1)) == 0
print("   = (2/9) beta gamma / sqrt(gamma - 1)   [exact; k/T0=2 grade carried]")

# ---------------------------------------------------------------
# 3. Evaluate downstream on the gamma bracket, beta symbolic + beta=1 ref.
f = gamma / sp.sqrt(gamma - 1)
# monotonicity of f on [2,4]:
df = sp.diff(f, gamma)
crit = sp.solve(sp.Eq(df, 0), gamma)
print("\n3. f(gamma) = gamma/sqrt(gamma-1); critical point:", crit,
      "(interior minimum at gamma = 2)")
fvals = {gv: sp.simplify(f.subs(gamma, gv)) for gv in [2, 3, 4]}
print("   f(2) =", fvals[2], "= 2 (bracket MIN, at the critical point)")
print("   f(4) =", fvals[4], "=", float(fvals[4]), "(bracket MAX)")

chi_of = lambda t2: sp.atan(t2) / 2
rows = []
for gv, lab in [(2, "gamma=2"), (4, "gamma=4")]:
    t2 = coeff * fvals[gv]  # times beta
    rows.append((lab, t2))
    print(f"   {lab}: tan(2 chi_d) = ({sp.nsimplify(t2)}) * beta = {float(t2):.5f} beta")

print("\n   beta = 1 REFERENCE POINT (labeled reference, not derivation):")
for lab, t2 in rows:
    chi = float(chi_of(t2.subs({})) )
    import math
    chi = 0.5 * math.atan(float(t2))
    s2 = math.sin(chi) ** 2
    eta = math.sin(2 * chi) ** 2 / 2
    print(f"   {lab}: chi_d = {chi:.5f} rad, sin^2(chi_d) = {s2:.5f}, "
          f"eta_conv = {eta:.5f}")

# ---------------------------------------------------------------
# 4. Monotonicity audit (honest intervals).
t2s = sp.Symbol("t", positive=True)
s2_expr = sp.sin(sp.atan(t2s) / 2) ** 2
d_s2 = sp.simplify(sp.diff(s2_expr, t2s))
print("\n4. d[sin^2 chi_d]/d[tan 2chi_d] =", d_s2, " > 0 on t > 0:")
print("   downstream quantities INCREASE with beta and with f(gamma);")
print("   gamma-bracket edges map to interval edges; intervals honest.")
import math
s2_lo = math.sin(0.5 * math.atan(4 / 9)) ** 2
s2_hi = math.sin(0.5 * math.atan(8 * math.sqrt(3) / 27)) ** 2
eta_lo = math.sin(math.atan(4 / 9)) ** 2 / 2
eta_hi = math.sin(math.atan(8 * math.sqrt(3) / 27)) ** 2 / 2
print(f"   sin^2(chi_d) bracket (beta=1 ref): [{s2_lo:.5f}, {s2_hi:.5f}]")
print(f"   eta_conv     bracket (beta=1 ref): [{eta_lo:.5f}, {eta_hi:.5f}]")
assert abs(s2_lo - 0.04309) < 1e-4 and abs(eta_hi - 0.10423) < 1e-4
print(f"   L_az/L_tr <= sin^2(chi_d): spin's leak is ~{100*s2_lo:.1f}-{100*s2_hi:.1f} percent of")
print("   the transverse leak per crossing at the reference geometry.")
print("   (Instrument catch logged: a draft of this block hardcoded stale")
print("   numbers; brackets now COMPUTED and assertion-locked.)")

print("\nVERDICT CLASS: DIMENSIONLESSLY PINNED at one named gate (beta),")
print("with r tau0 = 1/sqrt(gamma-1) EXACT and bracketed [0.577, 1].")
print("Absolute tau0 remains gated on r (scale ladder), as pre-committed.")
print("\nAll assertions passed.")
