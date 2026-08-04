"""FND-STRAND-013 (Modeled): THE TAIL-ROBUST REFIT -- survival-curve rate
fits on the archived STRAND-010/011/012 datasets, estimators locked before
the archives were touched (analysis/STRAND013_tail_refit_bars_LOCKED.md).

(B1) SHAPE: half the archive (7/14 points) FAILS the constant-hazard bar
     over [q25, q90] -- the escape process is not exponential-with-delay in
     general; the kinetics carry structure beyond one Kramers rate.
(B2) THE PROMOTION SURVIVES ITS SEVEREST TEST: nu lands in the O(1) window
     on BOTH estimators (0.451 mean-based, 1.467 rate-based) --
     CONFIRMED-ROBUST, with the barrier VALUE flagged estimator-sensitive
     (2.112 vs 2.634).
(B3) THE CROSSOVER IS ESTIMATOR-INDEPENDENT: robust nucleation pairwise
     slopes -2.04 / -1.80 / -0.81 retain the 012 signature. And the
     CONVENIENT ANSWER WAS REFUSED: per-batch robust rates at N = 24 swing
     by 2.0-2.5x (bar 1.35) -- no better than the mean -- so the smallest
     box's fragility is PHYSICAL (heterogeneity and/or aging hazard), not a
     tail artifact.
(B4) 011's exponent: robust reading -2.447 vs retired -1.661 -- further
     confirmation the exponent was malformed; the crossover is the object.

This benchmark re-executes the locked refit from the archives and pins the
registered numbers.
"""
import json
import os

import numpy as np

HERE = os.path.dirname(__file__)
A = lambda f: os.path.join(HERE, '..', '..', 'analysis', f)


def tau_rate(ts):
    t = np.sort(np.asarray(ts, float)); n = len(t)
    S = 1 - np.arange(1, n + 1)/(n + 1)
    q25, q90 = np.quantile(t, [0.25, 0.90])
    m = (t >= q25) & (t <= q90)
    sl, ic = np.polyfit(t[m], np.log(S[m]), 1)
    yh = sl*t[m] + ic
    r2 = 1 - np.sum((np.log(S[m]) - yh)**2)/np.sum((np.log(S[m]) - np.log(S[m]).mean())**2)
    return -1/sl, r2


def test():
    d10 = json.load(open(A('STRAND010_promotion_data.json')))
    d12 = json.load(open(A('STRAND012_four_point_data.json')))
    # B2: robust Arrhenius
    Ts = [0.34, 0.40, 0.47, 0.56]
    taus = [tau_rate(d10[str(T)])[0] for T in Ts]
    dE, ic = np.polyfit(1/np.array(Ts), np.log(taus), 1)
    nu = np.exp(-ic)
    assert abs(dE - 2.634) < 0.02, f"DeltaE_rob pinned, got {dE:.3f}"
    assert abs(nu - 1.467) < 0.03, f"nu_rob pinned, got {nu:.3f}"
    assert 1/3 <= nu <= 3, "B2: CONFIRMED-ROBUST window"
    # B3: crossover signature on robust nucleation channel
    Ns = [24, 48, 96, 192]
    tf = {N: tau_rate(d12[str(N)]['first'])[0] for N in Ns}
    pw = [np.log(tf[Ns[i+1]]/tf[Ns[i]])/np.log(2) for i in range(3)]
    assert pw[0] <= -1.15 and pw[1] <= -1.15 and pw[2] >= -1.0, \
        "crossover signature estimator-independent"
    # B3: N=24 heterogeneity refused the convenient answer
    a, b = tau_rate(d12['24']['mean'][:32])[0], tau_rate(d12['24']['mean'][32:])[0]
    ratio = max(a, b)/min(a, b)
    assert ratio > 1.35, "N=24 batch swing survives the robust estimator"
    # B1: shape flags exist (the archive is not exponential-with-delay overall)
    flags = sum(tau_rate(d10[str(T)])[1] < 0.95 for T in Ts)
    assert flags >= 2, "shape flags present in the S10 archive"
    print(f"B2: DeltaE_rob = {dE:.3f}, nu_rob = {nu:.3f} -- CONFIRMED-ROBUST")
    print(f"B3: robust nucleation pairwise {pw[0]:.2f}/{pw[1]:.2f}/{pw[2]:.2f} -- crossover holds")
    print(f"B3: N=24 batch ratio {ratio:.2f} (bar 1.35) -- heterogeneity is physical")
    print("PASS: identification robust on both estimators; barrier value flagged;")
    print("      the smallest box now carries a physical question, not a")
    print("      statistical one.")


if __name__ == "__main__":
    test()
