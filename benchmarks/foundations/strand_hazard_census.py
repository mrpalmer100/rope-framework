"""FND-STRAND-014 (Modeled): THE PER-SEED HAZARD CENSUS AT N = 24 -- the
smallest box's escape is NON-MEMORYLESS at the population level; the falling
hazard is not attributable to the measured weave functionals; and the
historical batch swings are CLOSED as pure distributional dispersion.

Bars locked blind (analysis/STRAND014_hazard_census_bars_LOCKED.md); results
with two conservative adjudications on their face
(analysis/STRAND014_hazard_census_results.md); 256-walker aligned dataset
archived (analysis/STRAND014_hazard_census_data.json).

(B1) TRACEABILITY: INTERMEDIATE -- weave-energy covariates are significant
     (rho ~ -0.17, more energy -> faster escape) but far below the 0.30 bar.
(B2) POOLED HAZARD: DECREASING, R = 0.326 -- survivors' escape rate falls
     ~3x mid-distribution.
(B3) SEPARATION: AGING-CLASS AS MEASURED -- all three covariate terciles
     show falling hazard (0.51/0.32/0.58); stratification flattens nothing.
     No promotion: a locked-clause conflict resolved conservative, and the
     frailty degeneracy (hidden-covariate heterogeneity) is named -- the
     survivor-thermometry session is designed to break it with a state
     measurement.
(B4) CLOSURE: the STRAND-011/012 batch ratios (2.07, 2.54) sit inside the
     census bootstrap 95% band [1.02, 3.39] -- no generator anomaly ever
     existed; the swings are what this distribution does at n = 32.

This benchmark re-executes the locked census statistics from the archive.
"""
import json
import os

import numpy as np

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, '..', '..', 'analysis',
                    'STRAND014_hazard_census_data.json')


def _lam(ts, qlo, qhi):
    s = np.sort(ts); n = len(s)
    S = 1 - np.arange(1, n + 1)/(n + 1)
    a, b = np.quantile(s, [qlo, qhi])
    m = (s >= a) & (s <= b)
    sl, _ = np.polyfit(s[m], np.log(S[m]), 1)
    return -sl


def _spearman(x, y):
    rx = np.argsort(np.argsort(x)); ry = np.argsort(np.argsort(y))
    return np.corrcoef(rx, ry)[0, 1]


def test():
    d = json.load(open(DATA))
    t = np.array(d['mean']); cov = np.array(d['cov'])
    assert len(t) == 256 and np.isfinite(t).all(), "census complete, censor-free"
    rhos = [_spearman(t, cov[:, i]) for i in range(3)]
    assert abs(rhos[0] + 0.165) < 0.02 and abs(rhos[1] + 0.166) < 0.02, \
        f"registered covariate correlations pinned, got {rhos}"
    assert max(abs(r) for r in rhos) < 0.30, "B1: below the traceable bar"
    R = _lam(t, 0.50, 0.90)/_lam(t, 0.25, 0.50)
    assert abs(R - 0.326) < 0.02, f"pooled hazard ratio pinned, got {R:.3f}"
    assert R <= 0.7, "B2: decreasing hazard"
    idx = np.argsort(cov[:, 1])
    Rt = []
    for ix in (idx[:85], idx[85:171], idx[171:]):
        Rt.append(_lam(t[ix], 0.50, 0.90)/_lam(t[ix], 0.25, 0.50))
    assert sum(r <= 0.7 for r in Rt) >= 2, "B3: aging-class signature"
    rng = np.random.default_rng(2026)
    ratios = []
    for _ in range(1000):
        def tr(x):
            s = np.sort(x); n = len(s)
            S = 1 - np.arange(1, n + 1)/(n + 1)
            a, b = np.quantile(s, [0.25, 0.90]); m = (s >= a) & (s <= b)
            sl, _ = np.polyfit(s[m], np.log(S[m]), 1)
            return -1/sl
        a, b = tr(rng.choice(t, 32, True)), tr(rng.choice(t, 32, True))
        ratios.append(max(a, b)/min(a, b))
    lo, hi = np.quantile(ratios, [0.025, 0.975])
    assert lo <= 2.07 <= hi and lo <= 2.54 <= hi, "B4: batch swings explained"
    print(f"B1: rhos = {[f'{r:+.3f}' for r in rhos]} -- intermediate")
    print(f"B2: pooled R = {R:.3f} -- decreasing hazard")
    print(f"B3: tercile R = {[f'{r:.2f}' for r in Rt]} -- aging-class as measured")
    print(f"B4: bootstrap band [{lo:.2f}, {hi:.2f}] contains 2.07 and 2.54 -- CLOSED")
    print("PASS: non-memoryless escape at the smallest box; batch-swing question")
    print("      closed as distributional; frailty degeneracy named for the")
    print("      survivor-thermometry session.")


if __name__ == "__main__":
    test()
