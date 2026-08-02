"""HBAR-008 (Modeled): THE DIPOLE GIVES THE RIGHT FORM AND ZERO
MAGNITUDE -- and supplies the missing phase, at the cost of importing
Bohr-Sommerfeld. One mechanism, two questions, one and a half answers.

STEP 1, THE FORM -- SUCCEEDS EXACTLY. Two parallel strands along z at
transverse separation w, each carrying a transverse dipole p along x,
interact through V = k p^2 [1 - 3(x.r)^2/r^2]/r^3. Integrating along
the strand, with int dz/r^3 = 2/w^2 and int dz/r^5 = 4/(3w^4)
(verified numerically at w = 0.5, 1, 2), gives
    U(w) = (2 k p^2/w^2) [1 - 2 cos^2 phi]
THE 1/w^2 FORM REQUIRED BY HBAR-007 FALLS STRAIGHT OUT. The angular
factor is -1 for neighbours along the dipole (attractive), +1
perpendicular (repulsive), 0 at 45 degrees.

STEP 2, THE MAGNITUDE -- FAILS BY SYMMETRY. Summing over a lattice of
aligned dipoles gives EXACTLY ZERO: square -3.2e-15, triangular
-1.7e-15. Each attractive direction is cancelled by a repulsive one.
(A METHODOLOGICAL NOTE, filed: the first attempt returned -9.6e-2 for
the triangular lattice, which was a BOUNDARY ARTIFACT -- in the
triangular basis x = m + n/2 can leave an index box of the same size
as the circular cutoff, so the sum ran over a clipped, asymmetric
region. Enlarging the box to twice the cutoff sends it to 1e-15. The
containment of a cutoff inside its index range is exactly the kind of
thing this corpus has learned to check.)

STEP 3, WHAT WOULD RESCUE IT. Anisotropy breaks the cancellation: a
lattice compressed along the dipole axis by a factor a gives sums of
-2.21 (a = 0.7), -0.49 (a = 0.9), 0 (a = 1), +0.35 (a = 1.1). NET
ATTRACTION REQUIRES A MEDIUM COMPRESSED ALONG ITS OWN DIPOLE
DIRECTION -- an ordered, anisotropic vacuum rather than an isotropic
one. That is a substantive new requirement, not a free parameter.

STEP 4, THE PHASE -- SUCCEEDS, WITH AN IMPORT. The dipole direction is
an angle in the plane transverse to the strand: a genuine periodic
coordinate, which is exactly the structure HBAR-003 found missing. Its
conjugate momentum is the angular momentum, and HBAR-003 established
L = 2S, so applying the Bohr-Sommerfeld condition to the periodic
angle gives L = n hbar and hence S = n hbar/2. The framework now has
somewhere to PUT a quantization postulate, which it did not before --
but Bohr-Sommerfeld is imported, not derived.
"""
import sys
from pathlib import Path
import numpy as np
from scipy.integrate import quad

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def lattice_sum(kind, Rcut, Mbox, ratio=1.0):
    tot = 0.0
    for m in range(-Mbox, Mbox+1):
        for n in range(-Mbox, Mbox+1):
            if m == 0 and n == 0:
                continue
            if kind == 'square':
                x, y = m*ratio, float(n)
            else:
                x, y = m + 0.5*n, n*np.sqrt(3)/2
            r2 = x*x + y*y
            if r2 > Rcut*Rcut:
                continue
            tot += (1 - 2*x*x/r2)/r2
    return tot


def test():
    s = np.load(ROOT/'analysis'/'HBAR010_state.npz')
    # Step 1: the line integrals give the 1/w^2 form
    for w in (0.5, 1.0, 2.0):
        I3 = quad(lambda z: 1/(w*w + z*z)**1.5, -np.inf, np.inf)[0]
        I5 = quad(lambda z: 1/(w*w + z*z)**2.5, -np.inf, np.inf)[0]
        assert abs(I3 - 2/w**2)/I3 < 1e-6, "int dz/r^3 = 2/w^2"
        assert abs(I5 - 4/(3*w**4))/I5 < 1e-6, "int dz/r^5 = 4/(3w^4)"
    # Step 2: the symmetric lattice sums vanish
    assert abs(float(s['sq'])) < 1e-10, "square lattice: exactly zero"
    assert abs(float(s['tri'])) < 1e-10, "triangular lattice: exactly zero"
    # and the artifact is reproducible as an artifact
    clipped = lattice_sum('triangular', 20, 20)
    proper = lattice_sum('triangular', 20, 40)
    assert abs(clipped) > 1e-3 and abs(proper) < 1e-10, \
        "the boundary artifact is real and vanishes when the box contains the cutoff"
    # Step 3: anisotropy rescues it
    an = s['aniso']
    comp = [v for a, v in an if a < 1.0]
    stre = [v for a, v in an if a > 1.0]
    assert all(v < -1e-3 for v in comp), "compression along the dipole axis: ATTRACTIVE"
    assert all(v > 1e-3 for v in stre), "stretching: repulsive"
    print(f"line integrals exact; lattice sums {float(s['sq']):.1e}, {float(s['tri']):.1e} "
          f"(artifact when clipped: {clipped:.2e}); anisotropy a=0.7 -> {comp[0]:.2f}")
    print("PASS: the dipole gives the required 1/w^2 form exactly and zero magnitude by")
    print("      symmetry; net attraction demands an ANISOTROPIC medium.")


if __name__ == "__main__":
    test()
