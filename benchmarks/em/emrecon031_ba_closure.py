"""COMMISSION EM-RECON-031 -- the b/a closure.

Executed under analysis/EMRECON031_ba_closure_bars_LOCKED.md.
Inputs (all registered): c4 = T0/8 (k/T0 = 2 adjudicated, FND-027);
exponential mode profiles; operating amplitude g* = 2 (the Kerr
saturation strain at k/T0 = 2). Full quartic cross-energy, no
model-form truncation; equilibrium found directly.
Targets: nuclear d0/L = 1.36, chemical bond/healing = 1.67; bands
+-25 percent (the registered log-weak honesty level).
"""
import numpy as np

T0 = 1.0
C4 = T0 / 8.0
XI = 1.0

def profile(x, center, g):
    return g * np.exp(-np.abs(x - center) / XI)

def energy(d, g):
    x = np.linspace(-30, 30, 240001)
    g1 = profile(x, -d/2, g)
    g2 = profile(x, +d/2, g)
    I2 = np.trapezoid(g1*g2, x)
    I31 = np.trapezoid(g1**3 * g2, x)
    I22 = np.trapezoid(g1**2 * g2**2, x)
    I13 = np.trapezoid(g1 * g2**3, x)
    return -(T0/2.0)*I2 + C4*(4*I31 + 6*I22 + 4*I13)

def d0(g):
    ds = np.linspace(0.05, 8.0, 1600)
    E = np.array([energy(d, g) for d in ds])
    i = int(np.argmin(E))
    if i == 0 or i == len(ds)-1:
        return None
    # parabolic refine
    a, b, c = E[i-1], E[i], E[i+1]
    dd = ds[1]-ds[0]
    return ds[i] + 0.5*dd*(a-c)/(a-2*b+c)

def main():
    print("EM-RECON-031 -- the b/a closure (locked bars)")
    print(f"c4/T0 = {C4:.4f}; g* = 2 (saturation strain at k/T0 = 2)\n")
    r = d0(2.0)
    if r is None:
        print("NO-MINIMUM at g* = 2 -> FAIL (kept)")
        return
    print(f"M1: d0/xi = {r:.4f} at g* = 2, zero free parameters")
    for name, t in (("nuclear 1.36", 1.36), ("chemical 1.67", 1.67)):
        dev = abs(r - t)/t
        print(f"  vs {name}: deviation {dev*100:.1f} percent -> "
              f"{'PASS' if dev <= 0.25 else 'MISS'}")
    print("\nM2 sensitivity (disclosure): d0/xi over g in [1, 3]:")
    for g in (1.0, 1.5, 2.0, 2.5, 3.0):
        rr = d0(g)
        print(f"  g = {g:.1f}: d0/xi = {'NONE' if rr is None else f'{rr:.4f}'}")

if __name__ == "__main__":
    main()
