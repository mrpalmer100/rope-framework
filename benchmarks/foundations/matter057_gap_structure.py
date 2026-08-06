"""FND-MATTER-057: the gap-structure diagnostic -- prompted by the operator's
question (does the factor ~4 cancel against the 25 percent lever?). Bars
locked BEFORE computing (analysis/MATTER057_gap_structure_results.md):
(1) THE CANCELLATION HYPOTHESIS IS TESTED FIRST, with a decisive
pre-committed diagnostic: if the 25 percent and the factor 4 cancel
structurally, the gap must be IDENTICAL for every knot. Any spread refutes
it. The test is run before any interpretation.
(2) THE SPREAD, IF PRESENT, IS THEN TESTED FOR IDENTITY before being
treated as physics. In the previous turn the assistant proposed the
knot-dependence of the gap as a NEW constraint on the closer ('a second
job'). That proposal is on trial here: if the spread is algebraically the
conditioning table restated, it is an IDENTITY, the proposal was
double-counting, and the session must say so plainly and withdraw it.
(3) IDENTITY CHECK IS SYMBOLIC-GRADE: the claimed constancy must hold to
machine precision across all three knots, not approximately.
(4) NO NEW CALIBRATION; the target and derived values are inherited from
FND-MATTER-055/056 unchanged. Nothing is re-fitted.
(5) The outcome updates FND-MATTER-056's results file as a registered
diagnostic; no claim status changes.
"""
import numpy as np

HBAR, C = 1.054571817e-34, 2.99792458e8
A_M, T0_M = 6.0056e-17, 434.0
R_OVER_A, LEVER = 9.4e-4, 0.25
J_PER_MEV = 1.602176634e-13
DEZP = {"ring": 3.81, "trefoil": 30.78, "5_1": 34.45}
LEN = {"ring": 3.141, "trefoil": 16.84, "5_1": 25.12}


def main():
    q = HBAR * C / A_M
    lam_d = np.pi * R_OVER_A**2

    # (1) THE CANCELLATION TEST
    print("(1) THE CANCELLATION HYPOTHESIS (tested first):")
    print("  IF the 25 percent lever and the factor ~4 cancel structurally,")
    print("  the gap MUST be identical for every knot. Diagnostic:")
    gaps, fracs = {}, {}
    for k in LEN:
        tens = T0_M * LEN[k] * A_M
        target = (LEVER / (1 - LEVER)) * tens / (DEZP[k] * q)
        gaps[k] = target / lam_d
        fracs[k] = DEZP[k] / LEN[k]
        pred_lever = lam_d * DEZP[k] * q / (tens + lam_d * DEZP[k] * q)
        print(f"    {k:8s}: gap {gaps[k]:.2f}x, and the derived lambda")
        print(f"              PREDICTS a lever of {100*pred_lever:.1f}% "
              f"(measured ~25%)")
    spread = max(gaps.values()) / min(gaps.values())
    print(f"  Spread across knots: {spread:.2f}x -- NOT identical.")
    print("  VERDICT: THE CANCELLATION IS REFUTED. And the direct check")
    print("  agrees: the derived mechanism predicts a 6-9 percent lever")
    print("  against a measured 25 percent, a real disagreement rather than")
    print("  an artifact of how the target was built. (Note the 25 percent")
    print("  sits in the target's NUMERATOR, so a larger lever would make")
    print("  the gap WORSE -- cancellation would require it below.)")
    assert spread > 1.2

    # (2)+(3) THE IDENTITY CHECK on the spread
    print("(2) IS THE SPREAD NEW INFORMATION? (the assistant's 'second job'")
    print("    proposal on trial):")
    prods = {k: gaps[k] * fracs[k] for k in LEN}
    vals = np.array(list(prods.values()))
    dev = vals.std() / vals.mean()
    for k in LEN:
        print(f"    {k:8s}: gap x (dE_zp/L) = {prods[k]:.6f}")
    print(f"  Relative deviation across knots: {dev:.2e}")
    assert dev < 1e-12
    const = (LEVER / (1 - LEVER)) * T0_M * A_M / (q * lam_d)
    print(f"  CONSTANT to machine precision, and its closed form is")
    print(f"  (0.25/0.75) x T0 a/(q lambda_d) = {const:.6f} -- no knot")
    print("  quantity appears in it.")
    assert abs(const / vals.mean() - 1) < 1e-12
    print("  VERDICT: IDENTITY. gap_k = const / (dE_zp/L)_k exactly, so the")
    print("  gap's knot-dependence IS the conditioning table's own")
    print("  fraction restated -- the same 1.51x MATTER055 already")
    print("  registered as the demanded-lever spread. It is ONE fact")
    print("  appearing twice, not two facts.")

    # the withdrawal
    print("WITHDRAWAL, stated plainly: the assistant proposed last turn that")
    print("  the knot-dependence gives the closer 'a second job' -- explain")
    print("  the factor AND its knot-dependence. That proposal was")
    print("  DOUBLE-COUNTING and is WITHDRAWN. The closer has ONE job: a")
    print("  single universal factor. The fifth identity catch of the")
    print("  campaign, and the first one caught in the assistant's own")
    print("  proposed research direction rather than in the registry.")

    print("WHAT THE DIAGNOSTIC ACTUALLY BUYS (the constructive residue):")
    print("  Because the relation is exact, the discrepancy can be stated")
    print("  as ONE number in a knot-free form. The mechanism must supply")
    print(f"  a universal enhancement of {const:.3f} / (dE_zp/L), i.e. the")
    print("  dilute-Casimir estimate is short by a single constant once the")
    print("  conditioning normalization is accounted for. A closer therefore")
    print("  needs to produce ONE factor, not a knot-dependent family --")
    print("  which is a materially easier target and a sharper falsifier:")
    print("  any candidate mechanism producing knot-dependent suppression")
    print("  is now excluded on sight.")
    print("NOT CLAIMED: lambda; any change to MATTER055/056's values; any")
    print("  new parameter; any lepton mass (PM-004 stands).")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
