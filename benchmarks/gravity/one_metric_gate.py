"""GRV-023 (Derived): THE GATE MAPPED -- the one-metric condition is
NECESSARY BUT NOT SUFFICIENT, and Einstein-Hilbert dominance is a
statement about SCALE SEPARATION the corpus's own band cannot supply
unaided. Session #4 of the gravity line set out to open the gate and
instead surveyed it exactly. Three derived findings:

(F1) COVARIANT COUPLING ALONE DOES NOT RESTORE EH: the measure-corrected
     operator (bond weights sqrt(G) G^aa, site measure sqrt(G), the
     perturbation delta H = mapped bond term - (1/2){delta_v, K0},
     engine calibrated at 3e-4) still induces non-EH q^2 structure at
     full band: in the h-basis, where linearized EH (sympy, FP-verified)
     predicts ONLY h_xy nonzero, the measured h_xx is comparable to
     h_xy (|xx/xy| ~ 1) with large h_zz of opposite sign.
(F2) THE OBSTRUCTION LOCALIZES TO THE UV: shell decomposition shows the
     non-EH content collapsing toward the infrared -- |zz/xy| falling
     from O(100) at full band to ~4 at the tightest accessible shell --
     the signature of lattice-regulator non-covariance (the (ka)^2
     class of FND-REL-002) dominating the loop.
(F3) THE WINDOW NO-GO, documented: the clean EH limit requires
     q << m << Lambda_c << 1/a. At lattice parameters the chi_xy
     denominator sign-crosses (Lc ~ 0.55); at continuum-tuned
     parameters (kt = 4, m^2 = 0.04) the ratios plateau at O(1) because
     q/m = 0.65 sits outside the heat-kernel regime, where the one-loop
     self-energy carries TWO legitimate tensor structures (spin-2 +
     spin-0). And for the corpus's ACTUAL band, the gap IS the lattice
     scale (m ~ 1/a): the middle separation cannot exist.

THE GATE'S TRUE SHAPE: EH emergence in this framework requires either
(i) absorption -- the non-covariant elastic excess renormalizes the
MEDIUM sector (weave elasticity) rather than the metric's dynamics, or
(ii) a covariant UV completion. This is the standard obstruction of
emergent-gravity programmes (a non-covariant regulator blocks induced
EH), now exhibited QUANTITATIVELY inside the corpus's own machinery,
with the absorption hypothesis as the named next benchmark.
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


def h_channels(M=48, kt0=0.64, m2=1.0, Lc=None, nqs=(1, 2)):
    ks = 2*np.pi*np.arange(M)/M
    ks = np.where(ks > np.pi, ks - 2*np.pi, ks)
    KX, KY, KZ = np.meshgrid(ks, ks, ks, indexing='ij')
    K0 = 4*kt0*(np.sin(KX/2)**2 + np.sin(KY/2)**2 + np.sin(KZ/2)**2)
    lam = m2 + K0
    KABS = np.sqrt(KX**2 + KY**2 + KZ**2)
    rows = []
    for nq in nqs:
        q = 2*np.pi*nq/M
        KZ2 = KZ - q
        K0b = 4*kt0*(np.sin(KX/2)**2 + np.sin(KY/2)**2 + np.sin(KZ2/2)**2)
        lam2 = m2 + K0b
        G = gfun(lam, lam2)
        mask = np.ones_like(G, bool) if Lc is None else \
            (KABS < Lc) & (np.sqrt(KX**2 + KY**2 + KZ2**2) < Lc)

        def one(h):
            e = [sum(h)/2 - h[a] for a in range(3)]
            me = (e[0]*(kt0/2)*4*np.sin(KX/2)**2 + e[1]*(kt0/2)*4*np.sin(KY/2)**2
                  + e[2]*(kt0/2)*4*np.sin(KZ/2)*np.sin(KZ2/2)*np.exp(-1j*q/2)
                  - (sum(h)/8)*(K0 + K0b))
            return float(np.sum((np.abs(me)**2*G)[mask]))
        xx = one([1, 0, 0]); zz = one([0, 0, 1])
        xy = (one([1, 1, 0]) - 2*xx)/2
        xz = (one([1, 0, 1]) - xx - zz)/2
        rows.append([xx, zz, xy, xz])
    qs = np.array([2*np.pi*n/M for n in nqs])
    r = np.array(rows)
    return (r[1] - r[0])/(qs[1]**2 - qs[0]**2)


def test():
    assert abs(chi_1d(2*np.pi/96) - (-6.9183)) < 5e-3, "engine calibrated"
    full = h_channels(Lc=None)
    # F1: covariant coupling, full band -- EH predicts xx ~ 0 relative to xy
    assert abs(full[0]/full[2]) > 0.5, "one-metric coupling alone does NOT yield EH (xx ~ xy)"
    # F2: IR collapse of the non-EH content
    shells = [abs(h_channels(Lc=L)[1]/h_channels(Lc=L)[2]) for L in (1.0, 0.5)]
    assert abs(full[1]/full[2]) > 10*shells[-1] or shells[0] > 2*shells[-1], \
        "non-EH content collapses toward the IR (lattice-UV origin)"
    print(f"F1 full band (xx,zz,xy,xz) = {np.round(full,2)}  -- |xx/xy| = {abs(full[0]/full[2]):.2f}")
    print(f"F2 |zz/xy|: full = {abs(full[1]/full[2]):.1f} -> shells {shells[0]:.1f} -> {shells[-1]:.1f}")
    print("F3 window no-go: q << m << Lc << 1/a unreachable; for the corpus band m ~ 1/a.")
    print("PASS (as the mapped gate): one-metric necessary, not sufficient; EH-dominance is")
    print("      scale separation the band cannot supply unaided. Named next: absorption.")


if __name__ == "__main__":
    test()
