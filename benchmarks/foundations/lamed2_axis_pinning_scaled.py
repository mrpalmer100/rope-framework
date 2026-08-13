#!/usr/bin/env python3
"""COMMISSION LAMED-2 -- the axis-pinning experiment, scaled.

Bars: analysis/LAMED2_axis_pinning_scaled_bars_LOCKED.md.
Reviewer's protocol, run at tractable s = r0/a with extrapolation in s
(NOT in a -- a is physical, see the bars).

THE PROXY (stated in full, per the bar): the core's anisotropy is
ELEC-091's structure -- azimuthal circulation on a sphere of radius r0
with two polar defects on the axis. Its coupling to the mesh is taken as
the overlap of that surface structure with the three-family strand
lattice: strands lie along x, y, z at spacing a; the interaction energy
of the core with a strand is taken proportional to the circulation
strength crossed with the strand direction, integrated over the core
surface. This is a PROXY, not the registered electron.
"""
import numpy as np

rng = np.random.default_rng(2)

def core_energy(axis, s, a=1.0, ntheta=240, nphi=480):
    """Overlap of ELEC-091's boundary structure with the 3-family mesh.

    Azimuthal field about `axis` on a sphere of radius r0 = s*a, sampled
    on a lat-lon grid; |v| = sin(theta) vanishing at the two poles.
    Mesh coupling: each surface patch couples to the three strand
    families through the local strand phase at that point, cos(2 pi x_i/a)
    summed over i = x, y, z, weighted by the circulation magnitude.
    """
    r0 = s * a
    axis = axis / np.linalg.norm(axis)
    # orthonormal frame with e3 = axis
    tmp = np.array([1.0, 0, 0]) if abs(axis[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = np.cross(axis, tmp); e1 /= np.linalg.norm(e1)
    e2 = np.cross(axis, e1)
    th = (np.arange(ntheta) + 0.5) * np.pi / ntheta
    ph = (np.arange(nphi) + 0.5) * 2 * np.pi / nphi
    TH, PH = np.meshgrid(th, ph, indexing="ij")
    # points on the sphere
    P = (r0 * (np.sin(TH)[..., None] * (np.cos(PH)[..., None] * e1
                                        + np.sin(PH)[..., None] * e2)
               + np.cos(TH)[..., None] * axis))
    w = np.sin(TH) * (np.pi / ntheta) * (2 * np.pi / nphi) * r0**2   # area
    circ = np.sin(TH)                      # |e_phi|, zero at the poles
    phase = (np.cos(2 * np.pi * P[..., 0] / a)
             + np.cos(2 * np.pi * P[..., 1] / a)
             + np.cos(2 * np.pi * P[..., 2] / a))
    return float(np.sum(w * circ * phase))

# symmetry-inequivalent axis directions for a cubic mesh
AXES = {
    "[100]": np.array([1.0, 0, 0]),
    "[110]": np.array([1.0, 1.0, 0]),
    "[111]": np.array([1.0, 1.0, 1.0]),
    "[210]": np.array([2.0, 1.0, 0]),
    "[211]": np.array([2.0, 1.0, 1.0]),
    "[321]": np.array([3.0, 2.0, 1.0]),
}

print("L2 -- ORIENTATION SCAN AT TRACTABLE s = r0/a")
print(f"{'s':>6} " + " ".join(f"{k:>11}" for k in AXES) + f" {'dE/E_scale':>12}")
S_LIST = [2.5, 3.5, 5.0, 7.0, 10.0, 14.0]
ratios = []
for s in S_LIST:
    E = {k: core_energy(v, s) for k, v in AXES.items()}
    vals = np.array(list(E.values()))
    scale = 4 * np.pi * (s ** 2) * (2.0 / 3.0)   # ~ surface x mean |circ|
    d = (vals.max() - vals.min()) / scale
    ratios.append(d)
    print(f"{s:>6.1f} " + " ".join(f"{E[k]:>11.3e}" for k in AXES)
          + f" {d:>12.3e}")

ratios = np.array(ratios); S = np.array(S_LIST)
print("\nL3 -- THE SCALING, both fits reported")
ok = ratios > 0
lp = np.polyfit(np.log(S[ok]), np.log(ratios[ok]), 1)
rp = np.log(ratios[ok]) - np.polyval(lp, np.log(S[ok]))
le = np.polyfit(S[ok], np.log(ratios[ok]), 1)
re_ = np.log(ratios[ok]) - np.polyval(le, S[ok])
print(f"   power law   exponent {lp[0]:+.3f}   SSR {np.sum(rp**2):.4e}")
print(f"   exponential rate     {le[0]:+.4f}   SSR {np.sum(re_**2):.4e}")
power = np.sum(rp**2) < np.sum(re_**2)
print(f"   => {'POWER LAW' if power else 'EXPONENTIAL'}")

print("\nL4 -- EXTRAPOLATION AND CONFRONTATION (bar 1e-6 eV)")
M_E = 510998.95
for s_phys in (82.6, 108.0):
    if power:
        frac = np.exp(np.polyval(lp, np.log(s_phys)))
    else:
        frac = np.exp(np.polyval(le, s_phys))
    E = M_E * frac
    print(f"   s = {s_phys:5.1f}:  dE/E = {frac:.3e}   E_pin = {E:.3e} eV   "
          f"{'PASS' if E < 1e-6 else 'FAIL'}")
