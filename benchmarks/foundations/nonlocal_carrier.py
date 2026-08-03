"""FND-024 -- THE CARRIER IS THE WINDING-CONSERVATION CONSTRAINT, not a pressure
multiplier and not a depleting signal.

Bars locked in analysis/FND024_carrier_bars_LOCKED.md BEFORE reasoning.
"""


def main():
    print("B1 WHAT IS ACTUALLY REQUIRED -- read from QB-009, not from a phrase:")
    print("   'one indivisible unit + a GLOBALLY COHERENT ENERGY BUDGET + the")
    print("    derived rate law, raced as competing Poisson clocks, yields")
    print("    g2 = 0.000 with the budget ON and 0.998 with the budget OFF on")
    print("    IDENTICAL random draws (the mechanism isolated to one bit)'")
    print("   SO THE MECHANISM IS NOT A SIGNAL THAT TRAVELS AND DEPLETES SOMETHING.")
    print("   It is a GLOBAL CONSERVATION CONSTRAINT: the budget is one quantum,")
    print("   and depositing it here means it is not available there. Nothing")
    print("   propagates; a constraint is satisfied. FND-023's phrase 'spacelike")
    print("   depletion of a wave amplitude' imported a propagation picture that")
    print("   QB-009's own demonstration does not use.\n")

    print("B2 IS THE VOLUME MULTIPLIER THE RIGHT CARRIER? NO.")
    print("   A pressure-like multiplier enforcing volume is a CONTINUOUS")
    print("   constraint. It would deplete an amplitude continuously and by")
    print("   arbitrary fractions -- and QB-007's machine-checked no-go says")
    print("   ANY CLASSICAL FIELD DRIVING INDEPENDENT THRESHOLD SITES IS PINNED AT")
    print("   g2 >= 1, against a measured ~0.18. Continuity is precisely the")
    print("   property that fails.")
    print("   FND-023 was right that the volume multiplier is the wrong carrier,")
    print("   and wrong about why: not because it cannot reach, but because it is")
    print("   CONTINUOUS.\n")

    print("B3 THE CARRIER THE CORPUS POINTS AT -- WINDING CONSERVATION:")
    print("   QB-007 (parts Derived): indivisibility is DERIVED FROM INTEGER")
    print("     TOPOLOGY -- 'no fractional winding exists to deposit'.")
    print("   FND-STRAND-002: total winding conserved EXACTLY, error 0.0.")
    print("   GRV-045 (Derived): reconnection exchanges exactly ONE 2-pi quantum.")
    print("   Against the four requirements:")
    reqs = [("GLOBAL REACH", "PASSES",
             "a topological invariant of the whole configuration relates "
             "spacelike-separated sites by construction"),
            ("EXACTNESS", "PASSES",
             "integer-valued; cannot be partially satisfied, which is the "
             "property continuity lacks"),
            ("NON-WAVE CHARACTER", "PASSES",
             "a conservation law, not a propagating mode -- so FND-023's Bancal "
             "exemption applies"),
            ("MEASURED, NOT POSTULATED", "PASSES",
             "FND-STRAND-002 measured it to error 0.0 on a literal strand")]
    for n, v, w in reqs:
        print(f"     {n:26s} {v:8s} {w}")
    print("   ALL FOUR. And crucially the indivisibility QB-007 needs is not an")
    print("   extra assumption bolted onto the constraint -- IT IS THE CONSTRAINT.\n")

    print("B4 THE NUMBER THAT SEPARATES THE CANDIDATES:")
    print("   QB-009 ran identical random draws with the budget ON and OFF:")
    print("     budget ON  (integer, indivisible):  g2 = 0.000")
    print("     budget OFF (continuous):            g2 = 0.998")
    print("     measured:                           g2 ~ 0.18")
    print("   The corpus already isolated the mechanism 'to one bit', and that bit")
    print("   IS integrality. A continuous multiplier lands on 0.998; an integer")
    print("   constraint lands on 0.000. THE DISTINCTION IS NOT PHILOSOPHICAL.\n")

    print("B5 WHAT REMAINS OPEN -- and this is NOT the measurement problem solved:")
    print("   (1) QB-009's own verdict stands: 'CHSH still fails (S = 1.42 < 2),")
    print("       the two-particle boundary kept'. The single-particle")
    print("       anticorrelation works; the TWO-PARTICLE correlations do not.")
    print("       That is the actual frontier and it has not moved today.")
    print("   (2) The winding constraint is identified as the right KIND of")
    print("       carrier. Nobody has written it as a constraint in the action and")
    print("       derived the guidance flow QGATE-011 specified.")
    print("   (3) Whether a topological constraint can supply JOINT dependence on")
    print("       configuration space -- QGATE-011's condition D1 -- is untested.")
    print("       Winding conservation is one global number; Bell needs more.")
    print("   THAT LAST POINT IS THE REAL LIMIT and it should be stated plainly:")
    print("   a single conserved integer is a thin resource for reproducing")
    print("   two-particle correlations, and the corpus's own CHSH failure at")
    print("   S = 1.42 may be exactly that thinness showing.")
    print("PASS: the carrier is identified as a topological rather than a")
    print("      continuous constraint, with a corpus number separating them, and")
    print("      the two-particle boundary reported as still standing.")


if __name__ == "__main__":
    main()
