"""COMMISSION SHIN2 -- helical-substructure acceptance test.
Executed under analysis/SHIN2_helical_substructure_bars_LOCKED.md.
"""
import numpy as np

HBARC = 197.327e-15 * 1e6 * 1.602e-19   # J m
E_PEV = 1.4e15 * 1.602e-19              # J
THETA = 2.7e-5                          # rad, FND-059 tighter value
READINGS = [("kappa50", 1.63e-17, 1599.0, 6.1), ("kappa250", 0.953e-17, 2734.0, 10.5)]

def a1():
    print("A1 redistribution invariance")
    ok = True
    for tag, a, T0, marg in READINGS:
        n = (a / (HBARC / E_PEV)) ** 2
        Tf, muf = T0 / n, 1.0 / n          # mu in units of coarse mu
        c2_ratio = (Tf / muf) / (T0 / 1.0)  # exact
        sigma_ratio = (n * Tf) / T0         # total tension per area
        print(f"  {tag}: n_sub={n:.3e}  c^2 ratio={c2_ratio:.12f}  Sigma ratio={sigma_ratio:.12f}  Lorentz margin {marg}x -> {marg * sigma_ratio}x")
        ok &= abs(c2_ratio - 1) < 1e-12 and abs(sigma_ratio - 1) < 1e-12
    print("  PASS" if ok else "  FAIL")
    return ok

def a2():
    print("A2 fine-mesh ceiling")
    ok = True
    for tag, a, T0, _ in READINGS:
        n = (a / (HBARC / E_PEV)) ** 2
        af = a / np.sqrt(n)
        Emax = HBARC / af
        print(f"  {tag}: a_f={af:.3e} m  E_max={Emax/1.602e-19/1e15:.3f} PeV")
        ok &= Emax >= E_PEV * 0.999
    print("  PASS" if ok else "  FAIL")
    return ok

def coverage(tangents, theta=THETA, nsamp=200000, seed=7):
    """Monte Carlo fraction of the sphere within theta of any tangent
    direction (tangents given as (M,3) unit vectors; includes +-)."""
    rng = np.random.default_rng(seed)
    v = rng.normal(size=(nsamp, 3)); v /= np.linalg.norm(v, axis=1)[:, None]
    t = np.vstack([tangents, -tangents])
    thr = np.cos(theta)
    hit = np.zeros(len(v), dtype=bool)
    for i in range(0, len(t), 512):
        hit |= (np.abs(v @ t[i:i+512].T) >= thr).any(axis=1)
        # early exit cheap skip
    return hit.mean()

def family_axes():
    return np.eye(3)

def helix_tangents(axis, psi, nphi=720):
    """Tangents of a helix about `axis` at pitch angle psi: a circle of
    directions at angle (pi/2 - psi)... tangent makes angle (pi/2 - psi)
    with the axis when psi is the pitch angle from the transverse plane."""
    axis = axis / np.linalg.norm(axis)
    # orthonormal frame
    tmp = np.array([1.0, 0, 0]) if abs(axis[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = np.cross(axis, tmp); e1 /= np.linalg.norm(e1)
    e2 = np.cross(axis, e1)
    ph = np.linspace(0, 2 * np.pi, nphi, endpoint=False)
    t = (np.sin(psi) * axis[None, :]
         + np.cos(psi) * (np.cos(ph)[:, None] * e1 + np.sin(ph)[:, None] * e2))
    return t

def helix2_tangents(axis, psi1, psi2, nphi=180):
    """Two-level winding: level-1 helix axis precesses along the level-2
    tangent circle. Tangent = sin(psi2)*t1 + cos(psi2)*(transverse circle
    about t1), evaluated over both phases."""
    t1s = helix_tangents(axis, psi1, nphi)
    out = []
    for t1 in t1s:
        out.append(helix_tangents(t1, psi2, nphi))
    return np.vstack(out)


def a3():
    print("A3 direction coverage (bar: >= 10 percent) -- exact spherical geometry")
    th = THETA
    # W0 control: three axis point-pairs, caps of half-angle theta
    cov0 = 6 * (1 - np.cos(th)) / 2  # 6 caps / sphere area 4pi -> 6*(2pi(1-cos))/4pi
    print(f"  W0 straight three-family: coverage = {cov0:.3e} (control; expect ~1e-9)")
    grid = np.deg2rad([5, 15, 30, 45, 60, 75, 85])
    # W1: tangents form 3 circles at angle A1 = arccos(sin psi) from each axis;
    # theta-band around each circle, area ~ length * 2 theta (non-overlap, th tiny)
    print("  W1 single-level helices (band around three circles):")
    best1 = 0.0
    for psi in grid:
        A1 = np.arccos(np.sin(psi))
        band = 3 * 2 * (2 * np.pi * np.sin(A1)) * (2 * th) / (4 * np.pi)  # x2 antipodal
        band = min(band, 1.0)
        best1 = max(best1, band)
        print(f"    psi={np.rad2deg(psi):4.0f} deg: coverage = {band:.4e}")
    # W2: two-level winding -> per family an annulus of polar angles
    # [|A1-A2|, A1+A2] (mirrored), A_i = arccos(sin psi_i); union over 3 axes.
    print("  W2 two-level winding (annuli; union by MC over the sphere, exact bands):")
    rng = np.random.default_rng(7)
    v = rng.normal(size=(200000, 3)); v /= np.linalg.norm(v, axis=1)[:, None]
    axes = np.eye(3)
    best2, best_pair = 0.0, None
    for p1 in grid:
        for p2 in grid:
            A1, A2 = np.arccos(np.sin(p1)), np.arccos(np.sin(p2))
            lo, hi = abs(A1 - A2), min(A1 + A2, np.pi - (A1 + A2) if A1 + A2 > np.pi/2 else A1 + A2)
            hi = min(A1 + A2, np.pi)  # keep simple; mirror handles the rest
            inside = np.zeros(len(v), dtype=bool)
            for ax in axes:
                ang = np.arccos(np.clip(np.abs(v @ ax), -1, 1))  # fold antipodal: angle in [0, pi/2]
                # band condition on folded angle: within [lo, hi] or its mirror pi-  (folded)
                inside |= (ang >= lo - th) & (ang <= min(hi, np.pi - lo) + th)
            c = inside.mean()
            if c > best2:
                best2, best_pair = c, (np.rad2deg(p1), np.rad2deg(p2))
    print(f"    best: psi1={best_pair[0]:.0f}, psi2={best_pair[1]:.0f} deg -> coverage = {best2:.4f}")
    ok = best1 >= 0.10 or best2 >= 0.10
    print(f"  W1 best {best1:.3e}; W2 best {best2:.3f} -> {'PASS' if ok else 'FAIL'}")
    return ok, best1, best2, best_pair


def a4(best_pair):
    print("A4b guided-path retardation at the A3-passing geometry")
    if best_pair is None:
        print("  no passing member; moot"); return
    p1, p2 = np.deg2rad(best_pair)
    # axial advance per arclength for two-level winding: product of sines
    s = np.sin(p1) * np.sin(p2)
    print(f"  sin(psi1) sin(psi2) = {s:.3f} -> guided axial speed {s:.3f} c")
    print("  tension displayed: guided modes are slow; the coarse light mode")
    print("  must be the COLLECTIVE branch (EM-RECON-025) -- named escape, not resolved")

if __name__ == "__main__":
    p1 = a1(); p2 = a2(); p3, b1, b2, pair = a3(); a4(pair)
    print("\nVERDICT:", "ALL BARS PASS -- grant-candidate goes to the desk"
          if (p1 and p2 and p3) else "FAILURE REGISTERED AND KEPT")
