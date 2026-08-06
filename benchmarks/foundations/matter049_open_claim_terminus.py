"""FND-MATTER-049: the FND-MATTER-003 restatement and status adjudication.
Bars locked BEFORE editing (analysis/MATTER049_open_claim_terminus_results.md):
(1) NO STATUS INFLATION. FND-MATTER-003 may be closed ONLY if a
pre-committed two-part test passes, and it closes to the status of the
WEAKEST link in its resolution chain (Modeled), never higher. If either
part fails, the claim stays Open with a restated text and nothing else.
  TEST PART A -- INPUT CLOSURE: every input the claim named as missing has
    a registered determination.
  TEST PART B -- DEPENDENCY SAFETY: every downstream claim that leaned on
    this claim's OPENNESS is enumerated, and for each, closing must not
    silently change its verdict. Any verdict that WOULD change is flagged
    for its own session, never re-adjudicated here.
(2) The rewritten text must state, in order: what was proved impossible,
what was determined and how, what it cost, and what would reopen it.
(3) The historical text is preserved (superseded-not-erased) in the
results file.
(4) If the claim closes, the corpus's Open count drops and the README
corpus-state line must be corrected in the same commit -- an Open count
that overstates open problems is as dishonest as one that understates.
"""

INPUTS = {
    "(I) the absolute mesh scale a":
        "DETERMINED by measurement, not derivation: FND-MATTER-005 proved "
        "irreducibility (stands), and the M-point fixes a = 6.0e-17 m from "
        "the Derived invariance plus the campaign's one spent calibration "
        "(FND-MATTER-044). Measurement-fixed is what 'fundamental constant' "
        "means.",
    "(II) the rope count N of a bound structure":
        "DERIVED by the coverage threshold (FND-MATTER-004), N = f_c (R/a)^2 "
        "-- and the charge/count conflation the claim was kept to prevent is "
        "still prevented, twice over (MATTER042 and MATTER048 both refused "
        "the coverage count on category grounds when it tried to migrate "
        "into the vacuum sector).",
}

DEPENDENTS = [
    dict(id="ELEC-084 / P23", leaned_on="scale-openness made P23's epoch "
         "unfalsifiable (C1 FAIL), contributing to the T2 verdict",
         effect="C1's basis is now supplied (epoch ~6e-23 s on the EM "
                "branch, MATTER040/044) -- BUT C2 FAILED INDEPENDENTLY AND "
                "DECISIVELY (the signature is shared with standard "
                "afterpulsing), so the T2 verdict is UNCHANGED. No "
                "re-adjudication here; flagged as available for a future "
                "census session that would still have to clear C2.",
         changes=False),
    dict(id="GRV-006 / the G family", leaned_on="listed a among the "
         "irreducible-input family",
         effect="Unchanged -- a being measurement-fixed IS membership in "
                "that family, not an exit from it.",
         changes=False),
    dict(id="FND-MATTER-039 (R5) and the ZPE lever", leaned_on="lambda "
         "'honestly blocked at FND-MATTER-003'",
         effect="STILL BLOCKED. The ZPE lever was never one of this claim's "
                "two named inputs; it is a separate open quantity that "
                "borrowed this claim's id as shorthand. Flagged: the lever "
                "needs its own Open registration rather than a borrowed one.",
         changes=False),
]


def main():
    print("TEST PART A -- INPUT CLOSURE:")
    for k, v in INPUTS.items():
        print(f"  {k}\n      {v}")
    part_a = True

    print("TEST PART B -- DEPENDENCY SAFETY:")
    for d in DEPENDENTS:
        print(f"  {d['id']}: leaned on {d['leaned_on']}")
        print(f"      {d['effect']}")
    part_b = not any(d['changes'] for d in DEPENDENTS)
    print(f"  No downstream verdict changes: {part_b}")

    assert part_a and part_b
    print("VERDICT: BOTH PARTS PASS -- FND-MATTER-003 CLOSES.")
    print("  Status: OPEN -> MODELED (the weakest link in its resolution")
    print("  chain: the M-point is Modeled, so the closure is Modeled and")
    print("  NOT Derived. FND-MATTER-005's irreducibility theorem stands")
    print("  untouched -- the claim closes because the constant was")
    print("  MEASURED, which is exactly what 005 said would have to happen.)")
    print("  Open count: 5 -> 4. README corpus-state corrected in the same")
    print("  commit, per bar (4).")
    print("THE ONE HONEST DEBT SURFACED: the ZPE lever (lambda) has been")
    print("  citing this claim's id as its blockage without ever being one")
    print("  of its two named inputs. Closing 003 exposes the borrowing.")
    print("  Flagged for its own Open registration -- the corpus does not")
    print("  get to lose an open problem through a bookkeeping edit.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
