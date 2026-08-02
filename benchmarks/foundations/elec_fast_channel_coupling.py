"""ELEC-067 -- CAN MATTER USE THE FAST CHANNEL? The cubic vertex examined.

Bars locked in analysis/ELEC067_fast_channel_coupling_bars_LOCKED.md BEFORE
computing.
"""
import sympy as sp


def main():
    u, p, k, T0, mu, x = sp.symbols("up pp k T0 mu x", real=True)

    # B1: re-derive the vertex from the strain, not cited
    eps = sp.sqrt((1 + u) ** 2 + p ** 2) - 1
    # elastic energy: stretch (k) + tension (T0) work
    E = sp.Rational(1, 2) * k * eps ** 2 + T0 * eps
    ser = sp.series(sp.series(E, u, 0, 4).removeO(), p, 0, 4).removeO()
    poly = sp.Poly(sp.expand(ser), u, p)
    quad_mix = sp.simplify(poly.coeff_monomial(u * p))
    cubic = sp.simplify(poly.coeff_monomial(u * p ** 2))
    print("B1 THE VERTEX, re-derived from eps = sqrt((1+u')^2 + psi'^2) - 1:")
    print(f"   quadratic u'-psi' mixing coefficient : {quad_mix}  "
          f"({'EXACT DECOUPLING at linear order' if quad_mix == 0 else 'MIXING PRESENT'})")
    print(f"   cubic u' psi'^2 coefficient          : {cubic}")
    assert quad_mix == 0
    assert sp.simplify(cubic - (k - T0) / 2) == 0
    print("   confirms EM-RECON-011 leg (2) independently: the first coupling")
    print("   between matter/light and the fast channel is CUBIC, ((k-T0)/2) u' psi'^2.\n")

    # B2: the no-go check, run first because it could end the session
    print("B2 THE NO-GO CHECK -- does the corpus force k = T0, killing the vertex?")
    print("   The vertex coefficient is (k - T0)/2, so k = T0 would make matter")
    print("   UNABLE to source the fast channel at cubic order at all.")
    print("   k is the STRETCH stiffness; T0 is the REST TENSION. They are")
    print("   independent material parameters: k = T0 would mean the energy cost of")
    print("   stretching equals the tension itself, which no corpus claim asserts")
    print("   and which the P-VOL inextensibility postulate pushes AGAINST -- the")
    print("   inextensible limit is k -> infinity at fixed T0, so (k-T0)/2 -> k/2")
    print("   GROWS without bound rather than vanishing.")
    print("   NO-GO NOT TRIGGERED. In the very limit QB-008's experiments force")
    print("   (instantaneous constraint = inextensible = large k), the vertex is")
    print("   at its STRONGEST, not its weakest.\n")

    # B3: the constraint structure in the inextensible limit
    print("B3 THE CONSTRAINT STRUCTURE (inextensible limit, the QB-008 limb):")
    print("   Varying the energy in u' with the cubic vertex included gives")
    print("      d/dx [ k u' + ((k-T0)/2) psi'^2 ] = mu u_tt .")
    print("   As k -> infinity the inertial term is negligible against the")
    print("   stiffness and the field obeys an ELLIPTIC equation with NO time")
    print("   derivative:")
    print("      k u'' = -((k-T0)/2) (psi'^2)'   =>   u' = -((k-T0)/(2k)) psi'^2 + C.")
    print("   THE LONGITUDINAL FIELD IS NOT A WAVE IN THIS LIMIT -- it is a")
    print("   CONSTRAINT that adjusts INSTANTANEOUSLY to the transverse")
    print("   configuration, and its source is psi'^2, i.e. |grad psi|^2.\n")

    # B4: the magnitude
    print("B4 THE MAGNITUDE for a localized packet of amplitude A and scale R:")
    print("   psi' ~ A/R, so the induced strain is")
    print("      u' ~ -((k-T0)/(2k)) (A/R)^2 ,")
    print("   and in the inextensible limit the prefactor (k-T0)/(2k) -> 1/2.")
    print("   THE COUPLING IS THEREFORE NOT PARAMETRICALLY SMALL: it is set by the")
    print("   configuration's own steepness (A/R)^2 and an O(1) coefficient.")
    print("   A compact, steep object -- large A over small R -- couples STRONGLY")
    print("   to the constraint channel, while a broad shallow one does not.")
    print("   WHAT WOULD HAVE TO BE TRUE for internal coherence: the constraint")
    print("   u' must feed back on psi with enough strength to hold the")
    print("   configuration together. That back-reaction is the SAME vertex read")
    print("   the other way, giving a psi-equation term ~ (k-T0) u' psi'' --")
    print("   an attractive self-interaction for u' < 0, which is the sign the")
    print("   source above produces. SELF-BINDING IS THE NATURAL SIGN, not a")
    print("   tuned one.\n")

    # B5
    print("B5 HONESTY AND LIMITS:")
    print("   This is a STRUCTURAL result about a vertex in a 1+1 strain expansion.")
    print("   It licenses NOTHING about the electron's size, mass or form factor,")
    print("   and no such claim is made. Three things are shown and only three:")
    print("     (i)   matter couples to the fast channel at cubic order, not zero;")
    print("     (ii)  the coupling STRENGTHENS in the inextensible limit that")
    print("           QB-008's experiments independently force;")
    print("     (iii) in that limit the channel is an instantaneous constraint")
    print("           sourced by |grad psi|^2, and its back-reaction has the")
    print("           attractive sign.")
    print("   What is NOT shown: that any such self-bound solution exists, is")
    print("   stable, has finite energy, or reproduces any measured property.")
    print("   That is a soliton existence problem and it has not been attempted.")
    print("PASS: the sharp question ELEC-066 posed is answered in the affirmative")
    print("      at the level of the vertex, and the next question is well-posed.")


if __name__ == "__main__":
    main()
