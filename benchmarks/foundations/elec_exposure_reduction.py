"""ELEC-072 -- REDUCING THE EXPOSURE: the 3D soliton exists for BOTH signs of
the parametrization-dependent quartic.

Bars locked in analysis/ELEC072_exposure_bars_LOCKED.md BEFORE computing.
"""
import numpy as np
import sympy as sp


def scan(a, b, d, s):
    f = lambda l: a * l + s * b / l + d / l ** 3
    ls = np.logspace(-2, 2, 400000)
    i = int(np.argmin(f(ls)))
    h = 0.01 * ls[i]
    e2 = (f(ls[i] + h) - 2 * f(ls[i]) + f(ls[i] - h)) / h ** 2
    return ls[i], f(ls[i]), e2


def main():
    L, A, B, Dc = sp.symbols("L A B D", positive=True)
    print("3D Derrick terms: gradient +A L, quartic sB/L (s = sign), sextic +D/L^3")
    print("The SEXTIC is parametrization-robust (+1/16 both ways, ELEC-070/071);")
    print("only the QUARTIC's sign is contingent.\n")

    print("B1 BOTH SIGNS TESTED:")
    results = {}
    for s, lab in ((-1, "ATTRACTIVE  (lab parametrization, FND-REL-002 forced)"),
                   (+1, "REPULSIVE   (arclength, the description the framework denies)")):
        E = A * L + s * B / L + Dc / L ** 3
        print(f"   {lab}\n      E = {E},  dE/dL = {sp.simplify(sp.diff(E, L))}")
        for (a, b, d) in ((1.0, 1.0, 0.05), (1.0, 0.3, 0.2), (1.0, 2.0, 0.01)):
            Ls, Es, e2 = scan(a, b, d, s)
            results[(s, a, b, d)] = (Ls, Es, e2)
            print(f"      A={a} B={b} D={d}: L*={Ls:.4f}  E(L*)={Es:+.4f}  "
                  f"E''={e2:+.2f} -> {'MINIMUM' if e2 > 0 else 'NO MINIMUM'}")
    assert all(v[2] > 0 for v in results.values())
    print("\n   EVERY CASE GIVES A STABLE MINIMUM. Both limits send E to +infinity")
    print("   for either sign -- the sextic diverges as L -> 0 and the gradient as")
    print("   L -> infinity -- so a minimum is guaranteed between them REGARDLESS")
    print("   of the quartic's sign. EXISTENCE DOES NOT DEPEND ON THE")
    print("   PARAMETRIZATION.\n")

    print("B2 WHAT STILL DEPENDS ON THE SIGN, stated without overstating the win:")
    print("   the LOCATION of the minimum, its DEPTH, and the binding energy's")
    print("   sign. Comparing matched parameters:")
    for (a, b, d) in ((1.0, 1.0, 0.05), (1.0, 0.3, 0.2)):
        la, ea, _ = results[(-1, a, b, d)]
        lr, er, _ = results[(+1, a, b, d)]
        print(f"      A={a} B={b} D={d}: L* {la:.4f} (attractive) vs {lr:.4f} "
              f"(repulsive), factor {lr/la:.2f}; E(L*) {ea:+.3f} vs {er:+.3f}")
    print("   So ELEC-071's exposure is REDUCED, not removed: FND-REL-002 still")
    print("   fixes the object's SIZE and ENERGY, but no longer its EXISTENCE.\n")

    print("B3 THE BINDING ENERGY:")
    print("   With the attractive quartic E(L*) can be NEGATIVE -- the configuration")
    print("   sits below the zero of the expansion. With the repulsive quartic it is")
    print("   positive. Neither means the object disperses: both limits cost")
    print("   infinite energy at fixed amplitude, so L* is a genuine global minimum")
    print("   under scaling either way. What the sign controls is whether the")
    print("   localized state is energetically favourable relative to the uniform")
    print("   medium, which is a question about FORMATION, not about existence.\n")

    print("B4 WHAT DERRICK SCALING CANNOT SEE:")
    print("   it varies ONE parameter -- the width -- at fixed profile shape and")
    print("   fixed amplitude. A minimum under scaling is NOT a proof of stability:")
    print("   the configuration may be unstable to shape changes, to amplitude")
    print("   changes, or to splitting, none of which this test explores. The")
    print("   result is a necessary condition that has been met, not a solution.")
    print("PASS: existence is parametrization-independent; the exposure is reduced")
    print("      to size and energy, and the topological fallback is not needed.")


if __name__ == "__main__":
    main()
