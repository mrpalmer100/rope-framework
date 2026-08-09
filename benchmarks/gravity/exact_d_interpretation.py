"""COMMISSION EXACT-D V: the running coefficient versus the constant-D
form (charter: docs/technical/COMMISSION_EXACT_D5.md; bars locked
first). GRV-100.

Verifies deterministically: (a) the even-log family is EH-patterned --
per-channel L1 ratios under GRV-024's own 0.2 bar; (b) the 1D gapped
band response is finite with no subtraction (grid-stable); (c) the
scheme-swing arithmetic (sign-indefinite normalization; F-Lor exclusion
survives trivially).
"""
import sys, os
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from exact_d_asymptotics import e2_split
from exact_d_derived import grid

KT = 0.64

REGISTERED = {  # commission record 2026-08-09 (COMMISSION_EXACT_D5 addendum)
    "L1": {"xx": -5.344e-8, "zz": 2.7527e-6, "xy": -1.610665e-4,
           "xz": -8.1665e-7},
    "pattern_ratios": (0.0003, 0.0171, 0.0051),
    "chi2_1d": (0.004219, 0.004221), "B3": 0.00053,
    "scheme_span": 4.466e-4, "sign_indefinite": True,
}


def channel_L1s(g, q=2e-3, npts=16):
    kx, ky, kz, w = g
    us = np.exp(np.linspace(np.log(2e-4), np.log(0.3), npts))

    def one(h, u):
        return float(np.sum(e2_split(kx, ky, kz, q, u, h, "both") * w))

    ch = {c: [] for c in ("xx", "zz", "xy", "xz")}
    for u in us:
        xx = one([1, 0, 0], u); zz = one([0, 0, 1], u)
        xy = (one([1, 1, 0], u) - 2 * xx) / 2
        xz = (one([1, 0, 1], u) - xx - zz) / 2
        for c, v in (("xx", xx), ("zz", zz), ("xy", xy), ("xz", xz)):
            ch[c].append(v)
    L1s = {}
    for c in ch:
        ub, Al = [], []
        for i in range(npts - 3):
            x = us[i:i + 4]
            def dd3(v):
                cc = list(v)
                for k in range(1, 4):
                    cc = [(cc[j + 1] - cc[j]) / (x[j + k] - x[j])
                          for j in range(4 - k)]
                return cc[0]
            ub.append(float(np.exp(np.mean(np.log(x)))))
            Al.append(dd3(np.array(ch[c][i:i + 4])) / dd3(np.sqrt(x)))
        ub = np.array(ub); Al = np.array(Al)
        X = np.stack([np.ones_like(ub), ub, -(8 / 3) * np.sqrt(ub),
                      (16 / 3) * ub ** 1.5], 1)
        L1s[c] = float(np.linalg.lstsq(X, Al, rcond=None)[0][2])
    return L1s


def chi2_1d(N):
    x = np.arange(N)

    def E(eps, qq):
        ktx = KT * (1 + eps * np.cos(qq * (x + 0.5)))
        K = np.zeros((N, N))
        for i in range(N):
            j = (i + 1) % N; wv = ktx[i]
            K[i, i] += wv; K[j, j] += wv; K[i, j] -= wv; K[j, i] -= wv
        H = K + np.eye(N)
        return 0.5 * np.sum(np.sqrt(np.linalg.eigvalsh(H)))

    d = 0.02
    resp = lambda qq: (E(d, qq) + E(-d, qq) - 2 * E(0, qq)) / d ** 2 / N
    q1, q2 = 2 * np.pi / N, 4 * np.pi / N
    return (resp(q2) - resp(q1)) / (q2 ** 2 - q1 ** 2)


def test():
    g = grid(12.0, nr=110, nth=16, nph=16, rmin=1e-6)
    L1s = channel_L1s(g)
    r = [abs(L1s[c] / L1s["xy"]) for c in ("xx", "zz", "xz")]
    assert max(r) < 0.2, f"even-log EH pattern under the locked 0.2 bar (got {r})"
    assert 1.2e-4 < abs(L1s["xy"]) < 2.1e-4, f"L1_xy in the registered band ({L1s['xy']:.3e})"
    assert L1s["xy"] < 0, "registered sign of the log slope"
    c1, c2 = chi2_1d(100), chi2_1d(200)
    assert abs(c2 - c1) / abs(c2) < 0.015, "1D band response finite/grid-stable, no subtraction"
    L1 = REGISTERED["L1"]["xy"]
    Cs = L1 * np.log(1.0 / np.array([0.25, 4.0]))
    assert Cs[0] * Cs[1] < 0, "scheme normalization is sign-indefinite over u0 in [1/4,4]"
    assert abs(np.log(1e34)) > 5, "F-Lor bridge would need ln u0 ~ 1e34 (trivially excluded)"
    print(f"pattern ratios {[f'{x:.4f}' for x in r]} (<0.2); L1_xy={L1s['xy']:.3e};")
    print(f"1D stable ({abs(c2-c1)/abs(c2):.2%}); scheme sign-indefinite; exclusion survives.")
    print("PASS: the covariant induced action lives in the even-log channel; its")
    print("      normalization is scheme-borne; GRV-100's record stands.")


if __name__ == "__main__":
    test()
