import numpy as np
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "explorations"))
sys.path.insert(0, str(ROOT / "benchmarks" / "em"))
import nuc_a_asymmetry as na
import nuc_c_coulomb as nc
from atomic_mass_predictor import B_EXP

RHO0 = nc.RHO0
A_D = nc.A_D
ETA = 0.5763
R_C = (3 * 12 / (4 * np.pi * RHO0))**(1/3)

def coordination(r, rho):
    rp = r[None, :]; rr = r[:, None]
    full = (rr + rp) <= R_C
    part = (np.abs(rr - rp) < R_C) & ~full
    g = np.zeros_like(rr * rp)
    g[full] = 4 * np.pi
    with np.errstate(divide="ignore", invalid="ignore"):
        gp = np.pi * (R_C**2 - (rr - rp)**2) / (rr * rp)
    g[part] = gp[part]
    return (g * (rp**2 * rho[None, :])) @ np.gradient(r)

def surface_deficit(A, profile):
    Ru = (3 * A / (4 * np.pi * RHO0))**(1/3)
    r = np.linspace(1e-3, Ru + 12 * A_D, 1200)
    if profile == "sharp":
        rho = np.where(r <= Ru, RHO0, 0.0)
    else:
        lo, hi = 0.2 * Ru, 2.0 * Ru
        for _ in range(60):
            Rh = 0.5 * (lo + hi)
            rho = RHO0 / (1 + np.exp((r - Rh) / A_D))
            Q = np.trapezoid(4 * np.pi * r**2 * rho, r)
            lo, hi = (Rh, hi) if Q < A else (lo, Rh)
    z = coordination(r, rho)
    Ebond_over_eps = -0.5 * np.trapezoid(rho * z * 4 * np.pi * r**2, r)
    return 6 * A + Ebond_over_eps

def main():
    print(f"rho0={RHO0:.4f}, a_d={A_D:.3f}, r_c(z=12)={R_C:.3f}, eta={ETA}\n")
    print("== VALIDATION: sharp-step vs NUC-006's 1.11 ==")
    sharp = [surface_deficit(A, "sharp") / (6 * A**(2/3)) for A in (40, 100, 208)]
    print(f"  sharp a_S/a_V: {sharp[0]:.3f}/{sharp[1]:.3f}/{sharp[2]:.3f} ({'OK' if all(abs(s-1.11)<0.15 for s in sharp) else 'FAIL -- kernel disagrees with monolayer'})\n")
    print("== DIFFUSE SURFACE (blind) ==")
    diff = {A: surface_deficit(A, "diffuse") for A in (16,40,60,80,100,120,140,180,208,238)}
    ratios = {A: d / (6 * A**(2/3)) for A, d in diff.items()}
    med = np.median(list(ratios.values()))
    print(f"  median a_S/a_V = {med:.3f} ({'IN' if 1.18<=med<=1.32 else 'OUT'}) sample: A=40:{ratios[40]:.3f} A=208:{ratios[208]:.3f}\n")
    A0, Z0, B0 = B_EXP["Ca-40"]
    EC = {}
    def ECf(A, Z):
        if (A, Z) not in EC: EC[(A, Z)] = nc.corrected_EC(A, Z, 1 - ETA)
        return EC[(A, Z)]
    D = dict(diff)
    def Dl(A):
        if A not in D: D[A] = surface_deficit(A, "diffuse")
        return D[A]
    # sharp-kernel joint model (the corrected reading)
    Ds = {}
    def Dsharp(A):
        if A not in Ds: Ds[A] = surface_deficit(A, "sharp")
        return Ds[A]
    nucs = na.load_table()
    for prof, Dfn, plab in (("diffuse", Dl, "diffuse-stack"), ("sharp", Dsharp, "sharp-kernel")):
        for e_lab, e in (("B1", ETA), ("B2", ETA**2)):
            eps = (B0 + ECf(A0, Z0)) / (6 * A0 - Dfn(A0))
            aA = 16.6 + 6 * eps * (1 - e) / (3 + e)
            def B(A, Z):
                return eps * (6 * A - Dfn(A)) - ECf(A, Z) - aA * (A - 2*Z)**2 / A
            R = np.array([B(A, Z) - Bexp for _, A, Z, Bexp in nucs])
            Be = np.array([b for *_, b in nucs]); Aarr = np.array([a for _, a, _, _ in nucs], float)
            hv = Aarr > 150
            devs = []
            for A, Zs in {40:20,60:28,80:34,100:44,120:50,140:58,180:72,208:82,238:92}.items():
                Zg = np.arange(max(2, Zs-12), Zs+13)
                M = -(np.array([B(A, z) for z in Zg]) + Zg*(939.565-938.783))
                devs.append(int(Zg[np.argmin(M)]) - Zs)
            print(f"  [{plab}/{e_lab}] eps={eps:.3f} aA={aA:.2f}: S1 rms {np.sqrt((R**2).mean()):.1f}, heavy {np.mean(np.abs(R[hv]/Be[hv]))*100:.2f}%; S2 mean|dev| {np.mean(np.abs(devs)):.1f}")

main()
