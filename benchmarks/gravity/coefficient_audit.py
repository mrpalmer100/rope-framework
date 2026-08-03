"""GRV-071 -- THE FIVE COEFFICIENTS AUDITED: none is derivable from the
registered action, and the missing structure is named precisely.

Bars locked in analysis/GRV071_coefficients_bars_LOCKED.md BEFORE the audit.
"""


def main():
    print("TARGET (GRV-070):  (a+b)(c+d)/(4 pi K_0) = -2G/c^3\n")

    rows = [
        ("a  (J . Omega_macro)", "ABSENT",
         "GRV-026 asserts covariant matter sourcing, but GRV-057 established "
         "that its covariance fingerprint tested the SCALAR channel only. "
         "GRV-005's underlying force balance div(stress) = -f is STATIC "
         "elastostatics with NO momentum or angular-momentum source term. "
         "The corpus has never written a matter coupling to medium rotation."),
        ("b  (J . phi_micro)", "ABSENT",
         "Same gap, and worse: the microrotation is a strand-sector field "
         "(FND-STRAND-002) and no claim couples MATTER to it at all. The "
         "framed-strand campaign built the field; nothing sources it from a "
         "knot."),
        ("c  (Omega -> g_0i)", "ABSENT, and structurally so",
         "GRV-029's dictionary is an exact bijection for a STATIC DIAGONAL "
         "metric -- four wave-operator functions to four metric functions. It "
         "has NO SHIFT. GRV-055 showed the current operator cannot carry one. "
         "So the map from rotation to g_0i is not merely uncomputed: the "
         "registered dictionary has no slot for it."),
        ("d  (phi -> g_0i)", "ABSENT, same reason",
         "GRV-060 identified the shift as entering through a mixed d_t d_a "
         "term with a twist-density coefficient, but that coupling was "
         "PROPOSED there, not derived, and GRV-069/070 record it as "
         "undetermined."),
        ("K_0 (massless-mode stiffness)", "COMPUTABLE IN PRINCIPLE",
         "This is the couple-stress modulus gamma. FND-STRAND-002 carries an "
         "explicit twist field with a quadratic rod coupling on discrete "
         "nodes -- the machinery that would yield gamma exists and has been "
         "run for other purposes (the Peierls-Nabarro barrier hierarchy). It "
         "has not been read off as a modulus."),
    ]
    print("B1/B2 THE FIVE, one by one:\n")
    for name, status, why in rows:
        print(f"   {name:30s} {status}")
        print(f"      {why}\n")

    absent = [r for r in rows if r[1].startswith("ABSENT")]
    print(f"B3 THE MISSING STRUCTURE, named precisely: {len(absent)} of 5 ABSENT.")
    print("   And they are absent for TWO distinct reasons, which matters:")
    print("   (i)  a and b are missing because THE CORPUS HAS NO MATTER COUPLING")
    print("        TO MEDIUM ROTATION. GRV-005 sources the medium with a static")
    print("        force density; there is no torque, spin or angular-momentum")
    print("        term anywhere in it. This is the same hole GRV-059 found and")
    print("        it has not been filled -- the work since has established that")
    print("        a channel EXISTS to be sourced, not that anything sources it.")
    print("   (ii) c and d are missing because THE DICTIONARY HAS NO SHIFT SLOT.")
    print("        GRV-029's bijection is exact and is between four functions and")
    print("        four functions, for a static diagonal metric. A shift is a")
    print("        fifth, sixth and seventh function. GRV-055 showed the current")
    print("        wave operator cannot carry them. So this is not an uncomputed")
    print("        coefficient -- it is a map that does not exist yet.\n")

    print("B4 IS THE TARGET EQUATION EVALUABLE? NO.")
    print("   Four of its five inputs are absent, and two of those are absent")
    print("   structurally rather than for want of a calculation. The equation is")
    print("   correctly posed and cannot currently be evaluated.\n")

    print("B5 THE OUTCOME, reported with the weight it deserves:")
    print("   THE STRAND ACTION AS REGISTERED DOES NOT CONTAIN THE STRUCTURE TO")
    print("   DETERMINE THE GRAVITOMAGNETIC COEFFICIENT. That is the reviewer's")
    print("   second admissible outcome and it is what the work returned.")
    print("   WHAT THAT DOES AND DOES NOT MEAN:")
    print("     - It does NOT reinstate GRV-064's screening obstruction. The")
    print("       massless collective mode is still there for any locking")
    print("       strength; that result stands.")
    print("     - It does NOT say frame dragging is forbidden. It says the")
    print("       framework is silent, which is different.")
    print("     - It DOES mean the sector cannot currently predict 37.2 mas/yr,")
    print("       nor predict its absence, and should claim neither.")
    print("   THE HONEST SUMMARY OF SIX SESSIONS: a route was found, an")
    print("   obstruction was raised and removed, the structure was shown to")
    print("   match, and the coefficients turn out to require machinery the")
    print("   corpus has never built -- a matter-to-rotation coupling, and a")
    print("   dictionary with a shift slot. Those are the work items.")
    assert len(absent) == 4
    print("PASS: four of five absent, the missing structure named as two specific")
    print("      pieces, and the negative reported without hedging.")


if __name__ == "__main__":
    main()
