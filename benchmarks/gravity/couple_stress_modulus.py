"""GRV-072 -- K_0 ATTEMPTED: the continuum limit is clean and the unit conversion
needs a quantity the corpus has never registered.

Bars locked in analysis/GRV072_K0_bars_LOCKED.md BEFORE computing.
"""
import sympy as sp

T_SETS = {"Sigma-route": 1.70e3, "lattice-anchored": 1203.0}


def main():
    a, kt = sp.symbols("a k_t", positive=True)

    print("B1 THE MODEL AS WRITTEN (strand_twist_transport.py):")
    print("   E = 0.5*kt*sum((delta phi)^2) + sum(1 - cos phi),  kt = w^2")
    print("   A discrete sine-Gordon chain in the TWIST ANGLE. kt is the gradient")
    print("   stiffness in LATTICE UNITS; w is the kink width in spacings. The")
    print("   second term is the on-site periodic potential -- the medium's")
    print("   DISCRETENESS, which is what produces the Peierls-Nabarro barrier")
    print("   FND-STRAND-002 measured.\n")

    print("B2 THE CONTINUUM LIMIT:")
    print("   with spacing a, (delta phi)^2 = a^2 (dphi/ds)^2 and sum -> (1/a) int ds")
    print(f"   E = (kt a/2) int (dphi/ds)^2 ds   =>   gamma = {kt * a} per strand")
    print("   (in the model's own energy units).\n")

    print("B3 DIMENSIONAL CHECK:")
    print("   GRV-068's operator carries (gamma/2)|k phi|^2 with phi DIMENSIONLESS,")
    print("   so [gamma] = energy/length -- THE SAME UNITS AS TENSION.")
    print("   That is consistent and it is a real check: the massless-mode")
    print("   stiffness K_0 is a TENSION-LIKE modulus, not an area- or")
    print("   volume-scaled one. Nothing in the chain contradicts it.\n")

    print("B4 THE UNIT CONVERSION -- and it does not close:")
    print("   kt = w^2 is stated RELATIVE TO AN ON-SITE POTENTIAL OF UNIT")
    print("   AMPLITUDE. In the continuum medium that potential is a DISCRETENESS")
    print("   ARTEFACT -- the Peierls term -- not a physical bulk energy. So the")
    print("   model fixes the RATIO of gradient stiffness to lattice barrier, and")
    print("   that ratio is exactly what FND-STRAND-002 used it for.")
    print("   CONVERTING kt TO JOULES PER METRE NEEDS THE STRAND'S PHYSICAL")
    print("   TORSIONAL RIGIDITY, which the corpus has never registered anywhere.")
    print("   THE MODEL WAS BUILT TO STUDY TRANSPORT, AND IT MEASURES TRANSPORT.")
    print("   It does not carry an absolute modulus and was never asked to.\n")

    print("   A DIMENSIONAL ESTIMATE, offered as an estimate:")
    print("   if the only scales available are the tension T and the spacing a,")
    print("   the unique combination with units of energy/length is gamma ~ T")
    print("   times a dimensionless factor. Taking that factor as O(1):")
    for lab, T0 in T_SETS.items():
        print(f"      {lab:18s} gamma ~ {T0:.3e} J/m   (O(1) factor unknown)")
    print("   THE ASSUMPTION, stated as one: that a strand's torsional rigidity is")
    print("   set by its TENSION rather than by an independent elastic modulus.")
    print("   For a real rod those are different -- torsional rigidity is a shear")
    print("   modulus times a polar moment, and a tensioned string with no shear")
    print("   modulus has no torsional stiffness at all. THE CORPUS HAS NEVER")
    print("   SAID WHICH ITS STRANDS ARE.\n")

    print("B5 THE OUTCOME:")
    print("   K_0 IS NOT DERIVED. What is established:")
    print("     - the continuum form, gamma = kt a per strand, cleanly;")
    print("     - the dimensional class, energy/length, tension-like, consistent")
    print("       with GRV-068's operator;")
    print("     - and the precise reason the number does not follow: the twist")
    print("       model fixes a RATIO to the lattice barrier, not an absolute")
    print("       modulus, because it was built to study transport.")
    print("   AN ESTIMATE gamma ~ T is available at O(1) IF strand torsional")
    print("   rigidity is tension-set, which is unestablished and is a genuine")
    print("   physical question about what a strand is.")
    print("   SO GRV-071's COUNT STANDS AT FOUR ABSENT AND ONE ESTIMATED, not")
    print("   four and one derived. The fifth coefficient turned out to need a")
    print("   constitutive fact about strands that the corpus has not registered.")
    print("PASS: the continuum limit and dimensional class are established, the")
    print("      absolute value is not, and the estimate is labelled as one.")


if __name__ == "__main__":
    main()
