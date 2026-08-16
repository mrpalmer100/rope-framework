"""THE Lambda_nat PRICING SESSION (NUN-GRV16, 2026-08-16).

Bars: analysis/NUNGRV16_lambdanat_price_bars_LOCKED.md (locked first).
Coarse level only; every factor sourced; numerology refused.
"""

import sympy as sp

# Registered coarse inputs (GRV-073; EM-RECON-040; FND-114 rider):
C_strand = 4.21e-36     # J.m per strand (torsional rigidity, GRV-073)
gamma_grav = 4.21e-4    # J/m (couple-stress modulus, GRV-073/GRV-105)
r = 9.35e-20            # m (strand radius = d_c/2, GRV-073)
rt_lo, rt_hi = 1/3**0.5, 1.0   # r*tau0 bracket (EM-RECON-040, exact)

tau_lo, tau_hi = rt_lo / r, rt_hi / r
print(f"1. coarse tau0 bracket: [{tau_lo:.3e}, {tau_hi:.3e}] /m")
assert abs(tau_lo - 6.17e18) / 6.17e18 < 0.01

# Numerator, both slot forms (kappa_conv decides which; carried both):
num_C = (C_strand * tau_lo, C_strand * tau_hi)         # J (per strand)
num_g = (gamma_grav * tau_lo, gamma_grav * tau_hi)     # J/m^2 (modulus)
print(f"   slot A (per-strand C x tau0):   [{num_C[0]:.3e}, {num_C[1]:.3e}] J")
print(f"   slot B (modulus gamma x tau0):  [{num_g[0]:.3e}, {num_g[1]:.3e}] J/m^2")
print("   NUMERATOR-PRICED: every factor registered; conditional riders")
print("   inherited: k/T0 = 2 (FND-114), gamma_lock bracket (EM-RECON-012),")
print("   level assignment COARSE (named residue, not adjudicated).")

# tau0 enters DIRECTLY (bars B5.4): no chi_d, hence no beta gate:
print("\n2. gate check: tau0 enters the numerator directly; the beta")
print("   (gyration) gate of EM-RECON-040 applies to chi_d only and is")
print("   NOT needed here. Verified by inspection of the formula.")

# Dimensional exhibit: Lambda_nat = kappa_conv * num * c^3 / (2 C_m)
c = 2.998e8
G_newton = 6.674e-11    # C_m's GR-calibrated value, m^3 kg^-1 s^-2
J, m_, kg, s = sp.symbols("J m kg s", positive=True)
dim_numC = J                      # slot A
dim_numg = J / m_**2              # slot B
dim_c3 = (m_ / s)**3
dim_Cm = m_**3 / (kg * s**2)
for label, dnum in [("A", dim_numC), ("B", dim_numg)]:
    dim_lam = sp.simplify(dnum * dim_c3 / dim_Cm)
    dim_lam = dim_lam.subs(J, kg * m_**2 / s**2)
    print(f"\n3. slot {label}: [num c^3/(2C_m)] = {sp.simplify(dim_lam)}")
    print(f"   kappa_conv must supply the inverse of this for a")
    print(f"   dimensionless Lambda_nat -- the normalization session's job.")

# Raw magnitudes (NOT Lambda_nat; the dimensional gate is open):
rawA = num_C[0] * c**3 / (2 * G_newton), num_C[1] * c**3 / (2 * G_newton)
print(f"\n   raw slot-A magnitude num*c^3/(2G): [{rawA[0]:.2e}, {rawA[1]:.2e}]")
print("   (units kg^2/s^3-class; quoted ONLY to show the pre-kappa scale;")
print("   NOT a Lambda_nat value; no dimensionless claim made.)")

# ---------------------------------------------------------------
# THE SUPPRESSION LEDGER (structure, not number):
print("\n4. SUPPRESSION LEDGER (registered, quoted at verdict level):")
print("   C_d side: twist couples BY IDENTITY, beta_J = 1, 'NO lambda")
print("   AND NO g_0i ANYWHERE IN THE LEG' (GRV-118 T2 / GRV-104/105).")
print("   UNSUPPRESSED at the source.")
print("   C_m side: '~40-order mass->strain suppression, LOCATED not")
print("   solved' (GRV-005); the induced strength is the registered")
print("   open problem (FND-MATTER-047 trichotomy).")
print("   COMPOSITION: Lambda_nat ~ UNSUPPRESSED / (40-order-suppressed)")
print("   -- the STRUCTURE places Lambda_nat on the LARGE side of 1.")
print("   The demand Lambda_nat >= ~4-6e18 is therefore STRUCTURALLY")
print("   CONSONANT: a hierarchy-enhanced natural amplitude tamed back")
print("   to Lambda ~ 1 by a ~1e-19 chirality fraction is the SHAPE the")
print("   registered ledger produces. Ceiling of the claim: plausible,")
print("   not derived.")

# Numerology refusal (B4):
print("\n5. FLAGGED AND REFUSED per the standing rule: the resemblance")
print("   '19 orders ~ half of the 40-order hierarchy' is numerology of")
print("   the l_chi-resemblance class (GRV-113 precedent). Displayed as")
print("   refused; nothing built on it.")

print("\nVERDICT: NUMERATOR-PRICED; DENOMINATOR-BLOCKED-AT (kappa_conv")
print("normalization; the induced-strength wall) WITH THE TRACE STATED:")
print("Lambda_nat's remaining question IS gravity's own strength")
print("question -- one wall, two sectors; STRUCTURAL-CONSONANCE affirmed.")
print("\nAll assertions passed.")
