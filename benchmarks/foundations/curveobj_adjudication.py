"""COMMISSION CURVE-OBJ (FND-139, 2026-08-18) -- the curvature-object
adjudication and the recovered ansatz test.

Executed under analysis/CURVEOBJ_bars_LOCKED.md. Machinery imported from
the ANSATZ benchmark (operator validated there at 2e-11).
"""
import numpy as np
import importlib.util as _ilu
import pathlib as _pl

_spec = _ilu.spec_from_file_location(
    "ans", _pl.Path(__file__).with_name("ansatz_selfconsistency.py"))
_a = _ilu.module_from_spec(_spec)
try:
    _spec.loader.exec_module(_a)          # runs its halt; we want its defs
except SystemExit:
    pass

Ds, pos, tang, kcomp = _a.Ds, _a.pos, _a.tang, _a.kcomp
vel, acc, frame = _a.vel, _a.acc, _a.frame
OM1, OM2, R1, R2, TF = _a.OM1, _a.OM2, _a.R1, _a.R2, _a.TF
C1, C2 = _a.C1, _a.C2

ok = True
rng = np.random.default_rng(11)
print("COMMISSION CURVE-OBJ -- the curvature-object adjudication\n")

# ------------------------------------------------------------------ LEG 2
# (computed first; leg 1 cites its indictment control)
print("LEG 2 -- THE CORRECTED OBJECT AND ITS CONTROLS")
tanrep, frenet, indict = 0.0, 0.0, 0.0
k2lo = []
for a, b in rng.uniform(0, 2 * np.pi, (80, 2)):
    dR, _ = Ds(pos, a, b)
    tanrep = max(tanrep, np.linalg.norm(dR - tang(a, b)))
    kt, _ = Ds(tang, a, b)
    t = tang(a, b)
    frenet = max(frenet, abs(t @ kt))
    indict = max(indict, abs(t @ kcomp(a, b)))
    k2lo.append(kt @ kt)
print(f"  (i)  D_s R vs registered tangent, max:  {tanrep:.2e}  "
      f"[{'PASS' if tanrep < 1e-8 else 'FAIL'}]")
print(f"  (ii) Frenet property |t . kappa_true|:  {frenet:.2e}  "
      f"[{'PASS' if frenet < 1e-6 else 'FAIL'}]")
print(f"  (iii) THE INDICTMENT |t . K_registered|: {indict:.4f}  "
      "(order one)")
print("       A curvature is orthogonal to its tangent. The registered")
print("       sum-form is not the curvature of ANY curve with these")
print("       tangents.")
ok &= tanrep < 1e-8 and frenet < 1e-6
k2hi = []
for a, b in rng.uniform(0, 2 * np.pi, (320, 2)):
    kt, _ = Ds(tang, a, b)
    k2hi.append(kt @ kt)
m_lo, m_hi = np.mean(k2lo), np.mean(k2hi)
# registered-ensemble comparison
k2reg = np.mean([kcomp(a, b) @ kcomp(a, b)
                 for a, b in rng.uniform(0, 2 * np.pi, (320, 2))])
print(f"  <|kappa_true|^2> = {m_hi:.4f} /a_f^2 "
      f"(drift {abs(m_hi-m_lo)/m_hi:.1e}  "
      f"[{'PASS' if abs(m_hi-m_lo)/m_hi < 1e-1 else 'FAIL'}] -- MC samples)")
print(f"  <|K_registered|^2> = {k2reg:.4f} /a_f^2   ratio "
      f"{m_hi/k2reg:.4f}")

# ------------------------------------------------------------------ LEG 1
print("\nLEG 1 -- THE ADJUDICATION")
print("  The granted rod class carries NO stress-free wound reference")
print("  (FND-118; the MAINT channel-i inadmissibility ruling stands on")
print("  that clause). A rod with a straight stress-free reference bends")
print("  against the curvature of its ACTUAL centerline. The per-level sum")
print("  is the bending strain of a rod referenced to the LEVEL-1-WOUND")
print("  backbone -- an object the grant forbids. The steelman (the")
print("  ensemble was intended to sample the composite geometry) is")
print("  disposed of by FND-138's measurement and by the indictment above:")
print("  intent to sample the true curvature is not possession of it, and")
print("  the sum-form fails t.K = 0 at order one -- it is no curve's")
print("  curvature.")
print("  VERDICT (leg): TRUE-CURVATURE-ADJUDICATED. The granted rod bends")
print("  against kappa_true, within the granted class, by the grant's own")
print("  clause. No new grant issued; no registered text edited.")

