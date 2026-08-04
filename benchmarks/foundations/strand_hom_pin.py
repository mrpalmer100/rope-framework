"""FND-STRAND-029 (Modeled): THE HONG-OU-MANDEL PIN -- the boundary bounded
from both sides in closed form. Classical wave interference into the
framework's own linear-response detectors caps the dip visibility at
V = X^2/(2 S^2) <= 1/2 (attained only at matched amplitudes); per-quantum
Grant-3 delivery gives NO dip at all (V = 0, coincidence 1/2, identical
to distinguishable photons); quantum mechanics gives V = 1 and experiment
routinely exceeds 0.9. The escape's shape is exact and NOT adopted: a
joint-delivery rule for indistinguishable quanta (the two-quantum analog
of Grant 3), which must give V = 1 at perfect indistinguishability,
track the measured dip's narrowing with delay, and leave 025-028's
single-quantum consequences untouched.

Derivation and the surveyed-edge ledger: analysis/STRAND029_hom_pin.md.
"""
import numpy as np

rng = np.random.default_rng(2032)
M = 400000


def classical_visibility(E1, E2):
    th = rng.uniform(0, 2*np.pi, M)
    S = (E1**2 + E2**2)/2; X = E1*E2
    Ic = S + X*np.cos(th); Id = S - X*np.cos(th)
    C = np.mean(Ic*Id); C0 = S**2
    return (C0 - C)/C0


def test():
    # classical cap: V = X^2/(2 S^2), maximal 1/2 at E1 = E2, degraded by imbalance
    for E1, E2 in [(1.0, 1.0), (1.0, 0.6), (1.0, 0.25)]:
        S = (E1**2 + E2**2)/2; X = E1*E2
        V_th = X**2/(2*S**2)
        V_mc = classical_visibility(E1, E2)
        assert abs(V_mc - V_th) < 0.01, (E1, E2, V_mc, V_th)
        assert V_th <= 0.5 + 1e-12
    assert abs(classical_visibility(1.0, 1.0) - 0.5) < 0.01, "cap attained at balance"
    # granular route: independent per-quantum delivery -> coincidence 1/2, V = 0
    a = rng.random(M) < 0.5
    b = rng.random(M) < 0.5
    coinc = np.mean(a != b)  # opposite ports
    assert abs(coinc - 0.5) < 0.005, "no dip under per-quantum Grant 3"
    # the pin table
    print("classical wave route: V = X^2/(2S^2); MC matches closed form at 3 ratios;")
    print(f"  cap 0.500 attained at matched amplitudes (measured {classical_visibility(1.0,1.0):.3f})")
    print(f"granular route: coincidence = {coinc:.3f} (= 1/2), V = 0 -- no dip")
    print("QM: V = 1; experiment: V > 0.9 -- THE PIN: a derived factor-of-two-at-")
    print("best shortfall, the g2 pin's sibling, with the escape's shape specified")
    print("(joint delivery for indistinguishable quanta) and NOT adopted.")
    print("PASS: the boundary is bounded from both sides in closed form.")


if __name__ == "__main__":
    test()
