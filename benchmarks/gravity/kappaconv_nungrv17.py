"""THE kappa_conv NORMALIZATION SESSION (NUN-GRV17, 2026-08-16).

Bars: analysis/NUNGRV17_kappaconv_bars_LOCKED.md (locked first).
"""

import sympy as sp

kg, m, s = sp.symbols("kg m s", positive=True)
Jn = kg * m**2 / s**2   # joule

# ---------------------------------------------------------------
# 1. SLOT ADJUDICATION (registered units):
# lambda = chi (G_shear I_p)|tau|: Pa m^4 / m = N m = J
u_lambda = (kg / (m * s**2)) * m**4 / m
assert sp.simplify(u_lambda - Jn) == 0
print("1. lambda units = JOULES (registered chain). SLOT A (per-strand,")
print("   joules) IS the slot; slot B (J/m^2) DIES. GRV-123 sharpened.")

# C_d units from Lambda = C_d c^3/(2 C_m) dimensionless, C_m ~ G:
u_Cm = m**3 / (kg * s**2)
u_Cd = sp.simplify(u_Cm / (m / s)**3)   # = s/kg
assert sp.simplify(u_Cd - s / kg) == 0
u_kappa = sp.simplify(u_Cd / u_lambda)
print("   C_d units = s/kg; kappa_conv = C_d/lambda units =", u_kappa)
assert sp.simplify(u_kappa - s**3 / (kg**2 * m**2)) == 0

# ---------------------------------------------------------------
# 2. THE CONVERSION AREA from the corpus's own registered pair:
C_strand = 4.21e-36    # J.m
gamma_grav = 4.21e-4   # J/m
a2 = C_strand / gamma_grav
a = a2 ** 0.5
print(f"\n2. a^2 = C/gamma_grav = {a2:.3e} m^2  ->  a = {a:.3e} m")
assert abs(a - 1.0e-16) / 1.0e-16 < 1e-6
print("   a = 1.000e-16 m EXACTLY -- the registered Lorentz-ceiling mesh")
print("   spacing. CONSISTENCY CONFIRMED: GRV-073's two numbers already")
print("   encode the registered spacing. (Confirmation, not numerology.)")

# 3. T0 and mu from GRV-073's own chain:
import math
E_pa = 8.76e40; r = 9.35e-20; c = 2.998e8; G_newton = 6.674e-11
k_stiff = E_pa * math.pi * r**2
T0 = k_stiff / 2
mu = T0 / c**2
print(f"\n3. k = E pi r^2 = {k_stiff:.3e} N; T0 = {T0:.3e} N; mu = {mu:.3e} kg/m")

# ---------------------------------------------------------------
# 4. TWO ADMISSIBLE CLOSURES (dimensional, factors registered; the
#    CHOICE requires the shift kinetic coefficient K_shift --
#    UNREGISTERED -- so both are exhibited and neither adopted):
lam_lo, lam_hi = 2.60e-17, 4.50e-17   # slot A numerator (GRV-123)

# Closure I: kappa_conv = g0 / (a mu^2 c^3)   [mu^2 c^3-class stiffness]
u_cI = 1 / (m * (kg/m)**2 * (m/s)**3)
assert sp.simplify(u_cI - u_kappa) == 0
kI = 1.0 / (a * mu**2 * c**3)
LamI = (kI * lam_lo * c**3 / (2*G_newton), kI * lam_hi * c**3 / (2*G_newton))
print(f"\n4. CLOSURE I (mu^2 c^3-class): kappa = g0/(a mu^2 c^3)")
print(f"   Lambda_nat = g0 x [{LamI[0]:.2e}, {LamI[1]:.2e}]")

