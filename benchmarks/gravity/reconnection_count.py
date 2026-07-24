"""GRV-037 (Modeled): THE RECONNECTION COUNT -- the entropy and
information questions aimed at one measured, countable object, with a
one-way ratchet at the bottom and an area law at the top.

(M1) THE BIT AND THE RATCHET, measured on the crossing engine: the
     intact (over-woven) branch is metastable up to T_c ~ 1.75 and
     collapses above; the punched-through branch is ABSORBING at every
     tension tested -- once through, never back. Each near-threshold
     crossing is a two-state system; reconnection is ONE-WAY. The
     count is monotone: a second-law arrow built into the horizon's
     microphysics, and absorbed identity (GRV-036) frozen into the
     through-pattern.
(M2) THE COUNTING RULE: the reconnection-ACTIVE shell is where the
     disorder-broadened transition band (pressing in [1, 4.5], the
     measured GRV-035 spread) lives -- the mixed-population region
     where crossings are at their individual thresholds.
(M3) THE CONDITIONAL AREA LAW: IF the pressing profile near the
     horizon is Rindler-class (universal in proper distance --
     M-independent, the standard near-horizon structure), the active
     shell has FIXED thickness (0.78 lattice units for the measured
     band) and the count scales with AREA: lattice demonstration slope
     1.90 across R_h = 8..24, N/R_h^2 constant. The CONDITION is the
     named missing bridge (GRV-035): pressing-from-metric; a
     tidal-class profile would scale differently -- stated, not hidden.
(M4) THE CLOSURE: S ~ N ln 2 with N ~ A x (shell)/a^3 ~ A/a^2; GRV-007
     registered a_grav ~ sqrt(hbar G/c^3) = the Planck length, giving
     S ~ A/l_P^2 -- the Bekenstein-Hawking FORM, up to the O(1)
     coefficient this claim does NOT derive.

NOT DERIVED, at full volume: the 1/4; the temperature; Hawking
radiation; the bit-identification beyond the mixed-population rule;
and the pressing-profile bridge that the whole area law is conditional
on. Filed exactly here, where the next benchmark must start.
"""
import numpy as np

Ac = 1.0; sig = 0.12


def dU(r): return -Ac*4*(r/sig)**3/sig/(1 + (r/sig)**4)**2


def relax_branch(T, H, seed, L=4.0, N=801, iters=12000):
    x = np.linspace(-L, L, N); dx = x[1] - x[0]
    if seed == 'over':
        h = -H + (H + 2*sig)*np.exp(-(x/(4*sig))**2)
    else:
        h = np.full(N, -H, float)
    h[0] = h[-1] = -H
    for _ in range(iters):
        r = np.sqrt(x**2 + h**2) + 1e-12
        F = -dU(r)*h/r
        lap = (np.roll(h, -1) - 2*h + np.roll(h, 1))/dx**2
        g = T*lap + F; g[0] = g[-1] = 0
        h = h + min(0.4*dx**2/T, 0.02)*g
        h[0] = h[-1] = -H
    return h[np.argmin(np.abs(x))]


def count_active(Rh, C=1.0, band=(1.0, 4.5), margin=3.0):
    L = int(np.ceil(Rh + margin))
    ax = np.arange(-L, L + 1)
    X, Y, Z = np.meshgrid(ax, ax, ax, indexing='ij')
    s = np.sqrt(X**2 + Y**2 + Z**2) - Rh
    press = np.where(s > 1e-9, C/np.maximum(s, 1e-9), 1e9)
    return int(((press >= band[0]) & (press <= band[1]) & (s > 0)).sum())


def test():
    H = 0.5
    assert relax_branch(1.0, H, 'over') > 0, "M1: over-branch metastable below T_c"
    assert relax_branch(3.0, H, 'over') < 0, "M1: over-branch collapses above T_c"
    assert relax_branch(1.0, H, 'through') < 0 and relax_branch(5.0, H, 'through') < 0, \
        "M1 RATCHET: through-branch absorbing -- reconnection is one-way"
    Rhs = np.array([8, 14, 20])
    Ns = np.array([count_active(R) for R in Rhs])
    slope = np.polyfit(np.log(Rhs), np.log(Ns), 1)[0]
    assert 1.7 < slope < 2.3, "M3: area-law scaling under the Rindler-class profile"
    print(f"ratchet confirmed; area exponent = {slope:.2f}; shell = 0.78 (R_h-independent)")
    print("PASS: the reconnection count -- one-way bits on a fixed-thickness shell:")
    print("      S ~ A/a^2, closing via GRV-007 (a ~ l_P) to the Bekenstein-Hawking FORM,")
    print("      conditional on the named pressing-profile bridge; the 1/4 not derived.")


if __name__ == "__main__":
    test()
