"""COMMISSION ANSATZ (FND-138, 2026-08-18) -- the composite-state
self-consistency test. Executed under
analysis/ANSATZ_selfconsistency_bars_LOCKED.md.

The stated motion (FND-135's ansatz):
    Cdot = Om1 (z x C),   ddot = Om1 (z x d) + s Om2 (t1 x d),
    t1dot = Om1 (z x t1)
Exact acceleration (one more derivative):
    rddot = Om1^2 z x (z x r)
          + s Om1 Om2 [ z x (t1 x d) + (z x t1) x d + t1 x (z x d) ]
          + Om2^2 t1 x (t1 x d)
Force at kb = 0: T times the arclength derivative of the unit tangent.
Units: T0_f = a_f = c = mu_f = 1. Clean test at kb = 0 (bars scope).
"""
import numpy as np

S1 = 1.0 / 3.0
S2 = (15 + 2 * np.sqrt(30)) / 35.0
C1, C2 = np.sqrt(S1), np.sqrt(S2)
ST1, ST2 = np.sqrt(1 - S1), np.sqrt(1 - S2)
B = 1.0 / (2 * np.pi)
TF = 1.5

R1 = B * np.sqrt(1 / C1 ** 2 - 1)
R2 = B * np.sqrt(1 / C2 ** 2 - 1)
KAP1 = 2 * np.pi * C1 * ST1
KAP2 = 2 * np.pi * C2 * ST2
OM1 = np.sqrt(KAP1 * TF / R1)
V2 = np.sqrt(KAP2 * R2 * TF)          # build's level-2 speed at kb = 0
OM2 = V2 / R2

Z = np.array([0., 0., 1.])


def frame(a):
    C = np.array([R1 * np.cos(a), R1 * np.sin(a), B * a])
    t1 = np.array([-R1 * np.sin(a), R1 * np.cos(a), B])
    t1 /= np.linalg.norm(t1)
    e1 = np.array([-np.cos(a), -np.sin(a), 0.0])
    e2 = np.cross(t1, e1)
    return C, t1, e1, e2


def pos(a, b):
    C, t1, e1, e2 = frame(a)
    return C + R2 * (np.cos(b) * e1 + np.sin(b) * e2)


def tang(a, b):
    _, t1, e1, e2 = frame(a)
    return ST2 * (-np.sin(b) * e1 + np.cos(b) * e2) + C2 * t1


def kcomp(a, b):
    _, t1, e1, e2 = frame(a)
    k1v = KAP1 * np.array([-np.cos(a), -np.sin(a), 0.0])
    return k1v + KAP2 * (-np.cos(b) * e1 - np.sin(b) * e2)


def vel(a, b, sg, om2=OM2):
    C, t1, e1, e2 = frame(a)
    d = R2 * (np.cos(b) * e1 + np.sin(b) * e2)
    return OM1 * np.cross(Z, C + d) + sg * om2 * np.cross(t1, d)


def acc(a, b, sg, om2=OM2):
    C, t1, e1, e2 = frame(a)
    d = R2 * (np.cos(b) * e1 + np.sin(b) * e2)
    r = C + d
    a1 = OM1 ** 2 * np.cross(Z, np.cross(Z, r))
    ax = sg * OM1 * om2 * (np.cross(Z, np.cross(t1, d))
                           + np.cross(np.cross(Z, t1), d)
                           + np.cross(t1, np.cross(Z, d)))
    a2 = om2 ** 2 * np.cross(t1, np.cross(t1, d))
    return a1 + ax + a2


H = 1e-5


def Ds(f, a, b, *args):
    """Arclength derivative along the fibre through (a, b)."""
    # fibre direction in (a,b): solve [dR/da, dR/db] (da,db) = t, then
    # normalize by |dR/ds| = 1.
    Ra = (pos(a + H, b) - pos(a - H, b)) / (2 * H)
    Rb = (pos(a, b + H) - pos(a, b - H)) / (2 * H)
    Mmat = np.stack([Ra, Rb], 1)
    t = tang(a, b)
    coef, res, *_ = np.linalg.lstsq(Mmat, t, rcond=None)
    resid = np.linalg.norm(Mmat @ coef - t)
    da, db = coef
    fa = (f(a + H, b, *args) - f(a - H, b, *args)) / (2 * H)
    fb = (f(a, b + H, *args) - f(a, b - H, *args)) / (2 * H)
    return da * fa + db * fb, resid


ok = True
print("COMMISSION ANSATZ -- self-consistency of the composite wave state\n")

# ------------------------------------------------------------------ LEG 1
print("LEG 1 -- SURFACE CONTROLS")
# (a) level-1 limit
res_l1 = np.linalg.norm(OM1 ** 2 * np.cross(Z, np.cross(Z, frame(0.7)[0]))
                        - TF * KAP1 * np.array([-np.cos(0.7), -np.sin(0.7), 0]))
print(f"  (a) level-1 limit balance residual: {res_l1:.2e}  "
      f"[{'PASS' if res_l1 < 1e-10 else 'HALT'}]")
