"""FND-STRAND-007 (Modeled): THE WEAVE AS RESERVOIR -- the bath derived.
The last generic ingredient in the measurement chain (the thermal noise
of FND-STRAND-006) is replaced by strand degrees of freedom: the detector
chain is coupled to weave modes (harmonic twist oscillators per site,
Ohmic-like frequency spread, Caldeira-Leggett form with counter-term),
and the ENTIRE COMPOSITE EVOLVES DETERMINISTICALLY -- symplectic,
energy-conserving, no injected noise anywhere. The only stochastic
element is the weave's THERMAL INITIAL CONDITIONS.

(B1) THE DOT SURVIVES THE DERIVATION: under deterministic composite
     dynamics, below threshold the detector is silent; above, a
     localized kink-pair nucleates and the winding advances irreversibly
     -- all three signatures, with friction and noise EMERGENT from the
     weave rather than postulated.
(B2) FLUCTUATION-DISSIPATION IN ACTION: before firing, the detector
     field equilibrates toward the weave's temperature (kinetic
     equipartition within the band), and total composite energy is
     conserved to a small relative drift (symplectic integration).
(B3) THE CHANNEL STILL DRIVES: escape times are monotone decreasing in
     the tilt across the sweep.

HONEST SCOPE: weave modes are harmonic stand-ins for the true strand
spectrum; the thermal initial condition is assumed ('the weave is warm'
-- an environmental boundary condition, not a dynamical law). The
measurement chain is now strand-native at every dynamical step; the one
remaining assumption is a temperature.
"""
import numpy as np


def run_weave(h, T=0.4, w=0.8, N=96, K=24, tmax=160000, dt=0.02, seed=0,
              want_profile=False):
    r = np.random.default_rng(seed)
    kt = w*w
    phi = np.zeros(N); pphi = np.zeros(N)
    om = np.linspace(0.3, 3.0, K)
    c = 0.35*om*np.sqrt(2/np.pi/K)
    q = r.standard_normal((N, K))*np.sqrt(T)/om
    p = r.standard_normal((N, K))*np.sqrt(T)

    def forces():
        lap = np.roll(phi, -1) - 2*phi + np.roll(phi, 1)
        Fphi = kt*lap - np.sin(phi) + h + np.sum(c*(q - c*phi[:, None]/om**2), axis=1)
        Fq = -om**2*(q - c*phi[:, None]/om**2)
        return Fphi, Fq

    def energy():
        d = np.roll(phi, -1) - phi
        E = 0.5*np.sum(pphi**2) + 0.5*kt*np.sum(d**2) + np.sum(1 - np.cos(phi)) - h*np.sum(phi)
        E += 0.5*np.sum(p**2) + 0.5*np.sum(om**2*(q - c*phi[:, None]/om**2)**2)
        return E
    E0 = energy(); esc = None; kin = []; prof = None; irrev = False
    for step in range(tmax):
        Fphi, Fq = forces()
        pphi += 0.5*dt*Fphi; p += 0.5*dt*Fq
        phi += dt*pphi; q += dt*p
        Fphi, Fq = forces()
        pphi += 0.5*dt*Fphi; p += 0.5*dt*Fq
        if step % 50 == 0:
            m = np.mean(phi)
            if esc is None and step > 2000:
                kin.append(np.mean(pphi**2))
            if esc is None and m > np.pi:
                esc = step*dt; prof = phi.copy()
            if esc is not None and m > 2*np.pi:
                irrev = True
                break
    drift = abs(energy() - E0)/abs(E0)
    out = {'esc': esc if esc is not None else np.inf,
           'kin': float(np.mean(kin)) if kin else np.nan,
           'drift': float(drift), 'irrev': irrev}
    if want_profile:
        out['prof'] = prof
    return out


def test():
    # B1 + B2: below threshold -- silent, equilibrated, energy conserved
    sub = run_weave(0.30, seed=1)
    assert not np.isfinite(sub['esc']), "below threshold: the deterministic composite is silent"
    assert 0.25 < sub['kin'] < 0.55, "kinetic equipartition toward the weave temperature"
    assert sub['drift'] < 0.02, "total composite energy conserved (no hidden thermostat)"
    # B1 above: localized, irreversible
    hi = run_weave(0.65, seed=1, want_profile=True)
    assert np.isfinite(hi['esc']) and hi['irrev'], "the dot fires and never un-fires"
    g = np.abs(np.diff(hi['prof']))
    assert g.max() > 4*np.median(g + 1e-9), "localized kink-pair at escape"
    # B3: monotone drive
    ts = []
    for h in (0.55, 0.65, 0.75):
        es = [run_weave(h, seed=s)['esc'] for s in (1, 2)]
        es = [e for e in es if np.isfinite(e)]
        assert es, "escapes at each drive"
        ts.append(np.mean(es))
    assert ts[0] > ts[1] > ts[2], "stronger channel, faster dot -- under the derived bath"
    print(f"B1: silent below; above: localized pair at t = {hi['esc']:.0f}, irreversible")
    print(f"B2: pre-escape <p^2> = {sub['kin']:.3f} (T = 0.4); energy drift {sub['drift']:.2e}")
    print(f"B3: escape times {['%.0f' % t for t in ts]} monotone in the channel")
    print("PASS: friction and noise EMERGE from weave strand modes under deterministic,")
    print("      energy-conserving dynamics -- the bath is derived; what remains is a temperature.")


if __name__ == "__main__":
    test()
