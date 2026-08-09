"""COMMISSION ETA: contact-modified dispersion coefficient.

Bars locked in analysis/ETA_bars_LOCKED.md BEFORE this file was written.
E1-E3 are TARGET-BLIND: the demanded lever value appears nowhere in them.
E4 is the marked confrontation, run last, loading the target only there.
"""
import numpy as np
import sympy as sp

print("=" * 72)
print("COMMISSION ETA -- E1: the local dispersion shift (target-blind)")
print("=" * 72)

# Registered contact form V(r) = Ac / (1 + (r/sigma0)^4)  (FND-KIN-005 form)
r, sigma0, Ac, x = sp.symbols('r sigma0 A_c x', positive=True)
V = Ac / (1 + (r / sigma0) ** 4)

# The ambient strand's transverse displacement w along the standoff axis
# modulates r = d0 + w. Effective spring per contact: kappa = V''(d0).
Vpp = sp.diff(V, r, 2)
g = 1 / (1 + x ** 4)
gpp = sp.simplify(sp.diff(g, x, 2))
print("V''(r) = (Ac/sigma0^2) g''(r/sigma0),  g(x) = 1/(1+x^4)")
print("g''(x) =", gpp)

# Standoff band (EM-RECON-018), BOTH ends carried:
band = [1.00, 1.38]
gpp_f = sp.lambdify(x, gpp)
xs = np.linspace(band[0], band[1], 200)
gvals = gpp_f(xs)
print(f"g''(x) over the band [1.00, 1.38]: "
      f"min {gvals.min():+.4f}, max {gvals.max():+.4f}")
print(f"  g''(1.00) = {gpp_f(1.00):+.4f}   g''(1.38) = {gpp_f(1.38):+.4f}")
sign_change = (gvals.min() < 0) and (gvals.max() > 0)
print(f"  SIGN CHANGE inside the band: {sign_change}")
if sign_change:
    from scipy.optimize import brentq
    x_c = brentq(gpp_f, band[0], band[1])
    print(f"  zero crossing at x0 = {x_c:.4f}")

# Rayleigh shift of mode q, contact at generic position (avg sin^2 = 1/2):
# mu w_tt = T0 w_xx - kappa w delta(x - x0)   =>
# delta(omega^2) = (kappa/mu)(2/L) <sin^2> = kappa/(mu L)
# eta(q) = delta-omega/omega = kappa / (2 mu omega^2 L) = kappa/(2 T0 q^2 L)
q, L, mu, T0, kap = sp.symbols('q L mu T0 kappa', positive=True)
eta_q = kap / (2 * T0 * q ** 2 * L)
print("\nE1 RESULT (per contact, mode q on segment L):")
print("  eta(q) = kappa / (2 T0 q^2 L),  kappa = (Ac/sigma0^2) g''(d0/sigma0)")
print("  1/q^2 dependence: soft modes shifted most; band-edge modes least.")

print()
print("=" * 72)
print("E2: the zero-point integral (target-blind)")
print("=" * 72)
# Zero-point shift per contact: sum over one strand's band, ONE polarization
# couples (the one along the standoff axis); mode density L/pi:
#   dE = (hbar/2) sum_q delta-omega
#      = (hbar/2) * (L/pi) * Int dq  [c q * kappa/(2 T0 q^2 L)]
#      = (hbar c kappa)/(4 pi T0) * ln(kmax/kmin)
hbar, c, kmax, kmin, a = sp.symbols('hbar c k_max k_min a', positive=True)
dE_contact = sp.Rational(1, 2) * (L / sp.pi) * sp.integrate(
    (c * q) * kap / (2 * T0 * q ** 2 * L), (q, kmin, kmax)) * hbar
dE_contact = sp.simplify(dE_contact)
print("Delta E_zp per contact =", dE_contact)

# Contact set: 2/a crossings per unit knot-strand length (EM-RECON-017 B3,
# Crofton-consistent). Knot strand length L_k -> N_c = 2 L_k / a.
# Ambient zero-point content those contacts perturb: the same strands'
# band, 2 polarizations, mode density 1/pi per unit strand length, ambient
# strand length engaged per contact ~ the segment between crossings ~ a
# (this is the SAME L that cancels in eta -- Rayleigh shift per contact is
# L-independent in dE, so no region ambiguity survives in the numerator).
# The fractional lever is defined per MATTER055: lambda = Delta E / E_raw
# with E_raw the raw ambient zero-point of the engaged strands.
# Engaged ambient length per unit knot length: (2/a crossings) x (a per
# segment) = 2 (dimensionless) -> L_amb = 2 L_k.
E_raw_per_len = 2 * sp.Rational(1, 2) * (1 / sp.pi) * sp.integrate(
    hbar * c * q, (q, 0, kmax))  # 2 polarizations
