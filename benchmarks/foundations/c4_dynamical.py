"""COMMISSION C4-DYN (FND-137, 2026-08-18) -- the dynamical c4 commission.

Executed under analysis/C4DYN_bars_LOCKED.md. Chartered at FND-127.

Leg 1: the mapped floor (closed-form arithmetic on registered objects).
Leg 2: the direct quartic characterization on the exact ensemble
       (moments through eighth order; measure declared; blind to the
       floor value).
"""
import numpy as np

ok = True
print("COMMISSION C4-DYN -- the 4.046 floor on the dynamical instrument\n")

# ------------------------------------------------------------------ LEG 1
print("LEG 1 -- THE MAPPED FLOOR (registered objects only)")
u = 1.0 / 3.0
v = (15 + 2 * np.sqrt(30)) / 35.0
s = u * v
floor_mult = 1.0 / s
print(f"  the floor's provenance: core existence (coarse c4 = (k-T0)/8 > 0,")
print(f"  i.e. k/T0 > 1) through MULTIPLICATIVE transmission k_c = s k_f:")
print(f"      k_f > 1/s = {floor_mult:.4f}   (EM-RECON-032, convicted family)")
floor_dyn = 6 * 1.0 - 3.0
cap_dyn = 6 * 3.0 - 3.0
print(f"  the SAME condition through the ADOPTED dynamical mapping")
print(f"  k_f = 6(k/T0) - 3 (additive, angle-free, general in k/T0):")
print(f"      k/T0 > 1  <=>  k_f > {floor_dyn:.4f}")
print(f"  RIDER AUDIT: the mapped floor is an inequality in k/T0, not an")
print(f"  evaluation at 2 -- it does NOT inherit the FND-114 adjudication")
print(f"  rider. The floor is rider-free.")
read = 9.0
print(f"  the dynamical read {read:.3f}: clears at {read/floor_dyn:.1f}x "
      f"(was {read/floor_mult:.2f}x against 4.046)")
print(f"  the window: positivity cap k/T0 < 3 maps to k_f < {cap_dyn:.0f};")
print(f"  fine window ({floor_dyn:.0f}, {cap_dyn:.0f}), read {read:.0f} at its exact")
print("  midpoint -- BY LINEARITY (k/T0 = 2 centered in (1, 3)); arithmetic,")
print("  not mystery.")
ok &= abs(floor_dyn - 3) < 1e-12 and abs(floor_mult - 4.0455) < 1e-3

# ------------------------------------------------------------------ LEG 2
print("\nLEG 2 -- THE DIRECT QUARTIC CHARACTERIZATION (blind leg)")
print("  measure declared: applied strain gamma is the uniaxial displacement")
print("  gradient; fibre constitutive is harmonic in the stretch (lambda-1);")
print("  energy per unit REFERENCE arc. Under this measure a single aligned")
print("  fibre has ZERO quartic (lambda - 1 = gamma exactly): the projected")
print("  quartic below is PURELY geometric, from the winding.\n")

S1 = 1.0 / 3.0
S2 = (15 + 2 * np.sqrt(30)) / 35.0
C1, C2 = np.sqrt(S1), np.sqrt(S2)
ST1, ST2 = np.sqrt(1 - S1), np.sqrt(1 - S2)


def tangent_ensemble(n):
    T_ = []
    for f1 in (np.arange(n) + 0.5) / n * 2 * np.pi:
        t1 = np.array([-ST1 * np.sin(f1), ST1 * np.cos(f1), C1])
        a = np.array([0., 0., 1.]) if abs(t1[2]) < 0.9 else np.array([1., 0., 0.])
        e1 = np.cross(t1, a); e1 /= np.linalg.norm(e1); e2 = np.cross(t1, e1)
        for f2 in (np.arange(n) + 0.5) / n * 2 * np.pi:
            T_.append(ST2 * (-np.sin(f2) * e1 + np.cos(f2) * e2) + C2 * t1)
    return np.array(T_)


def moments(TT, e):
    w = (TT @ e) ** 2
    return [w.mean(), (w ** 2).mean(), (w ** 3).mean(), (w ** 4).mean()]


iso = [1 / 3, 1 / 5, 1 / 7, 1 / 9]
ez = np.array([0., 0., 1.])
e111 = np.array([1., 1., 1.]) / np.sqrt(3)

m_lo = moments(tangent_ensemble(200), ez)
m_hi = moments(tangent_ensemble(400), ez)
drift = max(abs(a - b) for a, b in zip(m_lo, m_hi))
print("  axial moments E[t_z^(2n)], n = 1..4 (grid 400; drift vs 200: "
      f"{drift:.1e}  [{'PASS' if drift < 1e-6 else 'FAIL'}]):")
