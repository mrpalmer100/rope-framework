"""GRV-079: nonlinear settling. The exhaustion-softened wave equation on the
Schwarzschild-class background: sub-exhaustion disturbances ring down; an
exhaustion-crossing disturbance grows a floored core whose EXTERIOR still empties.
Bars locked in analysis/GRV079_nonlinear_settling_bars_LOCKED.md.
"""
import numpy as np

RS = 1.0
F_FLOOR = 0.01


def background(N=3000, r0=1.5, r1=40.0):
    r = np.linspace(r0, r1, N)
    alpha = np.sqrt(1 - RS / r)
    B = 1.0 / alpha
    return r, B / alpha, alpha * B         # r, mu, T


def run(amp, e_x, steps=90000, width=0.8, r_c=8.0):
    r, mu, T0 = background()
    N = len(r); dr = r[1] - r[0]; dt = 0.30 * dr
    u = amp * np.exp(-((r - r_c) / width) ** 2)
    v = np.zeros_like(u)
    c_in = np.sqrt(T0[0] / mu[0]); c_out = np.sqrt(T0[-1] / mu[-1])
    shell = (r > 2.0) & (r < 20.0)
    hit = np.zeros(N, dtype=bool)
    Es, vmax_run, ratio_peak = [], 0.0, 0.0
    kern = np.ones(9) / 9.0
    for n in range(steps):
        ux = np.gradient(u, dr)
        e_loc = 0.5 * (mu * v ** 2 + T0 * ux ** 2)
        e_s = np.convolve(e_loc, kern, mode="same")
        ratio_peak = max(ratio_peak, float((e_s / e_x).max()))
        soft = np.maximum(1.0 - e_s / e_x, F_FLOOR)
        hit |= soft <= F_FLOOR + 1e-12
        Teff = T0 * soft
        Tm = 0.5 * (Teff[1:] + Teff[:-1])
        flux = Tm * np.diff(u) / dr
        acc = np.zeros_like(u)
        acc[1:-1] = (flux[1:] - flux[:-1]) / (dr * mu[1:-1])
        v += dt * acc
        # Exhausted cells act as a dynamically formed INNER BOUNDARY: energy
        # entering them leaves the exterior problem (GRV-078's horizon-side
        # mechanism, applied to the region that has exhausted). Implemented as
        # absorption in floored cells; an in-session amendment to the model
        # commitment, disclosed in the claim (without it the floored toy TRAPS
        # energy at crawl speed and the runaway floors the whole domain --
        # observed, reported).
        floored = soft <= F_FLOOR + 1e-12
        v[floored] *= (1.0 - dt)
        v[-1] = -c_out * (u[-1] - u[-2]) / dr
        v[0] = c_in * (u[1] - u[0]) / dr
        u += dt * v
        vmax_run = max(vmax_run, float(np.abs(v).max()))
        if n % 500 == 0:
            Es.append(float(np.sum(e_loc[shell]) * dr))
    Es = np.array(Es)
    outer = (r > 12.0) & (r < 30.0)
    ux = np.gradient(u, dr)
    e_end = 0.5 * (mu * v ** 2 + T0 * ux ** 2)
    return dict(ratio=ratio_peak, decay=Es.max() / max(Es[-3:].mean(), 1e-300),
                vfin=float(np.abs(v).max()) / max(vmax_run, 1e-300),
                hit_frac=float(hit.mean()), hit_span=(r[hit][0], r[hit][-1]) if hit.any() else None,
                outer_final=float(np.sum(e_end[outer]) * dr))


def main():
    E_X = 0.02
    # B1: instrument check -- weak amplitude with nonlinearity ON
    w = run(amp=1e-3, e_x=E_X)
    print(f"B1       weak limit (peak e/e_x = {w['ratio']:.1e}): decay "
          f"{w['decay']:.1e}, residual motion {w['vfin']:.1e}")
    assert w['ratio'] < 0.01 and w['decay'] > 1e3
    print("B1 PASS  the nonlinear instrument reproduces GRV-078's relaxation in")
    print("         the weak limit (rule R1).")
    # B2: sub-exhaustion sweep
    print("B2       sub-exhaustion sweep (settled = decay > 100x AND residual")
    print("         motion < 1e-3, rule R3):")
    for amp in (0.02, 0.05, 0.08):
        s = run(amp=amp, e_x=E_X)
        print(f"           amp {amp:.2f}: peak e/e_x = {s['ratio']:.2f}, decay "
              f"{s['decay']:.1e}, residual {s['vfin']:.1e}, floored: "
              f"{s['hit_frac']:.1%}")
        assert s['ratio'] < 1.0 and s['decay'] > 100 and s['vfin'] < 1e-3
        assert s['hit_frac'] == 0.0
    print("B2 PASS  every sub-exhaustion disturbance SETTLES: P1'' holds in the")
    print("         reachable sub-exhaustion regime.")
    # B3: the crossing -- adjudicated per rule R5 (failures register at full
    # strength as bounds on P1'', not reframed).
    c = run(amp=0.12, e_x=E_X)
    print(f"B3       crossing run (amp 0.12): peak e/e_x = {c['ratio']:.1f};")
    print(f"         cumulative exhausted footprint {c['hit_frac']:.0%}; shell")
    print(f"         decay {c['decay']:.1f}x; residual motion {c['vfin']:.2f}")
    assert c['ratio'] > 1.0
    settled = (c['decay'] > 100) and (c['vfin'] < 1e-3)
    assert not settled
    print("B3 REGISTERED NEGATIVE (rule R5): the exhaustion-crossing disturbance")
    print("         DOES NOT SETTLE in this instrument, under either closure")
    print("         tried in-session: (i) the bare floor TRAPS energy at crawl")
    print("         speed and the flooring runs away across the domain; (ii) the")
    print("         sink amendment (exhausted cells as a dynamically formed inner")
    print("         boundary, GRV-078's mechanism) arrests the runaway's energy")
    print("         but leaves a spatially extended, non-settling configuration.")
    print("         In 1D a traveling pulse does not spread, so any super-")
    print("         exhaustion pulse carries its whole density across the domain")
    print("         -- the toy's crossing regime is OUTSIDE the linear-ramp")
    print("         stand-in's competence, and tonight says so instead of tuning")
    print("         until it settles.")
    print("B4       VERDICT: P1'' DISCHARGED-SUB-EXHAUSTION ONLY -- every")
    print("         disturbance with peak load below the exhaustion scale settles")
    print("         to the static exterior (decays 2e7-1e20 across the sweep);")
    print("         the CROSSING regime is registered OPEN at full strength: the")
    print("         collapse-flavored dynamics needs a real interior model, not a")
    print("         softening ramp, and the 1D non-spreading pathology is named")
    print("         as an instrument limit (a 3D pulse dilutes geometrically; the")
    print("         crossing question re-poses there). The horizon chain's")
    print("         residues: (P2') the O(1) crossing geometry, and now the")
    print("         explicitly-located frontier -- exhaustion-crossing dynamics.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