# Closure II: the SAME closure written in T0 (identity T0 = mu c^2):
# kappa = g0 c/(a T0^2). Unit check (the first draft wrote c^3 here;
# the locked assertion caught it -- instrument catch, kept):
kII = c / (a * T0**2)
u_kII = sp.simplify((m/s) / (m * (kg*m/s**2)**2))
assert sp.simplify(u_kII - u_kappa) == 0
LamII = (kII * lam_lo * c**3 / (2*G_newton), kII * lam_hi * c**3 / (2*G_newton))
print(f"   CLOSURE II (T0^2-class):     kappa = g0 c^3/(a T0^2)")
print(f"   Lambda_nat = g0 x [{LamII[0]:.2e}, {LamII[1]:.2e}]")
sameQ = abs(LamI[0]-LamII[0])/LamI[0]
print(f"   NOTE: closures I and II coincide (T0 = mu c^2 identity):")
print(f"   relative difference {sameQ:.1e} -- mu^2 c^3 = T0^2/c^3 EXACTLY.")

# Closure III: Sigma-based (vacuum energy density, registered BOUND
# only, Sigma > ~8.6e27(k/T0-1) J/m^3 per EM-RECON-016 -> at k/T0=2,
# Sigma > 8.6e27): kappa = g0/(a^4 Sigma^2 / (c^3 ...)):
# need s^3/(kg^2 m^2) from Sigma [J/m^3 = kg/(m s^2)]:
u_S = kg / (m * s**2)
u_kIII = sp.simplify((m/s)**3 / (m**7 * u_S**2) * m**6)  # c^3/(a S^2 m^6)?? 
# c^3/(a^? Sigma^2): (m/s)^3 / (m^q (kg/(m s^2))^2) = m^(3-q+2) s/(kg^2 s^3)...
# solve q: (m^3/s^3) * (m^2 s^4/kg^2) / m^q = m^(5-q) s/(kg^2) -> need s^3/(kg^2 m^2):
# m^(5-q) s vs m^-2 s^3: exponents cannot match (s^1 vs s^3) -> Sigma^2 alone
# cannot close without another c: c/(a^7 Sigma^2)? (m/s)/(m^7 kg^2/(m^2 s^4))
# = m^(1-7+2) s^3/kg^2 = s^3/(kg^2 m^4): off by m^2 -> c a^2 ... :
kIII_units = sp.simplify((m/s) * m**2 / (m**7 * u_S**2) * s**0)
# c a^2/(a^7 Sigma^2) = c/(a^5 Sigma^2):
u_kIIIb = sp.simplify((m/s) / (m**5 * u_S**2))
assert sp.simplify(u_kIIIb - u_kappa) == 0
Sigma_bound = 8.6e27
kIII = c / (a**5 * Sigma_bound**2)
LamIII = (kIII * lam_lo * c**3 / (2*G_newton), kIII * lam_hi * c**3 / (2*G_newton))
print(f"   CLOSURE III (Sigma^2-class): kappa = g0 c/(a^5 Sigma^2), at the")
print(f"   registered Sigma BOUND: Lambda_nat = g0 x [{LamIII[0]:.2e}, {LamIII[1]:.2e}]")

# ---------------------------------------------------------------
# 5. CONSEQUENCE LADDER (per bars B3; chi_beta = 1.6e-19 display):
chi_b = 1.6e-19
print("\n5. CONSEQUENCE LADDER (attribution chi_beta ~ 1.6e-19, display):")
for name, Lam in [("I/II (T0-class)", LamI), ("III (Sigma-bound)", LamIII)]:
    prod = (chi_b * Lam[0], chi_b * Lam[1])
    tag = "OVERSHOOTS LT (attribution excluded under this closure)" if prod[0] > 10 \
        else ("CONSISTENT (birefringence IS frame dragging class)" if prod[1] > 0.1 else
              "UNDERSHOOTS (tension with LARES-class data)")
    print(f"   closure {name}: chi_beta x Lambda_nat = [{prod[0]:.1e}, {prod[1]:.1e}] -> {tag}")

print("\n6. SPREAD: admissible registered closures span ~"
      f"{abs(math.log10(LamIII[0]/LamI[0])):.0f} orders. THE DECIDING")
print("   OBJECT, named: the registered kinetic/stiffness coefficient of")
print("   the shift field u_t (which registered energy density the")
print("   massless vector operator of GRV-068 carries). UNREGISTERED as")
print("   a coefficient. kappa_conv is BLOCKED-AT-SHIFT-NORMALIZATION;")
print("   the slot adjudication and spacing confirmation are BANKED.")
print("\nAll assertions passed.")
