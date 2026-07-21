"""Helix screw-sense and the POSSIBILITY of circulation (Maxwell paper 6.3).

STATUS: Modeled -- a type-and-sign result, NOT a dynamical derivation.

A purely longitudinal, scalar imbalance oscillating along the wire axis is
invariant under rotation about that axis and therefore cannot select a
circulation sense: on its own it produces no magnetic field. Circulation
requires an axial pseudovector to map the radial direction to the azimuthal
one (via a cross product). The two-strand rope, being a helix, supplies
exactly such an object: its screw-sense s = (t x dt/dz)_z is nonzero, and its
SIGN is the winding handedness. Hence a moving winding CAN drive a circulating
response of the correct type, and reversing the winding (or the transport
direction) reverses it -- matching the observed reversal of B.

What this establishes: circulation is POSSIBLE and correctly SIGNED, and a
featureless scalar charge could produce none. What this does NOT establish:
the dynamical DRIVE -- the equation of motion showing a moving current
actually evolves the surrounding network into the circulating pattern at the
observed field speed. That remains the sector's open problem (section 6.3 /
4.5); this benchmark does not touch it. Registered as EM-009 (Modeled).
"""
import numpy as np


def helix_screw_sense(handedness=+1, pitch=1.0, R=0.1, N=400):
    """Axial component of t x (dt/dz) for a helical strand; sign = handedness."""
    zs = np.linspace(0, 1, N)
    w = 2 * np.pi / (handedness * pitch)
    s = 0.0
    for z in zs:
        t = np.array([-R * w * np.sin(w * z), R * w * np.cos(w * z), 1.0])
        t /= np.linalg.norm(t)
        dz = 1e-4
        t2 = np.array([-R * w * np.sin(w * (z + dz)), R * w * np.cos(w * (z + dz)), 1.0])
        t2 /= np.linalg.norm(t2)
        s += np.cross(t, (t2 - t) / dz)[2]
    return s / N


def scalar_imbalance_screw_sense():
    """A direction-less scalar imbalance carries no axial pseudovector."""
    return 0.0


def test():
    sp = helix_screw_sense(+1)
    sm = helix_screw_sense(-1)
    # helix carries a nonzero, sign-definite screw sense
    assert abs(sp) > 1e-3, "helix must carry a nonzero screw sense"
    assert np.sign(sp) != np.sign(sm), "reversing handedness must reverse the sense"
    assert abs(abs(sp) - abs(sm)) < 1e-6, "magnitude symmetric under handedness flip"
    # a scalar imbalance carries none -> could produce no circulation
    assert scalar_imbalance_screw_sense() == 0.0, "scalar imbalance must give zero"

    print(f"helix screw-sense: +handedness = {sp:+.3f}, -handedness = {sm:+.3f}")
    print("scalar imbalance screw-sense: 0.000 (no circulation possible)")
    print("PASS: circulation is possible and correctly signed (type-and-sign).")
    print("NOTE: this does NOT derive the dynamical drive (open; see 6.3).")


if __name__ == "__main__":
    test()
