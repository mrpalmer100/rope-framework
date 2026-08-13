"""COMMISSION SHIN6 -- the 3D two-polarization Bloch instrument.
Executed under analysis/SHIN6_3d_bloch_bars_LOCKED.md.
Derived winding angles from FND-088; no free angles.
"""
import numpy as np
import itertools

PSI1 = np.arcsin(1/np.sqrt(3))
PSI2 = np.arcsin(np.sqrt((15 + 2*np.sqrt(30))/35))
KX = 0.08
KABS = 2*np.pi/24.0
DK = 1e-3

# 18-neighbor stencil (6 NN + 12 NNN)
NBRS = [b for b in itertools.product((-1,0,1), repeat=3)
        if 0 < sum(v*v for v in b) <= 2]

# 13 probe directions
DIRS = []
for b in itertools.product((0,1), repeat=3):
    if sum(b) > 0:
        DIRS.append(np.array(b, float)/np.linalg.norm(b))
for b in [(1,-1,0),(1,0,-1),(0,1,-1),(1,-1,1),(1,1,-1),(-1,1,1)]:
    DIRS.append(np.array(b, float)/np.linalg.norm(b))
DIRS = DIRS[:13]

def frame(t):
    """Orthonormal frame with third axis t."""
    a = np.array([1.0,0,0]) if abs(t[0]) < 0.9 else np.array([0,1.0,0])
    e1 = np.cross(t, a); e1 /= np.linalg.norm(e1)
    e2 = np.cross(t, e1)
    return e1, e2

def tangent(x, y, z, f, wound=True):
    """Two-level derived winding; f = fractional phase advance/step."""
    if not wound:
        return np.array([0.0, 0.0, 1.0])
    ph1 = 2*np.pi*f*x
    ph2 = 2*np.pi*f*(y + z)
    # level-1 tangent: pitch angle PSI1 from transverse plane, axis z
    t1 = np.array([np.cos(PSI1)*np.cos(ph1),
                   np.cos(PSI1)*np.sin(ph1),
                   np.sin(PSI1)])
    # level-2: same construction in the level-1 local frame, angle PSI2
    e1, e2 = frame(t1)
    return (np.cos(PSI2)*np.cos(ph2)*e1 +
            np.cos(PSI2)*np.sin(ph2)*e2 +
            np.sin(PSI2)*t1)

def build_cell(f, wound):
    """Minimal integer period of the phase advance."""
    P = 1 if not wound else int(round(1/f)) if abs(round(1/f)-1/f) < 1e-9 \
        else int(round(np.lcm(int(round(f*6)), 6)/int(round(f*6))*1))  # fallback
    # robust: find smallest P with f*P integer (f rational with small denom)
    P = 1
    while P < 13 and abs(f*P - round(f*P)) > 1e-9:
        P += 1
    if not wound:
        P = 1
    sites = list(itertools.product(range(P), repeat=3))
    T = {s: tangent(*s, f, wound) for s in sites}
    PR = {s: np.eye(3) - np.outer(T[s], T[s]) for s in sites}  # transverse projector
    return P, sites, T, PR

def dyn_matrix(kv, P, sites, T, PR):
    """Central-spring vector lattice; acoustic sum rule by construction."""
    n = len(sites)
    idx = {s: i for i, s in enumerate(sites)}
    D = np.zeros((3*n, 3*n), dtype=complex)
    for s in sites:
        i = idx[s]
        for b in NBRS:
            bh = np.array(b, float); r2 = bh @ bh; bh = bh/np.sqrt(r2)
            sj = tuple((s[m]+b[m]) % P for m in range(3))
            j = idx[sj]
            shell = 1.0 if r2 == 1 else 2.0   # g=2: null-isotropy calibration (locked addendum 4)
            w = shell*(KX + 0.5*((bh @ T[s])**2 + (bh @ T[sj])**2))/r2
            blk = w * np.outer(bh, bh)
            ph = np.exp(1j*(kv @ np.array(b, float)))
            D[3*i:3*i+3, 3*j:3*j+3] -= blk*ph
            D[3*i:3*i+3, 3*i:3*i+3] += blk
    return (D + D.conj().T)/2

def pw_vectors(kv, P, sites, T):
    """Two transverse-polarized plane-wave test vectors."""
    kh = kv/np.linalg.norm(kv)
    a = np.array([1.0,0,0]) if abs(kh[0]) < 0.9 else np.array([0,1.0,0])
    p1 = np.cross(kh, a); p1 /= np.linalg.norm(p1)
    p2 = np.cross(kh, p1)
    vs = []
    for p in (p1, p2):
        v = np.zeros(3*len(sites), dtype=complex)
        for i, s in enumerate(sites):
            v[3*i:3*i+3] = p*np.exp(1j*(kv @ np.array(s, float)))
        vs.append(v/np.linalg.norm(v))
    return vs

