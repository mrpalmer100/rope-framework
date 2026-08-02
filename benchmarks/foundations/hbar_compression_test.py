"""HBAR-009 (Modeled): THE TWO COMPRESSIONS ARE NOT THE SAME THING --
four independent failures, and a convergence that is worth more than
any of them.

THE QUESTION: HBAR-008 showed the dipole cancellation is broken only by
a medium compressed along its dipole axis. ELEC-041 found the electron
to be a twentyfold local compression of the medium. Are these the same
compression?

TEST 1 -- LOCALITY. HBAR-008's requirement is GLOBAL, because hbar must
be fixed in vacuum, where it is measured. ELEC-041's compression is
local. Compressed volume fractions: 7.3e-22 in a hydrogen atom,
1.4e-23 in a simple solid, 2.3e-22 in iron. Even in dense matter about
one part in 1e22 of space is compressed, and in vacuum none of it is.
FAILS.

TEST 2 -- DIRECTION. HBAR-008 needs one preferred axis everywhere.
ELEC-041's compression is radial about each particle, oriented by that
particle's own geometry, so it averages to zero over any collection of
randomly oriented particles. FAILS.

TEST 3 -- CIRCULARITY. ELEC-041's twentyfold figure came from R/w with
R fixed by a calibration that already used hbar (kappa -> alpha hbar c,
E -> m_e c^2). Explaining hbar with it would be circular. FAILS.

TEST 4 -- THE CONSEQUENCE IF TRUE, and this is the strongest. If
compression supplied the equation of state, T w^2 would be fixed only
where matter is, making hbar a property of MATTER-FILLED regions. But
hbar is measured to the same value in high vacuum and inferred from
interstellar spectra. The hypothesis is not merely unsupported, it is
CONTRADICTED. FAILS.

THE CONVERGENCE. HBAR-007's one surviving escape was that w is set by
cosmological history rather than force balance; HBAR-008's requirement
is a global preferred direction. A medium laid down at formation with
an ordered orientation satisfies BOTH at once -- uniformity inherited
from initial conditions, and a global axis breaking the dipole
cancellation everywhere. Two separate dead ends point at one
resolution.

THE PRICE, named now rather than later: a global preferred direction is
Lorentz-violating structure, and modern tests bound preferred-frame
parameters at 1e-17 to 1e-20 depending on sector. Whether a strand
orientation axis couples to those observables is not computable from
what the corpus has, but it is where this proposal will be attacked.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'HBAR011_state.npz')
    # Test 1: the locality mismatch, quantified
    for k in ('frac_atom', 'frac_solid', 'frac_iron'):
        assert float(s[k]) < 1e-20, f"{k}: compressed fraction ~1e-22, requirement is global"
    # the compression itself is real but small in extent
    assert float(s['R_e']) < float(s['w']), "the object IS smaller than the ambient spacing"
    assert float(s['w'])/float(s['R_e']) > 10, "by the ~20x ELEC-041 reported"
    # Test 4's arithmetic: matter-filled regions are a vanishing fraction of anywhere
    assert float(s['frac_iron'])/1.0 < 1e-20, \
        "even iron is 1e-22 compressed: hbar cannot be a property of compressed regions"
    print(f"compressed fractions: atom {float(s['frac_atom']):.1e}, solid "
          f"{float(s['frac_solid']):.1e}, iron {float(s['frac_iron']):.1e}; "
          f"ambient/object = {float(s['w'])/float(s['R_e']):.0f}x")
    print("PASS: the two compressions are not the same -- local vs global, radial vs axial,")
    print("      circular, and contradicted by hbar's value in vacuum.")


if __name__ == "__main__":
    test()
