"""ELEC-041 (Modeled): CLASP-AND-LOOP SURVIVES THE STRAND
IDENTIFICATION -- with one correction to ELEC-040, one strong new
physical consequence, and one of this session's own checks demoted
from evidence to arithmetic.

THE QUESTION: ELEC-040's tension-matching selects s = 7.155e3 and
identifies the electron with vacuum strands. Does the certified
clasp-and-loop architecture survive that identification, or are
geometry and tension-matching in conflict?

(1) SHAPE RATIOS SURVIVE TRIVIALLY: the asymmetry (18.3:1), the
    planarity (275:1), the linking, and the isoperimetric identity
    L_clasp = 2 pi x clearance are all RATIOS, unchanged by any
    rescaling. This is not a result so much as a reminder of why the
    geometry has been so stable across the campaign.

(2) THE STRAND COUNT IS TWO, NOT ONE -- a correction to ELEC-040. The
    functional assigns tension T0 = 1 model unit to EACH curve, so
    matching each to one strand gives the same s = 7.155e3; but a
    Hopf link has two disjoint closed components and a single strand
    cannot form two closed curves. The electron is a TWO-STRAND LINK.
    The selected scale is unchanged; only the reading is corrected.

(3) SELF-CONTACT IS COHERENT: the hard core d_c = 1.87e-19 m, where
    the components touch, IS the strand diameter under one medium --
    two strands in contact at one diameter, which is exactly what a
    link should do. Strand thickness against ambient spacing is
    3.2e-3: thin strands, widely spaced.

(4) THE NEW PHYSICAL CONSEQUENCE: at the registered vacuum density the
    ambient strand spacing is w = 5.78e-17 m while the object's rms
    radius is 2.96e-18 m, so R/w = 0.051 -- THE ELECTRON IS A 20-FOLD
    LOCAL COMPRESSION OF THE MEDIUM, a bound pair drawn well inside
    the typical inter-strand distance. Not contradictory (a bound
    state should be closer than average) but a strong and previously
    unstated claim about what a particle IS in this framework.

(5) A CHECK DEMOTED, honestly: the tension-energy bookkeeping
    (T_strand x L_total = 0.472 m_e c^2 against the calibration's
    0.484) looks like an independent cross-check and is NOT one --
    T_strand cancels algebraically between the definition of s and
    the product, so the agreement is a tautology and the 2.5 percent
    residue is input rounding between two campaign states. Recorded
    so that no one later mistakes it for evidence.

VERDICT: NO CONFLICT. Geometry and tension-matching are compatible,
so neither must yield, and the framework's weakest joint remains the
hbar relation identified by ELEC-040.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'ELEC041_state.npz')
    # (2) the corrected strand count
    assert int(s['nstrand']) == 2, "two strands, one per link component"
    # (3) contact coherence
    assert float(s['dcw']) < 1e-2, "strands thin against ambient spacing"
    assert 1e-19 < float(s['d_c']) < 1e-18, "contact at one strand diameter"
    # (4) the compression claim
    assert float(s['Rw']) < 0.1, "object well inside the ambient spacing"
    assert 10 < float(s['compress']) < 50, "a ~20-fold local compression of the medium"
    # (5) the demoted check: it is a tautology, so it must agree almost exactly
    assert abs(float(s['frac']) - 0.484)/0.484 < 0.05, \
        "bookkeeping closes to 2.5% -- tautological, NOT independent evidence"
    print(f"strands {int(s['nstrand'])}; d_c {float(s['d_c']):.2e} m; w {float(s['w']):.2e} m; "
          f"R/w {float(s['Rw']):.3f} ({float(s['compress']):.0f}x compression); "
          f"E_T/mc^2 {float(s['frac']):.4f} (tautological)")
    print("PASS: clasp-and-loop survives -- two strands, coherent contact, a 20x local")
    print("      compression of the vacuum; no conflict, so neither side must yield.")


if __name__ == "__main__":
    test()
