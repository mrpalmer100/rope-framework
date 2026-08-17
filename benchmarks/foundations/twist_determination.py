"""COMMISSION TWIST (FND-131, 2026-08-17) -- the twist determination.

The registration GRV-072 named never-determined, executed at the FINE level
under FND-130's pre-registered one-number sheet (C omega = 0.7162 T0_f a_f
sends KBSAT to adjudication-on-numbers; anything else forces the dynamical
reading and fires FND-121 condition 1 with FND-128's reverting set).

Legs
  1  THE MODULUS: C determined from the granted rod class + the registered
     Poisson chain -- no invention.
  2  THE DENSITY: the two formation-topology readings of omega, both
     computed; Fuller's writhe verified by a Gauss-integral numeric control.
  3  THE EXCLUSION: the static requirement swept over the ENTIRE admissible
     (nu, kb, omega) box -- including corners the standing values do not
     occupy -- against every registered-reading twist.
  4  VERDICT per the FND-130 sheet.
Numbers of the reverting set attach at the consequence leg only.
"""
import numpy as np

ok = True
print("COMMISSION TWIST -- the fine twist channel, determined")

print("\nLEG 1 -- THE MODULUS")
print("  FND-118 grants a homogeneous elastic rod: k_f = E_f A, kb = E_f I,")
print("  ONE modulus. For a circular section J = 2I EXACTLY, so the torsional")
print("  stiffness is C = G_f J = [E_f/(2(1+nu))] 2I = kb/(1+nu).")
print("  The Poisson chain is REGISTERED: GRV-073 imports G ~ E/2.5")
print("  (nu = 0.25) with its weakest-link caveat ('a factor of a few, not")
print("  seven orders'); NUN-GRV21 carried the same chain at the fine level.")
print("      C = kb/(1+nu) = 0.8 kb        [nu = 0.25, registered chain]")
print("  THE MODULUS HALF OF GRV-072's GAP FILLS AT THE FINE LEVEL: not an")
print("  invention -- the granted class plus a registered import.")

print("\nLEG 2 -- THE DENSITY: the two formation-topology readings")
# geometry, level 1, reading A
S1 = 1 / 3
c_ax = np.sqrt(S1)                       # axial cosine = sin psi_1
kap1 = 2 * np.pi * np.sqrt(S1 * (1 - S1))
tau1 = 2 * np.pi * S1
p = 1.0                                  # worst-case pitch a_f = 1
L_turn = 2 * np.pi / np.sqrt(kap1**2 + tau1**2)
print("  (a) WOUND-BORN / free twist: with twist unconstrained, minimizing")
print("      (1/2) C integral omega^2 ds at fixed centerline gives omega = 0")
print("      -- a THEOREM of the granted class, not a default.")
Wr_turn = 1 - c_ax                       # Fuller: writhe per turn = 1 - cos(alpha)
om_Lk = -2 * np.pi * Wr_turn / L_turn
print("  (b) STRAIGHT-BORN / Lk-conserving: a fibre formed straight and")
print("      untwisted (Lk = 0) then wound trades Tw = -Wr (the corpus's own")
print("      Calugareanu ledger, FND-STRAND-003). Fuller: Wr/turn = 1 - cos")
print(f"      alpha = {Wr_turn:.4f}; L_turn = {L_turn:.4f} a_f;")
print(f"      omega_Lk = -2 pi Wr/L = {om_Lk:.4f} / a_f  (sign OPPOSITE the")
print("      winding's handedness).")

# NUMERIC CONTROL: Gauss-integral writhe of a slender closed helical torus
def gauss_writhe(n_turns=30, aspect=60.0, M=6000):
    alpha = np.arccos(c_ax)
    # helical torus: big circle radius A, small radius r, n turns
    r_small = 1.0
    A = aspect * r_small
    th = np.linspace(0, 2 * np.pi, M, endpoint=False)
    ph = n_turns * th
    # pitch angle on the torus ~ alpha: choose r/velocity ratio to match
    # tangent axial cosine: local axis = big-circle direction; set r so that
    # cos(angle to local axis) = c_ax:  tan(alpha) = (r * n)/A
    r_small = A * np.tan(alpha) / n_turns
    x = (A + r_small * np.cos(ph)) * np.cos(th)
    y = (A + r_small * np.cos(ph)) * np.sin(th)
    z = r_small * np.sin(ph)
    r = np.stack([x, y, z], 1)
    d = np.roll(r, -1, 0) - r
    # discrete Gauss double sum
    Wr = 0.0
    for i in range(M):
        rij = r - r[i]
        cross = np.cross(d[i], d)
        num = np.einsum('ij,ij->i', cross, rij)
        dist = np.linalg.norm(rij, axis=1)
        mask = dist > 1e-9
        Wr += np.sum(num[mask] / dist[mask]**3)
    return Wr / (4 * np.pi) / n_turns

