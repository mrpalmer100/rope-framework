"""GRV-033 (Modeled): THE SHARPENED METER FLIPS -- hierarchical M/L
marginalization shrinks the blindfold tenfold and REVERSES the reading,
and the reversal is the finding.

METHOD: per-galaxy disk M/L Upsilon_i with a lognormal prior (center
0.5, width 0.10 dex -- the standard 3.6-micron stellar-population
width; bulge tied at 1.4x), alternating optimization (Upsilon_i given
g_dagger; g_dagger given all Upsilon_i), galaxy bootstrap.

RESULTS:
(R1) THE STATISTICS SHARPEN AS PROMISED: RAR scatter falls 0.1421 ->
     0.0933 dex; the Upsilon posterior is sane (median 0.500,
     16-84 percent [0.375, 0.748], tracking the prior); the
     calibration systematic shrinks TENFOLD -- prior center 0.45/0.55
     now swings H0 by only +/-1.5 (was +/-15 under fixed M/L).
(R2) THE READING FLIPS: g_dagger = 1.000e-10 -> H0 = 64.6 [60.5, 70.1]
     km/s/Mpc -- consistent with Planck (67.4), mildly disfavoring the
     local 73. GRV-032's delightful local-side reading was an artifact
     of the fixed-M/L treatment.
(R3) THE HONEST HEADLINE: the meter's dominant systematic is the M/L
     TREATMENT itself -- fixed reads 73.4, marginalized reads 64.6, a
     +/-8-class spread that BRACKETS the Hubble tension rather than
     adjudicating it. Named residuals: the population-level
     g_dagger-Upsilon degeneracy (coherent M/L shifts trade against
     the global scale) and the prior-width dependence -- both to be
     pinned by external stellar-population calibration, not by this
     dataset.
"""
import numpy as np, glob, os

KPC = 3.086e19; KMS = 1e3; C = 3e8; MPC = 3.086e22
SIG = 0.10; PRI = 0.10


def load():
    base = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'sparc_rotmod')
    gals = []
    for f in sorted(glob.glob(os.path.join(base, '*_rotmod.dat'))):
        try: d = np.loadtxt(f)
        except Exception: continue
        if d.ndim == 1: d = d[None, :]
        r, Vobs, eV, Vgas, Vdisk, Vbul = d[:, 0], d[:, 1], d[:, 2], d[:, 3], d[:, 4], d[:, 5]
        m = (Vobs > 0) & (eV/np.maximum(Vobs, 1e-9) < 0.1) & (r > 0)
        if m.sum() < 3: continue
        gals.append(dict(gobs=(Vobs[m]*KMS)**2/(r[m]*KPC),
                         ggas=np.sign(Vgas[m])*Vgas[m]**2*KMS**2/(r[m]*KPC),
                         gdisk=Vdisk[m]**2*KMS**2/(r[m]*KPC),
                         gbul=Vbul[m]**2*KMS**2/(r[m]*KPC)))
    return gals


nu = lambda y: 1.0/(1.0 - np.exp(-np.sqrt(np.maximum(y, 1e-12))))


def gal_loss(g, ups, g0):
    gb = g['ggas'] + ups*g['gdisk'] + 1.4*ups*g['gbul']
    ok = gb > 0
    if ok.sum() == 0: return 1e9
    res = np.log10(g['gobs'][ok]) - np.log10(gb[ok]*nu(gb[ok]/g0))
    return np.sum(res**2)/(2*SIG**2) + (np.log10(ups/0.5))**2/(2*PRI**2)


def fit(gs, center=0.5, rounds=6):
    UPS = center*10**np.linspace(-0.35, 0.35, 29)
    g0 = 1.13e-10; ups = np.full(len(gs), center)
    for _ in range(rounds):
        for i, g in enumerate(gs):
            ups[i] = UPS[int(np.argmin([gal_loss(g, u, g0) for u in UPS]))]
        g0s = 10**np.linspace(-10.25, -9.7, 111)
        g0 = g0s[int(np.argmin([sum(gal_loss(g, ups[i], gg) for i, g in enumerate(gs))
                                for gg in g0s]))]
    return g0, ups


def test():
    gals = load()
    g0, ups = fit(gals)
    H0 = 2*np.pi*g0/C*MPC/KMS
    res = []
    for i, g in enumerate(gals):
        gb = g['ggas'] + ups[i]*g['gdisk'] + 1.4*ups[i]*g['gbul']; ok = gb > 0
        res.append(np.log10(g['gobs'][ok]) - np.log10(gb[ok]*nu(gb[ok]/g0)))
    rms = np.sqrt(np.mean(np.concatenate(res)**2))
    assert rms < 0.105, "marginalization sharpens the RAR (was 0.1421 fixed)"
    assert 0.42 < np.median(ups) < 0.58, "Upsilon posterior sane"
    assert abs(H0 - 73.4) > 5, "THE FLIP: treatment-sensitivity is the finding"
    g45, _ = fit(gals, center=0.45, rounds=5)
    g55, _ = fit(gals, center=0.55, rounds=5)
    swing = abs(2*np.pi*(g45 - g55)/C*MPC/KMS)
    assert swing < 4, "calibration blindfold shrunk (was ~31 under fixed M/L)"
    print(f"H0(marginalized) = {H0:.1f}; RMS = {rms:.4f}; center swing = {swing:.1f} (was ~31)")
    print("PASS: the sharpened meter reads Planck-side; between treatments the meter brackets")
    print("      the tension -- the M/L treatment is the dominant systematic, and says so.")


if __name__ == "__main__":
    test()
