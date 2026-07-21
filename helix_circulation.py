"""The dynamical drive: a switched-on current evolves into the circulating
Ampere field and propagates at c.  (Maxwell paper section 6.4 / Tier-3.)

This is the 'movie' the magnetism sector previously lacked: not just that the
static circulating pattern MUST hold (topology, EM-009 type-and-sign), but that
the field-equation DYNAMICALLY evolves a current that switches on into that
pattern, at finite propagation speed.

The equation of motion is the Euler-Lagrange equation of
    L = (mu/2)|da/dt|^2 - (K/2)|curl a|^2 + J.a
namely
    mu d^2 a/dt^2 = -K curl(curl a) + J.
Two of the three terms are on firm ground: the stiffness (K/2)|curl a|^2 is
EM-007 (K linear in rope density), and the current coupling J.a is FORCED by
gauge invariance together with current conservation div J = 0 (EM-008): a
conserved current admits only the minimal gauge-invariant coupling integral J.a
(verified here: the coupling is invariant under a -> a + grad chi iff div J = 0).
The one remaining ASSUMPTION is the kinetic term form (mu/2)|da/dt|^2 -- standard
inertial dynamics with mu the rope mass density (which fixes c = sqrt(K/mu)); its
form is not derived from strand-level kinetics. Hence status Modeled, not Derived.

This benchmark verifies: (1) the coupling J.a is gauge invariant given div J=0;
(2) the EOM evolves a switched-on line current into an azimuthal field with a
~1/r profile (Ampere) that is a genuine curl (radial component negligible); and
(3) the disturbance propagates outward at finite speed of order c, not instantly.
Registered as EM-010 (Modeled).
"""
import numpy as np


def _lap(f, dx):
    return (np.roll(f, 1, 0) + np.roll(f, -1, 0)
            + np.roll(f, 1, 1) + np.roll(f, -1, 1) - 4 * f) / dx**2


def gauge_invariance_of_coupling(N=60, seed=0):
    """Build a divergence-free current J (as curl of a scalar) and confirm the
    coupling integral J.a is invariant under a -> a + grad chi."""
    dx = 1.0 / N
    rng = np.random.default_rng(seed)
    psi = rng.normal(size=(N, N))
    Jx = (np.roll(psi, -1, 1) - np.roll(psi, 1, 1)) / (2 * dx)
    Jy = -(np.roll(psi, -1, 0) - np.roll(psi, 1, 0)) / (2 * dx)
    divJ = ((np.roll(Jx, -1, 0) - np.roll(Jx, 1, 0)) / (2 * dx)
            + (np.roll(Jy, -1, 1) - np.roll(Jy, 1, 1)) / (2 * dx))
    chi = rng.normal(size=(N, N))
    gx = (np.roll(chi, -1, 0) - np.roll(chi, 1, 0)) / (2 * dx)
    gy = (np.roll(chi, -1, 1) - np.roll(chi, 1, 1)) / (2 * dx)
    dcoupling = np.sum(Jx * gx + Jy * gy) * dx * dx
    return float(np.abs(divJ).max()), float(abs(dcoupling))


def evolve_field(N=201, nsteps=120, K=1.0, mu=1.0):
    """Evolve mu a_tt = K lap(a) + J with a smoothly switched-on line current
    at the centre. Return azimuthal/radial profiles and the propagation front."""
    dx = 1.0 / N
    c = np.sqrt(K / mu)
    dt = 0.3 * dx / c
    az = np.zeros((N, N))
    azp = np.zeros((N, N))
    cx = cy = N // 2
    fronts = []
    for step in range(nsteps):
        amp = min(1.0, step / 50.0)
        J = np.zeros((N, N))
        J[cx, cy] = amp
        azn = 2 * az - azp + dt**2 * ((K / mu) * _lap(az, dx) + J / mu)
        azp = az
        az = azn
        if step in (40, 80, nsteps - 1):
            prof = np.abs(az[cx, cx:])
            thr = 0.02 * prof.max() if prof.max() > 0 else 1.0
            reached = np.where(prof > thr)[0]
            front = reached[-1] * dx if len(reached) else 0.0
            fronts.append((step * dt, front))
    Bx = (np.roll(az, -1, 1) - np.roll(az, 1, 1)) / (2 * dx)
    By = -(np.roll(az, -1, 0) - np.roll(az, 1, 0)) / (2 * dx)
    rs = np.array([8, 16, 32, 48])
    azim = np.array([By[cx + r, cy] for r in rs])   # azimuthal on +x axis is +y comp
    radial = np.array([Bx[cx + r, cy] for r in rs])  # radial is +x comp
    return rs, azim, radial, fronts, c


def test():
    # (1) coupling gauge-invariant iff div J = 0
    maxdiv, dcoup = gauge_invariance_of_coupling()
    assert maxdiv < 1e-9, "test current is not divergence-free"
    assert dcoup < 1e-9, "coupling J.a not gauge invariant"

    # (2) field profile: azimuthal ~1/r, curl (radial negligible)
    rs, azim, radial, fronts, c = evolve_field()
    mask = np.abs(azim) > 1e-9
    assert mask.sum() >= 3, "azimuthal field too weak to fit"
    slope = np.polyfit(np.log(rs[mask]), np.log(np.abs(azim[mask])), 1)[0]
    assert abs(slope - (-1.0)) < 0.4, f"azimuthal profile not ~1/r (slope {slope:.2f})"
    ratio = np.mean(np.abs(radial)) / (np.mean(np.abs(azim)) + 1e-12)
    assert ratio < 0.35, f"field not a clean curl (radial/azim {ratio:.2f})"

    # (3) finite propagation of order c
    speeds = [f / t for t, f in fronts if t > 0 and f > 0]
    assert speeds and all(0.5 < s < 1.6 for s in speeds), f"propagation not ~c: {speeds}"

    print(f"coupling gauge-invariant given div J=0: |change|={dcoup:.1e} (PASS)")
    print(f"azimuthal field slope vs r = {slope:.2f} (Ampere -1.0); radial/azim = {ratio:.2f}")
    print(f"propagation speeds (c=1): {[round(s,2) for s in speeds]}")
    print("PASS: EOM dynamically evolves a switched-on current into the")
    print("      propagating Ampere field. Drive derived up to the assumed")
    print("      inertial (kinetic) term; status Modeled.")


if __name__ == "__main__":
    test()
