"""Cosmological alpha-variation test of the rope-density hypothesis for the EM
coupling (Picture A). Result: the strong (local/matter-tracking) form is
FALSIFIED by observation; the surviving form is observationally empty.

Background. This session's analysis raised the hypothesis that the EM coupling
is set by rope density (Picture A), with the sharpened relation (from the
kinetic-term reconciliation): the impedance of free space, hence the
fine-structure constant, scales as alpha ~ Z0 ~ 1/L_v, where L_v is the rope
length per unit volume. The speed of light c is protected (mu0 and eps0 scale
oppositely so mu0*eps0 = 1/c^2 is density-independent), so the observable
signature of Picture A is alpha-variation across cosmic time, NOT c-variation.

Test. Observed bound (Keck HIRES Many-Multiplet, Songaila & Cowie; consistent
with VLT/ESPRESSO ~1 ppm): |Delta(alpha)/alpha| < ~2.4e-6 over z ~ 0.7-1.5.

  - LOCAL / matter-tracking scaling: if the relevant L_v is the density of
    ropes among matter atoms, L_v ~ (1+z)^3, so alpha ~ (1+z)^-3 and
    Delta(alpha)/alpha ~ -0.88 at z=1 -- of order tens of percent. This
    exceeds the observational bound by ~3.6e5 (five to six orders of
    magnitude). DECISIVELY FALSIFIED.

  - UNIVERSAL / horizon-scale scaling: if L_v is the near-conserved global
    atom-pair background, its fractional change over a few-Gyr lookback is
    tiny and the prediction can satisfy the bound -- but only by making alpha
    effectively constant, at which point Picture A is observationally
    indistinguishable from Picture B (the space-intrinsic field, density
    irrelevant). The density-source content is then unobservable.

Conclusion. The alpha-variation test rules out the strong, testable form of
Picture A (coupling tracks LOCAL rope density and varies with cosmic time),
and forces any surviving version into observational equivalence with Picture B.
The vivid claim 'rope density literally sets the EM coupling and should be seen
to vary' does NOT survive. This constrains an INTERPRETIVE claim only; the
structural EM results (Maxwell equations, charge quantization, stiffness
reconciliation EM-007, continuity EM-008, dynamical drive EM-010) are
independent of it and unaffected. Registered as EM-011 (Failed: the strong
density-source reading is falsified).
"""
import numpy as np

OBS_BOUND = 2.4e-6  # |Delta alpha/alpha| over z~0.7-1.5 (Keck MM null result)


def dalpha_local(z):
    """Picture A, local/matter-tracking: alpha ~ 1/L_v, L_v ~ (1+z)^3."""
    return 1.0 / (1.0 + z) ** 3 - 1.0


def test():
    # Local scaling grossly violates the observed bound across the probed range.
    for z in (0.5, 1.0, 1.5):
        pred = abs(dalpha_local(z))
        assert pred > 1e3 * OBS_BOUND, "local scaling should grossly exceed bound"
    factor = abs(dalpha_local(1.0)) / OBS_BOUND
    assert factor > 1e4, "falsification margin should be many orders of magnitude"

    # The falsification is the result: the strong density-source reading is dead.
    print(f"predicted |Dalpha/alpha| (local scaling, z=1) = {abs(dalpha_local(1.0)):.3f}")
    print(f"observed bound |Dalpha/alpha| ~ {OBS_BOUND:.1e}")
    print(f"prediction exceeds bound by factor ~ {factor:.1e}")
    print("RESULT: strong (local/matter-tracking) Picture A is FALSIFIED.")
    print("Surviving (universal) version is observationally equivalent to Picture B.")
    print("PASS (this benchmark records a NEGATIVE result: the strong density-")
    print("      source reading of the EM coupling does not survive observation).")


if __name__ == "__main__":
    test()
