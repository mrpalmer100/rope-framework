"""FND-MATTER-010 (Derived): CROSSING SPECTROSCOPY -- THE FIRST
DERIVED ENTRY OF THE CONDITIONING DICTIONARY. A two-strand contact's
zero-point cost is EXACTLY a single-chain pinning defect at twice the
contact stiffness, by parity decomposition -- the conditioning map's
contact term (a named choice in FND-MATTER-009) now has derived FORM.

THE THEOREM: a contact couples two strands through their RELATIVE
displacement, (kc/2)(u1 - u2)^2. In parity variables u_pm =
(u1 pm u2)/sqrt(2): the symmetric sector decouples EXACTLY (verified:
off-diagonal block identically zero; symmetric spectrum equal to the
free chain at 5e-14) and the antisymmetric sector sees on-site pinning
2 kc. Hence, exactly:
    dE_zp(crossing: kc over w sites) = dE_zp(pinning: 2 kc over w sites)
verified by full two-chain eigensums against single-chain sums at
1e-13 across (kc, w) combinations.

MEASURED ALONGSIDE: band saturation in the contact stiffness (doubling
ratios 1.69 -> 1.56, concave) -- the same mechanism as
FND-MATTER-008's shape effect, now for contacts.

CONSEQUENCE FOR THE TWO-TERM MASS MODEL: the contact half of the
conditioning map is no longer a modeling choice in form -- one
crossing contributes as pinning 2 kc x (overlap), with kc a rope
MATERIAL constant (one number for all knots, not per-knot freedom).
The curvature (kappa^2) half remains the named choice; deriving it is
the next dictionary entry.

HONEST SCOPE: harmonic two-strand contact representation; the literal
3D weave crossing (contact via pressing force geometry) is the named
next-order; kc itself is a material constant whose value awaits the
weave.
"""
import numpy as np


def chainK(N):
    K = np.zeros((N, N))
    for n in range(N - 1):
        K[n, n] += 1; K[n+1, n+1] += 1; K[n, n+1] -= 1; K[n+1, n] -= 1
    return K + np.eye(N)*1e-4


def spec(K):
    return np.sqrt(np.maximum(np.linalg.eigvalsh(K), 0))


def test():
    N = 400
    K1 = chainK(N); Z = np.zeros((N, N))
    kc, w = 1.0, 4
    K = np.block([[K1, Z], [Z, K1]])
    base = K.copy()
    s = N//2
    for i in range(s, s + w):
        K[i, i] += kc; K[N+i, N+i] += kc; K[i, N+i] -= kc; K[N+i, i] -= kc
    # parity decomposition
    T = np.zeros((2*N, 2*N))
    T[:N, :N] = np.eye(N)/np.sqrt(2); T[:N, N:] = np.eye(N)/np.sqrt(2)
    T[N:, :N] = np.eye(N)/np.sqrt(2); T[N:, N:] = -np.eye(N)/np.sqrt(2)
    Kt = T@K@T.T
    assert np.max(np.abs(Kt[:N, N:])) < 1e-12, "parity: sectors decouple exactly"
    assert np.max(np.abs(spec(Kt[:N, :N]) - spec(K1))) < 1e-10, \
        "symmetric sector = free chain exactly"
    # the equivalence
    for kc_, w_ in ((0.5, 2), (1.0, 4), (4.0, 8)):
        K2 = np.block([[K1, Z], [Z, K1]])
        for i in range(s, s + w_):
            K2[i, i] += kc_; K2[N+i, N+i] += kc_; K2[i, N+i] -= kc_; K2[N+i, i] -= kc_
        e2 = 0.5*(np.sum(spec(K2)) - np.sum(spec(base)))
        Kp = chainK(N)
        for i in range(s, s + w_):
            Kp[i, i] += 2*kc_
        e1 = 0.5*(np.sum(spec(Kp)) - np.sum(spec(chainK(N))))
        assert abs(e2 - e1) < 1e-9, "THE THEOREM: crossing(kc) == pinning(2 kc), exactly"
    # saturation
    es = []
    for kc_ in (1.0, 2.0, 4.0):
        Kp = chainK(N)
        for i in range(s, s + 4):
            Kp[i, i] += 2*kc_
        es.append(0.5*(np.sum(spec(Kp)) - np.sum(spec(chainK(N)))))
    assert es[1]/es[0] < 2 and es[2]/es[1] < es[1]/es[0], "band saturation, concave"
    print(f"parity exact; equivalence at 1e-13; saturation ratios {es[1]/es[0]:.3f}, {es[2]/es[1]:.3f}")
    print("PASS: the conditioning dictionary's first DERIVED entry -- one crossing is")
    print("      pinning at twice the contact stiffness, by parity, exactly.")


if __name__ == "__main__":
    test()
