"""FND-STRAND-020 (Derived): THE POISSONIZATION LAW -- S_N = S_24^{N/24},
parameter-free, PROMOTED at Derived: the strand-kinetics arc's cornerstone.

Bars committed before any comparison
(analysis/STRAND020_poissonization_bars_LOCKED.md); results
(analysis/STRAND020_poissonization_results.md). Under (A1) channel
independence, (A2) intensive per-channel law, (A3) count proportional to N,
the aggregate survival at size N is the pooled N = 24 reference survival
raised to the N/24 power -- the reference channel count CANCELS and the law
carries zero fitted constants. Mechanism: window compression -- the large
ring's quantile windows compress onto the early, locally flat stretch of an
intensive per-channel hazard, so R(N) -> 1 without any change in
per-channel physics.

CONFRONTATION (predictions from the n = 512 reference alone, against the
REGISTERED 019 table): R_pred = 0.292 / 0.647 / 0.930 at N = 48/96/192 vs
measured 0.281 / 0.479 / 0.972 -- ALL THREE inside the registered 95% CIs;
medians within factors 1.14 / 1.10 / 1.30 (bar 1.5), the lone small-N miss
in the 012-consistent direction (barrier relief), as pre-named.

Retired by this promotion: the size-effect fork's mechanism gap (019); the
hazard-shape session (013's flags are the law's corollary). Prediction 11
in closed form: dark-count survival = per-channel curve ^ channel count.

This benchmark re-derives the predictions from the archived reference and
pins the registered numbers.
"""
import json
import os

import numpy as np

HERE = os.path.dirname(__file__)
A = lambda f: os.path.join(HERE, '..', '..', 'analysis', f)


def load_reference():
    ref = (json.load(open(A('STRAND014_hazard_census_data.json')))['mean']
           + json.load(open(A('STRAND015_thermometry_data.json')))['esc']
           + json.load(open(A('STRAND016_force_noise_data.json')))['esc'])
    ref = np.sort(np.array(ref))
    assert len(ref) == 512 and np.isfinite(ref).all()
    return ref


def predictions(ref):
    n = len(ref)
    S = 1 - np.arange(1, n + 1)/(n + 1)

    def q24(p):
        return float(np.quantile(ref, p))

    def qN(p, N):
        return q24(1 - (1 - p)**(24.0/N))

    def lam(a, b):
        m = (ref >= a) & (ref <= b)
        sl, _ = np.polyfit(ref[m], np.log(S[m]), 1)
        return -sl

    out = {}
    for N in (48, 96, 192):
        t1, t2, t3 = qN(0.25, N), qN(0.50, N), qN(0.90, N)
        out[N] = (lam(t2, t3)/lam(t1, t2), qN(0.50, N))
    return out


def test():
    ref = load_reference()
    pred = predictions(ref)
    reg_R = {48: 0.292, 96: 0.647, 192: 0.930}
    CI = {48: (0.138, 0.530), 96: (0.247, 0.820), 192: (0.502, 1.513)}
    reg_med = {48: 136.3, 96: 80.2, 192: 53.7}
    meas_med = {48: 154.8, 96: 88.2, 192: 69.8}
    for N in (48, 96, 192):
        Rp, mp = pred[N]
        assert abs(Rp - reg_R[N]) < 0.02, f"R_pred({N}) pinned, got {Rp:.3f}"
        lo, hi = CI[N]
        assert lo <= Rp <= hi, f"B1: prediction inside registered CI at N={N}"
        assert abs(mp - reg_med[N]) < 2, f"median_pred({N}) pinned, got {mp:.1f}"
        r = max(mp, meas_med[N])/min(mp, meas_med[N])
        assert r <= 1.5, f"B2: median factor at N={N}"
    print("R_pred:", {N: f"{pred[N][0]:.3f}" for N in pred},
          "-- all inside registered 95% CIs")
    print("median factors:",
          {N: f"{max(pred[N][1], meas_med[N])/min(pred[N][1], meas_med[N]):.2f}"
           for N in pred}, "(bar 1.5)")
    print("PASS: S_N = S_24^(N/24), parameter-free, three sizes, zero fitted")
    print("      constants -- PROMOTED at Derived; the strand arc's cornerstone.")


if __name__ == "__main__":
    test()
