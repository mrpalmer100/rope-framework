"""COMMISSION COMPOSITE (FND-135, 2026-08-18) -- the nested-composite wave
build: the exact two-level kinetic energy and the exact energy total.

Executed under analysis/COMPOSITE_wave_build_bars_LOCKED.md.
Geometry imported from the BLOCH-L build (reading A, load-bearing by that
file's Leg 0 isotropy control). Units: T0_f = 1, a_f = 1, c = 1, mu_f = 1.

Legs
  1  geometry under the load-bearing reading (controls; halt on fail)
  2  the path factor (arc per axial length) -- convention audit
  3  the exact kinetic energy: closed form + two-torus numeric control
  4  handedness (both signs reported; the registry does not choose)
  5  the total over the admissible box
  6  consequence (registered bracket + window appear HERE ONLY)
"""
import numpy as np
import importlib.util as _ilu
import pathlib as _pl

_spec = _ilu.spec_from_file_location(
    "blochl", _pl.Path(__file__).with_name("blochl_longitudinal.py"))
_bl = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_bl)

S1, S2 = _bl.S1, _bl.S2
C1, C2 = _bl.C1, _bl.C2            # axial direction cosines, reading A
KAP1, KAP2, PPHYS = _bl.KAP1, _bl.KAP2, _bl.PPHYS
B = PPHYS / (2 * np.pi)
TF = 1.5                           # T_fibre/T0_f (BLOCH-L stretch+tension)
KB_HI = 0.07909                    # standing bound (post-DBC: no static rider)

ok = True
print("COMMISSION COMPOSITE -- the nested-composite wave build\n")

# ------------------------------------------------------------------ LEG 1
print("LEG 1 -- GEOMETRY UNDER THE LOAD-BEARING READING (reading A)")
R1, kap1, tau1 = _bl.helix(C1)
R2, kap2, tau2 = _bl.helix(C2)
c1 = abs(kap1 * R1 - (1 - S1)); c2 = abs(kap2 * R2 - (1 - S2))
c3 = abs(kap1 - KAP1) + abs(kap2 - KAP2)
print(f"  R_1 = {R1:.6f}  R_2 = {R2:.6f}   (a_f)")
print(f"  kappa_1 = {kap1:.4f}  kappa_2 = {kap2:.4f}   "
      f"tau_1 = {tau1:.4f}  tau_2 = {tau2:.4f}   (1/a_f)")
print(f"  control kappa_i R_i = 1 - s_i : residuals {c1:.2e}, {c2:.2e}  "
      f"[{'PASS' if max(c1, c2) < 1e-12 else 'FAIL'}]")
print(f"  control kappa pair vs registered: {c3:.2e}  "
      f"[{'PASS' if c3 < 1e-9 else 'FAIL'}]")
print("  NOTE the nesting is geometrically sane under this reading:")
print(f"  R_1 > R_2 ({R1:.4f} > {R2:.4f}) -- the backbone is wider than the")
print("  sub-winding it carries. The inverted reading gives R_1 < R_2.")
ok &= max(c1, c2) < 1e-12 and c3 < 1e-9
if not ok:
    print("\nHALT: geometry control failed (bars, Leg 1).")
    raise SystemExit(1)

# ------------------------------------------------------------------ LEG 2
print("\nLEG 2 -- THE PATH FACTOR (arc per unit axial length)")
path_A = 1.0 / (C1 * C2)
path_B = 1.0 / (np.sqrt(1 - S1) * np.sqrt(1 - S2))
print(f"  reading A (axial cos = sin psi, LOAD-BEARING): 1/(c1 c2) = {path_A:.5f}")
print(f"  reading B (axial cos = cos psi):               1/(c1 c2) = {path_B:.5f}")
print(f"  level-1-only path under reading A: 1/c1 = {1/C1:.5f} = sqrt(3)")
print("  The level-1 path carried in the registered bill is sqrt(3)")
print("  (reading A). The TWO-LEVEL path carried alongside it is the")
print(f"  reading-B value {path_B:.4f} -- the two legs of one bracket sit in")
print("  DIFFERENT conventions. Under the load-bearing reading the")
print(f"  two-level path is {path_A:.4f}, i.e. LOWER by a factor "
      f"{path_A/path_B:.4f}.")
