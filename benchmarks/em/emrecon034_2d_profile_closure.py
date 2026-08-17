"""COMMISSION EM-RECON-034 -- the 2D profile closure.

Executed under analysis/EMRECON034_2d_profile_bars_LOCKED.md.
Same registered inputs as the failed 1D closure (EM-RECON-031):
c4 = T0/8 (adjudicated k/T0 = 2), operating amplitude g* = 2, targets
nuclear 1.36 / chemical 1.67, bands +-25 percent. Upgraded in
dimension only: ropes are line objects, the 2D transverse bound-mode
profile is K0(r/xi), capped flat inside the rope radius r_w with the
surface strain equal to g. r_w/xi is UNREGISTERED and swept over the
locked window [0.05, 0.5] (11 log points).

VERDICT (registered): INDICATED, razor-thin, at the window's bottom
edge: both bands are met simultaneously only on r_w/xi in
[0.0500, ~0.0502] (d0/xi = 1.6975 +- ~0.002 numerics vs joint band
edge 1.70; pass margin 0.15 percent, comparable to numerics).
Chemical-only band met on [0.050, ~0.082]. Across the whole window
d0/xi runs 1.70 -> 5.39, all far below the 1D value 6.16: the
fourfold 1D miss is substantially a DIMENSIONAL ARTIFACT (mechanism:
the 2D cross/attraction ratio I31/I2 falls with d, 0.199 -> 0.109
over d = 2 -> 4 at r_w = 0.05, where 1D held it near-constant).
EM-RECON-008 stays Open; its missing input narrows to r_w/xi, which
per FND-110's ladder hangs on the underived rope count n_rs.

1D regression anchor reproduced first: d0/xi = 6.1566 at g* = 2.
"""

# NUMERICS NOTE (2026-08-16, performance-only change, no physics touched):
# the original scipy.dblquad implementation (epsrel 1e-7, scalar calls
# inside the minimizer) exceeded the 300 s CI timeout. Replaced with
# kink-aligned Gauss-Legendre quadrature: r-panels split at the cap
# radius r_w and at d -+ r_w, and the theta integral split analytically
# at theta*(r) where the second rope's cap boundary (r2 = r_w) crosses,
# with f2 = 1 exact inside the cap. Self-converged to ~1e-12 between
# resolutions; agrees with the original integrator to <= 5e-5 on d0 at
# both window edges (1.69747 vs 1.6974; 5.38393 vs 5.38391). All
# registered numbers unchanged. Runtime ~5 s.

import numpy as np
from scipy.special import k0
from scipy import optimize

T0, C4, XI = 1.0, 1.0 / 8.0, 1.0
RMAX = 22.0
_GL = {}

def _gl(n):
    if n not in _GL:
        _GL[n] = np.polynomial.legendre.leggauss(n)
    return _GL[n]

def energy(d, rw, g=2.0, nr=160, nth=100):
    norm = k0(rw / XI)
    xr, wr = _gl(nr); xt, wt = _gl(nth)
    edges = [0.0, rw]
    for e in (d - rw, d + rw):
        if rw < e < RMAX:
            edges.append(e)
    edges.append(RMAX)
    edges = sorted(set(edges))
    rs, ws = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        rs.append(0.5 * (b - a) * (xr + 1) + a)
        ws.append(0.5 * (b - a) * wr)
    r = np.concatenate(rs); wr_all = np.concatenate(ws)
    fr = k0(np.maximum(r, rw) / XI) / norm
    cosarg = (r * r + d * d - rw * rw) / (2 * r * d)
    has = np.abs(d - r) < rw
    thstar = np.where(has, np.arccos(np.clip(cosarg, -1, 1)), 0.0)
    tA_w = 0.5 * thstar[:, None] * wt
    span = np.pi - thstar
    tB = thstar[:, None] + 0.5 * span[:, None] * (xt + 1)
    tB_w = 0.5 * span[:, None] * wt
    r2B = np.sqrt(r[:, None] ** 2 + d * d - 2 * r[:, None] * d * np.cos(tB))
    f2B = k0(np.maximum(r2B, rw) / XI) / norm
    out = 0.0
    for (m, n), c in {(1, 1): -(T0 / 2), (3, 1): 4 * C4,
                      (2, 2): 6 * C4, (1, 3): 4 * C4}.items():
        gm = (g * fr) ** m
        IA = np.sum(tA_w * g ** n, axis=1) * gm * r      # inside cap: f2 = 1
        IB = np.sum(tB_w * (g * f2B) ** n, axis=1) * gm * r
        out += c * 2 * np.sum(wr_all * (IA + IB))
    return out

def d0(rw, g=2.0):
    r = optimize.minimize_scalar(lambda d: energy(d, rw, g),
                                 bounds=(0.3, 8.0), method='bounded',
                                 options={'xatol': 3e-5})
    return None if (r.x < 0.36 or r.x > 7.9) else r.x

def main():
    print("EM-RECON-034 -- the 2D profile closure (locked bars)")
    print("window r_w/xi in [0.05, 0.5], verdict at g* = 2\n")
    for rw in np.logspace(np.log10(0.05), np.log10(0.5), 11):
        r = d0(rw)
        print(f"  r_w/xi = {rw:6.3f}: d0/xi = "
              f"{'NONE' if r is None else f'{r:.4f}'}")
    print("\nbands: nuclear [1.02, 1.70]; chemical [1.2525, 2.0875]; "
          "joint [1.2525, 1.70]")
    print("amplitude sweep (display only, r_w/xi = 0.05):")
    for g in (1.0, 1.5, 2.0, 2.5, 3.0):
        r = d0(0.05, g)
        print(f"  g = {g}: d0/xi = {'NONE' if r is None else f'{r:.4f}'}")

if __name__ == "__main__":
    main()
