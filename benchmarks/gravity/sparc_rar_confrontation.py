"""GRV-030 (Modeled): THE SPARC CONFRONTATION -- one prediction confirmed
with no free parameters, one prediction takes its hit, both registered.

DATA: the full SPARC Rotmod_LTG set (175 galaxies, shipped in
data/sparc_rotmod/ for reproducibility); quality cut errV/Vobs < 0.1;
standard M/L 0.5 (disk) / 0.7 (bulge); 155 galaxies, ~2800 RAR points.

(R1) PREDICTION 1 CONFIRMED AT ZERO PARAMETERS: g_dagger = c H0 / 2 pi
     = 1.083e-10 m/s^2 (H0 = 70) sits 4.5 percent from the data-fitted
     value (1.134e-10), and the RAR RMS at the PREDICTED value (0.1423
     dex) is statistically indistinguishable from the RMS at the FITTED
     value (0.1421 dex): the horizon-coupling prediction performs as
     well as letting 2788 points choose.
(R2) PREDICTION 4 TAKES A HIT, registered per house rules: the data
     prefer the simple interpolation over the canonical tanh family by
     +0.0086 dex overall (tanh's fitted g_dagger runs to 1.645e-10, 45
     percent off, compensating its shape). The deeper finding: the
     paper's 'tanh-type' was never pinned to an exact nu(y) -- the
     shape prediction was UNDEROPERATIONALIZED. Named derivation debt:
     produce the rope tension-response nu(y) explicitly, or retire the
     shape prediction. Until then Prediction 4 stands WOUNDED at a
     named test, as the house rules require.
(R3) STRUCTURAL (from the precise-gravity arc): GRV-028/029 prove the
     corpus has no galaxy-scale scalar (screened at strand range), so
     the MOND phenomenon must ride the horizon channel ALONE -- the
     framework cannot retreat to a fifth force if (R1) ever fails.
     Total observed RAR scatter at the predicted g_dagger: 0.142 dex
     (includes observational and M/L scatter).
"""
import numpy as np, glob, os

KPC = 3.086e19; KMS = 1e3


def build_rar():
    base = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'sparc_rotmod')
    pts = []; ngal = 0
    for f in sorted(glob.glob(os.path.join(base, '*_rotmod.dat'))):
        try:
            d = np.loadtxt(f)
        except Exception:
            continue
        if d.ndim == 1: d = d[None, :]
        r, Vobs, eV, Vgas, Vdisk, Vbul = d[:, 0], d[:, 1], d[:, 2], d[:, 3], d[:, 4], d[:, 5]
        m = (Vobs > 0) & (eV/np.maximum(Vobs, 1e-9) < 0.1) & (r > 0)
        if m.sum() < 3: continue
        ngal += 1
        gobs = (Vobs[m]*KMS)**2/(r[m]*KPC)
        gbar = (np.sign(Vgas[m])*Vgas[m]**2 + 0.5*Vdisk[m]**2 + 0.7*Vbul[m]**2)*KMS**2/(r[m]*KPC)
        ok = gbar > 0
        pts.append(np.stack([gbar[ok], gobs[ok]], 1))
    P = np.vstack(pts)
    return ngal, P[:, 0], P[:, 1]


def nu_simple(y): return 1.0/(1.0 - np.exp(-np.sqrt(y)))


def gpred_tanh(gb, g0):
    go = np.maximum(np.sqrt(gb*g0), gb)
    for _ in range(60):
        x = go/g0
        f = go*np.tanh(x) - gb
        go = np.maximum(go - f/(np.tanh(x) + x/np.cosh(x)**2), 1e-16)
    return go


def test():
    ngal, gbar, gobs = build_rar()
    assert ngal > 140 and len(gbar) > 2500, "full SPARC set loaded"
    H0 = 70*KMS/3.086e22
    gp = 3e8*H0/(2*np.pi)
    def rms_simple(g0): return np.sqrt(np.mean((np.log10(gobs) - np.log10(gbar*nu_simple(gbar/g0)))**2))
    def rms_tanh(g0): return np.sqrt(np.mean((np.log10(gobs) - np.log10(gpred_tanh(gbar, g0)))**2))
    r_pred = rms_simple(gp)
    g0s = gp*10**np.linspace(-0.3, 0.3, 61)
    rs = [rms_simple(g) for g in g0s]
    g_fit = g0s[int(np.argmin(rs))]; r_fit = min(rs)
    assert abs(gp/g_fit - 1) < 0.10, "P1: predicted g_dagger within 10 percent of fitted"
    assert r_pred - r_fit < 0.002, "P1: predicted-g RMS indistinguishable from fitted"
    rt = [rms_tanh(g) for g in g0s]
    assert min(rt) > r_fit + 0.004, "R2 (the registered hit): data prefer simple over tanh"
    print(f"galaxies {ngal}, points {len(gbar)}; g_pred {gp:.3e} vs fitted {g_fit:.3e} "
          f"({100*(gp/g_fit-1):+.1f}%); RMS pred/fit = {r_pred:.4f}/{r_fit:.4f} dex")
    print(f"tanh best RMS {min(rt):.4f} vs simple {r_fit:.4f}: data prefer SIMPLE (the hit, kept)")
    print("PASS: g_dagger = cH0/2pi confirmed at zero parameters on the full SPARC RAR;")
    print("      the tanh shape wounded at a named test; the horizon channel the sole carrier.")


if __name__ == "__main__":
    test()
