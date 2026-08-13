#!/usr/bin/env python3
"""COMMISSION SAMEKH-2 -- extracting C_pin on the registered engine.

Bars: analysis/SAMEKH2_cpin_bars_LOCKED.md.
Form FIXED by ELEC-096: E_pin(n) = C_pin s^-3/2 K(n) E_core,
K(n) = sum_i n_i^4 - 3/5. Exponent is fixed input, NOT re-derived.
Estimator: projection of relaxed energy onto K(n), not max-minus-min.
"""
import numpy as np

KB = 0.6
AC, SIG = 1.0, 0.30
DT = 0.004
PROJ_ITERS = 25
A = 1.0

def seg_len(X): return np.linalg.norm(np.diff(X, axis=0), axis=1)

def project(Xs, R):
    for _ in range(PROJ_ITERS):
        d = Xs[:, 1:] - Xs[:, :-1]
        L = np.sqrt(np.einsum('sij,sij->si', d, d)) + 1e-15
        corr = d * (0.5 * (L - R) / L)[..., None]
        Xs[:, 1:-1] += corr[:, 1:] - corr[:, :-1]
    return Xs

def build(nrings, xanch, npts):
    offs = [(u, v) for u in np.arange(-nrings, nrings + 1)
            for v in np.arange(-nrings, nrings + 1)]
    t = np.linspace(-xanch, xanch, npts)
    Xl = []
    for ax in (0, 1, 2):
        o1, o2 = [i for i in range(3) if i != ax]
        for (u, v) in offs:
            P = np.zeros((npts, 3)); P[:, ax] = t; P[:, o1] = u; P[:, o2] = v
            Xl.append(P)
    return np.stack(Xl)

def inclusion(nvec, s, npts=41):
    d = np.asarray(nvec, float); d /= np.linalg.norm(d)
    return np.linspace(-s, s, npts)[:, None] * d[None, :] * A

def energy(Xs, inc):
    m = 0.5 * (Xs[:, :-1] + Xs[:, 1:])
    E = 0.0
    for i in range(m.shape[0]):
        D = m[i][:, None, :] - inc[None, :, :]
        r2 = np.sum(D * D, axis=2)
        E += np.sum(AC / (1.0 + (r2 / SIG**2) ** 2))
    lap = Xs[:, 2:] - 2 * Xs[:, 1:-1] + Xs[:, :-2]
    return float(E + 0.5 * KB * np.sum(lap * lap))

def relax(inc, nrings, xanch, npts, steps, seed=0):
    r = np.random.default_rng(seed)
    Xs = build(nrings, xanch, npts)
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
        G[:, :-1] += 0.5 * fm; G[:, 1:] += 0.5 * fm
        G[:, 0] = 0.0; G[:, -1] = 0.0
        Xs = project(Xs - DT * G, R)
    return energy(Xs, inc), Xs

def K(n):
    u = np.asarray(n, float); u = u / np.linalg.norm(u)
    return np.sum(u**4) - 0.6

# orientation set spanning the harmonic
DIRS = [(1,0,0),(1,1,0),(1,1,1),(2,1,0),(2,1,1),(3,2,1),(1,2,3),(2,2,1),(3,1,1)]
Kv = np.array([K(d) for d in DIRS])

NR, XA, NP, ST = 1, 9.0, 61, 600
print(f"box: nrings={NR} (offsets +-{NR}a), xanch={XA}, npts={NP}, steps={ST}")
print(f"strands: {3*(2*NR+1)**2}\n")

print("NOISE FLOOR at this box (before any signal is read):")
es = [relax(inclusion((1,0,0), 3.0), NR, XA, NP, ST, seed=k)[0] for k in (0,1,2)]
noise = max(es) - min(es)
print(f"   {['%.5f'%v for v in es]}   spread = {noise:.3e}\n")

print("PROJECTION ONTO THE ORDER-4 HARMONIC (per the bar)")
print(f"{'s':>5} {'amp':>12} {'|amp|/E':>11} {'R^2 of K-fit':>13}  regime")
prev = None
for s in (2.0, 3.0, 4.0, 5.0):
    E = np.array([relax(inclusion(d, s), NR, XA, NP, ST)[0] for d in DIRS])
    Aa = np.vstack([Kv, np.ones_like(Kv)]).T
    sol, *_ = np.linalg.lstsq(Aa, E, rcond=None)
    pred = Aa @ sol
    ss_res = np.sum((E - pred)**2); ss_tot = np.sum((E - E.mean())**2)
    r2 = 1 - ss_res/ss_tot if ss_tot > 0 else 0.0
    frac = abs(sol[0]) / abs(E.mean())
    trend = "" if prev is None else ("rising" if frac > prev else "FALLING")
    prev = frac
    print(f"{s:>5.1f} {sol[0]:>12.4e} {frac:>11.4e} {r2:>13.4f}  {trend}")

print("\nPer the bar: C_pin may be fitted ONLY from a falling (asymptotic)")
print("branch. If every point rises, the range is PRE-ASYMPTOTIC and no")
print("asymptotic coefficient may be extracted.")
