"""PRED-003 CONFRONTED WITH PUBLISHED DATA (2026-08-01).

The corpus's one prediction testable today against measurements already in the
literature. Bars locked in analysis/PRED003_confrontation_bars_LOCKED.md BEFORE
the arithmetic.
"""
import numpy as np

# D1: alpha drift (optical clocks)
ALPHA_DOT, ALPHA_ERR = 1.0e-18, 1.1e-18          # Filzinger et al. 2023, Yb+ E3/E2
ALPHA_DOT_T, ALPHA_ERR_T = 1.8e-19, 2.5e-19      # tighter supplemental fit
# D2: G drift (lunar laser ranging)
G_DOT, G_ERR = 7.1e-14, 7.6e-14                  # Hofmann & Muller 2018
G_DOT_O, G_ERR_O = 4e-13, 9e-13                  # Williams et al. 2004


def main():
    print("D1 alpha-dot/alpha = {:.1e} +/- {:.1e} /yr   (Yb+ E3/E2, PTB 2023)"
          .format(ALPHA_DOT, ALPHA_ERR))
    print("D2 Gdot/G          = {:.1e} +/- {:.1e} /yr   (LLR, Hofmann & Muller 2018)"
          .format(G_DOT, G_ERR))
    print("Both are consistent with zero at {:.1f} and {:.1f} sigma respectively.\n"
          .format(abs(ALPHA_DOT / ALPHA_ERR), abs(G_DOT / G_ERR)))

    # B1 forward
    pred = -2 * G_DOT
    pred_err = 2 * G_ERR
    diff = pred - ALPHA_DOT
    sig = abs(diff) / np.hypot(pred_err, ALPHA_ERR)
    print("B1 FORWARD TEST: from G, the relation predicts")
    print("   alpha-dot/alpha = -2 (Gdot/G) = {:+.2e} +/- {:.2e} /yr".format(pred, pred_err))
    print("   measured                      = {:+.2e} +/- {:.2e} /yr".format(ALPHA_DOT, ALPHA_ERR))
    print("   tension = {:.2f} sigma -> {}".format(
        sig, "CONSISTENT" if sig < 2 else ("TENSION" if sig < 3 else "REFUTED")))
    assert sig < 2
    for gd, ge, lab in ((G_DOT_O, G_ERR_O, "Williams 2004 (independent)"),):
        s2 = abs(-2 * gd - ALPHA_DOT) / np.hypot(2 * ge, ALPHA_ERR)
        print("   cross-check with {}: {:.2f} sigma".format(lab, s2))

    # B2 inverse
    inv, inv_err = -0.5 * ALPHA_DOT, 0.5 * ALPHA_ERR
    print("\nB2 INVERSE TEST: from alpha, the relation predicts")
    print("   Gdot/G = -(1/2)(alpha-dot/alpha) = {:+.2e} +/- {:.2e} /yr".format(inv, inv_err))
    print("   present LLR sensitivity is {:.1e} /yr -- the prediction sits {:.0f}x"
          .format(G_ERR, G_ERR / abs(inv_err)))
    print("   below current reach. With the tighter clock fit it is {:.0f}x below."
          .format(G_ERR / (0.5 * ALPHA_ERR_T)))
    print("   THE FRAMEWORK THEREFORE PREDICTS G IS STATIC to well beyond anything")
    print("   measurable today. That is a real commitment, not a hedge.")

    # B3 channel test
    print("\nB3 CHANNEL TEST (tension channel -2 vs spacing channel +1):")
    ratio = ALPHA_DOT / G_DOT
    print("   ratio of central values = {:.1e}, which is neither -2 nor +1.".format(ratio))
    print("   BUT BOTH MEASUREMENTS ARE NULL, so this ratio is a ratio of noise and")
    print("   carries NO information. THE CHANNEL IS UNDETERMINED BY PRESENT DATA.")
    print("   Reporting it as favouring either channel would be reading structure")
    print("   into two numbers consistent with zero.")

    # B4 falsification condition
    print("\nB4 WHAT KILLS IT: a confirmed nonzero Gdot/G at the current LLR central")
    print("   value would imply alpha-dot/alpha = {:+.1e}, which sits {:.0e} sigma"
          .format(-2 * G_DOT, abs(-2 * G_DOT - ALPHA_DOT) / ALPHA_ERR))
    print("   from the clock measurement. So ANY firm detection of G drift at or")
    print("   above ~1e-17 /yr refutes the relation outright.")
    gd_kill = ALPHA_ERR * 3 / 2
    print("   Quantitatively: |Gdot/G| > {:.1e} /yr at 3 sigma is incompatible."
          .format(gd_kill))
    print("   Current LLR reach is {:.1e}, so the test needs a ~{:.0e}x improvement"
          .format(G_ERR, G_ERR / gd_kill))
    print("   in G-drift sensitivity to become decisive from that side.")

    # B5
    print("\nB5 HONESTY: this is a NULL-VS-NULL consistency. Two measurements")
    print("   compatible with zero are compatible with almost any linear relation")
    print("   between them, so PASSING IS SURVIVAL, NOT CONFIRMATION. The relation")
    print("   has not been vindicated; it has failed to be killed by the one test")
    print("   currently available. The informative outcome lies with future G-drift")
    print("   work, where the framework has made a falsifiable commitment.")
    print("\nVERDICT: PRED-003 SURVIVES its first confrontation with published data")
    print("         at {:.2f} sigma, with the channel undetermined.".format(sig))


if __name__ == "__main__":
    main()
