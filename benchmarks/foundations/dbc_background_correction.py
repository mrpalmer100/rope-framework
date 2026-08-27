"""COMMISSION DBC -- the dynamical-background correction (FND-133).

Executed under analysis/DBC_background_correction_bars_LOCKED.md.
Instrument: FND-089-class supercell Bloch machinery, imported verbatim
from the BLOCH-L build (no re-implementation; the anchors under test are
that file's anchors). Units: T0_f = 1, a_f = 1, c = 1.

Legs
  1  background kinematics control (registered inputs only; halt on fail)
  2  mass-matrix derivation (displayed; cancellation by MAINT channel iii)
  3  rotation = common phase shift (isometry identity, machine precision)
  4  the instrument sweep: delta-dependence of c_L, c_T at m = 1,2,4,6,
     harmonic-counting prediction pre-registered in the bars
"""
import numpy as np

import importlib.util as _ilu
import pathlib as _pl

_spec = _ilu.spec_from_file_location(
    "blochl", _pl.Path(__file__).with_name("blochl_longitudinal.py"))
_bl = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_bl)

S1, C1, ST1 = _bl.S1, _bl.C1, _bl.ST1
S2, C2, ST2 = _bl.S2, _bl.C2, _bl.ST2
KAP1, KAP2, PPHYS = _bl.KAP1, _bl.KAP2, _bl.PPHYS
P, N, SITES, IDX = _bl.P, _bl.N, _bl.SITES, _bl.IDX
energy_form = _bl.energy_form

ok = True
print("COMMISSION DBC -- the dynamical-background correction")
print("instrument: the BLOCH-L build, imported verbatim\n")

# ---------------------------------------------------------------- LEG 1
print("LEG 1 -- BACKGROUND KINEMATICS CONTROL (registered inputs only)")
Tf = 1.5                       # T_fibre/T0_f, the BLOCH-L stretch+tension read
R1, kap1_h, tau1_h = _bl.helix(C1)
Omega = np.sqrt(kap1_h * Tf / R1)          # mu Omega^2 R = kappa T  (mu = 1)
vm = Omega * R1
e_a = abs(Omega**2 * R1 - kap1_h * Tf)
e_b = abs(vm - 1.0)
e_c = abs(kap1_h * R1 - (1 - S1))
print(f"  R_1 = {R1:.6f} a_f   kappa_1 = {kap1_h:.6f}/a_f   "
      f"Omega = {Omega:.6f} c/a_f")
print(f"  (a) centripetal balance residual: {e_a:.2e}  "
      f"[{'PASS' if e_a < 1e-9 else 'FAIL'}]")
print(f"  (b) material-speed identity v_m = Omega R = {vm:.8f} c  "
      f"[{'PASS' if e_b < 1e-6 else 'FAIL'}]  (FND-132, recomputed)")
print(f"  (c) kappa_1 R_1 = {kap1_h*R1:.8f} = sin^2 theta = {1-S1:.8f}  "
      f"[{'PASS' if e_c < 1e-9 else 'FAIL'}]")
ok &= e_a < 1e-9 and e_b < 1e-6 and e_c < 1e-9
if not ok:
    print("\nHALT: kinematics control failed (bars, Leg 1).")
    raise SystemExit(1)

# ---------------------------------------------------------------- LEG 2
print("\nLEG 2 -- THE MASS MATRIX (derivation, displayed)")
print("  Material coordinates r(s,t), s the material label. Kinetic density")
print("  (mu/2)|d_t r|^2 with r = r0(s,t) + u(s,t) expands to")
print("      (mu/2)|d_t r0|^2  +  mu d_t r0 . d_t u  +  (mu/2)|d_t u|^2.")
print("  The middle term integrates by parts (in t) to -mu d_t^2 r0 . u,")
print("  which cancels the LINEAR potential term because the background")
print("  satisfies its equation of motion -- the centripetal balance of")
print("  MAINT channel iii, equilibrated at level 1 kb-free (the neutrality")
print("  theorem) and at level 2 at any kb (MAINT sec. 4). The quadratic")
print("  form in u is therefore (mu/2)|d_t u|^2 + (1/2) u Q(t) u:")
print("  NO convective term, NO Coriolis term (material frame is inertial).")
print("  ALL background dependence sits in Q(t).")