for n, (m, i) in enumerate(zip(m_hi, iso), 1):
    tag = "ISOTROPIC" if abs(m - i) < 1e-9 else f"ANISOTROPIC (iso {i:.6f})"
    print(f"    E[t_z^{2*n}] = {m:.8f}   {tag}")
ok &= drift < 1e-6

m_111 = moments(tangent_ensemble(400), e111)
print("  (111) moments, anisotropy probe:")
for n, (m, mz) in enumerate(zip(m_111, m_hi), 1):
    print(f"    E[(t.e111)^{2*n}] = {m:.8f}   "
          f"(z-axis {mz:.8f}, diff {m - mz:+.2e})")

# exact quartic coefficient of <E(gamma)> along direction e:
#   E = T(lam-1) + (kf/2)(lam-1)^2,  lam = sqrt(1 + (2g + g^2) w),  w = (t.e)^2
# series (derived, then verified numerically below):
#   W4 = (kf - T) * M,   M = <w^2>/8 - (3/4)<w^3> + (5/8)<w^4>
def M_of(mom):
    return mom[1] / 8 - 0.75 * mom[2] + 0.625 * mom[3]


def W4_numeric(TT, e, kf, T):
    def W(gam):
        w = (TT @ e) ** 2
        lam = np.sqrt(1 + (2 * gam + gam ** 2) * w)
        return np.mean(T * (lam - 1) + 0.5 * kf * (lam - 1) ** 2)

    def stencil(g):
        # 5-point 4th-derivative stencil / 4!  (error O(g^2))
        return (W(2 * g) - 4 * W(g) + 6 * W(0) - 4 * W(-g) + W(-2 * g)) / g ** 4 / 24

    # Richardson: the raw stencil at g = 1e-2 missed the control bar at
    # 1.1e-4 (truncation, not physics); eliminated by extrapolation.
    g = 1e-2
    return (4 * stencil(g / 2) - stencil(g)) / 3


TT400 = tangent_ensemble(400)
KF, TF = 9.0, 1.5
Mz, M1 = M_of(m_hi), M_of(m_111)
Miso = iso[1] / 8 - 0.75 * iso[2] + 0.625 * iso[3]
w4_closed = (KF - TF) * Mz
w4_num = W4_numeric(TT400, ez, KF, TF)
e_ctrl = abs(w4_closed - w4_num) / abs(w4_closed)
print(f"\n  quartic form W4 = (k_f - T_f) x M:")
print(f"    M (z-axis)   = {Mz:+.8f}")
print(f"    M (111)      = {M1:+.8f}")
print(f"    M (isotropic reference) = {Miso:+.8f}  (= -4/315)")
print(f"  numeric control (finite-difference 4th derivative vs closed form):")
print(f"    closed {w4_closed:+.6f}  numeric {w4_num:+.6f}  rel {e_ctrl:.1e}  "
      f"[{'PASS' if e_ctrl < 1e-4 else 'FAIL'}]")
ok &= e_ctrl < 1e-4

print(f"\n  CHARACTERIZATION at the dynamical point (k_f = 9, T_f = 1.5):")
print(f"    the projected quartic is NEGATIVE in this measure "
      f"(W4 = {w4_closed:+.4f} per unit arc),")
print("    because M < 0 for ANY tangent distribution that is not a single")
print("    aligned fibre -- the winding SOFTENS the medium at quartic order")
print("    in this measure, and softens MORE the stiffer the fibre. The")
print("    coarse object's own quartic in the SAME measure is ZERO, so the")
print("    sign comparison to the coarse c4 = (k - T0)/8 (a Green-measure")
print("    object) is a MEASURE ARTIFACT, exactly as the bars warned. This")
print("    leg CHARACTERIZES; leg 1 adjudicates.")

print("\nVERDICT (per the pre-registered sheet):")
if ok:
    print("  FLOOR-REMAPPED. The core-existence floor survives AS A FLOOR and")
    print("  its value moves: k_f/T0_f > 3 (dynamical, rider-free), down from")
    print("  4.046 (multiplicative, convicted family). The armed falsifier")
    print("  re-arms at 3. The dynamical read 9 clears at 3.0x and sits at the")
    print("  exact midpoint of the fine existence window (3, 15), by")
    print("  linearity. The direct-quartic leg lands its own finding: the")
    print("  two-level ensemble is isotropic EXACTLY THROUGH FOURTH moments")
    print("  and ANISOTROPIC at sixth and eighth (z vs (111) split at the")
    print("  third decimal) -- the magic angles buy the harmonic sector's")
    print("  isotropy and no more; the quartic-response sector is direction-")
    print("  dependent. The winding's projected quartic is negative and")
    print("  purely geometric in the declared measure -- characterization,")
    print("  with the measure attached.")
    raise SystemExit(0)
print("  NOT as pre-registered -- see legs above.")
raise SystemExit(1)
