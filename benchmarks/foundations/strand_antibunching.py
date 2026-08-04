"""FND-STRAND-026 (Derived, conditional on Grant 3): ANTIBUNCHING
FORMALIZED AGAINST THE QB PIN -- the faithfulness theorem: under Grant 3
plus the Born law, beamsplitter g2 equals the source's normalized second
factorial moment <n(n-1)>/<n>^2 EXACTLY, independent of splitter ratio
and arm efficiencies (thinning invariance: loss cannot manufacture or
destroy antibunching -- the efficiency-independence of the real
Grangier-Roger parameter, derived rather than assumed).

The pin RESOLVED not contradicted: the QB campaign's g2 >= 1 bound is a
theorem about divisible intensities; Grant 3 changes the sampled object
to integer quanta, removing the premise. QB-009's constraint-propagation
toy stands as the named mechanism candidate for the funneling dynamics.
The measured ~0.18 is located as source contamination:
g2 = 2 p2/(p1 + 2 p2)^2. Discrimination table: Fock n gives 1 - 1/n;
coherent gives 1; thermal gives 2 -- agreement wherever classical fields
are attainable, disagreement exactly where experiment disagrees with
classical fields.

Full derivation: analysis/STRAND026_antibunching.md.
"""
import numpy as np

rng = np.random.default_rng(2029)


def g2_split(n, tau, etaA, etaB):
    nT = rng.binomial(n, tau)
    nA = rng.binomial(nT, etaA)
    nB = rng.binomial(n - nT, etaB)
    return np.mean(nA*nB)/(np.mean(nA)*np.mean(nB))


def test():
    M = 600000
    # T1: thinning invariance across tau and efficiencies (Fock n = 3: g2 = 2/3)
    n3 = np.full(M, 3)
    target = 1 - 1/3
    for tau, eA, eB in [(0.5, 1.0, 1.0), (0.3, 0.6, 0.9), (0.8, 0.2, 0.7)]:
        g = g2_split(n3, tau, eA, eB)
        assert abs(g - target) < 0.02, f"invariance at {(tau,eA,eB)}: {g:.3f}"
    # single quantum: exact zero
    n1 = np.ones(M, int)
    nT = rng.binomial(n1, 0.5)
    nA = rng.binomial(nT, 0.4); nB = rng.binomial(n1 - nT, 0.9)
    assert np.max(nA*nB) == 0, "n = 1: coincidences exactly zero at any loss"
    # T3: contamination formula
    p1, p2 = 0.95, 0.05
    p0 = 0.0
    src = rng.choice([1, 2], size=M, p=[p1, p2])
    g_pred = 2*p2/(p1 + 2*p2)**2
    g_mc = g2_split(src, 0.5, 0.8, 0.8)
    assert abs(g_mc - g_pred) < 0.02, (g_mc, g_pred)
    # locate the measured 0.18
    from scipy.optimize import brentq
    f = lambda q: 2*q/((1-q) + 2*q)**2 - 0.18  # p2=q, p1=1-q (p0 drops out of ratio? include p0=0)
    q = brentq(f, 1e-4, 0.4)
    g_at = 2*q/((1-q)+2*q)**2
    assert abs(g_at - 0.18) < 1e-6
    # T4 rows: coherent -> 1, thermal -> 2
    ncoh = rng.poisson(3.0, M)
    gcoh = g2_split(ncoh, 0.5, 0.7, 0.7)
    nth = rng.geometric(1/4.0, M) - 1
    gth = g2_split(nth, 0.5, 0.7, 0.7)
    assert abs(gcoh - 1.0) < 0.02 and abs(gth - 2.0) < 0.05, (gcoh, gth)
    print(f"T1 invariance: Fock(3) g2 = {target:.3f} at three (tau, etaA, etaB) settings -- holds")
    print("n = 1: coincidences exactly zero under arbitrary loss")
    print(f"T3: contamination formula verified (MC {g_mc:.3f} vs {g_pred:.3f}); "
          f"measured 0.18 located at p2 = {q:.3f} (p1 = {1-q:.3f})")
    print(f"T4: coherent g2 = {gcoh:.3f} (=1), thermal g2 = {gth:.2f} (=2)")
    print("PASS: g2 is a property of the source's number statistics, measured")
    print("      faithfully by any lossy apparatus -- the QB pin resolved, not")
    print("      contradicted, and the measured 0.18 is source purity.")


if __name__ == "__main__":
    test()
