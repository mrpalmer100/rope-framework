"""GRV-062 -- THE TARGET REDUCED: R5 is a G-free ratio, and GRV-020 puts the
structural requirements on Derived footing.

Bars locked in analysis/GRV062_ratio_target_bars_LOCKED.md BEFORE computing.
"""
import sympy as sp


def main():
    G, M, J, c, r, th = sp.symbols("G M J c r theta", positive=True)

    print("B1 DOES GRV-020 CHANGE THE FOOTING?")
    print("   GRV-020 (Derived), Corollary 2 -- the ANGULAR NO-MONOPOLE LEMMA:")
    print("     'zero net torque (statics) + zero net winding (neutrality) force")
    print("      DIPOLE-LED SOURCING'")
    print("   GRV-061 argued the monopole vanishes from J being a pseudovector.")
    print("   That argument is correct and it is now unnecessary: the corpus")
    print("   already holds the result as a DERIVED THEOREM, from two independent")
    print("   premises (statics and neutrality) rather than from symmetry alone.")
    print("   R2 (1/r^3 far field) and R3 (dipole structure) MOVE FROM A MODELLED")
    print("   ARGUMENT TO DERIVED FOOTING.")
    print("   NOTE ON PROCESS: this claim was never cited in the frame-dragging")
    print("   arc -- not by GRV-055, -056, -057, -058, -059, -060 or -061. It is")
    print("   the second time in this arc that the corpus already held what an")
    print("   audit went looking for.\n")

    print("B2 IS AN ABSOLUTE AMPLITUDE OBTAINABLE AT ALL?")
    print("   GRV-006 (Derived): G is NOT derivable from current commitments; it")
    print("   is inverse-measured. So an absolute gravitomagnetic amplitude was")
    print("   NEVER available to this framework -- not because of the twist route,")
    print("   but because the whole gravity sector calibrates G from measurement.")
    print("   R5 AS PREVIOUSLY POSED ('derive the numerical coefficient') WAS THE")
    print("   WRONG TARGET. It asked for something the sector cannot supply for")
    print("   ANY gravitational quantity, including the Newtonian one it already")
    print("   reproduces.\n")

    print("B3 THE REDUCTION:")
    h00 = 2 * G * M / (c ** 2 * r)
    gtphi = 2 * G * J * sp.sin(th) ** 2 / (c ** 3 * r)
    ratio = sp.simplify(gtphi / h00)
    print(f"   gravitoelectric   h_00   = {h00}")
    print(f"   gravitomagnetic   g_tphi = {gtphi}  (slow rotation)")
    print(f"   RATIO                     = {ratio}")
    assert G not in ratio.free_symbols
    print("   G CANCELS EXACTLY. The ratio is (J/Mc) sin^2(theta) -- pure")
    print("   kinematics, no gravitational coupling in it.")
    print("   AND THIS IS WHAT LENSE-THIRRING ACTUALLY TESTS: the Newtonian field")
    print("   is independently calibrated, so the measurement probes the RATIO of")
    print("   the two sectors, not the absolute strength of either.\n")

    print("B4 THE NEW TARGET, and the rescore:")
    print("   R5 RESTATED: does the framework give")
    print("      gravitomagnetic / gravitoelectric = J/(Mc) x sin^2(theta) ?")
    print("   A dimensionless, G-free question about the ratio of the twist-dipole")
    print("   sourcing to the mass-monopole sourcing the corpus already has.")
    rows = [("R1 total-J dependence", "MET",
             "dipole moment is J, linear by construction"),
            ("R2 1/r^3 far field", "MET (Derived footing)", "GRV-020 Corollary 2"),
            ("R3 dipole structure", "MET (Derived footing)", "GRV-020 Corollary 2"),
            ("R4 sign", "OPEN", "uncomputed"),
            ("R5 ratio to the static sector", "OPEN, WELL POSED",
             "G-free target J/(Mc); replaces the ill-posed absolute coefficient"),
            ("R6 static-sector consistency", "OPEN",
             "must not disturb GRV-029's one-metric result")]
    for n, v, w in rows:
        print(f"   {n:32s} {v:24s} {w}")
    print()

    print("B5 WHAT REDUCING A TARGET DOES NOT DO:")
    print("   It does not meet it. Nothing here computes the framework's ratio --")
    print("   this session establishes only that the ratio is the right quantity,")
    print("   that it is G-free, and that the structural requirements around it now")
    print("   rest on a Derived theorem rather than on a symmetry argument.")
    print("   THE ROUTE IS NOT CLOSED. What must still be done: compute the")
    print("   twist-dipole moment a rotating knot sources, in the same static")
    print("   force-and-torque framework GRV-005 used for mass, and divide by that")
    print("   claim's monopole sourcing. If the quotient is J/(Mc), the framework")
    print("   reproduces Lense-Thirring with no free parameter. If it is not, the")
    print("   route dies with a number rather than an argument.")
    print("PASS: the target is reduced to something G-free and well posed, and two")
    print("      structural requirements move to Derived footing.")


if __name__ == "__main__":
    main()
