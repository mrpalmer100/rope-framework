"""ELEC-029 (Modeled): THE THREE-STATE DECIDER -- THE 47x WAS STATE-LUCK,
THE METRIC MUST BE COMPUTED WHERE IT IS USED, AND WITH THAT FIXED THE
TROUGH FINALLY YIELDS. B3 passes for the first time in five sessions.

(1) THE DECIDER ANSWERED: measuring per-step gain at four campaign
    states under one protocol, the MISMATCHED scheme (ELEC-027's) is
    erratic -- 151.6x, 31.6x, 0.0x (total stall), 43.2x -- while the
    CONSTRAINT-AWARE scheme is robust at 15.7x to 47.4x, a spread of
    only 3.0x. ELEC-027's headline 47x was a favourable draw from an
    unstable distribution; the constraint-aware gain is a property.

(2) THE STALE-SPECTRUM DISCOVERY, which explains ELEC-028's shortfall:
    that session used a diagonal preconditioner computed at the
    ELEC-026 state and applied it elsewhere. The curvature spectrum is
    strongly state-dependent (chart conditioning 376x, 1535x, 1520x,
    977x across four states), and a stale metric surrenders most of
    the benefit -- 2.4x per step where a state-fresh metric gives
    15.7x at the very same point.

(3) B3 PASSES: at equal wall-clock from the ELEC-028 terminus, raw
    descent has effectively STALLED (dE = 9.2e-6 over 393 steps) while
    the constraint-aware scheme with a state-fresh spectrum recovers
    dE = 4.18e-2 in 515 steps. The ratio (4523x) is inflated by a
    near-zero baseline and should not be quoted as an engineering
    speedup; the meaningful statement is ABSOLUTE: one 75-second run
    recovered more energy than the entire ELEC-024 -> ELEC-028
    sequence of sessions combined (4.18e-2 versus 3.20e-2).

(4) SCOPE, stated plainly: this is a better DESCENT instrument, not a
    minimum. No census was run at the new state, no stationarity is
    claimed, and the standing warning stands -- every energy in this
    sector is an upper bound from unconverged descent. What has
    changed is that the bound now falls quickly.

THE GEOMETRY IS UNMOVED, as ever: the clasp holds its isoperimetric
floor with contact unbroken through the largest single-session energy
change the campaign has recorded.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'ELEC029_state.npz')
    mis = s['mis_ratio']; ca = s['ca_ratio']
    # (1) the decider
    assert mis.min() == 0.0 and mis.max() > 100, "mismatched scheme erratic: stall to 151x"
    assert ca.min() > 10 and ca.max()/ca.min() < 5, \
        "constraint-aware robust: 15.7-47.4x, spread 3.0x -- a property, not a draw"
    # (2) the stale-spectrum discovery
    meta = s['meta']
    conds = meta[:, 3]
    assert conds.max()/conds.min() > 3, "the curvature spectrum is strongly state-dependent"
    # (3) B3 passes, on the absolute statement
    assert float(s['speedup']) >= 10, "B3 PASS"
    assert float(s['dF']) > 0.03, "absolute recovery 4.18e-2 in 75s"
    assert float(s['dF']) > (15.524321 - 15.492341), \
        "one run exceeded the whole ELEC-024 -> ELEC-028 sequence"
    assert float(s['dR']) < 1e-4, "the raw baseline had effectively stalled (ratio is inflated)"
    print(f"mismatched {mis.min():.0f}-{mis.max():.0f}x (erratic); CA {ca.min():.1f}-{ca.max():.1f}x "
          f"(spread {ca.max()/ca.min():.1f}x); recovery {float(s['dF']):.3e} vs raw {float(s['dR']):.1e}")
    print("PASS: the 47x was state-luck; the metric must be computed where it is used; and with")
    print("      that fixed one run beat five sessions -- a better descent, still not a minimum.")


if __name__ == "__main__":
    test()
