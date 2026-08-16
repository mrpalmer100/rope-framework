"""COMMISSION EM-RECON-036 -- the registered-class closure.

Executed under analysis/EMRECON036_registered_class_bars_LOCKED.md.
For the first time in the arc, the profile is the registry's own
(MODE_OVERLAP_DERIVATION.md Sec 2 / harness line 13):
    f(r) = w(rho_perp/xi) e^(-rho/xi),  w(u) = u/sqrt(1+u^2)
(spherical envelope, cylindrical vortex core about the winding axis;
scalar strain amplitude; peak strain = g via f_max = 0.284878).
Inputs unchanged: c4 = T0/8, verdict at g* = 2, targets nuclear 1.36 /
chemical 1.67, bands +-25 percent, joint band [1.2525, 1.70]. Zero
free parameters, zero profile freedom.

Orientation handled by energy, not choice: coaxial / parallel-
transverse / crossed all computed; coaxial minimizes (E = -1.343 vs
-1.005) -- the sigma-like head-on geometry, consistent in direction
with EM-RECON-007's sigma > pi ordering (display).

VERDICT (registered): FAIL, kept. At g* = 2 the equilibrium is
d0/xi = 5.2003 (grid-converged at n = 140/180/220, identical to 4
decimals; integrator anchored on the analytic 3D Gaussian identity to
<0.001 percent). Outside both bands. Amplitude sweep (display, never
used): g = 0.7 -> 1.23, 0.9 -> 2.15, 1.0 -> 2.51, 1.5 -> 3.97,
2.0 -> 5.20, 2.5 -> 6.38, 3.0 -> NO-MINIMUM; the joint band is
reached only near g ~ 0.71-0.80, roughly 2.5-2.8x BELOW the Kerr
saturation identification; equilibrium abolished above g ~ 2.6-3,
echoing EM-RECON-031's abolition finding.

With profile freedom gone, the arc's residual points at exactly one
remaining suspect: the operating-amplitude identification (g* = 2).
"""
import numpy as np

T0, C4, FMAX = 1.0, 1.0 / 8.0, 0.284878

def d0_coax(g, n=140, L=9.0, lo=0.1, hi=7.5, npts=60):
    x = np.linspace(-L, L, n); dx = x[1] - x[0]
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    def f(cx):
        rho = np.sqrt((X - cx) ** 2 + Y ** 2 + Z ** 2)
        rp = np.sqrt(Y ** 2 + Z ** 2)
        return g * (rp / np.sqrt(1 + rp * rp)) * np.exp(-rho) / FMAX
    ds = np.linspace(lo, hi, npts); Es = []
    for d in ds:
        f1 = f(-d / 2); f2 = f(+d / 2)
        Es.append((-(T0 / 2) * np.sum(f1 * f2)
                   + C4 * (4 * np.sum(f1 ** 3 * f2)
                           + 6 * np.sum(f1 ** 2 * f2 ** 2)
                           + 4 * np.sum(f1 * f2 ** 3))) * dx ** 3)
    Es = np.array(Es); i = int(np.argmin(Es))
    if i == 0 or i == len(ds) - 1:
        return None
    a, b, c = Es[i - 1], Es[i], Es[i + 1]; dd = ds[1] - ds[0]
    return ds[i] + 0.5 * dd * (a - c) / (a - 2 * b + c)

def main():
    print("EM-RECON-036 -- the registered-class closure (locked bars)")
    r = d0_coax(2.0)
    print(f"coaxial equilibrium at g* = 2: d0/xi = {r:.4f}")
    print("bands: nuclear [1.02, 1.70]; chemical [1.2525, 2.0875]")
    print("verdict: FAIL (outside both), kept\n")
    print("amplitude sweep (display only):")
    for g in (0.7, 0.9, 1.0, 1.5, 2.0, 2.5, 3.0):
        x = d0_coax(g)
        print(f"  g = {g}: d0/xi = {'NONE' if x is None else f'{x:.4f}'}")

if __name__ == "__main__":
    main()
