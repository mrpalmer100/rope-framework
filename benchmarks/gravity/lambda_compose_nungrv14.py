"""COMMISSION LAMBDA-COMPOSE (NUN-GRV14, 2026-08-16).

Bars: analysis/NUNGRV14_lambda_compose_bars_LOCKED.md (locked first).
Same-chi verified at verdict level (GRV-112 <-> GRV-113, one
defining relation). Pure algebra on registered objects; fine-scale
numerics refused per the FND-091 kb precedent.
"""

import sympy as sp

chi, GIp, tau, c, C_m, kappa = sp.symbols(
    "chi GI_p tau_abs c C_m kappa_conv", positive=True
)

# ---------------------------------------------------------------
# THE CHAIN (each leg a registered claim, quoted in results):
# GRV-111/112: lambda = chi * (G I_p) * |tau|
lam = chi * GIp * tau
# GRV-120: Lambda = C_d c^3 / (2 C_m), with C_d = kappa_conv * lambda
# (kappa_conv the operator-normalization factor mapping the granted
# L_C3 coefficient into GRV-120's dipole coupling slot; carried
# symbolic -- it is a bookkeeping constant of the two registered
# conventions, not physics freedom, and it does not affect the
# STRUCTURE results below).
C_d = kappa * lam
Lambda = C_d * c**3 / (2 * C_m)
Lambda = sp.simplify(Lambda)
print("COMPOSITION: Lambda =", Lambda)

# Natural scale: Lambda at chi = 1:
Lambda_nat = sp.simplify(Lambda.subs(chi, 1))
print("Lambda_nat (chi = 1) =", Lambda_nat)
assert sp.simplify(Lambda - chi * Lambda_nat) == 0
print("Lambda = chi x Lambda_nat   [exact factorization: the vacuum's")
print("chirality fraction multiplies the natural-scale amplitude]")

# ---------------------------------------------------------------
# THE ZERO NULL (B3.2): parity-symmetric vacuum, chi = 0:
assert Lambda.subs(chi, 0) == 0
print("\nNULL: chi = 0  ==>  Lambda = 0 EXACTLY.")
print("THE FRAMEWORK'S DEFAULT (parity-symmetric) VACUUM PREDICTS")
print("ZERO FRAME DRAGGING. Stated at full volume per bars B3.2.")

# ---------------------------------------------------------------
# THE DEMAND (B3.1/B3.3): GR-strength dragging is Lambda = 1:
chi_req = sp.solve(sp.Eq(Lambda, 1), chi)[0]
print("\nDEMAND: Lambda = 1  ==>  chi_required =", chi_req, "= 1/Lambda_nat")
# Cap propagation: chi <= chi_cap = 2.49e-19 (GRV-113, registered):
chi_cap = sp.Rational(249, 100) * sp.Integer(10)**(-19) * sp.Integer(10)**0
chi_cap = sp.nsimplify(2.49e-19, rational=True)
Lambda_nat_min = sp.simplify(1 / chi_cap)
print("CAP PROPAGATION: chi <= 2.49e-19  ==>  GR-strength dragging")
print("requires Lambda_nat >= 1/2.49e-19 =", float(Lambda_nat_min), "~ 4.0e18")

# Monotonicity (honest inequality direction):
dL = sp.diff(Lambda, chi)
assert sp.simplify(dL - Lambda_nat) == 0 and Lambda_nat.is_positive
print("monotone: Lambda strictly increasing in chi; the cap maps to a")
print("floor on Lambda_nat, direction verified.")

# ---------------------------------------------------------------
# GATES (named, not filled): fine-scale (G I_p), |tau| in absolute
# units, kappa_conv, C_m calibration -- ALL inside Lambda_nat, which
# stays symbolic per the FND-091 kb precedent. NUMERICALLY-CLOSED is
# not reached, as the bars expected.
print("\nGATES: Lambda_nat = kappa_conv (G I_p)|tau| c^3/(2 C_m) stays")
print("SYMBOLIC (fine-scale G I_p unregistered; FND-091 kb precedent).")
print("The demand Lambda_nat >= 4.0e18 is registered as an INTERNAL")
print("STRUCTURAL DEMAND for the day the fine scale pins. No")
print("observational verdict issued (condition 4 unchanged).")

print("\nAll assertions passed.")
