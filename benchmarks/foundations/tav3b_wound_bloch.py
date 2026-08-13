"""COMMISSION TAV3B -- wound-carrier Bloch check.
Executed under analysis/TAV3B_wound_bloch_bars_LOCKED.md."""
import numpy as np

P1, P2 = 24, 60
KX = 0.08
KABS = 2*np.pi/6.0
DIRS = np.deg2rad(np.arange(0, 360, 45))
NBRS = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

def weights(phi):
    ws = []
    for dx, dy in NBRS:
        th = np.arctan2(dy, dx)
        w = (KX + np.cos(th - phi)**2)/(dx*dx + dy*dy)
        ws.append(w)
    return ws

def dyn_matrix(k, wound=True):
    n = P1*P2
    idx = lambda x, y: (x % P1)*P2 + (y % P2)
    D = np.zeros((n, n), dtype=complex)
    for x in range(P1):
        for y in range(P2):
            phi = 2*np.pi*x/P1 + 2*np.pi*y/P2 if wound else 0.0
            ws = weights(phi)
            i = idx(x, y)
            for (dx, dy), w in zip(NBRS, ws):
                j = idx(x+dx, y+dy)
                bloch = np.exp(1j*(k[0]*dx + k[1]*dy))
                D[i, j] -= w*bloch
                D[i, i] += w
    return D

def norm_scale():
    # straight medium along-fiber small-k speed -> 1
    kk = 0.05
    D = dyn_matrix((kk, 0.0), wound=False)
    w2 = np.linalg.eigvalsh((D + D.conj().T)/2)
    om = np.sqrt(max(w2.min(), 0))
    return (om/kk)

def pw_vec(k):
    v = np.zeros(P1*P2, dtype=complex)
    for x in range(P1):
        for y in range(P2):
            v[x*P2+y] = np.exp(1j*(k[0]*x + k[1]*y))
    return v/np.linalg.norm(v)

def spectral_peak(kv, wound, scale):
    D = dyn_matrix(kv, wound)
    w2, V = np.linalg.eigh((D + D.conj().T)/2)
    om = np.sqrt(np.clip(w2, 0, None))/scale
    psi = pw_vec(kv)
    wts = np.abs(V.conj().T @ psi)**2
    b = int(np.argmax(wts))
    return om[b], wts[b], b

def acoustic_speed(k, wound, scale, dk=1e-3):
    """Plane-wave spectral identification of the propagating branch."""
    om0, wt, b = spectral_peak(k, wound, scale)
    omx, _, _ = spectral_peak((k[0]+dk, k[1]), wound, scale)
    omy, _, _ = spectral_peak((k[0], k[1]+dk), wound, scale)
    g = np.array([(omx-om0)/dk, (omy-om0)/dk])
    gs = np.linalg.norm(g)
    ps = om0/KABS
    ang = np.degrees(np.arccos(np.clip(g @ np.array(k)/(gs*np.linalg.norm(k)+1e-30), -1, 1)))
    return ps, gs, ang, b, wt

def main():
    scale = norm_scale()
    print(f"normalization: straight along-fiber speed -> 1 (scale {scale:.4f})")
    for wound, tag in [(False, "W0 straight control"), (True, "wound")]:
        print(f"\n{tag}:")
        ps_list, gs_list, ang_list = [], [], []
        for th in DIRS:
            k = (KABS*np.cos(th), KABS*np.sin(th))
            ps, gs, ang, b, wt = acoustic_speed(k, wound, scale)
            ps_list.append(ps); gs_list.append(gs); ang_list.append(ang)
            print(f"  theta={np.degrees(th):5.1f}: phase v={ps:6.3f} group v={gs:6.3f} group-angle err={ang:5.1f} deg (band {b}, pw weight {wt:.2f})")
        ps_a, gs_a, an_a = map(np.array, (ps_list, gs_list, ang_list))
        spread = (ps_a.max()-ps_a.min())/ps_a.mean()
        print(f"  phase-speed spread={spread:.4f}  min group v={gs_a.min():.3f}  max angle err={an_a.max():.1f}")
        if not wound:
            valid = spread > 0.3 or gs_a.min() < 0.3
            print("  CONTROL", "shows the obstruction (instrument valid)" if valid else "INVALID")
        else:
            b1 = gs_a.min() >= 0.3
            b2 = spread <= 0.05
            b3 = an_a.max() <= 15
            print(f"  B1 propagation {'PASS' if b1 else 'FAIL'}; B2 isotropy {'PASS' if b2 else 'FAIL'}; B3 straightness {'PASS' if b3 else 'FAIL'}")

if __name__ == "__main__":
    main()
