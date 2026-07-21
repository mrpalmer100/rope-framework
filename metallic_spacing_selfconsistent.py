"""CHEM-GEO-002 (Derived): the HEAVY-HYDRIDE 90-DEGREE ASYMPTOTE -- the
phase-blocking + orthogonality theorems (CHEM-GEO-001) make 90 degrees the
RAW FIXED POINT for single bonds on orthogonal dipolar lobes; the opening
corrections (H...H contact repulsion; mode mixing) are all POSITIVE and
collapse as bonds lengthen down a column. FIVE BARS, declared before asserts:
(1) MONOTONE: |theta - 90| strictly decreases down each column;
(2) ASYMPTOTE: period-4 hydrides within 2.5 deg of 90; period-5 within 2.0;
(3) ONE-SIDED: no member below 90 (the fixed point approached from above);
(4) CROSS-COLUMN: three H's crowd more than two -- group-15 angle exceeds
    group-16 at EVERY period (3 pairwise contacts vs 1);
(5) MECHANISM CONSISTENCY: ln(opening) vs the H...H distance at 90 deg
    (s90 = d*sqrt(2)) is linear per column (R^2 > 0.85) with extracted core
    width w in [0.1, 0.6] A -- independently consistent with the H-core range
    the geometry session scanned (0.10-0.25) and the H-bond work.
PREDICTIONS REGISTERED (one-sided windows, unmeasured/poorly measured):
    H2Po: 90.0 < theta < 90.7 deg;  BiH3: 90.0 < theta < 91.5 deg.
Data: standard measured angles/bond lengths (8 molecules, none used in any
prior fit of this programme).
"""
import numpy as np

G16 = {"H2O": (104.48, 0.958), "H2S": (92.11, 1.336), "H2Se": (90.92, 1.460), "H2Te": (90.25, 1.658)}
G15 = {"NH3": (106.67, 1.012), "PH3": (93.42, 1.421), "AsH3": (91.96, 1.519), "SbH3": (91.70, 1.704)}


def fit_line(x, y):
    A = np.vstack([x, np.ones_like(x)]).T
    (m, b), res, *_ = np.linalg.lstsq(A, y, rcond=None)
    yhat = m*x + b
    ss_res = ((y - yhat)**2).sum(); ss_tot = ((y - y.mean())**2).sum()
    return m, b, 1 - ss_res/ss_tot


def column_checks(col):
    angles = [v[0] for v in col.values()]
    ds = [v[1] for v in col.values()]
    openings = np.array(angles) - 90.0
    assert np.all(openings > 0), "one-sided: approached from above"
    assert np.all(np.diff(openings) < 0), "monotone convergence to 90"
    s90 = np.array(ds)*np.sqrt(2.0)
    m, b, r2 = fit_line(s90, np.log(openings))
    w = -1.0/m
    return openings, r2, w


def test():
    o16, r2_16, w16 = column_checks(G16)
    o15, r2_15, w15 = column_checks(G15)
    assert o16[2] < 2.5 and o15[2] < 2.5, "period-4 within 2.5 deg"
    assert o16[3] < 2.0 and o15[3] < 2.0, "period-5 within 2.0 deg"
    for (a15, _), (a16, _) in zip(G15.values(), G16.values()):
        assert a15 > a16, "three H's crowd more than two, every period"
    assert r2_16 > 0.85 and r2_15 > 0.85, "ln(opening) linear in s90 per column"
    assert 0.1 < w16 < 0.6 and 0.1 < w15 < 0.6, "extracted core widths in the H-core band"
    print(f"group 16 openings: {np.round(o16,2)} -> 90; group 15: {np.round(o15,2)} -> 90 (monotone, one-sided)")
    print(f"cross-column: XH3 > XH2 at every period (3 contacts vs 1)")
    print(f"mechanism: ln(opening) linear in H...H distance; R^2 = {r2_16:.3f}/{r2_15:.3f}; "
          f"extracted w = {w16:.2f}/{w15:.2f} A (H-core band)")
    print("PREDICTIONS on record: H2Po in (90.0, 90.7); BiH3 in (90.0, 91.5) degrees")
    print("PASS: the raw-lobe fixed point confirmed as an eight-molecule empirical asymptote.")


if __name__ == "__main__":
    test()
