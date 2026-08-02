"""ELEC-068 -- THE SOLITON QUESTION: static collapse, dynamical stabilization,
and a scale that is not the strand spacing.

Bars locked in analysis/ELEC068_soliton_bars_LOCKED.md BEFORE computing.
"""
import numpy as np
import sympy as sp


def main():
    pp, k, T0 = sp.symbols("pp k T0", positive=True)

    # B1 the elimination
    alpha = (k - T0) / (2 * k)
    E = (sp.Rational(1, 2) * T0 * pp ** 2
         + sp.Rational(1, 2) * k * (alpha * pp ** 2) ** 2
         + ((k - T0) / 2) * (-alpha * pp ** 2) * pp ** 2)
    E = sp.expand(E)
    quartic = sp.simplify(sp.Poly(E, pp).coeff_monomial(pp ** 4))
    print("B1 THE ELIMINATION -- effective energy density in psi' alone:")
    print(f"   E = (T0/2) psi'^2 + ({quartic}) psi'^4")
    print(f"   quartic coefficient = {sp.factor(quartic)}")
    assert sp.simplify(quartic + (k - T0) ** 2 / (8 * k)) == 0
    print("   THE QUARTIC IS NEGATIVE for any k != T0 -- and it is a perfect")
    print("   square over k, so the attraction cannot be tuned away by any choice")
    print("   of material parameters. The coupling that made the channel usable")
    print("   is the same one that makes the configuration want to collapse.\n")

    # B2 the static verdict
    L, A, B, C = sp.symbols("L A B C", positive=True)
    Est = A / L - B / L ** 3
    Ls = sp.solve(sp.Eq(sp.diff(Est, L), 0), L)[0]
    d2 = sp.simplify(sp.diff(Est, L, 2).subs(L, Ls))
    print("B2 THE STATIC VERDICT: E(L) = A/L - B/L^3")
    print(f"   stationary point L* = {Ls}")
    print(f"   E''(L*) = {d2}  -> NEGATIVE for all positive A, B")
    print("   THIS IS A MAXIMUM, NOT A MINIMUM. There is NO static soliton: the")
    print("   stationary point is a BARRIER, with collapse below it and dispersal")
    print("   above. A STATIC LOCALIZED ELECTRON DOES NOT EXIST IN THIS SYSTEM,")
    print("   independently of ELEC-036's form factor and ELEC-057's sweep.\n")

    # B3 the dynamical test
    print("B3 THE DYNAMICAL TEST: internal circulation adds an inertial term")
    print("   ~ integral omega^2 psi^2 dx, which scales as +C L, giving")
    print("   E(L) = A/L - B/L^3 + C L.")
    print("   params (A,B,C)          discriminant   L* outer     E2nd  verdict")
    found = False
    for (a, b, c) in ((1.0, 0.05, 1.0), (1.0, 0.02, 1.0), (1.0, 0.05, 0.3),
                      (1.0, 0.05, 2.0)):
        disc = a ** 2 - 12 * b * c
        if disc <= 0:
            print(f"   {str((a,b,c)):22s} {disc:13.4f}  {'--':>9s} {'--':>10s}  "
                  f"no stationary point")
            continue
        Lo = np.sqrt(2 * (a + np.sqrt(disc))) / (2 * np.sqrt(c))
        e2 = 2 * a / Lo ** 3 - 12 * b / Lo ** 5
        found |= e2 > 0
        print(f"   {str((a,b,c)):22s} {disc:13.4f}  {Lo:9.4f} {e2:+10.4f}  "
              f"{'MINIMUM (stable)' if e2 > 0 else 'maximum'}")
    assert found
    print("   A STABLE BRANCH EXISTS. The outer stationary point is a genuine")
    print("   minimum whenever A^2 > 12 B C -- an EXISTENCE WINDOW, not automatic:")
    print("   too strong an attraction or too fast an internal frequency and the")
    print("   solution ceases to exist rather than becoming unstable.")
    print("   THE INNER BRANCH IS THE COLLAPSE BARRIER, inherited from B2.\n")

    # B4 the scale -- the deciding question
    mu, om, Bs = sp.symbols("mu omega B", positive=True)
    Lstar = sp.sqrt(2 * (T0 + sp.sqrt(T0 ** 2 - 12 * Bs * mu * om ** 2))) / (
        2 * sp.sqrt(mu * om ** 2))
    weak = sp.simplify(sp.limit(Lstar, Bs, 0))
    cc = sp.sqrt(T0 / mu)
    print("B4 THE SCALE, with A ~ T0 (tension) and C ~ mu omega^2 (internal inertia):")
    print(f"   L* -> {weak} in the weak-attraction limit")
    print(f"   and c = sqrt(T0/mu), so L* = c / omega EXACTLY "
          f"({sp.simplify(weak - cc/om) == 0}).")
    print("   THE SCALE IS SET BY THE INTERNAL FREQUENCY, NOT BY THE STRAND")
    print("   SPACING. L* = c/omega contains no reference to a.")
    print("   CONSEQUENCE FOR ELEC-066's CONJECTURE: ELEC-057's no-go swept the")
    print("   electron gate using r_e ~ a, which followed from rigid staticness.")
    print("   A dynamically stabilized object has r ~ c/omega and is OUTSIDE that")
    print("   sweep. The conjecture survives its first quantitative test.")
    print("   NOTED WITHOUT CLAIM: L = c/omega is the form of the Compton relation.")
    print("   That is an observation about the shape of the result, not a")
    print("   derivation of anything, and nothing here fixes omega.\n")

    # B5
    print("B5 WHAT THIS IS NOT, all four stated:")
    print("   (i)   Derrick scaling shows a stationary point exists under an")
    print("         assumed profile family; it does NOT construct a solution.")
    print("   (ii)  Uniqueness is not established.")
    print("   (iii) The amplitude is not fixed -- only the scale, and only given")
    print("         omega, which nothing here determines.")
    print("   (iv)  No connection is made to any measured electron property:")
    print("         not charge, not mass, not the form factor ELEC-036 tested.")
    print("   The system is 1+1 and the transverse field is a scalar stand-in.")
    print("PASS: static collapse established, dynamical stabilization established")
    print("      with its existence window, and the stabilized scale identified.")


if __name__ == "__main__":
    main()
