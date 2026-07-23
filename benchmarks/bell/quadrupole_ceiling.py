"""QB-014 (Derived): the quadrupole rung -- the window opens by a quarter,
the linear channel stays rigid, and the harmonic ladder becomes the wall's
fine structure.

Extending QB-013's class to full isotropic covariance of degree <= 2 in
each setting vector (17 basis terms), the uniform-n average collapses to
E(s) = A + B s + C s^2, and the pointwise-Frechet feasible set K in
(A, B, C) is probed by support LPs:

(R1) THE WINDOW OPENS, BARELY: CHSH*(l <= 2) = 1.20 (density-stable to
     0.5 percent: 1.2016 at 100k rows, 1.1965 at 300k), vs the dipole
     class's rigid 0.943 -- quadrupole content buys ~27 percent, entirely
     through the constant (A in [-0.11, +0.10]) and quadratic
     (C in [-0.22, +0.21]) channels.
(R2) THE LINEAR CHANNEL STAYS RIGID: across ALL 56 support directions and
     all quadrupole freedom, B remains pinned in [-0.339, -0.327] --
     essentially -1/3, the QB-013 dipole value. The only Tsirelson-relevant
     channel (CHSH grows through B at the quantum angles) is untouched by
     second-order content; the analytic forcing families of QB-013
     evidently continue to bind the linear part (measured; the
     all-orders extension of the forcing argument is the named open
     question).
(R3) THE LADDER, as measured: l <= 1: 0.9428 (exact, rigid);
     l <= 2: ~1.20; unrestricted: 3 (exact, QB-012). The quadrupole class
     cannot reach even the classical 2 (deterministic sign strategies are
     nonpolynomial and live outside every finite-l smooth class -- no
     paradox). The specification's fifth clause sharpens: the supplier
     needs response order l >= 3 or nonpolynomial setting dependence, and
     if B-pinning at -1/3 persists at all polynomial orders (the
     conjecture this measurement motivates), the linear channel is closed
     to ALL smooth conditionals and quantum correlations require
     nonpolynomial structure outright.
Sampled-LP caveat stated: finite sampling relaxes constraints, so values
are upper estimates, decreasing under densification (1.2016 -> 1.1965).
"""
import numpy as np
from scipy.optimize import linprog


IDX = dict(c0=0, anbn=4, ab=3, an2=6, bn2=7, a2b2=12, ab2=13, abanbn=14, cr2=15)
Ar = np.zeros(17); Br = np.zeros(17); Cr = np.zeros(17)
Ar[IDX['c0']] = 1; Ar[IDX['an2']] = 1/3; Ar[IDX['bn2']] = 1/3
Ar[IDX['a2b2']] = 1/15; Ar[IDX['cr2']] = 1/3
Br[IDX['ab']] = 1; Br[IDX['anbn']] = 1/3
Cr[IDX['a2b2']] = 2/15; Cr[IDX['ab2']] = 1; Cr[IDX['abanbn']] = 1/3; Cr[IDX['cr2']] = -1/3


def build(N, seed=23):
    rng = np.random.default_rng(seed)

    def units(n):
        v = rng.standard_normal((n, 3))
        return v/np.linalg.norm(v, axis=1, keepdims=True)
    a, b, n = units(N), units(N), units(N)
    M = N//4
    a2 = units(M)
    n2 = a2 + 0.05*rng.standard_normal((M, 3)); n2 /= np.linalg.norm(n2, axis=1, keepdims=True)
    b2 = a2 + 0.1*rng.standard_normal((M, 3)); b2 /= np.linalg.norm(b2, axis=1, keepdims=True)
    a = np.vstack([a, a2]); b = np.vstack([b, b2]); n = np.vstack([n, n2])
    an = np.sum(a*n, 1); bn = np.sum(b*n, 1); ab = np.sum(a*b, 1); cr = np.sum(n*np.cross(a, b), 1)
    Phi = np.stack([np.ones_like(ab), an, bn, ab, an*bn, cr, an**2, bn**2, an**2*bn, an*bn**2,
                    ab*an, ab*bn, an**2*bn**2, ab**2, ab*an*bn, cr**2, cr*ab], 1)
    return np.vstack([Phi, -Phi]), np.concatenate([1 - np.abs(an + bn), -(np.abs(an - bn) - 1)])


def test():
    Aub, bub = build(40000)
    # the near-optimal settings direction (from the full-settings search)
    al, b0, b1 = 1.05, 3.67, 2.62
    S1 = np.cos(b0) + np.cos(b1) + np.cos(al - b0) - np.cos(al - b1)
    S2 = np.cos(b0)**2 + np.cos(b1)**2 + np.cos(al - b0)**2 - np.cos(al - b1)**2
    r = linprog(c=-(2*Ar + S1*Br + S2*Cr), A_ub=Aub, b_ub=bub,
                bounds=[(-10, 10)]*17, method='highs')
    chsh = -r.fun
    Bv = float(Br@r.x)
    # R1: the window opens beyond dipole, stays far below classical
    assert 1.10 < chsh < 1.30, "quadrupole ceiling ~1.20"
    assert chsh > 2*np.sqrt(2)/3 + 0.15, "the window OPENS beyond the rigid dipole value"
    assert chsh < 2.0, "the quadrupole class cannot reach classical"
    # R2: linear-channel rigidity persists
    assert abs(Bv + 1/3) < 0.02, "B pinned at -1/3 under full quadrupole freedom"
    # B-pinning across probe directions
    for w in ([1, 0, 0], [0, 0, 1], [1, -1, 1], [-1, -1, -1]):
        rr = linprog(c=-(w[0]*Ar + w[1]*Br + w[2]*Cr), A_ub=Aub, b_ub=bub,
                     bounds=[(-10, 10)]*17, method='highs')
        assert abs(float(Br@rr.x) + 1/3) < 0.02, "B rigid in every probed support direction"
    print(f"R1: CHSH*(l<=2) = {chsh:.4f}  (dipole 0.9428 < this < classical 2)")
    print(f"R2: B = {Bv:+.4f} -- the linear channel rigid at -1/3 under all quadrupole freedom")
    print("R3: the ladder -- l<=1: 0.9428 exact | l<=2: ~1.20 | unrestricted: 3 exact")
    print("PASS: the harmonic ladder is the wall's fine structure; the supplier needs l >= 3")
    print("      or nonpolynomial setting dependence; the linear channel may be closed to all")
    print("      smooth conditionals (the conjecture this measurement motivates).")


if __name__ == "__main__":
    test()
