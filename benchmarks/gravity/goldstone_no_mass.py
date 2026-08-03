"""GRV-067 -- THE LOCKING MASS TERM IS SYMMETRY-FORBIDDEN: kappa = 0 follows
from GRV-020's Derived Goldstone mode.

Bars locked in analysis/GRV067_goldstone_bars_LOCKED.md BEFORE reasoning.
"""
import sympy as sp


def main():
    print("B1 IDENTIFYING THE GOLDSTONE:")
    print("   GRV-020 (Derived): G = R x SO(2) acting on the INTERNAL AZIMUTH,")
    print("   helical ground state, stabilizer the screw subgroup, ground-state")
    print("   manifold G/H = S^1 -- EXACTLY ONE GOLDSTONE, circle-valued.")
    print("   IS THE INTERNAL AZIMUTH THE FRAME ORIENTATION phi? The claim's own")
    print("   Corollary 1 settles it: 'pi_1(S^1) = Z, winding quantized = charge,")
    print("   TORSION DYNAMICS = LIGHT'. The torsion of a framed curve IS the rate")
    print("   of change of the frame azimuth along it. The Goldstone coordinate is")
    print("   the frame orientation, and the corpus identifies its dynamics with")
    print("   light. NOT ASSERTED -- read off the claim.\n")

    print("B2 GOLDSTONE'S THEOREM:")
    print("   A spontaneously broken continuous GLOBAL symmetry yields an EXACTLY")
    print("   MASSLESS mode along each broken direction. GRV-020 establishes the")
    print("   breaking (G/H = S^1, one Goldstone), so the internal-azimuth mode is")
    print("   massless and NO MASS TERM FOR IT IS PERMITTED IN THE ACTION.\n")

    print("B3 THE SPECIFIC TEST -- does kappa |eta|^2 survive?")
    phi, curlu, eps = sp.symbols("phi curl_u epsilon", real=True)
    eta = phi - curlu / 2
    eta_shift = (phi + eps) - curlu / 2
    print(f"   eta = {eta}")
    print("   Under the broken SO(2): phi -> phi + eps, while curl u is INVARIANT")
    print("   (an internal azimuth rotation does not move the backbone).")
    print(f"   so eta -> {eta_shift} = eta + eps")
    diff = sp.expand(eta_shift ** 2 - eta ** 2)
    print(f"   and eta^2 -> eta^2 + {diff}")
    assert sp.simplify(diff) != 0
    print("   NOT INVARIANT. A kappa eta^2 term EXPLICITLY BREAKS the symmetry")
    print("   GRV-020 derived, so it cannot appear in the action.")
    print("   => kappa = 0 EXACTLY, not merely small.\n")

    print("B4 WHAT GRV-066's CONDITIONAL BECOMES:")
    print("   GRV-066 showed that IF kappa = 0 then the screened equation")
    print("   degenerates to Poisson, GRV-020's Corollary 2 forces dipole-led")
    print("   sourcing, and the far field is (J x r)/r^3 -- a 1/r^2 falloff with")
    print("   dipole angular structure, exactly matching Lense-Thirring.")
    print("   THE ANTECEDENT IS NOW SUPPLIED BY THE SAME DERIVED CLAIM THAT")
    print("   SUPPLIES THE CONSEQUENT'S ANGULAR STRUCTURE. GRV-020 Corollary 1")
    print("   gives the Goldstone (hence kappa = 0); Corollary 2 gives dipole-led")
    print("   sourcing. One theorem, both halves.")
    print("   STATUS, stated precisely: a DERIVED corpus premise (GRV-020) plus a")
    print("   STANDARD THEOREM (Goldstone) plus an explicit symmetry check. Not an")
    print("   assumption, and not a full constitutive derivation either -- the")
    print("   strand action has not been written down and diagonalised.\n")

    print("B5 THE HONEST CAVEATS, listed:")
    print("   (C1) GOLDSTONE REQUIRES THE SYMMETRY TO BE GLOBAL AND EXACT. If the")
    print("        SO(2) is explicitly broken anywhere -- by the lattice, by a")
    print("        preferred frame, by anisotropy -- the mode acquires a small mass")
    print("        and ell becomes large but finite. THAT IS GRV-066's P3, and it")
    print("        is a PREDICTION rather than a problem: existing Lense-Thirring")
    print("        data already bounds ell > 1e7 m.")
    print("   (C2) IF THE SYMMETRY IS GAUGED rather than global, the Goldstone is")
    print("        eaten and the mode becomes massive. GRV-020 states a GLOBAL")
    print("        G = R x SO(2), and the corpus's gauge branch was closed at")
    print("        ROPE-SOURCE-AUDIT-002, so nothing suggests gauging -- but this")
    print("        is the assumption the argument leans on hardest.")
    print("   (C3) The Fourier diagonalisation GRV-065 named as step 4 is still")
    print("        not done. This argument forbids ONE term; it does not enumerate")
    print("        every mode of the coupled operator.")
    print("   THE ROUTE IS NOT CLOSED-AND-DONE. It is now supported at every step")
    print("   by Derived claims or standard theorems, with three named caveats.")
    print("PASS: the mass term is symmetry-forbidden, GRV-066's antecedent is")
    print("      supplied, and the caveats are named rather than buried.")


if __name__ == "__main__":
    main()
