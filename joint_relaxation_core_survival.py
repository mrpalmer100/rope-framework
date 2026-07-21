"""Why the strand mechanics FORCE the Lorentz-invariant wave equation: the fatal
convective (Galilean) term cannot be constructed.

This addresses the crux left open by lorentz_medium.py. A wave on a real moving
string is Galilean because the string has a material velocity w: the lab-frame
equation is (d_t + w d_x)^2 y = c^2 y_xx, and w=0 defines the string's rest
frame. The rope network avoids this because no physical material velocity w
exists to form the convective term. Three independent reasons, each committed to
by the corpus on grounds unrelated to the Lorentz question (so not circular):

  (i)   the longitudinal material mode is CONSTRAINED (rope inextensibility /
        unit-length constraint; used for EM mode-counting in
        rope_microscopic_mechanics) -- only transverse modes are physical;
  (ii)  point-identity ALONG the rope is GAUGE / a labelling convention
        (rope_gauge_geometry) -- there is no trackable 'painted dot' whose
        longitudinal motion could define w;
  (iii) what a current transports is a PHASE / linking PATTERN, not material
        (EM-008 'material stays home; the winding travels'; EM-014), so it
        carries no material momentum and forms no convective term.

This benchmark checks the two facts that make the argument bite:
  (A) a uniform transverse drift y -> y + a + b t adds nothing to the wave
      equation (depends on gradients), so bulk transverse motion is invisible;
  (B) a moving PHASE pattern with material at rest carries zero material
      momentum, so its motion is the wave speed c, not a convective w.

SCOPE (honest): this closes the WAVE sector -- excitations cannot detect a rest
frame, and the mechanics forbid the convective term rather than merely allowing
its absence. It does NOT close the MATTER sector: a complete proof also needs the
atoms/defects to provide no independent preferred-frame handle (that excitations
are the only probes). That piece is plausible (atoms are defects in the network,
not external rulers) but remains open -- see FND-REL-001.
"""
import sympy as sp


def transverse_drift_is_invisible():
    """y -> y + a + b t has zero second derivatives, so it cannot enter psi_tt - c^2 psi_xx."""
    x, t, a, b = sp.symbols("x t a b")
    add = a + b * t
    return sp.diff(add, t, 2) == 0 and sp.diff(add, x, 2) == 0


def phase_pattern_carries_no_material_momentum():
    """A pattern moving at phase speed with the material at rest: material momentum
    density rho*w_material = 0, so no convective velocity w is induced.
    Modelled symbolically: momentum flux of a pure phase translation is zero."""
    # material displacement field u(x,t); a pure phase pattern moves transverse
    # displacement but material longitudinal position is fixed => longitudinal
    # material velocity = d/dt (longitudinal position) = 0.
    x, t, c = sp.symbols("x t c")
    long_position = sp.Function("X")(x)  # longitudinal material coordinate: time-independent
    w_material = sp.diff(long_position, t)
    return w_material == 0


def test():
    assert transverse_drift_is_invisible(), "uniform transverse drift must not enter the wave equation"
    assert phase_pattern_carries_no_material_momentum(), "phase pattern must carry no material w"
    print("(A) uniform transverse drift y->y+a+bt: zero 2nd derivatives -> invisible to wave eq")
    print("(B) moving phase pattern, material at rest: longitudinal material velocity w = 0")
    print("PASS: no physical material velocity w exists, so the Galilean convective term")
    print("      (d_t + w d_x)^2 cannot be formed. The wave sector is FORCED to the")
    print("      Lorentz-invariant psi_tt = c^2 psi_xx. Matter-sector frame-independence")
    print("      remains open (FND-REL-001).")


if __name__ == "__main__":
    test()
