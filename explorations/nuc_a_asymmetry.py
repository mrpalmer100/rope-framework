import numpy as np
import sys
from pathlib import Path
from scipy.special import spherical_jn
from scipy.optimize import brentq
import periodictable as pt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "benchmarks" / "em"))
from atomic_mass_predictor import structure_constants, calibrate_aV, binding, D0

HBARC = 197.32698
MN = 938.918
R0 = (3 / (4 * np.pi * np.sqrt(2)))**(1 / 3) * D0

def bessel_zeros(l, n_zeros):
    zs, x0 = [], l + 1.5
    while len(zs) < n_zeros:
        x1 = x0 + 0.5
        if spherical_jn(l, x0) * spherical_jn(l, x1) < 0:
            zs.append(brentq(lambda x: spherical_jn(l, x), x0, x1))
        x0 = x1
    return zs

def ladder_box(n_states=800):
    lev = []
    for l in range(0, 25):
        for x in bessel_zeros(l, 8):
            lev.append((x**2, 2 * (2 * l + 1)))
    lev.sort()
    return lev[:n_states]

def ladder_iso(n_shells=25):
    return [((N + 1.5), (N + 1) * (N + 2)) for N in range(n_shells)]

def fill(ladder, n_particles, scale):
    E, left = 0.0, n_particles
    for e, g in ladder:
        take = min(g, left)
        E += take * e * scale
        left -= take
        if left == 0:
            return E
    raise RuntimeError("ladder too short")

def kinetic_deficit(A, dN, ladder_fn):
    R = R0 * A**(1 / 3)
    if ladder_fn is ladder_box:
        scale = HBARC**2 / (2 * MN * R**2)
        lad = ladder_box()
    else:
        lad = ladder_iso()
        box = ladder_box()
        cum, i = 0, 0
        while cum < A // 2:
            cum += box[i][1]; i += 1
        EF_box = box[i - 1][0] * HBARC**2 / (2 * MN * (R0 * A**(1/3))**2)
        cum, j = 0, 0
        while cum < A // 2:
            cum += lad[j][1]; j += 1
        scale = EF_box / lad[j - 1][0]
        lad = ladder_iso()
    Z = A // 2 - dN // 2
    N = A - Z
    Esym = fill(lad, A // 2, scale) + fill(lad, A - A // 2, scale)
    Easy = fill(lad, Z, scale) + fill(lad, N, scale)
    return Easy - Esym

def extract_aA(ladder_fn, label):
    rows = []
    for A in (40, 60, 80, 100, 120, 140, 180, 208, 238):
        for frac in (0.10, 0.15, 0.20, 0.25, 0.30, 0.35):
            dN = 2 * int(frac * A / 2)
            if dN < 2:
                continue
            rows.append((A, dN, kinetic_deficit(A, dN, ladder_fn)))
    arr = np.array(rows)
    x = arr[:, 1]**2 / arr[:, 0]
    y = arr[:, 2]
    aA = float(np.linalg.lstsq(x[:, None], y, rcond=None)[0][0])
    r2 = 1 - np.var(y - aA * x) / np.var(y)
    print(f"  {label}: a_A(kinetic) pooled = {aA:.1f} MeV, shape r^2 vs (N-Z)^2/A = {r2:.4f}")
    return aA

def load_table():
    M_H1, M_N_u, U = 1.00782503207, 1.00866491588, 931.49410242
    out = []
    for el in pt.elements:
        if el.number == 0:
            continue
        for iso in el:
            try:
                ab = iso.abundance
            except Exception:
                ab = 0
            A, Z = iso.isotope, el.number
            if A < 12:
                continue
            if (ab and ab > 0) or (el.symbol, A) in {("Th",232),("U",235),("U",238)}:
                B = (Z * M_H1 + (A - Z) * M_N_u - iso.mass) * U
                out.append((el.symbol, A, Z, B))
    return sorted(set(out), key=lambda t: (t[1], t[2]))

def s1_table_closure(aA, label, nucs, aV, aSaV, aC):
    R = []
    for sym, A, Z, Bexp in nucs:
        Bp = binding(A, Z, aV, aSaV, aC) - aA * (A - 2 * Z)**2 / A
        R.append(Bp - Bexp)
    R = np.array(R)
    Be = np.array([b for *_, b in nucs])
    A_ = np.array([a for _, a, _, _ in nucs], float)
    hv = A_ > 150
    print(f"    S1[{label}]: table rms {np.sqrt((R**2).mean()):.1f} MeV; heavy-table |err| {np.mean(np.abs(R[hv]/Be[hv]))*100:.2f}% (was 8.8% no-asym)")
    return float(np.sqrt((R**2).mean()))

def s2_valley(aA, label, aV, aSaV, aC):
    devs = []
    stable_Z = {40: 20, 60: 28, 80: 34, 100: 44, 120: 50, 140: 58, 180: 72, 208: 82, 238: 92}
    for A, Zs in stable_Z.items():
        Zgrid = np.arange(max(2, Zs - 15), Zs + 16)
        B = np.array([binding(A, z, aV, aSaV, aC) - aA * (A - 2 * z)**2 / A for z in Zgrid])
        M = -(B + Zgrid * (939.565 - 938.783))
        Zstar = int(Zgrid[np.argmin(M)])
        devs.append(Zstar - Zs)
    devs = np.array(devs)
    print(f"    S2[{label}]: dev {devs.tolist()} (mean |dev| {np.mean(np.abs(devs)):.1f})")
    return float(np.mean(np.abs(devs)))

def main():
    aSaV, aC = structure_constants()
    aV = calibrate_aV(aSaV, aC)
    print(f"derived geometry: r0 = {R0:.3f} fm; NUC-005 a_V = {aV:.3f} MeV\n")
    print("== PRIMARY + WELL-PROFILE VARIANTS (kinetic, blind) ==")
    aA_v1 = extract_aA(ladder_box, "V1 spherical box")
    aA_v2 = extract_aA(ladder_iso, "V2 isotropic ladder")
    print(f"  V3 = V1 + a_V = {aA_v1:.1f} + {aV:.1f} = {aA_v1 + aV:.1f} MeV\n")
    print("== WINDOW CHECK (17-27 MeV) ==")
    for lab, v in (("V1", aA_v1), ("V2", aA_v2), ("V3", aA_v1 + aV)):
        print(f"  {lab}: {v:.1f} MeV -> {'IN WINDOW' if 17 <= v <= 27 else 'OUT (lead if shape held)'}")
    print()
    print("== SECOND PREDICTIONS ==")
    nucs = load_table()
    print(f"  ({len(nucs)} nuclides loaded)")
    for lab, v in (("V1", aA_v1), ("V2", aA_v2), ("V3", aA_v1 + aV)):
        s1_table_closure(v, lab, nucs, aV, aSaV, aC)
        s2_valley(v, lab, aV, aSaV, aC)
        print()

if __name__ == "__main__":
    main()
