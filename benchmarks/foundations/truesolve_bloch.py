"""COMMISSION TRUE-SOLVE (2026-08-18) -- the Bloch-instrument bending
re-solve under kappa_true.

Executed under analysis/TRUESOLVE_bars_LOCKED.md. Instrument imported
from the FND-126 benchmark (superseded-not-erased; that file is
untouched). The ONE change: local_set's k0 is the Frenet curvature of
the actual nested curve, kappa_true = D_s(that), via the operator
validated at FND-138/139. Clean-room: no target value appears in any
build or solve leg; comparisons happen in the final leg only.
Units: T0_f = a_f = c = mu_f = 1.
"""
import numpy as np
import importlib.util as _ilu
import pathlib as _pl

_here = _pl.Path(__file__).parent


def _load(name, fname):
    spec = _ilu.spec_from_file_location(name, _here / fname)
    mod = _ilu.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except SystemExit:
        pass                        # the ANSATZ module halts by design
    return mod


_bl = _load("blochl", "blochl_longitudinal.py")     # the instrument
_an = _load("ansatz", "ansatz_selfconsistency.py")  # the operator

energy_form = _bl.energy_form
NB, SITES, IDX, GW, P, H = _bl.NB, _bl.SITES, _bl.IDX, _bl.GW, _bl.P, _bl.H
N = _bl.N
PPHYS = _bl.PPHYS
ST1, ST2, C1, C2 = _bl.ST1, _bl.ST2, _bl.C1, _bl.C2
KAP1, KAP2 = _bl.KAP1, _bl.KAP2

Ds, pos, tang = _an.Ds, _an.pos, _an.tang

ok = True
rng = np.random.default_rng(7)
print("COMMISSION TRUE-SOLVE -- Bloch bending re-solve under kappa_true\n")

# ---------------------------------------------------------- kappa_true
_KMEMO = {}


def kappa_true(f1, f2):
    """Frenet curvature of the nested curve at instrument phases.
    Frame identity (bars, on the face): ansatz phase = (f1, f2 + pi)."""
    key = (round(f1 % (2 * np.pi), 12), round(f2 % (2 * np.pi), 12))
    if key not in _KMEMO:
        kt, _ = Ds(tang, key[0], key[1] + np.pi)
        _KMEMO[key] = kt
    return _KMEMO[key]


def t_of(f1, f2):
    return tang(f1 % (2 * np.pi), (f2 % (2 * np.pi)) + np.pi)


def local_set_true(s, m):
    out = []
    for j1 in range(m):
        f1 = 2 * np.pi * (s[0] / P + j1 / m)
        for j2 in range(m):
            f2 = 2 * np.pi * ((s[1] + s[2]) / P + j2 / m)
            out.append((t_of(f1, f2), kappa_true(f1, f2)))
    return out


def t_bloch(f1, f2):
    t1 = np.array([-ST1 * np.sin(f1), ST1 * np.cos(f1), C1])
    a = np.array([0., 0., 1.]) if abs(t1[2]) < 0.9 else np.array([1., 0., 0.])
    e1 = np.cross(t1, a); e1 /= np.linalg.norm(e1); e2 = np.cross(t1, e1)
    return ST2 * (-np.sin(f2) * e1 + np.cos(f2) * e2) + C2 * t1


# ------------------------------------------------------------ CONTROLS
print("CONTROLS (i)-(iii) -- frame identity and the operator")
fid, tanrep, frenet, indict = 0.0, 0.0, 0.0, 0.0
for f1, f2 in rng.uniform(0, 2 * np.pi, (40, 2)):
    fid = max(fid, np.linalg.norm(t_of(f1, f2) - t_bloch(f1, f2)))
    dR, _ = Ds(pos, f1 % (2 * np.pi), (f2 % (2 * np.pi)) + np.pi)
    t = t_of(f1, f2)
    tanrep = max(tanrep, np.linalg.norm(dR - t))
    kt = kappa_true(f1, f2)
    frenet = max(frenet, abs(t @ kt))
    k1v = KAP1 * np.array([-np.cos(f1), -np.sin(f1), 0.0])
    t1 = np.array([-ST1 * np.sin(f1), ST1 * np.cos(f1), C1])
    a = np.array([0., 0., 1.])
    e1 = np.cross(t1, a); e1 /= np.linalg.norm(e1); e2 = np.cross(t1, e1)
    kreg = k1v + KAP2 * (-np.cos(f2) * e1 - np.sin(f2) * e2)
    indict = max(indict, abs(t @ kreg))
