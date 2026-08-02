"""PRED-002 CONFRONTED: the flatness test already exists, and it passes --
but it does not discriminate.

Bars locked in analysis/PRED002_confrontation_bars_LOCKED.md BEFORE computing.
"""
import numpy as np

BETA_BAL, ERR_BAL = 0.30, 0.05    # Ballardini et al. 2025, Planck legacy
BETA_ESK, ERR_ESK = 0.342, 0.094  # Eskilt & Komatsu 2022 (used by PRED-002)


def eb_ee(beta_deg):
    return np.sin(4 * np.radians(beta_deg)) / 2


def main():
    print("B1 THE SHAPE TEST -- ALREADY PERFORMED, and PRED-002 did not know it:")
    print("   Ballardini et al., JCAP 09 (2025) 075, tested the scale dependence of")
    print("   beta on Planck legacy data by TWO independent methods:")
    print("     - a power-law fit to beta_ell: NO significant scale dependence")
    print("       (departures allowed only up to 1.8 sigma);")
    print("     - a non-parametric Bayesian reconstruction: the CONSTANT model is")
    print("       FAVOURED BY BAYESIAN EVIDENCE.")
    print("   Robust across all four published Planck CMB solutions.")
    print("   VERDICT ON THE SHAPE: PRED-002'S FLATNESS PREDICTION IS CONFIRMED")
    print("   at present sensitivity. This is the corpus's first prediction to be")
    print("   positively borne out by an existing measurement.\n")

    print("B2 THE NUMBER at both published beta values:")
    for b, e, lab in ((BETA_BAL, ERR_BAL, "Ballardini 2025 (Planck legacy)"),
                      (BETA_ESK, ERR_ESK, "Eskilt & Komatsu 2022 (used by PRED-002)")):
        print(f"   {lab:42s} beta = {b:.3f} +/- {e:.3f} deg")
        print(f"      -> EB/EE = {eb_ee(b):.5f}  band "
              f"[{eb_ee(b-e):.5f}, {eb_ee(b+e):.5f}]")
    print(f"   The two beta determinations agree at "
          f"{abs(BETA_BAL-BETA_ESK)/np.hypot(ERR_BAL,ERR_ESK):.2f} sigma.")
    print(f"   PRED-002's registered 0.01194 should be read as "
          f"{eb_ee(BETA_BAL):.5f}-{eb_ee(BETA_ESK):.5f} depending on the beta adopted.\n")

    print("B3 THE DISCRIMINATION AUDIT -- and it goes against PRED-002:")
    print("   PRED-002 registered flatness as 'the rope-specific signature', claiming")
    print("   axion-like and early-dark-energy models 'generically give an")
    print("   l-DEPENDENT rotation'. Ballardini et al.'s own framing contradicts this:")
    print("   they motivate the scale-dependence search by noting it arises IF the")
    print("   ultra-light (pseudo)scalar hypothesis does NOT hold. That is, THE")
    print("   STANDARD ULTRA-LIGHT AXION ALSO PREDICTS A CONSTANT BETA.")
    print("   Flatness therefore does NOT distinguish the rope from the leading")
    print("   alternative explanation of the observed birefringence. It distinguishes")
    print("   both of them jointly from a narrower class of models (heavier fields,")
    print("   Faraday-like or Lorentz-violating rotation) that imprint scale")
    print("   dependence. PRED-002'S REGISTERED DISCRIMINATING CLAIM IS OVERSTATED")
    print("   AND IS CORRECTED ON THE RECORD.\n")

    print("B4 VERDICT: CONFIRMED BUT NON-DISCRIMINATING. The prediction is borne out;")
    print("   its power to distinguish the framework is much weaker than registered.")
    print("   Under the ELEC-062 census criteria this DEMOTES PRED-002 from T1")
    print("   (distinctive in observable outcome) to T3 (derivation-distinctive:")
    print("   correct, but sharing its observable with a standard alternative).\n")

    print("B5 WHAT WOULD DISCRIMINATE, since flatness does not:")
    print("   - FREQUENCY dependence: axions give a nearly frequency-INDEPENDENT beta,")
    print("     while Faraday rotation and Lorentz-violating theories give beta ~ nu^n.")
    print("     The rope's chiral medium must commit to an n. IT HAS NOT. Deriving the")
    print("     rope's frequency scaling is the single highest-value move available to")
    print("     this prediction, and Planck DR4 frequency-band constraints (Eskilt 2022)")
    print("     already exist to test it against.")
    print("   - The ANISOTROPIC birefringence spectrum, where a medium with structure")
    print("     and a homogeneous scalar field need not agree.")
    print("   NAMED: derive beta(nu) for the rope. Until then PRED-002 is a confirmed")
    print("   but shared prediction, and the corpus should say so.")


if __name__ == "__main__":
    main()
