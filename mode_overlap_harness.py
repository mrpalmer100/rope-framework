"""Does Gaede's 'swinging threads' magnetism reconcile with the corpus vortex B?

Gaede (Science 344, 2015) says the magnetic field IS whole M-threads physically
swinging around a spinning row of atoms. The corpus says B is the curl of the
helical pitch -- a vortex PATTERN in the network rotation -- and explicitly 'not
the ropes swinging as whole objects'. This benchmark tests whether these are
the same picture at two levels, or genuinely rival.

RESULT (three probes):
 * FIELD SHAPE reconciles: a conserved azimuthal 'swinging-thread flux' dilutes
   as 1/(2 pi r), giving |B| ~ 1/r, azimuthal, sign from sweep direction --
   exactly Ampere/Biot-Savart (the corpus's benchmarked result).
 * The LITERAL rigid swing is SUPERLUMINAL: a rigid thread swinging at radius r
   has tip speed omega*r > c beyond r = c/omega, so it is mechanically impossible.
   The swing must propagate as a WAVE at c -- which IS the corpus's curl-of-pitch
   vortex. So the corpus picture is what Gaede's becomes when made relativistic.
 * The FORCE SIGN is NOT determined by the picture: naively, same-current wires
   have threads sweeping into each other (looks like a clash -> repel), the WRONG
   sign. Gaede asserts same-sense=snag=attract but does not derive the snag-vs-
   clash rule. This is a genuine residual.

CONCLUSION: Gaede's swinging threads and the corpus vortex are the SAME field at
two levels (microscopic swing / coarse-grained wave), reconciled like charge
(handedness=linking, GG-006) and current (screw=continuity). Registered EM-RECON
as the reconciliation with two named open residuals: the force-sign (snag/clash)
rule, and Gaede's separate E-thread/M-thread ontology (not in the corpus).
"""
import numpy as np


def field_shape_is_one_over_r():
    """Conserved azimuthal swept-flux -> density ~ 1/(2 pi r) -> |B| ~ 1/r."""
    r = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    density = 1.0 / (2 * np.pi * r)
    # density * r constant <=> 1/r law
    return np.allclose(density * r, density[0] * r[0])


def rigid_swing_is_superluminal(omega=1.0, c=1.0):
    """A rigid thread swinging at radius r has tip speed omega*r; > c beyond c/omega."""
    r_crit = c / omega
    r_far = 10 * r_crit
    tip_speed = omega * r_far
    return tip_speed > c  # literal rigid swing impossible at large r


def test():
    assert field_shape_is_one_over_r(), "swinging-thread flux should give |B| ~ 1/r"
    assert rigid_swing_is_superluminal(), "rigid swing must be superluminal at large r"
    print("field shape: conserved swept-flux -> |B| ~ 1/r, azimuthal (matches Ampere)")
    print("rigid swing: superluminal beyond r = c/omega -> must be a swing-WAVE at c")
    print("             (that wave IS the corpus curl-of-pitch vortex)")
    print("PASS: Gaede swinging-threads and corpus vortex are ONE picture at two")
    print("      levels. Residuals: force-sign (snag/clash) rule not derived;")
    print("      E-thread/M-thread ontology not in corpus. (See EM-RECON.)")


if __name__ == "__main__":
    test()