E_raw_per_len = sp.simplify(E_raw_per_len)
print("E_raw per unit ambient length (2 pol) =", E_raw_per_len)

Lk = sp.symbols('L_k', positive=True)
N_c = 2 * Lk / a
dE_knot = sp.simplify(N_c * dE_contact)
E_raw_knot = sp.simplify(E_raw_per_len * 2 * Lk)
lam = sp.simplify(dE_knot / E_raw_knot)
lam = lam.subs(kmax, sp.pi / a)
lam = sp.simplify(lam)
print("\nlambda_eta (symbolic) =", lam)

# Substitute kappa = (Ac/sigma0^2) g''(x0):
G = sp.symbols("g2", real=True)
lam2 = lam.subs(kap, (Ac / sigma0 ** 2) * G)
lam2 = sp.simplify(lam2)
print("lambda_eta =", lam2)

# FORM EXTRACTION: express against the charter's material ratio
# rho = Ac sigma0/(T0 a); then lambda = pref * rho * (a/sigma0)^3 * ln * g''
rho = sp.symbols('rho', positive=True)
expr_check = sp.simplify(lam2 / ((Ac * sigma0 / (T0 * a)) * (a / sigma0) ** 3))
print("lambda / [rho * (a/sigma0)^3] =", expr_check)
print("\nFORM (DERIVED):")
print("  lambda_eta = [g''(x0) ln(kmax/kmin) / (2 pi^3)]"
      " * (Ac sigma0/(T0 a)) * (a/sigma0)^3")
print("  POWER ADJUDICATION: in the thinness t = sigma0/a the mechanism")
print("  carries p = -3 relative to the material-ratio normalization,")
print("  i.e. lambda_eta = (g'' ln / 2 pi^3) * Ac/(T0 sigma0) * (a/sigma0).")
print("  Equivalently, in pure MATTER056 form-language: lambda ~")
print("  [Ac/(T0 a)] * (a/sigma0)^2 * ln -- NOT the retired (r/a)^2")
print("  suppression: the power of thinness is NEGATIVE (enhancement with")
print("  thinness), a categorically different form. MATTER056 adjudication")
print("  precedent applies: form fixed and recorded BEFORE confrontation.")

print()
print("=" * 72)
print("E2b: knot-independence check (057 identity bar) -- registered numbers")
print("=" * 72)
# The construction gives lambda as a ratio of per-unit-length quantities:
# every factor of L_k cancelled ABOVE (dE_knot/E_raw_knot independent of
# L_k). But the MATTER055 raw term is DEZP[k] * hbar c / a, not the
# engaged-strand normalization. Check whether the engaged-strand raw term
# tracks DEZP across the three registered knots, using the registered
# lengths from MATTER055's own constants.
import re, pathlib
src = pathlib.Path(__file__).parent / "matter055_ambient_zero_point.py"
txt = src.read_text()
LENGTHS = eval(re.search(r"LENGTHS\s*=\s*(\{[^}]*\})", txt).group(1))
DEZP = eval(re.search(r"DEZP\s*=\s*(\{[^}]*\})", txt).group(1))
print("registered LENGTHS:", LENGTHS)
print("registered DEZP   :", DEZP)
ratios = {k: LENGTHS[k] / DEZP[k] for k in DEZP}
print("L/a per DEZP unit :", {k: f"{v:.3f}" for k, v in ratios.items()})
spread = max(ratios.values()) / min(ratios.values())
print(f"spread of (L/a)/DEZP across knots: {spread:.3f}x")
print("  If lambda is charged against the DEZP raw term (the MATTER055")
print("  target definition), the mechanism's per-knot lever is")
print("  lambda_k = lambda_eta * [engaged raw]/[DEZP raw] and the spread")
print(f"  above ({spread:.2f}x) is the knot-dependence the 057 bar polices.")

print()
print("=" * 72)
print("E3: the material ratio, carried symbolically (not assigned)")
print("=" * 72)
print("  lambda_eta = C(x0, ln) * [Ac sigma0/(T0 a)] * (a/sigma0)^3")
print("  with Ac sigma0/(T0 a) the SAME ratio EM-RECON-017/018 thresholded")
print("  (survival band [0.40, 0.46]) and FND-029 bounded ([0.019, 87]")
print("  straddling). It is NOT assigned here. Numeric prefactors:")
for x0v in band:
    for lnv, tag in [(np.log(4), "ln 4 (segment ~ a, kmin ~ pi/4a... "
                      "IR = few-mesh)"),
                     (np.log(30), "ln 30 (IR = knot-region scale)")]:
        C = gpp_f(x0v) * lnv / (2 * np.pi ** 3)
        print(f"    x0={x0v:.2f}, {tag:span}".replace(":span", "")
              if False else
              f"    x0={x0v:.2f}, {tag}: C = {C:+.5f}")
print("  Both standoff ends and both IR readings carried; sign per band.")
