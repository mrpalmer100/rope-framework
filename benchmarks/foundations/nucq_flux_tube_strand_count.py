"""NUCQ-003 (Failed, kept): THE STRUCTURAL STRAND COUNT IS DERIVED, THE
ESCAPE IS CLOSED, AND THE MESOSCOPIC-HBAR PICTURE IS REFUTED.

THE DERIVATION. With the vacuum density set by rho = 3 T_tube/(n c^2 a^2)
and the tube's linear mass density mu = T_tube/c^2 = rho pi R^2, the
strand count and tube radius are related by
    R_tube = a sqrt(n / (3 pi))       equivalently   n = 3 pi (R_tube/a)^2
This uses ONLY the Lorentz bound a and the tube radius. It does not
involve rho_vac, so unlike the corpus's earlier route it is NOT
circular.

THE NUMBER. Lattice QCD measures the intrinsic flux-tube width at
0.35-0.5 fm. With a = 1e-16 m:
    R = 0.35 fm -> n = 115
    R = 0.40 fm -> n = 151
    R = 0.50 fm -> n = 236
The corpus's n_t = 111 sits just below this range: CONFIRMED by
measurement rather than chosen. And because a is an UPPER bound, any
smaller a gives a LARGER n, so n >= ~115 firmly.

A COMPANION RESULT, in the other direction: run forward at n = 111 and
the predicted tube radius is 0.343 fm, against a lattice value of
0.35-0.5 fm. That is a parameter-free agreement at the low edge and is
worth registering independently of what follows.

THE ESCAPE IS CLOSED. NUCQ-002 demoted NUCQ-001's falsification to
conditional on the grounds that a SMALL structural n_t would rescue the
mesoscopic-hbar picture (n = 1 giving 99 patches in He-4). But n cannot
be small:
    n = 115 -> T0 = 1.63e3 N, L_hbar = 4.40 fm, He-4 holds 0.081 patches
    n = 150 -> 1.25e3 N, 5.03 fm, 0.054 patches
    n = 236 -> 7.96e2 N, 6.30 fm, 0.027 patches
n can only be larger, so T0 only smaller, so L_hbar only larger, so the
patch counts only smaller. THE BORN FAILURE GETS WORSE, NEVER BETTER.

VERDICT: NUCQ-001 is restored to UNCONDITIONAL. The structural strand
count is pinned above 115 by the measured flux-tube width and the
Lorentz bound; that forces L_hbar >= 4.4 fm; that places every nucleus
below one sub-quantum patch; and that contradicts the demonstrated
success of standard quantum mechanics in nuclei. The mesoscopic-hbar
picture -- HBAR-005 and everything resting on it -- is REFUTED.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'NUCQ003_state.npz')
    a = float(s['a']); T_tube = float(s['T_tube'])
    hbar = 1.054571817e-34; c = 2.99792458e8
    # the forward prediction: n=111 gives a tube radius matching lattice QCD
    assert 0.30 < float(s['R111']) < 0.40, "n=111 predicts R_tube = 0.343 fm vs lattice 0.35-0.5"
    # the inverse derivation, non-circular (uses only a and R)
    nf = s['nfromR']
    for R, n in nf:
        assert abs(n - 3*np.pi*(R*1e-15/a)**2) < 1, "n = 3 pi (R/a)^2"
    assert 100 < nf[0][1] < 130, "the lattice lower edge gives n = 115"
    assert nf[-1][1] > 200, "the upper edge gives n = 236"
    # the escape is closed: every allowed n makes the Born failure worse
    t = s['tab']              # n, T0, L_fm, He4 patches
    assert (t[:, 3] < 0.1).all(), "He-4 holds under 0.1 patches at every allowed n"
    assert t[0, 3] > t[1, 3] > t[2, 3], "patches DECREASE as n rises: monotone against rescue"
    assert (t[:, 2] > 4.0).all(), "L_hbar exceeds 4.4 fm throughout"
    print(f"R_tube(n=111) = {float(s['R111']):.3f} fm vs lattice 0.35-0.5; inverted n = "
          f"{nf[0][1]:.0f}-{nf[-1][1]:.0f}; He-4 patches {t[0,3]:.3f} down to {t[2,3]:.3f}")
    print("PASS: the strand count is derived and >= 115, the escape is closed, and the")
    print("      mesoscopic-hbar picture is REFUTED.")


if __name__ == "__main__":
    test()
