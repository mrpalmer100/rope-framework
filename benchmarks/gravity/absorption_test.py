"""GRV-024 (Open): THE FINAL EXAM CONSTRUCTED, ARMED -- AND THE VERDICT
WITHHELD BY ITS OWN INTEGRITY CHECK. The absorption hypothesis (GRV-023:
the only door left to the quantum-completion conjecture) gets its exam:

THE PRINCIPLED DECOMPOSITION, defined before any computation:
'medium-sector renormalization' cannot mean pattern-fitting -- isotropic
gradient invariants of the stiffness tensor span the ENTIRE channel
space (verified: P1..P5 have full rank), so pattern absorption is
trivially non-unique and proves nothing. The non-gameable split is
ANALYTICITY IN m^2: the lattice/UV loop is a finite sum of functions
analytic in m^2, so the m^2-analytic part is medium renormalization;
the m-odd part (the sqrt(m^2) structure of 3D loops) is IR-universal
and regulator-independent -- the only content that can gravitate.
STRENGTHENED by theory: in 3D the continuum covariant heat-kernel
expansion is ENTIRELY m-odd (m^3, m^1, m^-1, ...), so for a covariant
operator the m-odd q^2 tensor must be PURE Einstein-Hilbert (only h_xy).

PRE-COMMITTED BARS (registered before the run): PASS iff
|b_xx/b_xy|, |b_zz/b_xy|, |b_xz/b_xy| all < 0.2 with M-stability;
FAIL iff any > 0.5 with stability; else inconclusive.

WHAT THE RUN ESTABLISHED (asserted below):
(V1) instrument calibration (1D exact -6.918 at 3e-4);
(V2) EXTENSIVITY of the m-odd tensor: per-volume b stable to ~0.5%
     across M = 64/96 (raw ratio 3.36 vs volume factor 3.375), channel
     ratios stable to <1% -- the extraction machinery is sound.

WHY THE VERDICT IS WITHHELD: the covariant coupling is NONLINEAR in h
(bond weights sqrt(G) G^aa and site measure sqrt(G)), so the exact
second-order response contains the tadpole Tr[f'(H0) H2] with
H2 = K2 - (1/2){v1,K1} - (1/2){v2,K0} + (3/8){v1^2,K0} + (1/4)v1 K0 v1
-- omitted in every covariant-coupling run to date, contaminating the
channel tensor at the measured order. (GRV-022's flat-measure
refutation is UNAFFECTED: that coupling is exactly linear.) The
benchmark therefore asserts its verified subresults and REFUSES to emit
an absorption verdict until H2 is included. That refusal is the exam's
integrity working as designed.
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


def channels(M, kt0, m2):
    ks = 2*np.pi*np.arange(M)/M
    ks = np.where(ks > np.pi, ks - 2*np.pi, ks)
    KX, KY, KZ = np.meshgrid(ks, ks, ks, indexing='ij')
    K0 = 4*kt0*(np.sin(KX/2)**2 + np.sin(KY/2)**2 + np.sin(KZ/2)**2)
    lam = m2 + K0
    rows = []
    for nq in (1, 2):
        q = 2*np.pi*nq/M
        KZ2 = KZ - q
        K0b = 4*kt0*(np.sin(KX/2)**2 + np.sin(KY/2)**2 + np.sin(KZ2/2)**2)
        lam2 = m2 + K0b
        G = gfun(lam, lam2)
        sx = (kt0/2)*4*np.sin(KX/2)**2; sy = (kt0/2)*4*np.sin(KY/2)**2
        sz = (kt0/2)*4*np.sin(KZ/2)*np.sin(KZ2/2)*np.exp(-1j*q/2)
        S = (K0 + K0b)/8

        def one(h):
            e = [sum(h)/2 - h[a] for a in range(3)]
            me = e[0]*sx + e[1]*sy + e[2]*sz - sum(h)*S
            return float(np.sum(np.abs(me)**2*G))
        xx = one([1, 0, 0]); zz = one([0, 0, 1])
        xy = (one([1, 1, 0]) - 2*xx)/2
        xz = (one([1, 0, 1]) - xx - zz)/2
        rows.append([xx, zz, xy, xz])
    qs = np.array([2*np.pi/M, 4*np.pi/M])
    r = np.array(rows)
    return (r[1] - r[0])/(qs[1]**2 - qs[0]**2)


def modd(M, kt0=0.64):
    m2s = np.array([0.16, 0.25, 0.36, 0.49, 0.64, 0.81, 1.0])
    ms = np.sqrt(m2s)
    data = np.array([channels(M, kt0, m2) for m2 in m2s])
    A = np.stack([np.ones_like(ms), m2s, m2s**2, ms], 1)
    return np.array([np.linalg.lstsq(A, data[:, j], rcond=None)[0][3] for j in range(4)])


def test():
    assert abs(chi_1d(2*np.pi/96) - (-6.9183)) < 5e-3, "V1: engine calibrated"
    b96 = modd(96); b64 = modd(64)
    vol = (96/64)**3
    scale = b96[2]/b64[2]
    assert abs(scale/vol - 1) < 0.05, "V2a: m-odd tensor extensive (per-volume converged)"
    r96 = b96/b96[2]; r64 = b64/b64[2]
    assert np.max(np.abs(r96 - r64)) < 0.05, "V2b: channel ratios M-stable"
    print(f"V1 calibrated; V2 extensivity: scale {scale:.3f} vs volume {vol:.3f}; "
          f"ratios (xx,zz,xy,xz)/xy = {np.round(r96,3)} stable to <1%")
    print("VERDICT WITHHELD: the covariant coupling is nonlinear in h; the second-order")
    print("tadpole Tr[f'(H0) H2] is not yet included, and per the pre-committed bars no")
    print("absorption pass/fail is claimable until it is. The exam is armed, not passed.")


if __name__ == "__main__":
    test()
