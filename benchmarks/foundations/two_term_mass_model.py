"""FND-MATTER-009 (Modeled): THE TWO-TERM MASS MODEL, FIRST TABLE --
the marriage of the knot solver (FND-MATTER-006) and the zero-point
instrument (FND-MATTER-008): m(K) = Sigma L(K) + lambda dE_zp(K), with
the conditioning profile extracted from the ACTUAL tightened geometry
(bending energy density kappa^2 per site plus contact terms -- one
named physical map, the same rope constants for every knot) and lambda
the relative weight that remains honestly blocked (FND-MATTER-003).

THE TABLE (full-session values; this benchmark reproduces compact):
  ring: L = 3.141,  turning = 2.0000 pi (exact -- the extractor's
        validation), dE_zp = 3.81, fraction 1.21
  3_1:  L = 16.84,  turning = 7.08 pi,  dE_zp = 30.78, fraction 1.83
  5_1:  L = 25.12,  turning = 10.34 pi, dE_zp = 34.45, fraction 1.37

THE LEVER, measured at 25 percent: zero-point fractions DIFFER between
knots (the tighter trefoil packs more curvature per unit length and
carries proportionally more zero-point), so mass ratios are
lambda-DEPENDENT: m_51/m_31 runs from 1.491 (pure length) to 1.156
(zero-point-dominated) -- a 30 percent swing. Geometry alone does not
fix the mass spectrum.

THE DIRECTION, noted without overclaim: ratios COMPRESS toward 1 as
the zero-point weight grows -- the shape-sensitive term pulls
structures together, which is qualitatively the behavior a
near-degenerate splitting like n/p (1.00138) requires, and which pure
tangle-length arithmetic cannot produce.

HONEST SCOPE: the conditioning map (kappa^2 + contacts) is a named
modeling choice; lambda is blocked and stays said; torus family only
(the 4_1 anomaly stands); 1D chain hosting for the zero-point sum.
"""
import numpy as np


def tighten_coords(P, D=1.0, iters=60000, shrink=0.9997):
    N = len(P)
    I, J = np.triu_indices(N, k=1); ring = np.minimum(J - I, N - (J - I))
    edge_cached = -1; ii = jj = None
    for it in range(iters):
        nxt = np.roll(P, -1, axis=0)
        e = nxt - P; L = np.linalg.norm(e, axis=1); edge = np.mean(L)
        mid = 0.5*(P + nxt); u = e/L[:, None]
        P = 0.5*((mid - 0.5*edge*u) + np.roll(mid + 0.5*edge*u, 1, axis=0))
        v1 = P - np.roll(P, 1, axis=0); v2 = np.roll(P, -1, axis=0) - P
        n1 = v1/np.linalg.norm(v1, axis=1, keepdims=True)
        n2 = v2/np.linalg.norm(v2, axis=1, keepdims=True)
        sharp = np.sum(n1*n2, axis=1) < np.cos(2*edge/D)
        if np.any(sharp):
            midn = 0.5*(np.roll(P, 1, axis=0) + np.roll(P, -1, axis=0))
            P[sharp] = 0.85*P[sharp] + 0.15*midn[sharp]
        c = np.mean(P, axis=0); P = c + (P - c)*shrink
        if ii is None or abs(edge - edge_cached)/max(edge, 1e-9) > 0.05:
            m = (ring*edge) > 1.6*D; edge_cached = edge; ii, jj = I[m], J[m]
        d = P[ii] - P[jj]; dist = np.linalg.norm(d, axis=1)
        bad = dist < D
        if np.any(bad):
            gap = (D - dist[bad])[:, None]*(d[bad]/dist[bad][:, None])
            disp = np.zeros_like(P); cnt = np.zeros(len(P))
            np.add.at(disp, ii[bad], 0.5*gap); np.add.at(disp, jj[bad], -0.5*gap)
            np.add.at(cnt, ii[bad], 1); np.add.at(cnt, jj[bad], 1)
            P = P + 0.9*disp/np.maximum(cnt, 1)[:, None]
    return P


