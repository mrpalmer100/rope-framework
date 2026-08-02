"""ELEC-037 (Modeled): A SCALE-INVARIANT NO-GO -- the form-factor
failure and the cross-sector clash pull in OPPOSITE directions, their
product is invariant, and the two-objects declaration is thereby forced
into a decision with a computable price.

THE TEST: rescale the length unit (object smaller by s) with the mass
anchor held, and watch both failures.

(1) OPPOSITE EXPONENTS, verified numerically: the size failure scales
    as s^-1.000 (a smaller object fits the scattering bound better)
    while the hbar shortfall scales as s^+1.000 (a smaller object makes
    W = n_t C T d^2/c smaller and the clash worse). The reason is
    analytic: rms ~ L0, while T0 ~ 1/L0 and d_c ~ L0 give W ~ L0.

(2) THE INVARIANT: their product is 7.8662e6 at s = 1, 10, 1e3 and
    1e5 -- constant to 4.4e-16, i.e. to machine precision. NO CHOICE
    OF LENGTH UNIT CAN SATISFY BOTH CONSTRAINTS.

(3) THE BEST BALANCE: equalizing the two failures at s = 7.544 leaves
    both at 2.80e3 -- so the most favourable rescaling available still
    misses each constraint by nearly three thousandfold.

(4) WHAT COULD CLOSE IT: the invariant reduces to rms_model /
    (n_t d_model^2 E0u), so L0 cancels and only two levers remain.
    Geometry (d^2/rms) is bounded because the tube cannot exceed the
    object, giving at most 263x of the 7.87e6 required. That leaves
    the collective number: closing the invariant demands
    n_t ~ 8.7e8 strands acting collectively, against the 111 the scale
    branch adopted -- a concrete, falsifiable prediction rather than a
    hope.

(5) THE DECLARATION, forced: if vacuum strands and matter ropes are
    DIFFERENT objects, the hbar normalization never constrained this
    rope, the 372x clash dissolves, and the framework faces the
    form-factor problem alone (2.1e4). If they are ONE object, the
    invariant stands and no length unit works. The corpus must choose,
    and the choice is now priced.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'ELEC037_state.npz')
    a = np.load(ROOT/'analysis'/'ELEC037_audit.npz')
    # (1) opposite exponents
    assert abs(float(s['a_size']) + 1) < 0.01, "size failure ~ s^-1"
    assert abs(float(s['a_hbar']) - 1) < 0.01, "hbar shortfall ~ s^+1"
    # (2) the invariant
    P = s['P']
    assert P.max()/P.min() - 1 < 1e-12, "product invariant to machine precision"
    assert 5e6 < float(s['inv']) < 1e7, "invariant = 7.87e6"
    # (3) the best balance
    assert 2e3 < float(s['best']) < 4e3, "best simultaneous failure ~2.8e3 on both"
    # (4) the levers
    assert float(a['n_req']) > 1e8, "closing it needs n_t ~ 8.7e8 collective strands"
    assert float(a['geo_max_gain']) < 1e3, "geometry can buy at most ~263x"
    assert float(a['geo_short']) > 1e4, "geometry alone falls short by >1e4"
    print(f"exponents {float(s['a_size']):+.3f} / {float(s['a_hbar']):+.3f}; invariant "
          f"{float(s['inv']):.4e} (spread {P.max()/P.min()-1:.1e}); best balance "
          f"{float(s['best']):.2e}; n_t required {float(a['n_req']):.2e}")
    print("PASS: a scale-invariant no-go -- no length unit satisfies both constraints, the")
    print("      two-objects declaration is forced, and its alternative is priced at n_t ~ 1e9.")


if __name__ == "__main__":
    test()