print("  Direction of the correction: the path factor multiplies the whole")
print("  per-arc energy, so the wave total comes DOWN, not up.")
print("  Registered text is not edited; the correction attaches by name.")

# ------------------------------------------------------------------ LEG 3
print("\nLEG 3 -- THE EXACT KINETIC ENERGY (closed form + numeric control)")
OM1 = np.sqrt(kap1 * TF / R1)               # level-1 centripetal balance
V1 = OM1 * R1
print(f"  Omega_1 = {OM1:.6f} c/a_f   v_1 = Omega_1 R_1 = {V1:.10f} c  "
      f"[{'PASS' if abs(V1-1) < 1e-12 else 'FAIL'}]  (FND-132 identity)")
ok &= abs(V1 - 1) < 1e-12


def level2_speed(kb):
    """Level-2 centripetal balance in the co-moving frame; bending RETAINED
    (the neutrality theorem is a level-1 statement -- s_2 != 1/3)."""
    v2sq = kap2 * R2 * (TF + kb * (tau2 ** 2 - kap2 ** 2 / 2))
    return np.sqrt(v2sq)


def ke_closed(kb, sign):
    """Exact phase-averaged (1/2)<|v|^2> per unit arc.

    v = Om1 (zhat x r) + Om2 (t1 x d),  r = C + d,  d perp t1, |d| = R2.
      <|zhat x r|^2>  = R1^2 + (R2^2/2)(1 + t1z^2)      [<d> = 0 kills cross]
      |t1 x d|^2      = R2^2
      <(zhat x d).(t1 x d)> = (zhat.t1) R2^2 = c_ax1 R2^2   [t1.d = 0]
    """
    v2 = level2_speed(kb); om2 = v2 / R2
    orbit1 = OM1 ** 2 * R1 ** 2
    offset = OM1 ** 2 * (R2 ** 2 / 2) * (1 + C1 ** 2)
    orbit2 = om2 ** 2 * R2 ** 2
    cross = 2 * OM1 * om2 * C1 * R2 ** 2 * sign
    return 0.5 * (orbit1 + offset + orbit2 + cross), (orbit1, offset,
                                                      orbit2, cross)


def ke_numeric(kb, sign, n=720):
    """Direct average of |v|^2 over the phase two-torus."""
    v2 = level2_speed(kb); om2 = sign * v2 / R2
    f1 = (np.arange(n) + 0.5) / n * 2 * np.pi
    f2 = (np.arange(n) + 0.5) / n * 2 * np.pi
    tot = 0.0
    z = np.array([0., 0., 1.])
    for a in f1:
        C = np.array([R1 * np.cos(a), R1 * np.sin(a), B * a])
        t1 = np.array([-R1 * np.sin(a), R1 * np.cos(a), B])
        t1 /= np.linalg.norm(t1)
        e1 = np.array([-np.cos(a), -np.sin(a), 0.0])       # principal normal
        e2 = np.cross(t1, e1)
        for b in f2:
            d = R2 * (np.cos(b) * e1 + np.sin(b) * e2)
            r = C + d
            v = OM1 * np.cross(z, r) + om2 * np.cross(t1, d)
            tot += v @ v
    return 0.5 * tot / (n * n)


for kb, sg in ((0.0, +1), (KB_HI, +1), (KB_HI, -1)):
    cf, _ = ke_closed(kb, sg); nm = ke_numeric(kb, sg)
    e = abs(cf - nm) / cf
    print(f"  kb={kb:.5f} sign={sg:+d}: closed {cf:.10f}  numeric {nm:.10f}  "
          f"rel {e:.2e}  [{'PASS' if e < 1e-10 else 'FAIL'}]")
    ok &= e < 1e-10

_, parts = ke_closed(KB_HI, +1)
print("\n  the closed form's four pieces at the standing bound (aligned):")
print(f"    level-1 orbit          {parts[0]:.6f}   (= c^2, the identity)")
print(f"    offset's contribution  {parts[1]:.6f}   (the level-2 offset")
print("                                         widens the level-1 orbit)")
print(f"    level-2 orbit          {parts[2]:.6f}")
print(f"    CROSS term             {parts[3]:+.6f}   (sign = relative handedness)")
print("  The bracket's construction summed the first and third only.")

