"""FND-MATTER-052: the lever session, part 2 -- the expression-fraction
derivation. Bars locked BEFORE computing
(analysis/MATTER052_expression_fraction_results.md):
(1) INSTRUMENT INHERITED, not re-chosen: the raw term is MATTER051's
committed continuum form E_raw = hbar c La/(4 pi a^2). Choosing the
instrument in a PRIOR session for prior reasons is the anti-retrofit
provenance this derivation rests on; the alternative (single-mode) form's
effect is displayed as sensitivity, not adopted.
(2) THE PHYSICAL HYPOTHESIS, stated: in this medium every action is
TENSION x AREA / c (GRV-093, machine-exact), and hbar corresponds to the
quantum area l_q^2/(4 pi alpha). A cell-scale mode cannot engage the
quantum area (the knot is one cell); it engages a CELL-SCALE area. The
expressed fraction of each naive hbar/2 is therefore
A_cell / A_quantum -- 'the medium expresses one cell's worth of area per
mode against the quantum area's worth the naive sum charges.'
(3) CANDIDATE AREAS PRE-NAMED before any evaluation (the GRV-093
discipline): CA1 the square cell a^2; CA2 the cell DISC pi a^2; CA3 the
coherence cell w^2 = a^2/3. All three are evaluated and displayed; the
measured ~25 percent lever selects among them; no candidate may be added
after seeing numbers.
(4) EXACTNESS CHECK, symbolic: for the selected candidate the predicted
lever fraction must be computed by sympy with the registered hbar relation
substituted, to verify the claimed cancellation (scale-free, alpha-free)
is an identity, not a numeric accident.
(5) STATUS DISCIPLINE: the winning structure registers as
MODELED-CONDITIONAL on one named geometric postulate (the expressed-area
identification). The postulate is a CANDIDATE GRANT -- adopting postulates
is the author's decision by standing rule -- so FND-MATTER-050 remains
OPEN pending that decision. Falsifier armed regardless: the structure
predicts the lever EXACTLY (parameter-free), so any sharpened measurement
of the zero-point share away from the predicted value kills the postulate.
"""
import numpy as np
import sympy as sp

HBAR, C = 1.054571817e-34, 2.99792458e8
ALPHA = 1 / 137.036
A_M, T0_M = 6.0056e-17, 434.0
L_RING = 3.141
LEVER_MEASURED = 0.25


def main():
    lq2 = 4 * np.pi * ALPHA * HBAR * C / T0_M
    A_quant = lq2 / (4 * np.pi * ALPHA)
    cands = {"CA1 square cell a^2": A_M**2,
             "CA2 cell disc pi a^2": np.pi * A_M**2,
             "CA3 coherence cell a^2/3": A_M**2 / 3}
    print("THE CANDIDATES (pre-named), predicted lever fraction f =")
    print("  E_raw * (A_cell/A_quant) / (T0 L a), instrument inherited:")
    E_raw_over_tension = HBAR * C / (4 * np.pi * A_M**2 * T0_M)
    results = {}
    for k, A in cands.items():
        f = E_raw_over_tension * (A / A_quant)
        results[k] = f
        print(f"  {k:26s}: f = {f:.4f}")
    print(f"  measured lever: ~{LEVER_MEASURED}")
    sel = "CA2 cell disc pi a^2"
    assert abs(results[sel] - 0.25) < 1e-6
    assert abs(results["CA1 square cell a^2"] - 0.0796) < 1e-3
    print(f"SELECTION: {sel} lands on the measurement; the square misses at")
    print("  0.0796 and the coherence cell at 0.0265 -- both displayed.")

    # EXACTNESS: symbolic cancellation
    hbarc, T0, a, lq, al = sp.symbols('hbarc T0 a l_q alpha', positive=True)
    E_raw = hbarc * sp.Symbol('L', positive=True) * a / (4 * sp.pi * a**2)
    frac = (sp.pi * a**2) / (lq**2 / (4 * sp.pi * al))
    tension = T0 * sp.Symbol('L', positive=True) * a
    f_sym = sp.simplify((E_raw * frac / tension).subs(
        hbarc, T0 * lq**2 / (4 * sp.pi * al)))
    print(f"EXACTNESS (sympy, hbar relation substituted): f = {f_sym}")
    assert f_sym == sp.Rational(1, 4)
    print("  f = 1/4 EXACTLY -- every scale cancels: a, T0, l_q, alpha, and")
    print("  the ropelength L all drop out through the registered hbar")
    print("  relation. The lever is predicted SCALE-FREE, which")
    print("  retroactively explains a fact the campaign observed without")
    print("  explaining: the ~25 percent survived every re-accounting of")
    print("  (a, T0) because it never depended on them.")

    print("SENSITIVITY (displayed, not adopted): the single-mode discrete")
    print("  form of the raw term carries coefficient 2x the continuum's,")
    print("  which would move the disc prediction to 1/2 -- the derivation's")
    print("  O(1) rests on the instrument committed in MATTER051's bars,")
    print("  and that provenance (chosen last session, for other reasons,")
    print("  before tonight's hypothesis existed) is what makes the 1/4 a")
    print("  prediction rather than a retrofit.")

    print("THE POSTULATE, named for the author's decision (a CANDIDATE")
    print("  GRANT, per the standing rule that grants are Mark's call):")
    print("  'A cell-scale fluctuation mode expresses the cell DISC's area")
    print("  against the quantum area.' IF ADOPTED: lambda closes at")
    print("  Modeled, f = 1/4 exactly and parameter-free, every band in the")
    print("  scale campaign tightens, and the MATTER051 whisper is")
    print("  PARTIALLY EXPLAINED (lambda and n_q are both cell-to-quantum")
    print("  area ratios; their O(few) offset is the snap stack vs the")
    print("  disc). FALSIFIER ARMED regardless of adoption: any sharpened")
    print("  measurement of the zero-point share away from exactly 1/4")
    print("  kills the postulate -- a parameter-free number is maximally")
    print("  exposed. FND-MATTER-050 REMAINS OPEN pending the decision.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
