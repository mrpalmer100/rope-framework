"""Current as transported linking: the no-wind-up, continuity, and closed-loop
conditions are one and the same. (Maxwell paper section 6.1.)

A current is the transport of linking density rho along a conductor, with
flux J = rho*v and local balance d(rho)/dt = -dJ/dx (continuity). This
benchmark demonstrates, by direct simulation, that three statements coincide:

  (i)   open circuit (wraps injected with no return path) -> the local linking
        (twist) density accumulates without bound -- unphysical wind-up;
  (ii)  a steady state exists iff net inflow over the domain is zero, i.e.
        integral of div J = 0 -- the continuity equation in steady state;
  (iii) a closed loop with a balanced pump/return (a battery) sustains a
        genuine nonzero circulating current with BOUNDED local twist.

This REPRODUCES charge conservation (FND-008: conservation of linking under
continuous deformation) as a mechanical picture; it makes no prediction beyond
standard circuit theory. Its role is to show the mechanical interpretation in
section 6.1 is self-consistent and would fail visibly if it were not.
Registered as EM-008.
"""
import numpy as np


def _step_periodic(rho, v, dx, dt, src_nodes):
    """One upwind advection step on a periodic (looped) wire with sources.
    src_nodes: dict {node: rate} (positive = pump in, negative = remove)."""
    flux = v * rho
    drho = -(flux - np.roll(flux, 1)) / dx
    for node, rate in src_nodes.items():
        drho[node] += rate / dx
    rho = rho + dt * drho
    rho[rho < 0] = 0.0
    return rho


def open_circuit_accumulates(N=100, steps=400, seed=0):
    """Blocked-end wire: wraps pumped in at node 0, no outflow. Returns total
    linking over time (should grow monotonically = wind-up)."""
    dx = 1.0 / N; v = 1.0; dt = 0.4 * dx / v
    rho = np.zeros(N); src = 1.0; totals = []
    for _ in range(steps):
        flux = v * rho
        flux[-1] = 0.0  # blocked end: no return path
        drho = np.zeros(N)
        drho[1:] -= (flux[1:] - flux[:-1]) / dx
        drho[0] += src / dx
        rho = rho + dt * drho; rho[rho < 0] = 0
        totals.append(rho.sum() * dx)
    return np.array(totals)


def closed_loop_steady(N=120, steps=4000):
    """Balanced pump (node 0) and return sink (node N/2) on a periodic loop.
    Returns (total_linking_series, local_max_series, mean_abs_flux)."""
    dx = 1.0 / N; v = 1.0; dt = 0.4 * dx / v
    rho = np.ones(N) * 1.0; src = 0.5
    totals = []; locmax = []
    for _ in range(steps):
        rho = _step_periodic(rho, v, dx, dt, {0: src, N // 2: -src})
        totals.append(rho.sum() * dx); locmax.append(rho.max())
    mean_flux = float(np.mean(np.abs(v * rho)))
    return np.array(totals), np.array(locmax), mean_flux


def broken_loop_winds_up(N=120, steps=2000):
    """Pump with no return sink: net source > 0 -> unbounded local twist."""
    dx = 1.0 / N; v = 1.0; dt = 0.4 * dx / v
    rho = np.ones(N) * 1.0; src = 0.5; locmax = []
    for _ in range(steps):
        rho = _step_periodic(rho, v, dx, dt, {0: src})
        locmax.append(rho.max())
    return np.array(locmax)


def test():
    # (i) open circuit accumulates without bound
    tot = open_circuit_accumulates()
    assert tot[-1] > tot[len(tot)//2] > tot[len(tot)//4] > 0, "open circuit should wind up"

    # (iii) closed balanced loop: bounded local twist + genuine nonzero current
    totals, locmax, mean_flux = closed_loop_steady()
    assert abs(totals[-1] - totals[len(totals)//2]) < 1e-3, "total linking must be conserved"
    assert locmax[-1] < 10 * locmax[len(locmax)//8], "local twist must stay bounded"
    assert mean_flux > 0.1, "a genuine circulating current must be present"

    # (ii) the dividing condition: removing the return sink -> wind-up
    lm = broken_loop_winds_up()
    assert lm[-1] > lm[len(lm)//2] > lm[len(lm)//4], "broken loop should wind up"

    print(f"open circuit: total linking grows {tot[0]:.2f} -> {tot[-1]:.2f} (wind-up)")
    print(f"closed loop: total conserved ~{totals[-1]:.3f}, local twist bounded "
          f"({locmax[len(locmax)//8]:.2f} -> {locmax[-1]:.2f}), mean|J|={mean_flux:.3f} (real current)")
    print(f"broken loop: local twist grows {lm[len(lm)//4]:.2f} -> {lm[-1]:.2f} (wind-up)")
    print("PASS: no-wind-up = continuity (div J=0) = closed-loop are one condition.")


if __name__ == "__main__":
    test()
