"""FND-STRAND-004 (Modeled): TANGIBILITY EMERGES ON THE ENGINE -- Phase 3:
the FND-MATTER-004 coverage threshold reproduced on literal strands.

Setup: a straight probe strand is passed through a square brush of M x M
parallel strands at spacing d, all interactions through the corpus's
FINITE contact form Ac/(1 + (r/sigma)^4) -- the interpenetration
primitive is intact: every barrier in this benchmark is finite, and
'solid' is a statement about heights, never about prohibitions.

(B1) THE PRIMITIVE: a single strand-strand crossing costs a finite
     barrier of order Ac -- one strand passes anything, at a price.
(B2) EMERGENT SOLIDITY: the pass-through barrier vs brush spacing spans
     more than three orders of magnitude, monotone -- a sparse brush is
     effectively transparent (barrier << drive scales), a dense brush
     effectively solid (barrier ~ M-fold Ac) -- tangibility as a smooth
     emergent property of coverage, on actual strands.
(B3) THE THRESHOLD IS GEOMETRIC AND ORDER-UNITY: the crossover (barrier
     = 1 in Ac units) sits at gap ~ sigma -- coverage of order one in
     contact-radius units, the same threshold structure FND-MATTER-004
     used at the field level to fix N ~ 3e11. The fidelity chain closes:
     single strands interpenetrate; bundles at order-unity coverage do
     not (in practice); no crossing axiom anywhere.
"""
import numpy as np


def barrier(d, M=7, sig=0.12, Ac=1.0, Lprobe=2.0):
    """penetration barrier for a probe strand PARALLEL to an M x M brush
    (spacing d), slipping lengthwise through a gap: pushed in z from well
    outside to the slab center at mid-gap x = d/2. Strand lines along y at
    (x_i, z_j); distance is y-independent, so E = Lprobe * sum of contact."""
    xs = (np.arange(M) - M//2)*d
    zs = (np.arange(M) - M//2)*d
    z0s = np.linspace(-(M/2*d + 10*sig), 0.0, 201)
    Es = []
    for z0 in z0s:
        r = np.sqrt((d/2 - xs[:, None])**2 + (z0 - zs[None, :])**2) + 1e-12
        Es.append(Lprobe*np.sum(Ac/(1 + (r/sig)**4)))
    Es = np.array(Es)
    return float(Es.max() - Es[0])


def test():
    sig = 0.12
    # B1: single crossing finite ~ Ac scale (head-on: strand at origin)
    seg = np.linspace(-3, 3, 400); ds = seg[1] - seg[0]
    z0s = np.linspace(-2, 2, 201)
    Eh = np.array([np.sum(1.0/(1 + ((np.sqrt(seg**2 + z0**2) + 1e-12)/sig)**4))*ds
                   for z0 in z0s])
    b1 = float(Eh.max() - Eh.min())
    assert 0.01 < b1 < 5.0, "single crossing: finite, order-Ac (the primitive)"
    # B2: coverage sweep
    dd = np.array([1.0, 1.5, 2.0, 3.0, 4.5, 6.0, 8.0])*sig*2
    bs = np.array([barrier(d) for d in dd])
    assert np.all(np.diff(bs) < 0), "barrier monotone decreasing with spacing"
    assert bs[0]/bs[-1] > 1e3, "spans > 3 orders: transparent to solid"
    # B3: threshold at gap ~ sigma (order-unity coverage)
    # crossover where barrier = 1 (Ac units)
    i = int(np.argmin(np.abs(np.log(bs) - 0.0)))
    gap_star = dd[i]/2 - 0*sig
    assert 0.5*sig < gap_star < 6*sig, "crossover gap of order sigma: coverage O(1)"
    print(f"B1 single crossing barrier = {b1:.3f} (finite; the primitive intact)")
    for d, b in zip(dd, bs):
        print(f"  spacing d = {d/sig:4.1f} sigma: pass-through barrier = {b:9.3e}")
    print(f"B3 crossover at gap ~ {gap_star/sig:.1f} sigma -- order-unity coverage,")
    print("   the FND-MATTER-004 threshold structure on literal strands.")
    print("PASS: tangibility emerges on the engine -- solid is a height, not a rule.")


if __name__ == "__main__":
    test()