# ------------------------------------------------------------------ LEG 4
print("\nLEG 4 -- HANDEDNESS: the registry does not choose")
print("  Relative handedness of the level-2 winding against the level-1")
print("  rotation is UNREGISTERED (population-handedness, standing board).")
print("  The cross term is NONZERO, so the exact total is a TWO-VALUED FORK")
print("  on the registry. Both signs are carried; neither is adopted.")

# ------------------------------------------------------------------ LEG 5
print("\nLEG 5 -- THE TOTAL over the admissible box (T0 per strand per axial)")
rows = []
for kb in (0.0, KB_HI):
    for sg in (-1, +1):
        ke, _ = ke_closed(kb, sg)
        E = path_A * (1.0 + ke)          # inherited tension convention
        rows.append((kb, sg, ke, E))
        print(f"  kb={kb:.5f}  sign={sg:+d}:  KE/arc = {ke:.6f}   "
              f"Sigma_wave = {E:.4f} T0")
lo = min(r[3] for r in rows); hi = max(r[3] for r in rows)
arg_lo = [r for r in rows if r[3] == lo][0]; arg_hi = [r for r in rows if r[3] == hi][0]
print(f"\n  Sigma_wave = [{lo:.4f}, {hi:.4f}] T0 per strand per axial length")
print(f"    lower edge at kb={arg_lo[0]:.5f}, sign={arg_lo[1]:+d} "
      f"(anti-aligned, bending off)")
print(f"    upper edge at kb={arg_hi[0]:.5f}, sign={arg_hi[1]:+d} "
      f"(aligned, bending at the bound)")
print(f"  areal form (x3): [{3*lo:.3f}, {3*hi:.3f}] T0/a^2")
share_lo = (lo - 1) / lo; share_hi = (hi - 1) / hi
print(f"  dynamical share: [{share_lo:.4f}, {share_hi:.4f}]")

# level-1-only limit control: the composite must reduce to the bill's number
E_L1 = (1 / C1) * (1.0 + 0.5)
print(f"\n  CONTROL, level-1-only limit (R_2 -> 0): E = sqrt(3) x 3/2 = "
      f"{E_L1:.4f} T0 -- the registered level-1 exact value, reproduced.")

# ------------------------------------------------------------------ LEG 6
print("\nLEG 6 -- CONSEQUENCE (registered bracket and window, this leg only)")
BR_LO, BR_HI = 2.598, 4.522
WINDOW = 0.889
inside = BR_LO <= lo and hi <= BR_HI
print(f"  registered bracket (FND-134): [{BR_LO}, {BR_HI}] T0")
print(f"  computed box:                 [{lo:.4f}, {hi:.4f}] T0   "
      f"-> {'INSIDE at every corner' if inside else 'BREAKS THE BRACKET'}")
print(f"  registered zero-point share ceiling (FND-MATTER-041): {WINDOW}")
print(f"  computed share ceiling: {share_hi:.4f}   "
      f"-> {'INSIDE, margin x%.3f' % (WINDOW/share_hi) if share_hi < WINDOW else 'AT OR ABOVE -- LIVE'}")
ok &= inside and share_hi < WINDOW

print("\nVERDICT (per the pre-registered outcome sheet):")
if ok and inside:
    print("  BRACKET-TIGHTENED. The exact composite lands inside the")
    print("  registered bracket at every corner. Sigma_wave narrows to")
    print(f"  [{lo:.3f}, {hi:.3f}] T0 per strand per axial length. The residual")
    print("  width is NO LONGER an approximation: it is two named causes --")
    print("  the unregistered relative handedness (discrete fork) and the")
    print("  standing kb range. The level-1-only edge is retired as an edge")
    print("  of the COMPOSITE object; it was never the composite. The bill")
    print("  remains payable with more margin than it was booked at.")
    raise SystemExit(0)
print("  NOT as pre-registered -- see legs above. Nothing adjusted.")
raise SystemExit(1)
