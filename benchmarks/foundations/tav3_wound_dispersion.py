"""COMMISSION TAV3 -- wound-carrier dispersion check (2D engine test).
Executed under analysis/TAV3_wound_dispersion_bars_LOCKED.md.
"""
import numpy as np

N = 240            # grid
P1, P2 = 24, 60    # winding periods (a_f units), locked
KX_RATIO = 0.08    # crossing / fiber coupling, locked
LAM = 6.0          # carrier wavelength, locked
SLAB = 4 * 60      # slab thickness = 4 * max(P1, P2)
DIRS = np.deg2rad(np.arange(0, 360, 45))

NBRS = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

def build_weights(wound=True):
    x = np.arange(N)
    X, Y = np.meshgrid(x, x, indexing='ij')
    phi = 2*np.pi*(X/P1) + 2*np.pi*(Y/P2) if wound else np.zeros((N, N))
    Ws = []
    for dx, dy in NBRS:
        th = np.arctan2(dy, dx)
        w = KX_RATIO + np.cos(th - phi)**2
        w /= (dx*dx + dy*dy)      # metric weight for diagonals
        Ws.append(w)
    tot = sum(Ws)
    Ws = [w/ (tot/  len(NBRS) ) for w in Ws]   # normalize mean row-sum
    return Ws

def laplacian(u, Ws):
    out = -u * sum(Ws)
    for (dx, dy), w in zip(NBRS, Ws):
        out += w * np.roll(np.roll(u, dx, 0), dy, 1)
    return out

def run_direction(theta, Ws, steps=1400, dt=0.28):
    """Launch a Gaussian wave packet at angle theta; track centroid."""
    x = np.arange(N)
    X, Y = np.meshgrid(x, x, indexing='ij')
    kx, ky = 2*np.pi/LAM*np.cos(theta), 2*np.pi/LAM*np.sin(theta)
    cx = cy = N//4
    # start packet at quarter point along -theta so it crosses the slab
    cx = int(N/2 - (SLAB/2)*np.cos(theta)) % N
    cy = int(N/2 - (SLAB/2)*np.sin(theta)) % N
    R2 = ((X-cx+N/2) % N - N/2)**2 + ((Y-cy+N/2) % N - N/2)**2
    env = np.exp(-R2/(2*12.0**2))
    phase = kx*(X-cx) + ky*(Y-cy)
    u = env*np.cos(phase)
    # traveling-wave launch: v = -c d u / d s_along  (c ~ 1 after normalization)
    us = env*np.sin(phase)
    k = np.hypot(kx, ky)
    v = k*us  # d/dt of cos(phase - w t) at t=0 gives +w sin(phase); w = c k ~ k
    E0 = None
    # centroid via energy density
    ts, cents = [], []
    for s in range(steps):
        a = laplacian(u, Ws)
        v += dt*a; u += dt*v
        if s % 50 == 0:
            e = v**2 + 1e-30
            # unwrap centroid near expected line
            wsum = e.sum()
            gx = (np.angle(np.exp(1j*2*np.pi*X/N)*e).sum())  # not robust; use direct on shifted coords
            Xs = ((X-cx+N/2) % N) - N/2
            Ys = ((Y-cy+N/2) % N) - N/2
            mx = (e*Xs).sum()/wsum; my = (e*Ys).sum()/wsum
            ts.append(s*dt); cents.append((mx, my))
        if E0 is None:
            E0 = (v**2).sum() + 1e-30
    cents = np.array(cents); ts = np.array(ts)
    # distance along theta and transverse
    along = cents[:,0]*np.cos(theta) + cents[:,1]*np.sin(theta)
    perp  = -cents[:,0]*np.sin(theta) + cents[:,1]*np.cos(theta)
    # group speed from linear fit over the middle stretch
    m = (along > 10) & (along < SLAB*0.6)
    if m.sum() < 4:
        return 0.0, 1e9, 1e9
    sp = np.polyfit(ts[m], along[m], 1)[0]
    drift = abs(perp[m][-1] - perp[m][0]) / SLAB
    # transmission proxy: energy within a corridor around the ray at end
    return sp, drift, along[-1]

def main():
    print("TAV3 -- wound-carrier dispersion check (locked bars)")
    for wound, tag in [(False, "W0 straight control"), (True, "wound (P1=24, P2=60)")]:
        Ws = build_weights(wound)
        print(f"\n{tag}:")
        sps, drs = [], []
        for th in DIRS:
            sp, dr, reach = run_direction(th, Ws)
            sps.append(sp); drs.append(dr)
            print(f"  theta={np.rad2deg(th):5.1f}: group speed={sp:6.3f}  transverse drift={dr:6.3f}  reach={reach:7.1f}")
        sps = np.array(sps); drs = np.array(drs)
        spread = (sps.max()-sps.min())/max(sps.mean(), 1e-9)
        print(f"  speed spread (max-min)/mean = {spread:.4f}; max drift = {drs.max():.3f}")
        if not wound:
            control_fails = spread > 0.05 or (sps.min() < 0.5*sps.max())
            print(f"  CONTROL {'FAILS off-axis as required (instrument valid)' if control_fails else 'DOES NOT FAIL -- INSTRUMENT-INVALID'}")
        else:
            m2 = spread <= 0.05
            m3 = drs.max() <= 0.1
            print(f"  M2 speed isotropy {'PASS' if m2 else 'FAIL'}; M3 straightness {'PASS' if m3 else 'FAIL'}")

if __name__ == "__main__":
    main()
