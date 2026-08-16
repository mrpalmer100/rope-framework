"""GRV-111 -- COMMISSION NUN-GRV7: THE lambda-DERIVATION ATTEMPT.

Bars locked in analysis/NUNGRV7_lambda_derivation_bars_LOCKED.md
BEFORE this script was written. Grant condition (1) of GRV-110.
Clean-room held. Permitted inventory: registered Kirchhoff structure,
strand twist transport, topological bookkeeping.
"""
import sympy as sp


def main():
    print("STEP 1 -- THE STRAIGHT-CONFIGURATION TEST (symbolic, per bars):")
    s, t = sp.symbols("s t")                    # arclength, time
    E, G, I, Ip, mu_l, rho_j, lam = sp.symbols(
        "E G I I_p mu_l rho_j lambda", positive=True)
    y = sp.Function("y")(s, t)                  # transverse displacement
    ph = sp.Function("phi")(s, t)               # twist about the tangent
    # Kirchhoff quadratic Lagrangian about the STRAIGHT configuration,
    # built from the registered elastic set (GRV-009: torsion ~ r^4 rod;
    # GRV-073: E, G possessed):
    L = (sp.Rational(1, 2) * mu_l * sp.diff(y, t) ** 2
         - sp.Rational(1, 2) * E * I * sp.diff(y, s, 2) ** 2
         + sp.Rational(1, 2) * rho_j * sp.diff(ph, t) ** 2
         - sp.Rational(1, 2) * G * Ip * sp.diff(ph, s) ** 2)
    # Every cross bilinear between the twist and bend sectors:
    crosses = []
    for da in (sp.diff(ph, t), sp.diff(ph, s)):
        for db in (sp.diff(y, t), sp.diff(y, s), sp.diff(y, s, 2)):
            crosses.append(sp.simplify(sp.diff(L, da, db)))
    print("   Kirchhoff quadratic L about the straight configuration:")
    print("   all twist-bend cross bilinears d2L/d(phi_.)d(y_.):")
    print(f"   {crosses}")
    assert all(c == 0 for c in crosses)
    print("   ALL IDENTICALLY ZERO. This is the known exact statement:")
    print("   about a straight rod, twist and bend DECOUPLE at quadratic")
    print("   order. Registered strand mechanics generates NO bilinear")
    print("   (grad phi) . u_t from the straight-strand mesh. lambda is")
    print("   NOT generated at the granted order from this inventory.\n")

    print("STEP 2 -- THE CHANNEL THAT EXISTS, at the order it exists:")
    print("   The corpus's topological bookkeeping conserves linking:")
    print("   Lk = Tw + Wr (the winding/linking class GG-006 commits to).")
    print("   d_t Tw = -d_t Wr, and the writhe rate about a NEARLY straight")
    print("   configuration is BILINEAR in the backbone:")
    print("     d_t Wr ~ integral (y' x y_t') . z_hat ds   (order u^2),")
    print("   so the twist-bend coupling from Lk conservation enters the")
    print("   action at CUBIC order (phi, y, y), not bilinear. Expanding")
    print("   that cubic vertex around a CURVED/ENTANGLED background")
    print("   y_bar(s) produces an EFFECTIVE bilinear:")
    print("     lambda_eff ~ (G Ip) x <kappa_bar>   (schematic),")
    print("   where <kappa_bar> is a mesh background curvature/entanglement")
    print("   statistic. THE COEFFICIENT EXISTS AS A CHANNEL; ITS VALUE")
    print("   REQUIRES <kappa_bar> -- and the registry contains NO measured")
    print("   or derived background curvature statistic for the mesh. Per")
    print("   the bars' named failure mode: an effective coupling around an")
    print("   unregistered background is NOT a derived constant.\n")

    print("STEP 3 -- WHAT WAS REFUSED (per bars B2):")
    print("   A dimensional assembly lambda ~ sqrt(mu gamma) x a was")
    print("   available and REFUSED: the GRV-073 lesson is that the real")
    print("   coefficient can sit orders below the dimensional estimate,")
    print("   and the writhe channel's <kappa_bar> suppression is exactly")
    print("   such a hidden factor. No number is quoted.\n")

    print("VERDICT (per bars B1): NOT-PINNED, with the structure located.")
    print("   (a) ZERO at bilinear order from straight strands -- shown")
    print("       symbolically, all cross bilinears identically zero;")
    print("   (b) the generation channel is the Lk-conservation twist-")
    print("       writhe exchange, cubic, yielding lambda_eff proportional")
    print("       to an UNREGISTERED mesh curvature statistic <kappa_bar>;")
    print("   (c) lambda therefore remains a granted free parameter, and")
    print("       GRANT CONDITION (4) STANDS INDEFINITELY: any LARES-class")
    print("       work is measurement framing, not a kill test.")
    print("   The honest reading of (a)+(b) together, stated at volume:")
    print("   the granted term is microscopically supported ONLY as an")
    print("   effective coupling of a curved mesh -- a mesh of straight")
    print("   strands gives lambda = 0 exactly. The named registrable")
    print("   route to a pin: derive or measure <kappa_bar> from the")
    print("   corpus's own mesh construction; that is a chartered-size")
    print("   question, not a session-size one.")


if __name__ == "__main__":
    main()
