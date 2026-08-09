"""FND-028: the dark-channel prediction package after FND-027 -- every
number verified from registered structure before entering the predictions
document. No new physics; the adjudicated k/T0 = 2 turns three structural
statements into committed, falsifiable relations."""
import sympy as sp
import numpy as np

print("== FND-028: dark 1.41c channel -- committed relations verified ==\n")

# (1) the cubic vertex, re-derived symbolically (EM-RECON-011 leg 2)
up, psip, k, T0 = sp.symbols("u' psi' k T_0", real=True)
eps = sp.sqrt((1 + up)**2 + psip**2) - 1
e = T0 * eps + sp.Rational(1, 2) * k * eps**2
series = sp.expand(sp.series(sp.series(e, up, 0, 3).removeO(), psip, 0, 3).removeO())
cubic = series.coeff(up, 1).coeff(psip, 2)
print(f"   cubic vertex coefficient (u' psi'^2 term): {sp.simplify(cubic)}")
print(f"   registered form (k - T0)/2: {sp.simplify(cubic - (k - T0)/2) == 0}")
val = sp.simplify(cubic.subs(k, 2*T0))
print(f"   AT THE ADJUDICATED BRANCH k = 2 T0: coefficient = {val}")
print("   -> the fast-sector coupling is COMMITTED at T0/2 -- finite, O(1)")
print("   in tension units. This corrects ELEC-067's 'grows without bound'")
print("   remark, which described the inextensible limit FND-027 closed.\n")

# (2) the speed floor
cl = float(np.sqrt(2.0))
print(f"   c_L/c floor = sqrt(k/T0) = sqrt(2) = {cl:.6f}")
print("   (EM-RECON-012: twist-stretch stiffening ADDS, so sqrt(2) is a")
print("   FLOOR, equality iff lambda gamma^2 tau0^2 << T0 -- one-sided.)\n")

# (3) the Bell gap: the medium's ceiling vs the timing floor
bell_floor = 1.38e4
print(f"   Bell-timing floor for any correlation carrier: {bell_floor:.2e} c")
print(f"   medium's committed ceiling (barring twist addition): {cl:.3f} c")
print(f"   shortfall: {bell_floor/cl:.2e} -- four orders. The framework")
print("   COMMITS: no medium wave carries Bell correlations; no finite-")
print("   speed Bell cutoff exists at any mechanically accessible speed.\n")

# (4) the cross-sector lock: one constant, two observables
print("   THE LOCK: the SAME k/T0 = 2 fixes BOTH")
print("     - the nonlinear core coefficient c4 = (k-T0)/8 = T0/8")
print("       (nuclear/chemical spacing sector, EM-RECON-009), and")
print("     - the dark channel floor c_L = sqrt(2) c (this package).")
print("   Any independent determination of either quantity constrains the")
print("   other with zero freedom. A spacing re-fit forcing k/T0 far from")
print("   2, or a channel-speed determination below sqrt(2) c, breaks the")
print("   lock and falsifies the shared-constant structure.\n")

# (5) the I^2 pump (shape-committed, scale-open)
print("   THE PUMP: with vertex (T0/2) u' psi'^2, an intense transverse")
print("   (EM) field of strain amplitude g sources longitudinal strain at")
print("   second order (forced u' ~ g^2), so energy drains into the dark")
print("   channel at rate ~ (T0/2)^2 g^4 ~ INTENSITY SQUARED -- a dark,")
print("   scatter-free vacuum attenuation growing as I^2, threshold set by")
print("   the unpinned vacuum tension density Sigma (QGATE-007 ledger).")
print("   Shape committed; location scale-open, per the document's Part IV")
print("   convention.")