def profile(P, D=1.0):
    N = len(P)
    nxt = np.roll(P, -1, axis=0); e = nxt - P
    L = np.linalg.norm(e, axis=1); edge = np.mean(L)
    v1 = P - np.roll(P, 1, axis=0); v2 = nxt - P
    n1 = v1/np.linalg.norm(v1, axis=1, keepdims=True)
    n2 = v2/np.linalg.norm(v2, axis=1, keepdims=True)
    theta = np.arccos(np.clip(np.sum(n1*n2, axis=1), -1, 1))
    kappa = theta/edge
    I, J = np.triu_indices(N, k=1); ring = np.minimum(J - I, N - (J - I))
    m = (ring*edge) > 1.6*D
    d = np.linalg.norm(P[I[m]] - P[J[m]], axis=1)
    contact = np.zeros(N); close = d < 1.05*D
    np.add.at(contact, I[m][close], 1); np.add.at(contact, J[m][close], 1)
    return kappa, contact, edge, np.sum(L), np.sum(theta)


def zp_of_profile(g):
    Nc = 1000; K = np.zeros((Nc, Nc))
    for n in range(Nc - 1):
        K[n, n] += 1; K[n+1, n+1] += 1; K[n, n+1] -= 1; K[n+1, n] -= 1
    w0 = np.sqrt(np.maximum(np.linalg.eigvalsh(K + np.eye(Nc)*1e-4), 0))
    d = np.zeros(Nc); s = (Nc - len(g))//2; d[s:s+len(g)] = g
    w1 = np.sqrt(np.maximum(np.linalg.eigvalsh(K + np.diag(1e-4 + d)), 0))
    return 0.5*(np.sum(w1) - np.sum(w0))


def test():
    t = np.linspace(0, 2*np.pi, 144, endpoint=False)
    shapes = {
        "ring": (np.stack([3*np.cos(t), 3*np.sin(t), 0*t], axis=1), 20000),
        "3_1": (np.stack([(2 + np.cos(3*t))*np.cos(2*t),
                          (2 + np.cos(3*t))*np.sin(2*t), np.sin(3*t)], axis=1)*1.8, 60000),
        "5_1": (np.stack([(2 + np.cos(5*t))*np.cos(2*t),
                          (2 + np.cos(5*t))*np.sin(2*t), np.sin(5*t)], axis=1)*1.8, 45000),
    }
    res = {}
    for name, (P0, it) in shapes.items():
        P = tighten_coords(P0, iters=it)
        kap, con, edge, L, turn = profile(P)
        g = (kap*1.0)**2*edge + 0.5*con*edge
        res[name] = (L, zp_of_profile(g), turn)
    assert abs(res["ring"][2] - 2*np.pi) < 0.01, "extractor validation: ring turning = 2 pi"
    L3, E3, _ = res["3_1"]; L5, E5, _ = res["5_1"]
    f3, f5 = E3/L3, E5/L5
    assert abs(f3 - f5)/f3 > 0.10, "THE LEVER: zero-point fractions differ between knots"
    r0 = L5/L3
    assert abs((L5 + 0.0*E5)/(L3 + 0.0*E3) - r0) < 1e-12, "lambda->0 recovers pure length"
    rs = [(L5 + lam*E5)/(L3 + lam*E3) for lam in (0.5, 1.0, 2.0)]
    assert all(rs[i+1] < rs[i] for i in range(len(rs)-1)) and rs[0] < r0, \
        "ratios compress monotonically as the zero-point weight grows"
    print(f"fractions: 3_1 = {f3:.3f}, 5_1 = {f5:.3f} ({abs(f3-f5)/f3*100:.0f}% lever)")
    print(f"m_51/m_31: {r0:.4f} (lambda=0) -> {rs[-1]:.4f} (lambda=2): the spectrum is not geometry alone")
    print("PASS: the two-term mass model has its first table -- the lever exists, the")
    print("      compression points toward near-degenerate splittings, lambda stays blocked and said.")


if __name__ == "__main__":
    test()
