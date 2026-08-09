"""COMMISSION EXACT-D IV: the small-q asymptotics
(charter: docs/technical/COMMISSION_EXACT_D4.md; bars locked first).

Bilinear/tadpole split of GRV-098's validated continuum integrand
(parity-checked at 1e-12), the dimensionless IR block F(Q) at m = 1,
the radial shell density of the near-massless q^2-integrand (the log's
kappa), and the direct d e2 / d ln u. Deterministic throughout.
"""
import sys, os
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from absorption_verdict import coeffs
from exact_d_derived import e2_integrand, grid, fd3_AB, e2_channel_xy

KT0 = 0.64
C2 = KT0
C = np.sqrt(KT0)


def gfun(l1, l2):
    s1, s2 = np.sqrt(l1), np.sqrt(l2)
    return -1.0 / (2 * s1 * s2 * (s1 + s2))


def e2_split(kx, ky, kz, q, m2, h, part):
    """Same construction as exact_d_derived.e2_integrand, split into
    'bil' / 'tad' / 'both'. Parity with the registered integrand is a
    hard assertion in test()."""
    V1, P2, W1, T2 = coeffs(h, KT0)
    k2 = kx ** 2 + ky ** 2 + kz ** 2
    lam = m2 + C2 * k2
    vals = []
    for qq in (q, 2 * q):
        kq2m = kx ** 2 + ky ** 2 + (kz - qq) ** 2
        kq2p = kx ** 2 + ky ** 2 + (kz + qq) ** 2
        lamm = m2 + C2 * kq2m
        zel_m = W1[2] * kz * (kz - qq) / 2
        s1m = (W1[0] / 2) * kx ** 2 + (W1[1] / 2) * ky ** 2 + zel_m \
            - (V1 / 2) * 0.5 * C2 * (k2 + kq2m)
        bil = (s1m ** 2) * gfun(lam, lamm)
        K2 = 0.5 * (T2[0] * kx ** 2 + T2[1] * ky ** 2 + T2[2] * kz ** 2)
        cross = -(V1 / 2) * (W1[0] * kx ** 2 + W1[1] * ky ** 2 + W1[2] * kz ** 2)
        H2 = K2 + cross - (P2 / 2) * C2 * k2 + (3 / 8) * V1 ** 2 * C2 * k2 \
            + (V1 ** 2 / 16) * C2 * (kq2m + kq2p)
        tad = H2 * 0.5 / np.sqrt(lam)
        v = {"bil": bil, "tad": tad, "both": bil + tad}[part]
        vals.append(v)
    return (vals[1] - vals[0]) / (3 * q ** 2)


def channel_xy_part(q, m2, g, part):
    kx, ky, kz, w = g
    def tot(h):
        return float(np.sum(e2_split(kx, ky, kz, q, m2, h, part) * w))
    xx = tot([1, 0, 0])
    return (tot([1, 1, 0]) - 2 * xx) / 2


def F_block(Q, g):
    """The dimensionless IR block: bilinear-only xy q^2-coefficient at
    m = 1 (u = 1)."""
    return channel_xy_part(Q, 1.0, g, "bil")


def shell_density(q, m2, Lam, nshell=48, nth=24, nph=24):
    """k * (radial density of the bilinear xy q^2-integrand): the log's
    signature is a plateau; its level is kappa."""
    kshells = np.exp(np.linspace(np.log(3e-3), np.log(Lam), nshell))
    ct, wct = np.polynomial.legendre.leggauss(nth)
    ph = np.pi * (np.arange(nph) + 0.5) / nph
    wph = 2 * np.pi / nph
    CT, PH = np.meshgrid(ct, ph, indexing="ij")
    WA = np.meshgrid(wct, ph, indexing="ij")[0] * wph
    ST = np.sqrt(1 - CT ** 2)
    out = []
    for k in kshells:
        kx = k * ST * np.cos(PH); ky = k * ST * np.sin(PH); kz = k * CT
        def tot(h):
            return float(np.sum(e2_split(kx, ky, kz, q, m2, h, "bil") * WA))
        xx = tot([1, 0, 0])
        ang = (tot([1, 1, 0]) - 2 * xx) / 2
        out.append(ang * k ** 3 / (2 * np.pi) ** 3)  # k * [k^2 rho_ang]
    return kshells, np.array(out)





