"""FND-MATTER-054: the knot-mode asymmetry -- is the internal transverse
mode band an OMITTED TERM in the two-term mass model, and what does its
discontinuity across the knot table do?
Bars locked BEFORE computing (analysis/MATTER054_knot_mode_asymmetry_results.md):
(1) SCOPE, stated first to prevent a category error: the registered
dE_zp (FND-MATTER-008 / the two-term model) is a CURVATURE-CONDITIONING
quantity (kappa^2 per site on a 1D host), NOT a count of internal
transverse standing waves. The mode band found in FND-MATTER-053 is a
DIFFERENT object. This session asks whether it is an OMITTED ADDITIONAL
term, and may not conflate the two.
(2) MODE COUNTING inherited from FND-MATTER-053, not re-chosen: closed
loop -> periodic BCs, k_n = 2 pi n/(L a), cutoff k <= 1/a, degeneracy 4
per |n| (two circulation senses x two transverse polarizations). Stated
in advance; the degeneracy is displayed as a sensitivity since it only
scales the result.
(3) THE TEST IS A MAGNITUDE CONFRONTATION with a pre-committed bar: an
omitted term is ADMISSIBLE only if it is at most comparable to the
tension term it would join (factor <= ~1). A term exceeding the tension
term by more than an order of magnitude is EXCLUDED -- it would not
correct the mass model, it would destroy it.
(4) THE DISCONTINUITY IS PART OF THE TEST, not a separate observation:
because the ring admits ZERO modes and the trefoil admits two, an
admissible internal term must not introduce a jump between neighbouring
knots that the observed mass table forbids.
(5) PERMITTED OUTCOMES include EXCLUSION (the mode band contributes
nothing to rest mass), which would independently corroborate
FND-MATTER-053's ambient conclusion rather than merely echo it.
"""
import numpy as np

HBAR, C = 1.054571817e-34, 2.99792458e8
A_M, T0_M = 6.0056e-17, 434.0
MEV = 1.602176634e-13 * 1e-6 / 1e-6  # J per MeV = 1.602e-13
J_PER_MEV = 1.602176634e-13
KNOTS = {"ring (3.141)": 3.141, "trefoil (16.84)": 16.84, "5_1 (25.12)": 25.12}
DEGEN = 4


def modes(L):
    n_max = int(np.floor(L / (2 * np.pi)))
    return list(range(1, n_max + 1))


def main():
    hbarc_over_a = HBAR * C / A_M
    print(f"SCALE: hbar c / a = {hbarc_over_a / J_PER_MEV:.0f} MeV at the "
          f"M-point.")
    print("TENSION TERMS (the model's first term, T0 L a):")
    tens = {}
    for k, L in KNOTS.items():
        E = T0_M * L * A_M
        tens[k] = E
        print(f"  {k:16s} = {E / J_PER_MEV:.3f} MeV")
    print("  (the ring is the electron by construction -- the campaign's one")
    print("   spent calibration, FND-MATTER-044.)")

    print("INTERNAL MODE BAND (counting inherited from MATTER053, "
          f"degeneracy {DEGEN} per |n|):")
    for k, L in KNOTS.items():
        ns = modes(L)
        E_int = sum(DEGEN * 0.5 * HBAR * C * (2 * np.pi * n / (L * A_M))
                    for n in ns)
        ratio = E_int / tens[k] if E_int > 0 else 0.0
        print(f"  {k:16s} n = {ns if ns else '[] (EMPTY)'}, "
              f"E_int = {E_int / J_PER_MEV:8.1f} MeV, "
              f"E_int/E_tension = {ratio:.3e}")
        if k.startswith("ring"):
            assert E_int == 0
        else:
            assert ratio > 1e2

    # (3) the magnitude bar
    L_t = KNOTS["trefoil (16.84)"]
    E_t = sum(DEGEN * 0.5 * HBAR * C * (2 * np.pi * n / (L_t * A_M))
              for n in modes(L_t))
    print("MAGNITUDE VERDICT (bar: admissible only if <= ~1x the tension "
          "term):")
    print(f"  the trefoil's internal band is {E_t / tens['trefoil (16.84)']:.0f}x "
          f"its tension term -- {E_t / J_PER_MEV:.0f} MeV against "
          f"{tens['trefoil (16.84)']/J_PER_MEV:.2f} MeV.")
    print("  EXCLUDED by more than three orders. Adding this term would not")
    print("  correct the mass model; it would replace every knot mass with a")
    print("  GeV-scale number and destroy the table.")
    print("  SENSITIVITY: the verdict is degeneracy-independent -- dividing")
    print("  out all 4 states still leaves ~3 orders of excess.")

    # (4) the discontinuity
    print("DISCONTINUITY VERDICT (part of the same test):")
    print("  the ring gets NOTHING (empty band) while the trefoil gets a")
    print("  GeV -- so an admissible internal term would have to introduce a")
    print("  three-order JUMP between the two lightest knots in the table.")
    print("  The observed lepton/hadron mass table has no such jump at that")
    print("  place. The asymmetry is therefore not a feature to be modelled")
    print("  but a REDUCTIO: it is the sharpest available proof that the")
    print("  internal band cannot be in the mass ledger at all.")

    print("VERDICT: THE INTERNAL MODE BAND CONTRIBUTES NOTHING TO REST MASS.")
    print("  Excluded twice over -- by magnitude (>1000x) and by")
    print("  discontinuity (a jump the table forbids). No omitted term.")
    print("WHAT THIS BUYS, and it is not an echo:")
    print("  1. INDEPENDENT CORROBORATION of FND-MATTER-053. That session")
    print("     killed the internal-mode picture for the RING by finding an")
    print("     empty band -- a result that could have been dismissed as an")
    print("     accident of the ring being small. This session kills it for")
    print("     the knots that DO have modes, by magnitude, which is a")
    print("     different argument reaching the same place.")
    print("  2. A RETROACTIVE VINDICATION of the registered model: the")
    print("     two-term model's dE_zp is a smooth curvature-conditioning")
    print("     quantity, and this session shows that choice was not merely")
    print("     convenient but FORCED -- the alternative is excluded.")
    print("  3. THE AMBIENT ROUTE IS NOW THE ONLY SURVIVOR for the")
    print("     zero-point term, reached from three directions (empty band,")
    print("     excess magnitude, forbidden discontinuity).")
    print("NOT CLAIMED: any lepton mass prediction (PM-004 stands untouched),")
    print("  any change to the registered two-term table, any new parameter.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