ok &= res_l1 < 1e-10
# (b) tangent-in-span + curvature reproduction
rng = np.random.default_rng(5)
span_max, curv_max = 0.0, 0.0
for a, b in rng.uniform(0, 2 * np.pi, (40, 2)):
    dt, resid = Ds(tang, a, b)
    span_max = max(span_max, resid)
    curv_max = max(curv_max, np.linalg.norm(dt - kcomp(a, b)))
print(f"  (b) tangent-in-span residual max: {span_max:.2e}  "
      f"[{'PASS' if span_max < 1e-8 else 'FAIL'}]")
print(f"      D_s(tangent) vs registered composite curvature, max: "
      f"{curv_max:.2e}  [{'PASS' if curv_max < 1e-6 else 'FAIL'}]")
ok &= span_max < 1e-8 and curv_max < 1e-6
if not ok:
    print("\nHALT: surface control (b2) failed (bars, leg 1). DIAGNOSTIC:")
    print("  The tangent-in-span control PASSED (2e-11): the operator is")
    print("  validated. The failing object is the REGISTERED curvature.")
    # empirical decomposition, no hypothesis: along the fibre,
    #   D_s t = (da/ds) da_t + (db/ds) db_t   (chain rule),
    # and the registered K = k1(a) + kappa_2 u_n(b). Compare piecewise.
    gap_max = 0.0
    d_apiece, d_bpiece = 0.0, 0.0
    for a, b in rng.uniform(0, 2 * np.pi, (60, 2)):
        dt, _ = Ds(tang, a, b)
        K = kcomp(a, b)
        gap_max = max(gap_max, np.linalg.norm(dt - K))
        Ra = (pos(a + H, b) - pos(a - H, b)) / (2 * H)
        Rb = (pos(a, b + H) - pos(a, b - H)) / (2 * H)
        coef, *_ = np.linalg.lstsq(np.stack([Ra, Rb], 1), tang(a, b),
                                   rcond=None)
        dads, dbds = coef
        ta = (tang(a + H, b) - tang(a - H, b)) / (2 * H)
        tb = (tang(a, b + H) - tang(a, b - H)) / (2 * H)
        k1v = KAP1 * np.array([-np.cos(a), -np.sin(a), 0.0])
        _, t1, e1, e2 = frame(a)
        un = KAP2 * (-np.cos(b) * e1 - np.sin(b) * e2)
        d_apiece = max(d_apiece, np.linalg.norm(dads * ta - k1v))
        d_bpiece = max(d_bpiece, np.linalg.norm(dbds * tb - un))
    print(f"  |D_s t - K_registered| max over torus: {gap_max:.4f} /a_f")
    print(f"  piecewise: |(da/ds) d_a t  -  k1|      max {d_apiece:.4f} /a_f")
    print(f"             |(db/ds) d_b t  -  kappa_2| max {d_bpiece:.4f} /a_f")
    print("  BOTH pieces mismatch at order one: the registered sum-form")
    print("  weights the level-1 curvature as if the backbone advanced at")
    print("  unit rate per composite arc (it advances at less), and assigns")
    print("  the level-2 term a straight-axis rate the curved backbone does")
    print("  not have. The sum-form is a PER-LEVEL curvature sum; the Frenet")
    print("  curvature of the nested curve is a different object.")
    mt = []
    mr = []
    for a, b in rng.uniform(0, 2 * np.pi, (200, 2)):
        dt, _ = Ds(tang, a, b)
        mt.append(np.linalg.norm(dt)); mr.append(np.linalg.norm(kcomp(a, b)))
    mt, mr = np.array(mt), np.array(mr)
    print(f"  |curvature| actual:     [{mt.min():.4f}, {mt.max():.4f}] /a_f,"
          f"  RMS {np.sqrt((mt**2).mean()):.4f}")
    print(f"  |K_registered|:         [{mr.min():.4f}, {mr.max():.4f}] /a_f,"
          f"  RMS {np.sqrt((mr**2).mean()):.4f}")
    print(f"  <|k|^2> actual / registered: {(mt**2).mean()/(mr**2).mean():.4f}"
          "   (the bending-energy-weighting ratio)")
    print("\nVERDICT: HALTED-AT-CONTROL, DIFFERENT-OBJECTS-FOUND.")
    print("  The registered composite curvature and the Frenet curvature of")
    print("  the stated nested curve are DIFFERENT OBJECTS, mismatching at")
    print("  order one in BOTH per-level pieces. The self-consistency test")
    print("  cannot run as chartered (the force side is ambiguous: which")
    print("  curvature does the granted rod's bending respond to?). The")
    print("  question goes to a curvature-object adjudication, and every")
    print("  bending-channel number priced through K_registered goes ON")
    print("  NOTICE, not superseded.")
    # ---- verifier exit semantics (2026-08-19, suite run for v3.27.2) ----
    # This halt IS the registered content of FND-138. Under verify_corpus
    # a benchmark's job is to confirm the REGISTERED record reproduces,
    # not to re-litigate the commission: exit 0 = the kept failure is
    # confirmed as registered; exit 1 stays reserved for breakage (which
    # also keeps import errors from ever counting as a pass). Gates are
    # the registered numbers from the FND-138 note.
    ratio = (mt ** 2).mean() / (mr ** 2).mean()
    reproduced = (res_l1 < 1e-10 and span_max < 1e-8
                  and abs(gap_max - 1.5058) < 5e-3
                  and abs(ratio - 0.7316) < 5e-3)
    if reproduced:
        print("\nVERIFIER VERDICT: REGISTERED HALT REPRODUCED (FND-138's")
        print("  kept failure confirmed: gap 1.506, ratio 0.732, operator")
        print("  controls at machine precision). PASS as a record check.")
        raise SystemExit(0)
    print("\nVERIFIER VERDICT: the registered halt did NOT reproduce --")
    print(f"  gap_max {gap_max:.4f} (registered 1.5058), ratio "
          f"{ratio:.4f} (registered 0.7316). BREAKAGE.")
    raise SystemExit(1)

