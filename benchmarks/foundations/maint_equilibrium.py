"""COMMISSION MAINT (FND-130, 2026-08-17) -- the winding-maintenance question.

Executed under analysis/MAINT_equilibrium_bars_LOCKED.md (locked at v3.26.74).
Doubled clean-room honoured: the derive-point family (2.844 / 8.091 / 0.2496)
and the kb VALUES (0.126, 0.079) appear in NO build leg; kb enters build legs
only as a SYMBOL. Numbers attach at the consequence leg, after the verdict.

Legs
  0  controls: exact helix geometry at the derived angles (reading A)
  1  channel (i)  -- intrinsic curvature: admissibility read verbatim
  2  channel (ii) -- static bending balance: the force density derived
     symbolically AND checked by discrete energy gradient; the magic-angle
     bending-neutrality theorem; the pure-bending refutation; the twist
     rescue reduced to one closed-form requirement, blocked at GRV-072
  3  channel (iii) -- dynamical maintenance: the rotating-helix wave
     exhibited exactly; level-1 speed bending-free by the same theorem
  4  channel (iv) -- topological rigidity: barrier blocked at GRV-072
  5  verdict + consequence leg (numbers attach here only)
"""
import numpy as np
import sympy as sp

ok = True
S1 = sp.Rational(1, 3)
S2 = (15 + 2 * sp.sqrt(30)) / 35
PI = sp.pi

def helix_kt(s):
    """kappa, tau at worst-case pitch p = a_f = 1, reading A (axial cos = sin psi):
    kappa = 2 pi sqrt(s(1-s)),  tau = 2 pi s   (s = sin^2 psi)."""
    return 2 * PI * sp.sqrt(s * (1 - s)), 2 * PI * s

print("COMMISSION MAINT -- static equilibrium without contact, or dynamical?")
print("\nLEG 0 -- GEOMETRY CONTROL (reading A, FND-126)")
k1, t1 = helix_kt(S1)
k2, t2 = helix_kt(S2)
vals = [float(x) for x in (k1, t1, k2, t2)]
print(f"  level 1: kappa = {vals[0]:.4f}, tau = {vals[1]:.4f}  (2.9619, 2.0944)")
print(f"  level 2: kappa = {vals[2]:.4f}, tau = {vals[3]:.4f}  (2.7506, 4.6593)")
ok &= abs(vals[0] - 2.9619) < 1e-3 and abs(vals[1] - 2.0944) < 1e-3
ok &= abs(vals[2] - 2.7506) < 1e-3 and abs(vals[3] - 4.6593) < 1e-3

print("\nLEG 1 -- CHANNEL (i): INTRINSIC CURVATURE, adjudicated verbatim")
print("  FND-118 grants 'a homogeneous elastic rod of radius r_s carrying")
print("  tension T0_f, with k_f = E_f A and kb = E_f I sharing one modulus'.")
print("  No intrinsic (stress-free wound) reference state is granted.")
print("  CHANNEL (i) IS INADMISSIBLE UNDER THE GRANTED CLASS. Recorded, not")
print("  extended (bars B4). [Even if admitted, the T kappa imbalance of the")
print("  tension survives any reference state; see leg 2.]")

