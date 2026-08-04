"""FND-STRAND-010 (Modeled): THE PROMOTION RERUN -- the nu-identification
promoted: the attempt rate IS the weave band gap to O(1).

Bars locked before computation (analysis/STRAND010_promotion_bars_LOCKED.md):
h re-locked at 0.55 with rationale (discharging STRAND-009's deviation by
re-lock, not pardon), and the seed budget priced to the exponential estimator
(S = 64/point) BEFORE reusing the 0.97 r^2 bar. Registered dataset archived
verbatim in analysis/STRAND010_promotion_data.json.

(B1') BOLTZMANN LIMB, PASS: ln(tau_mean) vs 1/T over four T points at 64
      seeds each, zero censoring -- DeltaE_eff = 2.112, r^2 = 0.9965 vs the
      unchanged 0.97 bar.
(B2') NU-IDENTIFICATION, PROMOTED: nu = 0.451 x omega_min, inside [1/3, 3].
      tau = O(1) x omega_min^-1 x exp(DeltaE/T) with every symbol's
      provenance corpus-internal (bath derived, spectrum measured, regime
      attempt-limited).

This benchmark (a) refits the ARCHIVED registered dataset and pins the
registered numbers, and (b) runs a small live ensemble on the same engine as
a smoke check that the archived physics is reproducible in this environment
(self-consistent within its own run; magnitudes live in the archive).
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from strand_attempt_rate import ensemble_escape
from strand_weave_spectrum import measured_spectrum

ARCHIVE = os.path.join(os.path.dirname(__file__), '..', '..', 'analysis',
                       'STRAND010_promotion_data.json')


def archived_fit():
    d = json.load(open(ARCHIVE))
    Ts = sorted(float(k) for k in d)
    means = []
    for T in Ts:
        e = np.array(d[str(T)])
        assert len(e) == 64, "locked budget: 64 seeds per point"
        assert np.isfinite(e).all(), "registered dataset is censor-free"
        means.append(e.mean())
    x = 1/np.array(Ts); y = np.log(means)
    dE, ic = np.polyfit(x, y, 1)
    yhat = dE*x + ic
    r2 = 1 - np.sum((y - yhat)**2)/np.sum((y - y.mean())**2)
    return dE, np.exp(-ic), r2


def test():
    dE, nu, r2 = archived_fit()
    assert r2 >= 0.97, f"B1' bar: r^2 = {r2:.4f}"
    assert abs(dE - 2.112) < 0.02, f"registered DeltaE_eff pinned, got {dE:.3f}"
    assert 1/3 <= nu <= 3, f"B2' window: nu = {nu:.3f}"
    assert abs(nu - 0.451) < 0.02, f"registered nu pinned, got {nu:.3f}"
    om, _ = measured_spectrum()
    e_lo = ensemble_escape(0.55, om, 0.40, S=6, tmax=250000)
    e_hi = ensemble_escape(0.55, om, 0.56, S=6, tmax=250000)
    assert np.isfinite(e_lo).all() and np.isfinite(e_hi).all(), "smoke: escapes complete"
    assert e_lo.mean() > e_hi.mean(), "smoke: escape monotone in T on this engine"
    print(f"B1': archived fit DeltaE_eff = {dE:.3f}, r^2 = {r2:.4f} (bar 0.97) -- PASS")
    print(f"B2': nu = {nu:.3f} x omega_min, window [1/3, 3] -- PROMOTED")
    print(f"smoke: live means {e_lo.mean():.0f} > {e_hi.mean():.0f}, monotone")
    print("PASS: the attempt rate is the weave band gap to O(1) -- promoted on a")
    print("      priced budget, censor-free, h honored as re-locked.")


if __name__ == "__main__":
    test()
