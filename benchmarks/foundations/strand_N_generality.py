"""FND-STRAND-019 (Modeled): THE N-GENERALITY SESSION -- the fork resolves
SIZE-EFFECT: the non-exponential escape transient is a genuine smallness
phenomenon, strong at N = 24-48, gone by N = 192, with slope s_R = +0.495
in ln R vs ln N and R(192) = 0.97 consistent with fully exponential.

Bars locked blind with the pricing language committed (fork, not decimal)
(analysis/STRAND019_N_generality_bars_LOCKED.md); results with the
Poissonization explanation candidate
(analysis/STRAND019_N_generality_results.md); fresh N = 48/192 data
archived (analysis/STRAND019_N_generality_data.json), archives pooled per
the committed rule.

The explanation candidate needs no new mechanism: many independent escape
channels Poissonize the aggregate first-passage (Khinchin superposition)
regardless of per-channel memory -- cohering with STRAND-012's
rate-additivity crossover and STRAND-018's intensive tau_mix. Prediction
11's final form (pending derivation): the non-Poisson dark-count transient
carries a SIZE CONDITION set by channel count, a counting statement rather
than a new constant.

This benchmark recomputes the committed table from the archives and pins
the registered numbers.
"""
import json
import os

import numpy as np

HERE = os.path.dirname(__file__)
A = lambda f: os.path.join(HERE, '..', '..', 'analysis', f)


def _lam(ts, qlo, qhi):
    s = np.sort(ts); n = len(s)
    S = 1 - np.arange(1, n + 1)/(n + 1)
    a, b = np.quantile(s, [qlo, qhi]); m = (s >= a) & (s <= b)
    sl, _ = np.polyfit(s[m], np.log(S[m]), 1)
    return -sl


def _R(ts):
    return _lam(ts, 0.50, 0.90)/_lam(ts, 0.25, 0.50)


def test():
    fresh = json.load(open(A('STRAND019_N_generality_data.json')))
    data = {
        24: np.array(json.load(open(A('STRAND014_hazard_census_data.json')))['mean']
                     + json.load(open(A('STRAND015_thermometry_data.json')))['esc']
                     + json.load(open(A('STRAND016_force_noise_data.json')))['esc']),
        48: np.array(fresh['48']),
        96: np.array(json.load(open(A('STRAND011_N_sweep_data.json')))['96']['mean']
                     + json.load(open(A('STRAND012_four_point_data.json')))['96']['mean']),
        192: np.array(fresh['192']),
    }
    reg = {24: 0.371, 48: 0.281, 96: 0.479, 192: 0.972}
    Rs = {}
    for N, t in data.items():
        assert np.isfinite(t).all(), f"censor-free at N={N}"
        Rs[N] = _R(t)
        assert abs(Rs[N] - reg[N]) < 0.02, f"R({N}) pinned, got {Rs[N]:.3f}"
    x = np.log(sorted(Rs)); y = np.log([Rs[N] for N in sorted(Rs)])
    sR, _ = np.polyfit(x, y, 1)
    assert abs(sR - 0.495) < 0.02, f"slope pinned, got {sR:.3f}"
    assert sR >= 0.25, "SIZE-EFFECT branch of the fork"
    assert Rs[24] < 0.5 and Rs[48] < 0.5, "transient strong at small N"
    assert Rs[192] > 0.8, "transient gone by N = 192"
    print("R(N):", {N: f"{Rs[N]:.3f}" for N in sorted(Rs)}, f"; s_R = {sR:.3f}")
    print("PASS: SIZE-EFFECT -- the non-exponential transient is a smallness")
    print("      phenomenon; Poissonization by channel count is the named,")
    print("      theorem-shaped explanation candidate for its own session.")


if __name__ == "__main__":
    test()
