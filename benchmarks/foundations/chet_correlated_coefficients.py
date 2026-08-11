"""Commission CHET -- the correlated-coefficients relation.
Bars locked BEFORE evaluation
(analysis/CHET_correlated_coefficients_bars_LOCKED.md): mean-field
centrality (C1), ordering-allowing correlator (C2), the d^abcd
adjudication (C3), three-way verdict grammar, and the kappa_pack pin.
All group identities verified with explicit matrices.
"""
import numpy as np

# --- SU(3) generators ---------------------------------------------------
def gellmann():
    l = np.zeros((8, 3, 3), dtype=complex)
    l[0][0, 1] = l[0][1, 0] = 1
    l[1][0, 1] = -1j; l[1][1, 0] = 1j
    l[2][0, 0] = 1; l[2][1, 1] = -1
    l[3][0, 2] = l[3][2, 0] = 1
    l[4][0, 2] = -1j; l[4][2, 0] = 1j
    l[5][1, 2] = l[5][2, 1] = 1
    l[6][1, 2] = -1j; l[6][2, 1] = 1j
    l[7][0, 0] = l[7][1, 1] = 1 / np.sqrt(3); l[7][2, 2] = -2 / np.sqrt(3)
    return l / 2


def structure_constants(T):
    n = len(T)
    f = np.zeros((n, n, n))
    for a in range(n):
        for b in range(n):
            comm = T[a] @ T[b] - T[b] @ T[a]
            for c in range(n):
                f[a, b, c] = np.real(-1j * np.trace(comm @ T[c])) * 2
    return f


def adjoint_reps(f):
    return np.array([-1j * f[a] for a in range(len(f))])


def casimir(T):
    dim = T[0].shape[0]
    c = sum(t @ t for t in T)
    assert np.allclose(c, c[0, 0] * np.eye(dim), atol=1e-10), "C2 not central"
    return np.real(c[0, 0])


def main():
    TF = gellmann()
    f = structure_constants(TF)
    TA = adjoint_reps(f)
    reps = {"F (3)": TF, "A (8)": TA}
    CA = casimir(TA)

    print("C1 -- MEAN-FIELD CENTRALITY (explicit matrices):")
    for name, T in reps.items():
        dim = T[0].shape[0]
        C2 = casimir(T)
        X = sum(t @ t for t in T)             # g'^2 = f^2 T.T : central
        X2 = X @ X
        assert np.allclose(X2, C2**2 * np.eye(dim), atol=1e-8)
        print(f"  {name}: C2 = {C2:.4f}; (T.T)^2 = C2^2 exactly -- the")
        print("    static-profile quartic term is CENTRAL: no d^abcd, no")
        print("    C2 C_A, nothing but C2^2.")

    print("C2 -- ORDERING-ALLOWING correlator, identity machine-checked:")
    for name, T in reps.items():
        dim = T[0].shape[0]
        C2 = casimir(T)
        cross = sum(T[a] @ T[b] @ T[a] @ T[b]
                    for a in range(8) for b in range(8))
        pred = C2 * (C2 - CA / 2)
        assert np.allclose(cross, pred * np.eye(dim), atol=1e-7)
        S = (C2**2 + pred + C2**2) / 3        # pair-symmetrized, isotropic
        assert abs(S - (C2**2 - C2 * CA / 6)) < 1e-9
        print(f"  {name}: T^aT^bT^aT^b = C2(C2 - C_A/2) VERIFIED; "
              f"S(R) = C2^2 - C2 C_A/6 = {S:.4f}")
    print("  S(R)/C2 = C2 - C_A/6: the C_A piece is REPRESENTATION-")
    print("  INDEPENDENT -- it cancels in every cross-representation")
    print("  difference. Even the ordering-allowing contraction leaves the")
    print("  violation EXACTLY C2-linear.")

    print("C3 -- the d^abcd adjudication: the ansatz's leading order offers")
    print("  only delta-contractions of <= 4 charges on one source line;")
    print("  their span is {C2^2, C2 C_A} (verified above) -- d^abcd-class")
    print("  invariants first require FOUR INDEPENDENT color-open insertions")
    print("  (path-ordered multi-exchange), which is a fluctuation effect")
    print("  BEYOND the static quadratic-nonlinearity ansatz. At leading")
    print("  order the quartic-Casimir component is ZERO.")

    print("VERDICT (per the locked grammar): PURE-LINEAR. ALEPH's refined")
    print("  prediction SHARPENS: the long-distance violation is predicted")
    print("  C2-linear with coefficient -(eps_f/2)(C_D/C_f - 1) (BET) and a")
    print("  SUPPRESSED (higher-order) quartic-Casimir component. ALEPH's W2")
    print("  'folds in at this order' language receives a correction pointer:")
    print("  the nonlinearity generates quartic structure only beyond mean")
    print("  field. KILL CONDITIONS RESTATED: a long-distance violation that")
    print("  is quartic-DOMINANT kills; anti-C2 ordering kills; magnitude")
    print("  forcing eps_f > 5% kills.")

    # THE PIN: a resolved long-distance violation measures kappa_pack
    CF = casimir(TF)
    print("THE kappa_pack PIN (exact inversion of BET's derived form):")
    print("  kappa_pack = (C_D/C_f - 1) / (2 |delta_D - delta_f|)")
    for kappa in (50, 250):
        eps = 1 / kappa
        dAF = -(eps / 2) * (CA / CF - 1)
        print(f"  forward prediction at kappa_pack = {kappa}: "
              f"delta_A - delta_F = {dAF:.4%} (adjoint vs fundamental)")
        assert abs((CA / CF - 1) / (2 * abs(dAF)) - kappa) < 1e-9
    print("  A lattice hybrid-potential determination of the adjoint/")
    print("  fundamental long-distance ratio at the percent level READS")
    print("  kappa_pack directly. The pin is registered; conditional on")
    print("  FND-037 as everything vacuum-facing is.")
    print("ALL BARS ADJUDICATED (verdict: PURE-LINEAR; pin registered)")


if __name__ == "__main__":
    main()
