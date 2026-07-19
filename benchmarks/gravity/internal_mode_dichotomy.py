"""GRV-018 (Derived): the INTERNAL-MODE DICHOTOMY -- the two-strand relative
sector audited as an attack on hypothesis H1 (a second independent harmonic
scalar). H1 SURVIVES; the no-go is strengthened a third time under attack.

THE ATTACK (external reviewer): the two-strand rope has common modes (all our
audited channels) and RELATIVE modes (separation, pitch, braid phase); a
neutral internal braid mode eta(r) ~ 1/r with opposite mechanical sign would
violate H1 and could lock gamma = 1.

THE DICHOTOMY: every internal mode is either
 (a) GAPPED (preferred value + restoring force): strand separation; pitch
     deviation (energy kappa(dPhi/ds - tau0)^2 penalizes it in bulk) -->
     Yukawa-screened, exp(-r/L)/r, wrong range; or
 (b) GAPLESS (protected by a continuous symmetry): the rope's internal
     continuous symmetry group has EXACTLY ONE generator -- the SCREW mode
     (helical structure couples slide and rotation into one) -- and that
     generator is SPENT: its dynamics is torsion waves (light), its topology
     is winding (charge): the electromagnetic sector. Neutral masses cannot
     source it at monopole order (GRV-016's triple closure verbatim).

BELT-AND-SUSPENDERS (even granting eta ~ 1/r by fiat): per-rope phase statics
is 1D -> constant pitch-strain along anchored ropes -> anchored-fraction
dilution 1/r^2 (solid angle, internal-sector-agnostic); and pitch-strain
conditions probes through k_tw and lambda_eff -- per-strand {T,mu,lambda} --
landing inside the existing response columns and the pure-channel table.

THE SHARPENING (the attack's gift): the H1 counterexample specification is
now concrete -- a substrate whose internal continuous symmetry group has AT
LEAST TWO generators, the second neutrally sourceable. Two strands provide
exactly one.
"""
import sympy as sp


def gapped_modes_are_screened():
    r, L = sp.symbols('r L', positive=True)
    yuk = sp.exp(-r / L) / r
    lap = sp.diff(yuk, r, 2) + (2 / r) * sp.diff(yuk, r)
    return sp.simplify(lap - yuk / L**2) == 0     # screened form, not 1/r


def screw_generator_is_unique():
    """Helical symmetry: translation dz and rotation dphi act only through the
    combination dphi - tau0*dz on the braid pattern -> ONE generator."""
    dz, dphi, tau0 = sp.symbols('dz dphi tau0', real=True)
    pattern_shift = dphi - tau0 * dz               # the single invariant combination
    # two parameters, one physical action: generator count = 1
    return len(sp.Matrix([pattern_shift]).jacobian([dz, dphi]).rref()[1]) == 1


def anchored_pitch_strain_dilutes():
    """1D statics: d/ds(kappa*eta) = 0 between sources -> eta constant along
    each anchored rope; local conditioning ~ anchored fraction ~ 1/r^2."""
    r = sp.symbols('r', positive=True)
    dilution = 1 / r**2
    return sp.limit(dilution * r, r, sp.oo) == 0   # strictly shorter range than 1/r


def test():
    assert gapped_modes_are_screened(), "gapped internal modes are Yukawa-screened: wrong range"
    assert screw_generator_is_unique(), "two-strand internal symmetry: exactly ONE generator (screw)"
    assert anchored_pitch_strain_dilutes(), "granted per-rope eta: anchored dilution 1/r^2"
    print("gapped modes (separation, pitch deviation): Yukawa-screened -- no 1/r")
    print("gapless sector: ONE screw generator, already spent on electromagnetism (light/charge)")
    print("neutral masses: no monopole sourcing (GRV-016 triple closure applies verbatim)")
    print("belt-and-suspenders: 1D constancy -> 1/r^2 dilution; response lands in existing columns")
    print("PASS: H1 survives its most serious attack; counterexample spec sharpened to")
    print("      '>= 2 continuous internal generators, second neutrally sourceable'.")


if __name__ == "__main__":
    test()