print(f"  (i)   frame identity |t_ans(f2+pi) - t_bloch|: {fid:.2e}  "
      f"[{'PASS' if fid < 1e-12 else 'HALT'}]")
print(f"  (ii)  operator, D_s R vs tangent:              {tanrep:.2e}  "
      f"[{'PASS' if tanrep < 1e-8 else 'HALT'}]")
print(f"  (iii) Frenet |t . kappa_true|: {frenet:.2e}  "
      f"[{'PASS' if frenet < 1e-6 else 'HALT'}]   "
      f"(|t . K_reg| = {indict:.3f}, the indictment, display)")
ok &= fid < 1e-12 and tanrep < 1e-8 and frenet < 1e-6
if not ok:
    print("\nVERDICT: INSTRUMENT-FAULT at the operator controls")
    raise SystemExit(1)

# ------------------------------------------- linear assembly machinery
def assemble_parts(kvec, m):
    """D = kf*DA + T*DB + kb*DC  (exact: energy_form is linear in each)."""
    DA = np.zeros((3 * N, 3 * N), dtype=complex)
    DB = np.zeros_like(DA); DC = np.zeros_like(DA)
    for s in SITES:
        i = IDX[s]
        L = local_set_true(s, m)
        QA = sum(energy_form(t, k0, 1, 0, 0) for t, k0 in L) / len(L)
        QB = sum(energy_form(t, k0, 0, 1, 0) for t, k0 in L) / len(L)
        QC = sum(energy_form(t, k0, 0, 0, 1) for t, k0 in L) / len(L)
        G = np.zeros((9, 3 * N), dtype=complex)
        for n_i, n in enumerate(NB):
            j = IDX[tuple((s[q] + n[q]) % P for q in range(3))]
            ph = np.exp(1j * (kvec @ (np.array(n, float) * H))); gw = GW[:, n_i]
            for a in range(3):
                for b in range(3):
                    G[3 * a + b, 3 * j + a] += gw[b] * ph
                    G[3 * a + b, 3 * i + a] -= gw[b]
        for QX, DX in ((QA, DA), (QB, DB), (QC, DC)):
            DX += G.conj().T @ QX.reshape(9, 9) @ G
    return tuple((D + D.conj().T) / 2 for D in (DA, DB, DC))


def dynamical_true(kvec, kf, T, kb, m):
    D = np.zeros((3 * N, 3 * N), dtype=complex)
    for s in SITES:
        i = IDX[s]
        L = local_set_true(s, m)
        Q = sum(energy_form(t, k0, kf, T, kb) for t, k0 in L) / len(L)
        G = np.zeros((9, 3 * N), dtype=complex)
        for n_i, n in enumerate(NB):
            j = IDX[tuple((s[q] + n[q]) % P for q in range(3))]
            ph = np.exp(1j * (kvec @ (np.array(n, float) * H))); gw = GW[:, n_i]
            for a in range(3):
                for b in range(3):
                    G[3 * a + b, 3 * j + a] += gw[b] * ph
                    G[3 * a + b, 3 * i + a] -= gw[b]
        D += G.conj().T @ Q.reshape(9, 9) @ G
    return (D + D.conj().T) / 2


