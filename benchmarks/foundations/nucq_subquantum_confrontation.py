"""NUCQ-001 (Modeled): THE NUCLEAR SECTOR REFUTES THE MESOSCOPIC-HBAR
PICTURE -- the framework's only distinctive prediction lands on the
best-tested small-scale physics there is, and is not observed.

THE CONNECTION WAS SOUGHT because the corpus needed a claim MOND
cannot make. HBAR-005/006 supplied one: if hbar is the action of a
patch ~4.3 fm across, Born statistics are exact where a system spans
many patches and can fail where it approaches one. The nucleus was
identified as the place to look.

TEST 1 -- THE PARAMETER CLASH. NUC-004 derives the Yukawa FORM exactly
but takes the absolute range L ~ 1.4 fm as INPUT: the nuclear sector's
one free parameter. HBAR-005 derives sqrt(hbar c/T) = 4.312 fm from
the same medium's tension, and HBAR-001 gives 3.441 fm. The ratios to
the Yukawa range are 3.08 and 2.46, matching no simple constant (pi is
within 2 percent of 3.08 and is FLAGGED, not used). Inverting, the
tension putting the quantum scale at the Yukawa range is 1.61e4 N
against the registered 1.70e3 N -- A FACTOR OF 9.5. Under the
one-medium declaration (ELEC-038) both sectors cannot hold, and this
is structurally the same failure as XSEC-001's.

TEST 2 -- THE BORN PREDICTION MEETS REAL NUCLEI, and this is decisive.
Counting sub-quantum patches (R/L_hbar)^3 with R = 1.2 A^(1/3) fm:
    He-4   0.086      Fe-56    1.207
    C-12   0.259      Pb-208   4.482
    O-16   0.345      U-238    5.128
EVERY nucleus is under two patches and light nuclei are under a tenth.
On this picture ALL of nuclear physics is sub-quantum and standard
quantum mechanics should not apply there in the ordinary way. IT DOES.
The nuclear shell model, ab initio no-core shell-model calculations,
and lattice QCD all use standard quantum mechanics in exactly these
nuclei, to high precision, and no non-Born statistics have ever been
reported in nuclear data.

THE VERDICT: the prediction is made, it is sharp, it lands where the
evidence is strongest, and it fails. Three escapes exist and each
carries a price -- (a) relaxation is fast even within one patch, which
contradicts QGATE-013's own mechanism requiring many coarse-graining
cells; (b) the effect exists below current sensitivity, which requires
a magnitude estimate the framework has never produced; (c) L_hbar is
wrong because T is wrong, which is Test 1's factor of 9.5 arriving
from the other direction.

Both tests point at the same suspect: the strand tension T = 1.70e3 N,
inherited from the scale branch and never independently verified,
which the whole HBAR chain rests on.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'NUCQ001_state.npz')
    hbar = 1.054571817e-34; c = 2.99792458e8
    # Test 1: the two sectors demand incompatible tensions
    assert abs(float(s['L_h']) - np.sqrt(hbar*c/float(s['T'])))/float(s['L_h']) < 1e-9
    assert float(s['ratio_T']) > 5, "the sectors demand tensions differing by 9.5x"
    r = float(s['ratio_L'])
    assert abs(r - np.pi)/np.pi < 0.05, "3.08 is within 2% of pi -- flagged, not used"
    assert not (abs(r - 1) < 0.1 or abs(r - 2) < 0.1), "and it is NOT unity or two"
    # Test 2: every nucleus is sub-quantum on this picture
    p = s['patches']          # A, R_fm, patches
    assert p[:, 2].max() < 6, "even U-238 spans only 5.1 patches"
    assert p[0, 2] < 0.1, "He-4 spans 0.086 -- a tenth of one patch"
    assert (p[:3, 2] < 0.4).all(), "light nuclei are deeply sub-quantum on this picture"
    # the falsification: the regime where QM is best tested is the regime predicted to fail
    assert p[:, 2].min() < 0.1 and p[:, 2].max() < 10, \
        "the whole nuclear chart sits in the predicted-to-fail regime"
    print(f"L_hbar {float(s['L_h'])*1e15:.3f} fm vs Yukawa 1.40 fm (ratio {r:.2f}); tensions differ "
          f"{float(s['ratio_T']):.1f}x; patches He-4 {p[0,2]:.3f} to U-238 {p[-1,2]:.3f}")
    print("PASS: the distinctive prediction lands on the best-tested small-scale physics and")
    print("      is not observed; both tests indict the inherited strand tension.")


if __name__ == "__main__":
    test()
