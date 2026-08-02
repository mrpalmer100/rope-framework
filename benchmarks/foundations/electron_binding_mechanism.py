"""ELEC-042 (Modeled): WHAT BINDS THE PAIR -- the functional supplies
three mechanisms, the medium supplies two of them, and the missing one
is the hbar outlier wearing different clothes.

PART 1 -- THE FORCE BUDGET, in newtons. The strand tension is
T = 1.70e3 N (J/m is a force). The clasp rides at radius
r = 1.877e-19 m, twice the hard core, so its inward line force is
T/r = 9.06e21 N/m, integrating to 1.07e4 N around its circumference --
that is the force with which the clasp squeezes its partner, and what
the hard core (the KKT multiplier) must supply outward. Independently,
the field holds the loop open with E_F/R = 1.43e4 N against tension's
E_T/R = 1.34e4 N: the virial balance of ELEC-010, now expressed as
opposing forces agreeing to 6 percent.

PART 2 -- IS THE LINK ACTION-PROTECTED? The framework's own
reconnection action, evaluated for ONE strand pair at the electron's
own scale, is W_1 = 1.80 T d_c^2/c = 3.57e-43 J s, which is
3.4e-9 of hbar. A reconnection event therefore costs a billionth of
the quantum of action: the link carries NO barrier of quantum size,
and nothing in the medium prevents the two strands from reconnecting
and unlinking.

PART 3 -- THE IDENTIFICATION. Making one reconnection cost hbar would
require n_t = 2.95e8 strands acting collectively. That is ELEC-037's
obstruction arrived at from a completely different direction --
STABILITY rather than calibration -- and to the same order. The
functional binds the pair with tension, field, and contact, all three
of which are strand properties the medium supplies; the fourth
ingredient, topological protection, is IMPOSED by the certifier and is
NOT derived. The medium does not supply it, because reconnection is
action-cheap. The hbar outlier and the binding question are one
problem.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'ELEC042_state.npz')
    # Part 1: the virial balance as opposing forces
    Ff, Ft = float(s['F_field']), float(s['F_tens'])
    assert abs(Ff - Ft)/Ff < 0.15, "field and tension forces balance to ~6%"
    assert 1e3 < Ff < 1e5, "both are ~1e4 N at this scale"
    assert float(s['F_tot']) > 1e3, "the clasp's contact force is of the same order"
    assert abs(float(s['r_clasp'])/float(s['d_c']) - 1.0) < 0.1, "the clasp rides the core"
    # Part 2: the link is not action-protected
    assert float(s['W1_hbar']) < 1e-6, "one reconnection costs 3.4e-9 hbar: no barrier"
    # Part 3: the identification with ELEC-037's obstruction
    n = float(s['n_needed'])
    assert 1e8 < n < 1e9, "n_t ~ 2.95e8 needed for a quantum-sized barrier"
    assert abs(np.log10(n) - np.log10(8.731e8)) < 0.6, \
        "same order as ELEC-037's 8.7e8, reached from stability not calibration"
    print(f"forces: field {Ff:.2e} N vs tension {Ft:.2e} N (balance {abs(Ff-Ft)/Ff*100:.0f}%); "
          f"clasp contact {float(s['F_tot']):.2e} N; W_1/hbar {float(s['W1_hbar']):.2e}; "
          f"n_t for a quantum barrier {n:.2e}")
    print("PASS: three binding mechanisms supplied by the medium, the fourth (topological")
    print("      protection) is imposed not derived -- and its price is the hbar obstruction.")


if __name__ == "__main__":
    test()
