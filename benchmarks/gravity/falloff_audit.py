"""GRV-063 -- THE FALLOFF AUDIT: GRV-060's R2 was scored wrong, the lemma kills
the rotlet, and the real question is whether the medium is micropolar.

Bars locked in analysis/GRV063_falloff_bars_LOCKED.md BEFORE computing.
"""
import sympy as sp


def main():
    r, J, th = sp.symbols("r J theta", positive=True)

    print("B1 FALLOFF, stated carefully:")
    mag = sp.simplify(J * r * sp.sin(th) / r ** 3)
    print(f"   |(J x r)/r^3| = J r sin(theta)/r^3 = {mag}")
    print("   THE SHIFT FALLS AS 1/r^2. The r^3 is in the formula; the falloff is")
    print("   one power slower, because the numerator carries a factor of r.")
    print("   GRV-060 scored 'R2 1/r^3 far field MET' by matching a 1/r^3 ROTATION")
    print("   field to the FORM (J x r)/r^3. THAT MATCH WAS WRONG -- it compared a")
    print("   falloff to a formula. R2 IS WITHDRAWN as scored.\n")

    print("B2 THE ELASTIC ANGULAR LADDER:")
    print("   ROTLET (torque monopole): u_phi ~ M/r^2, local rotation ~ 1/r^3")
    print("   TORQUE DIPOLE:            u ~ 1/r^3,     local rotation ~ 1/r^4\n")

    print("B3 THE LEMMA'S BITE:")
    print("   GRV-017 (Derived) and GRV-020 (Derived): a static isolated defect")
    print("   exerts ZERO NET FORCE and ZERO NET TORQUE -- otherwise it linearly or")
    print("   angularly accelerates, contradicting statics. A steadily rotating")
    print("   body has zero angular ACCELERATION, so zero net torque.")
    print("   THE ROTLET AMPLITUDE VANISHES. The angular ladder starts at the")
    print("   torque dipole, whose rotation falls as 1/r^4.")
    print("   AGAINST A REQUIRED 1/r^2, that is off by TWO POWERS if the shift")
    print("   couples to twist density, and by ONE if it couples to displacement.\n")

    print("B4 THE ESCAPE -- IS TORQUE EVEN THE RIGHT SOURCE? It is not, and this")
    print("   is the session's real finding:")
    print("   In general relativity frame dragging is sourced by ANGULAR MOMENTUM")
    print("   J, not by torque. A body spinning at constant rate has constant J and")
    print("   exerts NO TORQUE. So matching J to a rotlet -- which is a TORQUE")
    print("   source -- was the wrong analogy from the start, and the lemma that")
    print("   kills the rotlet does not touch J at all.")
    print("   DOES STANDARD ELASTICITY HAVE A SOURCE THAT CARRIES ANGULAR MOMENTUM")
    print("   WITHOUT TORQUE? NO. Classical elasticity has no intrinsic spin: its")
    print("   angular content is entirely orbital, carried by the displacement")
    print("   field, and a static source with zero net torque has no standing")
    print("   angular source term.")
    print("   COSSERAT (MICROPOLAR) MEDIA DO. A Cosserat continuum carries an")
    print("   independent microrotation field and an intrinsic spin density, and")
    print("   supports couple stresses that classical elasticity lacks.")
    print("   AND THIS CORPUS'S STRANDS ARE FRAMED. FND-STRAND-002/003 give every")
    print("   strand an explicit twist field on its nodes with a Calugareanu")
    print("   ledger -- which IS a microrotation degree of freedom. THE MEDIUM MAY")
    print("   BE MICROPOLAR, and if it is, it has exactly the source class that")
    print("   classical elasticity lacks and that angular momentum requires.\n")

    print("B5 VERDICT:")
    print("   CORRECTED: GRV-060's R2 was scored by comparing a falloff to a")
    print("   formula and is withdrawn. Its R3 (dipole angular structure) stands --")
    print("   GRV-020 gives dipole-led sourcing as a theorem, and that is about")
    print("   angular structure, not falloff.")
    print("   AND THE ELASTOSTATIC ANALOGY GRV-060 USED IS THE WRONG ONE: a rotlet")
    print("   is torque-sourced, the lemma kills torque monopoles, and J is not a")
    print("   torque.")
    print("   THE REMAINING QUESTION, stated and NOT decided: does the framed-strand")
    print("   medium constitute a Cosserat continuum with an intrinsic spin density,")
    print("   and if so what falloff does a steady spin density source? That is a")
    print("   question about the medium's constitutive structure, the corpus has the")
    print("   ingredient (framed strands with measured twist transport), and nobody")
    print("   has asked it.")
    print("   THE ROUTE IS NEITHER CLOSED NOR ADVANCED. It is correctly posed for")
    print("   the first time.")
    print("PASS: an error in my own prior scoring is corrected, the wrong analogy")
    print("      identified, and the right question named without being answered.")


if __name__ == "__main__":
    main()
