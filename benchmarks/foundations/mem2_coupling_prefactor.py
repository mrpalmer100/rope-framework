#!/usr/bin/env python3
"""COMMISSION MEM-2 -- the coupling prefactor on the registered engine.

Bars: analysis/MEM2_coupling_prefactor_bars_LOCKED.md.
Engine: FND-STRAND-001 as implemented in matter062_settler.py --
inextensible curves by exact projection, bending, finite smooth contact.
NO coupling model is introduced; the coupling is whatever the registered
contact energetics produce.
"""
import numpy as np

rng = np.random.default_rng(7)

# ---- registered engine parameters (unchanged) ----
KB = 0.6
AC, SIG = 1.0, 0.30
DT, STEPS = 0.004, 4000
PROJ_ITERS = 25
A = 1.0                      # weave spacing
XANCH = 7.0
NPTS = 81

def make_family(axis, offs):
    """strands along `axis` at transverse offsets `offs` (mesh spacing A)."""
    t = np.linspace(-XANCH, XANCH, NPTS)
    out = []
    for (u, v) in offs:
        P = np.zeros((NPTS, 3))
        P[:, axis] = t
        o1, o2 = [i for i in range(3) if i != axis]
        P[:, o1] = u; P[:, o2] = v
        out.append(P)
    return out

def inclusion(axis_dir, s, npts=61):
    """prolate rigid inclusion: a segment of half-length s*A along axis_dir,
    the minimal anisotropic core available to a contact engine."""
    d = np.asarray(axis_dir, float); d /= np.linalg.norm(d)
    t = np.linspace(-s, s, npts)[:, None]
    return t * d[None, :] * A

def seg_len(X): return np.linalg.norm(np.diff(X, axis=0), axis=1)

def project(Xs, R):
    for _ in range(PROJ_ITERS):
        d = Xs[:, 1:] - Xs[:, :-1]
        L = np.sqrt(np.einsum('sij,sij->si', d, d)) + 1e-15
        corr = d * (0.5 * (L - R) / L)[..., None]
        Xs[:, 1:-1] += corr[:, 1:] - corr[:, :-1]
    return Xs

def contact_energy(Xs, inc):
    """registered finite contact Ac/(1+(r/sigma)^4), summed over midpoints."""
    m = 0.5 * (Xs[:, :-1] + Xs[:, 1:])
    E = 0.0
    for i in range(m.shape[0]):
        D = m[i][:, None, :] - inc[None, :, :]
        r2 = np.sum(D * D, axis=2)
        E += np.sum(AC / (1.0 + (r2 / SIG**2) ** 2))
    return float(E)

def bend_energy(Xs):
    lap = Xs[:, 2:] - 2 * Xs[:, 1:-1] + Xs[:, :-2]
    return float(0.5 * KB * np.sum(lap * lap))

def relax(inc, seed=0, steps=STEPS):
    r = np.random.default_rng(seed)
    offs = [(u, v) for u in (-1.0, 0.0, 1.0) for v in (-1.0, 0.0, 1.0)]
    Xl = []
    for ax in (0, 1, 2):
        Xl += make_family(ax, offs)
    Xs = np.stack(Xl)
    Xs[:, 1:-1] += r.normal(0, 1e-3, Xs[:, 1:-1].shape)
    R = np.stack([seg_len(X) for X in Xs])
    for _ in range(steps):
        G = np.zeros_like(Xs)
        lap = np.zeros_like(Xs)
        lap[:, 1:-1] = Xs[:, 2:] - 2 * Xs[:, 1:-1] + Xs[:, :-2]
        bl = np.zeros_like(Xs)
        bl[:, 1:-1] = lap[:, 2:] - 2 * lap[:, 1:-1] + lap[:, :-2]
        G += KB * bl
        m = 0.5 * (Xs[:, :-1] + Xs[:, 1:])
        fm = np.zeros_like(m)
        for i in range(m.shape[0]):
            D = m[i][:, None, :] - inc[None, :, :]
            r2 = np.sum(D * D, axis=2)
            u = (r2 / SIG**2) ** 2
            w = -AC * 4.0 * u / (r2 + 1e-12) / (1.0 + u) ** 2
            fm[i] = np.einsum('nm,nmk->nk', w, D)
        G[:, :-1] += 0.5 * fm
        G[:, 1:] += 0.5 * fm
        G[:, 0] = 0.0; G[:, -1] = 0.0
        Xs = project(Xs - DT * G, R)
    return contact_energy(Xs, inc) + bend_energy(Xs), Xs

AXES = {"[100]": (1, 0, 0), "[110]": (1, 1, 0), "[111]": (1, 1, 1)}

print("NOISE FLOOR (required before any Delta E is reported):")
e_seeds = [relax(inclusion(AXES["[100]"], 2.0), seed=k, steps=1500)[0]
           for k in (0, 1, 2)]
noise = max(e_seeds) - min(e_seeds)
print(f"   [100], s=2.0, three seeds: {['%.6f' % v for v in e_seeds]}")
print(f"   convergence spread (noise floor) = {noise:.3e}\n")

print("M1/M2 -- ORIENTATION SCAN ON THE REGISTERED ENGINE")
print(f"{'s':>5} " + " ".join(f"{k:>12}" for k in AXES)
      + f" {'dE':>11} {'dE/E':>11}  vs noise")
for s in (1.5, 2.0, 3.0):
    E = {k: relax(inclusion(v, s), seed=0, steps=1500)[0]
         for k, v in AXES.items()}
    vals = np.array(list(E.values()))
    dE = vals.max() - vals.min()
    frac = dE / abs(vals.mean())
    print(f"{s:>5.1f} " + " ".join(f"{E[k]:>12.6f}" for k in AXES)
          + f" {dE:>11.3e} {frac:>11.3e}  "
          + ("SIGNAL" if dE > 3 * noise else "NOISE-LIMITED"))
