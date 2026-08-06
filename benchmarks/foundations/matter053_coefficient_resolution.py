"""FND-MATTER-053: the coefficient session -- continuum vs discrete mode
counting for a cell-scale knot, run as the pre-condition of the
MATTER052 grant decision (the author chose option C: settle the counting
before deciding the postulate).
Bars locked BEFORE computing (analysis/MATTER053_coefficient_results.md):
(1) THE BOUNDARY CONDITION IS NAMED FIRST AND IS NOT FREE: the electron
knot is a RING (closed loop, ropelength L*a). A closed loop takes PERIODIC
boundary conditions, k_n = 2 pi n/(L a), n = +-1, +-2, ...  The open-string
form k_n = n pi/(L a) used implicitly by the continuum instrument applies
to a segment with ends, which a ring does not have. This is fixed by the
ontology, not chosen for convenience.
(2) THE CUTOFF is the registered mesh cutoff k_max = 1/a (one mode per
cell; FND-017's spacing is the medium's own shortest wavelength).
(3) VERDICT GRAMMAR, pre-committed THREE ways:
    (a) if the discrete sum reproduces the continuum coefficient within a
        factor 1.5, the 1/4 HARDENS and the grant decision proceeds;
    (b) if it differs by a bounded O(1) factor, the 1/4 is REPLACED by the
        corrected exact value and the grant is re-posed with that number;
    (c) if the discrete count returns ZERO admissible modes, the
        mode-sum PICTURE ITSELF is falsified for cell-scale knots, the
        MATTER052 derivation is KILLED-AND-KEPT, and the session must
        report what the zero-point term in the two-term mass model can
        then legitimately be.
(4) NO RESCUE BY RECHOOSING: if the verdict is (c), the session may NOT
switch boundary conditions, cutoffs, or knot identifications to recover a
non-zero count. Any such move is a retrofit and is forbidden here; it may
be proposed as a future session with its own bars.
(5) The MATTER052 claim must be updated on its face with whatever verdict
lands, tonight.
"""
import numpy as np

HBAR, C = 1.054571817e-34, 2.99792458e8
A_M, T0_M = 6.0056e-17, 434.0
L_RING = 3.141          # ring ropelength in units of a (FND-MATTER-007)
L_TREFOIL, L_51 = 16.84, 25.12


def admissible_modes(L):
    """Periodic BCs on a loop of circumference L*a; cutoff k <= 1/a."""
    # k_n = 2 pi n / (L a) <= 1/a  =>  n <= L/(2 pi)
    n_max = int(np.floor(L / (2 * np.pi)))
    return n_max


def main():
    print("BOUNDARY CONDITION (fixed by the ontology, not chosen):")
    print("  the knot is a CLOSED LOOP -> periodic BCs, k_n = 2 pi n/(L a).")
    print("  The open-segment form n pi/(L a) does not apply to a ring.")
    print(f"CUTOFF: k_max = 1/a (registered mesh cutoff).")
    print("ADMISSIBLE MODE COUNT n_max = floor(L/(2 pi)):")
    for name, L in (("ring (electron)", L_RING), ("trefoil", L_TREFOIL),
                    ("5_1", L_51)):
        n = admissible_modes(L)
        k1 = 2 * np.pi / (L * A_M)
        print(f"  {name:16s} L = {L:6.3f} -> n_max = {n}"
              f"   (lowest mode k_1 = {k1 * A_M:.2f}/a)")
    n_ring = admissible_modes(L_RING)
    assert n_ring == 0

    print("VERDICT: BRANCH (c) -- ZERO ADMISSIBLE MODES for the ring.")
    print("  The electron ring's circumference is pi a, so its LONGEST")
    print("  available wavelength is pi a and its lowest transverse")
    print("  wavenumber is k_1 = 2/a -- a factor 2 ABOVE the mesh cutoff.")
    print("  A cell-scale loop cannot host a transverse standing wave at")
    print("  all: there is no room for one wavelength inside one cell.")
    print("  THE MODE-SUM PICTURE IS FALSIFIED for cell-scale knots.")
    print("CONSEQUENCE 1: FND-MATTER-052's derivation is KILLED-AND-KEPT.")
    print("  The 1/4 was computed from a continuum integral over a mode")
    print("  band that, counted honestly under the ontology's own boundary")
    print("  condition, is EMPTY. The exact cancellation was real algebra")
    print("  performed on an empty set -- which is exactly the failure mode")
    print("  the sensitivity clause flagged and the reason option C existed.")
    print("CONSEQUENCE 2: the MATTER051 hierarchy (1607x) DISSOLVES with it.")
    print("  There is no 'naive one-loop term 1607x too big' to suppress;")
    print("  the knot has no internal zero-point tower to renormalize.")
    print("CONSEQUENCE 3, the constructive part -- what the two-term model's")
    print("  dE_zp term can LEGITIMATELY be, given the count:")
    print("  NOT the knot's own internal modes (none exist). The surviving")
    print("  candidates, named for a future bars session and NOT adjudicated")
    print("  here: (i) the AMBIENT weave's modes perturbed by the knot's")
    print("  presence (a Casimir-type with/without difference in the")
    print("  surrounding medium, which is what dE_zp was always DEFINED as")
    print("  in FND-MATTER-009 -- the with/without framing survives intact);")
    print("  (ii) longitudinal or torsional branches, whose dispersion and")
    print("  cutoff differ and must be counted separately before any claim;")
    print("  (iii) sub-cell structure, which has no registered carrier")
    print("  (FND-MATTER-047's arm (i)) and cannot be invoked for free.")
    print("  Note (i) is not a rescue of tonight's kill: it is the ORIGINAL")
    print("  registered definition, and it lives in the AMBIENT medium where")
    print("  mode counting is unproblematic -- so lambda remains OPEN and")
    print("  the campaign's factor 2-3 ZPE bar STANDS UNCHANGED.")
    print("GRANT DECISION: the MATTER052 postulate is WITHDRAWN FROM")
    print("  CONSIDERATION -- not declined by the author but voided by its")
    print("  own pre-condition. The bet count and the grant count are")
    print("  UNCHANGED at their prior values; nothing was adopted.")
    print("NO RESCUE ATTEMPTED, per bar (4): boundary conditions, cutoff,")
    print("  and knot identification are left exactly as registered.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
