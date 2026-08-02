"""ELEC-070 -- DERRICK IN 3+1: the 1D stabilization dies, and a positive sextic
takes its place.

Bars locked in analysis/ELEC070_derrick_3d_bars_LOCKED.md BEFORE computing.
"""
import numpy as np
import sympy as sp


def main():
    L, A, B, C, Dc = sp.symbols("L A B C D", positive=True)

    print("B1 THE 3D VERDICT ON ELEC-068's MECHANISM")
    for D in (1, 3):
        E = A * L ** (D - 2) - B * L ** (D - 4) + C * L ** D
        d1 = sp.simplify(sp.diff(E, L))
        sols = [s for s in sp.solve(sp.Eq(d1, 0), L) if s.is_real is not False]
        print(f"   D={D}: E = {sp.simplify(E)}")
        print(f"        dE/dL = {d1}")
        print(f"        stationary points: {'yes' if sols else 'NONE for positive A,B,C'}")
    print("   In D = 3 every term of dE/dL is POSITIVE, so E is monotone increasing")
    print("   and its infimum is at L -> 0, where -B/L diverges. THE DYNAMICAL")
    print("   STABILIZATION OF ELEC-068 IS A ONE-DIMENSIONAL ARTIFACT. Nothing")
    print("   computed there was wrong; its relevance to a real particle is")
    print("   withdrawn. The internal-frequency term grows as L^3 in 3D and")
    print("   cannot fight a collapse that diverges as 1/L.\n")

    print("B2 THE SEXTIC'S SIGN, computed from the strain expansion:")
    t, k, T0 = sp.symbols("t k T0", positive=True)
    a1, a2 = sp.symbols("a1 a2", real=True)
    eps = sp.sqrt((1 + a1 * t + a2 * t ** 2) ** 2 + t) - 1
    E6 = sp.Rational(1, 2) * k * eps ** 2 + T0 * eps
    S = sp.expand(sp.series(E6, t, 0, 4).removeO())
    P = sp.Poly(S, t)
    a1v = sp.solve(sp.diff(P.coeff_monomial(t ** 2), a1), a1)[0]
    c6 = sp.factor(sp.simplify(P.coeff_monomial(t ** 3).subs(a1, a1v)))
    print(f"   a1 = {a1v}  (the cubic-order constraint, reproducing ELEC-067)")
    print(f"   psi'^6 coefficient = {c6}")
    print("   This is POSITIVE whenever k > 2 T0. The registered stiffness ratio")
    print("   is k/T0 >= 1.9e8 (QB-008, Bell timing), so the condition holds by")
    print("   eight orders of magnitude. THE SEXTIC IS REPULSIVE AT SHORT SCALE --")
    print("   the Skyrme-class term a 3D soliton needs.\n")

    print("B3 THE 3D TEST WITH THE SEXTIC: E = A L - B/L + D/L^3")
    E3 = A * L - B / L + Dc / L ** 3
    d1 = sp.simplify(sp.diff(E3, L))
    star = [s for s in sp.solve(sp.Eq(d1, 0), L) if s.is_real is not False]
    print(f"   dE/dL = {d1}")
    print(f"   stationary point L* = {sp.simplify(star[0])}")
    ok = True
    for (a, b, d) in ((1.0, 1.0, 0.05), (1.0, 2.0, 0.05), (1.0, 0.5, 0.2)):
        f = lambda l: a * l - b / l + d / l ** 3
        ls = np.logspace(-2, 2, 200000)
        i = int(np.argmin(f(ls)))
        h = 0.01 * ls[i]
        e2 = (f(ls[i] + h) - 2 * f(ls[i]) + f(ls[i] - h)) / h ** 2
        ok &= e2 > 0
        print(f"   A={a} B={b} D={d}: L*={ls[i]:.4f}, E''={e2:+.2f} -> "
              f"{'MINIMUM (stable)' if e2 > 0 else 'not a minimum'}")
    assert ok
    print("   A STABLE 3D SOLITON EXISTS, and it does NOT require the internal")
    print("   frequency at all: the positive sextic alone balances the attractive")
    print("   quartic. THE STABILIZATION IS STRUCTURAL, NOT DYNAMICAL.\n")

    print("B4 THE CAVEAT, and it is serious:")
    print("   The EXACT elimination of the longitudinal field is DEGENERATE.")
    print("   Solving dE/du' = 0 exactly gives eps = -T0/k and hence a CONSTANT")
    print("   energy independent of psi' -- an inextensible medium can absorb any")
    print("   transverse displacement by shortening. The perturbative elimination")
    print("   used here and in ELEC-067/068/069 is therefore an approximation")
    print("   whose domain of validity is NOT established, and the sextic")
    print("   coefficient inherits that uncertainty. Everything above is")
    print("   conditional on the truncation being physical.\n")

    print("B5 NO CLAIM ABOUT THE ELECTRON. What the scaling says and nothing more:")
    print("   the 1D dynamical mechanism does not survive to 3D; a positive sextic")
    print("   does stabilize in 3D under a condition the corpus's own registered")
    print("   stiffness satisfies; the scale is then set by the balance of three")
    print("   terms rather than by c/omega, so ELEC-068's L* = c/omega does NOT")
    print("   carry over and the Compton-form observation lapses with it.")
    print("PASS: the dimension check was run, it killed the previous mechanism,")
    print("      and a different one survived in its place.")


if __name__ == "__main__":
    main()
