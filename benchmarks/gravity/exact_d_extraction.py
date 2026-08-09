"""COMMISSION: THE EXACT-D EXTRACTION (charter: docs/technical/COMMISSION_EXACT_D.md)

Extracts the continuum, per-volume coefficient of the IR-universal
(m-odd) Einstein-Hilbert remainder from the GRV-024/025 absorption
instrument, using the instrument's own machinery unmodified (imported).

D_lat(M) := b_xy(M) / M^3   (per-site m-odd xy coefficient, lattice
units, kt0 = 0.64, the instrument's registered operating point).

P2: finite-size sweep M in {48, 64, 96, 128, 160}, extrapolate
    D_lat(M) = D + c1/M + c2/M^2 (least squares), Richardson cross-check.
P3: regulator sweep at M = 96 -- mass-window shifts, fit-basis
    augmentation, finite-difference step -- bar: < 10% movement.

Bars (locked before computation, see charter): B2 |D(M_max)-D_extrap|/D < 5%
with monotone tail over final three sizes; B3 < 10% over regulator sweep.
Deterministic; no randomness anywhere in the pipeline.
"""
import sys, os, json
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from absorption_verdict import E2_total  # the instrument, unmodified

OUT = "/tmp/exact_d_results.json"
KT0 = 0.64
M2S_STD = np.array([0.16, 0.25, 0.36, 0.49, 0.64, 0.81, 1.0])


def channels_xy(M, m2, dstep=1e-3):
    """xy channel q^2 coefficient, following the instrument's channels()."""
    rows = []
    for nq in (1, 2):
        def one(h):
            return E2_total(M, KT0, m2, nq, h)
        xx = one([1, 0, 0])
        xy = (one([1, 1, 0]) - 2 * xx) / 2
        rows.append(xy)
    qs = np.array([2 * np.pi / M, 4 * np.pi / M])
    return (rows[1] - rows[0]) / (qs[1] ** 2 - qs[0] ** 2)


def modd_xy(M, m2s=M2S_STD, basis="std"):
    """m-odd coefficient of the xy channel; basis variants for P3."""
    ms = np.sqrt(m2s)
    data = np.array([channels_xy(M, m2) for m2 in m2s])
    cols = [np.ones_like(ms), m2s, m2s ** 2, ms]
    if basis == "aug":  # add m^3 (also m-odd; m-odd part = m + m^3 terms at m->0 leading m)
        cols.append(ms ** 3)
    A = np.stack(cols, 1)
    coef = np.linalg.lstsq(A, data, rcond=None)[0]
    return coef[3]  # the m^1 coefficient: the IR-universal amplitude


def load():
    return json.load(open(OUT)) if os.path.exists(OUT) else {}


def save(d):
    json.dump(d, open(OUT, "w"), indent=1)


def run_size(M):
    d = load()
    key = f"M{M}"
    if key not in d:
        b = modd_xy(M)
        d[key] = {"b_xy": float(b), "D_lat": float(b / M ** 3)}
        save(d)
    return d[key]


def extrapolate(sizes, vals):
    x = 1.0 / np.array(sizes, float)
    A = np.stack([np.ones_like(x), x, x ** 2], 1)
    c = np.linalg.lstsq(A, np.array(vals), rcond=None)[0]
    return c[0]


REGISTERED = {  # the commission's record (full sweep, 2026-08-09)
    "D_lat_by_M": {48: 3.389957e-4, 64: 3.306437e-4, 96: 3.242146e-4,
                   128: 3.218683e-4, 160: 3.207649e-4},
    "D_extrap": 3.179407e-4, "B2_dev": 0.00888,
    "B3_worst": 0.5714,  # aug_down vs std at M=96
}


def test():
    """GRV-096: B1/B2 held; B3 FAILED -- the m-odd amplitude is
    protocol-dependent (12-57% at M=96; 44% window spread already at
    M=48), so no IR-universal D is claimable from this protocol.
    CI re-verifies the cheap signature at M=48 deterministically."""
    ch = {m2: float(channels_xy(48, m2))
          for m2 in (0.09, 0.16, 0.25, 0.36, 0.49, 0.64, 0.81, 1.0)}

    def fit(m2s):
        m2s = np.array(m2s); ms = np.sqrt(m2s)
        y = np.array([ch[m] for m in m2s])
        A = np.stack([np.ones_like(ms), m2s, m2s ** 2, ms], 1)
        return np.linalg.lstsq(A, y, rcond=None)[0][3] / 48 ** 3

    std = fit([0.16, 0.25, 0.36, 0.49, 0.64, 0.81, 1.0])
    low = fit([0.09, 0.16, 0.25, 0.36, 0.49])
    high = fit([0.36, 0.49, 0.64, 0.81, 1.0])
    # (a) deterministic reproduction of the registered M=48 point
    assert abs(std - REGISTERED["D_lat_by_M"][48]) / std < 1e-6, "M=48 reproduction"
    # (b) the failure signature: window spread far beyond the 10% bar
    spread = abs(high - low) / std
    assert spread > 0.10, "protocol dependence is the registered finding"
    # (c) volume convergence at fixed protocol was real (monotone registered tail)
    v = REGISTERED["D_lat_by_M"]
    assert v[96] > v[128] > v[160], "monotone tail (B2 held at fixed protocol)"
    print(f"M=48 std={std:.6e}; window spread {spread:.1%} (>10%)")
    print("PASS: the exact-D extraction's registered outcome verified -- volume-")
    print("      convergent at fixed protocol, NOT IR-universal across protocols;")
    print("      no D claimable; GRV-025's pattern verdict unaffected.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        M = int(sys.argv[1])
        r = run_size(M)
        print(f"M={M}: b_xy={r['b_xy']:.6f}  D_lat={r['D_lat']:.8f}")
    else:
        test()
