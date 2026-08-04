"""FND-STRAND-016 (Modeled): FORCE-NOISE SPECTROSCOPY -- the dressed-drive
mechanism KILLED; the exclusion triangle closes; the smallest box is
registered MECHANISM-OPEN and the theory session is commissioned by the
bars' own pre-committed consequence.

Bars locked blind with the FLAT consequence committed in advance
(analysis/STRAND016_force_noise_bars_LOCKED.md); results with the
kill-verdict audit on their face (analysis/STRAND016_force_noise_results.md);
lean archived dataset (analysis/STRAND016_force_noise_data.json).

(B1) FLAT: rho_V = 0.9994 vs a 0.90 reduction bar -- dressed-drive
     intensity constant to 6 parts in 10^4; instrument audited against the
     closed-form FDT initialization (within 5%, the K-subsampling offset).
(B2) MOOT; descriptively R_pred = 0.997 vs R_meas = 0.428.
(B3) NOT-TRACEABLE at the boundary: rho = -0.1497 (p = 0.09), trivial sign.

THE EXCLUSION TRIANGLE, three sessions, three instruments: hazard falls
2-3x (thrice replicated: 0.33/0.43/0.43) while kinetic temperature is flat
(5e-4), drive intensity is flat (6e-4), and no early-state covariate
carries fate. The non-exponential escape at N = 24 is invisible to every
natural state variable of the noise channel -- the stochastic-process
language ("hazard", "aging") imported from the Langevin limit may itself be
the error, and the commissioned theory session must decide between
phase-pattern frailty, recurrence-structured deterministic first-passage,
and spectral reshaping. Prediction 11's honest form: NON-EXPONENTIAL
dark-count waiting times at small scale, with drift-vs-diversity open.

This benchmark refits the archived dataset and pins the registered numbers.
"""
import json
import os

import numpy as np

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, '..', '..', 'analysis',
                    'STRAND016_force_noise_data.json')


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
    esc = np.array(d['esc']); V0i = np.array(d['V0i'])
    assert len(esc) == 128 and np.isfinite(esc).all(), "census complete"
    rhoV = d['V_late']/d['V_early']
    assert abs(rhoV - 0.9994) < 0.002, f"flat verdict pinned, got {rhoV:.4f}"
    assert rhoV >= 0.97, "B1: FLAT -- dressed-drive mechanism killed"
    assert abs(d['V0_pool']/d['V_theory'] - 0.95) < 0.03, \
        "audit: instrument reads FDT initialization (K-subsampling offset)"
    R = _lam(esc, 0.50, 0.90)/_lam(esc, 0.25, 0.50)
    assert abs(R - 0.428) < 0.02, f"hazard ratio pinned, got {R:.3f}"
    assert R <= 0.7, "the phenomenon replicates a third time"
    rf = _spearman(esc, V0i)
    assert abs(rf - (-0.1497)) < 0.02, f"B3 rho pinned, got {rf:+.4f}"
    print(f"B1: rho_V = {rhoV:.4f} (bar 0.90) -- FLAT; instrument audited (5%)")
    print(f"B2 (moot): R_pred ~ 1.00 vs R_meas = {R:.3f}")
    print(f"B3: rho_drive = {rf:+.3f} -- not traceable (boundary reported)")
    print("PASS: the exclusion triangle closes -- temperature, drive intensity,")
    print("      and early state all innocent while the hazard falls thrice-")
    print("      replicated. MECHANISM-OPEN; the theory session is commissioned.")


if __name__ == "__main__":
    test()
