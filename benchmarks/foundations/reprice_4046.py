"""COMMISSION REPRICE (FND-127, 2026-08-17) -- the 4.046/8.091 re-pricing.

Executes the re-pricing FND-126 named as owed: every quantity priced through
the superseded multiplicative compensation (spend 4.046, fine ratio 2/s =
8.091, compensated tension T_f = 4.046 T0_f) is recomputed under the
dynamical mapping (k_f/T0_f = 6(k/T0) - 3 = 9 exactly at k/T0 = 2;
T_fibre = 3/2 T0_f). Arithmetic only; no new physics read; the FND-114
inheritance rider (conditional on adjudicated k/T0 = 2) is carried by every
re-priced number exactly as it was carried by the old ones.

NOT re-priced here, by name:
  - EM-RECON-032's 4.046 core-existence FLOOR (quartic projection, a
    different object from stiffness homogenization; survives with a caution
    flag -- see FND-127 face).
  - Anything gated on the contact rule (pre-stress terms, KBSAT firing).
  - The KBSAT grant VALUE (author's decision; consequences displayed only).
"""
import numpy as np

u = 1 / 3
v = (15 + 2 * np.sqrt(30)) / 35
s = u * v                                     # projection transmission
KT0 = 2.0                                     # FND-114, ADOPTED-ADJUDICATED (rider)
KF_DYN = 6 * KT0 - 3                          # dynamical mapping (FND-126) = 9 exact
TF_DYN = 4.5 - 1.5 * KT0                      # fibre tension = 3/2 T0_f
KF_PROJ = 2 / s                               # superseded-in-form projection value
MARGIN = 6.1                                  # registered tight Lorentz floor (kappa50)
K1 = np.pi * 2 * np.sqrt(2) / 3               # helix curvatures (convention-blind)
K2 = np.pi * 2 * np.sqrt(v * (1 - v))
KTOT = K1 + K2

ok = True
print("COMMISSION REPRICE -- the 4.046 family under the dynamical mapping")
print(f"  projection: 1/s = {1/s:.4f}, 2/s = {KF_PROJ:.4f}  (superseded in form)")
print(f"  dynamical:  k_f/T0_f = {KF_DYN:.4f}, T_fibre/T0_f = {TF_DYN:.4f}")
print(f"  mapping coefficient 4.5 vs 4.046: +{(4.5/(1/s)-1)*100:.1f}% (FND-126's 11.2%, reproduced)\n")
ok &= abs(KF_DYN - 9) < 1e-12 and abs(TF_DYN - 1.5) < 1e-12

print("LEG 1 -- SHIN7 kb ceiling (FND-091), re-priced")
eps_old = MARGIN / (1 / s) - 1
kb_old = 2 * eps_old / KTOT**2 * (1 / s)
eps_new = MARGIN / TF_DYN - 1
kb_stat = 2 * eps_new / KTOT**2 * TF_DYN
kb_disp = 2 * eps_new / (np.pi / 2)**2 * TF_DYN
print(f"  registered: eps = {eps_old:.4f}, kb <= {kb_old:.4f} T0_f a_f^2")
print(f"  re-priced:  eps = {eps_new:.4f}, kb <= {kb_stat:.5f} T0_f a_f^2 (static, BINDING)")
print(f"              dispersive {kb_disp:.4f} ({kb_disp/kb_stat:.1f}x looser -- structure preserved)")
print("  CONDITIONAL on the energy-price form surviving the form supersession")
print("  (the price is mechanism-generic headroom arithmetic; the tension it")
print("  prices against is now the dynamical 1.5, not the compensated 4.046).")
ok &= abs(kb_old - 0.126) < 1e-3 and abs(kb_stat - 0.28192) < 1e-4

print("\nLEG 2 -- FND-119 price sheet, re-expressed")
coef_old, coef_new = KF_PROJ / 4, KF_DYN / 4
print(f"  DERIVES k/T0 = 2 iff kb/(T0_f r_s^2) = {coef_new:.4f}  (was {coef_old:.4f})")
print(f"  at KBSAT kb = 0.126: r_s = {np.sqrt(0.126/coef_new):.4f} a_f")
print("  (equals BLOCH-L's read 0.2365 BY IDENTITY -- the sheet and the read")
print("   are now the same equation; the sheet's discriminating power is spent")
print("   and re-arms only on an INDEPENDENT (kb, r_s) determination)")
corner_old = 4 * 0.126 / 0.355**2
corner_new = 4 * kb_stat / 0.3529**2
print(f"  CORNER EXCLUSION: old {corner_old:.3f} < 4.046 (the 1.2% squeeze);")
print(f"  re-priced {corner_new:.3f} > 4.046 -- THE EXCLUSION DISSOLVES.")
print("  The first-ever bottom-fiber constraint is superseded-not-erased.")
ok &= corner_old < 4.046 < corner_new

print("\nLEG 3 -- GRV-128 ceiling at the dynamical ratio (Branch MAX held)")
T0, af = 1.203e3, 2.214e-22
C = KF_DYN * 0.355**2 * 4.6593 / (4 * 1.25)
lam = C * T0 * af
a, c, G = 1e-16, 2.998e8, 6.674e-11
mu = T0 / c**2
Lam = (1 / (a * mu**2 * c**3)) * lam * c**3 / (2 * G)
print(f"  C = 9 x 0.355^2 x 4.6593 / 5 = {C:.4f}   (v3.26.71: 0.9502 at 8.091)")
print(f"  lambda_strand <= {lam:.3e} J")
print(f"  Lambda_nat <= {Lam:.3e}   chi_required >= {1/Lam:.2e}")
print("  (x1.1123 on the SWEEP-TAU ceiling; linear-in-a_f gate unchanged)")
ok &= abs(Lam - 1.177e35) / 1.177e35 < 0.01

print("\nLEG 4 -- the floor and the cap, mapped not superseded")
print(f"  4.046 floor (quartic projection, DISTINCT object): SURVIVES, flagged;")
print(f"  via the dynamical mapping it reads k/T0 >= {(4.046+3)/6:.4f} -- satisfied.")
print(f"  positivity cap k/T0 < 3 (FND-126) reads k_f/T0_f < 15 -- read 9.008 inside.")
print(f"  dynamical read 9.008 >= 4.046: EM-RECON-032's falsifier NOT fired.")

print("\nLEG 5 -- KBSAT consequence, DISPLAYED NOT DECIDED")
print(f"  The grant saturated a ceiling of 0.126; the ceiling re-prices to {kb_stat:.3f}.")
print("  Condition 1 fires only on determinations BELOW the ceiling: NOT fired.")
print("  The extremal principle now points at 0.282, which BLOCH-L's anchors")
print("  make MORE infeasible (feasibility kb <= 0.079, conditional). The")
print("  grant's value question goes to the author's desk; nothing moved here.")

print("\nVERDICT:", "PASS -- re-pricing arithmetic verified" if ok else "FAILURE")
raise SystemExit(0 if ok else 1)
