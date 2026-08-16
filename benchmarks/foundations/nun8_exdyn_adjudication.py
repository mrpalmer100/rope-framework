#!/usr/bin/env python3
"""NUN8 (FND-113): GRANT-EXDYN-OVERLAP adjudication at the pre-built bar.

Granted form (FND-112, fixed before computation): exchange amplitude =
transverse profile overlap along the transport path; direct path d,
reversed path 2d; w2 = O(2d)/O(d); echo per partner at own amplitude:
    f(N) = (1 + w2)/2 + w2/(N-1)
Near-coaxial reading (FND-108): binding fraction = overlap fraction,
    O(d_N) = f(N)   [one equation, one unknown, zero free parameters]
Profile: CHROMO-PROFILE-CLEM (FND-111), E(x_t) ~ K0(sqrt(mu^2 x_t^2
+ alpha^2)), central alpha = 1/0.27 per NUN8 bars B3.

VERDICT (registered): NOT-SOLVABLE for N = 4, 5, 6 across the whole
alpha band [3.0, 4.2] -> DEMOTED per bars B4. The N -> infinity
equation alone has a solution (f = 0.658-0.671, inside the 0.64(10)
band) but at d* = 2.4-2.8 / mu, outside the near-coaxial condition.
"""
import numpy as np
from scipy.special import k0
from scipy import optimize

def make_O(alpha, L=14.0, n=700):
    x = np.linspace(-L, L, n)
    X, Y = np.meshgrid(x, x, indexing='ij')
    R = np.sqrt(X**2 + Y**2)
    E = k0(np.sqrt(R**2 + alpha**2))
    norm = np.sum(E * E)
    dx = x[1] - x[0]
    def O(d):
        s = d / dx
        i = int(np.floor(s)); fr = s - i
        if i + 1 >= n:
            return 0.0
        Esh = (1 - fr) * np.roll(E, i, axis=0) + fr * np.roll(E, i + 1, axis=0)
        Esh[:i + 1, :] = 0.0
        return float(np.sum(E * Esh) / norm)
    return O

def main():
    for alpha in (3.0, 1 / 0.27, 4.2):
        O = make_O(alpha)
        print(f"alpha = {alpha:.3f}")
        for N in (4, 5, 6):
            ds = np.linspace(0.05, 8.0, 300)
            gaps = []
            for d in ds:
                Od, O2d = O(d), O(2 * d)
                w2 = O2d / Od
                gaps.append((1 + w2) / 2 + w2 / (N - 1) - Od)
            gmin = min(gaps)
            print(f"  N={N}: min(f_demand - O) = {gmin:+.4f} "
                  f"-> {'SOLUTION' if gmin <= 0 else 'NO SOLUTION'}")
        g = lambda d: O(d) - (1 + O(2 * d) / O(d)) / 2
        r = optimize.brentq(g, 1.0, 6.0, xtol=1e-6)
        print(f"  N=inf: d* = {r:.4f}/mu, f = {O(r):.4f}")

if __name__ == "__main__":
    main()
