"""FND-MATTER-048: the arm-(ii) survey -- non-spectral mechanisms enumerated
under locked bars. Bars locked BEFORE computing
(analysis/MATTER048_nonspectral_survey_results.md):
(1) THE ENUMERATION IS CLOSED AND PRE-COMMITTED, drawn from the registry's
actual non-spectral structures: C1 coverage/percolation counting
(FND-MATTER-004's f_c (R/a)^2), C2 linking-number density (GG-006's
integer-valued charge), C3 the Chern-Weil/holonomy input (the EM sector's
topological quantization), C4 constraint counting per cell (FND-005's
single dimensionless coupling Pi), C5 the load-sharing count itself
(GRV-006's EH/T0). No candidate may be added after the first number.
(2) ADMISSION CRITERIA, all four required, applied BEFORE numerics:
  A1 NON-SPECTRAL: the mechanism must not be a mode sum (else MATTER047
     already excluded it in-class);
  A2 REGISTERED CARRIER: the structure must exist in the registry with a
     status, not be invented here;
  A3 EXTENSIVE-CAPABLE: it must admit a large pure number WITHOUT a new
     input -- a mechanism whose size is itself a free parameter is not an
     explanation and is refused as a relabeling;
  A4 VACUUM-SECTOR: it must be a property of the ambient weave, not of a
     bound structure (the FND-MATTER-004 category rule from MATTER042).
(3) A candidate failing ANY criterion is refused WITHOUT numerical
evaluation -- numbers are not computed for refused candidates, because a
number invites a coincidence and the corpus has paid for that lesson.
(4) VERDICT GRAMMAR: if no candidate passes all four, the arm is registered
CLOSED-BY-ENUMERATION at the survey's scope, the trichotomy collapses to
two arms, and arm (iii) (G as input) is registered as the CORPUS'S WORKING
POSITION -- not a defeat, a determination.
(5) SCOPE CLAUSE, mandatory on the claim's face: closed-by-enumeration is
bounded by the enumeration. An unregistered mechanism is not excluded; the
claim must state what would reopen the arm.
"""

CANDIDATES = [
    dict(id="C1", name="coverage/percolation counting (FND-MATTER-004)",
         A1=True,  A2=True,  A3=True,  A4=False,
         why="f_c (R/a)^2 counts ropes in a BOUND STRUCTURE (an atom's R). "
             "The vacuum weave has no R. Refused on the same category rule "
             "MATTER042 applied to N^(3/2) -- and note this is the SECOND "
             "time this candidate has presented itself in the campaign."),
    dict(id="C2", name="linking-number density (GG-006)",
         A1=True,  A2=True,  A3=False, A4=True,
         why="Lk is the charge quantum and is integer-valued per defect; a "
             "LARGE linking density in the vacuum would be a large vacuum "
             "charge density, which the EM sector's neutrality forbids. Its "
             "size is not free -- it is pinned to zero in the ambient weave."),
    dict(id="C3", name="Chern-Weil / holonomy quantization (EM sector)",
         A1=True,  A2=True,  A3=False, A4=True,
         why="The topological input QUANTIZES (fixes integers and the Dirac "
             "condition); it supplies no magnitude. A quantization condition "
             "cannot generate 1e28 -- it constrains, it does not scale."),
    dict(id="C4", name="constraint counting per cell (FND-005)",
         A1=True,  A2=True,  A3=False, A4=True,
         why="FND-005 is Derived and states the parameter count exactly: ONE "
             "dimensionless coupling Pi = kappa a/T. A constraint-counting "
             "enhancement would need a second large dimensionless number in "
             "the same sector, which the Derived count forbids. This is the "
             "survey's sharpest refusal: the corpus's own theorem excludes it."),
    dict(id="C5", name="load-sharing count (GRV-006's EH/T0)",
         A1=True,  A2=True,  A3=False, A4=True,
         why="This is the RESTATEMENT of the gap in count form (MATTER045 "
             "proved it an identity). Admitting it would be the phantom "
             "anchor returning as a mechanism. Refused as identity."),
]


def main():
    print("THE ENUMERATION (closed, pre-committed; five candidates):")
    passed = []
    for c in CANDIDATES:
        crit = [c['A1'], c['A2'], c['A3'], c['A4']]
        names = ["A1 non-spectral", "A2 registered carrier",
                 "A3 extensive-capable", "A4 vacuum-sector"]
        fails = [n for n, ok in zip(names, crit) if not ok]
        status = "ADMITTED" if not fails else f"REFUSED ({', '.join(fails)})"
        print(f"  {c['id']} {c['name']}")
        print(f"      {status}")
        print(f"      {c['why']}")
        if not fails:
            passed.append(c)

    assert not passed, "a candidate passed -- numerics required, grammar changes"
    print("VERDICT (pre-committed grammar): NO CANDIDATE PASSES ALL FOUR.")
    print("  ARM (ii) IS CLOSED-BY-ENUMERATION at this survey's scope. No")
    print("  numbers were computed for refused candidates, by bar (3) -- a")
    print("  number invites a coincidence, and the corpus has paid for that.")
    print("  THE TRICHOTOMY COLLAPSES TO TWO:")
    print("    (i)   sub-strand structure -- Conjecture, no registered")
    print("          carrier, unchanged by this survey;")
    print("    (iii) G AS IRREDUCIBLE INPUT -- registered as the CORPUS'S")
    print("          WORKING POSITION. Not a defeat: a determination, now")
    print("          reached by three independent routes (GRV-006's")
    print("          underdetermination exhibit, MATTER047's channel")
    print("          exhaustion, and tonight's enumeration).")
    print("THE PATTERN, fourth occurrence: C1 is the coverage count")
    print("  presenting itself a SECOND time, and C5 is the phantom anchor")
    print("  returning as a mechanism -- the campaign's misassigned-ontology")
    print("  failure mode tries to re-enter through every new door, which is")
    print("  precisely why the criteria are applied before the arithmetic.")
    print("SCOPE CLAUSE (mandatory): closed-by-enumeration is bounded BY the")
    print("  enumeration. An unregistered mechanism is NOT excluded. WHAT")
    print("  WOULD REOPEN ARM (ii): any registered structure that is")
    print("  (a) non-spectral, (b) a property of the ambient weave, and")
    print("  (c) carries a magnitude not fixed by an existing Derived count")
    print("  -- FND-005 is the gate, so a genuinely new vacuum-sector")
    print("  dimensionless quantity would have to enter the corpus first,")
    print("  and that entry would itself be the finding.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