# ---------------------------------------------------------------- LEG 3
print("\nLEG 3 -- ROTATION = COMMON PHASE SHIFT (isometry identity)")


def level1_tk(f1):
    t1 = np.array([-ST1 * np.sin(f1), ST1 * np.cos(f1), C1])
    k1 = KAP1 * np.array([-np.cos(f1), -np.sin(f1), 0.0])
    return t1, k1


def rotz(d):
    c, s = np.cos(d), np.sin(d)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.]])


rng = np.random.default_rng(7)
err = 0.0
for _ in range(50):
    f1, d = rng.uniform(0, 2 * np.pi, 2)
    t_a, k_a = level1_tk(f1 + d)                 # shifted phase
    t_b, k_b = (rotz(d) @ v for v in level1_tk(f1))   # rotated pattern
    err = max(err, np.abs(t_a - t_b).max(), np.abs(k_a - k_b).max())
print(f"  max |shifted - rotated| over 50 random (f1, delta): {err:.2e}  "
      f"[{'PASS' if err < 1e-12 else 'FAIL'}]")
print("  The rotating background at time t IS the static configuration with")
print("  all level-1 phases advanced by delta = Omega t. The perturbation")
print("  problem's entire time dependence is a common shift in local_set.")
ok &= err < 1e-12

# ---------------------------------------------------------------- LEG 4
print("\nLEG 4 -- THE INSTRUMENT SWEEP (the decisive leg)")
print("  Pre-registered prediction (bars): the fibre energy form is degree")
print("  <= 4 in the phase trigonometrics, so the m-point phase average is")
print("  alias-free for m >= 5: delta-dependence expected at m = 1, 2, 4,")
print("  NONE at m = 6 (the production multiplicity).\n")


def local_set_shifted(s, m, d1, d2):
    out = []
    for j1 in range(m):
        f1 = 2 * np.pi * (s[0] / P + j1 / m) + d1
        t1 = np.array([-ST1 * np.sin(f1), ST1 * np.cos(f1), C1])
        k1 = KAP1 * np.array([-np.cos(f1), -np.sin(f1), 0.0])
        a = (np.array([0., 0., 1.]) if abs(t1[2]) < 0.9
             else np.array([1., 0., 0.]))
        e1 = np.cross(t1, a); e1 /= np.linalg.norm(e1); e2 = np.cross(t1, e1)
        for j2 in range(m):
            f2 = 2 * np.pi * ((s[1] + s[2]) / P + j2 / m) + d2
            out.append((ST2 * (-np.sin(f2) * e1 + np.cos(f2) * e2) + C2 * t1,
                        k1 + KAP2 * (-np.cos(f2) * e1 - np.sin(f2) * e2)))
    return out


import itertools
NB, H, GW = _bl.NB, _bl.H, _bl.GW


def dynamical_shifted(kvec, kf, T, kb, m, d1, d2):
    D = np.zeros((3 * N, 3 * N), dtype=complex)
    for s in SITES:
        i = IDX[s]
        L = local_set_shifted(s, m, d1, d2)
        Q = sum(energy_form(t, k0, kf, T, kb) for t, k0 in L) / len(L)
        G = np.zeros((9, 3 * N), dtype=complex)
        for n_i, n in enumerate(NB):
            j = IDX[tuple((s[q] + n[q]) % P for q in range(3))]
            ph = np.exp(1j * (kvec @ (np.array(n, float) * H)))
            gw = GW[:, n_i]
            for a in range(3):
                for b in range(3):
                    G[3 * a + b, 3 * j + a] += gw[b] * ph
                    G[3 * a + b, 3 * i + a] -= gw[b]
        D += G.conj().T @ Q.reshape(9, 9) @ G
    return (D + D.conj().T) / 2


