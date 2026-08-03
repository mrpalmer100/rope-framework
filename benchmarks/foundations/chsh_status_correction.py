"""FND-026 -- CORRECTION: the two-particle boundary fell at QB-027 and I reported
it as standing in two consecutive claims.

Bars locked in analysis/FND026_chsh_correction_bars_LOCKED.md BEFORE writing.
"""
import numpy as np

S_QB009 = 1.42
S_QB027 = 2.66
S_ERR = 0.01
V = 0.97
TSIRELSON = 2 * np.sqrt(2)
S_SEVERED = 0.85


def main():
    print("B1 THE CORRECTION:")
    print(f"   FND-024 and FND-025 both stated 'CHSH still fails at S = {S_QB009}")
    print("   < 2, the two-particle boundary kept', citing QB-009.")
    print(f"   QB-027 reports CHSH = {S_QB027} +/- {S_ERR}. THE BOUNDARY FELL.")
    print(f"   I reported a superseded failure TWICE, in consecutive claims.")
    print("   WHY: I searched the corpus but did NOT run forward_check.py on")
    print("   QB-009 before quoting its verdict. The tool was built TODAY for")
    print("   exactly this, and running it now returns QB-010 in its first hit.\n")

    print("B2 WHAT QB-027 ACTUALLY DID -- and the methodology matters:")
    print("   'no analytic response law anywhere in the loop': the analyzers are")
    print("   QB-026's engine devices CALIBRATED BY MEASUREMENT -- a theta-grid of")
    print("   full 2D lattice runs producing a weight table -- and THE MEASURED")
    print("   TABLE, NOT cos^2(theta/2), drives every trial, with the ribbon and")
    print("   reel per QB-023.")
    print("   So the violation is not a formula being evaluated. It is simulated")
    print("   hardware producing trials.\n")

    print("B3 THE SHORTFALL FROM TSIRELSON IS A VERIFICATION, NOT A FAILURE:")
    pred = V ** 2 * TSIRELSON
    dev = abs(pred / S_QB027 - 1)
    print(f"   measured per-wing visibility from device pole leakage: V ~ {V}")
    print(f"   predicted S = V^2 x 2sqrt2 = {pred:.4f}")
    print(f"   measured  S = {S_QB027}")
    print(f"   agreement: {dev*100:.2f} percent")
    assert dev < 0.01
    print("   THE IMPERFECT ANALYZER PRODUCES EXACTLY THE IMPERFECT VIOLATION A")
    print("   REAL LABORATORY SEES, because the imperfections propagate through")
    print("   the trials by design. A model that landed exactly on 2sqrt2 with a")
    print("   leaky device would have been the suspicious result.\n")

    print("B4 THE CONTROL, and it is the cleanest part:")
    print(f"   identical hardware with SEVERED BOOKKEEPING gives CHSH ~ {S_SEVERED}")
    print("   -- below the classical bound, at the leakage-degraded wall.")
    print("   ONE SWITCH separates the wall from the violation WITH THE HARDWARE")
    print("   HELD FIXED. That is the shared-ribbon premise isolated as cleanly as")
    print("   an experiment can isolate anything.\n")

    print("B5 WHAT THIS DOES TO FND-024 AND FND-025:")
    print("   WITHDRAWN from both: 'the two-particle boundary kept', and")
    print("   FND-024's speculation that the CHSH shortfall 'may be that thinness")
    print("   showing'. There is no shortfall to explain. The shortfall that")
    print("   exists is instrumental and is quantitatively accounted for.")
    print("   STANDING from both: a conserved SCALAR fails D1 at S = 1.418")
    print("   (QB-010's physical-space race) while a SHARED OBJECT succeeds --")
    print("   FND-025's central distinction is not only intact but now confirmed")
    print("   end-to-end by QB-027's control.")
    print("   WHAT GENUINELY REMAINS is what QB-010 called the summit question and")
    print("   FND-025 named correctly: whether configuration-space guidance can")
    print("   EMERGE from physical-space dynamics. QB-023's shared ribbon is still")
    print("   a PREMISE. QB-027 shows the premise WORKS; it does not show the")
    print("   medium produces it.")
    print("   THE ONE ENCOURAGING POINTER, not a result: FND-STRAND-006 has a")
    print("   KINK-ANTIKINK PAIR NUCLEATING IN ONE STRAND'S TWIST FIELD -- two")
    print("   excitations that are features of a single object by construction.")
    print("   Whether that generalises to a separated pair is untested.")
    print("PASS: the correction is registered, the magnitude stated, and the")
    print("      process failure named as a skipped tool.")


if __name__ == "__main__":
    main()
