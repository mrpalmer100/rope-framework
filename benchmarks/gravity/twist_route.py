"""GRV-060 -- THE TWIST ROUTE: the medium's own twist sector supplies the right
STRUCTURE for gravitomagnetism, and not yet a coefficient.

Bars locked in analysis/GRV060_twist_route_bars_LOCKED.md BEFORE computing.
"""
import sympy as sp


def main():
    t, x = sp.symbols("t x")
    lam, tau = sp.symbols("lambda tau", real=True)
    u = sp.Function("u")(t, x)

    print("B1 DOES A TWIST-DENSITY COUPLING PRODUCE A STATIONARY SHIFT?")
    L = lam * tau * sp.diff(u, t) * sp.diff(u, x)
    el = sp.expand(sp.diff(sp.diff(L, sp.diff(u, t)), t)
                   + sp.diff(sp.diff(L, sp.diff(u, x)), x))
    print(f"   L = lambda tau_a (d_t u)(d_a u)  ->  EL term: {el}")
    print("   A MIXED d_t d_a term with coefficient 2 lambda tau_a: this IS a")
    print("   shift, with g_0a proportional to the twist density.")
    print("   AND IT IS STATIONARY IF tau_a IS. That is exactly the property")
    print("   GRV-058's mechanism lacked -- that one needed d_t of the field,")
    print("   this one needs only a standing twist.\n")

    print("B2 WHAT TWIST DOES A ROTATING BODY PRODUCE? Classical elasticity, not")
    print("   assumption -- the rotating-sphere (Reissner-Sagoci) solution for a")
    print("   sphere driven about its axis in an infinite medium of shear modulus G:")
    r, th, M, G = sp.symbols("r theta M G", positive=True)
    u_phi = M * sp.sin(th) / (8 * sp.pi * G * r ** 2)
    print(f"      u_phi = {u_phi}")
    rot = sp.simplify(sp.diff(u_phi, r))
    print(f"      local rotation ~ d(u_phi)/dr = {rot}")
    print("   R2 FAR FIELD: the rotation field falls as 1/r^3. MET.")
    print("   R3 ANGULAR STRUCTURE: sin(theta)/r^2 in the displacement, giving the")
    print("      dipole form of (J x r)/r^3 in the rotation. MET.")
    print("   R1 J-DEPENDENCE: the amplitude is set by the driving torque, which")
    print("      for a body of angular momentum J is proportional to J in any")
    print("      steady-state balance. MET STRUCTURALLY.\n")

    print("B3 THE HONEST OBSTACLE, stated and not skipped:")
    print("   A body rotating steadily in a medium rigidly attached to it WINDS UP")
    print("   WITHOUT BOUND -- the twist grows linearly in time and there is no")
    print("   stationary state. A body that slips freely accumulates NO twist and")
    print("   sources nothing. Neither limit gives Lense-Thirring.")
    print("   The corpus does have the ingredient that could fix this: RECONNECTION")
    print("   (GRV-027's measured punch-through, GRV-045's 2-pi writhe exchange).")
    print("   Steady rotation would inject twist at a rate ~ omega and reconnection")
    print("   would relax it at a rate ~ Gamma, giving a stationary")
    print("      tau ~ omega / Gamma.")
    print("   THAT IS A REAL MECHANISM AND IT INTRODUCES A FREE PARAMETER. Gamma is")
    print("   not derived anywhere in the corpus, so the AMPLITUDE of the resulting")
    print("   gravitomagnetic field is undetermined -- and an undetermined")
    print("   amplitude cannot be compared with 37.2 mas/yr.\n")

    print("B4 SCORING AGAINST GRV-059's SIX REQUIREMENTS:")
    rows = [("R1 total-J dependence", "MET structurally",
             "torque balance is linear in J"),
            ("R2 1/r^3 far field", "MET",
             "classical rotating-sphere solution"),
            ("R3 (J x r)/r^3 dipole", "MET",
             "sin(theta)/r^2 displacement gives the dipole rotation"),
            ("R4 sign", "OPEN", "not computed; depends on the coupling's sign"),
            ("R5 coefficient", "NOT MET",
             "requires the reconnection relaxation rate Gamma, underived"),
            ("R6 static-sector consistency", "OPEN",
             "the twist coupling must not disturb GRV-029's one-metric result")]
    for name, verdict, why in rows:
        print(f"   {name:30s} {verdict:18s} {why}")
    print("   THREE OF SIX MET, all three STRUCTURAL. Two open, one NOT MET.\n")

    print("B5 THE CONSEQUENCE FOR GRV-059:")
    print("   ITS FAILED STATUS STANDS AS A STATEMENT ABOUT THE PRESENT ACTION --")
    print("   no registered term couples to a mass current, and that remains true.")
    print("   BUT ITS PESSIMISM IS QUALIFIED. GRV-059 said recovery would require a")
    print("   coupling 'not currently contained in the framework', implying the")
    print("   ingredients were absent. They are not: the medium has a registered")
    print("   twist sector, and elastostatics gives that sector exactly the radial")
    print("   and angular structure Lense-Thirring needs. The step-1 search looked")
    print("   for velocity and momentum density and did not consider TWIST, which")
    print("   is this medium's own vector quantity.")
    print("   THE CORRECTED POSITION: the gravity sector has no gravitomagnetic")
    print("   coupling and does possess the raw material for one, with the right")
    print("   structure and no derived amplitude. That is a live research problem,")
    print("   not a closed refutation -- and NOT a rescue either, until Gamma is")
    print("   derived and the sign and static-consistency are checked.")
    print("PASS: the operator's objection is substantially correct on structure,")
    print("      and does not yet supply a number.")


if __name__ == "__main__":
    main()
