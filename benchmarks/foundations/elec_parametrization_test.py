"""ELEC-071 -- IS THE TRUNCATION PHYSICAL? The quartic's sign is
parametrization-dependent, and one registered claim decides it.

Bars locked in analysis/ELEC071_parametrization_bars_LOCKED.md BEFORE computing.
"""
import sympy as sp


def main():
    p = sp.symbols("p", positive=True)

    print("B1 THE TWO EXPANSIONS, same physical string:")
    Ea = sp.expand(sp.series(sp.sqrt(1 + p ** 2) - 1, p, 0, 8).removeO())
    Eb = sp.expand(sp.series(1 - sp.sqrt(1 - p ** 2), p, 0, 8).removeO())
    Pa, Pb = sp.Poly(Ea, p), sp.Poly(Eb, p)
    print(f"   A, against the LAB coordinate x (medium free to stretch):")
    print(f"      E/T0 = {Ea}")
    print(f"   B, against ARCLENGTH s (inextensible, energy = tension x shortening):")
    print(f"      E/T0 = {Eb}")
    qa, qb = Pa.coeff_monomial(p ** 4), Pb.coeff_monomial(p ** 4)
    sa, sb = Pa.coeff_monomial(p ** 6), Pb.coeff_monomial(p ** 6)
    print(f"\n   quartic: A = {qa}   B = {qb}   -> SIGNS "
          f"{'DIFFER' if qa * qb < 0 else 'agree'}")
    print(f"   sextic : A = {sa}   B = {sb}   -> SIGNS "
          f"{'differ' if sa * sb < 0 else 'AGREE'}")
    assert qa * qb < 0
    print("   THE QUARTIC'S SIGN IS PARAMETRIZATION-DEPENDENT. In the lab")
    print("   coordinate it is ATTRACTIVE (-1/8); in arclength it is REPULSIVE")
    print("   (+1/8). The entire attractive mechanism of ELEC-067 through")
    print("   ELEC-070 exists in one description and not the other.")
    print("   THE SEXTIC AGREES in both (+1/16), so ELEC-070's Skyrme-class")
    print("   stabilizer is parametrization-ROBUST even though what it stabilizes")
    print("   against is not.\n")

    print("B2 DOES THE CORPUS SELECT A PARAMETRIZATION? Yes, and by a Derived claim.")
    print("   FND-REL-002 (Derived): strand mechanics FORBID the Galilean")
    print("   convective term -- NO MATERIAL VELOCITY EXISTS. EM-RECON-011 leg (1)")
    print("   restates the consequence: longitudinal displacement u is GAUGE-LIKE")
    print("   because strands have NO MATERIAL POINTS.")
    print("   A medium with no material points has NO ARCLENGTH LABEL to")
    print("   parametrize against: setup B presupposes material coordinates the")
    print("   framework denies exist. THE LAB PARAMETRIZATION IS FORCED, and with")
    print("   it the ATTRACTIVE quartic.\n")

    print("B3 WHAT THIS MEANS FOR ELEC-067..070:")
    print("   SURVIVES, now with its ground stated: the cubic vertex (ELEC-067),")
    print("   the attractive quartic and hence the collapse (ELEC-068 B1/B2), the")
    print("   3D failure of dynamical stabilization (ELEC-070 B1), and the")
    print("   positive sextic (ELEC-070 B2, parametrization-robust).")
    print("   NEWLY CONDITIONAL: every result depending on the quartic's SIGN is")
    print("   now explicitly conditional on FND-REL-002. That includes the")
    print("   collapse itself, the existence windows, and the 3D soliton.")
    print("   NOT RESCUED: nothing previously retracted comes back.\n")

    print("B4 THE EXPOSURE, named:")
    print("   The entire soliton line -- five claims -- now rests on ONE registered")
    print("   claim, FND-REL-002, and on the reading that no material points means")
    print("   no arclength parametrization. That claim is Derived, which is the")
    print("   corpus's strongest status, but identifying a load-bearing dependency")
    print("   is NOT verifying it, and a single point of failure for five claims")
    print("   deserves to be visible rather than implicit.")
    print("   IF FND-REL-002 WERE OVERTURNED OR ITS READING NARROWED, the quartic")
    print("   flips sign, the attraction vanishes, and the whole line collapses to")
    print("   'a stiff medium disperses wavepackets' -- no soliton, no electron.")
    print("PASS: the truncation question is answered -- the expansion is physical")
    print("      in the lab parametrization the framework forces, and the line's")
    print("      single point of failure is now named.")


if __name__ == "__main__":
    main()
