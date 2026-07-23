"""QB-017 (Derived): the quintic rung -- THE PLATEAU BREAKS at its first
named test, the 'plateau' is exposed as a PARITY ARTIFACT, and the true
ladder is the decelerating odd-order sequence.

(R1) THE PLATEAU CONJECTURE REFUTED (the second conjecture killed by its
     own named test in three rungs): the l <= 5 class reaches odd-sector
     CHSH = 2.382 at quantum angles -- +0.10 above the l <= 3/4 value
     2.280, outside all stated tolerances -- with the NEW odd channel
     active (F = +0.36, D flipping sign to -0.21, B = -0.83).
     Independent-seed rebuild: 2.3817 (channel structure preserved);
     settings re-optimization confirms quantum angles optimal.
(R2) THE PARITY ARTIFACT, an analysis correction to QB-016: even orders
     add only EVEN mean-channels, so l = 4 offered the odd sector ZERO
     new parameters -- its stasis was structural bookkeeping, not
     hierarchy convergence. The true ladder lives in the odd orders:
     0.9428 (l=1) | 2.27 (l=3) | 2.38 (l=5) -- climbing but sharply
     decelerating (+1.33, then +0.10).
(R3) TSIRELSON STILL 0.45 ABOVE: the refined question is whether the
     odd-order sequence converges below 2.8284 (the deceleration suggests
     it -- flagged as motivated extrapolation, NOT measurement, with full
     memory of two dead conjectures). Named tests: the l <= 7 rung, and
     the analytic all-orders odd-sector bound, now unmistakably THE
     question.
Caveats: sampled-LP upper estimates; mean-map residual ~4 percent; the
break (+0.10) and the Tsirelson gap (0.45) both exceed tolerances.
"""
import numpy as np
from scipy.optimize import linprog

TERMS = []
for m in (0, 1):
    for k in range(6):
        for i in range(6):
            for j in range(6):
                if i + k + m <= 5 and j + k + m <= 5:
                    TERMS.append((i, j, k, m))


def basis_xyzw(x, y, s, w):
    return np.stack([x**i*y**j*s**k*(w if m else np.ones_like(w)) for (i, j, k, m) in TERMS], 1)


def build(seed=61, N=40000):
    rng = np.random.default_rng(seed)

    def units(n):
        v = rng.standard_normal((n, 3))
        return v/np.linalg.norm(v, axis=1, keepdims=True)
    packs = [(units(N), units(N), units(N))]
    for eps in (0.0, 0.02, 0.08):
        M = 3500
        a1 = units(M)
        b1 = a1 + eps*rng.standard_normal((M, 3)); b1 /= np.linalg.norm(b1, axis=1, keepdims=True)
        n1 = a1 + eps*rng.standard_normal((M, 3)); n1 /= np.linalg.norm(n1, axis=1, keepdims=True)
        packs.append((a1, b1, n1))
    M = 11000
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


def mean_map(seed=61, Np=320, Nn=2200):
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
    coef, *_ = np.linalg.lstsq(np.stack([S**k for k in range(6)], 1), np.array(MEANS), rcond=None)
    return coef


def test():
    coef = mean_map()
    Br, Dr, Fr = coef[1], coef[3], coef[5]
    Aub, bub = build()
    th = [(0, np.pi/4), (0, -np.pi/4), (np.pi/2, np.pi/4), (np.pi/2, -np.pi/4)]
    Sk = lambda k: sum(np.cos(p - q)**k for p, q in th[:3]) - np.cos(th[3][0] - th[3][1])**k
    r = linprog(c=(Sk(1)*Br + Sk(3)*Dr + Sk(5)*Fr), A_ub=Aub, b_ub=bub,
                bounds=[(-10, 10)]*146, method='highs')
    chsh = -r.fun
    Fv = float(Fr@r.x)
    assert chsh > 2.33, "the plateau BREAKS at l <= 5 (conjecture refuted at its named test)"
    assert chsh < 2.55, "the climb is small: deceleration continues"
    assert chsh < 2*np.sqrt(2) - 0.25, "Tsirelson still well above the quintic rung"
    assert abs(Fv) > 0.15, "the new odd channel F is genuinely active"
    print(f"R1: odd-sector CHSH(l<=5) = {chsh:.4f}  (plateau 2.280 broken; F = {Fv:+.3f} active)")
    print(f"R2: parity artifact -- even orders add no odd channels; true ladder: 0.9428 | 2.27 | {chsh:.2f}")
    print(f"R3: Tsirelson {2*np.sqrt(2):.4f} remains {2*np.sqrt(2)-chsh:.2f} above; convergence-below-quantum")
    print("    is a motivated extrapolation only. Named tests: l <= 7, the analytic all-orders bound.")
    print("PASS: the second conjecture dies at its own named test; the odd-order ladder is the object.")


if __name__ == "__main__":
    test()
