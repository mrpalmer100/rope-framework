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
import numpy as np
from scipy.special import k0
from scipy import integrate, optimize

T0, C4, XI = 1.0, 1.0 / 8.0, 1.0

def make(rw):
    norm = k0(rw / XI)
    return lambda rr: k0(np.maximum(rr, rw) / XI) / norm

def energy(d, rw, g=2.0):
    f = make(rw)
    def I(m, n):
        def integrand(rr, th):
            r2 = np.sqrt(rr * rr + d * d - 2 * rr * d * np.cos(th))
            return (g * f(rr)) ** m * (g * f(r2)) ** n * rr
        v, _ = integrate.dblquad(lambda th, rr: integrand(rr, th),
                                 0, 22, 0, np.pi,
                                 epsabs=1e-10, epsrel=1e-7)
        return 2 * v
    return -(T0 / 2) * I(1, 1) + C4 * (4 * I(3, 1) + 6 * I(2, 2) + 4 * I(1, 3))

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
