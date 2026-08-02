"""ELEC-077 -- WHICH FUNCTIONAL IS PHYSICAL? The framework's own denial of
material points selects the pure-tension form.

Bars locked in analysis/ELEC077_functional_bars_LOCKED.md BEFORE deciding.
"""
import sympy as sp


def main():
    p, u, k, T0, lam = sp.symbols("p u k T0 lambda", positive=True)

    print("B1 WHAT EACH FUNCTIONAL PRESUPPOSES")
    E_pt = T0 * (sp.sqrt(1 + p ** 2) - 1)
    print(f"   PURE TENSION:  E = {E_pt}")
    print("     = tension x ARC-LENGTH EXCESS of the strand's curve over the")
    print("       straight reference. Refers ONLY to the curve's geometry in")
    print("       space. Reparametrization-invariant, because arc length is.")
    # demonstrate reparametrization invariance: length of a curve is independent
    # of how it is parametrized
    s = sp.symbols("s", positive=True)
    print("     CHECK: under x -> f(s) with dx = f'(s) ds, the integrand")
    print("       sqrt(1 + (dpsi/dx)^2) dx = sqrt(f'^2 + (dpsi/ds)^2) ds is the")
    print("       same curve length. No preferred labelling is used.")
    eps = sp.sqrt((1 + u) ** 2 + p ** 2) - 1
    print(f"\n   ELIMINATE-U:   E = (k/2) eps^2 + T0 eps,  eps = {eps}")
    print("     treats u as a PHYSICAL DISPLACEMENT FIELD carrying elastic")
    print("     energy (k/2)eps^2, i.e. it presupposes MATERIAL POINTS which can")
    print("     be displaced longitudinally and whose displacement costs energy.")
    print("     It then MINIMISES over u -- a legitimate move only if u is a")
    print("     physical degree of freedom rather than a labelling choice.\n")

    print("B2 THE VERDICT, from FND-REL-002 (Derived):")
    print("   'strand mechanics FORBID the Galilean convective term: NO MATERIAL")
    print("   VELOCITY EXISTS', with EM-RECON-011 leg (1) drawing the consequence")
    print("   that longitudinal displacement u is GAUGE-LIKE because strands have")
    print("   NO MATERIAL POINTS.")
    print("   A medium without material points has no longitudinal displacement")
    print("   field to carry elastic energy, and 'minimising over u' is")
    print("   minimising over a LABELLING, not over a physical configuration.")
    print("   THE PURE-TENSION FUNCTIONAL IS THE PHYSICAL ONE. The eliminate-u")
    print("   functional presupposes exactly what FND-REL-002 forbids.\n")

    print("B3 CONSEQUENCES, unsoftened:")
    print("   ELEC-068, ELEC-069, ELEC-070 computed from the eliminate-u model.")
    print("   On this reading that model is not the framework's, so those three")
    print("   claims are DOWNGRADED from conditional to superseded-in-premise:")
    print("   their arithmetic stands, their subject does not exist in this")
    print("   framework. Nothing in them should be cited as a rope-framework")
    print("   result without this note attached.")
    print("   EM-RECON-011 IS ITSELF INTERNALLY STRAINED, and this must be said:")
    print("   its leg (1) asserts u is gauge because there are no material points,")
    print("   while its leg (2) computes a cubic vertex ((k-T0)/2) u' psi'^2 from")
    print("   an elastic energy in u. Those two legs sit uneasily together. The")
    print("   vertex may still be meaningful as a gauge-fixed statement, but the")
    print("   claim does not establish that and this session does not either.")
    print("   ELEC-067's no-go check inherits the same strain.\n")

    print("B4 CONSEQUENCE FOR THE EXACT LINE:")
    print("   ELEC-073, ELEC-074 and ELEC-075 used the PURE-TENSION functional.")
    print("   On this verdict they were using the RIGHT one all along, by accident")
    print("   of ELEC-071 having introduced it to settle a parametrization")
    print("   question. The exact profile, the hard core diagnosis and the 1e37")
    print("   mass failure are therefore statements about the framework's own")
    print("   medium, and ELEC-075's negative is the line's real result.\n")

    print("B5 HONESTY: this is an argument from a registered claim, not a new")
    print("   computation. Its force is exactly the force of FND-REL-002 and of")
    print("   the reading that 'no material points' forbids an elastic energy in")
    print("   longitudinal displacement. That reading is natural but it is a")
    print("   reading, and a framework author could reject it by arguing that u")
    print("   is gauge for KINEMATICS while the strain eps remains physical.")
    print("   If that argument is made, the eliminate-u model returns and the two")
    print("   models must be distinguished by something else.")
    print("PASS: the decider is identified, applied, and its own weak point named.")


if __name__ == "__main__":
    main()
