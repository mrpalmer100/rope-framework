"""FND-STRAND-017 (Failed, kept): THE THEORY SESSION -- the phase-winding
picture KILLED at its own first checkpoint. The amplitude-freezing premise
(T1) failed its pre-committed bar by 9x: the weave is an INTERNALLY MIXING
thermal network, not a bundle of frozen-amplitude oscillators, and per the
locked bars the session stopped there (the pre-registered scramble
experiment was not run after a failed premise).

Bars: analysis/STRAND017_theory_bars_LOCKED.md. Results and the reframing
the failure bought: analysis/STRAND017_theory_results.md -- the exclusion
triangle (temperature flat, drive flat, hazard falling) is what
equilibrium-static AGGREGATES over a mixing MICROSTATE look like, and the
refined candidate is SLOW-MIXING MEMORY: the hazard falls while the bath
still remembers its initial microstate, with tau_mix ~ the hazard-fall
window and a plateau predicted beyond it.

This benchmark re-executes the T1 check and asserts the FAILURE (the kill
is the registered result): among walkers alive at t = 2000, per-mode
energies have reorganized far beyond the 0.10 freezing bar.
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from strand_weave_spectrum import measured_spectrum


def t1_drift(S=16, seed=121, tmax_steps=100000):
    N, h, T, c0, w, K, dt = 24, 0.55, 0.40, 0.35, 0.8, 16, 0.02
    kt = w*w
    om_band, _ = measured_spectrum()
    om = om_band[np.linspace(0, len(om_band) - 1, K).astype(int)]
    c = c0*om*np.sqrt(2/np.pi/K)
    r = np.random.default_rng(seed)
    phi = np.zeros((S, N)); pphi = np.zeros((S, N))
    q = r.standard_normal((S, N, K))*np.sqrt(T)/om
    p = r.standard_normal((S, N, K))*np.sqrt(T)

    def modeE():
        qs = q - c*phi[..., None]/om**2
        return 0.5*p**2 + 0.5*om**2*qs**2

    E0 = modeE()

    def F():
        lap = np.roll(phi, -1, 1) - 2*phi + np.roll(phi, 1, 1)
        return (kt*lap - np.sin(phi) + h
                + np.einsum('k,snk->sn', c, q - c*phi[..., None]/om**2),
                -om**2*(q - c*phi[..., None]/om**2))

    alive = np.ones(S, bool)
    for step in range(tmax_steps):
        f1, f2 = F(); pphi += 0.5*dt*f1; p += 0.5*dt*f2
        phi += dt*pphi; q += dt*p
        f1, f2 = F(); pphi += 0.5*dt*f1; p += 0.5*dt*f2
        if step % 25 == 0:
            alive &= ~(np.mean(phi, 1) > np.pi)
    E1 = modeE()
    drift = np.abs(E1 - E0).sum(axis=(1, 2))/E0.sum(axis=(1, 2))
    return drift, alive


def test():
    drift, alive = t1_drift()
    assert alive.sum() >= 3, "enough survivors at t=2000 for the alive reading"
    med_alive = float(np.median(drift[alive]))
    med_all = float(np.median(drift))
    assert med_alive > 0.10, "the kill: alive-walker drift far beyond the bar"
    assert med_alive > 0.5, f"registered magnitude: ~90% reorganization, got {med_alive:.2f}"
    assert med_all > 0.10, "the committed all-walker statistic also fails"
    print(f"T1 check: alive-walker median mode-energy drift = {med_alive:.2f} "
          f"(bar 0.10) -- FAILED by ~9x; all-walker statistic {med_all:.0f}")
    print("PASS (the registered result IS the failure): the weave is an")
    print("      internally mixing thermal network; the phase-winding theory")
    print("      died at its own checkpoint, and the slow-mixing-memory")
    print("      candidate inherits the brief.")


if __name__ == "__main__":
    test()
