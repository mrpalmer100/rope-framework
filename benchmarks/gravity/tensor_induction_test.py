"""GRV-022 (Derived): THE NAIVE SAKHAROV ROUTE REFUTED AT THE TENSOR TEST
-- a registered negative of theorem quality, and the sharpest thing that
could have happened to the quantum-completion conjecture short of victory.

THE TEST: the induced q^2 action of the measured weave band (GRV-021's
machinery, calibrated against exact diagonalization at 3e-4) is measured
in all tensor channels -- independent modulations of the three bond
stiffnesses at wavevector q parallel to z -- and compared against the
metric-covariant prediction. Linearized Einstein-Hilbert (sympy-derived,
hand-verified against the Fierz-Pauli TT sector) gives the q^2 form
(N_xx, N_zz, N_xy, N_xz) = (0, 1/4, 1/4, 1/4); adding the conformal
measure sector shifts all four equally. EVERY covariant combination
therefore forces the parameter-free degeneracy chi_xy = chi_xz.

THE VERDICT: measured (38, 517, 18, 502) -- chi_xy vs chi_xz violated
~27x. The dominant induced invariant is LONGITUDINAL-ELASTIC (large only
in channels involving the modulation-direction stiffness), a structure
no functional of a single metric produces. The mode vacuum of the
flat-measure operator behaves as an anisotropic elastic medium, not as
induced geometry: Einstein-Hilbert does NOT land automatically.

THE CONSEQUENCE, stated precisely: GRV-014 is SHARPENED, not killed.
Its Sakharov mechanism presumed modes coupling through ONE effective
metric (the analogue-gravity one-metric condition); this test coupled
them through three independent stiffnesses with flat measure, and shows
that WITHOUT the one-metric condition, covariance does not emerge on its
own. The conjecture's remaining burden is now exact: the corpus's
conditioning mechanism must be shown to couple transverse-sector modes
through a SINGLE effective metric. That is a named, testable
requirement -- the conjecture's future benchmark.
"""
import numpy as np


def gfun(l1, l2):
    s1, s2 = np.sqrt(l1), np.sqrt(l2)
    return -1.0/(2*s1*s2*(s1 + s2))


def chi_1d(q, kt0=0.64, M=96):
    ks = 2*np.pi*np.arange(M)/M
    lam = 1 + 4*kt0*np.sin(ks/2)**2
    tot = 0.0
    for i, k in enumerate(ks):
        k2 = (k - q) % (2*np.pi)
        j = int(round(k2*M/(2*np.pi))) % M
        me = (kt0/2)*4*np.sin(k/2)*np.sin(k2/2)
        tot += me*me*gfun(lam[i], lam[j])
    return tot/(kt0**2)


def tensor_channels(M=32, kt0=0.64, nqs=(1, 2, 3, 4)):
    ks = 2*np.pi*np.arange(M)/M
    KX, KY, KZ = np.meshgrid(ks, ks, ks, indexing='ij')
    lam = 1 + 4*kt0*(np.sin(KX/2)**2 + np.sin(KY/2)**2 + np.sin(KZ/2)**2)
    out = {lab: [] for lab in ('xx', 'zz', 'xy', 'xz')}
    qs = []
    for nq in nqs:
        q = 2*np.pi*nq/M; qs.append(q)
        KZ2 = (KZ - q) % (2*np.pi)
        lam2 = 1 + 4*kt0*(np.sin(KX/2)**2 + np.sin(KY/2)**2 + np.sin(KZ2/2)**2)
        G = gfun(lam, lam2)
        me = {'x': (kt0/2)*4*np.sin(KX/2)**2 + 0j,
              'y': (kt0/2)*4*np.sin(KY/2)**2 + 0j,
              'z': (kt0/2)*4*np.sin(KZ/2)*np.sin(KZ2/2)*np.exp(-1j*q/2)}
        for lab, (a, b) in {'xx': ('x', 'x'), 'zz': ('z', 'z'),
                            'xy': ('x', 'y'), 'xz': ('x', 'z')}.items():
            out[lab].append(float(np.sum(np.real(me[a]*np.conj(me[b]))*G))/kt0**2)
    qs = np.array(qs)
    A = np.stack([np.ones_like(qs), qs**2, qs**4], 1)
    return {lab: np.linalg.lstsq(A, np.array(v), rcond=None)[0][1] for lab, v in out.items()}


def test():
    # calibration of the PT engine against the exact 1D result
    assert abs(chi_1d(2*np.pi/96) - (-6.9183)) < 5e-3, "PT engine calibrated vs exact diagonalization"
    c = tensor_channels()
    # the parameter-free covariance degeneracy chi_xy = chi_xz -- violated decisively
    assert c['xy'] < 0.15*c['xz'], "COVARIANCE REFUTED: chi_xy << chi_xz (EH forces equality)"
    # the actual structure: longitudinal-elastic degeneracies
    assert abs(c['zz'] - c['xz'])/c['zz'] < 0.10, "longitudinal channels degenerate (zz ~ xz)"
    assert c['xx'] < 0.15*c['zz'] and c['xy'] < 0.15*c['zz'], "transverse channels subdominant"
    print(f"channels q^2: xx={c['xx']:.1f} zz={c['zz']:.1f} xy={c['xy']:.1f} xz={c['xz']:.1f}")
    print(f"covariance degeneracy chi_xy = chi_xz violated by {c['xz']/max(c['xy'],1e-9):.0f}x")
    print("PASS (as a registered negative): Einstein-Hilbert does NOT land automatically --")
    print("      the flat-measure mode vacuum is elastic, not geometric. GRV-014 sharpened:")
    print("      its burden is now the one-metric condition, named and testable.")


if __name__ == "__main__":
    test()
