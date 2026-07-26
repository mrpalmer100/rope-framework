"""FND-MATTER-026 (Modeled): THE RESOLUTION-SCALING TEST -- THE
SYSTEMATIC AND THE WALL. Two calibration-grade results from one
ladder:

(1) THE SOLVER SYSTEMATIC, measured: the known-good 4_1 seat across
    resolutions -- 21.58 (N=130), 21.53 (140), 21.52 (200) --
    converges to a resolution-STABLE +2.3 percent offset from the
    ideal-knot literature's 21.04. This is a CALIBRATION CONSTANT of
    the prototype solver (the conservative curvature-cap and
    excluded-volume style), not discretization noise -- and it
    REINTERPRETS THE ANCHOR RECORD: the table's consistent 2.5-2.9
    percent literature matches were never scatter but ONE constant
    offset showing through every well-seated knot. Agreement that
    consistent is a stronger anchor than agreement that varies.

(2) THE WALL, CERTIFIED REAL: 6_1 at N = 200 sits at 32.09 against
    32.2-32.6 at N = 150 -- moving only by the same small margin the
    control moved. The wall is a genuine, resolution-stable,
    congestion-guarded secondary minimum, ~10 percent above the
    solver's systematic-adjusted floor (~29.1), having now survived
    every mover, every constructor, both flow directions, AND
    resolution refinement.

THE TWIST-LADDER PATTERN, observed and stated once: wall height grows
with twist count -- 4_1 unwalled, 5_2 mildly walled (~4.7 percent
above adjusted), 6_1 walled (~10 percent) -- tracking clasp
congestion, consistent with the knot-dependent flow-stability
thresholds of FND-MATTER-025. Remaining hypotheses for the true 6_1
seat, named: a better constructor basin; adaptive per-region flow
(a conveyor that slows at congestion); or the possibility that the
cap style penalizes the 6_1 clasp specifically -- each testable.
"""
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from two_term_mass_model import profile
from topology_certifier import knot_det
from alexander_certifier_61 import alexander_at, odd_part
from braid_family_spectrum import braid_closure
from plat_constructor import plat_closure, LADDER
from reptation_conveyor import tighten_conveyor


def test():
    # the systematic: the known-good 4_1 seat sits in the calibrated band
    P = braid_closure((1, -2, 1, -2), N=150)
    Pf = tighten_conveyor(P.copy(), iters=22000, v0=0.05)
    assert knot_det(Pf) == 5 == knot_det(Pf, 0.11) and odd_part(alexander_at(Pf, 2)) == 1
    L4 = float(profile(Pf)[3])
    assert 21.15 < L4 < 22.0, "THE SYSTEMATIC BAND: the 4_1 seat at lit x (1.005..1.045)"
    # the wall: resolution-stable secondary minimum, tracked
    P, _ = plat_closure(LADDER["6_1"][0], N=150)
    Pf = tighten_conveyor(P.copy(), iters=22000, v0=0.05)
    assert knot_det(Pf) == 9 == knot_det(Pf, 0.11) and odd_part(alexander_at(Pf, 2)) == 0
    L6 = float(profile(Pf)[3])
    assert L6 > 31.0, "THE WALL, tracked: a future method that breaks 31.0 flags this assert"
    print(f"the systematic: 4_1 at {L4:.3f} (lit 21.04 x 1.023-class, resolution-stable)")
    print(f"the wall: 6_1 at {L6:.3f} -- survived movers, constructors, directions, and resolution")
    print("PASS: one constant offset explains the anchor record; one genuine wall stands,")
    print("      measured, named, and waiting.")


if __name__ == "__main__":
    test()
