# ELEC-056 — Does the sub-quantum programme survive the loss of its anchor? Locked bars

## Commission
ELEC-055 excluded the mesoscopic-hbar picture and ELEC-054 corrected the
admissible coherent length from 4.31 fm to >= 10.81 fm. HBAR-006 had supplied
the pilot-wave programme (QGATE-011..017) with "a scale for the sub-quantum
layer it never had". That anchor is now gone. Question: does the programme
survive, and in what status?

## Locked bars
B1 (DEPENDENCY AUDIT, structural). Machine-check the registry: do any of
   QGATE-011..017 depend, directly or transitively, on HBAR-005 or HBAR-006?
   Report the actual closure, not an impression.
B2 (DIMENSIONALITY AUDIT, structural). Machine-check their benchmarks for any
   dimensionful length, mass or action constant. If the code is scale-free,
   the anchor was never load-bearing IN THE MECHANISM, whatever the prose said.
B3 (WHAT WAS ACTUALLY LOST). Recompute HBAR-006's cell counts at the corrected
   length for an atom and a nucleus. Determine precisely which of its two
   conclusions survives: (a) Born exactness at atomic scales, (b) the nuclear
   non-Born prediction. Report each separately -- the anchor may have been
   carrying one and not the other.
B4 (STATUS VERDICT). Assign one of: SURVIVES INTACT / SURVIVES UNANCHORED /
   FALLS. The distinction that matters is between losing a foundation and
   losing a bridge to observation. State which, and register the consequence
   for the programme's testability without softening it.
B5 (HYGIENE). benchmarks/foundations/hbar_constancy_and_scale.py asserts the
   4.31 fm scale. Its ARITHMETIC is correct (sqrt(hbar c/T) is that number);
   only the identification of that length as the admissible coherent segment
   was wrong. Per the no-silent-edit rule: add a supersession banner, do not
   alter the assert or any locked bar.