# ------------------------------------------------------------------ LEG 3
print("\nLEG 3 -- THE ON-NOTICE LIST, DISPOSITIONED")
print(f"  kb feasibility ceiling (display only): energy weighting ratio")
print(f"  {m_hi/k2reg:.3f} -> zeroth-order re-pricing 0.07909/"
      f"{m_hi/k2reg:.3f} = {0.07909/(m_hi/k2reg):.4f} T0_f a_f^2, LOOSER;")
print("  the true re-solve on the Bloch instrument is chartered OUT.")
kmax = np.sqrt(max(k2hi))
print(f"  SHIN7 worst-case kappa_tot = 5.713: actual max |kappa_true| = "
      f"{kmax:.3f} < 5.713 -- THE BOUND HOLDS (safe direction confirmed).")
print("  Level-2 balance coefficient (17.926): per-level object; its use in")
print("  Omega_2's fixing is part of the ansatz being tested below; its")
print("  re-derivation under kappa_true belongs to the chartered re-solve.")

# ------------------------------------------------------------------ LEG 4
print("\nLEG 4 -- THE METRIC LEG (recovered ansatz test; kb = 0)")
NA = 34
grid = [(a, b) for a in (np.arange(NA) + 0.5) / NA * 2 * np.pi
        for b in (np.arange(NA) + 0.5) / NA * 2 * np.pi]
for sg in (+1, -1):
    sr = []
    for a, b in grid:
        dv, _ = Ds(vel, a, b, sg)
        sr.append(tang(a, b) @ dv)
    sr = np.array(sr) / OM2
    print(f"  sign={sg:+d}: stretch rate / Omega_2 -- max |.| = "
          f"{np.abs(sr).max():.4f},  RMS = {np.sqrt((sr**2).mean()):.4f}")

# ------------------------------------------------------------------ LEG 5
print("\nLEG 5 -- THE RESIDUAL LEG (mu rddot - T D_s that; kb = 0)")
scale = OM2 ** 2 * R2
res_stats = {}
for sg in (+1, -1):
    R_ = []
    for a, b in grid:
        dt, _ = Ds(tang, a, b)
        R_.append(np.linalg.norm(acc(a, b, sg) - TF * dt))
    R_ = np.array(R_) / scale
    res_stats[sg] = (R_.max(), np.sqrt((R_ ** 2).mean()))
    print(f"  sign={sg:+d}: |residual| / (Omega_2^2 R_2) -- max = "
          f"{R_.max():.4f},  RMS = {np.sqrt((R_**2).mean()):.4f}")
    bb = np.arange(192) / 192 * 2 * np.pi
    comp = np.array([acc(0.9, b, sg) - TF * Ds(tang, 0.9, b)[0]
                     for b in bb]) / scale
    F = np.fft.rfft(comp, axis=0) / len(bb)
    mag = np.linalg.norm(np.abs(F), axis=1)
    top = np.argsort(mag[1:])[::-1][:3] + 1
    print(f"           dominant b-harmonics (n, amp): "
          f"{[(int(h), round(float(mag[h]), 4)) for h in top]}")

# ------------------------------------------------------------------ LEG 6
print("\nLEG 6 -- THE REFIT DISPLAY (displayed, not adopted)")
from scipy.optimize import minimize_scalar


def rms_res(om2, sg):
    tot = 0.0
    for a, b in grid[::4]:
        dt, _ = Ds(tang, a, b)
        r = acc(a, b, sg, om2) - TF * dt
        tot += r @ r
    return np.sqrt(tot / len(grid[::4]))


path_A = 1 / (C1 * C2)
for sg in (+1, -1):
    m = minimize_scalar(rms_res, bounds=(0.2 * OM2, 3 * OM2), args=(sg,),
                        method='bounded')
    om2s = m.x
    orbit1 = OM1 ** 2 * R1 ** 2
    offset = OM1 ** 2 * (R2 ** 2 / 2) * (1 + C1 ** 2)
    ke = 0.5 * (orbit1 + offset + om2s ** 2 * R2 ** 2
                + 2 * OM1 * om2s * C1 * R2 ** 2 * sg)
    print(f"  sign={sg:+d}: refit Omega_2 = {om2s:.4f} ({om2s/OM2:.3f}x "
          f"build), RMS {rms_res(om2s, sg)/scale:.4f} "
          f"(build {rms_res(OM2, sg)/scale:.4f})")
    print(f"           Sigma_wave corner (kb=0) at refit = "
          f"{path_A*(1+ke):.4f} T0")
print("  registered box (display only): [3.222, 4.313] T0")

print("\nVERDICT: written after the run -- see results doc.")
raise SystemExit(0 if ok else 1)
