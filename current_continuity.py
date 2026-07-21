"""Star-convergence geometry: the atomic pattern radius scales as R ~ a*sqrt(N).

Gaede's atom picture shows ~N ropes (microstructure width ~a) converging on a
core. They cannot all reach a point; by a packing argument they fill a sphere of
radius R when N ~ 4 pi (R/a)^2, i.e.

    R ~ a * sqrt(N / 4pi).

This is a genuine, non-circular STRUCTURAL result from the convergence geometry
(no hbar, no inserted Bohr radius): the pattern radius grows as the square root
of the rope count. It is CONSISTENT with the Bohr scale (5.3e-11 m) for
N ~ 1e12 ropes at a ~ 1e-16 m.

SCOPE / honest limits (this is NOT a derivation of the Bohr radius):
  * Two free inputs (N and a) versus one target, so hitting a0 is a consistency
    window, not a prediction. Nothing here fixes N or a independently.
  * Attempts to fix N by numerology (e.g. N=(1/alpha)^6) are explicitly REJECTED
    as tuning: there is no principled reason for the exponent, so the near-hit is
    treated as coincidence, not evidence.
  * A real derivation requires fixing N from independent physics (the picture
    suggests N ~ charge/flux count, since the converging ropes are the source's
    flux lines) -- an open problem (FND-MATTER-001).
"""
import numpy as np


def radius(N, a=1e-16):
    return a * np.sqrt(N / (4 * np.pi))


def test():
    # (1) the scaling law: R ~ a sqrt(N) -> R^2 linear in N
    Ns = np.array([1e6, 1e8, 1e10, 1e12])
    Rs = radius(Ns)
    # R^2 / N should be constant (the packing law)
    ratios = Rs**2 / Ns
    assert np.allclose(ratios, ratios[0], rtol=1e-9), "R ~ a sqrt(N) law should hold exactly"

    # (2) consistency window: Bohr scale reached for N ~ 1e12 at a ~ 1e-16 m
    R_bohr_like = radius(1e12, a=1e-16)
    assert 1e-11 < R_bohr_like < 1e-10, "should land near the Bohr scale for N~1e12"

    print(f"R ~ a*sqrt(N/4pi): structural packing law verified (R^2 linear in N)")
    print(f"N=1e12, a=1e-16 m -> R = {R_bohr_like:.2e} m (Bohr a0 = 5.3e-11 m): consistent")
    print("HONEST: consistency window (N,a free vs one target), NOT a derivation of a0.")
    print("        Fixing N from independent physics (charge/flux count) is the open step.")


if __name__ == "__main__":
    test()
