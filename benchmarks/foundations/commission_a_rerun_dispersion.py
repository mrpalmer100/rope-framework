"""COMMISSION A RERUN (2026-08-09): the dispersion coefficient beta.

CONTAMINATION DISCLOSED: the record (beta = 1/12 - B/(T0 a^2), LHAASO
exclusion, a <~ 9.4e-28 m) has been read. This is a re-derivation
confronting the recorded numbers. Bars honored where available:
B1 (symbolic derivation, observational numbers loaded after the form),
B2 (next order reported), B3 (identities sympy-grade), B4 (bound
web-verified LIVE this session: arXiv:2402.06009, E_QG,2 > 6e-8 E_Pl,
95% CL -- discharging the original session's logged B4 breach a second
time, now in-session as the bar demanded).
"""
import numpy as np
import sympy as sp

print("=" * 72)
print("A1: THE DERIVATION (symbolic; no observational number in this block)")
print("=" * 72)
k, a, T0, mu, B, c = sp.symbols('k a T0 mu B c', positive=True)

# Registered transverse operator on the discrete weave (FND-STRAND-001 /
# GRV-029 nearest-neighbor form): tension term is the standard chain,
#   omega^2_T = (4 T0 / (mu a^2)) sin^2(k a / 2),
# and the registered bending channel adds the discrete curvature term,
#   omega^2_B = (16 B / (mu a^4)) sin^4(k a / 2).
w2 = (4*T0/(mu*a**2))*sp.sin(k*a/2)**2 + (16*B/(mu*a**4))*sp.sin(k*a/2)**4
series = sp.series(w2, k, 0, 7).removeO()
c2 = T0/mu
# write as c^2 k^2 [1 - beta (ka)^2 + gamma (ka)^4 ...]
expr = sp.simplify(series / (c2*k**2))
poly = sp.Poly(sp.expand(expr), k)
coeffs = {deg: sp.simplify(cf) for (deg,), cf in poly.terms()}
beta = sp.simplify(-coeffs.get(2, 0)/a**2 * a**2)   # coefficient of (ka)^2
beta = sp.simplify(-coeffs[2]/a**2)*a**2
print("omega^2 / (c^2 k^2) = 1 +", sp.simplify(coeffs[2]), "k^2 +",
      sp.simplify(coeffs.get(4, 0)), "k^4 + ...")
beta_sym = sp.simplify(-(coeffs[2]) / a**2 * a**2)
beta_final = sp.simplify(sp.Rational(1,12) - B/(T0*a**2))
check = sp.simplify(-(coeffs[2]) - beta_final*a**2/a**2*a**2/a**2)
print("beta (derived) =", sp.simplify(-coeffs[2]/a**2)*a**2)
assert sp.simplify(-coeffs[2] - (sp.Rational(1,12) - B/(T0*a**2))*a**2) == 0, \
    "beta must equal 1/12 - B/(T0 a^2) exactly"
print(">>> beta = 1/12 - B/(T0 a^2)  EXACT (matches record; B3 identity)")
print("B2 next order (reported):", sp.simplify(coeffs.get(4,0)),
      " -- the O((ka)^4) coefficient, carried not confronted.")
print("Sign structure: lattice tension SOFTENS (subluminal, +1/12); the")
print("bending channel STIFFENS (superluminal, -B/T0a^2). beta = 0 iff")
print("B = T0 a^2 / 12 -- a measure-zero tuning, NOT an identity: the")
print("charter's outcome-1 (exact cancellation) is EXCLUDED at B3 grade.")

print()
print("=" * 72)
print("A2: BAND-TOP EXISTENCE (still no observational number: structure)")
print("=" * 72)
wmax = sp.sqrt(w2.subs(k, sp.pi/a))
print("omega(pi/a) =", sp.simplify(wmax), " -- FINITE band ceiling:")
print("no transverse mode exists above E_max = hbar*omega_max. This is an")
print("EXISTENCE statement independent of beta's value.")

print()
print("=" * 72)
print("A3: CONFRONTATION (observational numbers loaded HERE)")
print("=" * 72)
HBARC = 0.19732698   # GeV * fm  = 1.9733e-16 GeV*m
E_PL = 1.22091e19    # GeV
EQG2 = 6e-8 * E_PL   # LHAASO GRB 221009A, 95% CL, arXiv:2402.06009 (verified live)
A_M = 6.0056e-17     # m, the M-point (registered)
print(f"Bound (web-verified this session): E_QG,2 > 6e-8 E_Pl = {EQG2:.2e} GeV")
# Convention: omega = c k sqrt(1 - beta (ka)^2) -> v_g = c[1 - (3/2) beta (ka)^2]
# LIV n=2 convention: v = c[1 - (3/2)(E/E_QG2)^2]  =>  E_QG2_pred = hbar c/(a sqrt(beta))
beta_sub = 1.0/12.0
hbarc_m = HBARC * 1e-15      # GeV * m
EQG2_pred = hbarc_m / (A_M * np.sqrt(beta_sub))
print(f"M-point prediction (subluminal branch, beta = 1/12): "
      f"E_QG,2 = hbar c/(a sqrt(beta)) = {EQG2_pred:.2f} GeV")
deficit = EQG2 / EQG2_pred
print(f"EXCLUSION: predicted scale sits {deficit:.2e} = 1e{np.log10(deficit):.1f}"
      f" ORDERS below the bound -- the a = 6.0e-17 m mesh with O(1)")
print("dispersion is DEAD in the photon sector (record's 11 orders: "
      f"{np.log10(deficit):.1f}, reproduced).")
a_live = hbarc_m / (EQG2 * np.sqrt(beta_sub))
print(f"LIVE BOUND (subluminal branch): a <= {a_live:.2e} m "
      f"(record: 9.4e-28 m -- reproduced to {abs(a_live-9.4e-28)/9.4e-28*100:.0f}%)")
# QB-008 branch (Amendment 1, record): beta ~ -115, bending-dominated
beta_qb = 115.0
a_qb = hbarc_m / (EQG2 * np.sqrt(beta_qb))
print(f"QB-008 branch (|beta| ~ 115, record): a <= {a_qb:.2e} m "
      f"(record: 2.5e-29 -- reproduced to {abs(a_qb-2.5e-29)/2.5e-29*100:.0f}%; "
      f"tightening factor {np.sqrt(beta_qb/beta_sub):.0f}, record ~37)")
print("SUPERSESSION NOTE: FND-027 (2026-08-09) has since ADJUDICATED")
print("k/T0 = 2, dissolving the QB-008 branch entirely -- Amendment 1's")
print("branch dependence and Amendment 2's decay kill are now historical")
print("(triply-dead branch), carried per superseded-not-erased.")

print()
print("BAND-TOP KILL (numbers):")
Emax = 2*hbarc_m/A_M   # hbar * omega_max = 2 hbar c / a (tension term; bending raises it O(1))
print(f"E_max = 2 hbar c / a = {Emax:.2f} GeV at the M-point; LHAASO's")
print(f"Galactic PeV photons (>= 1e6 GeV, Crab/Cygnus 2021) exceed the")
print(f"band ceiling by {1e6/Emax:.1e} -- photons that CANNOT EXIST on the")
print("M-point mesh are routinely observed. Existence-level kill,")
print("independent of beta and of timing precision (record, reproduced).")
print()
print("VERDICT: charter outcome 2 -- beta != 0 (exact form derived),")
print("confrontation EXCLUDES the M-point + lumped-operator combination")
print("at ~11 orders plus an existence kill; the suppression question is")
print("the named problem (loaded continuum, Commission G's subject).")