def speeds(DA, DB, DC, kvec, kf, T, kb):
    d = kvec / np.linalg.norm(kvec)
    w2, V = np.linalg.eigh(kf * DA + T * DB + kb * DC)
    out = {}
    for lab, pol in (('L', d),
                     ('T', np.cross(d, [0, 0, 1.] if abs(d[2]) < 0.9 else [1., 0, 0]))):
        pol = pol / np.linalg.norm(pol)
        v = np.zeros(3 * N, dtype=complex)
        for s in SITES:
            v[3 * IDX[s]:3 * IDX[s] + 3] = pol * np.exp(
                1j * (kvec @ (np.array(s, float) * H)))
        v /= np.linalg.norm(v)
        b = int(np.argmax(np.abs(V.conj().T @ v) ** 2))
        out[lab] = np.sqrt(max(w2[b], 0)) / np.linalg.norm(kvec)
    return out


KV24 = (2 * np.pi / (24 * PPHYS)) * np.array([0., 0., 1.])
KV48 = (2 * np.pi / (48 * PPHYS)) * np.array([0., 0., 1.])

print("\nAssembling the instrument (m = 6, lambda = 24p and 48p) ...")
D24 = assemble_parts(KV24, 6)
D48 = assemble_parts(KV48, 6)

print("CONTROL (iv) -- linearity decomposition")
kf0, T0v, kb0 = 7.3, 1.1, 0.05
Ddir = dynamical_true(KV24, kf0, T0v, kb0, 6)
Dlin = kf0 * D24[0] + T0v * D24[1] + kb0 * D24[2]
lin = np.abs(Ddir - Dlin).max() / max(np.abs(Ddir).max(), 1e-30)
print(f"  |direct - linear| / |direct| = {lin:.2e}  "
      f"[{'PASS' if lin < 1e-10 else 'HALT'}]")
ok &= lin < 1e-10

print("\nCONTROL (v) -- straight control (unwound; inherited)")
r = _bl.branch(9.0, 1.5, 0.0, 1, 24, wound=False)
e1c = abs(r['L'][0] - 3.0) / 3.0
e2c = abs(r['T'][0] - np.sqrt(1.5)) / np.sqrt(1.5)
print(f"  c_L = {r['L'][0]:.6f} (3.000000), c_T = {r['T'][0]:.6f} "
      f"({np.sqrt(1.5):.6f})  [{'PASS' if max(e1c, e2c) < 2e-3 else 'HALT'}]")
ok &= max(e1c, e2c) < 2e-3

print("\nCONTROL (ix) -- ensemble statistic (display)")
k2 = np.mean([kappa_true(f1, f2) @ kappa_true(f1, f2)
              for f1, f2 in rng.uniform(0, 2 * np.pi, (400, 2))])
print(f"  <|kappa_true|^2> = {k2:.4f} /a_f^2  "
      "(FND-138 grid 0.732x reg, FND-139 MC 0.776x reg -- display)")

# ------------------------------------------------------------ the solve
from scipy.optimize import fsolve

KT0 = 2.0


def resid(x, kb, Dp):
    s = speeds(*Dp, KV24, max(x[0], 1e-6), x[1], kb)
    return [s['T'] ** 2 - 1.0, s['L'] ** 2 - KT0]


print("\nLEG A -- anchor re-solve at kb = 0  [CONTROL (vi), instrument-unchanged]")
kfA, TA = fsolve(resid, [9.0, 1.5], args=(0.0, D24))
print(f"  k_f/T0_f = {kfA:.5f}   T_fibre/T0_f = {TA:.5f}   "
      f"(FND-126: 9, 1.5)  [{'PASS' if abs(kfA - 9.0) < 0.02 else 'HALT'}]")
ok &= abs(kfA - 9.0) < 0.02
if not ok:
    print("\nVERDICT: INSTRUMENT-FAULT -- nothing registers")
    raise SystemExit(1)

print("\nCONTROL (vii) -- reading window at kb = 0")
sL24 = speeds(*D24, KV24, kfA, TA, 0.0)['L']
sL48 = speeds(*D48, KV48, kfA, TA, 0.0)['L']
drift = abs(sL24 - sL48) / (0.5 * (sL24 + sL48))
print(f"  c_L(24p) = {sL24:.6f}  c_L(48p) = {sL48:.6f}  "
      f"drift = {drift * 100:.4f}%  [{'PASS' if drift <= 0.005 else 'HALT'}]")
