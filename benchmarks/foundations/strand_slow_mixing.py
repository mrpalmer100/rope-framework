"""FND-STRAND-018 (Modeled): THE SLOW-MIXING SESSION -- two limbs pass, the
size limb fails decisively, and the failure reframes the arc: tau_mix is
INTENSIVE (~175 at both N = 24 and 96), and the falling hazard is plausibly
N-GENERAL, not a small-box anomaly.

Bars locked blind (analysis/STRAND018_slow_mixing_bars_LOCKED.md); results
with the edge-geometry honesty note and the labeled exploratory check
(analysis/STRAND018_slow_mixing_results.md); mixing curves archived
(analysis/STRAND018_mixing_curves.json).

(P1) IN-WINDOW: tau_mix(24) = 177 inside the pooled hazard-fall window
     [114, 3378] -- at the EARLY edge, noted at full volume.
(P2) PLATEAU-CONSISTENT on the pooled n = 512: l2/l1 = 0.371, then
     l3/l2 = 0.778 -- the fall decelerates strongly toward a floor.
(P3) DOES-NOT-SHRINK: r_N = 0.971 vs a 0.5 bar -- mixing is a LOCAL
     process (each site's modes mix through its own chain coordinate) and
     its clock cannot know the ring size. No promotion.

Exploratory (labeled, feeds the next bars): pooled archived N = 96 escapes
give R(96) = 0.479 -- the hazard falls at N = 96 as at N = 24.

This benchmark refits the archived curves and pooled escape data and pins
the registered numbers.
"""
import json
import os

import numpy as np

HERE = os.path.dirname(__file__)
A = lambda f: os.path.join(HERE, '..', '..', 'analysis', f)


def _tau(times, O):
    v = np.array(O, dtype=float); t = np.array(times)
    m = np.isfinite(v)
    v, t = v[m], t[m]
    ix = np.where(v <= 1/np.e)[0]
    i = ix[0]
    return t[i] if i == 0 else t[i-1] + (t[i]-t[i-1])*((v[i-1]-1/np.e)/(v[i-1]-v[i]))


def _lam(ts, qlo, qhi):
    s = np.sort(ts); n = len(s)
    S = 1 - np.arange(1, n + 1)/(n + 1)
    a, b = np.quantile(s, [qlo, qhi]); m = (s >= a) & (s <= b)
    sl, _ = np.polyfit(s[m], np.log(S[m]), 1)
    return -sl


def test():
    mx = json.load(open(A('STRAND018_mixing_curves.json')))
    t24 = _tau(mx['N24']['times'], mx['N24']['O'])
    t96 = _tau(mx['N96']['times'], mx['N96']['O'])
    assert abs(t24 - 177.3) < 2 and abs(t96 - 172.2) < 2, (t24, t96)
    rN = t96/t24
    assert rN >= 0.8, "P3: tau_mix does not shrink -- mixing is intensive"
    esc = (json.load(open(A('STRAND014_hazard_census_data.json')))['mean']
           + json.load(open(A('STRAND015_thermometry_data.json')))['esc']
           + json.load(open(A('STRAND016_force_noise_data.json')))['esc'])
    t = np.array(esc); assert len(t) == 512 and np.isfinite(t).all()
    q25, q90 = np.quantile(t, [0.25, 0.90])
    assert q25 <= t24 <= q90, "P1: in-window"
    l1 = _lam(t, 0.25, 0.50); l2 = _lam(t, 0.50, 0.90); l3 = _lam(t, 0.90, 0.98)
    assert l2/l1 <= 0.7 and 0.6 <= l3/l2 <= 1.5, "P2: plateau-consistent"
    e96 = np.array(json.load(open(A('STRAND011_N_sweep_data.json')))['96']['mean']
                   + json.load(open(A('STRAND012_four_point_data.json')))['96']['mean'])
    R96 = _lam(e96, 0.50, 0.90)/_lam(e96, 0.25, 0.50)
    assert abs(R96 - 0.479) < 0.02 and R96 < 0.7, \
        "exploratory pinned: the hazard falls at N = 96 too"
    print(f"tau_mix: {t24:.0f} (N=24) vs {t96:.0f} (N=96) -- INTENSIVE (r={rN:.2f})")
    print(f"pooled n=512: l2/l1 = {l2/l1:.3f}, l3/l2 = {l3/l2:.3f} -- deceleration to a floor")
    print(f"exploratory: R(96) = {R96:.3f} -- the phenomenon is plausibly N-general")
    print("PASS: two limbs hold, the size limb fails informatively; the arc's")
    print("      'small-box anomaly' framing is retired in favor of the")
    print("      N-generality question, now a named blind session.")


if __name__ == "__main__":
    test()
