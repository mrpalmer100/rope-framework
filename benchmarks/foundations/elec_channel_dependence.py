"""ELEC-076 -- DOES THE SURVIVING SOLITON NEED THE FAST CHANNEL? No -- and the
two energy functionals used in this line disagree by eight orders.

Bars locked in analysis/ELEC076_channel_dependence_bars_LOCKED.md BEFORE computing.
"""
import sympy as sp

K_OVER_T0 = 1.9e8   # QB-008, Bell timing


def main():
    p, k, T0 = sp.symbols("p k T0", positive=True)
    E_lab = T0 * (sp.sqrt(1 + p ** 2) - 1)
    q_lab = sp.Poly(sp.expand(sp.series(E_lab, p, 0, 8).removeO()), p).coeff_monomial(p ** 4)
    q_elim = -(k - T0) ** 2 / (8 * k)

    print("B1 THE TWO QUARTICS, never previously compared:")
    print(f"   (i)  eliminate-u (ELEC-068 B1):        {q_elim}")
    print(f"   (ii) pure tension (ELEC-071/074):      {sp.simplify(q_lab)}")
    sols = sp.solve(sp.Eq(q_lab, q_elim), k)
    print(f"   They agree ONLY at k/T0 = "
          f"{[round(float(s.subs(T0,1)),4) for s in sols]}")
    ratio = sp.simplify(q_elim / q_lab)
    print(f"   Their ratio is {ratio}, which is ~ k/T0 at large k.")
    print(f"   At the registered k/T0 >= {K_OVER_T0:.1e} they differ by EIGHT ORDERS.\n")

    print("B2 WHICH FUNCTIONAL DID THE EXACT WORK USE?")
    print(f"   ELEC-073/074/075 solved r^2 F(p) = C with F = dE/dp for")
    print(f"   E = T0(sqrt(1+p^2) - 1). Does k appear? {'k' in str(E_lab)}")
    print("   IT DOES NOT. The exact profile, the hard core, the scaling relations")
    print("   and the 1e37 mass failure were all computed from PURE TRANSVERSE")
    print("   TENSION GEOMETRY, with no longitudinal field and no stiffness k.\n")

    print("B3 THE ANSWER: NO. The surviving soliton does NOT require the fast")
    print("   channel. It is a feature of a string under tension displaced")
    print("   transversely -- the arc-length excess sqrt(1+p^2) - 1 and nothing")
    print("   more. The longitudinal sector, its cubic vertex, its instantaneous")
    print("   constraint structure and its Bell-timing stiffness bound play NO")
    print("   role in ELEC-073, ELEC-074 or ELEC-075.\n")

    print("B4 THE CONSEQUENCE FOR ELEC-067..070, not minimised:")
    print("   ELEC-067's cubic vertex and its no-go check STAND as statements")
    print("   about matter's coupling to the longitudinal sector -- they were")
    print("   derived independently and remain true.")
    print("   ELEC-068's effective quartic, ELEC-069's steepness window and")
    print("   ELEC-070's sextic sign were all computed from the ELIMINATE-U")
    print("   functional, which the exact line did not use and which disagrees")
    print("   with it by k/T0. Those three claims describe a DIFFERENT MODEL from")
    print("   the one ELEC-073..075 solved. Their internal arithmetic is not in")
    print("   question; their connection to the exact results is.")
    print("   THE LINE CONTAINS TWO MODELS THAT WERE TREATED AS ONE.\n")

    print("B5 NO REPAIR ATTEMPTED. Which functional is physical depends on what")
    print("   the medium does when a strand is displaced transversely -- whether")
    print("   it shortens at constant tension (giving the pure-tension form) or")
    print("   resists with stiffness k (giving the eliminate-u form). That is a")
    print("   real physical question about the framework and it has not been")
    print("   answered. Registering the inconsistency is the whole of this claim.")
    print("   NOTE THE DIRECTION: the pure-tension quartic is WEAKER by k/T0, so")
    print("   the exact line used the LESS attractive of the two -- the mass")
    print("   failure would only worsen under the other, since a stronger")
    print("   attraction gives a smaller object at the same excursion.")
    assert float(sp.simplify(q_elim/q_lab).subs({k: K_OVER_T0, T0: 1})) > 1e7
    print("PASS: the question is answered -- no fast channel required -- and an")
    print("      internal inconsistency of the line is registered.")


if __name__ == "__main__":
    main()
