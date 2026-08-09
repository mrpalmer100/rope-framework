"""COMMISSION EXACT-D II: the ordered-limit extraction
(charter: docs/technical/COMMISSION_EXACT_D2.md; bars locked first).

Scaling window m in [3 c q(M), 1.0], c = sqrt(kt0), q = 2 pi / M;
15 log-spaced points in u = m^2; global fit over
{1, u, u^2, u^3, sqrt(u), u^(3/2)}; independent FD3 extractor
(third difference in u kills all polynomials; residual ~ A (3/8) u^(-5/2)).
A is per-volume, q^2-normalized -- the same D_lat convention as GRV-096.
Deterministic throughout.
"""
import sys, os, json
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from absorption_verdict import E2_total

KT0 = 0.64
C = np.sqrt(KT0)
CACHE = "/tmp/exact_d2_cache.json"


def window(M, npts=15):
    lo = (3.0 * C * 2 * np.pi / M) ** 2
    return np.exp(np.linspace(np.log(lo), np.log(1.0), npts))


def channels_xy(M, m2):
    rows = []
    for nq in (1, 2):
        xx = E2_total(M, KT0, m2, nq, [1, 0, 0])
        xy = (E2_total(M, KT0, m2, nq, [1, 1, 0]) - 2 * xx) / 2
        rows.append(xy)
    qs = np.array([2 * np.pi / M, 4 * np.pi / M])
    return (rows[1] - rows[0]) / (qs[1] ** 2 - qs[0] ** 2)


def scan(M):
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    key = f"M{M}"
    us = window(M)
    got = cache.get(key, {})
    for u in us:
        uk = f"{u:.10e}"
        if uk not in got:
            got[uk] = float(channels_xy(M, u) / M ** 3)
            cache[key] = got
            json.dump(cache, open(CACHE, "w"))
    return us, np.array([got[f"{u:.10e}"] for u in us])


def basis(us, cols=("1", "u", "u2", "u3", "sq", "s3")):
    mp = {"1": np.ones_like(us), "u": us, "u2": us ** 2, "u3": us ** 3,
          "sq": np.sqrt(us), "s3": us ** 1.5}
    return np.stack([mp[c] for c in cols], 1), list(cols)


def fit_A(us, ys, cols=("1", "u", "u2", "u3", "sq", "s3")):
    A, names = basis(us, cols)
    coef, *_ = np.linalg.lstsq(A, ys, rcond=None)
    cond = np.linalg.cond(A.T @ A)
    return coef[names.index("sq")], cond


def fd3_profile(us, ys):
    """Third divided difference (Newton) on consecutive quadruples:
    for f = poly2 in u it is 0; for sqrt(u) it equals (3/8) ubar^(-5/2)/6? --
    we use exact divided differences: dd3[sqrt] known numerically, so
    calibrate A locally as dd3(data)/dd3(sqrt)."""
    out = []
    for i in range(len(us) - 3):
        x = us[i:i + 4]
        def dd3(v):
            c = list(v)
            for k in range(1, 4):
                c = [(c[j + 1] - c[j]) / (x[j + k] - x[j]) for j in range(4 - k)]
            return c[0]
        d_data = dd3(ys[i:i + 4])
        d_sqrt = dd3(np.sqrt(x))
        d_s3 = dd3(x ** 1.5)
        # local model: data ~ A sqrt + B s3 (+ poly, annihilated). One-eq
        # estimate ignoring s3 (registered as the raw estimator):
        out.append((float(np.exp(np.mean(np.log(x)))), d_data / d_sqrt,
                    d_s3 / d_sqrt))
    return out





REGISTERED = {  # full record 2026-08-09 (see COMMISSION_EXACT_D2 addendum)
    "A_fit": {64: 1.081405e-4, 96: 8.628002e-5, 128: 7.462553e-5},
    "A_fd3_intercept96": 1.042151e-4, "B_u32_96": 4.826148e-4,
    "B_over_A": 5.59, "B2_dev": 0.2079, "B3_worst": 1.0368,
    "B4_dev": 1.0298, "B5_slope": -2.011, "ident_dev": 4.02e-14,
}


def test():
    """GRV-097: the ordered-limit extraction fails its bars (B2/B3/B4/B5)
    and DISCOVERS the two-term m-odd structure A sqrt(u) + B u^(3/2),
    B/A ~ 5.6, with the exact FD3 identity dd3(u^1.5)/dd3(u^0.5) = -u.
    CI re-verifies the signature at M=64 deterministically."""
    us, ys = scan(64)
    prof = fd3_profile(us, ys)
    # (a) the exact identity, machine precision
    ident = max(abs(p[2] + p[0]) / p[0] for p in prof)
    assert ident < 1e-9, f"FD3 identity dd3(s3)/dd3(sq) = -u (dev {ident:.1e})"
    # (b) the two-term structure: A_local is linear in u to high fidelity
    ub = np.array([p[0] for p in prof]); Al = np.array([p[1] for p in prof])
    lin = np.polyfit(ub, Al, 1); res = Al - np.polyval(lin, ub)
    r2 = 1 - np.sum(res ** 2) / np.sum((Al - Al.mean()) ** 2)
    assert r2 > 0.97, f"A_local(u) linear (two-term m-odd; registered 0.979 at M=64), R^2={r2:.5f}"
    B, A0 = lin[0], lin[1]
    assert 3.0 < B / abs(A0) < 12.0, f"B/A in the registered band (got {B/abs(A0):.2f})"
    # (c) the registered failure signature: dropping u^1.5 moves A far past 10%
    A_full = fit_A(us, ys)[0]
    A_drop = fit_A(us, ys, ("1", "u", "u2", "u3", "sq"))[0]
    assert abs(A_drop - A_full) / abs(A_full) > 0.10, "basis dependence is the finding"
    # (d) deterministic reproduction of the registered M=64 fit
    assert abs(A_full - REGISTERED["A_fit"][64]) / abs(A_full) < 1e-6, "M=64 reproduction"
    print(f"identity dev {ident:.1e}; A_local linear R^2={r2:.5f}; B/A={B/abs(A0):.2f}")
    print("PASS: two-term m-odd structure verified; the EH amplitude is subdominant")
    print("      (B/A ~ 5.6) -- no bar-clean D from fitting; GRV-097's record stands.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        M = int(sys.argv[1])
        us, ys = scan(M)
        A6, cond = fit_A(us, ys)
        print(f"M={M}: A_fit(full basis) = {A6:.6e}   cond = {cond:.2e}")
    else:
        test()
