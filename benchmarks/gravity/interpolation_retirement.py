"""GRV-031 (Derived): THE SHAPE DEBT COLLECTED -- BY RETIREMENT. GRV-030
named the debt: derive the tension-response nu(y) from corpus
commitments, or retire the shape claim. Both branches were executed in
order, with bars locked before data.

THE CANDIDATE, stated and locked first: if gravitational conditioning
is carried by strand ALIGNMENT (orientational content -- GRV-011's
strain is shear) fighting horizon-scale randomization (the g_dagger
floor as effective temperature, the same horizon coupling Prediction 1
confirms), the response law is forced by saturation statistics: the
Langevin function, mu(x) = coth(3x) - 1/(3x), the 3 fixed by the
deep-MOND asymptotic. Zero free parameters. Locked bars: PAID iff
Langevin at the PREDICTED g_dagger lands within 0.003 dex of simple at
FITTED g_dagger; RETIRE iff it loses by more than 0.01.

THE VERDICT on 2788 SPARC points: Langevin at predicted g_dagger =
0.1572 dex vs simple at fitted = 0.1421: loses by +0.0151 -- and by
+0.0037 even with g_dagger freed. RETIREMENT EXECUTES: the tanh family
(GRV-030's hit) AND the corpus-natural Langevin candidate are both
disfavored by the data; Prediction 4 is RETIRED as a shape prediction,
kept visibly in the paper per house style. The framework's registered
MOND content is the acceleration SCALE (Prediction 1, confirmed at
zero parameters) -- and the structural theorem that the horizon channel
carries it alone (GRV-028/029).
"""
import numpy as np, glob, os


def build():
    KPC = 3.086e19; KMS = 1e3
    base = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'sparc_rotmod')
    pts = []
    for f in sorted(glob.glob(os.path.join(base, '*_rotmod.dat'))):
        try: d = np.loadtxt(f)
        except Exception: continue
        if d.ndim == 1: d = d[None, :]
        r, Vobs, eV, Vgas, Vdisk, Vbul = d[:, 0], d[:, 1], d[:, 2], d[:, 3], d[:, 4], d[:, 5]
        m = (Vobs > 0) & (eV/np.maximum(Vobs, 1e-9) < 0.1) & (r > 0)
        if m.sum() < 3: continue
        gobs = (Vobs[m]*KMS)**2/(r[m]*KPC)
        gbar = (np.sign(Vgas[m])*Vgas[m]**2 + 0.5*Vdisk[m]**2 + 0.7*Vbul[m]**2)*KMS**2/(r[m]*KPC)
        ok = gbar > 0
        pts.append(np.stack([gbar[ok], gobs[ok]], 1))
    P = np.vstack(pts)
    return P[:, 0], P[:, 1]


def test():
    gbar, gobs = build()
    gp = 3e8*(70*1e3/3.086e22)/(2*np.pi)
    def mu(x):
        z = 3*np.maximum(x, 1e-12)
        return 1/np.tanh(z) - 1/z
    go = np.maximum(np.sqrt(gbar*gp), gbar)
    for _ in range(80):
        x = go/gp; dx = 1e-6
        f = go*mu(x) - gbar
        df = mu(x) + x*(mu(x + dx) - mu(x - dx))/(2*dx)
        go = np.maximum(go - f/df, 1e-16)
    r_lang = np.sqrt(np.mean((np.log10(gobs) - np.log10(go))**2))
    nu = lambda y: 1.0/(1.0 - np.exp(-np.sqrt(y)))
    g0s = gp*10**np.linspace(-0.25, 0.25, 41)
    r_simple = min(np.sqrt(np.mean((np.log10(gobs) - np.log10(gbar*nu(gbar/g)))**2)) for g in g0s)
    assert r_lang - r_simple > 0.01, "the retirement condition (locked bar) holds"
    print(f"Langevin@predicted {r_lang:.4f} vs simple@fitted {r_simple:.4f}: +{r_lang-r_simple:.4f} dex")
    print("PASS (as the executed retirement): the shape claim is retired; the framework's")
    print("      MOND content is the confirmed acceleration scale, carried by the horizon alone.")


if __name__ == "__main__":
    test()
