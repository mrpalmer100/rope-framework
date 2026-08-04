"""FND-STRAND-027 (Derived): THE MANDEL COUNTING FORMULA FROM THRESHOLD
NUCLEATION -- P(m) = <(eta W)^m e^{-eta W}/m!> derived from the registered
detector (021's steady-state exponential escape; 020's Poissonization)
plus weak-drive linear response, with the domain stated. Consequences:
coherent -> Poisson; thermal -> Bose-Einstein; Mandel Q >= 0 for EVERY
classical drive (sub-Poissonian counting requires Grant 3's integer
quanta, the counting twin of g2 < 1).

THE CORRESPONDENCE THEOREM (T5): the Cox route and the Grant-3 route
agree EXACTLY on classical sources -- constant-I Poisson = thinned
Poisson; exponential-W geometric = binomially thinned geometric (the
geometric family is thinning-invariant). Semiclassical and granular
descriptions of classical light are one theory at two grains, which is
why photon counting alone never proved photons -- reproduced here as a
theorem the framework states about itself.

Derivation: analysis/STRAND027_mandel_counting.md.
"""
import numpy as np

rng = np.random.default_rng(2030)
M = 500000


def cox_counts(W, eta=1.0):
    return rng.poisson(eta*W)


def Q(m):
    return np.var(m)/np.mean(m) - 1.0


def test():
    # (i) coherent: constant W -> Poisson (Q = 0)
    m = cox_counts(np.full(M, 3.0))
    assert abs(Q(m)) < 0.01, "coherent: Poisson"
    # (ii) thermal: exponential W -> Bose-Einstein pmf
    wbar = 2.5
    m = cox_counts(rng.exponential(wbar, M))
    p_th = lambda k: (wbar**k)/((1 + wbar)**(k + 1))
    for k in range(6):
        assert abs(np.mean(m == k) - p_th(k)) < 0.004, f"BE pmf at k={k}"
    assert abs(Q(m) - wbar) < 0.05, "thermal: Q = <W> (super-Poissonian)"
    # (iii) Q >= 0 across classical drive ensembles
    for W in (rng.gamma(2.0, 1.5, M), rng.lognormal(0.3, 0.6, M),
              rng.uniform(0.5, 4.0, M)):
        q = Q(cox_counts(W))
        assert q > -0.01, f"classical bound: Q >= 0, got {q:.3f}"
    # (iv) T5 correspondence: thinned geometric = geometric with thinned mean
    nbar = 4.0; eta = 0.35
    nth = rng.geometric(1/(1 + nbar), M) - 1
    m_grant = rng.binomial(nth, eta)
    mbar = eta*nbar
    for k in range(6):
        assert abs(np.mean(m_grant == k) - (mbar**k)/((1 + mbar)**(k + 1))) < 0.004, \
            f"thinning invariance of geometric at k={k}"
    # coherent correspondence
    m_grant_c = rng.binomial(rng.poisson(6.0, M), 0.5)
    m_cox_c = cox_counts(np.full(M, 3.0))
    assert abs(np.mean(m_grant_c) - np.mean(m_cox_c)) < 0.02
    assert abs(Q(m_grant_c)) < 0.01 and abs(Q(m_cox_c)) < 0.01
    # (v) sub-Poissonian requires the grant: Fock n
    mF = rng.binomial(np.full(M, 4), 0.6)
    assert Q(mF) < -0.5, "Fock via Grant 3: Q < 0 (here Q = -eta = -0.6)"
    assert abs(Q(mF) + 0.6) < 0.01
    print("coherent -> Poisson (Q = 0); thermal -> Bose-Einstein (pmf to 6 terms, Q = <W>)")
    print("classical bound: Q >= 0 across gamma, lognormal, uniform drives")
    print("T5: thinned geometric = geometric (exact); coherent routes agree")
    print(f"Fock(4) via Grant 3: Q = {Q(mF):.3f} = -eta -- sub-Poissonian needs quanta")
    print("PASS: Mandel's formula from threshold nucleation; the classical")
    print("      boundary at Q = 0; the two routes one theory at two grains.")


if __name__ == "__main__":
    test()
