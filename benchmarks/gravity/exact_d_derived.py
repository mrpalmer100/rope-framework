"""COMMISSION EXACT-D III: the continuum response and the B-derivation
(charter: docs/technical/COMMISSION_EXACT_D3.md; bars locked first).

Continuum limit of the absorption instrument's second-order response.
Lattice elements -> exact small-k forms; the q^2 coefficient of the xy
channel evaluated with the two-point construction inside the integrand
(pointwise, no large cancellations); radial-log spherical quadrature.
h-derivative constants (V1, P2, W1, T2) come from the instrument's own
coeffs() at kt0 = 0.64. Deterministic throughout.
"""
import sys, os, json
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from absorption_verdict import coeffs

KT0 = 0.64
C2 = KT0


def gfun(l1, l2):
    s1, s2 = np.sqrt(l1), np.sqrt(l2)
    return -1.0 / (2 * s1 * s2 * (s1 + s2))


def e2_integrand(kx, ky, kz, q, m2, h):
    """Continuum per-mode contribution to [E(2q)-E(q)]/(3q^2), the
    instrument's own q^2-coefficient construction, pointwise."""
    V1, P2, W1, T2 = coeffs(h, KT0)
    k2 = kx ** 2 + ky ** 2 + kz ** 2
    lam = m2 + C2 * k2
    out = 0.0
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
        vals.append(H2 * 0.5 / np.sqrt(lam) + bil)
    return (vals[1] - vals[0]) / (3 * q ** 2)


def grid(Lam, nr=140, nth=24, nph=24, rmin=1e-5):
    """Radial-log x Gauss-Legendre angular grid with weights, measure
    d^3k/(2pi)^3."""
    s, ws = np.polynomial.legendre.leggauss(nr)
    smin, smax = np.log(rmin), np.log(Lam)
    r = np.exp(0.5 * (s + 1) * (smax - smin) + smin)
    wr = ws * 0.5 * (smax - smin) * r  # ds -> dr/r weight folded
    ct, wct = np.polynomial.legendre.leggauss(nth)
    ph = np.pi * (np.arange(nph) + 0.5) / nph  # symmetry: kx^2,ky^2 even
    wph = 2 * np.pi / nph
    R, CT, PH = np.meshgrid(r, ct, ph, indexing="ij")
    WR, WCT, _ = np.meshgrid(wr, wct, ph, indexing="ij")
    ST = np.sqrt(1 - CT ** 2)
    KX = R * ST * np.cos(PH); KY = R * ST * np.sin(PH); KZ = R * CT
    W = WR * WCT * wph * R ** 2 / (2 * np.pi) ** 3
    return KX.ravel(), KY.ravel(), KZ.ravel(), W.ravel()


def e2_channel_xy(q, m2, Lam, g=None):
    kx, ky, kz, w = g if g is not None else grid(Lam)
    def tot(h):
        return float(np.sum(e2_integrand(kx, ky, kz, q, m2, h) * w))
    xx = tot([1, 0, 0])
    return (tot([1, 1, 0]) - 2 * xx) / 2


def profile(us, Lam, q=1e-2):
    g = grid(Lam)
    return np.array([e2_channel_xy(q, u, Lam, g) for u in us])


def fd3_AB(us, ys):
    """FD3 annihilator; local (A + B u) via the exact identity, then a
    linear fit over the profile."""
    ub, Al = [], []
    for i in range(len(us) - 3):
        x = us[i:i + 4]
        def dd3(v):
            c = list(v)
            for k in range(1, 4):
                c = [(c[j + 1] - c[j]) / (x[j + k] - x[j]) for j in range(4 - k)]
            return c[0]
        ub.append(float(np.exp(np.mean(np.log(x)))))
        Al.append(dd3(ys[i:i + 4]) / dd3(np.sqrt(x)))
    lin = np.polyfit(ub, Al, 1)
    return lin[1], lin[0], np.array(ub), np.array(Al)  # A, B





REGISTERED = {  # commission record 2026-08-09 (COMMISSION_EXACT_D3 addendum)
    "B_ordered_q1e2": 1.291273e-3, "B_ordered_q3e3": 1.307497e-3,
    "A_ordered_q1e2": 2.153384e-5, "A_ordered_q3e3": 2.007044e-5,
    "B3_lambda_dev": {"A": 8e-5, "B": 2e-4},
    "recon_at_qlat": {"A_eff": 1.050602e-4, "B_eff": 4.178357e-4,
                      "lattice_A": 8.628e-5, "lattice_B": 4.826e-4},
    "B2_dev": 1.675,  # |1.291e-3 - 4.826e-4| / 4.826e-4
    "cliff": {"A_q1e3": 4.658139e-6, "A_q5e4": 3.787258e-6, "drift": 0.23},
}


def test():
    """GRV-098: the q -> 0 and m -> 0 limits DO NOT COMMUTE. The
    continuum machinery, evaluated at the lattice's own q over the
    lattice window, reproduces GRV-097's measured pair (the
    reconciliation); the q->0-first coefficients are different objects
    (B = 1.29e-3 vs measured 4.83e-4), and the true ordered-limit A is
    unpinned at a numerical precision cliff. CI re-verifies the
    reconciliation and the Lambda-stability signature on a coarse grid."""
    g6 = grid(6.0, nr=100, nth=16, nph=16, rmin=1e-5)
    g9 = grid(9.0, nr=100, nth=16, nph=16, rmin=1e-5)
    us = np.exp(np.linspace(np.log(1e-3), np.log(0.2), 10))
    A6, B6, _, _ = fd3_AB(us, np.array([e2_channel_xy(1e-2, u, 6.0, g6) for u in us]))
    A9, B9, _, _ = fd3_AB(us, np.array([e2_channel_xy(1e-2, u, 9.0, g9) for u in us]))
    assert abs(B9 - B6) / abs(B9) < 0.05, "Lambda-stability of B (coarse)"
    assert 1.0e-3 < B9 < 1.6e-3, f"ordered-limit B in the registered band (got {B9:.3e})"
    # the reconciliation: continuum at the lattice q over the lattice window
    q_lat = 2 * np.pi / 96
    lo = (3 * np.sqrt(KT0) * q_lat) ** 2
    us_l = np.exp(np.linspace(np.log(lo), np.log(1.0), 15))
    ysl = np.array([e2_channel_xy(q_lat, u, 9.0, g9) for u in us_l])
    _, B_eff, _, _ = fd3_AB(us_l, ysl)
    dev = abs(B_eff - 4.826e-4) / 4.826e-4
    assert dev < 0.30, f"reconciliation with GRV-097's measured B (dev {dev:.2%})"
    print(f"B(Lam=6,9) = {B6:.4e}, {B9:.4e}; reconciliation B_eff = {B_eff:.4e} (dev {dev:.1%})")
    print("PASS: non-commuting limits verified -- the finite-q object matches the")
    print("      lattice; the ordered-limit object differs; GRV-098's record stands.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        us = np.exp(np.linspace(np.log(1e-4), np.log(0.2), 20))
        for Lam in (6.0, 12.0):
            ys = profile(us, Lam)
            A, B, _, _ = fd3_AB(us, ys)
            print(f"Lambda={Lam}: A = {A:.6e}   B = {B:.6e}")
    else:
        test()
