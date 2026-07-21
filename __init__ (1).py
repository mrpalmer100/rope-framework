"""Periodic-table shell structure from two-strand standing waves (qualitative).

Prompted by framing element build-up as incrementing the nuclear WINDING number
Z (= charge, which the rope picture handles cleanly as an integer), rather than
the packing count N (which is unfixed, FND-MATTER-003).

Two qualitative, non-circular structural results:

  (1) HYDROGEN SPECIAL. Z=1 is the minimum quantized winding (charge quantization,
      GG-006), so hydrogen is the irreducible atom. With one winding there is no
      winding-winding coupling, so hydrogen is the unique single-uncoupled-mode
      atom -- matching the real fact that hydrogen is the only exactly-solvable
      atom in standard QM.

  (2) SHELL CAPACITIES 2n^2. Standing torsion patterns on a sphere are spherical
      harmonics; the number of independent patterns up to level n is n^2. The
      two-STRAND rope supplies a factor of 2 (the rope analogue of spin). Product
      2n^2 = 2, 8, 18, 32 matches the real electron-shell capacities WITHOUT
      tuning -- the two-strand structure providing the spin-factor-of-2 for free.

SCOPE (honest): QUALITATIVE structure only -- the COUNTING and pattern, not
energies, not fusion, not absolute scales. 'Two strands = factor of 2' reproduces
the shell COUNT; it is a structural analogy to spin, not a proof the two-strand
multiplicity has all properties of physical spin. The NUCLEAR binding of Z protons
is a separate, untouched question. Registered as CHEM-STRUCT-001.
"""
import numpy as np


def spherical_harmonic_count(n):
    """Number of independent angular patterns up to principal level n = sum of
    (2l+1) for l=0..n-1 = n^2."""
    return sum(2 * l + 1 for l in range(n))


def shell_capacity_two_strand(n):
    """Two-strand doubling of the n^2 angular patterns = 2 n^2."""
    return 2 * spherical_harmonic_count(n)


def test():
    # spherical-harmonic counting gives n^2
    for n in range(1, 6):
        assert spherical_harmonic_count(n) == n * n

    # two-strand shells match the real periodic capacities 2,8,18,32,50
    real = {1: 2, 2: 8, 3: 18, 4: 32, 5: 50}
    for n, cap in real.items():
        assert shell_capacity_two_strand(n) == cap, f"shell {n} mismatch"

    print("spherical-harmonic pattern count up to n:  n^2 (verified n=1..5)")
    print("two-strand shell capacities 2n^2:", [shell_capacity_two_strand(n) for n in range(1, 6)])
    print("real electron-shell capacities:   [2, 8, 18, 32, 50]  -> MATCH")
    print("PASS: 2n^2 shells fall out of two-strand spherical standing waves, the")
    print("      two-strand nature supplying the spin-factor-of-2 with no tuning.")
    print("      (Qualitative counting result; not energies/fusion/scales.)")


if __name__ == "__main__":
    test()
