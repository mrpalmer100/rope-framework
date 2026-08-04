"""FND-STRAND-012 (Modeled): THE BLIND FOUR-POINT SWEEP -- no single power
law exists; the honest object is a CROSSOVER, and both STRAND-011 suspects
are real in different regimes.

Bars locked blind before any trajectory
(analysis/STRAND012_four_point_bars_LOCKED.md); results and archived
two-channel dataset in analysis/STRAND012_four_point_results.md /
_data.json. Zero censoring on any channel at any box (per-N window pricing).

(B1) NUCLEATION CHANNEL (t_first): s_f = -1.218 -- INTERMEDIATE per the
     locked grammar; pairwise slopes -1.45 / -1.45 / -0.67 flatten toward
     rate-additivity at large N: finite-size barrier relief exhausts itself
     as the ring grows.
(B2) CONVERSION CHANNEL (t_conv): s_c = -1.082 -- PARALLEL CONVERSION,
     clean pass: more simultaneous seeds convert a bigger ring
     proportionally faster.
(B3) CLOSURE: recomposition t_mean = t_first + t_conv exact per run;
     continuity with STRAND-011's exponent FAILS (+0.529) and is diagnosed
     as N = 24 heavy-tail estimator fragility (the arc's third pricing
     miss: seeds, window, now distribution shape) -- STRAND-011's
     super-extensive CLASSIFICATION survives on the clean mid legs
     (-1.545 / -1.70), its exponent VALUE retired as estimator-limited.

No promotion, per the bars' own criteria -- for the physical reason (a
crossover) rather than a statistical breach. This benchmark refits the
archived dataset and pins the registered numbers.
"""
import json
import os

import numpy as np

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, '..', '..', 'analysis',
                    'STRAND012_four_point_data.json')
NS = [24, 48, 96, 192]


def archived_channels():
    d = json.load(open(DATA))
    tf, tc, tm = {}, {}, {}
    for N in NS:
        m = np.array(d[str(N)]['mean']); f = np.array(d[str(N)]['first'])
        assert len(m) == 64 and np.isfinite(m).all() and np.isfinite(f).all(), \
            "archived points complete and censor-free"
        conv = m - f
        assert (conv >= -1e-9).all(), "per-run alignment: conversion nonnegative"
        tf[N], tc[N], tm[N] = f.mean(), conv.mean(), m.mean()
        assert abs(tm[N] - (tf[N] + tc[N])) < 1e-9, "recomposition exact"
    return tf, tc, tm


def _slope(vals):
    x = np.log(NS); y = np.log([vals[N] for N in NS])
    s, ic = np.polyfit(x, y, 1)
    return s


def test():
    tf, tc, tm = archived_channels()
    sf, sc, sm = _slope(tf), _slope(tc), _slope(tm)
    assert abs(sf - (-1.218)) < 0.02, f"registered s_f pinned, got {sf:.3f}"
    assert abs(sc - (-1.082)) < 0.02, f"registered s_c pinned, got {sc:.3f}"
    assert abs(sm - (-1.132)) < 0.02, f"registered s_m pinned, got {sm:.3f}"
    assert sc <= -0.5, "B2: parallel conversion class"
    assert -1.3 < sf < -1.15, "B1: intermediate class as registered"
    pw = [np.log(tf[NS[i+1]]/tf[NS[i]])/np.log(NS[i+1]/NS[i]) for i in range(3)]
    assert pw[0] < -1.3 and pw[2] > -1.0, \
        "the crossover: steep small-N legs flattening toward additivity"
    assert all(tf[NS[i]] > tf[NS[i+1]] for i in range(3)), "t_first monotone"
    print(f"channels: s_first = {sf:.3f}, s_conv = {sc:.3f}, s_mean = {sm:.3f}")
    print(f"nucleation pairwise: {pw[0]:.2f} / {pw[1]:.2f} / {pw[2]:.2f} -- the crossover")
    print("PASS: both suspects real in different regimes -- barrier relief at")
    print("      small N (exhausting), parallel conversion throughout; no single")
    print("      power law; promotion withheld by the blind bars' own criteria.")


if __name__ == "__main__":
    test()
