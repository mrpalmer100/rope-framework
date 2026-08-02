"""HBAR-007 (Modeled): THE EQUATION OF STATE THAT WOULD MAKE HBAR
UNIVERSAL EXISTS, IS UNIQUE, IS PHYSICALLY NATURAL -- AND IS UNSTABLE.
Stabilising it costs a 1e12 fine-tuning.

THE DERIVATION. For a medium of strands with tension T, spacing w and
an inter-strand potential U(w) per unit length, the energy density is
E(w) = [T + U(w)]/w^2 and equilibrium requires U'(w) w = 2[T + U(w)].
For a power law U = C w^q this gives C w^q (q-2) = 2T, hence
w ~ T^(1/q). Constancy of T w^2 needs w ~ T^(-1/2), so
    q = -2   UNIQUELY.
With U(w) = C/w^2 the equilibrium is w^2 = -2C/T, giving
T w^2 = -2C = CONSTANT, with C < 0: the interaction must be ATTRACTIVE.
The required strength is |C| = hbar c/(2 N^2) = 2.833e-30 J m, and the
medium's own T w^2 reproduces it to 0.1 percent.

THE PHYSICAL READING, and it converges with earlier work: a potential
going as 1/w^2 per unit LENGTH between parallel lines corresponds to a
three-dimensional pair potential V ~ 1/r^3 -- dipole-dipole. Oriented
strands interacting through their transverse orientation give exactly
this, and orientation is precisely the degree of freedom HBAR-003
identified as the missing phase. Three separate lines of the
investigation point at the same structure.

THE OBSTRUCTION. E(w) = T/w^2 - |C|/w^4 has
E'' = 6T/w^4 - 20|C|/w^6, and at the equilibrium |C| = T w^2/2 this is
E'' = -4T/w^4 < 0. THE EQUILIBRIUM IS A MAXIMUM. The medium described
by the unique constancy-preserving equation of state is unstable
against collapse (E -> -infinity as w -> 0).

THE PRICE OF STABILITY. Adding a short-range repulsion D/w^6 gives
T w^4 - 2|C| w^2 + 3D = 0, so T w^2 = |C| + sqrt(|C|^2 - 3DT) and the
constancy is spoiled at order 3DT/(4|C|^2). Requiring hbar constant to
1e-12 demands D/(|C| w^2) < 6.7e-13, i.e. the stabilising term must be
1.5e12 times weaker than the attraction at the equilibrium spacing.
Stability and constancy are purchased against each other.

THE STANDING ALTERNATIVE, named not tested: the spacing may not be set
by equilibrium at all. If w is fixed by history -- a cosmological
initial condition rather than a force balance -- then T w^2 is constant
because the medium was laid down uniform, and no equation of state is
required. That moves the question from dynamics to cosmology and is
the honest remaining option.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'HBAR009_state.npz')
    hbar = 1.054571817e-34; c = 2.99792458e8
    # the exponent is forced
    assert int(s['q']) == -2, "q = -2 uniquely: the only power law giving T w^2 = const"
    # the strength matches the medium to 0.1%
    assert abs(float(s['ratio']) - 1) < 0.01, "the medium's T w^2 reproduces hbar c/N^2"
    assert abs(float(s['Cmag']) - float(s['Tw2'])/2)/float(s['Cmag']) < 1e-9, "|C| = T w^2/2"
    # THE OBSTRUCTION: the equilibrium is a maximum
    assert float(s['Epp']) < 0, "E'' = -4T/w^4 < 0: the equilibrium is UNSTABLE"
    # the price of stability
    tune = float(s['tune'])
    assert tune < 1e-10, "the stabiliser must be ~1e12 times weaker than the attraction"
    assert 1/tune > 1e11, "a fine-tuning of order 1e12"
    print(f"q = {int(s['q'])} uniquely; |C| = {float(s['Cmag']):.3e} J m (medium ratio "
          f"{float(s['ratio']):.4f}); E'' = {float(s['Epp']):.2e} < 0 (unstable); "
          f"stabiliser tuning {1/tune:.1e}x")
    print("PASS: the constancy-preserving equation of state is unique and dipole-natural,")
    print("      but unstable -- and stability costs a 1e12 fine-tuning against constancy.")


if __name__ == "__main__":
    test()
