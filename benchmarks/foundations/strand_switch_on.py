"""FND-STRAND-021 (Modeled): THE SWITCH-ON SESSION -- the per-channel shape
question ANSWERED: the falling hazard is PRODUCT-STATE SLIP, gone under
true metastable-well equilibrium preparation; the plateau is the
stationary Kramers rate; the strand-kinetics program closes.

Bars locked first with the preparation recipe fixed and the Gaussian draw
verified against variance targets
(analysis/STRAND021_switch_on_bars_LOCKED.md); results
(analysis/STRAND021_switch_on_results.md); data archived
(analysis/STRAND021_switch_on_data.json).

(B1) CONSTANT: R_eq = 0.932 in [0.75, 1.33] -- against the product-state
     0.33-0.43, thrice replicated. The transient was preparation.
(B2) CLOSED: lambda_eq = 5.46e-4 vs the registered plateau 4.06e-4
     (factor 1.34, bar 2) -- the plateau IS the equilibrium rate.
(B3) PASS: exponential escape (r^2 = 0.956).
Corroboration: the equilibrium ensemble is SLOWER (median 1016 vs 350) --
the product state's early epoch was escape-enhanced, as slip requires.

PREDICTION 11 final form: two regimes -- after a quench, the switch-on
transient (compressed away at scale per STRAND-020); in steady state,
Poisson at the plateau rate with the band-gap prefactor, at every size.

This benchmark refits the archived ensemble and pins the registered
numbers.
"""
import json
import os

import numpy as np

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, '..', '..', 'analysis',
                    'STRAND021_switch_on_data.json')


def test():
    t = np.array(json.load(open(DATA))['esc'])
    assert len(t) == 128 and np.isfinite(t).all(), "ensemble complete"
    s = np.sort(t); n = len(s)
    S = 1 - np.arange(1, n + 1)/(n + 1)
    q25, q50, q90 = np.quantile(t, [0.25, 0.50, 0.90])

    def lam(a, b):
        m = (s >= a) & (s <= b)
        sl, ic = np.polyfit(s[m], np.log(S[m]), 1)
        yh = sl*s[m] + ic
        r2 = 1 - np.sum((np.log(S[m]) - yh)**2)/np.sum(
            (np.log(S[m]) - np.log(S[m]).mean())**2)
        return -sl, r2

    l1, _ = lam(q25, q50); l2, _ = lam(q50, q90)
    R = l2/l1
    assert abs(R - 0.932) < 0.02, f"R_eq pinned, got {R:.3f}"
    assert 0.75 <= R <= 1.33, "B1: CONSTANT -- the transient is gone"
    leq, r2 = lam(q25, q90)
    assert abs(leq - 5.46e-4) < 2e-5, f"lambda_eq pinned, got {leq:.2e}"
    fac = max(leq, 4.06e-4)/min(leq, 4.06e-4)
    assert fac <= 2, "B2: plateau = equilibrium rate"
    assert r2 >= 0.95, "B3: exponential"
    assert np.median(t) > 800, "corroboration: equilibrium slower than quench"
    print(f"B1: R_eq = {R:.3f} (product-state: 0.33-0.43) -- CONSTANT")
    print(f"B2: lambda_eq = {leq:.2e} vs plateau 4.06e-4 (factor {fac:.2f}) -- CLOSED")
    print(f"B3: r^2 = {r2:.4f} -- exponential")
    print("PASS: the falling hazard was PRODUCT-STATE SLIP; the plateau is the")
    print("      stationary Kramers rate; the kinetics program closes with a")
    print("      two-regime Prediction 11 in which every clause has a")
    print("      registered provenance.")


if __name__ == "__main__":
    test()
