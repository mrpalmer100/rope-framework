"""PRED-003 -- THE COUPLING-DRIFT RATIO: d ln alpha = -2 d ln G.

Registers falsifiable_predictions P6, closing part of the traceability gap
ELEC-063 found. Testable NOW against existing bounds.
"""
import numpy as np
import sympy as sp


def main():
    T, kappa, a, s = sp.symbols('T kappa a s', positive=True)
    alpha = 2 * T ** 2 / (kappa * a)      # DERIVED (EM energy coefficient chain)
    G = 1 / (T * a)                        # ASSUMED (tension-rigidity form)
    print("The two couplings in the SAME medium primitives:")
    print(f"   alpha ~ {alpha}    [DERIVED to rope primitives, J = T^2/kappa exact")
    print("                        in the harmonic regime]")
    print(f"   G ~ {G}            [ASSUMED: the natural tension-rigidity form]")

    # vary through T alone, at fixed kappa and a
    dln_alpha = sp.simplify(sp.diff(sp.log(alpha.subs(T, s)), s) * s)
    dln_G = sp.simplify(sp.diff(sp.log(G.subs(T, s)), s) * s)
    ratio = sp.simplify(dln_alpha / dln_G)
    print(f"\nVarying through the tension at fixed kappa, a:")
    print(f"   d ln alpha / d ln T = {dln_alpha}")
    print(f"   d ln G     / d ln T = {dln_G}")
    print(f"   THE PREDICTION: d ln alpha / d ln G = {ratio}   (paper: -2)")
    assert ratio == -2

    # the same ratio must NOT hold if variation runs through a instead: report it
    dln_alpha_a = sp.simplify(sp.diff(sp.log(alpha.subs(a, s)), s) * s)
    dln_G_a = sp.simplify(sp.diff(sp.log(G.subs(a, s)), s) * s)
    print(f"\n   SCOPE, stated honestly: through the strand SPACING instead, the ratio")
    print(f"   is {sp.simplify(dln_alpha_a/dln_G_a)}, not -2. The prediction is "
          f"specifically that")
    print("   cosmological drift runs through the TENSION channel; a measured ratio")
    print("   of +1 would indicate spacing drift, and any other value kills both.")

    print("\nCONFRONTATION WITH EXISTING BOUNDS (testable now, no new instrument):")
    bounds = [("quasar absorption, alpha-dot/alpha", 1e-17),
              ("lunar laser ranging, G-dot/G", 1e-13),
              ("pulsar timing, G-dot/G", 1e-12)]
    for name, b in bounds:
        print(f"   {name:38s} |rate| < {b:.0e} /yr")
    print("   Combining: the -2 relation ties these two independent limits together.")
    print("   The tighter alpha bound implies |G-dot/G| < 5e-18 /yr IF the relation")
    print("   holds -- five orders below the direct G limits, so the relation is")
    print("   ALREADY under pressure to be tested by improving G-dot measurements.")
    print("   FALSIFIER: a measured drift ratio inconsistent with -2.")
    print("   HONEST CAVEAT (from the paper): PROVISIONAL on the G ~ 1/(Ta) form,")
    print("   which is assumed rather than derived.")
    print("PASS: P6 recomputed from stated inputs and registered.")


if __name__ == "__main__":
    main()
