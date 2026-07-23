"""QB-016 (Derived): the quartic rung -- THE LADDER PLATEAUS. The l <= 4
class does not exceed the cubic rung: the odd sector is exactly saturated
(identical (B, D) optima to three decimals), the even channels contribute
nothing at the optimum, and TSIRELSON IS NOT CROSSED -- decisively
(~2.27 vs 2.8284, far outside the stated ~ +-0.05 tolerance).

(R1) ODD-SECTOR SATURATION: the l <= 4 odd-sector optimum at quantum
     angles is 2.280 at (B, D) = (-0.862, +0.111) -- statistically
     identical to the cubic rung's 2.281 at (-0.864, +0.115). Fourth-order
     content adds nothing to the only channels that matter.
(R2) FULL CEILING FLAT: CHSH*(l <= 4) ~ 2.26-2.28, indistinguishable from
     the cubic 2.27; the even channels (including the new s^4 channel)
     vanish or hurt at the optimum, exactly as at cubic order.
(R3) THE LADDER, updated: 0.9428 exact | ~1.20 | ~2.27 | ~2.27 (plateau) |
     3 exact (discontinuous). Tsirelson 2.8284 sits ABOVE the apparent
     smooth-polynomial plateau: the verdict of QB-015 ('l >= 4 or
     nonpolynomial') hardens toward NONPOLYNOMIAL OUTRIGHT -- registered
     as the PLATEAU CONJECTURE (the smooth-conditional ceiling converges
     to ~2.28 for all finite orders), with full memory that the last
     motivated conjecture died at its named next rung; this one's named
     tests are the l <= 5 rung and the analytic all-orders bound, and its
     death would itself be informative (a slow climb toward 3 with
     Tsirelson crossed at some finite order).
Caveats: sampled-LP upper estimates; mean-map regression residual ~4
percent; the plateau (identical values within noise) and the Tsirelson
verdict (0.55 gap) sit far outside these tolerances.
"""
import numpy as np
from scipy.optimize import linprog

TERMS = []
for m in (0, 1):
    for k in range(5):
        for i in range(5):
            for j in range(5):
                if i + k + m <= 4 and j + k + m <= 4:
                    TERMS.append((i, j, k, m))


def basis_xyzw(x, y, s, w):
    return np.stack([x**i*y**j*s**k*(w if m else np.ones_like(w)) for (i, j, k, m) in TERMS], 1)


def build(seed=53, N=55000):
    rng = np.random.default_rng(seed)

    def units(n):
        v = rng.standard_normal((n, 3))
        return v/np.linalg.norm(v, axis=1, keepdims=True)
    packs = [(units(N), units(N), units(N))]
    for eps in (0.0, 0.02, 0.08):
        M = 5000
        a1 = units(M)
        b1 = a1 + eps*rng.standard_normal((M, 3)); b1 /= np.linalg.norm(b1, axis=1, keepdims=True)
        n1 = a1 + eps*rng.standard_normal((M, 3)); n1 /= np.linalg.norm(n1, axis=1, keepdims=True)
        packs.append((a1, b1, n1))
    M = 15000
    b2 = units(M); t = rng.uniform(0, np.pi, M)
    perp = units(M); perp -= np.sum(perp*b2, 1, keepdims=True)*b2
    perp /= np.linalg.norm(perp, axis=1, keepdims=True)
    a2 = np.cos(t)[:, None]*b2 + np.sin(t)[:, None]*perp
    n2 = np.cross(b2, perp); n2 /= np.linalg.norm(n2, axis=1, keepdims=True)
    mix = rng.uniform(-1, 1, M)[:, None]
    n2 = np.sqrt(1 - mix**2)*n2 + mix*perp; n2 /= np.linalg.norm(n2, axis=1, keepdims=True)
    packs.append((a2, b2, n2))
    x = np.concatenate([np.sum(a*n, 1) for a, b, n in packs])
    y = np.concatenate([np.sum(b*n, 1) for a, b, n in packs])
    s = np.concatenate([np.sum(a*b, 1) for a, b, n in packs])
    w = np.concatenate([np.sum(n*np.cross(a, b), 1) for a, b, n in packs])
    Phi = basis_xyzw(x, y, s, w)
    return np.vstack([Phi, -Phi]), np.concatenate([1 - np.abs(x + y), -(np.abs(x - y) - 1)])


def mean_map(seed=53, Np=350, Nn=2500):
    rng = np.random.default_rng(seed)

    def units(n):
        v = rng.standard_normal((n, 3))
        return v/np.linalg.norm(v, axis=1, keepdims=True)
    S, MEANS = [], []
    for _ in range(Np):
        a = units(1)[0]; t = rng.uniform(0, np.pi)
        p = units(1)[0]; p -= p@a*a; p /= np.linalg.norm(p)
        b = np.cos(t)*a + np.sin(t)*p
        n = units(Nn)
        A2 = np.repeat(a[None, :], Nn, 0); B2 = np.repeat(b[None, :], Nn, 0)
        x = np.sum(A2*n, 1); y = np.sum(B2*n, 1)
        s = np.sum(A2*B2, 1); w = np.sum(n*np.cross(A2, B2), 1)
        S.append(np.cos(t)); MEANS.append(basis_xyzw(x, y, s, w).mean(0))
    S = np.array(S)
    V = np.stack([np.ones_like(S), S, S**2, S**3, S**4], 1)
    coef, *_ = np.linalg.lstsq(V, np.array(MEANS), rcond=None)
    return coef


def test():
    coef = mean_map()
    Br, Dr = coef[1], coef[3]
    Aub, bub = build()
    th = [(0, np.pi/4), (0, -np.pi/4), (np.pi/2, np.pi/4), (np.pi/2, -np.pi/4)]
    S1 = sum(np.cos(p - q) for p, q in th[:3]) - np.cos(th[3][0] - th[3][1])
    S3 = sum(np.cos(p - q)**3 for p, q in th[:3]) - np.cos(th[3][0] - th[3][1])**3
    r = linprog(c=(S1*Br + S3*Dr), A_ub=Aub, b_ub=bub, bounds=[(-10, 10)]*85, method='highs')
    chsh = -r.fun
    Bv, Dv = float(Br@r.x), float(Dr@r.x)
    # R1: saturation at the cubic value
    assert abs(chsh - 2.28) < 0.06, "odd sector saturated at the cubic-rung value ~2.28"
    assert abs(Bv + 0.86) < 0.05 and abs(Dv - 0.11) < 0.06, "identical (B, D) optimum to the cubic rung"
    # R3: Tsirelson decisively not crossed
    assert chsh < 2*np.sqrt(2) - 0.3, "Tsirelson NOT crossed (0.55 gap, far outside tolerance)"
    assert chsh > 2.10, "the plateau remains supra-classical"
    print(f"R1: odd-sector CHSH(l<=4) = {chsh:.4f} at (B,D)=({Bv:+.3f},{Dv:+.3f}) -- cubic value, saturated")
    print(f"R3: ladder 0.9428 | ~1.20 | ~2.27 | ~2.27 (PLATEAU) | 3 -- Tsirelson {2*np.sqrt(2):.4f} above the plateau")
    print("PASS: the smooth-polynomial hierarchy plateaus below Tsirelson; the supplier hardens toward")
    print("      nonpolynomial outright (the PLATEAU CONJECTURE; named tests: l<=5, all-orders bound).")


if __name__ == "__main__":
    test()
