"""COMMISSION SHIN3 -- tight-winding window + Bloch check.
Executed under analysis/SHIN3_tight_winding_bars_LOCKED.md."""
import numpy as np, itertools

# ---------- G1: the window ----------
def g1():
    print("G1 constructibility window")
    grid = np.deg2rad(np.arange(5, 90, 1.0))
    ok_readings = []
    for tag, margin in [("kappa50", 6.1), ("kappa250", 10.5)]:
        found = []
        for p1, p2 in itertools.product(grid, grid):
            s = np.sin(p1)*np.sin(p2)
            if s*s < 1.0/margin:      # W-b
                continue
            A1, A2 = np.arccos(np.sin(p1)), np.arccos(np.sin(p2))
            lo, hi = abs(A1-A2), min(A1+A2, np.pi/2)
            cov = np.cos(lo) - np.cos(hi)   # folded annulus fraction per family (>= one family)
            if cov < 0.10:            # W-c
                continue
            found.append((np.degrees(p1), np.degrees(p2), s, cov))
        ok = len(found) > 0
        ok_readings.append(ok)
        if ok:
            a = np.array(found)
            print(f"  {tag}: window NON-EMPTY ({len(found)} grid members); "
                  f"psi ranges {a[:,0].min():.0f}-{a[:,0].max():.0f} x {a[:,1].min():.0f}-{a[:,1].max():.0f} deg; "
                  f"sin(psi_eff) {a[:,2].min():.3f}-{a[:,2].max():.3f}")
        else:
            print(f"  {tag}: window EMPTY")
    print("  G1", "PASS" if all(ok_readings) else "FAIL")
    return all(ok_readings)

# ---------- G2: Bloch at tight pitch (TAV3B machinery) ----------
KX = 0.08
KABS = 2*np.pi/6.0
DIRS = np.deg2rad(np.arange(0, 360, 45))
NBRS = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

def dyn_matrix(k, P1, P2, wound=True):
    n = P1*P2
    idx = lambda x, y: (x % P1)*P2 + (y % P2)
    D = np.zeros((n, n), dtype=complex)
    for x in range(P1):
        for y in range(P2):
            phi = 2*np.pi*x/P1 + 2*np.pi*y/P2 if wound else 0.0
            i = idx(x, y)
            for dx, dy in NBRS:
                th = np.arctan2(dy, dx)
                w = (KX + np.cos(th - phi)**2)/(dx*dx + dy*dy)
                j = idx(x+dx, y+dy)
                D[i, j] -= w*np.exp(1j*(k[0]*dx + k[1]*dy))
                D[i, i] += w
    return D

def norm_scale():
    kk = 0.05
    D = dyn_matrix((kk, 0.0), 3, 4, wound=False)
    w2 = np.linalg.eigvalsh((D + D.conj().T)/2)
    return np.sqrt(max(w2.min(), 0))/kk

def pw_vec(k, P1, P2):
    v = np.zeros(P1*P2, dtype=complex)
    for x in range(P1):
        for y in range(P2):
            v[x*P2+y] = np.exp(1j*(k[0]*x + k[1]*y))
    return v/np.linalg.norm(v)

def peak(kv, P1, P2, scale):
    D = dyn_matrix(kv, P1, P2)
    w2, V = np.linalg.eigh((D + D.conj().T)/2)
    om = np.sqrt(np.clip(w2, 0, None))/scale
    wts = np.abs(V.conj().T @ pw_vec(kv, P1, P2))**2
    b = int(np.argmax(wts))
    return om[b], wts[b]

def g2():
    print("\nG2 tight-wound Bloch check (locked pitch set)")
    scale = norm_scale()
    passing = None
    for P1, P2 in [(3,4),(4,6),(5,6),(6,6)]:
        ps, gs, an, wt = [], [], [], []
        for th in DIRS:
            k = (KABS*np.cos(th), KABS*np.sin(th))
            dk = 1e-3
            om0, w0 = peak(k, P1, P2, scale)
            omx, _ = peak((k[0]+dk, k[1]), P1, P2, scale)
            omy, _ = peak((k[0], k[1]+dk), P1, P2, scale)
            g = np.array([(omx-om0)/dk, (omy-om0)/dk]); gsp = np.linalg.norm(g)
            ang = np.degrees(np.arccos(np.clip(g @ np.array(k)/(gsp*KABS+1e-30), -1, 1)))
            ps.append(om0/KABS); gs.append(gsp); an.append(ang); wt.append(w0)
        ps, gs, an, wt = map(np.array, (ps, gs, an, wt))
        spread = (ps.max()-ps.min())/ps.mean()
        b1, b2, b3 = gs.min() >= 0.3, spread <= 0.05, an.max() <= 15
        print(f"  (P1,P2)=({P1},{P2}): mean phase v={ps.mean():.3f} spread={spread:.4f} "
              f"min group v={gs.min():.3f} max angle err={an.max():.1f} min pw wt={wt.min():.2f} "
              f"-> B1 {'P' if b1 else 'F'} B2 {'P' if b2 else 'F'} B3 {'P' if b3 else 'F'}")
        if b1 and b2 and b3 and passing is None:
            passing = (P1, P2, ps.mean(), spread)
    print("  G2", f"PASS at {passing[:2]}, speed factor {passing[2]:.3f}" if passing else "FAIL")
    return passing

if __name__ == "__main__":
    ok1 = g1()
    res = g2()
    print("\nVERDICT:", "PASS -- adoption per standing authorization" if (ok1 and res) else "FAILED-AND-KEPT, no adoption")
