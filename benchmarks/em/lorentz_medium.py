"""Is the rope medium's rest frame detectable by its own waves? (Partial result.)

A physical medium filling space naively defines a preferred rest frame, which
Michelson-Morley-class experiments exclude. This benchmark records what CAN be
shown and sharpens what cannot.

SHOWN (this file): the rope wave equation psi_tt = c^2 psi_xx is EXACTLY
Lorentz-form-invariant and NOT Galilean-invariant. Under a Galilean boost it
develops a cross term and a direction-dependent speed c^2 - v^2 (the sound/
aether behaviour that would fail Michelson-Morley); under a Lorentz boost the
d'Alembertian maps to itself exactly. So the rope wave equation, AS WRITTEN, is
of the relativistic type: its own excitations cannot detect the medium's rest
frame. This rebuts the naive 'any medium is Galilean like sound' objection.

NOT SHOWN (open, see FND-REL-001): WHY the massive-strand mechanics yield the
Lorentz-invariant wave equation rather than a Galilean one. A wave on a literal
moving string is Galilean (preferred frame = the string). Whether the rope
mechanics force the Lorentz-invariant form -- e.g. because excitations are the
only probes and material rest position is operationally undefinable, as in some
emergent-Lorentz condensed-matter models -- is NOT established. This benchmark
therefore verifies a necessary (not sufficient) condition.
"""
import sympy as sp


def galilean_breaks_wave_equation():
    """Galilean boost introduces a cross term / direction-dependent speed."""
    v, c = sp.symbols("v c", positive=True)
    a, b = sp.symbols("Dt Dx")  # d/dt', d/dx'
    # Galilean: d/dt = Dt - v Dx ; d/dx = Dx
    dt = a - v * b
    dx = b
    expr = sp.expand(dt**2 - c**2 * dx**2)  # from psi_tt - c^2 psi_xx
    # invariant form would be a**2 - c**2 b**2; check the difference is nonzero
    diff = sp.simplify(expr - (a**2 - c**2 * b**2))
    return diff != 0


def lorentz_preserves_wave_equation():
    """Lorentz boost maps the d'Alembertian to itself exactly."""
    v, c = sp.symbols("v c", positive=True)
    g = 1 / sp.sqrt(1 - v**2 / c**2)
    a, b = sp.symbols("Dt Dx")
    dt = g * (a - v * b)
    dx = g * (b - (v / c**2) * a)
    box = sp.expand((1 / c**2) * dt**2 - dx**2)
    target = sp.expand((1 / c**2) * a**2 - b**2)
    return sp.simplify(box - target) == 0


def test():
    assert galilean_breaks_wave_equation(), "Galilean boost should break the wave equation"
    assert lorentz_preserves_wave_equation(), "Lorentz boost should preserve the wave equation"
    print("Galilean boost: breaks the wave equation (cross term, speed c^2 - v^2) -> sound-like")
    print("Lorentz boost:  preserves the d'Alembertian exactly -> relativistic type")
    print("PASS (PARTIAL): the rope wave equation as written cannot detect the medium's")
    print("      rest frame. OPEN (FND-REL-001): whether strand mechanics FORCE this")
    print("      Lorentz form rather than a Galilean one is not established.")


if __name__ == "__main__":
    test()
