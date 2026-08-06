"""QB-035: the timescale lever -- does the ribbon ontology supply an
intrinsic cutting time, and is that even the right SHAPE of prediction?
Bars locked BEFORE computing (analysis/QB035_timescale_lever_results.md):
(1) NO FITTING TO OBSERVED LIFETIMES, at any point, for any purpose. The
substrate time is built from registered quantities ONLY (the M-point mesh
scale and c); if it misses, it misses.
(2) THE UNIVERSALITY TEST RUNS FIRST, before any magnitude comparison,
because it is the stronger test and does not depend on getting the number
right: a substrate-intrinsic cutting time is a property of the MEDIUM, so
it must be the SAME for every physical platform. Observed memory
coherence times vary by many orders across platforms. If the shape of the
prediction (universality) is already excluded, the magnitude comparison is
reported as a secondary consistency note, not as the finding.
(3) MAGNITUDE COMPARISON, if run, uses only ORDER-OF-MAGNITUDE bracket
values for platform lifetimes -- stated as textbook-level uncontroversial
ranges, NOT as citations, and NOT as fitted or optimized numbers. Any
quantitative claim needing precision requires a literature session, which
this is not.
(4) A RESCUE IS PRE-BANNED: invoking an unfixed suppression factor to
reconcile a substrate time with observation is refused by name -- today's
FND-MATTER-042/047 established that the corpus's suppression mechanisms
are exhausted or unfixed, so borrowing one here would be circular.
(5) PERMITTED OUTCOMES include: the lever is dead (the ontology makes no
timescale prediction), or the lever is alive with a stated falsifier.
"""
import numpy as np

C = 2.99792458e8
A_M = 6.0056e-17          # M-point mesh scale (FND-MATTER-044)

# Order-of-magnitude brackets ONLY, per bar (3). Uncontroversial ranges.
PLATFORMS = {
    "atomic ensemble (warm/cold)": (1e-6, 1e-3),
    "trapped ion": (1e-3, 1e1),
    "rare-earth doped crystal": (1e-3, 1e4),
    "NV center (room T)": (1e-6, 1e-3),
}


def main():
    # (2) THE UNIVERSALITY TEST -- runs first, needs no magnitude
    lo = min(v[0] for v in PLATFORMS.values())
    hi = max(v[1] for v in PLATFORMS.values())
    spread = hi / lo
    print("THE UNIVERSALITY TEST (run first; magnitude-independent):")
    print("  A substrate-intrinsic cutting time is a property of the MEDIUM.")
    print("  The same weave underlies every apparatus, so such a time must be")
    print("  UNIVERSAL -- identical for every platform, and untunable by")
    print("  engineering. Observed coherence times, order-of-magnitude only:")
    for k, (a, b) in PLATFORMS.items():
        print(f"    {k:30s} ~{a:.0e} .. {b:.0e} s")
    print(f"  Observed spread across platforms: ~{spread:.0e}x "
          f"({np.log10(spread):.0f} orders).")
    print("  And the spread is SYSTEMATIC, not noise: it tracks isolation,")
    print("  temperature, and material engineering -- i.e. it tracks the")
    print("  ENVIRONMENT, which is exactly what a substrate-intrinsic time")
    print("  cannot do.")
    assert spread > 1e6
    print("  VERDICT: THE SHAPE OF THE PREDICTION IS EXCLUDED. An intrinsic")
    print("  ribbon-cutting time is falsified before any number is computed,")
    print("  because coherence is demonstrably an ENGINEERABLE quantity and")
    print("  a property of the medium is not engineerable.")

    # (3) SECONDARY consistency note -- magnitude, reported not relied upon
    t_mesh = A_M / C
    print("SECONDARY NOTE (magnitude; reported, not the finding):")
    print(f"  The corpus's ONLY registered time built from the mesh is")
    print(f"  a/c = {t_mesh:.2e} s. Against even the shortest bracket above")
    print(f"  ({lo:.0e} s), a parameter-free substrate lifetime is short by")
    print(f"  ~{np.log10(lo / t_mesh):.0f} orders; against the longest, "
          f"~{np.log10(hi / t_mesh):.0f} orders.")
    print("  So the magnitude fails too, and fails by an amount that VARIES")
    print("  with platform -- which is the universality verdict restated in")
    print("  numbers rather than an independent second failure.")
    assert lo / t_mesh > 1e15

    # (4) the pre-banned rescue, named and refused
    print("THE PRE-BANNED RESCUE, named and refused: one could posit an")
    print("  unfixed suppression factor carrying the ~19-28 orders. REFUSED")
    print("  by bar (4) and independently by today's results -- FND-MATTER-042")
    print("  found the corpus's suppression candidates unfixed and")
    print("  FND-MATTER-047 exhausted its channels, so borrowing one here")
    print("  would be circular. A suppression that also had to VARY by")
    print("  platform would not be a substrate property at all, which is the")
    print("  universality objection returning as arithmetic.")

    # (5) verdict and what survives
    print("VERDICT: THE TIMESCALE LEVER IS DEAD. The ribbon ontology supplies")
    print("  no decoherence timescale, and -- more decisively -- it should")
    print("  not: decoherence is environmental in this picture as in the")
    print("  standard one, so the ribbon is cut BY the environment on the")
    print("  environment's schedule, not by the medium on its own.")
    print("WHAT SURVIVES, and it is the constructive half:")
    print("  1. The ontology is CONSISTENT with platform-dependent coherence")
    print("     precisely BECAUSE it predicts no intrinsic time -- consistency")
    print("     by silence, which is worth stating but is not evidence FOR")
    print("     the picture and must never be cited as such.")
    print("  2. QB-034's conclusion is now CLOSED FROM BOTH SIDES: no lever")
    print("     in the decay SHAPE (degenerate or killed) and none in the")
    print("     TIMESCALE (wrong shape of prediction entirely). The")
    print("     repeater-network question is settled negatively and")
    print("     completely, with benchmarks on both halves.")
    print("  3. A GENUINE STRUCTURAL POINT for the ontology, registered as")
    print("     the session's positive: 'cutting the ribbon' must be an")
    print("     ENVIRONMENTAL COUPLING event, so any future ribbon dynamics")
    print("     owes a coupling term to the ambient weave -- the same place")
    print("     FND-MATTER-053 sent dE_zp tonight. Two independent sessions")
    print("     now point the same direction: the action is in the AMBIENT")
    print("     medium, not the object's interior.")
    print("NOT CLAIMED: any specific platform lifetime, any citation-grade")
    print("  comparison, any preferred-frame or protocol consequence.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
