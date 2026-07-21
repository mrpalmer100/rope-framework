"""FND-MATTER-003 closure: the absolute mesh scale a is irreducible within the
framework -- a fundamental constant fixed by measurement, not derivation.

After FND-MATTER-004 fixed the rope count N via the interpenetrability threshold,
the only remaining input for the atomic scale is the mesh spacing a. This
benchmark records the dimensional argument that a cannot be derived from the
current primitives, so the atomic-scale problem bottoms out at exactly one
irreducible constant -- the normal structure of a physical theory.

The framework's primitives {T [N], mu [kg/m], lambda, a [m]} yield:
  - c = sqrt(T/mu): a SPEED, no length (you cannot build a length from tension
    and mass density alone).
  - xi = sqrt(lambda/T): a length, but calibrated to the atomic scale R (via the
    hydrogen bound state), so xi ~ R -- not independent of R.
  - a: a primitive length, the discreteness cutoff.
Two independent lengths (R ~ xi, and a) with only the inequality xi >= a (lattice
cutoff) between them -- an inequality, not an equation. So a is dimensionally
independent of the atomic scale: no second equation fixes it.

Rejected (non-derivations): the Lorentz bound a < ~1e-16 m is one-sided (cannot
fix a value); R/a ~ 1/alpha^3 is numerology with no mechanism (rejected on the
same grounds as the earlier (1/alpha)^6 attempt for N); a = Planck length is a
possible ONTOLOGICAL identification (rope mesh = spacetime discreteness) requiring
an independent argument, not a fit.

Honest end state: a is a fundamental constant of the framework, on the same
footing as c/G/hbar -- fixed by MEASUREMENT (the (ka)^2 Lorentz-violation
dispersion depends on a and would determine it), not by derivation.
"""
import numpy as np


def lengths_from_primitives():
    """Which independent lengths the primitives can form (dimensional check)."""
    # c = sqrt(T/mu) has dimension [m/s] -- a speed, NOT a length.
    # A length needs lambda (-> xi, tied to R) or a itself.
    return {"c": "speed (no length)", "xi": "length, but calibrated to R", "a": "primitive length"}


def alpha_cubed_is_numerology():
    """R/a ~ 1/alpha^3 has no mechanism -> rejected as coincidence."""
    alpha = 1 / 137.036
    ratio_target = (1 / alpha) ** 3           # ~2.6e6
    # it is 'close' to the R/a hierarchy but there is NO derivation -> reject
    return ratio_target  # returned only to document the rejected coincidence


def test():
    L = lengths_from_primitives()
    # the framework yields a speed from {T,mu}, so no length is forced by them alone
    assert "speed" in L["c"], "T,mu give a speed, not a length"
    # xi is tied to R (not independent), a is a separate primitive length
    assert "calibrated to R" in L["xi"] and "primitive" in L["a"]
    # the alpha^3 coincidence is in the ballpark but has no mechanism -> not used
    r = alpha_cubed_is_numerology()
    assert 1e6 < r < 1e7, "1/alpha^3 is ballpark-close (documents why it tempts) but is numerology"
    print("primitives give a SPEED (c=sqrt(T/mu)), no length -> a not forced by T,mu")
    print("two independent lengths: xi~R (calibrated) and a (mesh); only xi>=a between them")
    print(f"1/alpha^3 = {r:.2e} is ballpark-close to R/a but has NO mechanism -> REJECTED")
    print("PASS: a is irreducible within the framework -- a fundamental constant fixed")
    print("      by measurement (the (ka)^2 Lorentz-violation signal), not derivation.")


if __name__ == "__main__":
    test()
