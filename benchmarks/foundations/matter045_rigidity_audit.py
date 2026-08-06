"""FND-MATTER-045: the rigidity audit. Bars locked BEFORE computing
(analysis/MATTER045_rigidity_audit_results.md):
(1) IDENTITY TEST FIRST: if GRV-074's 1.4-2.0e39 coefficient is
definitionally EH/T0 evaluated at the card's own T0 range, then the
'GRV-074 rigidity anchor' used by MATTER040/041/044 is NOT independent --
it is T0_card wearing rigidity units -- and the audit MUST void it and
mandate bracketed corrections on every claim that counted it, whatever
that does to the campaign's tables. The R3 guardrail applies to us.
(2) The corrected anchor cluster is recomputed and its effect on the
MATTER040 fingerprint re-stated honestly (strengthen or weaken, as found).
(3) GRV-074's B3 quantifications are recomputed at the M-point and
registered as updates.
(4) GRV-074's named decider ('the thin-strand suppression audit for the
39-order gap') is adjudicated against MATTER043's measured power law.
(5) OUT OF SCOPE, untouched: GRV-074's J1713 decision structure (B4/B5).
"""
import numpy as np

HBAR, C, G = 1.054571817e-34, 2.99792458e8, 6.67430e-11
EH = C**4 / (16 * np.pi * G)
T0_CARD = (1203.0, 1700.0)          # the card range GRV-074 had
GRV074_BAND = (1.4e39, 2.0e39)      # the registered quantification
ANCHORS_INDEP = {"R1 quantum-area": 119.3, "lattice": 1203.0,
                 "Sigma-route": 1700.0}
# M-point (MATTER044)
A_M, T0_M = 6.0056e-17, 434.0
R_PHYS = 9.4e-20                    # r fixed physically (card r/a at a=1e-16)


def main():
    # (1) THE IDENTITY TEST
    implied = tuple(EH / t for t in T0_CARD[::-1])
    print(f"IDENTITY TEST: EH/T0 over the card range = "
          f"{implied[0]:.2e}..{implied[1]:.2e}")
    print(f"  GRV-074's registered band:              "
          f"{GRV074_BAND[0]:.2e}..{GRV074_BAND[1]:.2e}")
    match = all(abs(a / b - 1) < 0.02 for a, b in zip(implied, GRV074_BAND))
    assert match
    print("  MATCH to <2%: the 1.4-2.0e39 IS the identity EH/T0 at the card's")
    print("  own tension. VERDICT: the 'GRV-074 rigidity anchor' (implied T0")
    print("  ~ 4800-6900 J/m) that MATTER040/041/044 carried as a FOURTH")
    print("  independent determination is VOID -- it was T0_card wearing")
    print("  rigidity units. The campaign committed the exact double-count")
    print("  the R3 guardrail names. Bracketed corrections MANDATED on")
    print("  FND-MATTER-040, -041, -044.")

    # (2) The corrected cluster and the fingerprint restated
    vals = np.array(list(ANCHORS_INDEP.values()))
    spread = vals.max() / vals.min()
    t0_closure = 2.0159e20
    gap = t0_closure / np.median(vals)
    print(f"CORRECTED CLUSTER: three independent anchors, spread {spread:.1f}x")
    print(f"  (was 'four within 49x'). Closure-T0 gap: {gap:.1e}.")
    print("  EFFECT ON THE MATTER040 FINGERPRINT: STRENGTHENED -- a tighter")
    print("  cluster of genuinely independent determinations disagreeing with")
    print("  the F-Sak closure in unison. The conclusion survives its own")
    print("  correction with room.")
    assert spread < 15 and gap > 1e16
    # Effect on MATTER044: the 13.5x 'rigidity flag' dissolves as a
    # non-comparison; remaining comparisons were all inside the bar already.
    print("EFFECT ON MATTER044: the 13.5x rigidity flag DISSOLVES (it compared")
    print("  T0_M to EH/T0_card, a category error). All surviving pairwise")
    print("  comparisons were already inside the ZPE bar; the pricing verdict")
    print("  is unchanged and cleaner.")

    # (3) B3 quantifications at the M-point
    q_zpe = EH / (HBAR * C / A_M**2)
    q_t0 = EH / T0_M
    print(f"B3 AT THE M-POINT (registered as updates to GRV-074's numbers):")
    print(f"  EH / (hbar c / a^2) = {q_zpe:.2e}   (was 7.6e35 at the bound)")
    print(f"  EH / T0             = {q_t0:.2e}   (was 1.4-2.0e39)")

    # (4) The named decider adjudicated with MATTER043
    enh = (2 / 3) * (A_M / R_PHYS)**2
    residual = q_zpe / enh
    print(f"THE NAMED DECIDER ('thin-strand suppression audit'): GRV-074 filed")
    print(f"  (r/a)^2 per power, 'needing five to six powers', not leaned on.")
    print(f"  MATTER043 MEASURED the power: ONE (r/a)^2 (p = 2.000), giving")
    print(f"  {enh:.2e} at the M-point geometry -- the five-to-six-power hope")
    print(f"  UNDERSHOOTS reality's demand: residual {residual:.2e} "
          f"({np.log10(residual):.1f} orders)")
    print("  remains. The decider is CLOSED: the corpus-native suppression")
    print("  source supplies one power, and the 39-order gap becomes a")
    print("  quantified ~30-order open item, consistent with MATTER043's")
    print("  1e30 to within the a-shift.")
    assert 0.3 < residual / 1.0e30 < 3.3

    print("OUT OF SCOPE, untouched: GRV-074's J1713 form-robustness (B4/B5).")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
