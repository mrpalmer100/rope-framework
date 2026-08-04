"""FND-STRAND-015 (Modeled): SURVIVOR THERMOMETRY -- the cooling-bath
mechanism KILLED by its own designed test; the aging at the smallest box is
NON-THERMAL, and the dressed drive is the named suspect.

Bars locked blind (analysis/STRAND015_thermometry_bars_LOCKED.md; clauses
checked pairwise per the STRAND-014 lesson); results with the kill-verdict
audit on their face (analysis/STRAND015_thermometry_results.md); lean
archived dataset (analysis/STRAND015_thermometry_data.json).

(B1) FLAT: rho_T = 0.9995 against a 0.90 cooling bar -- the weave's kinetic
     temperature is constant to 5 parts in 10^4 across the hazard-relevant
     range. The audit confirms the instrument (reads the 0.400
     initialization exactly; resolves the genuine 3.5% early equilibration
     dip); the kill is real.
(B2) MOOT by its own clause; descriptively the measured DeltaT predicts
     R_pred = 0.998 vs R_meas = 0.429 -- the thermal channel accounts for
     essentially none of the hazard fall.
(B3) SHARED-AGING SUPPORTED: rho_frail = -0.051 (n.s.) -- a walker's early
     thermal state carries no fate information.

FINDING: NON-THERMAL AGING. The hazard falls 2-3x while temperature is flat
and early state is uninformative. Named suspect: the DRESSED DRIVE --
weave-chain correlations develop from zero and can reduce the effective
noise at constant kinetic temperature. Prediction 11 sharpens: dark-count
drift with FLAT stage temperature, which no thermal-drift model reproduces.

This benchmark refits the archived dataset and pins the registered numbers.
"""
import json
import os

import numpy as np

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, '..', '..', 'analysis',
                    'STRAND015_thermometry_data.json')


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
    esc = np.array(d['esc']); T0 = np.array(d['T0'])
    assert len(esc) == 128 and np.isfinite(esc).all(), "census complete"
    Te, Tl = d['T_early'], d['T_late']
    rhoT = Tl/Te
    assert abs(rhoT - 0.9995) < 0.002, f"flat verdict pinned, got {rhoT:.4f}"
    assert rhoT >= 0.97, "B1: FLAT -- cooling mechanism killed"
    R = _lam(esc, 0.50, 0.90)/_lam(esc, 0.25, 0.50)
    assert abs(R - 0.429) < 0.02, f"hazard ratio pinned, got {R:.3f}"
    assert R <= 0.7, "the aging itself reproduces on independent seeds"
    for dE in (2.112, 2.634):
        Rp = np.exp(-dE*(1/Tl - 1/Te))
        assert Rp > 0.99, "thermal channel predicts ~no hazard fall"
    rf = _spearman(esc, T0)
    assert abs(rf - (-0.051)) < 0.02, f"frailty rho pinned, got {rf:+.3f}"
    assert abs(rf) < 0.15, "B3: early thermal state uninformative"
    curve = [v for v in d['pooled_Tw'] if v is not None]
    # grid starts at t = 10 (mid equilibration dip): between init 0.400 and floor
    assert 0.385 < curve[0] < 0.400, "thermometer curve consistent at t=10"
    print(f"B1: rho_T = {rhoT:.4f} (bar 0.90) -- FLAT; instrument audited")
    print(f"B2 (moot, descriptive): R_pred ~ 1.00 vs R_meas = {R:.3f}")
    print(f"B3: rho_frail = {rf:+.3f} -- early state carries no fate")
    print("PASS: NON-THERMAL AGING -- hazard falls 2-3x at constant bath")
    print("      temperature with uninformative early state; the dressed drive")
    print("      is the named suspect; Prediction 11 gains the flat-temperature")
    print("      dark-count-drift signature.")


if __name__ == "__main__":
    test()