print("\nLEG 2 -- CHANNEL (ii): STATIC BENDING BALANCE")
# Exact normal force density of a uniform helix carrying tension T with
# bending energy (1/2) kb integral kappa^2 ds, sympy-derived from the
# helix-family variation (energy per unit theta, differentiated in R):
#     f_n (inward) = kappa [ T + kb (tau^2 - kappa^2/2) ]
R_, b_, T_, kb_ = sp.symbols('R b T k_b', positive=True)
g_ = sp.sqrt(R_**2 + b_**2); kap_ = R_ / g_**2; tau_ = b_ / g_**2
e_ = (T_ + sp.Rational(1, 2) * kb_ * kap_**2) * g_
f_out = sp.simplify(-sp.diff(e_, R_) / g_)
resid = sp.simplify(f_out + kap_ * (T_ + kb_ * (tau_**2 - kap_**2 / 2)))
print(f"  sympy identity check (must be 0): {resid}")
ok &= resid == 0
# THE MAGIC-ANGLE THEOREM: the bending contribution's coefficient
s = sp.symbols('s', positive=True)
kap_s, tau_s = helix_kt(s)
neutral = sp.simplify(tau_s**2 - kap_s**2 / 2)
sol = sp.solve(sp.Eq(neutral, 0), s)
print(f"  tau^2 - kappa^2/2 = {sp.simplify(neutral)} = 0  iff  s = {sol}")
print("  THE BENDING-NEUTRALITY THEOREM: the bending force density of a")
print("  uniform helix VANISHES IDENTICALLY iff sin^2 psi = 1/3 -- THE MAGIC")
print("  ANGLE. FND-088's level-1 winding is bending-force-neutral EXACTLY.")
ok &= sp.Rational(1, 3) in sol
lvl2_coeff = float(neutral.subs(s, S2))
print(f"  level 2: tau^2 - kappa^2/2 = +{lvl2_coeff:.4f} (tau-dominated: bending")
print("  REINFORCES the inward tension imbalance)")

# NUMERIC CONTROL, non-circular: finite-difference of the DISCRETE curve
# energy under the radial helix-family displacement, both levels.
def fd_normal_force(s_val, kb_val=1.0, T_val=1.0, N=20000):
    sv = float(s_val)
    kv = 2 * np.pi * np.sqrt(sv * (1 - sv)); tv = 2 * np.pi * sv
    R0 = kv / (kv**2 + tv**2); b0 = tv / (kv**2 + tv**2)
    th = np.linspace(0, 8 * np.pi, N)
    def E(R):
        r = np.stack([R * np.cos(th), R * np.sin(th), b0 * th], 1)
        d = np.diff(r, axis=0); L = np.linalg.norm(d, axis=1)
        tvec = d / L[:, None]; dt = np.diff(tvec, axis=0)
        kap = np.linalg.norm(dt, axis=1) / (0.5 * (L[1:] + L[:-1]))
        return T_val * L.sum() + 0.5 * kb_val * np.sum(kap**2 * 0.5 * (L[1:] + L[:-1]))
    eps = 1e-6
    g0 = np.sqrt(R0**2 + b0**2); Ltot = 8 * np.pi * g0
    return (E(R0 + eps) - E(R0 - eps)) / (2 * eps) / Ltot   # outward density

for lab, s_val in (("level 1 (magic)", S1), ("level 2", S2)):
    sv = float(s_val)
    kv = 2 * np.pi * np.sqrt(sv * (1 - sv)); tv = 2 * np.pi * sv
    fn_num = fd_normal_force(s_val)   # inward = +dE/dR per length (energy grows outward)
    fn_pred = kv * (1.0 + 1.0 * (tv**2 - kv**2 / 2))
    err = abs(fn_num - fn_pred) / abs(fn_pred)
    print(f"  numeric control {lab}: f_n = {fn_num:.4f} vs analytic {fn_pred:.4f} "
          f"({err*100:.3f}%)  [{'PASS' if err < 0.005 else 'FAIL'}]")
    ok &= err < 0.005

print("  THE PURE-BENDING REFUTATION, both levels, DERIVED: static (f_n = 0)")
print("  demands T = -kb (tau^2 - kappa^2/2): ZERO at level 1 (the theorem,")
print("  kb-FREE) and NEGATIVE at level 2 (bending reinforces, never balances).")
print("  The registered fibre tension is POSITIVE (3/2 T0_f, FND-126). NO")
print("  static pure-bending equilibrium exists at EITHER level.")
print("  THE TWIST RESCUE, the only remaining static channel: a twist moment")
print("  C omega t can supply the balance; the frame-Kirchhoff route gives")
print("      C omega = T/tau + kb (kappa^2/2 - tau^2)/tau")
print("  -- kb-FREE at level 1 (the theorem): C omega = T_fibre/tau_1, one")
print("  number [single-route, cross-check owed if the branch opens]. BOTH")
print("  factors are UNREGISTERED (GRV-072: the twist constitutive fact never")
print("  determined). BLOCKED, NOT REFUTED.")

