#!/usr/bin/env python3
"""COMMISSION LAMED -- the nuclear residual classifier.

Bars locked first: analysis/LAMED_residual_classifier_bars_LOCKED.md.
Baseline: registered rope SEMF chain (NUC-018 corrected geometry, NUC-A/B
derived asymmetry 19.85 MeV, a_V calibrated once on Ca-40, pairing excluded
per the locked bar). Data: AME2012 evaluated masses (masstable package).
Protocol: seed-3141 50/50 split, OLS, univariate + joint out-of-sample R^2,
swap test, 1000-permutation null.
"""
import numpy as np, glob, os

rng = np.random.default_rng(3141)
D_H, D_N = 7.28897, 8.07132
MAGIC = np.array([2, 8, 20, 28, 50, 82, 126])

# --- data ---
import masstable
path = [p for p in glob.glob(os.path.dirname(masstable.__file__) + "/data/*")
        if p.endswith("AME2012.txt")][0]
rows = [l.split() for l in open(path).read().splitlines()[1:] if l.strip()]
Z = np.array([int(r[0]) for r in rows]); N = np.array([int(r[1]) for r in rows])
DEL = np.array([float(r[2]) for r in rows])
A = Z + N
B = Z * D_H + N * D_N - DEL
keep = A >= 12
Z, N, A, B = Z[keep], N[keep], A[keep], B[keep]

# --- registered baseline (fixed by the locked bar) ---
r0_over_d0 = (3 / (4 * np.pi * np.sqrt(2))) ** (1 / 3)
D0 = 2.026                       # NUC-017
AS_OVER_AV = 1.108               # NUC-018 registered-best row (round 2 addendum)
A_C = 0.6 * 1.44 / (r0_over_d0 * D0)   # derived Coulomb
A_A = 19.85                      # NUC-A + NUC-B (derived)
# calibrate a_V once on Ca-40:
Aca, Zca = 40, 20
Bca = B[(A == 40) & (Z == 20)][0]
A_V = (Bca + A_C * Zca**2 / Aca**(1/3)) / (Aca - AS_OVER_AV * Aca**(2/3))
def b_rope(A, Z):
    Nn = A - Z
    return (A_V * A - AS_OVER_AV * A_V * A**(2/3)
            - A_C * Z**2 / A**(1/3) - A_A * (Nn - Z)**2 / A)
R = B - b_rope(A, Z)

# --- descriptors (closed list) ---
def vdist(x): return np.min(np.abs(x[:, None] - MAGIC[None, :]), axis=1)
D1 = vdist(Z) + vdist(N)
D2 = np.where((Z % 2 == 0) & (N % 2 == 0), 1, np.where((A % 2) == 1, 0, -1))
D3 = A ** (1 / 3)
D4 = Z / A
D5 = ((A % 4 == 0) & (Z == N)).astype(float)
D6 = (N - Z) ** 4 / A ** 3
X = np.column_stack([np.ones_like(D3), D1, D2, D3, D4, D5, D6])
names = ["const", "D1 shell", "D2 pairing", "D3 curvature",
         "D4 linking", "D5 alpha", "D6 iso-quartic"]

# --- split (seed 3141, drawn blind) ---
idx = rng.permutation(len(R)); half = len(R) // 2
tr, te = idx[:half], idx[half:]

def ols(Xm, y):
    beta, *_ = np.linalg.lstsq(Xm, y, rcond=None); return beta
def r2(y, yhat):
    ss = np.sum((y - yhat) ** 2); tot = np.sum((y - np.mean(y)) ** 2)
    return 1 - ss / tot

print(f"nuclides (A>=12): {len(R)}; residual R = B_exp - B_rope")
print(f"a_V = {A_V:.3f}, a_S/a_V = {AS_OVER_AV}, a_C = {A_C:.4f}, a_A = {A_A}")
print(f"R stats: mean {R.mean():.2f} MeV, rms {np.sqrt((R**2).mean()):.2f}, "
      f"train rms {np.sqrt((R[tr]**2).mean()):.2f}")

print("\nUNIVARIATE out-of-sample R^2 (bar: >= 0.5):")
uni = {}
for j in range(1, 7):
    Xu = X[:, [0, j]]
    b = ols(Xu[tr], R[tr]); s = r2(R[te], Xu[te] @ b)
    uni[names[j]] = s
    print(f"  {names[j]:>15}: {s:+.3f} {'FINDING' if s >= 0.5 else ''}")

b = ols(X[tr], R[tr])
joint = r2(R[te], X[te] @ b)
b_sw = ols(X[te], R[te])
resid_tr = R[tr] - X[tr] @ b
sigma2 = np.sum(resid_tr**2) / (len(tr) - X.shape[1])
cov = sigma2 * np.linalg.inv(X[tr].T @ X[tr])
tvals = b / np.sqrt(np.diag(cov))
print(f"\nJOINT out-of-sample R^2 = {joint:+.3f} (bar: >= 0.6)")
print("coef (train)     t      coef (swap)   sign-stable?")
swap_ok = True
for j in range(len(names)):
    stable = np.sign(b[j]) == np.sign(b_sw[j])
    if abs(tvals[j]) > 3 and not stable: swap_ok = False
    print(f"  {names[j]:>15}: {b[j]:+9.4f}  t={tvals[j]:+7.1f}  "
          f"{b_sw[j]:+9.4f}  {'yes' if stable else 'NO'}"
          f"{'  (retained)' if abs(tvals[j])>3 else ''}")

perm = np.empty(1000)
for i in range(1000):
    yp = rng.permutation(R[tr])
    bp = ols(X[tr], yp)
    perm[i] = r2(R[te], X[te] @ bp)
p = np.mean(perm >= joint)
print(f"\nPERMUTATION (1000): null oos R^2 max {perm.max():+.3f}, "
      f"p(joint by chance) = {p:.4f} (bar: < 0.01)")
print(f"swap test: {'PASS' if swap_ok else 'FAIL'}")

verdict = ("STRUCTURE-FOUND" if joint >= 0.6 and swap_ok and p < 0.01
           else "DIFFUSE" if joint > 0 else "NULL")
print(f"\nVERDICT (pre-committed grammar): {verdict}")
print("findings (univariate):", [k for k, v in uni.items() if v >= 0.5] or "none")
