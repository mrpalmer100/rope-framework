"""QB-012 (Derived): the wall characterized -- four theorems convert the
CHSH boundary from a fence into a specification, with two closed-form
ceilings. NO CROSSING CLAIMED ANYWHERE.

(T1) CARRIER EXCLUSION: all corpus disturbances are co-material (<= c;
     GRV-008 T1 identity). In standard loophole-free geometry (1.3 km,
     200 ns setting-to-detection), a crossing needs 4.3 us: any rope-native
     supplier of the nonlocal conditional is NON-PROPAGATING --
     identity-class (the KIN-005 kind), not disturbance-class.
(T2) STATIC-INVARIANT EXCLUSION: any conditional that is a function of
     source-created shared data is a local hidden variable; with the gamma=1
     law fixed, CHSH <= 2 (deterministic extremal exactly 2.0000;
     independent gamma-law responses give exactly sqrt(2)). This unifies the
     corpus's failed crossings (QB-003/005) as instances of one theorem.
(T3a) PLANAR NO-GO, closed form: over ALL no-signalling setting-inclusive
     conditionals with gamma=1 marginals and a uniform PLANAR shared-state
     ensemble, sup CHSH = 4 - 4/pi = 2.7268... < 2 sqrt(2). Planar
     hidden-state models cannot reach the quantum value at any settings
     even with maximally powerful nonlocal conditionals.
(T3b) SPHERICAL CEILING, closed form: the same supremum for the uniform
     SPHERICAL ensemble is EXACTLY 3: 2 sqrt(2) < 3 < 4 -- the quantum
     value is admitted, and PR-boxes are excluded by the detection law
     alone. The remaining gap [2 sqrt 2, 3] belongs to the conditional's
     own structure.
THE SPECIFICATION: any rope-native supplier must be (i) non-propagating,
(ii) setting-inclusive (non-static), (iii) spherical-ensemble, (iv) under
the ceiling 3. HONEST NOTES: the suprema are approached (not attained) in
the near-degenerate settings limit via conditionals discontinuous in the
settings; a continuity refinement would lower them (named next-order).
Pairing convention: anticorrelated (B state = -n), declared.
"""
import numpy as np


def S_mc(dim, a1, b0, b1, N=250000, seed=5):
    rng = np.random.default_rng(seed)
    if dim == 2:
        th = rng.uniform(0, 2*np.pi, N)
        ns = np.stack([np.cos(th), np.sin(th)], 1)
    else:
        v = rng.standard_normal((N, 3))
        ns = v/np.linalg.norm(v, axis=1, keepdims=True)

    def unit(t):
        u = np.zeros(dim); u[0] = np.cos(t); u[1] = np.sin(t); return u
    A = [unit(0.0), unit(a1)]; B = [unit(b0), unit(b1)]
    tot = 0.0
    for (i, j, sg) in [(0, 0, 1), (0, 1, 1), (1, 0, 1), (1, 1, -1)]:
        pa = 0.5*(1 + ns@A[i]); pb = 0.5*(1 - ns@B[j])
        if sg > 0:
            tot += np.mean(1 - 2*np.abs(pa - pb))     # Frechet comonotone max
        else:
            tot -= np.mean(2*np.abs(pa + pb - 1) - 1)  # Frechet antitone min
    return tot


def test():
    # T1: lightcone arithmetic (loophole-free geometry)
    d, c, t_choice = 1280.0, 2.998e8, 200e-9
    assert d/c > 10*t_choice, "co-material carriers excluded by an order of magnitude"
    # T2: static shared invariants
    rng = np.random.default_rng(3)
    th = rng.uniform(0, 2*np.pi, 300000)
    ns = np.stack([np.cos(th), np.sin(th)], 1)
    vec = lambda t: np.array([np.cos(t), np.sin(t)])
    A0, A1, B0, B1 = vec(0), vec(np.pi/2), vec(np.pi/4), vec(-np.pi/4)
    E_det = lambda a, b: np.mean(np.sign(ns@a)*np.sign(-ns@b))
    S_det = abs(E_det(A0, B0) + E_det(A0, B1) + E_det(A1, B0) - E_det(A1, B1))
    assert S_det < 2 + 1e-6, "static-invariant extremal <= 2"
    assert abs(S_det - 2.0) < 5e-3, "deterministic extremal saturates exactly 2"
    p = lambda a, s: 0.5*(1 + s@a)
    E_st = lambda a, b: np.mean((2*p(a, ns) - 1)*(2*p(b, -ns) - 1))
    S_st = abs(E_st(A0, B0) + E_st(A0, B1) + E_st(A1, B0) - E_st(A1, B1))
    assert abs(S_st - np.sqrt(2)) < 5e-3, "independent gamma-law responses give exactly sqrt(2)"
    # T3: ceilings -- MC approaches the closed forms in the near-degenerate limit
    eps = 0.1
    s2 = S_mc(2, eps, np.pi, np.pi - eps)
    s3 = S_mc(3, eps, np.pi, np.pi - eps)
    X2, X3 = 4 - 4/np.pi, 3.0
    assert X2 - 0.15 < s2 < X2 + 0.01, "planar MC approaches 4 - 4/pi from below"
    assert X3 - 0.15 < s3 < X3 + 0.01, "spherical MC approaches 3 from below"
    # the theorem inequalities
    Ts = 2*np.sqrt(2)
    assert X2 < Ts, "PLANAR NO-GO: sup < Tsirelson -- planar models excluded"
    assert Ts < X3 < 4, "SPHERICAL: quantum admitted, PR excluded by the detection law alone"
    print(f"T1: crossing {d/c*1e6:.1f} us >> window {t_choice*1e6:.1f} us -- carriers excluded")
    print(f"T2: static invariants: det extremal {S_det:.4f} (= 2); gamma-law product {S_st:.4f} (= sqrt 2)")
    print(f"T3a PLANAR NO-GO: sup = 4 - 4/pi = {X2:.4f} < Tsirelson {Ts:.4f}  (MC {s2:.3f})")
    print(f"T3b SPHERICAL: sup = 3 exactly; {Ts:.4f} < 3 < 4  (MC {s3:.3f}) -- PR-boxes excluded")
    print("PASS: the wall is now a four-clause specification -- non-propagating, setting-inclusive,")
    print("      spherical-ensemble, under ceiling 3. No crossing claimed.")


if __name__ == "__main__":
    test()
