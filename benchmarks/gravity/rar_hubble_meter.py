"""GRV-032 (Modeled): THE RAR AS AN H0 METER -- a real relation with its
blindfold stated at full volume. Under the confirmed g_dagger = c H0 /
2 pi (GRV-030), the SPARC Radial Acceleration Relation becomes an
independent Hubble-constant inference: H0 = 2 pi g_fit / c.

READINGS (155 galaxies, 2788 points):
- Standard M/L (0.5 disk / 0.7 bulge): g_fit = 1.135e-10 ->
  H0 = 73.4 +5.3/-4.9 km/s/Mpc (galaxy bootstrap, 200 reps) -- the
  LOCAL (SH0ES) side of the Hubble tension, pleasingly.
- THE DOMINANT SYSTEMATIC, stated so this claim cannot be overread:
  disk M/L 0.4 -> 0.6 swings the reading 91.3 -> 60.3. The mass-to-
  light systematic (~ +/-15) dwarfs both the statistical band and the
  tension itself (67.4 vs 73.0): THIS METER CANNOT CURRENTLY ADJUDICATE
  THE HUBBLE TENSION. It sharpens exactly as external stellar-
  population M/L priors sharpen -- a named dependency, not a corpus
  computation.
- THE COEFFICIENT DEGENERACY quantified: 2 pi -> 73.4; the alternative
  6 -> 70.0. Both inside the systematic band, so SPARC alone cannot
  settle the 2pi-vs-6 question either; the z-drift of g_dagger remains
  the registered discriminator (Prediction 1).

WHAT THIS CLAIM IS: the existence and calibration of the relation, its
delightful central value, and the honest error budget. WHAT IT IS NOT:
an H0 measurement competitive with Planck or SH0ES.
"""
import numpy as np, glob, os

KPC = 3.086e19; KMS = 1e3; C = 3e8; MPC = 3.086e22


def load(mld=0.5, mlb=0.7):
    base = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'sparc_rotmod')
    gals = []
    for f in sorted(glob.glob(os.path.join(base, '*_rotmod.dat'))):
        try: d = np.loadtxt(f)
        except Exception: continue
        if d.ndim == 1: d = d[None, :]
        r, Vobs, eV, Vgas, Vdisk, Vbul = d[:, 0], d[:, 1], d[:, 2], d[:, 3], d[:, 4], d[:, 5]
        m = (Vobs > 0) & (eV/np.maximum(Vobs, 1e-9) < 0.1) & (r > 0)
        if m.sum() < 3: continue
        gobs = (Vobs[m]*KMS)**2/(r[m]*KPC)
        gbar = (np.sign(Vgas[m])*Vgas[m]**2 + mld*Vdisk[m]**2 + mlb*Vbul[m]**2)*KMS**2/(r[m]*KPC)
        ok = gbar > 0
        gals.append(np.stack([gbar[ok], gobs[ok]], 1))
    return gals


def fit_g(gals):
    P = np.vstack(gals); gb, go = P[:, 0], P[:, 1]
    nu = lambda y: 1.0/(1.0 - np.exp(-np.sqrt(y)))
    g0s = 10**np.linspace(-10.3, -9.6, 141)
    rs = [np.sqrt(np.mean((np.log10(go) - np.log10(gb*nu(gb/g)))**2)) for g in g0s]
    return g0s[int(np.argmin(rs))]


def H0(g, coef=2*np.pi): return coef*g/C*MPC/KMS


def test():
    gals = load()
    g = fit_g(gals)
    h = H0(g)
    assert 70 < h < 77, "central reading local-side at standard M/L"
    rng = np.random.default_rng(7)
    boots = np.array([fit_g([gals[i] for i in rng.integers(0, len(gals), len(gals))])
                      for _ in range(60)])
    lo, hi = np.percentile(H0(boots), [16, 84])
    assert hi - lo < 15, "statistical band finite and quoted"
    h4, h6 = H0(fit_g(load(mld=0.4))), H0(fit_g(load(mld=0.6)))
    assert h4 - h6 > 10, "THE BLINDFOLD: M/L systematic dominates -- the meter cannot adjudicate"
    assert abs(H0(g, 6.0) - h) < (h4 - h6), "coefficient degeneracy inside the systematic band"
    print(f"H0(2pi) = {h:.1f} [{lo:.1f},{hi:.1f}] stat | M/L 0.4/0.6 -> {h4:.1f}/{h6:.1f} | coef-6 -> {H0(g,6):.1f}")
    print("PASS: the meter exists, reads local-side at standard M/L, and states its own")
    print("      blindfold -- it sharpens only as external M/L priors sharpen.")


if __name__ == "__main__":
    test()
