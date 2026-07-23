"""QB-021 (Derived): COMPOSITE POSITIVITY ELIMINATED FROM THE TSIRELSON
DERIVATION -- the third axiom this framework has retired by its own
structure (after impenetrability, FND-KIN-005, and the harmonic-order
clause, QB-018). The cap needs only three corpus-held ingredients:

  (i)   MECHANISM-UNITY: one linear functional omega evaluates the pair
        (QB-019's principle);
  (ii)  the LINEAR RESPONSE FORM: the observable is a.sigma -- linear in
        the setting -- which is QB-011's derived gamma = 1 dipole
        structure, whose single-wing uniqueness QB-013 proved;
  (iii) outcomes are +-1, so |E(a, b)| <= 1 at every setting pair -- an
        empirical triviality, not an axiom.

From (i) + (ii): E(a, b) = omega(A_a x B_b) is BILINEAR -- E = a.T.b --
whether or not omega is positive. From (iii): sup |a.T.b| = sigma_max(T)
<= 1. Horodecki: CHSH = 2 sqrt(t1^2 + t2^2) <= 2 sqrt 2. POSITIVITY DOES
NO WORK IN THE CAP.

(B1) verified: ensembles of INDEFINITE omega (states with negative
     eigenvalues), rescaled only to satisfy |E| <= 1, are exactly
     bilinear and cap at 2 sqrt 2; the cap is saturable (T = -I).
(B2) THE PRECISE RESIDUE OF POSITIVITY, exhibited: T = +I (perfect
     CORRELATION at every equal setting) satisfies |E| <= 1 and reaches
     CHSH = 2 sqrt 2 under the mechanism form -- but no positive state
     produces it: positivity selects WHICH Tsirelson-capped correlations
     are physical (the Bell-diagonal tetrahedron), not the cap itself.
(B3) tetrahedron check: T = -I inside (the singlet vertex); T = +I
     outside (minimum eigenvalue of the reconstructed operator < 0).

THE WALL'S FINAL ACCOUNTING: the import list is now MECHANISM-UNITY,
alone. The detection law is derived (QB-011); its linearity and
uniqueness are derived (QB-013); the cap follows from unity + linearity +
arithmetic (this claim); the saturating state is forced by isotropy +
the pairing convention (QB-020). One principle remains, and it is the
one whose physical content -- a measurement is a single local process --
was never mysterious.
"""
import numpy as np


def suite():
    rng = np.random.default_rng(127)
    sx = np.array([[0, 1], [1, 0]], complex)
    sy = np.array([[0, -1j], [1j, 0]])
    sz = np.array([[1, 0], [0, -1]], complex)
    S = [sx, sy, sz]

    def units(n):
        v = rng.standard_normal((n, 3))
        return v/np.linalg.norm(v, axis=1, keepdims=True)

    def obs(a):
        return a[0]*sx + a[1]*sy + a[2]*sz
    # B1: indefinite omega ensembles
    worst_bil = 0.0; worst_chsh = 0.0; any_indef = 0
    for _ in range(50):
        H = rng.standard_normal((4, 4)) + 1j*rng.standard_normal((4, 4))
        W = (H + H.conj().T)/2                       # Hermitian, generally INDEFINITE
        W = W - np.trace(W)*np.eye(4)/4 + np.eye(4)/4  # unit trace, still indefinite
        if np.linalg.eigvalsh(W).min() < -1e-9:
            any_indef += 1
        T = np.array([[np.trace(W@np.kron(S[i], S[j])).real for j in range(3)]
                      for i in range(3)])
        sm = np.linalg.svd(T, compute_uv=False)[0]
        if sm > 1:
            W = W/sm + (1 - 1/sm)*np.eye(4)/4        # rescale correlations into |E|<=1
            T = T/sm
        # bilinearity of omega-correlations (positivity never used)
        for a, b in zip(units(12), units(12)):
            E = np.trace(W@np.kron(obs(a), obs(b))).real
            worst_bil = max(worst_bil, abs(E - a@T@b))
        sv = np.linalg.svd(T, compute_uv=False)
        worst_chsh = max(worst_chsh, 2*np.sqrt(sv[0]**2 + sv[1]**2))
    # B2/B3: T = +I passes the cap machinery but fails positivity; T = -I is physical
    def op_from_T(T):
        W = np.eye(4, dtype=complex)/4
        for i in range(3):
            for j in range(3):
                W = W + T[i, j]*np.kron(S[i], S[j])/4
        return W
    lam_plus = np.linalg.eigvalsh(op_from_T(np.eye(3))).min()
    lam_minus = np.linalg.eigvalsh(op_from_T(-np.eye(3))).min()
    svI = np.linalg.svd(np.eye(3), compute_uv=False)
    chsh_I = 2*np.sqrt(svI[0]**2 + svI[1]**2)
    return worst_bil, worst_chsh, any_indef, lam_plus, lam_minus, chsh_I


def test():
    bil, cap, n_indef, lp, lm, chshI = suite()
    Ts = 2*np.sqrt(2)
    assert n_indef > 30, "the ensemble is genuinely indefinite (positivity absent)"
    assert bil < 1e-10, "bilinearity holds WITHOUT positivity (unity + linear response)"
    assert cap <= Ts + 1e-9, "|E|<=1 alone caps CHSH at 2 sqrt 2"
    assert chshI > Ts - 1e-9, "T=+I reaches the cap under the mechanism form"
    assert lp < -1e-6, "but T=+I is NOT positive-state realizable (positivity's residue)"
    assert lm > -1e-9, "while T=-I (the singlet) is physical"
    print(f"B1: {n_indef}/50 omegas indefinite; bilinearity {bil:.1e}; cap {cap:.6f} <= {Ts:.6f}")
    print(f"B2: T=+I: CHSH = {chshI:.6f} (at the cap) but min eigenvalue {lp:.3f} < 0 -- unphysical")
    print(f"B3: T=-I: min eigenvalue {lm:.1e} >= 0 -- the singlet is the physical saturator")
    print("PASS: positivity eliminated from the cap derivation; the wall's import list is")
    print("      mechanism-unity, alone. Positivity's residue: selecting the physical set.")


if __name__ == "__main__":
    test()
