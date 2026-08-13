"""COMMISSION TAV2 -- bundle-bundle contact scaling on the strand engine.

Executed under analysis/TAV2_bundle_contact_bars_LOCKED.md. All
conventions (gap values, touching convention, sweep, bands) fixed at
lock. Contact form: the FND-STRAND-004 registered finite form
Ac/(1 + (r/sigma)^4), Ac = 1, sigma = 0.12.
"""
import numpy as np

SIG = 0.12
AC = 1.0
G_HEX = 0.050 * SIG
G_FC = 0.799 * SIG
PITCH = lambda g: SIG + g  # centerline pitch = 2 r_s + gap, r_s = sigma/2

def f(r):
    return AC / (1.0 + (r / SIG) ** 4)

def hex_bundle(n, pitch):
    """First n sites of a hex spiral (centered), scaled by pitch."""
    pts = [(0.0, 0.0)]
    ring = 1
    while len(pts) < n:
        # ring of 6*ring sites
        for k in range(6 * ring):
            side, step = divmod(k, ring)
            ang0 = np.pi / 3 * side
            ang1 = np.pi / 3 * (side + 1)
            p0 = ring * np.array([np.cos(ang0), np.sin(ang0)])
            p1 = ring * np.array([np.cos(ang1), np.sin(ang1)])
            pts.append(tuple(p0 + (p1 - p0) * step / ring))
            if len(pts) == n:
                break
        ring += 1
    return np.array(pts[:n]) * pitch

def e_lat(n, gap):
    """Lateral contact: two parallel bundles, surface gap = gap.
    Energy per unit length = sum over cross pairs f(d_ij)."""
    p = PITCH(gap)
    b = hex_bundle(n, p)
    R = b[:, 0].max() - b[:, 0].min()
    # place second bundle to the right; nearest centerline pair at pitch(gap)
    shift = b[:, 0].max() - b[:, 0].min() + PITCH(gap)
    b2 = b.copy()
    b2[:, 0] += b[:, 0].max() - b[:, 0].min() + PITCH(gap) - (b[:, 0].max() - b[:, 0].min())
    # cleaner: min cross-pair centerline distance == PITCH(gap)
    b2 = b + np.array([0.0, 0.0])
    dx0 = b[:, 0].max() - b[:, 0].min()
    b2 = b.copy(); b2[:, 0] += dx0 + PITCH(gap)
    d = np.sqrt(((b[:, None, :] - b2[None, :, :]) ** 2).sum(-1))
    return f(d).sum()

def e_ax(n, gap):
    """Axial contact: facing cross sections at end-plane gap = gap
    (end-to-end nearest distance = PITCH(gap) for aligned pairs)."""
    p = PITCH(gap)
    b = hex_bundle(n, p)
    z = PITCH(gap)
    d = np.sqrt(((b[:, None, :] - b[None, :, :]) ** 2).sum(-1) + z * z)
    return f(d).sum()

def e1(gap, geom):
    d = PITCH(gap)
    return f(d)

def sweep(geom, gap):
    ns = [5, 7, 9, 19, 37, 45, 61, 63, 73, 81, 91]
    E = []
    for n in ns:
        E.append((e_lat if geom == "LAT" else e_ax)(n, gap))
    return np.array(ns), np.array(E)

def fit_p(ns, E):
    x, y = np.log(ns), np.log(E)
    p = np.polyfit(x, y, 1)[0]
    h = len(ns) // 2
    plo = np.polyfit(x[:h + 1], y[:h + 1], 1)[0]
    phi = np.polyfit(x[h:], y[h:], 1)[0]
    return p, plo, phi, abs(plo - phi) <= 0.1

def classify(p):
    if 0.85 <= p <= 1.15: return "FULL-SECTION"
    if 0.40 <= p <= 0.60: return "LINE"
    if 0.61 <= p <= 0.84: return "PATCH"
    return "UNCLASSIFIED"

def main():
    print("TAV2 -- bundle-bundle contact scaling (locked bars)")
    results = {}
    for geom in ("LAT", "AX"):
        for name, gap in (("hex", G_HEX), ("f_c", G_FC)):
            ns, E = sweep(geom, gap)
            meff = E / e1(gap, geom)
            p, plo, phi, stable = fit_p(ns, E)
            cls = classify(p) if stable else "UNSTABLE"
            results[(geom, name)] = (ns, meff, p, cls)
            print(f"\nG-{geom} / {name}: p = {p:.3f} "
                  f"(halves {plo:.3f}/{phi:.3f}, stable={stable}) -> {cls}")
            for n, m in zip(ns, meff):
                print(f"  n = {n:3d}: m_eff = {m:9.3f}")
    # readout against the MEM pin, per bars
    PIN = (63.0, 73.4)
    print("\n-- n_b readout: {n : m_eff(n) in [63.0, 73.4]} --")
    for key, (ns, meff, p, cls) in results.items():
        sel = [int(n) for n, m in zip(ns, meff) if PIN[0] <= m <= PIN[1]]
        print(f"G-{key[0]}/{key[1]} ({cls}): {sel if sel else 'EMPTY at sampled n'}")
        # interpolated crossing for full-section geometries
        if cls == "FULL-SECTION":
            lo = np.interp(PIN[0], meff, ns)
            hi = np.interp(PIN[1], meff, ns)
            print(f"   interpolated n window for pin: [{lo:.1f}, {hi:.1f}]")

if __name__ == "__main__":
    main()
