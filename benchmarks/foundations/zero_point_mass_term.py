"""FND-MATTER-008 (Modeled): THE ZERO-POINT MASS TERM, FIRST
MEASUREMENT -- the fence's named layer (quantum kinetic / zero-point
energy, FND-BOUND-001) instrumented for the first time inside the
corpus, and the 1836 fork's energetics branch measured LIVE.

THE OBJECT: a knot conditions the medium around it; a conditioned
region shifts every wave mode of the weave; so a knot carries a
Casimir-class zero-point self-energy dE_zp = (1/2) sum(omega') -
(1/2) sum(omega), computed here EXACTLY by eigenvalue sums (the
lattice band is the regulator; no divergences, no scheme).

MEASURED:
(B1) EXACT AND CONVERGED: stable to 3e-7 under doubling N.
(B2) BULK PLUS SURFACE: dE_zp(w) = A w - B (doubling ratios marching
     to 2 from below) -- a per-length term plus a measured negative
     boundary correction.
(B3) THE VERDICT: equal-length, equal-total-strength defects of
     different SHAPE differ by 43 percent (uniform 5.62 vs
     edge-concentrated 3.19 at w = 16) -- far beyond the 5 percent
     verdict bar. MASS IS NOT PURE LENGTH wherever zero-point terms
     contribute: mass ratios need not equal length ratios, and the
     thousand-crossing arithmetic of FND-MATTER-007 is NOT binding.
(B4) THE MECHANISM: sublinear strength-scaling (x4 strength gives
     x2.7-2.9 energy -- band saturation), which is exactly why
     concentration matters: spreading conditioning shifts more modes.

WHAT THIS DOES NOT SETTLE, at full volume: the RELATIVE weight of the
zero-point term against the static tension-length term requires the
absolute scale -- blocked at FND-MATTER-003 and honestly still so. The
geometry branch (a large-tangle proton) is NOT excluded; what is
established is that the energetics branch EXISTS, is exactly
computable, and is strongly structural. The fork stands, now with both
tines instrumented.
"""
import numpy as np


def zp(N, defect):
    def spec(dvec):
        K = np.zeros((N, N))
        for n in range(N - 1):
            K[n, n] += 1; K[n+1, n+1] += 1; K[n, n+1] -= 1; K[n+1, n] -= 1
        K += np.diag(1e-4 + dvec)
        return np.sqrt(np.maximum(np.linalg.eigvalsh(K), 0))
    d1 = np.zeros(N)
    for i, v in defect:
        d1[i] += v
    return 0.5*(np.sum(spec(d1)) - np.sum(spec(np.zeros(N))))


def test():
    mk = lambda N, c, w, g: [(c + k, g) for k in range(w)]
    e1 = zp(600, mk(600, 300, 8, 2.0))
    e2 = zp(1200, mk(1200, 600, 8, 2.0))
    assert abs(e1 - e2)/abs(e2) < 1e-3, "B1: exact and N-converged"
    N = 1200
    es = [zp(N, mk(N, N//2, w, 2.0)) for w in (4, 8, 16, 32)]
    ratios = [es[i+1]/es[i] for i in range(3)]
    assert all(r < 2.0 for r in ratios) and ratios[-1] > ratios[0], \
        "B2: bulk-plus-surface -- sub-extensive, ratios marching to 2 from below"
    w = 16; gtot = 32.0
    e_uni = zp(N, mk(N, N//2, w, gtot/w))
    e_edge = zp(N, [(N//2, gtot/2), (N//2 + w - 1, gtot/2)])
    assert abs(e_uni - e_edge)/e_uni > 0.20, \
        "B3: THE VERDICT -- equal length, different shape, different mass term"
    ga = zp(N, mk(N, N//2, 8, 2.0)); gb = zp(N, mk(N, N//2, 8, 8.0))
    assert gb/ga < 3.5, "B4: sublinear strength-scaling (band saturation)"
    print(f"B1: {abs(e1-e2)/abs(e2):.1e} converged; B2 ratios: " + " ".join(f"{r:.3f}" for r in ratios))
    print(f"B3: uniform {e_uni:.3f} vs edge {e_edge:.3f} -- {abs(e_uni-e_edge)/e_uni*100:.0f}% shape effect")
    print(f"B4: x4 strength -> x{gb/ga:.2f} energy (saturation)")
    print("PASS: the zero-point mass term measured -- mass is not pure length; the 1836")
    print("      arithmetic is not binding; the fork stands with both tines instrumented.")


if __name__ == "__main__":
    test()
