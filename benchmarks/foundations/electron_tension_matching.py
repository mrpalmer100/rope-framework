"""ELEC-040 (Modeled): THE COINCIDENCE DISSOLVED, AND A NEW ONE-MEDIUM
CONSTRAINT THAT NEARLY RESCUES THE SCATTERING BOUND. Two results: the
recurring 2e4 is a tautology, and tension-matching selects a scale at
which the object is only 3x too large.

(1) THE THREE 2e4's ARE ONE NUMBER. F1 (form-factor failure) =
    rms_model L0 / r_bound; ELEC-036's branch A ratio =
    (alpha hbar c)/kappa_req = L0/L0_req; its branch B ratio =
    m_req/m_e = L0/L0_req. Since L0_req is DEFINED as r_bound/rms_model,
    all three are the same quantity written three ways (agreeing to
    2.4 percent, the difference being the recalibration between
    ELEC-036 and ELEC-034). F3, the H4 nuclear-vacuum shortfall, is
    F1 multiplied by n_t0 (hbar/W0)(T0_s/c^2)/(rho_nuc R L) = 0.986 --
    proportional to F1 by construction through ELEC-037's invariant,
    with the near-unity prefactor an accident. THE RECURRENCE IS NOT
    EVIDENCE OF ANYTHING, and the corpus's rule against leaning on
    underived coincidences is hereby discharged by deriving it away.

(2) THE TENSION-MATCHING CONSTRAINT, which ELEC-038's declaration
    forces and nobody had imposed: under ONE medium an electron rope
    must be a whole number of vacuum strands. The calibrated rope
    tension is 0.2376 J/m against a registered single-strand tension
    of 1.70e3 J/m -- a ratio of 1.4e-4, i.e. AT THE PUBLISHED SCALE
    THE ELECTRON IS A ROPE MADE OF LESS THAN ONE STRAND, which one
    medium forbids outright.

(3) IMPOSING THE MINIMAL CASE (exactly one strand) selects
    s = 7.155e3, and at that scale:
      rms charge radius 2.96e-3 fm -- the scattering bound is missed
      by 3.0x, not 21158x: a 7.2e3-fold improvement from a constraint
      that was never tuned to it;
      rope thickness 1.87e-19 m against a nuclear-density strand
      spacing of 2.87e-16 m (a COMPARISON value under the nuclear-density
      hypothesis, per ELEC-049 not the medium's registered spacing; the
      adjudicated w is 5.78e-17 m), so the rope is comfortably thinner than
      the spacing -- geometrically coherent for a single strand;
      the hbar shortfall degrades to 2.66e6, and the ELEC-037
      invariant is conserved to 5.9e-4 as it must be.

WHAT THIS REFRAMES: two independent one-medium conditions -- the
scattering bound and tension-matching -- now agree to within a factor
of three, while the hbar normalization W = 1.80 T D^2/c is the lone
outlier at 2.7e6. The campaign has been treating the object's size as
the problem; on this reading the problem is the hbar relation.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'ELEC040_state.npz')
    a = np.load(ROOT/'analysis'/'ELEC040_audit.npz')
    # (1) the tautology
    assert abs(float(s['F2a']) - float(s['F2b'])) < 1, "branches A and B are the same number"
    assert abs(float(s['F2a'])/float(s['F1']) - 1) < 0.05, "and equal to F1 up to recalibration"
    assert abs(float(s['pref']) - 1) < 0.05, "F3 = F1 x 0.986: proportional by construction"
    # (2) the new constraint and the contradiction it exposes
    assert float(s['ratio']) < 1e-3, "the rope carries 1.4e-4 of a single strand: forbidden"
    # (3) the scale it selects
    assert 5e3 < float(a['s_one']) < 1e4, "tension matching selects s = 7.16e3"
    assert float(a['size']) < 5, "at which the scattering bound is missed by only 3.0x"
    assert float(a['size']) > 1, "still missed, not met"
    assert float(a['hbar']) > 1e6, "while the hbar shortfall degrades to 2.7e6"
    assert abs(float(a['prod'])/float(a['INV']) - 1) < 1e-2, "ELEC-037's invariant conserved"
    assert float(a['ratio_dw']) < 1e-2, "rope thinner than the strand spacing: coherent"
    print(f"F1={float(s['F1']):.3e}, branchA={float(s['F2a']):.3e}, F3/F1={float(s['pref']):.3f}; "
          f"T_rope/T_strand={float(s['ratio']):.2e}; s_one={float(a['s_one']):.3e} -> size miss "
          f"{float(a['size']):.2f}x, hbar {float(a['hbar']):.2e}")
    print("PASS: the recurring 2e4 is a tautology; tension-matching is a new forced constraint")
    print("      that brings the scattering bound to 3x -- the hbar relation is now the outlier.")


if __name__ == "__main__":
    test()