def two_bands(kv, P, sites, T, PR, scale):
    D = dyn_matrix(kv, P, sites, T, PR)
    w2, V = np.linalg.eigh(D)
    om = np.sqrt(np.clip(w2, 0, None))/scale
    vs = pw_vectors(kv, P, sites, T)
    # transverse plane-wave weight per band (sum over both polarizations)
    wt = sum(np.abs(V.conj().T @ v)**2 for v in vs)
    order = np.argsort(-wt)
    b1, b2 = order[0], order[1]
    return (om[b1], wt[b1]), (om[b2], wt[b2])

def norm_scale(P, sites, T, PR):
    kk = 0.05
    kv = np.array([0, 0, kk])
    D = dyn_matrix(kv, P, sites, T, PR)
    w2, V = np.linalg.eigh(D)
    om = np.sqrt(np.clip(w2, 0, None))
    vs = pw_vectors(kv, P, sites, T)
    wt = sum(np.abs(V.conj().T @ v)**2 for v in vs)
    b = int(np.argmax(wt))
    return om[b]/kk

def run_case(f, wound, label):
    P, sites, T, PR = build_cell(f, wound)
    # normalization always from the straight medium along z
    Ps, ss, Ts, PRs = build_cell(f, False)
    scale = norm_scale(Ps, ss, Ts, PRs)
    ps, gs, an, wt, split = [], [], [], [], []
    for d in DIRS:
        kv = KABS*d
        (o1, w1), (o2, w2b) = two_bands(kv, P, sites, T, PR, scale)
        for om in (o1, o2):
            ps.append(om/KABS)
        wt += [w1, w2b]
        split.append(abs(o1-o2)/((o1+o2)/2 + 1e-30))
        # group velocity on the upper-weight band
        g = np.zeros(3)
        for m in range(3):
            kp = kv.copy(); kp[m] += DK
            (op, _), _ = two_bands(kp, P, sites, T, PR, scale)
            g[m] = (op - o1)/DK
        gsp = np.linalg.norm(g)
        gs.append(gsp)
        an.append(np.degrees(np.arccos(np.clip(g @ d/(gsp+1e-30), -1, 1))))
    ps, gs, an, wt, split = map(np.array, (ps, gs, an, wt, split))
    spread = (ps.max()-ps.min())/ps.mean()
    res = dict(P=P, mean_v=ps.mean(), spread=spread, min_g=gs.min(),
               max_ang=an.max(), min_wt=wt.min(), max_split=split.max())
    print(f"  {label}: P={P} mean v={ps.mean():.3f} spread={spread:.4f} "
          f"min g={gs.min():.3f} max ang={an.max():.1f} "
          f"min pw wt={wt.min():.2f} max pol split={split.max():.4f}")
    return res

if __name__ == "__main__":
    print("SHIN6 -- 3D two-polarization Bloch (derived angles "
          f"psi1={np.degrees(PSI1):.4f}, psi2={np.degrees(PSI2):.4f})")
    print("\nCTRL straight medium:")
    c = run_case(1/3, False, "straight")
    ctrl_fail = c['spread'] >= 0.20
    print(f"  CTRL {'obstruction visible (valid)' if ctrl_fail else 'INSTRUMENT-INVALID'}")
    print("\nWound members:")
    r8 = run_case(1/3, True, "f=1/3 (in regime, aliased 4th moment, context)")
    r6 = run_case(1/4, True, "f=1/4 (in regime, aliased 4th moment, context)")
    r5 = run_case(1/5, True, "f=1/5 (in regime, isotropy-capable, ADJUDICATING)")
    import os
    if os.environ.get("SHIN6_LOOSE"):
        rL = run_case(1/8, True, "f=1/8 (out of regime, loose control, p=lambda/3)")
    b = r5
    bars = dict(B1=b['min_g'] >= 0.3, B2=b['spread'] <= 0.05,
                B3=b['max_ang'] <= 15, B4=b['min_wt'] >= 0.5,
                B5=b['max_split'] <= 0.05)
    print("\nBars on the adjudicating member (f=1/5):")
    for k, v in bars.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")
    verdict = ctrl_fail and all(bars.values())
    print("\nVERDICT:", "PASS -- debt 3 cleared, proceed to FND-REL-002"
          if verdict else "FAILED-AND-KEPT" if ctrl_fail else "INSTRUMENT-INVALID")