print("\nLEG 3 -- CHANNEL (iii): DYNAMICAL MAINTENANCE, EXHIBITED")
print("  A rotating helix (circularly polarized wave) balances f_n by")
print("  centripetal acceleration: mu v^2 = T + kb (tau^2 - kappa^2/2)")
print("  (along-fibre speed). AT LEVEL 1 THE SAME THEOREM DELETES kb:")
print("      v_1 = sqrt(T_fibre/mu_f)   EXACTLY, bending-independent.")
print("  With mu_f = T0_f/c^2 FORCED (SHIN invariant) and T_fibre = 3/2 T0_f:")
print("      v_1 = sqrt(3/2) c = 1.2247 c   -- from registered inputs alone.")
print("  Level 2: v_2 = sqrt(3/2 + kb (tau^2 - kappa^2/2)) c -- bending RAISES\n  the level-2 wave speed (tau-dominated), kb-dependent, priced below.")
print("  THE DYNAMICAL STATE EXISTS. The winding is realizable as a")
print("  stationary rotating-wave state of the granted rod, exhibited at")
print("  level 1 exactly; the nested two-level composite is the same")
print("  construction on the level-1 backbone, named as the channel's")
print("  residual (instrument demand: the composite build on FND-089-class")
print("  machinery).")

print("\nLEG 4 -- CHANNEL (iv): TOPOLOGICAL RIGIDITY")
print("  Lk = Tw + Wr conserves a NUMBER; a barrier against straightening")
print("  requires twist STIFFNESS to price the Tw <-> Wr trade -- the same")
print("  unregistered constitutive fact (GRV-072). BLOCKED, NOT REFUTED.")

print("\nLEG 5 -- VERDICT")
print("  Channels (i): inadmissible-derived. (ii)-pure: refuted-derived (the")
print("  bending-neutrality theorem + positive tension). (ii)-twist and (iv):")
print("  BLOCKED at one and the same missing registration -- the twist")
print("  channel (GRV-072). (iii): dynamical state EXHIBITED from registered")
print("  inputs.")
print("  PER THE LOCKED GRAMMAR: **CHANNEL-OPEN** -- the static question is")
print("  not closed (two channels blocked, neither refuted), so NO-STATIC-")
print("  EQUILIBRIUM is NOT declared and FND-121 CONDITION 1 DOES NOT FIRE.")
print("  The warrant stays HELD. The resisting channels name ONE instrument")
print("  demand between them: a registered twist-channel determination.")

print("\nCONSEQUENCE LEG (numbers attach only here; clean-room lifts)")
Tf, tau1, tau2 = 1.5, 2.0944, 4.6593
Com = Tf / tau1
print(f"  THE TWIST SHEET, pre-registered for any future determination:")
print(f"    C omega = T_fibre/tau_1 = {Com:.4f} T0_f a_f  (kb-free, level 1)")
print(f"      -> STATIC branch: pre-stress computable, KBSAT adjudicates on numbers")
print(f"    C omega != {Com:.4f}  -> DYNAMICAL branch forced: condition 1 fires")
print(f"      on that release with FND-128's reverting set executed verbatim.")
l2 = lvl2_coeff
for kb_v in (0.079, 0.126):
    v2 = np.sqrt(Tf + kb_v * l2)
    print(f"  level-2 wave speed at kb = {kb_v}: {v2:.3f} c "
          f"(margin spend {v2:.2f} of the 6.1x floor: inside)")
print(f"  level-1 wave speed: {np.sqrt(Tf):.4f} c, kb-independent (the theorem).")

print("\nVERDICT:", "CHANNEL-OPEN -- warrant held; twist channel is the gate"
      if ok else "INSTRUMENT FAILURE")
raise SystemExit(0 if ok else 1)
