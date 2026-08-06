import numpy as np
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "explorations"))
sys.path.insert(0, str(ROOT / "benchmarks" / "em"))
import nuc_a_asymmetry as na
from atomic_mass_predictor import structure_constants, calibrate_aV, D0

E2 = 1.44
R0N = (3 / (4 * np.pi * np.sqrt(2)))**(1/3) * D0
XI = D0 / 1.36
A_D = XI / 2.0
RHO0 = 3.0 / (4 * np.pi * R0N**3)

def coulomb_fermi(Z, A):
    rho_p0 = (Z / A) * RHO0
    Ru = (3 * Z / (4 * np.pi * rho_p0))**(1/3)
    r = np.linspace(1e-3, Ru + 12 * A_D, 4000)
    def charge(Rh):
        rho = rho_p0 / (1 + np.exp((r - Rh) / A_D))
        return np.trapezoid(4 * np.pi * r**2 * rho, r), rho
    lo, hi = 0.2 * Ru, 2.0 * Ru
    for _ in range(60):
        Rh = 0.5 * (lo + hi)
        Q, rho = charge(Rh)
        lo, hi = (Rh, hi) if Q < Z else (lo, Rh)
    q_in = np.concatenate([[0], np.cumsum(0.5 * (4*np.pi*r[1:]**2*rho[1:] + 4*np.pi*r[:-1]**2*rho[:-1]) * np.diff(r))])
    outer = np.concatenate([np.cumsum((4*np.pi*r*rho)[::-1][:-1] * np.diff(r)[::-1])[::-1], [0]])
    phi = E2 * (q_in / r + outer)
    E = 0.5 * np.trapezoid(rho * phi * 4 * np.pi * r**2, r)
    E_uniform = 0.6 * E2 * Z**2 / Ru
    return E, E_uniform

def exchange_hole(Z, A, depth=1.0):
    rho_p = (Z / A) * RHO0
    r_h = (3 / (4 * np.pi * rho_p))**(1/3)
    per_proton = 0.5 * depth * rho_p * E2 * 2 * np.pi * r_h**2
    return Z * per_proton

def corrected_EC(A, Z, depth=1.0):
    Ef, Eu = coulomb_fermi(Z, A)
    return Ef - exchange_hole(Z, A, depth)

def binding_corrected(A, Z, aV, aSaV, aA, depth=1.0):
    return (aV * A - aSaV * aV * A**(2/3) - corrected_EC(A, Z, depth) - aA * (A - 2 * Z)**2 / A)

def main():
    aSaV, aC0 = structure_constants()
    aV = calibrate_aV(aSaV, aC0)
    print(f"r0={R0N:.3f}, xi={XI:.3f}, a_d=xi/2={A_D:.3f}, rho0={RHO0:.4f}, uniform a_C={aC0:.3f}\n")
    line = [(40,20),(60,28),(80,34),(100,44),(120,50),(140,58),(180,72),(208,82),(238,92)]
    print("== effective a_C across stable line ==")
    for depth, lab in ((1.0, "C1 full-depth"), (0.424, "C2 (1-eta)-depth")):
        effs = np.array([corrected_EC(A, Z, depth) * A**(1/3) / Z**2 for A,Z in line])
        print(f"  {lab}: a_C = {effs.min():.3f}-{effs.max():.3f} (median {np.median(effs):.3f}) -> {'IN 0.68-0.75' if 0.68<=np.median(effs)<=0.75 else 'OUT'}")
    Ef, Eu = coulomb_fermi(82, 208)
    print(f"  Pb-208: uniform {Eu:.0f} -> diffuse {Ef:.0f} ({(Ef/Eu-1)*100:+.1f}%), exchange -{exchange_hole(82,208):.0f} ({-exchange_hole(82,208)/Eu*100:.1f}%)\n")
    print("== SECOND PREDICTIONS ==")
    nucs = na.load_table()
    for aA, alab in ((18.52, "B1"), (19.85, "B2")):
        for depth, clab in ((1.0, "C1"), (0.424, "C2")):
            R = np.array([binding_corrected(A, Z, aV, aSaV, aA, depth) - Bexp for sym,A,Z,Bexp in nucs])
            Be = np.array([b for *_, b in nucs])
            Aarr = np.array([a for _, a, _, _ in nucs], float)
            hv = Aarr > 150
            devs = []
            for A, Zs in dict(line).items():
                Zg = np.arange(max(2, Zs-15), Zs+16)
                M = -(np.array([binding_corrected(A, z, aV, aSaV, aA, depth) for z in Zg]) + Zg*(939.565-938.783))
                devs.append(int(Zg[np.argmin(M)]) - Zs)
            print(f"  [{alab}+{clab}] S1: rms {np.sqrt((R**2).mean()):.1f}, heavy {np.mean(np.abs(R[hv]/Be[hv]))*100:.2f}%  |  S2 mean|dev| {np.mean(np.abs(devs)):.1f}, U238 {devs[-1]}")
    # the regression diagnostic: is the S1 rms mostly a smooth volume+surface shape?
    print("\n== S1 regression diagnostic (B2+C2) ==")
    R = np.array([binding_corrected(A, Z, aV, aSaV, 19.85, 0.424) - Bexp for sym,A,Z,Bexp in nucs])
    Aarr = np.array([a for _, a, _, _ in nucs], float)
    # fit residual to smooth volume+surface shape: c0*A + c1*A^(2/3)
    X = np.vstack([Aarr, Aarr**(2/3)]).T
    coef, *_ = np.linalg.lstsq(X, R, rcond=None)
    smooth = X @ coef
    resid = R - smooth
    smooth_frac = 1 - np.var(resid)/np.var(R)
    print(f"  raw rms {np.sqrt((R**2).mean()):.1f}; smooth vol+surf explains {smooth_frac*100:.1f}%; residual rms {np.sqrt((resid**2).mean()):.1f}")
    print(f"  implied surface correction: a_S/a_V shift direction (diffuse raises it)")

main()
