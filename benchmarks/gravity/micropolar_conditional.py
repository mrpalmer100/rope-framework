"""GRV-065 -- DOWNGRADE: GRV-064's closure is a CANDIDATE OBSTRUCTION, and the
1e23 exponent is conditional on the argument's least-established step.

Bars locked in analysis/GRV065_conditional_bars_LOCKED.md BEFORE writing.
"""


def main():
    print("B1 THE THREE UNESTABLISHED STEPS, and the withdrawals they force:\n")
    print("   U1 THE CHARACTERISTIC LENGTH IS NOT AUTOMATICALLY THE SPACING.")
    print("      ell^2 ~ (couple-stress modulus)/(rotation-locking modulus) is a")
    print("      RATIO OF MODULI, often ASSOCIATED with microstructure size but")
    print("      not identical to it. If the locking modulus is zero, small,")
    print("      symmetry-protected or scale-dependent, ell can be MACROSCOPIC or")
    print("      DIVERGENT.")
    print("      GRV-064 ASSERTED ell ~ w = 5.774e-17 m on the grounds that 'both")
    print("      moduli are set by the microstructure'. That is a plausibility")
    print("      argument, not a derivation. THE 1e23 EXPONENT RESTS ENTIRELY ON")
    print("      IT and is WITHDRAWN as a derived number.\n")
    print("   U2 CALUGAREANU CONSERVATION IS NOT LOCAL LOCKING.")
    print("      Lk = Tw + Wr is a GLOBAL TOPOLOGICAL LEDGER. It does not set the")
    print("      local energy penalty for phi - (1/2) curl u, which is what")
    print("      determines the locking modulus. An exactly conserved integer")
    print("      coexists with soft twist-writhe redistribution, weak local")
    print("      frame-backbone coupling, gapless twist waves and LARGE")
    print("      characteristic lengths.")
    print("      GRV-064 called it 'the tightest tie available', conflating")
    print("      TOPOLOGICAL BOOKKEEPING with ENERGETIC STIFFNESS. Escape E1 was")
    print("      NOT closed. WITHDRAWN.\n")
    print("   U3 SCREENING THE RELATIVE ROTATION DOES NOT SCREEN EVERYTHING.")
    print("      Micropolar systems have COUPLED displacement and microrotation")
    print("      sectors. The nonclassical part may decay exponentially while the")
    print("      ORDINARY ELASTIC DISPLACEMENT keeps an algebraic far field. If")
    print("      u_phi ~ sin(theta)/r^2 is an ordinary displacement solution, its")
    print("      curl retains a 1/r^3 tail no matter what the Cosserat correction")
    print("      does. GRV-064 never established WHICH FIELD the metric shift")
    print("      couples to. WITHDRAWN.\n")
    print("   AND BOTH ESCAPE CLOSURES ARE NOT DECISIVE:")
    print("     E1' NEUTRALITY does not eliminate a DIPOLE. A globally neutral")
    print("         medium supports local positive and negative twist, dipole")
    print("         moments and circulating currents. Zero net charge does not")
    print("         forbid long-range multipoles -- and frame dragging IS dipolar.")
    print("     E2' 'LINKING IS SCALAR' IS NOT A NO-GO. The rotating source")
    print("         supplies the axial vector J, so Lk J or a constitutive")
    print("         pseudoscalar times J is available. Scalar-versus-vector")
    print("         character alone proves nothing.\n")

    print("B2 WHAT OF GRV-064 SURVIVES:")
    print("   ONE THING, and it is worth keeping: the medium IS a Cosserat")
    print("   continuum. Framed strands carry a microrotation independent of the")
    print("   displacement gradient, which is the textbook definition, and")
    print("   FND-STRAND-002 exhibits it. That confirms GRV-063's conjecture and")
    print("   is not affected by any of the above.")
    print("   WHAT DOES NOT SURVIVE: the screening length, the 1e23 exponent, both")
    print("   escape closures, and the verdict that the route is closed.\n")

    print("B3 THE FOUR STEPS THAT WOULD MAKE THE CLOSURE RIGOROUS:")
    for i, s in enumerate((
        "FIELD IDENTIFICATION -- show the candidate metric shift depends on the "
        "RELATIVE microrotation eta = phi - (1/2) curl u, rather than on an "
        "unscreened displacement or macrorotation component.",
        "CONSTITUTIVE DERIVATION -- derive the static equation and its "
        "coefficients: (grad^2 - ell^-2) eta = S(J).",
        "LENGTH-SCALE DERIVATION -- compute ell^2 = gamma/kappa from registered "
        "rope parameters, with uncertainty. Do NOT substitute ell = a.",
        "NO UNSCREENED CHANNEL -- diagonalise the coupled static operator in "
        "Fourier space and show every source-coupled metric-vector mode carries "
        "k^2 + ell^-2 rather than a massless k^2 denominator."), 1):
        print(f"   ({i}) {s}")
    print("   THE FOURTH IS THE DECISIVE ONE and none of them is done.\n")

    print("B4 THE HONEST STATUS -- MICROPOLAR_SCREENING_CANDIDATE_OBSTRUCTION:")
    print("   The rope's framed structure admits a Cosserat description, and")
    print("   standard micropolar constitutive dynamics screen relative")
    print("   microrotation over a material characteristic length. IF the")
    print("   gravitomagnetic candidate is that relative-rotation mode, AND the")
    print("   corpus derives its characteristic length as microscopic, THEN")
    print("   Earth-scale frame dragging is exponentially suppressed.")
    print("   The argument has not derived the modulus ratio, has not shown")
    print("   Calugareanu conservation implies local locking, and has not excluded")
    print("   an unscreened coupled vector mode.")
    print("   THE ROUTE IS NOT CLOSED. It has a candidate obstruction.\n")

    print("B5 THE PROCESS FAILURE, recorded:")
    print("   This is the SECOND over-conclusion in this arc. GRV-059 declared a")
    print("   falsification without searching the corpus for the mechanism; the")
    print("   operator caught it. GRV-064 declared a closure with three steps")
    print("   asserted rather than derived; a reviewer caught it. Both times the")
    print("   claim carried a bar saying escapes had been checked, and both times")
    print("   the check was shallower than the verdict.")
    print("   THE RULE THAT WOULD HAVE CAUGHT BOTH: a verdict may not be stronger")
    print("   than its weakest derived step. GRV-064's weakest step was an")
    print("   assertion about a modulus ratio, and its verdict was 'genuinely")
    print("   closed'. That gap is the error, independent of the physics.")
    print("   NAMED NEXT-ORDER: derive and diagonalise the rope's linear Cosserat")
    print("   constitutive operator. The reviewer is right that this is cheaper")
    print("   and more decisive than any further astrophysical benchmark.")


if __name__ == "__main__":
    main()