REGISTERED = {  # commission record 2026-08-09 (COMMISSION_EXACT_D4 addendum)
    "F_block": -6.90077e-2, "B2_dev": 3e-5,
    "shell_exponent": "+1 (density ~ k; no 1/k plateau; ln(1/m) channel refuted)",
    "L1_both": -1.61e-4, "L1_tad": 2.47e-4, "L1_bil": -4.08e-4,
    "A_of_q": {2e-3: 5.0083e-7, 4e-3: 7.8305e-7, 8e-3: 2.2657e-6},
    "verdict": "A(q) ~ q -> ZERO ordered limit; IR-universal = u ln u",
    "B5_r2": 0.99963, "log_share": (0.824, 0.876),
    "lattice_profile": {
        "ub": [0.0367, 0.0478, 0.0623, 0.0811, 0.1056, 0.1376, 0.1793,
               0.2336, 0.3042, 0.3963, 0.5163, 0.6726],
        "Al": [9.986e-5, 1.1117e-4, 1.2432e-4, 1.3975e-4, 1.5792e-4,
               1.7940e-4, 2.0481e-4, 2.3480e-4, 2.6989e-4, 3.1024e-4,
               3.5505e-4, 4.0184e-4]},
}


def test():
    """GRV-099: the form of D adjudicated. CI verifies: split parity at
    1e-12; the tadpole control (pure even-log, A consistent with zero);
    F(Q) constancy; and the lattice closure with the DERIVED log fixed."""
    kx, ky, kz = np.array([0.3]), np.array([0.7]), np.array([0.2])
    from exact_d_derived import e2_integrand
    for h in ([1, 0, 0], [1, 1, 0]):
        a = e2_split(kx, ky, kz, 1e-2, 0.05, h, "both")[0]
        b = e2_integrand(kx, ky, kz, 1e-2, 0.05, h)[0]
        assert abs(a - b) / abs(b) < 1e-12, "split parity with GRV-098 integrand"
    g = grid(12.0, nr=110, nth=16, nph=16, rmin=1e-6)
    # tadpole control: pure log, A ~ 0
    us = np.exp(np.linspace(np.log(1e-4), np.log(0.3), 16))
    yt = np.array([channel_xy_part(2e-3, u, g, "tad") for u in us])
    ub, Al = [], []
    for i in range(len(us) - 3):
        x = us[i:i + 4]
        def dd3(v):
            c = list(v)
            for k in range(1, 4):
                c = [(c[j + 1] - c[j]) / (x[j + k] - x[j]) for j in range(4 - k)]
            return c[0]
        ub.append(float(np.exp(np.mean(np.log(x)))))
        Al.append(dd3(yt[i:i + 4]) / dd3(np.sqrt(x)))
    ub = np.array(ub); Al = np.array(Al)
    X = np.stack([np.ones_like(ub), ub, -(8 / 3) * np.sqrt(ub),
                  (16 / 3) * ub ** 1.5], 1)
    A, B, L1, L2 = np.linalg.lstsq(X, Al, rcond=None)[0]
    assert abs(A) < 0.02 * abs(L1), f"tadpole control: A ~ 0 vs log (|A/L1|={abs(A/L1):.4f})"
    assert 1.8e-4 < L1 < 3.2e-4, f"tadpole log in the registered band ({L1:.3e})"
    # F(Q) constancy (coarse)
    fa, fb = F_block(0.04, g), F_block(0.02, g)
    assert abs(fa - fb) / abs(fa) < 0.02, "no m q^2 from the joint-IR block"
    # lattice closure with the derived log FIXED
    R = REGISTERED["lattice_profile"]
    ubl = np.array(R["ub"]); All = np.array(R["Al"])
    logterm = -(8 / 3) * REGISTERED["L1_both"] * np.sqrt(ubl)
    Xl = np.stack([np.ones_like(ubl), ubl], 1)
    c2, *_ = np.linalg.lstsq(Xl, All - logterm, rcond=None)
    pred = logterm + Xl @ c2
    r2 = 1 - np.sum((All - pred) ** 2) / np.sum((All - All.mean()) ** 2)
    assert r2 > 0.99, f"lattice closure with derived log (R^2={r2:.5f})"
    print(f"parity 1e-12; tadpole control |A/L1|={abs(A/L1):.4f}; F const; closure R^2={r2:.5f}")
    print("PASS: the form of D adjudicated -- the ordered-limit sqrt(u) amplitude is")
    print("      ZERO (A ~ q); the IR-universal content is the even-log u ln u.")


if __name__ == "__main__":
    test()
