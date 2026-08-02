"""ELEC-039 (Modeled): THE COUNTING MATTERS BY FOUR ORDERS, AND NO
COUNTING ESCAPES. ELEC-038's price was computed under the most
conservative hypothesis; the most defensible one is ~1900x cheaper,
and even the most generous conceivable one does not reach ordinary
densities.

THE QUESTION: ELEC-038 priced the one-medium declaration assuming
n_t counts strands across the ROPE TUBE's cross-section,
n_t = (d_c/w)^2. If coherent reconnection recruits strands along the
rope's length, or across the whole object's extent rather than the
tube's, the exponent and the price both change.

THE GEOMETRY, from the certified state: d_c = 1.338 fm,
R (rms charge radius) = 21.16 fm, L (total curve length) = 162.6 fm,
so L/d_c = 121.5 and R/d_c = 15.8 -- the object offers two large
ratios the counting could exploit.

THE PRICES (n_t = area/w^2 with n_t = 8.73e8 required):
  H1 tube cross-section   (d_c^2): w = 4.5e-20 m, 4.01e7 x nuclear
  H2 tube length-recruited (d_c L): w = 5.0e-19 m, 3.30e5 x nuclear
  H3 object cross-section    (R^2): w = 7.2e-19 m, 1.60e5 x nuclear
  H4 object length-recruited  (R L): w = 2.0e-18 m, 2.09e4 x nuclear
  H5 object sheet            (L^2): w = 5.5e-18 m, 2.72e3 x nuclear
Every hypothesis keeps w between 2.8e15 and 3.4e17 Planck lengths, so
none is excluded on that ground.

THE VERDICT: the counting choice is worth 1.5e4 -- four orders -- so
ELEC-038's headline of ~1.9e8 x nuclear is the WORST CASE, not the
expected one. But no counting reaches ordinary matter: the most
generous conceivable hypothesis (recruitment across an area L^2, far
larger than the object itself and hard to justify) still demands
2.7e3 x nuclear, and the most defensible (H4) demands 2.1e4.
Inverted: a nuclear-density vacuum supplies only 4.2e4 strands under
H4 against the 8.7e8 required, short by 2.1e4 -- the same order as
the form-factor failure it was meant to relieve.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'ELEC039_state.npz')
    x = s['xnuc']
    assert len(x) == 5, "five counting hypotheses"
    assert x[0] > 1e7, "H1 (tube cross-section) is the expensive one ELEC-038 assumed"
    assert x[-1] < 1e4, "H5 (object sheet) is the cheapest"
    assert float(s['spread']) > 1e3, "the counting choice is worth four orders"
    # but none escapes
    assert float(s['best']) > 1e3, "NO counting reaches below 1e3 x nuclear"
    assert x[3] > 1e4, "the most defensible (H4) still demands 2.1e4 x nuclear"
    # all permitted on Planck grounds
    assert s['wp'].min() > 1e10, "every hypothesis keeps w far above the Planck length"
    # the inverted statement
    assert float(s['short']) > 1e4, "a nuclear vacuum is short by 2.1e4 strands under H4"
    print(f"prices x nuclear: " + ", ".join(f"{v:.1e}" for v in x) +
          f"; spread {float(s['spread']):.1e}; best {float(s['best']):.2e}; "
          f"nuclear-vacuum shortfall {float(s['short']):.1e}")
    print("PASS: counting is worth four orders -- ELEC-038's figure was the worst case -- but")
    print("      no counting escapes; the most defensible still demands 2e4 x nuclear.")


if __name__ == "__main__":
    test()
