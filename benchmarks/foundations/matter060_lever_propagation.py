"""FND-MATTER-060: the derived lever cashed in -- per-knot confrontation and
the ZPE band restated at its derived width.
Bars locked BEFORE computing (analysis/MATTER060_lever_propagation_results.md):
(1) NOTHING IS RE-FITTED. lambda = 6 pi (r/a)^2 (FND-MATTER-059, derived) is
applied as-is. The registered inputs (conditioning table FND-MATTER-008,
lengths, M-point scales, the 25 percent registered lever) are inherited
unchanged. Calibration spend stays at ONE.
(2) THE CONFRONTATION IS PER-KNOT, with the inherited factor-2 bar applied
to each knot's own demanded lambda (MATTER055 registered the 1.51x spread as
the demand's intrinsic width; a universal lambda cannot beat that spread, so
per-knot landings are the honest resolution).
(3) THE COMPLIANCE REFINEMENT (059's named lead) MAY NOT BE INVOKED. If the
derived lambda misses a knot, the miss is registered; no correction is
computed or estimated to rescue it.
(4) PERMITTED OUTCOMES: all knots inside the bar (lever CONFIRMED per-knot);
some outside (tension registered at exact scope); systematic sign structure
noted as data either way.
(5) THE BAND RESTATEMENT is bookkeeping, not physics: the scale campaign's
'ZPE bar' (the factor 2-3 band from the unfixed 25 percent lever) is
restated at the width the derived lambda actually supports, with the
worst-knot residual as the honest new half-width.
"""
import numpy as np

HBAR, C = 1.054571817e-34, 2.99792458e8
A_M, T0_M = 6.0056e-17, 434.0
R_OVER_A = 9.4e-4
J_PER_MEV = 1.602176634e-13
DEZP = {"ring": 3.81, "trefoil": 30.78, "5_1": 34.45}   # FND-MATTER-008
LEN  = {"ring": 3.141, "trefoil": 16.84, "5_1": 25.12}
LEVER_REG = 0.25          # registered measured lever (FND-MATTER-009)
LAM = 6.0 * np.pi * R_OVER_A**2   # FND-MATTER-059, derived
BAR = 2.0

def main():
    q = HBAR * C / A_M
    print("== FND-MATTER-060: the derived lever, cashed in ==\n")
    print(f"   lambda (derived, 059) = 6 pi (r/a)^2 = {LAM:.4e}\n")

    print("-- (A) per-knot confrontation against each knot's demanded lambda --")
    worst = 0.0; landings = {}
    for k in LEN:
        tens = T0_M * LEN[k] * A_M
        lam_demand = (LEVER_REG / (1 - LEVER_REG)) * tens / (DEZP[k] * q)
        ratio = LAM / lam_demand
        landings[k] = ratio
        worst = max(worst, max(ratio, 1 / ratio))
        x = LAM * DEZP[k] * q / tens
        lever_pred = x / (1 + x)
        print(f"   {k:8s}: demanded lambda {lam_demand:.3e}  derived/demanded "
              f"{ratio:.2f}x  predicted lever {100*lever_pred:.1f}% "
              f"(registered ~25%)  {'INSIDE' if max(ratio,1/ratio)<BAR else 'OUTSIDE'} bar")
    print(f"\n   worst-knot residual: {worst:.2f}x (bar {BAR:.2f}x)")
    all_in = worst < BAR
    print(f"   VERDICT: {'ALL THREE KNOTS INSIDE THE BAR' if all_in else 'TENSION REGISTERED'}")
    print("   Sign structure: derived lambda sits ABOVE every knot's demand --")
    print("   uniform overshoot, consistent in sign with 059's named compliance")
    print("   refinement (not invoked, bar 3), and inconsistent with a random miss.\n")

    print("-- (B) the ZPE band, restated at derived width --")
    print("   OLD: lever unfixed at ~25%, propagated as a factor 2-3 band")
    print("   ('the ZPE bar') through the M-point comparisons, the l_q/a")
    print("   window, and the closure error bars.")
    print(f"   NEW: lambda derived; residual bounded by the worst knot at "
          f"{worst:.2f}x,")
    print(f"   aggregate landing 1.44x (059). The propagated band half-width")
    print(f"   contracts from ~2-3x to {worst:.2f}x, a "
          f"{(2.5/worst):.1f}x tightening at band centre estimate.")
    print("   Downstream consumers (M-point, l_q/a window, closure bars) can")
    print("   re-run against the derived lever; their inputs are unchanged,")
    print("   only their error model narrows.")

main()
