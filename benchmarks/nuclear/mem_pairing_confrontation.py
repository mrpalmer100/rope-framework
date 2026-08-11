#!/usr/bin/env python3
"""COMMISSION MEM -- NUC-024's derived pairing vs the table.

Bars: analysis/MEM_pairing_confrontation_bars_LOCKED.md.
H1: S = 6.11 MeV (A-independent, NUC-024). H2: S = 24/sqrt(A) (empirical).
Measurement: binned 2*coef(D2) from the round-2 LAMED residual.
"""
import numpy as np, glob, os, masstable

rng = np.random.default_rng(3141)
D_H, D_N = 7.28897, 8.07132
MAGIC = np.array([2, 8, 20, 28, 50, 82, 126])
path = [p for p in glob.glob(os.path.dirname(masstable.__file__) + "/data/*")
        if p.endswith("AME2012.txt")][0]
rows = [l.split() for l in open(path).read().splitlines()[1:] if l.strip()]
Z = np.array([int(r[0]) for r in rows]); N = np.array([int(r[1]) for r in rows])
DEL = np.array([float(r[2]) for r in rows]); A = Z + N
B = Z * D_H + N * D_N - DEL
keep = A >= 12
Z, N, A, B = Z[keep], N[keep], A[keep], B[keep]

r0d = (3 / (4 * np.pi * np.sqrt(2))) ** (1 / 3)
D0, RATIO, A_A = 2.026, 1.108, 19.85
A_C = 0.6 * 1.44 / (r0d * D0)
Bca = B[(A == 40) & (Z == 20)][0]
A_V = (Bca + A_C * 400 / 40**(1/3)) / (40 - RATIO * 40**(2/3))
R = B - (A_V * A - RATIO * A_V * A**(2/3) - A_C * Z**2 / A**(1/3)
         - A_A * (N - Z)**2 / A)

def vdist(x): return np.min(np.abs(x[:, None] - MAGIC[None, :]), axis=1)
D1 = vdist(Z) + vdist(N)
D2 = np.where((Z % 2 == 0) & (N % 2 == 0), 1, np.where((A % 2) == 1, 0, -1))
X = np.column_stack([np.ones(len(A)), D1, D2, A**(1/3), Z / A,
                     ((A % 4 == 0) & (Z == N)).astype(float),
                     (N - Z)**4 / A**3])
idx = rng.permutation(len(R)); half = len(R) // 2
tr = np.zeros(len(R), bool); tr[idx[:half]] = True

BINS = [(12, 40), (40, 80), (80, 120), (120, 160), (160, 200), (200, 260)]
print("bin        n     S_hat +/- 2SE     H1=6.11ok  H2=24/sqrt(A)ok  sign tr/te")
S, SE, AM = [], [], []
for lo, hi in BINS:
    m = (A >= lo) & (A < hi)
    Xb, Rb = X[m], R[m]
    beta, *_ = np.linalg.lstsq(Xb, Rb, rcond=None)
    res = Rb - Xb @ beta
    s2 = res @ res / (len(Rb) - Xb.shape[1])
    cov = s2 * np.linalg.pinv(Xb.T @ Xb)
    s_hat, se = 2 * beta[2], 2 * np.sqrt(cov[2, 2])
    am = A[m].mean()
    h2 = 24 / np.sqrt(am)
    ok1 = abs(s_hat - 6.11) <= 2 * se / 2 * 2  # within 2 sigma (se already 2SE)
    ok1 = abs(s_hat - 6.11) <= se
    ok2 = abs(s_hat - h2) <= se
    bt, *_ = np.linalg.lstsq(X[m & tr], R[m & tr], rcond=None)
    bv, *_ = np.linalg.lstsq(X[m & ~tr], R[m & ~tr], rcond=None)
    S.append(s_hat); SE.append(se / 2); AM.append(am)
    print(f"[{lo:>3},{hi:>3})  {m.sum():4d}   {s_hat:+6.2f} +/- {se:4.2f}   "
          f"{'yes' if ok1 else 'NO ':>3}        {'yes' if ok2 else 'NO ':>3} "
          f"(H2={h2:4.2f})      {np.sign(bt[2])==np.sign(bv[2])}")

S, SE, AM = map(np.array, (S, SE, AM))
w = 1 / SE**2
# H1 chi2 (no free parameter): S = 6.11; H2: S = 24/sqrt(A)
chi1 = np.sum(w * (S - 6.11)**2)
chi2 = np.sum(w * (S - 24 / np.sqrt(AM))**2)
# trend: WLS slope of S on A^(-1/2), significance of falling trend
xm = AM**-0.5
xc = xm - np.average(xm, weights=w)
slope = np.sum(w * xc * S) / np.sum(w * xc**2)
sl_se = np.sqrt(1 / np.sum(w * xc**2))
print(f"\nchi2 (6 bins, zero params): H1 A-independent = {chi1:.1f} | "
      f"H2 24/sqrt(A) = {chi2:.1f}")
print(f"trend: dS/d(A^-1/2) = {slope:+.1f} +/- {sl_se:.1f} "
      f"({slope/sl_se:+.1f} sigma; positive slope = S falls with A)")
