"""FND-MATTER-033 (Derived): THE MICROSTRUCTURE DERIVATION -- THE
GATE COLLAPSES, AND THE COLLAPSED GATE AUDITS THE CONDITIONAL. The
last pure-theory item on the board, executed: two of the gate's
unknowns fall to exact identities, lambda reduces to one measured
constant -- and the first act of the reduced gate is to run the
doublet hypothesis through the framework's own bounds and DISFAVOR
it.

THE TWO IDENTITIES (Derived; verified numerically):
  (1) THE BEADED-STRING IDENTITY: the conditioning modes are
      transverse vibrations of the tensioned rope, so the transverse
      coupling is NOT an independent constant -- kt = T/a. Verified:
      with kt = T/a the lattice's long-wave speed equals the
      continuum string's sqrt(T/rho) to machine precision.
  (2) THE WAVE-SPEED CLOSURE: torque/transverse waves at c (the
      framework's own postulate) fixes mu = T a / c^2 (the
      relativistic-string relation rho = T/c^2), whence the mode
      unit collapses: sqrt(kt/mu) = c/a -- the light-crossing
      frequency of one mesh cell, as a medium with wave speed c
      demands.

THE COLLAPSE: lambda = hbar c / (a T D). The gate's unknowns reduce
from {kt, mu, T, a, D} to ONE measured dimensionless combination,
Lambda = T a D / (hbar c), lambda = 1/Lambda -- the same epistemic
class FND-MATTER-005 assigned to a itself. (Stated fork: this is the
QUANTUM reading of the mode term, hbar per mode; the classical-
amplitude reading would replace hbar with a free action scale.)

THE AUDIT, exact arithmetic: doublet = n/p demands lambda* =
0.029-0.035; the proton scale gives T D = m_p / 27.75 = 33.8 MeV;
the collapsed gate then FORCES a = hbar c / (lambda* T D) = 167-204
fm (102 fm even under the band-top factor of two) -- against the
corpus's own Lorentz bound a < ~0.1 fm: VIOLATION BY THREE ORDERS OF
MAGNITUDE, robust across every granted ambiguity. THE VERDICT: under
the quantum mode reading, the doublet = n/p hypothesis is
INCONSISTENT with the framework's microstructure. The named escape
routes, honestly: (a) the doublet is not n/p -- the near-degeneracy
stays a coincidence of configuration (the cleanest reading; this
audit is evidence for it); (b) the classical-amplitude reading --
which reopens a free scale and surrenders the model's rigidity;
(c) sub-unity mode occupations -- ad hoc without a mechanism. The
conditional was built to be wrong. The microstructure caught it.
"""
import numpy as np


def test():
    # LINK 1: beaded-string identity
    T, a, mu = 2.7, 0.31, 1.9
    kt = T/a
    assert abs(a*np.sqrt(kt/mu) - np.sqrt(T/(mu/a))) < 1e-12, \
        "kt = T/a reproduces the tensioned string exactly"
    # LINK 2: wave-speed closure
    c = 1.0
    mu_fixed = T*a/c**2
    assert abs(np.sqrt((T/a)/mu_fixed) - c/a) < 1e-12, "mode unit collapses to c/a"
    # LINK 4: the audit
    hbarc, mp, massD = 197.327, 938.272, 27.75
    TD = mp/massD
    for lam_star in (0.0286, 0.0349):
        a_forced = (hbarc/lam_star)/TD
        assert a_forced > 100.0, "the forced mesh scale exceeds 100 fm across the lambda* range"
    a_band_top = (hbarc/(2*0.0286))/TD
    assert a_band_top > 50.0, "even the band-top factor of two leaves a > 50 fm"
    violation = ((hbarc/0.0286)/TD)/0.1
    assert violation > 500, "the Lorentz bound violated by orders of magnitude, robustly"
    print(f"identities verified to machine precision; the gate collapses to lambda = hbar c/(a T D)")
    print(f"the audit: doublet=n/p forces a = {(hbarc/0.0286)/TD:.0f} fm vs the bound 0.1 fm")
    print(f"           ({violation:.0f}x violation; {a_band_top:.0f} fm even band-top)")
    print("PASS: two identities derived, the gate reduced to one measured constant, and the")
    print("      conditional -- built to be wrong -- caught by the framework's own microstructure.")


if __name__ == "__main__":
    test()
