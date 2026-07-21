"""Lattice Lorentz violation bounds the rope spacing a to sub-nuclear scales.

The rope defect core is regularized by a discrete lattice (FND-REL-003). A
lattice breaks Lorentz invariance at short distance: the standard discrete-chain
dispersion is omega^2 = c^2 k^2 [1 - (k a)^2/12 + ...], so the fractional
deviation of the signal speed from c is ~ (k a)^2 / 24. Experiments that bound
Lorentz violation therefore bound the absolute lattice spacing a.

The rope theory leaves a FREE (rope_parameter_count: the primitives {T, kappa, a}
form one dimensionless group Pi = kappa a / T; a is a dimensionful scale, not
fixed by the theory). So the model is NOT committed to a being atomic; the bound
below is what experiment requires of a.

This benchmark checks:
  (1) the terrestrial optical-cavity bound forces a well below the atomic scale
      (so 'ropes between atoms' cannot be the fundamental spacing);
  (2) the allowed a is still enormously above the Planck scale (so there is a
      consistent, non-empty window -- the tension is not fatal).

SCOPE / honesty: this shows the lattice Lorentz-violation problem is SURVIVABLE
(a consistent sub-nuclear window exists), at the cost of decoupling rope
discreteness from the atomic scale. It is a falsifiable EFT constraint, not a
derivation of a's value. Tightening Lorentz bounds directly squeezes a.
"""
import numpy as np

C = 2.998e8
HBAR = 1.055e-34
ATOMIC = 1e-10
NUCLEAR = 1e-15
PLANCK = 1.616e-35


def a_max_from_bound(k, delta):
    """(k a)^2 / 24 < delta  =>  a < sqrt(24 delta)/k."""
    return np.sqrt(24 * delta) / k


def test():
    # (1) terrestrial optical cavity: k at ~500 nm, fractional anisotropy < 1e-18
    k_opt = 2 * np.pi / 5e-7
    a_opt = a_max_from_bound(k_opt, 1e-18)
    assert a_opt < ATOMIC / 1e5, "optical bound should force a far below atomic"
    assert a_opt > PLANCK * 1e10, "allowed a should remain far above Planck"

    # (2) high-energy astrophysical photon (~10 GeV), quadratic-LV fractional ~1e-16
    k_grb = (1e10 * 1.602e-19) / (HBAR * C)
    a_grb = a_max_from_bound(k_grb, 1e-16)
    assert a_grb < NUCLEAR, "astro bound should push a sub-nuclear"

    print(f"terrestrial optical bound: a < {a_opt:.2e} m  (atomic is {ATOMIC:.0e} m)")
    print(f"  -> lattice spacing cannot be atomic, by ~{ATOMIC/a_opt:.0e}x")
    print(f"astrophysical bound:       a < {a_grb:.2e} m  (sub-nuclear)")
    print(f"consistent window: {PLANCK:.0e} m (Planck)  <<  a  <<  {a_opt:.0e} m")
    print("PASS: lattice Lorentz violation is SURVIVABLE (non-empty sub-nuclear window)")
    print("      but REFUTES the 'ropes between atoms' fundamental scale; atoms are")
    print("      coarse defects in a >1e6x finer rope mesh. Falsifiable via LV bounds.")


if __name__ == "__main__":
    test()
