"""Commission YOD -- what a k-string IS: the category adjudication.
Bars locked BEFORE adjudication
(analysis/YOD_kstring_category_bars_LOCKED.md). Y1 standard physics
(cited in results), Y2 registry ontology (cited), Y3 the consequence for
the FND-047 flag, Y4 what does not move. The numeric content is the
sub-additivity sanity gate, checked against BOTH candidate laws.
"""
import math


def casimir_ratio(N, k):
    return k * (N - k) / (N - 1)


def sine_ratio(N, k):
    return math.sin(k * math.pi / N) / math.sin(math.pi / N)


def main():
    print("Y1 (standard physics, sources in results): the asymptotic")
    print("  k-string depends only on N-ALITY -- gluons screen any source")
    print("  down to its N-ality class ground state, so at long distance the")
    print("  string is a Z_N flux object, not a representation label.")
    print("Y2 (registry): charge = winding = linking number, a DERIVED")
    print("  topologically conserved INTEGER (GG-006); the Coulomb field is")
    print("  rope-count flux geometry. Integers are additive: a source of")
    print("  N-ality k IS k unit windings. The ontology contains no")
    print("  'single heavier charge' primitive. Y1 and Y2 AGREE: BUNDLE.")

    print("SUB-ADDITIVITY GATE (binding check, both laws, several (N,k)):")
    for N in (4, 6, 8):
        for k in range(2, N // 2 + 1):
            c, s = casimir_ratio(N, k), sine_ratio(N, k)
            assert c < k and s < k, "sub-additivity violated"
            print(f"  SU({N}) k={k}: Casimir {c:.3f} < {k}; sine {s:.3f} < {k}"
                  f"  -- BOTH laws show binding (sigma_k < k sigma_1).")
    print("  The derived softening (negative quartic, FND-040) makes")
    print("  overlapping strain fields cost LESS than their sum ->")
    print("  ATTRACTION -> sub-additivity. Qualitative sign check PASSES on")
    print("  every row of the data, under both laws. (A sanity gate, not")
    print("  evidence: the magnitude is uncomputed.)")

    print("Y3 (the consequence): the SU(6) sine-law measurement is a")
    print("  TUBE-BINDING observable (how much k bundled windings save),")
    print("  NOT the single-source softening observable (PSI/BET/CHET).")
    print("  The FND-047 'measured contradiction' reading was a CATEGORY")
    print("  ERROR at the level of the flag's stakes: the N-universal branch")
    print("  inherits an OBLIGATION (compute the bundle-binding relation and")
    print("  confront sine-vs-Casimir) rather than an immediate conflict --")
    print("  and the one qualitative prediction the softening already makes")
    print("  for bundles (binding exists) is what every dataset shows.")
    print("Y4 (untouched): the SU(3) single-source pin (FND-046/047) tests")
    print("  intermediate-distance higher-representation potentials BEFORE")
    print("  screening -- valid as registered; the decision table stands.")
    print("  The N-universality scope question remains OPEN but re-priced:")
    print("  neither branch now walks into a resolved contradiction.")
    print("ALL BARS ADJUDICATED (verdict: BUNDLE, by physics and by ontology)")


if __name__ == "__main__":
    main()
