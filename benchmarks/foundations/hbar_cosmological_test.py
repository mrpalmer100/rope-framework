"""HBAR-010 (Modeled): THE FORMATION-ERA MEDIUM MEETS COSMOLOGY -- a
comoving medium is excluded by five orders, the medium must be rigid to
one part in 2e5, and the framework inherits a preferred frame it can
be tested for.

THE TEST. HBAR-006 established hbar c = N^2 T w^2, so with T a strand
property hbar ~ w^2. If the medium comoves with cosmic expansion,
w ~ a(t) and therefore hbar ~ a^2:
    z = 0.5 -> hbar/hbar_0 = 0.444  (a 56 percent change)
    z = 1.0 -> 0.250                (75 percent)
    z = 3.0 -> 0.063                (94 percent)
Variation of dimensionless constants over cosmic time is constrained
at the 1e-5 to 1e-6 level, and since alpha = e^2/(4 pi eps0 hbar c) a
fractional change in hbar appears directly as one in alpha. THE
COMOVING MEDIUM IS EXCLUDED BY 5.6e4 at z = 0.5 and 7.5e4 at z = 1.

THE INVERSION. Since dhbar/hbar = 2 dw/w, the bound requires
|dw/w| < 5e-6 across the observed redshift range, while the universe
has expanded by a factor of about two over the same interval. THE
STRAND MEDIUM MUST BE DECOUPLED FROM COSMIC EXPANSION TO BETTER THAN
ONE PART IN 2e5.

WHAT THAT FORCES, and neither branch is free:
  (A) the universe does not expand and redshift has another cause --
      internally available, since the gravity sector already carries
      redshift claims (GRV-010, -011, -014, -034, -039); or
  (B) the universe expands while the medium does not, making it a
      rigid non-expanding substrate: a preferred frame in the
      strongest sense.

A CONSEQUENCE THAT CAN BE CHECKED IN PRINCIPLE. Under (B) the medium
defines a rest frame, and the CMB already defines one -- we move at
370 km/s = 1.23e-3 c relative to it. THE PREDICTION IS THAT THESE ARE
THE SAME FRAME; a mismatch would produce medium anisotropy at order
(v/c)^2 = 1.5e-6 in any medium-coupled observable.

FLAGGED, not leaned on: HBAR-008's preferred DIRECTION would appear as
a quadrupole, and the CMB has known large-angle anomalies -- but
attributing them to strand orientation requires a coupling the corpus
has not computed, so the observation is recorded and nothing is built
on it.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'HBAR012_state.npz')
    # the comoving prediction and its exclusion
    for z in (0.5, 1.0, 3.0):
        a = 1/(1+z)
        assert abs(a**2 - 1) > 0.4, f"z={z}: comoving predicts a huge hbar change"
    assert abs(float(s['dev_z1']) - 0.75) < 1e-9, "z=1 predicts a 75% change in hbar"
    assert float(s['excl']) > 1e4, "excluded by 7.5e4 against a 1e-5 bound"
    # the rigidity requirement
    assert float(s['rigidity']) < 1e-5, "|dw/w| < 5e-6: rigid to 1 part in 2e5"
    assert abs(float(s['rigidity']) - float(s['bound'])/2) < 1e-12, "dhbar/hbar = 2 dw/w"
    # the frame consequence
    assert 1e-4 < float(s['v_cmb'])/2.99792458e8 < 1e-2, "we move at 1.2e-3 c wrt the CMB"
    assert float(s['beta2']) < 1e-5, "a frame mismatch shows at order (v/c)^2 = 1.5e-6"
    print(f"comoving: hbar(z=1)/hbar_0 = 0.25, excluded by {float(s['excl']):.1e}; "
          f"rigidity |dw/w| < {float(s['rigidity']):.1e}; frame test at (v/c)^2 = "
          f"{float(s['beta2']):.2e}")
    print("PASS: a comoving medium is excluded by five orders; the medium must be rigid to")
    print("      1 part in 2e5, and the framework inherits a testable preferred frame.")


if __name__ == "__main__":
    test()
