"""FND-STRAND-025 (Derived, conditional on Grant 3): THE THIRD GRANT AND
ITS FIRST CONSEQUENCE -- indivisible delivery ("the quantum arrives
whole") plus the registered Born-from-channel-energy law yields the full
beamsplitter phenomenology in counting arithmetic: single-arm P = tau,
exact anticoincidence (g2 = 0) for single quanta, Binomial(n, tau) Fock
counting, the coherent limit RECOVERED (independent Poisson thinning,
g2 = 1 -- the grant cannot fake quantumness for classical light), and
thermal bunching (g2 = 2) for free.

Grant statement, scope discipline (bookkeeping at absorption, not
dynamics; no entanglement granted; QB-003 untouched), falsifiers F1-F3,
the retirement clause F4, and the austerity ledger:
analysis/STRAND025_third_grant.md. What it does NOT buy is stated there
first: HOM's exchange interference and CHSH remain on the far side.

This benchmark executes the counting arithmetic numerically against the
closed forms.
"""
import numpy as np

rng = np.random.default_rng(2028)


def split_quanta(n_arr, tau):
    return rng.binomial(n_arr, tau)


def g2_zero(nA, nB=None):
    if nB is None:
        n = nA
        num = np.mean(n*(n-1)); den = np.mean(n)**2
    else:
        num = np.mean(nA*nB); den = np.mean(nA)*np.mean(nB)
    return num/den


def test():
    M = 400000
    # (i)+(ii) single quantum at tau
    for tau in (0.5, 0.3, 0.8):
        nA = split_quanta(np.ones(M, int), tau)
        nB = 1 - nA
        assert abs(nA.mean() - tau) < 0.005, "single-arm P = tau"
        assert np.all(nA + nB == 1) and np.max(nA*nB) == 0, \
            "exact anticoincidence: one quantum, one click"
    # (iii) Fock counting: Binomial(n, tau)
    n = 5; tau = 0.37
    nA = split_quanta(np.full(M, n), tau)
    from math import comb
    for k in range(n + 1):
        p_emp = np.mean(nA == k)
        p_th = comb(n, k)*tau**k*(1 - tau)**(n - k)
        assert abs(p_emp - p_th) < 0.005, f"Binomial at k={k}"
    # (iv) coherent limit: independent Poisson thinning, g2 = 1
    lam = 3.0
    ncoh = rng.poisson(lam, M)
    nA = split_quanta(ncoh, 0.5); nB = ncoh - nA
    g2_cross = g2_zero(nA, nB)
    assert abs(g2_cross - 1.0) < 0.02, f"coherent g2 = 1, got {g2_cross:.3f}"
    r = np.corrcoef(nA, nB)[0, 1]
    assert abs(r) < 0.01, "arms independent for coherent input"
    # single-quantum g2 cross = 0 exactly (already asserted); sub-Poisson discriminates
    # (v) thermal: geometric number, g2 = 2 and cross-bunching
    p = 1/(1 + lam)
    nth = rng.geometric(p, M) - 1
    nA = split_quanta(nth, 0.5); nB = nth - nA
    g2a = g2_zero(nA); g2x = g2_zero(nA, nB)
    assert abs(g2a - 2.0) < 0.05 and abs(g2x - 2.0) < 0.05, (g2a, g2x)
    print("single-arm P = tau (3 values); anticoincidence exact (g2 = 0)")
    print(f"Fock(5): Binomial verified all k; coherent: g2 = {g2_cross:.3f} (=1), arms independent")
    print(f"thermal: g2_auto = {g2a:.2f}, g2_cross = {g2x:.2f} (=2) -- HBT bunching for free")
    print("PASS: the quantum arrives whole -- Grangier-Roger, Fock counting,")
    print("      the classical limit, and thermal bunching from one sentence")
    print("      plus the registered Born law.")


if __name__ == "__main__":
    test()
