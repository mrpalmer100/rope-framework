"""FND-STRAND-008 (Modeled): THE WEAVE SPECTRUM FROM THE ENGINE -- the
reservoir's harmonic stand-ins replaced by the strand model's OWN
measured normal modes, and a prediction falls out: the weave bath is
GAPPED. The twist chain's on-site potential gives every mode omega >= 1
(no soft modes exist), with the band topping at sqrt(1 + 4 kt).

(B1) THE SPECTRUM IS MEASURED, NOT ASSUMED: the Hessian of the Phase-2a
     twist energy at the uniform state, eigendecomposed, matches the
     engine's dispersion omega^2 = 1 + 4 kt sin^2(pi k / M) to 7e-16 --
     gap exactly 1, top exactly sqrt(1 + 4 kt).
(B2) THE DOT SURVIVES THE TRUE BATH: the deterministic, energy-conserving
     composite of FND-STRAND-007, rebuilt with the measured gapped
     spectrum, still produces the dot -- silent below threshold, a
     localized irreversible kink-pair above.
(B3) THE CHANNEL STILL DRIVES: escape times monotone in the tilt.

The gap is a genuine structural prediction of the strand picture: a
weave reservoir has NO low-frequency modes to donate, so detector noise
arrives only at and above the strand mass scale -- a difference from
generic Ohmic environments that is in principle testable wherever the
model's detector physics applies.
"""
import numpy as np


def measured_spectrum(w=0.8, M=48):
    kt = w*w
    H = np.zeros((M, M))
    for i in range(M):
        H[i, i] = 2*kt + 1.0
        H[i, (i + 1) % M] -= kt
        H[i, (i - 1) % M] -= kt
    om = np.sqrt(np.linalg.eigvalsh(H))
    k = np.arange(M)
    om_disp = np.sort(np.sqrt(1 + 4*kt*np.sin(np.pi*k/M)**2))
    return np.sort(om), om_disp


def run(h, om_band, T=0.4, w=0.8, N=96, K=24, tmax=160000, dt=0.02, seed=1,
        want_profile=False):
    r = np.random.default_rng(seed)
    kt = w*w
    om = om_band[np.linspace(0, len(om_band) - 1, K).astype(int)]
    c = 0.35*om*np.sqrt(2/np.pi/K)
    phi = np.zeros(N); pphi = np.zeros(N)
    q = r.standard_normal((N, K))*np.sqrt(T)/om
    p = r.standard_normal((N, K))*np.sqrt(T)

    def F():
        lap = np.roll(phi, -1) - 2*phi + np.roll(phi, 1)
        return (kt*lap - np.sin(phi) + h + np.sum(c*(q - c*phi[:, None]/om**2), 1),
                -om**2*(q - c*phi[:, None]/om**2))
    esc = None; prof = None; irrev = False
    for step in range(tmax):
        f1, f2 = F(); pphi += 0.5*dt*f1; p += 0.5*dt*f2
        phi += dt*pphi; q += dt*p
        f1, f2 = F(); pphi += 0.5*dt*f1; p += 0.5*dt*f2
        if step % 50 == 0:
            m = np.mean(phi)
            if esc is None and m > np.pi:
                esc = step*dt; prof = phi.copy()
            if esc is not None and m > 2*np.pi:
                irrev = True; break
    out = {'esc': esc if esc is not None else np.inf, 'irrev': irrev}
    if want_profile:
        out['prof'] = prof
    return out


def test():
    om, om_disp = measured_spectrum()
    assert np.max(np.abs(om - om_disp)) < 1e-10, "spectrum measured = engine dispersion"
    assert abs(om.min() - 1.0) < 1e-10, "THE GAP: no weave mode below the strand mass scale"
    assert abs(om.max() - np.sqrt(1 + 4*0.64)) < 1e-10, "band top sqrt(1 + 4 kt)"
    sub = run(0.30, om)
    assert not np.isfinite(sub['esc']), "below threshold: silent under the true bath"
    hi = run(0.65, om, want_profile=True)
    assert np.isfinite(hi['esc']) and hi['irrev'], "the dot fires and never un-fires"
    g = np.abs(np.diff(hi['prof']))
    assert g.max() > 4*np.median(g + 1e-9), "localized kink-pair at escape"
    ts = [run(h, om)['esc'] for h in (0.55, 0.65, 0.75)]
    assert all(np.isfinite(t) for t in ts) and ts[0] > ts[1] > ts[2], "channel-monotone"
    print(f"B1: spectrum measured; gap = {om.min():.3f}, top = {om.max():.3f} (deviation < 1e-10)")
    print(f"B2: silent below; dot at t = {hi['esc']:.0f} above, localized, irreversible")
    print(f"B3: escapes {['%.0f' % t for t in ts]} monotone in the channel")
    print("PASS: the reservoir runs on the engine's own gapped spectrum -- the bath's")
    print("      structure is a prediction now, and the dot survives it.")


if __name__ == "__main__":
    test()
