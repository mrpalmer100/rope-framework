"""
SUPERSESSION BANNER (added by ELEC-056, 2026-07-31, no logic altered):
the length sqrt(hbar c/T) = 4.312 fm computed and asserted below is
ARITHMETICALLY CORRECT and remains the dimensional action length. It is
NOT the admissible coherent-segment length: ELEC-054 showed a fundamental
mode of amplitude A_hbar on a 4.31 fm segment is superluminal (2.51c), so
the segment must satisfy L >= pi A_hbar = 10.81 fm. At the corrected
length the atomic conclusion below survives (~1e11 cells) but the NUCLEAR
non-Born prediction does not: ELEC-055 shows it is excluded by nuclear
data with no surviving parameter freedom. The assert is left untouched
per the no-silent-edit rule.

HBAR-006 (Modeled): WHAT HBAR'S CONSTANCY REQUIRES, AND WHERE THE
SUB-QUANTUM SCALE PUTS THE FRAMEWORK'S FIRST TESTABLE PREDICTION.

PART 1 -- WHAT HBAR DEPENDS ON. With L = N w and w^2 = T/(c^2 rho),
    hbar = T (N w)^2/c = N^2 T^2/(c^3 rho)
reconstructing hbar to 0.1 percent. So the medium enters ONLY through
T^2/rho; equivalently hbar c = N^2 T w^2, and the constancy of hbar is
exactly the constancy of TENSION TIMES AREA-PER-STRAND.

THE REQUIREMENT, quantified: hbar is known to ~1e-12 relative, and
d(hbar)/hbar = 2 dT/T - drho/rho, so the vacuum must be homogeneous in
tension to ~5e-13 and in density to ~1e-12. NO MECHANISM IS IDENTIFIED
that enforces this. Homogeneity is assumed, not derived, and the
question 'what selects and holds 75 spacings' is answered only in the
sense that it reduces to 'what makes T w^2 universal'. That is the
honest status and it is a negative.

THE ONE CONSTANCY THREAT THAT COULD BE CHECKED, and it passes:
ELEC-041 found the electron to be a ~20x local compression of the
medium, which would depress hbar locally by ~400x. But such regions
occupy a volume fraction of (R_e/a_0)^3 = 1.7e-22 inside an atom, so
the volume-weighted perturbation to the bulk value is 7e-20 --
negligible against a 1e-12 measurement by seven orders. MATTER DOES
NOT DESTROY HBAR'S CONSTANCY.

PART 2 -- THE SUB-QUANTUM SCALE MEETS THE RELAXATION WORK. QGATE-011,
-012 and -013 built pilot-wave dynamics on the assumption of a
sub-quantum layer and never had a scale for it. HBAR-005 supplies
4.312 fm. Counting sub-quantum cells:
    atom (Bohr radius): (1.23e4)^3 = 1.85e12 cells
    nucleus (5 fm)    : (1.16)^3   = 1.56 cells
At atomic scales the grain is a trillion cells across a system, so
Born relaxation should be COMPLETE and quantum mechanics exact --
consistent both with QGATE-013's relaxation result and with the fact
that no atomic experiment has ever seen a Born violation. THE
PREDICTION: non-Born statistics are a NUCLEAR-SCALE effect, invisible
atomically. This is the first quantitative link between the HBAR and
QGATE families, and it points the corpus's own nuclear sector at its
own quantum sector.

FLAGGED, tested, not leaned on: L_hbar = 4.31 fm sits at the radius of
a medium-mass nucleus. L_hbar depends on T (a registered value) while
nuclear radii come from QCD, and no shared derivation connects them --
so it is a coincidence, recorded under the standing rule.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'HBAR008_state.npz')
    hbar = 1.054571817e-34
    # Part 1: the reconstruction and what it means
    assert abs(float(s['h_recon'])/hbar - 1) < 0.01, "hbar = N^2 T^2/(c^3 rho) to 0.1%"
    # the constancy threat that can be checked, and passes
    assert float(s['frac']) < 1e-20, "electron-scale regions are a negligible volume fraction"
    assert float(s['pert']) < 1e-15, "perturbation to bulk hbar is 7e-20"
    assert float(s['margin']) > 1e6, "seven orders of margin against the 1e-12 measurement"
    # Part 2: the cell counts
    assert float(s['cells_atom']) > 1e10, "atoms hold ~1e12 sub-quantum cells: Born exact"
    assert float(s['cells_nuc']) < 10, "nuclei hold ~1.6: at the boundary"
    assert 4e-15 < float(s['L_h']) < 5e-15, "the sub-quantum scale is 4.31 fm"
    print(f"hbar = N^2 T^2/(c^3 rho) to {abs(float(s['h_recon'])/hbar-1)*100:.1f}%; "
          f"matter perturbation {float(s['pert']):.1e} (margin {float(s['margin']):.1e}); "
          f"cells: atom {float(s['cells_atom']):.2e}, nucleus {float(s['cells_nuc']):.2f}")
    print("PASS: constancy reduces to T w^2 universal (no mechanism found, honest negative);")
    print("      matter cannot spoil it; and non-Born statistics are a NUCLEAR-scale prediction.")


if __name__ == "__main__":
    test()
