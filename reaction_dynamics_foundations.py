"""Geometry-dependence of the dipolar/field-term ordering (Path C stress test).

EM-RECON-003 found the 2D square-lattice SWIRL-field strain favors antiferro.
This benchmark tests whether that answer is universal. It is NOT: using true
magnetic dipole-dipole energy on the same lattice, the ordering FLIPS with moment
orientation:
  * OUT-of-plane moments (the swirl geometry of EM-RECON-003): antiferro lower.
  * IN-plane moments: ferro lower.
3D simple-cubic dipoles are near-degenerate (the known dipolar cubic cancellation),
so 3D is not decisive. Conclusion: the field-term's ferro/antiferro preference is
geometry-dependent (moment orientation + lattice), exactly as real dipolar physics
is. EM-RECON-003's antiferro answer is correct for its geometry but not universal.
"""
import numpy as np


def dipole_pair_U(m1, m2, r_vec):
    r = np.linalg.norm(r_vec); rhat = r_vec / r
    return (np.dot(m1, m2) - 3 * np.dot(m1, rhat) * np.dot(m2, rhat)) / r**3


def square_energy(N, moment_dir, pattern, a=1.0):
    pos = [np.array([(i - (N - 1) / 2) * a, (j - (N - 1) / 2) * a, 0.0]) for i in range(N) for j in range(N)]
    idx = [(i, j) for i in range(N) for j in range(N)]
    signs = [1 if pattern == 'ferro' else (1 if (i + j) % 2 == 0 else -1) for (i, j) in idx]
    m = [s * np.array(moment_dir, float) for s in signs]
    E = 0.0
    for a_ in range(len(pos)):
        for b_ in range(a_ + 1, len(pos)):
            E += dipole_pair_U(m[a_], m[b_], pos[b_] - pos[a_])
    return E


def test():
    # out-of-plane: antiferro lower
    ef_out = square_energy(6, [0, 0, 1], 'ferro')
    ea_out = square_energy(6, [0, 0, 1], 'af')
    # in-plane: ferro lower
    ef_in = square_energy(6, [1, 0, 0], 'ferro')
    ea_in = square_energy(6, [1, 0, 0], 'af')
    assert ea_out < ef_out, "out-of-plane should favor antiferro"
    assert ef_in < ea_in, "in-plane should favor ferro"
    print(f"out-of-plane moments: ferro={ef_out:+.2f} af={ea_out:+.2f} -> ANTIFERRO lower")
    print(f"in-plane moments:     ferro={ef_in:+.2f} af={ea_in:+.2f} -> FERRO lower")
    print("PASS: field-term ordering is GEOMETRY-DEPENDENT (flips with moment")
    print("      orientation). EM-RECON-003's antiferro is specific to out-of-plane,")
    print("      not universal -- matching real dipolar physics.")


if __name__ == "__main__":
    test()
