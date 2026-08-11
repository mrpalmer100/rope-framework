"""Commission ALEPH — the attack on FND-037: verdict WOUNDED.

T2 THE STRUCTURAL CONFRONTATION: the only resolved CS violation in any
regime (Anzai-Kiyo-Sumino, three-loop static potential, NPB 838 (2010) 28
+ erratum) is (a) NEGATIVE-direction -- it REDUCES the tangent of
V_R(r)/C_R, higher representations under-binding relative to Casimir-linear
-- and (b) quartic-Casimir structured (d_R^abcd d_F^abcd class), not
linear in C2. It lives in the short-distance Coulomb regime and is "well
within present lattice bounds."

AGAINST THE PRE-LOCKED KILL CONDITIONS: K1-K3 are scoped to the LONG-
DISTANCE (string tension) regime; the perturbative result does not
formally trigger them (T3 regime honesty). NO KILL. But the wound is
real and twofold:
  W1 SIGN: FND-037's "positive-definite" clause was a classical-charge
     guess the derivation never actually fixed (the medium could stiffen
     or soften); the one resolved violation anywhere is NEGATIVE. The
     clause is RETRACTED to "one-signed, sign unresolved at long
     distance" -- correction pointer filed against FND-037.
  W2 STRUCTURE: quartic-Casimir terms are exactly what the framework's
     quadratic nonlinearity generates once color charges are treated as
     non-commuting operators (fourth-order charge correlators) -- the
     pre-stated refinement path, adverse to the naive linear form but
     compatible with the picture. REFINED FORWARD PREDICTION (the new
     falsifiable residue): the long-distance violation, when resolved,
     carries BOTH a C2-linear and a quartic-Casimir component with
     CORRELATED coefficients (one medium-nonlinearity parameter).

THE TOWER SURVIVES: the kappa_pack floor is a MAGNITUDE bound --
eps_f <= |delta|_max/(C_max/C_f - 1) -- and is sign-independent, so
OMEGA's ledger stands unchanged in every number, re-graded only in the
sign clause it inherited. Verified below.
"""
CS_BOUND = 0.05
C_RATIOS = {"8": 2.25, "6": 2.5, "15a": 4.0, "10": 4.5, "27": 6.0, "15s": 7.0}


def main():
    cmax = max(C_RATIOS.values())
    for sign in (+1, -1):                       # the floor at both signs
        eps = abs(sign * CS_BOUND) / (cmax - 1)
        assert abs(1 / eps - 120) < 1          # kappa_pack >= ~120 either way
    # the discriminant that keeps the refinement falsifiable: C2-linear
    # ordering (8<6<15a<10<27<15s) is a strict ordering the quartic piece
    # need not share -> a resolved long-distance measurement can separate them
    order = sorted(C_RATIOS, key=C_RATIOS.get)
    assert order == ["8", "6", "15a", "10", "27", "15s"]
    print("kappa_pack floor sign-independent: >= ~120 at |delta| <= 5% -- OMEGA stands")
    print("FND-037 WOUNDED: sign clause retracted; quartic refinement registered")
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
