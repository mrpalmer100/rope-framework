"""FND-STRAND-011 (Modeled): THE N-SWEEP -- nu is NOT box-free; the scaling
is SUPER-EXTENSIVE (registered as measured, not promoted).

Bars locked before computation (analysis/STRAND011_N_sweep_bars_LOCKED.md);
audit addendum with informed-status ceiling owned on its face
(analysis/STRAND011_N_sweep_audit_ADDENDUM.md); results and dataset in
analysis/STRAND011_N_sweep_results.md / _data.json (N = 48 point = the
STRAND-010 archive, reused as pre-committed).

(LOCKED PROTOCOL) NO-VERDICT: one censored run at N = 24 invalidated the
     point; the window-pricing miss is owned.
(AUDIT) The censored run COMPLETED by deterministic replay under a uniform
     window extension (no imputation): three-point slope s = -1.661 at
     r^2 = 0.9984 -- SUPER-EXTENSIVE, outside every originally committed
     grammar, registered as measured per the addendum's ceiling.
(CLEAN-SUBSET CONSEQUENCE, full strength): the censor-free 48 -> 96 leg
     alone (-1.545) excludes the INTENSIVE grammar by many sigma --
     STRAND-010's promoted identification acquires a scope note: it is the
     N = 48 statement; the gap sets the per-event Arrhenius clock, the
     N-dependence carries the event entropy, and it carries MORE than pure
     rate-additivity (-1 would be per-site).

This benchmark refits the archived datasets and pins the registered numbers,
plus a small live smoke check of the scaling direction.
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from strand_attempt_rate import ensemble_escape
from strand_weave_spectrum import measured_spectrum

HERE = os.path.dirname(__file__)
D011 = os.path.join(HERE, '..', '..', 'analysis', 'STRAND011_N_sweep_data.json')
D010 = os.path.join(HERE, '..', '..', 'analysis', 'STRAND010_promotion_data.json')


def archived_fit():
    d = json.load(open(D011))
    a = json.load(open(D010))
    means = {24: np.mean(d['24']['mean']),
             48: np.mean(a['0.4']),
             96: np.mean(d['96']['mean'])}
    for N in ('24', '96'):
        e = np.array(d[N]['mean'])
        assert len(e) == 64 and np.isfinite(e).all(), \
            "archived points complete and censor-free after audit"
    x = np.log(sorted(means)); y = np.log([means[k] for k in sorted(means)])
    s, ic = np.polyfit(x, y, 1)
    yh = s*x + ic
    r2 = 1 - np.sum((y - yh)**2)/np.sum((y - y.mean())**2)
    s_hi = np.log(means[96]/means[48])/np.log(2.0)
    return s, r2, s_hi


def test():
    s, r2, s_hi = archived_fit()
    assert abs(s - (-1.661)) < 0.02, f"registered slope pinned, got {s:.3f}"
    assert r2 > 0.99, f"three-point fit quality, got {r2:.4f}"
    assert s_hi < -0.3, "clean 48->96 leg excludes the intensive grammar"
    assert s < -1.3, "super-extensive class (registered as measured)"
    om, _ = measured_spectrum()
    e48 = ensemble_escape(0.55, om, 0.40, N=48, S=6, tmax=250000)
    e96 = ensemble_escape(0.55, om, 0.40, N=96, S=6, tmax=250000)
    assert np.isfinite(e48).all() and np.isfinite(e96).all()
    assert e48.mean() > e96.mean(), "smoke: bigger box escapes faster"
    print(f"archive: three-point slope s = {s:.3f} (r^2 = {r2:.4f}); "
          f"48->96 leg {s_hi:.3f}")
    print(f"smoke: live means {e48.mean():.0f} (N=48) > {e96.mean():.0f} (N=96)")
    print("PASS: nu is NOT box-free -- intensive excluded on censor-free data;")
    print("      super-extensive scaling registered as measured; promotion")
    print("      reserved for the blind four-point session.")


if __name__ == "__main__":
    test()
