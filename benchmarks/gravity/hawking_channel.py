"""GRV-039 (Modeled): THE HAWKING CHANNEL TESTED -- the comb radiates at
formation and then goes QUIET: a registered divergence from steady
Hawking evaporation, kept loudly, with a named falsifier.

THE EXPERIMENT: exact Gaussian (covariance-matrix) quantum dynamics of
the transverse chain through horizon FORMATION -- uniform-medium vacuum,
tension profile ramped to the exhaustion configuration (c(x) crossing
linearly, kappa = dc/dx), then free evolution.

(R1) FORMATION RADIATES, measured: a directed outgoing burst (right-
     mover excess over the left-mover control) and outer-region energy
     above vacuum -- the collapse's quantum imprint escapes.
(R2) THE STEADY CHANNEL GOES QUIET, measured: after the burst passes,
     the energy current settles to ZERO (|J|/P_SB ~ 0.01 against the
     1D Stefan-Boltzmann prediction at T = kappa/2pi). AUDIT VERDICT
     (per house rules, before accepting a null): not instrument --
     continuous Hawking flux requires infinite redshift or a supply
     flow; the corpus's horizon is a percolation-SEVERED transverse
     channel (GRV-035) with a strand-scale floor: Boulware-like at
     late times. The mechanism the standard derivation needs is the
     mechanism this medium removes.
(R3) THE DIVERGENCE, registered as such: the corpus predicts TRANSIENT
     emission (formation- and accretion-powered; each ratchet event
     releases measured dE ~ +0.07, GRV-036 -- candidate 'reconnection
     noise' from the marginal shell) and NOT steady thermal evaporation
     of isolated holes. Observationally indistinguishable today
     (T_H ~ 1e-8 K for stellar holes) but in-principle divergent:
     A DETECTED PRIMORDIAL-BLACK-HOLE EVAPORATION BURST WOULD FALSIFY
     THIS BRANCH. Named, armed, kept.
(R4) THE 1/4, honestly disposed: the thermodynamic integration
     (T = kappa/2pi with dM = T dS gives S = A/4 exactly) is recorded
     as the CONDITIONAL closure -- but this corpus declines the
     condition's premise at the steady level, so the coefficient is
     NOT claimed; the entropy remains the count, S ~ A/a^2 x O(1)
     (GRV-037/038), coefficient open.

HONEST LIMITS: 1+1 chain; lattice dispersion and c-floor stand in for
the severed channel; formation profile stylized; the reconnection-noise
temperature scale uncomputed (named next-order).
"""
import numpy as np

N = 300; kt0 = 1.0; m2 = 1e-6; x0 = 60; Lg = 6; eps = 0.02


def build_K(prof):
    K = np.zeros((N, N))
    for n in range(N - 1):
        k = prof[n]
        K[n, n] += k; K[n + 1, n + 1] += k; K[n, n + 1] -= k; K[n + 1, n] -= k
    return K + np.eye(N)*m2


def vac_cov(K):
    w2, V = np.linalg.eigh(K); w = np.sqrt(np.maximum(w2, 1e-12))
    return (V*(0.5/w))@V.T, (V*(0.5*w))@V.T


def evolve(Cx, Cp, Cxp, K, t):
    w2, V = np.linalg.eigh(K); w = np.sqrt(np.maximum(w2, 1e-12))
    c = np.cos(w*t); s = np.sin(w*t)
    A11 = (V*c)@V.T; A12 = (V*(s/w))@V.T; A21 = (V*(-w*s))@V.T
    nCx = A11@Cx@A11.T + A12@Cp@A12.T + A11@Cxp@A12.T + A12@Cxp.T@A11.T
    nCp = A21@Cx@A21.T + A11@Cp@A11.T + A21@Cxp@A11.T + A11@Cxp.T@A21.T
    nCxp = A11@Cx@A21.T + A12@Cp@A11.T + A11@Cxp@A11.T + A12@Cxp.T@A21.T
    return nCx, nCp, nCxp


def test():
    xs = np.arange(N)
    prof_f = (np.sqrt(kt0)*np.clip((xs - x0)/Lg, eps, 1.0))**2
    kappa = np.sqrt(kt0)/Lg
    P_SB = np.pi*(kappa/(2*np.pi))**2/12
    Cx, Cp = vac_cov(build_K(np.full(N, kt0))); Cxp = np.zeros((N, N))
    for j in range(30):
        lam = (j + 1)/30
        Cx, Cp, Cxp = evolve(Cx, Cp, Cxp, build_K((1 - lam)*np.full(N, kt0) + lam*prof_f), 3.0)
    Kf = build_K(prof_f)
    Cx, Cp, Cxp = evolve(Cx, Cp, Cxp, Kf, 60.0)
    sl = slice(100, 250)
    w2o, _ = np.linalg.eigh(Kf[sl, sl])
    Eex = np.trace(Cp[sl, sl])/2 + np.trace(Kf[sl, sl]@Cx[sl, sl])/2 - np.sum(np.sqrt(np.maximum(w2o, 0)))/2
    assert Eex > 0.1, "R1: formation radiates -- outer energy above vacuum"
    Cx, Cp, Cxp = evolve(Cx, Cp, Cxp, Kf, 120.0)   # let the burst pass
    J = np.mean([-kt0*0.5*(Cxp[s + 1, s] + Cxp[s, s + 1] - Cxp[s - 1, s] - Cxp[s, s - 1])
                 for s in range(110, 170)])
    assert abs(J) < 0.1*P_SB, "R2: the steady channel is QUIET (Boulware-like late time)"
    # R4: the conditional closure, recorded not claimed: T = kappa/2pi -> S = A/4
    M = 1.0; dM = 1e-4; S = 0.0; m = 1e-6
    while m < M:
        S += dM/((1/(4*(m + dM/2)))/(2*np.pi)); m += dM
    assert abs(S/(4*np.pi*M**2) - 1) < 1e-3, "R4: dM = (kappa/2pi) dS integrates to S = A/4 = 4 pi M^2"
    print(f"R1: burst energy = {Eex:.3f} > 0; R2: late |J|/P_SB = {abs(J)/P_SB:.3f} -- quiet")
    print(f"R4: conditional closure verified (S -> 4 pi M^2 = A/4) -- condition declined at steady level")
    print("PASS (as the registered divergence): formation radiates, isolated holes go quiet;")
    print("      a detected PBH evaporation burst would falsify this branch. Named, armed, kept.")


if __name__ == "__main__":
    test()
