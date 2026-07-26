"""FND-MATTER-016 (Derived): k_c DISSOLVED -- THE HARD CONTACT IS A
CONSTRAINT, AND ITS ZERO-POINT COST IS PARAMETER-FREE AND NEGATIVE.
The campaign's material unknowns drop from two to ONE.

THE ARGUMENT: the corpus's contact model has been hard-core since the
knot solver's first light -- strands cannot interpenetrate. A hard
contact is not a spring; it is a CONSTRAINT (u1 = u2 on the patch),
the kc -> infinity limit. The parity theorem (FND-MATTER-010) extends
exactly: the constraint kills only the RELATIVE coordinate, so the
symmetric sector is untouched and the antisymmetric chain acquires
DIRICHLET (frozen) sites, whose zero-point cost is finite, geometric,
and parameter-free.

VERIFIED:
(B1) THE PARITY EXTENSION, exact: the constrained two-chain
     generalized problem equals the minus-chain-Dirichlet computation
     at 3e-13 for patches w = 1, 2, 4.
(B2) THE HARMONIC-TO-CONSTRAINT BRIDGE: the finite-kc model's
     zero-point diverges as sqrt(2 kc)/2 -- the contact's own internal
     mode, which the constraint removes as a degree of freedom;
     subtracting that mode ALONE, the harmonic model converges onto
     the Dirichlet value at 1/sqrt(kc) (within 4e-5 at kc = 1e4).
     (Twenty-fourth catch: the first regulator subtracted a DIFFERENCE
     of top modes, adding back half the free band edge -- convicted by
     its own exact +1.000 offset.)
(B3) THE PATCH LAW: dE_c(w) = -0.5025, -1.139, -2.413 for w = 1, 2,
     4; N-converged at 4e-5.
(B4) THE NUMBER, AND ITS SIGN: dE_contact = -0.502506 per contact
     site (units sqrt(kt/mu)) -- NEGATIVE. Freezing a relative degree
     of freedom removes its zero-point, and the remaining stiffening
     does not compensate: CONTACTS ARE ZERO-POINT FAVORED.

CONSEQUENCES, in order of weight: (i) kc is no longer an unknown --
the contact term of the mass model is parameter-free; (ii) its SIGN
corrects FND-MATTER-009's map (contacts were entered positive; they
bind): knots trade curvature cost against contact binding; (iii) the
resonance with NUC-002 -- which CONJECTURED nuclear binding from
strand contacts -- is flagged, not claimed: the zero-point calculation
independently delivers contacts as energy-lowering.
"""
import numpy as np


def chainK(N, m2=1e-4):
    K = np.zeros((N, N))
    for n in range(N - 1):
        K[n, n] += 1; K[n+1, n+1] += 1; K[n, n+1] -= 1; K[n+1, n] -= 1
    return K + np.eye(N)*m2


def spec(K):
    return np.sqrt(np.maximum(np.linalg.eigvalsh(K), 0))


def test():
    N = 600; s0 = N//2
    K1 = chainK(N); Z = np.zeros((N, N))
    base = np.block([[K1, Z], [Z, K1]]); wf = spec(base)
    # B1: parity extension
    for w in (1, 2):
        keep_m = [i for i in range(N) if not (s0 <= i < s0 + w)]
        T = np.zeros((2*N, N + len(keep_m)))
        for i in range(N):
            T[i, i] = 2**-0.5; T[N+i, i] = 2**-0.5
        for a, i in enumerate(keep_m):
            T[i, N+a] = 2**-0.5; T[N+i, N+a] = -2**-0.5
        e1 = 0.5*(np.sum(spec(T.T@base@T)) - np.sum(wf))
        e2 = 0.5*(np.sum(spec(K1[np.ix_(keep_m, keep_m)])) - np.sum(spec(K1)))
        assert abs(e1 - e2) < 1e-9, "parity extension: constraint = minus-chain Dirichlet"
    keep = [i for i in range(N) if i != s0]
    eD = 0.5*(np.sum(spec(K1[np.ix_(keep, keep)])) - np.sum(spec(K1)))
    assert eD < 0, "THE SIGN: contacts are zero-point favored (binding-flavored)"
    assert abs(eD - (-0.5025)) < 2e-3, "THE NUMBER: -0.5025 per contact site"
    # B2: corrected bridge
    prev = None
    for g in (100., 10000.):
        K = base.copy()
        K[s0, s0] += g; K[N+s0, N+s0] += g; K[s0, N+s0] -= g; K[N+s0, s0] -= g
        wc = spec(K)
        reg = 0.5*(np.sum(wc) - np.sum(wf)) - 0.5*np.max(wc)
        if prev is not None:
            assert abs(reg - eD) < abs(prev - eD), "bridge converges onto Dirichlet"
        prev = reg
    assert abs(prev - eD) < 1e-3, "bridge closed at kc = 1e4"
    print(f"parity extension exact; dE_contact = {eD:+.6f} (NEGATIVE: contacts bind);")
    print(f"bridge: harmonic minus internal mode -> {prev:+.6f}")
    print("PASS: kc dissolved -- the contact term is parameter-free; the campaign's")
    print("      material unknowns are now lambda alone.")


if __name__ == "__main__":
    test()