Wr_num = gauss_writhe()
err = abs(Wr_num - Wr_turn) / Wr_turn
print(f"  NUMERIC CONTROL (Gauss double integral, slender helical torus):")
print(f"      Wr/turn = {Wr_num:.4f} vs Fuller {Wr_turn:.4f}  ({err*100:.2f}%)"
      f"  [{'PASS' if err < 0.05 else 'FAIL'}]")
ok &= err < 0.05

print("\nLEG 3 -- THE EXCLUSION, swept over the ENTIRE admissible box")
T_f = 1.5
om_req = lambda nu, kb: (T_f / tau1) * (1 + nu) / kb
print("  Static requirement (FND-130): C omega = T_fibre/tau_1, i.e.")
print("      omega_req = (T_fibre/tau_1)(1 + nu)/kb.")
print("  Admissible box, every edge a registered ceiling or physical bound:")
print("    nu in [0, 0.5]; kb <= 0.282 T0_f a_f^2 (the LOOSEST standing")
print("    ceiling, FND-127); |omega| <= tau_1 = 2.0944/a_f (the Frenet-")
print("    locked rate, the maximum any bend-following material frame")
print("    carries -- itself above both registered readings).")
corner = om_req(0.0, 0.282)
standing = om_req(0.25, 0.126)
print(f"  requirement at the MOST FAVOURABLE corner (nu = 0, kb = 0.282):")
print(f"      omega_req = {corner:.4f}/a_f  vs ceiling {tau1:.4f}  "
      f"(margin {corner/tau1:.2f}x)")
print(f"  requirement at the standing values (nu = 0.25, kb <= 0.126):")
print(f"      omega_req >= {standing:.4f}/a_f  vs the Lk reading "
      f"{abs(om_Lk):.4f}  (margin {standing/abs(om_Lk):.1f}x, and the sign")
print("      is wrong besides; the free-twist reading gives zero).")
ok &= corner > tau1 and standing > abs(om_Lk)
print("  **THE STATIC BRANCH IS UNREACHABLE**: for every kb inside every")
print("  standing ceiling and every physical nu, the required twist density")
print("  exceeds the maximum any registered or formation-topology reading")
print("  can supply -- by 1.2x at the most favourable corner the corpus does")
print("  not occupy, and by 4.6x at the values it does. The determination is")
print("  therefore ROBUST: C omega != 0.7162 T0_f a_f on every reading.")
print("  [Chirality note: reading (b)'s per-fibre omega is signed opposite")
print("  each fibre's own handedness -- parity-EVEN in the mesh mean, so")
print("  GRV-113's chi <= 2.5e-19 cap is not implicated either way.]")

print("\nLEG 4 -- VERDICT, per FND-130's pre-registered sheet")
print("  C omega != 0.7162 T0_f a_f, DETERMINED. THE DYNAMICAL READING IS")
print("  FORCED, NOT ADOPTED: the winding is a rotating-wave state (v_1 =")
print("  sqrt(3/2) c exactly, FND-130 leg 4). Per the sheet and per FND-121")
print("  condition 1's own text, THE TRIPWIRE FIRES ON THIS RELEASE:")
print("  KBSAT auto-supersedes; kb reverts to bound status; the reverting")
print("  set executes verbatim (consequence leg).")

print("\nCONSEQUENCE LEG -- the reverting set (FND-128, executed)")
kb_b = 0.07909
print(f"  kb <= {kb_b:.5f} T0_f a_f^2  [BLOCH-L's feasibility, converting to")
print("      the standing bound: the contact pre-stress class is empty")
print("      (GRANT-CONTACT) and the twist channel is now determined; the")
print("      NAMED residual gap is the dynamical-background correction --")
print("      the anchor solve was run on a static winding, and the")
print("      rotating-wave background's second-order corrections are")
print("      unpriced. Bound-with-named-gap, the corpus's standard class.]")
print(f"  r_s <= {2*np.sqrt(kb_b/9.00823):.4f} a_f     (rod identity at the dynamical k_f)")
print(f"  (G I_p)_f <= {4*kb_b/5:.4f} T0_f a_f^2   (was the KBSAT value 0.1008)")
sc = kb_b / 0.126
print(f"  FND-122 dividend -> <= {0.4697*sc:.4f} T0 a_f; Lambda ceiling")
print(f"      5.2e34 -> {5.2e34*sc:.1e}; chi_required >= {1.9e-35/sc:.1e}")
print("  GRV-128's k_f-built chain: UNCHANGED at 1.18e35.")
print("  Every remaining KBSAT-conditional display reverts to bound form.")

print("\nVERDICT:", "DYNAMICAL-FORCED -- condition 1 fires; the winding is a wave"
      if ok else "INSTRUMENT FAILURE")
raise SystemExit(0 if ok else 1)
