#!/usr/bin/env python3
"""COMMISSION KAF -- the bundle-binding computation.

Bars locked first: analysis/KAF_bundle_binding_bars_LOCKED.md.
Registered functional: e(x) = T0 (x/2 - x^2/8)  [FND-040, softening]
Counter-reading:       e(x) = T0 (x/2 + x^2/8)  [EM-RECON-009 at k=2T0]
Winding additivity: k-string = k unit windings (GG-006, FND-048).
Registered strain domain: x <= 0.04 (FND-040 dominance clause).

Configuration family (Q1): overlap fraction f in [0, 1].
k windings; a fraction f of each tube's profile volume is shared coherently
(strain multiplies k-fold there), the remainder disjoint. Per unit profile
volume of a single tube:
  E(f) = f * e(k^2 x) / k_share + (1 - f) * k * e(x)   -- careful bookkeeping:
Coherent region: ONE region carrying strain variable k^2 x (gradient adds
k-fold, x is the squared measure), volume f (shared by all k).
Disjoint remainder: k regions of volume (1 - f) each at strain x.
  E(f) = f * e(k^2 x) + k * (1 - f) * e(x)
E(0) = k e(x) (separated), E(1) = e(k^2 x) (fully coherent).
The minimum over f is taken; nothing is chosen by hand.
"""
import math

X_REG = 0.04          # registered tube-strain bound (FND-040)
BRACKET = (1.600, 1.767)   # pre-committed SU(6) k=2 bar

def e_soft(x): return x / 2 - x * x / 8      # FND-040
def e_stiff(x): return x / 2 + x * x / 8     # EM-RECON-009 @ k=2T0

def E(f, k, x, e): return f * e(k * k * x) + k * (1 - f) * e(x)

def minimize(k, x, e, n=100001):
    best = min(range(n), key=lambda i: E(i / (n - 1), k, x, e))
    f = best / (n - 1)
    return f, E(f, k, x, e)

def casimir_ratio(N, k): return k * (N - k) / (N - 1)
def sine_ratio(N, k): return math.sin(math.pi * k / N) / math.sin(math.pi / N)

print("Q1 -- sign, both quartic readings, k = 2..4 at x =", X_REG)
for name, e in (("FND-040 softening", e_soft), ("EM-RECON-009 stiffening", e_stiff)):
    print(f"  [{name}]")
    for k in (2, 3, 4):
        f, Emin = minimize(k, X_REG, e)
        Esep = E(0, k, X_REG, e)
        ratio = Emin / e(X_REG)
        bound = "BOUND" if Emin < Esep - 1e-15 else "UNBOUND"
        print(f"    k={k}: f_min={f:.3f}  sigma_k/sigma_1={ratio:.4f}  "
              f"(k sigma_1 -> {k})  {bound}")

print("\nQ1b -- strain threshold for binding (softening reading, coherent vs sep):")
for k in (2, 3, 4):
    x_thr = 4 / (k * k + k + 1)   # exact: binding iff x > 4/(k^2+k+1)
    print(f"    k={k}: binding requires x > {x_thr:.3f} "
          f"({x_thr / X_REG:.0f}x above the registered bound)")

print("\nQ2 -- the pre-committed bracket, SU(6) k=2:")
pred = minimize(2, X_REG, e_soft)[1] / e_soft(X_REG)
lo, hi = BRACKET
print(f"    prediction sigma_2/sigma_1 = {pred:.4f} vs bracket [{lo}, {hi}]"
      f"  -> {'LANDS' if lo <= pred <= hi else 'MISS'}"
      f" ({100 * (pred - hi) / hi:+.1f}% past the upper edge)" )

print("\nQ3 -- (N,k) form: the registered ontology's N-carrier check.")
print("    Inputs: T0, x, k (winding count). N appears NOWHERE. The derived")
print("    law is N-independent: sigma_k/sigma_1 = k at registered strains.")
print("    Required binding fraction b_k(N) = 1 - sigma_k/(k sigma_1), per row:")
for N in (4, 6, 8):
    for k in (2, 3):
        if k >= N: continue
        bc = 1 - casimir_ratio(N, k) / k
        bs = 1 - sine_ratio(N, k) / k
        print(f"    SU({N}) k={k}: Casimir b={bc:.3f}  sine b={bs:.3f}")
print("    Data ordering: b decreases with N (vanishes as N -> infinity),")
print("    b ~ (k-1)/(N-1) at Casimir -- an explicit 1/N structure the")
print("    additive-winding ontology cannot produce from registered claims.")
