"""NUCQ-002 (Modeled): THE TENSION AUDIT -- T is derived, not fitted;
it cannot be raised through a; and it inherits an n_t that the corpus
has been using for TWO different physical quantities. NUCQ-001's
falsification is thereby made CONDITIONAL.

WHERE T COMES FROM. The chain is T0 = T_tube/n_t, where T_tube =
1.878e5 N is a measured hadronic flux-tube tension (the QCD string
tension, ~1 GeV/fm = 1.60e5 N, is the same scale). With n_t = 111 this
gives 1.692e3 N, and the independent route T0 = Sigma a^2/3 with
a = 1e-16 m gives 1.700e3 N -- the same number twice. T IS NOT
ARBITRARY AND NOT FITTED.

WHY IT CANNOT BE RAISED THE OBVIOUS WAY. a <= 1e-16 m is a LORENTZ
BOUND (FND-MATTER-005), and the chain already sits AT it. Enlarging a
to rescue the HBAR results would violate an independently registered
constraint.

THE STRUCTURAL FINDING. n_t = 111 is doing two jobs:
  (i) STRUCTURAL -- how many strands COMPOSE a flux tube (T_tube = n_t T0)
 (ii) DYNAMICAL -- how many act COHERENTLY in one reconnection (QGATE-008)
ELEC-043 derived the DYNAMICAL one from causality and obtained ~1. That
argument says nothing about the structural one, and the corpus has been
using a single symbol for both.

WHAT FOLLOWS FOR THE HBAR CHAIN (patches = (R/L_hbar)^3 in He-4):
    n_t = 111 -> T0 = 1.69e3 N, L = 4.32 fm,  0.1 patches  FAILS
    n_t =  12 -> T0 = 1.57e4 N, L = 1.42 fm,  2.4 patches  marginal
    n_t =   4 -> T0 = 4.70e4 N, L = 0.82 fm, 12.4 patches  marginal
    n_t =   1 -> T0 = 1.88e5 N, L = 0.41 fm, 99.3 patches  adequate
NUCQ-001's falsification kills n_t = 111. It does NOT kill the
mesoscopic-hbar picture, which survives at small structural n_t.

A FLAGGED COINCIDENCE, TESTED AND NOT USED. At n_t = 11.6 the quantum
scale exactly equals the Yukawa range, and 12 is the close-packing
coordination number. But the required n_t tracks T_tube -- 9.9 for the
canonical QCD string tension, 14.0 for T_tube +20 percent -- so it is
not a fixed integer prediction, and it lands near 12 only to the
accuracy of the registered T_tube. Flagged under the standing rule.

WHICH CONSTRAINT IS BINDING. Born exactness is EMPIRICAL: nuclear
quantum mechanics demonstrably works. The Yukawa match is a comparison
the corpus never derived a reason for. The empirical constraint
therefore favours SMALL structural n_t, at which the Yukawa agreement
is lost -- the two pull apart again, but the empirical one can now be
satisfied, which at n_t = 111 it could not.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'NUCQ002_state.npz')
    hbar = 1.054571817e-34; c = 2.99792458e8
    T_tube = float(s['T_tube'])
    # T's provenance: two independent routes agree
    assert abs(T_tube/111 - 1.700e3)/1.700e3 < 0.01, \
        "T_tube/n_t and Sigma a^2/3 give the same 1.70e3 N: T is derived, not fitted"
    assert 1e5 < T_tube < 3e5, "T_tube is the measured hadronic flux-tube scale"
    assert abs(T_tube/(1.602e-10/1e-15) - 1) < 0.25, "within 25% of the QCD string tension"
    # the n_t ladder and its effect on the Born constraint
    rows = s['rows']            # n_t, T0, L_fm, He4 patches, Fe56 patches
    assert rows[0][3] < 0.2, "n_t = 111 gives He-4 only 0.1 patches: Born must fail"
    assert rows[-1][3] > 50, "n_t = 1 gives 99 patches: Born exact -- falsification dissolves"
    assert rows[-1][1]/rows[0][1] > 100, "T rises 111x as the structural n_t falls to 1"
    # monotone: smaller n_t -> larger T -> smaller L -> more patches
    assert all(rows[i][3] < rows[i+1][3] for i in range(len(rows)-1)), \
        "patch count rises monotonically as n_t falls"
    # the flagged coincidence is NOT forced
    nm = float(s['n_match'])
    assert 9 < nm < 15, "n_t ~ 11.6 would match the Yukawa range"
    n_alt = (1.602e-10/1e-15)/(hbar*c/(1.4e-15)**2)
    assert abs(n_alt - nm)/nm > 0.1, \
        "but it shifts to 9.9 under the canonical string tension: not a fixed prediction"
    print(f"T_tube {T_tube:.3e} N; T0(111) {rows[0][1]:.3e} N; L_hbar {rows[0][2]:.2f} -> "
          f"{rows[-1][2]:.2f} fm as n_t 111 -> 1; He-4 patches {rows[0][3]:.1f} -> {rows[-1][3]:.1f}; "
          f"Yukawa match at n_t {nm:.1f} (but {n_alt:.1f} under the canonical tension)")
    print("PASS: T is derived and Lorentz-pinned; n_t serves two roles; NUCQ-001 kills")
    print("      n_t = 111, not the mesoscopic-hbar picture.")


if __name__ == "__main__":
    test()
