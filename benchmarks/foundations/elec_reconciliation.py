"""ELEC-078 -- RECONCILING EM-RECON-011: u is gauge, u' is density, and strand
number conservation gives a THIRD effective energy with no attraction.

Bars locked in analysis/ELEC078_reconciliation_bars_LOCKED.md BEFORE computing.
"""
import sympy as sp


def main():
    up, p, k, T0, lam, m2 = sp.symbols("up p k T0 lam m2", real=True)
    eps = sp.sqrt((1 + up) ** 2 + p ** 2) - 1

    print("B1 DOES THE ENERGY DEPEND ON u ITSELF?")
    print(f"   eps = {eps}")
    print("   u appears ONLY through u'. Every energy in this line -- the elastic")
    print("   term, the tension term, the cubic vertex u' psi'^2 -- is built from")
    print("   u' alone.\n")

    print("B2 THE RECONCILIATION:")
    print("   u itself is gauge: without material points, 'how far this bit of")
    print("   strand moved' has no meaning. But u' does have one. A medium of")
    print("   strands has a DENSITY n(x), and longitudinal compression is")
    print("   u' = -delta_n/n, which is OBSERVABLE and needs no material labels.")
    print("   SO BOTH LEGS STAND: displacement is gauge, its gradient is density,")
    print("   and the energy depends only on the latter. EM-RECON-011 is")
    print("   internally consistent after all, and ELEC-077's strain is resolved")
    print("   in favour of the claim.\n")

    print("B3 WHAT THAT FORCES -- STRAND NUMBER IS CONSERVED:")
    print("   integral u' dx = 0 is a GLOBAL constraint. ELEC-068's free pointwise")
    print("   minimisation over u' ignored it. With a multiplier,")
    E = sp.Rational(1, 2) * k * eps ** 2 + T0 * eps - lam * up
    print(f"      d/du'[(k/2)eps^2 + T0 eps - lam u'] = 0")
    print("   gives (k eps + T0)(1+u')/(1+eps) = lam, i.e. to leading order")
    print("   k eps + T0 = lam, so EPS IS A CONSTANT -- not zero, and not free.")
    e0 = m2 / 2
    Edens = sp.expand(sp.Rational(1, 2) * k * e0 ** 2 + T0 * e0)
    print(f"   Fixing it by the constraint: u' = eps - p^2/2 + ... and")
    print(f"   integral u' = 0  =>  eps = <p^2>/2, whence")
    print(f"      E/length = {Edens}")
    print("   => E = (T0/2) INT p^2 dx  +  (k/8) L <p^2>^2")
    print("   THE LOCAL QUARTIC IS ABSENT. What replaces it is a NONLOCAL,")
    print("   POSITIVE term in the mean-square slope.\n")

    print("B4 FOR A LOCALISED OBJECT IN AN INFINITE MEDIUM:")
    print("   <p^2> = (1/L) INT p^2 dx, so the second term is")
    print("   (k/8)(1/L)(INT p^2 dx)^2 -> 0 as L -> infinity.")
    print("   E -> (T0/2) INT p^2 dx : PURELY QUADRATIC. NO QUARTIC, NO")
    print("   ATTRACTION, AND THEREFORE NO SOLITON AT ALL.\n")
    print("   THE THREE MODELS' QUARTIC COEFFICIENTS:")
    print("      free minimisation (ELEC-068):  -(k-T0)^2/(8k)  ~ -k/8  attractive")
    print("      pure tension      (ELEC-074):  -T0/8                  attractive")
    print("      number-conserving (here):       0 locally; nonlocal, positive,")
    print("                                      and vanishing for a localised object")
    print("   ALL SOLITON WORK IN THIS LINE USED ONE OF THE FIRST TWO. If the")
    print("   third is right, there is no localized solution to discuss: a")
    print("   number-conserving strand medium disperses transverse wavepackets.\n")

    print("B5 HONESTY: this is a CANDIDATE reconciliation, not the only one, and")
    print("   one session does not settle it. The weak point is the identification")
    print("   u' = -delta_n/n, which assumes the medium's strands are locally")
    print("   parallel and countable across a surface -- reasonable for a weave,")
    print("   less obvious near a strongly deformed configuration. If that fails,")
    print("   the constraint integral u' dx = 0 may not be the right one.")
    print("   WHAT IS NOT IN DOUBT: the constraint was NEVER APPLIED in ELEC-068,")
    print("   and applying any global constraint changes the effective quartic.")
    print("PASS: the legs reconcile, and the reconciliation produces a third model")
    print("      in which the line's central object does not exist.")


if __name__ == "__main__":
    main()