def branch_shifted(kf, T, kb, m, lam_over_p, d1, d2, direction=(0, 0, 1.)):
    d = np.array(direction, float); d /= np.linalg.norm(d)
    kv = (2 * np.pi / (lam_over_p * PPHYS)) * d
    w2, V = np.linalg.eigh(dynamical_shifted(kv, kf, T, kb, m, d1, d2))
    out = {}
    for lab, pol in (('L', d),
                     ('T', np.cross(d, [0, 0, 1.] if abs(d[2]) < 0.9
                                    else [1., 0, 0]))):
        pol = pol / np.linalg.norm(pol)
        v = np.zeros(3 * N, dtype=complex)
        for s in SITES:
            v[3 * IDX[s]:3 * IDX[s] + 3] = pol * np.exp(
                1j * (kv @ (np.array(s, float) * H)))
        v /= np.linalg.norm(v)
        b = int(np.argmax(np.abs(V.conj().T @ v) ** 2))
        out[lab] = np.sqrt(max(w2[b], 0)) / np.linalg.norm(kv)
    return out


KF, TT_, KB = 9.0, 1.5, 0.0        # instrument point (controls' values; kb symbolic->0
                                   # here, and swept at the standing bound below)
DELTAS = [0.0, 0.37, 1.13, 2.51, 4.02, 5.55]
verdict_null = True
for m in (1, 2, 4, 6):
    rows = {}
    for tag, dirv in (("001", (0, 0, 1.)), ("111", (1, 1, 1.))):
        sp = [branch_shifted(KF, TT_, KB, m, 24, d, 0.0, dirv) for d in DELTAS]
        cl = np.array([r['L'] for r in sp]); ct = np.array([r['T'] for r in sp])
        rows[tag] = (np.ptp(cl) / cl.mean(), np.ptp(ct) / ct.mean())
    print(f"  m={m} ({m*m:2d} fibres/cell):  "
          f"spread c_L/c_T (001) = {rows['001'][0]:.2e}/{rows['001'][1]:.2e}   "
          f"(111) = {rows['111'][0]:.2e}/{rows['111'][1]:.2e}")
    if m == 6:
        m6max = max(rows['001'] + rows['111'])
        verdict_null &= m6max < 1e-6

print("\n  level-2 independent shift at m=6 (rate unregistered; theorem must")
print("  hold at ANY rate -- common d2 swept with d1 fixed and jointly):")
sp = [branch_shifted(KF, TT_, KB, 6, 24, d1, d2)
      for d1, d2 in ((0, 0.9), (0.7, 2.2), (2.1, 4.8), (3.3, 0.4))]
cl = np.array([r['L'] for r in sp]); ct = np.array([r['T'] for r in sp])
s2max = max(np.ptp(cl) / cl.mean(), np.ptp(ct) / ct.mean())
print(f"  spread c_L/c_T over (d1,d2) pairs: "
      f"{np.ptp(cl)/cl.mean():.2e}/{np.ptp(ct)/ct.mean():.2e}")
verdict_null &= s2max < 1e-6

print("\n  bending channel on, at the standing bound (kb as the symbol's")
print("  standing value; the solve is NOT rerun -- only delta-dependence of")
print("  D is at issue):")
sp = [branch_shifted(9.0, 1.5, 0.079, 6, 24, d, 0.0) for d in (0.0, 1.7, 3.9)]
cl = np.array([r['L'] for r in sp]); ct = np.array([r['T'] for r in sp])
kbmax = max(np.ptp(cl) / cl.mean(), np.ptp(ct) / ct.mean())
print(f"  spread c_L/c_T: {np.ptp(cl)/cl.mean():.2e}/{np.ptp(ct)/ct.mean():.2e}")
verdict_null &= kbmax < 1e-6

# ---------------------------------------------------------------- VERDICT
print("\nVERDICT (per the pre-registered outcome sheet):")
if ok and verdict_null:
    print("  NULL-CORRECTION. The dynamical matrix on the rotating background")
    print("  is time-independent AT THE PRODUCTION INSTRUMENT (m = 6): the")
    print("  degree-4 phase content of the fibre energy form is averaged")
    print("  alias-free, the Floquet problem degenerates to the static one,")
    print("  and the BLOCH-L anchors carry ZERO background-rotation")
    print("  correction at every order. The static-background conditionality")
    print("  on the standing kb bound is DISCHARGED. The Kirchhoff-only")
    print("  conditionality (pre-stress, contact-gated) STANDS, untouched.")
    raise SystemExit(0)
print("  NOT NULL at the pre-registered bar -- see sweep rows above;")
print("  conditionality stands; no number moves (bars, outcome sheet).")
raise SystemExit(1)