ok &= drift <= 0.005

print("\nLEG B -- the feasibility scan (bisection on T_fibre > 0)")


def tension_at(kb, Dp):
    return fsolve(resid, [9.0, 1.5], args=(kb, Dp))[1]


KB_SEARCH_HI = 0.5
if tension_at(KB_SEARCH_HI, D24) > 0:
    print(f"  T > 0 at kb = {KB_SEARCH_HI}: NO-CEILING-IN-RANGE")
    ceiling = None
else:
    lo, hi = 0.0, KB_SEARCH_HI
    while hi - lo > 1e-4:
        mid = 0.5 * (lo + hi)
        if tension_at(mid, D24) > 0:
            lo = mid
        else:
            hi = mid
    ceiling = lo
    kfC, TC = fsolve(resid, [9.0, 1.5], args=(ceiling, D24))
    print(f"  feasibility ceiling under kappa_true: "
          f"kb <= {ceiling:.5f} T0_f a_f^2")
    print(f"  at the edge: k_f/T0_f = {kfC:.4f}, T_fibre/T0_f = {TC:.5f}")

print("\nCONTROL (viii) -- multiplicity at the feasibility-relevant read")
ceils = {}
for m in (2, 4):
    Dm = assemble_parts(KV24, m)
    lo, hi = 0.0, KB_SEARCH_HI
    if tension_at(hi, Dm) > 0:
        ceils[m] = None
        print(f"  m={m}: no ceiling in range")
        continue
    while hi - lo > 5e-4:
        mid = 0.5 * (lo + hi)
        if tension_at(mid, Dm) > 0:
            lo = mid
        else:
            hi = mid
    ceils[m] = lo
    print(f"  m={m} ({m * m:2d} fibres/cell): ceiling = {lo:.5f}")
if ceiling is not None and ceils.get(4):
    mdrift = abs(ceils[4] - ceiling) / ceiling
    print(f"  m=4 vs m=6 drift on the ceiling: {mdrift * 100:.3f}%  "
          f"[{'PASS' if mdrift <= 0.01 else 'MULTIPLICITY RIDER'}]")

print("\nLEG C -- the SHIN7 worst case (value owed per FND-139)")
kmax = max(np.sqrt(kappa_true(f1, f2) @ kappa_true(f1, f2))
           for f1, f2 in [(2 * np.pi * i / 240, 2 * np.pi * j / 240)
                          for i in range(240) for j in range(240)])
print(f"  max |kappa_true| over the phase torus (240^2): {kmax:.4f} /a_f "
      "(SHIN7 bound context: 5.713)")

print("\nLEG D -- the 17.926 disposition, by name")
print("  tau_2^2 - kappa_2^2/2 is a per-level object inside the composite")
print("  build's level-2 speed; its host state was measured off-shell")
print("  (FND-139) and proven nonexistent in the rigid family (FND-140).")
print("  Re-derivation GATED ON TRUE-STATE STAGE 2. No number issued here.")

# ------------------------------------------------------ comparison leg
print("\nCOMPARISON LEG (clean-room: targets appear here only)")
if ceiling is not None:
    print(f"  ceiling of record (FND-126/131): 0.07909  ->  {ceiling:.5f}  "
          f"({'LOOSER' if ceiling > 0.07909 else 'TIGHTER -- SURPRISE'})")
    print(f"  zeroth-order display (FND-139) was 0.102: "
          f"actual/display = {ceiling / 0.102:.3f}")
    for v, lab in ((0.126, "KBSAT historical 0.126"),
                   (0.282, "re-priced ceiling 0.282")):
        print(f"  {lab}: {'INSIDE' if v <= ceiling else 'OUTSIDE'} "
              "the new ceiling  (desk display only)")

print("\nVERDICT:", "PASS -- re-solve delivered" if ok else
      "INSTRUMENT/BAR FAILURE")
raise SystemExit(0 if ok else 1)
