"""WHY-WINDING BRICK 1 -- the dispersion lattice, executed under
analysis/WHYWIND_dispersion_bars_LOCKED.md (locked before this file
was written). Pure numpy desk computation; no solves, no marches.
"""
from collections import deque

import numpy as np

OM1 = (2 * np.pi / np.sqrt(3)) * np.sqrt(1.5)          # 4.442883

CELLS = {                       # q: (N1, N2, [om2 members: first, deepest])
    '4/3': (3, 4, [2.14842, 2.21540]),
    '3/2': (2, 3, [3.20, 3.27]),
    '5/3': (3, 5, [4.23408, 4.38221]),
}


def orders(n1, n2, ncap=6, mcap=40, ocap=8):
    """BFS over the content lattice C = {(+-1,+-N2),(0,+-N1)}."""
    gens = [(1, n2), (1, -n2), (-1, n2), (-1, -n2), (0, n1), (0, -n1)]
    dist = {(0, 0): 0}
    dq = deque([(0, 0)])
    while dq:
        p = dq.popleft()
        d = dist[p]
        if d == ocap:
            continue
        for g in gens:
            np_ = (p[0] + g[0], p[1] + g[1])
            if abs(np_[0]) <= ncap and abs(np_[1]) <= mcap and np_ not in dist:
                dist[np_] = d + 1
                dq.append(np_)
    return dist


def lattice(n1, n2):
    """All resonance lines with their coupling order."""
    dist = orders(n1, n2)
    out = []
    for n in range(1, 7):
        for m in range(-40, 41):
            om2 = OM1 * (m / n1 - 1) / n
            if om2 <= 0 or om2 > 8:
                continue
            o = dist.get((n, m), 99)
            out.append(dict(n=n, m=m, om2=om2, order=o))
    return out


def report(q):
    n1, n2, mem = CELLS[q]
    lat = lattice(n1, n2)
    first, deep = mem
    for L in lat:
        L['d_first'] = (first - L['om2']) / L['om2']
        L['d_deep'] = (deep - L['om2']) / L['om2']
    lo = [L for L in lat if L['order'] <= 5]
    lo.sort(key=lambda L: abs(L['d_deep']))
    print(f"\n== q = {q}  (N1={n1}, N2={n2})  om2: {first} -> {deep}"
          f"  (om2/Om1 = {deep/OM1:.4f})")
    print("   nearest order<=5 lines at the deepest member:")
    for L in lo[:4]:
        appr = abs(L['d_deep']) < abs(L['d_first'])
        print(f"     (n={L['n']:2d}, m={L['m']:3d})  Om2 = {L['om2']:.5f}"
              f"  = {L['om2']/OM1:.4f} Om1   order {L['order']}"
              f"   delta_deep {L['d_deep']:+.4f}"
              f"   approach {'YES' if appr else 'no'}")
    best = lo[0]
    anyl = sorted(lat, key=lambda L: abs(L['d_deep']))[0]
    print(f"   nearest line of ANY order: (n={anyl['n']},m={anyl['m']}) "
          f"order {anyl['order']}  delta {anyl['d_deep']:+.4f}")
    return best, lo


def main():
    print("WHY-WINDING BRICK 1 -- dispersion lattice under locked bars")
    print(f"Om1 = {OM1:.6f}; lines Om2 = Om1(m/N1 - 1)/n; "
          "order = BFS over C = {(+-1,+-N2),(0,+-N1)}, cap 8")
    res = {}
    for q in CELLS:
        res[q] = report(q)

    print("\n== VERDICT BLOCK (mechanical, per the locked lines) ==")
    b43, b32 = res['4/3'][0], res['3/2'][0]
    d43, d32 = abs(b43['d_deep']), abs(b32['d_deep'])
    a43 = d43 < abs(b43['d_first'])
    a32 = d32 < abs(b32['d_first'])
    r1 = d43 <= 0.02 and d32 <= 0.02 and a43 and a32
    print(f"R1 collapsers within 2pct of an order<=5 line, approaching:"
          f" 4/3 |d|={d43:.4f} appr={a43}; 3/2 |d|={d32:.4f} appr={a32}"
          f"  -> {'PASS' if r1 else 'FAIL'}")
    worst = max(d43, d32)
    lo53 = res['5/3'][1]
    d53 = abs(lo53[0]['d_deep']) if lo53 else np.inf
    r2a = d53 >= 3 * worst
    firing_omax = max(b43['order'], b32['order'])
    lat53 = lattice(3, 5)
    near53 = sorted(lat53, key=lambda L: abs((CELLS['5/3'][2][1] - L['om2'])
                                             / L['om2']))[0]
    r2b = near53['order'] >= firing_omax + 2
    print(f"R2 flat cell: nearest order<=5 |d|={d53:.4f} "
          f"(>=3x worst collapser {3*worst:.4f}: {r2a}); nearest any-order "
          f"line order {near53['order']} vs firing max {firing_omax} "
          f"(+2 rule: {r2b})  -> {'PASS' if (r2a or r2b) else 'FAIL'}")
    r3 = (b43['n'], b43['m'], 3) != (b32['n'], b32['m'], 2)
    print(f"R3 distinct firing lines: 4/3 (n={b43['n']},m={b43['m']}) vs "
          f"3/2 (n={b32['n']},m={b32['m']})  -> {'PASS' if r3 else 'FAIL'}")
    v = 'RES-CONSISTENT' if (r1 and (r2a or r2b) and r3) else 'RES-OPEN'
    print(f"\n**** VERDICT: {v} ****")

    print("\n== om2(q) empirical interpolation (deepest members) ==")
    qs = np.array([4/3, 3/2, 5/3])
    om = np.array([CELLS['4/3'][2][1], CELLS['3/2'][2][1],
                   CELLS['5/3'][2][1]])
    A = np.vstack([qs, np.ones(3)]).T
    sl, ic = np.linalg.lstsq(A, om, rcond=None)[0]
    resid = om - (sl * qs + ic)
    print(f"   om2 ~ {sl:.4f} q + {ic:+.4f}   residuals {resid}")
    for qq, nn1, nn2 in [(7/5, 5, 7), (8/5, 5, 8), (5/4, 4, 5),
                         (7/4, 4, 7)]:
        pred = sl * qq + ic
        lat = lattice(nn1, nn2)
        lo = [L for L in lat if L['order'] <= 5]
        lo.sort(key=lambda L: abs((pred - L['om2']) / L['om2']))
        L = lo[0]
        print(f"   q={qq:.3f} (N1={nn1},N2={nn2}): om2_pred {pred:.4f}; "
              f"nearest order<=5 line (n={L['n']},m={L['m']}) "
              f"Om2={L['om2']:.4f} order {L['order']} "
              f"delta {(pred-L['om2'])/L['om2']:+.4f}")


if __name__ == '__main__':
    main()