# ------------------------------------------------------------------ LEG 2
print("\nLEG 2 -- THE METRIC LEG (stretch rate of the stated motion)")
NA = 48
grid = [(a, b) for a in (np.arange(NA) + 0.5) / NA * 2 * np.pi
        for b in (np.arange(NA) + 0.5) / NA * 2 * np.pi]
for sg in (+1, -1):
    sr = []
    for a, b in grid[:: max(1, len(grid) // 1152)]:
        dv, _ = Ds(vel, a, b, sg)
        t = tang(a, b)
        sr.append(t @ dv)                       # d/dt (ds)/ds = t . D_s v
    sr = np.array(sr) / OM2
    print(f"  sign={sg:+d}: stretch rate / Omega_2 -- max |.| = "
          f"{np.abs(sr).max():.4f},  RMS = {np.sqrt((sr**2).mean()):.4f}")

# ------------------------------------------------------------------ LEG 3
print("\nLEG 3 -- THE RESIDUAL LEG (mu rddot - T D_s that, kb = 0)")
scale = OM2 ** 2 * R2
harm = {}
for sg in (+1, -1):
    R_ = []
    bs = []
    for a, b in grid[:: max(1, len(grid) // 1152)]:
        dt, _ = Ds(tang, a, b)
        r = acc(a, b, sg) - TF * dt
        R_.append(np.linalg.norm(r)); bs.append(b)
    R_ = np.array(R_) / scale
    print(f"  sign={sg:+d}: |residual| / (Omega_2^2 R_2) -- max = "
          f"{R_.max():.4f},  RMS = {np.sqrt((R_**2).mean()):.4f}")
    # harmonic content in b along a fixed backbone phase
    a0 = 0.9
    bb = (np.arange(256)) / 256 * 2 * np.pi
    comp = []
    for b in bb:
        dt, _ = Ds(tang, a0, b)
        comp.append(acc(a0, b, sg) - TF * dt)
    comp = np.array(comp) / scale
    F = np.fft.rfft(comp, axis=0) / len(bb)
    mag = np.linalg.norm(np.abs(F), axis=1)
    top = np.argsort(mag[1:])[::-1][:3] + 1
    harm[sg] = [(int(h), float(mag[h])) for h in top]
    print(f"           dominant b-harmonics (n, amplitude): {harm[sg]}")

# ------------------------------------------------------------------ LEG 4
print("\nLEG 4 -- THE REFIT DISPLAY (displayed, not adopted)")
from scipy.optimize import minimize_scalar


def rms_res(om2, sg):
    tot = 0.0; n = 0
    for a, b in grid[:: max(1, len(grid) // 288)]:
        dt, _ = Ds(tang, a, b)
        r = acc(a, b, sg, om2) - TF * dt
        tot += r @ r; n += 1
    return np.sqrt(tot / n)


path_A = 1 / (C1 * C2)
print(f"  build's Omega_2 = {OM2:.4f}  (kb = 0)")
for sg in (+1, -1):
    m = minimize_scalar(rms_res, bounds=(0.2 * OM2, 3 * OM2),
                        args=(sg,), method='bounded')
    om2s = m.x
    # KE at refit (closed form from the composite build)
    orbit1 = OM1 ** 2 * R1 ** 2
    offset = OM1 ** 2 * (R2 ** 2 / 2) * (1 + C1 ** 2)
    orbit2 = om2s ** 2 * R2 ** 2
    cross = 2 * OM1 * om2s * C1 * R2 ** 2 * sg
    ke = 0.5 * (orbit1 + offset + orbit2 + cross)
    E = path_A * (1 + ke)
    print(f"  sign={sg:+d}: refit Omega_2 = {om2s:.4f} "
          f"({om2s/OM2:.3f}x build), refit-RMS = {rms_res(om2s, sg)/scale:.4f}"
          f" (build-RMS {rms_res(OM2, sg)/scale:.4f})")
    print(f"           KE/arc at refit = {ke:.4f}  ->  "
          f"Sigma_wave corner (kb=0) = {E:.4f} T0")
print("  registered box for comparison (this display only): "
      "[3.222, 4.313] T0")

print("\nVERDICT: written after the run -- see results doc.")
raise SystemExit(0)
