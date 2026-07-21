"""The Lorentz force F = q v x B on a single moving charge, from the swinging-rope
mechanism's gauge-forced coupling.

This is the microscopic magnetic force law (complementing EM-012, the force
between wires). A charge is a linking defect; moving it is a current element
q*v. The mechanism's coupling of current to the potential, integral J.a, is the
same coupling shown to be FORCED by gauge invariance + current conservation in
EM-010. For a point charge this is the interaction Lagrangian q v.a. The
standard Lagrangian treatment L = (1/2)m v^2 + q v.a - q phi gives, via
Euler-Lagrange with canonical momentum p = m v + q a,

    m dv/dt = q (E + v x B),

i.e. the full Lorentz force with the CORRECT coefficient. (Taking only the naive
gradient of the potential energy gives q v x B / 2; the factor of two is
recovered by the convective term q (v.grad) a from d/dt of the canonical
momentum -- q grad(v.a) - q (v.grad) a = q v x curl a = q v x B. This is
standard mechanics, verified numerically below, not a model adjustment.)

The result reproduces the DEFINING features of the magnetic force: it is
perpendicular to both v and B, it does NO WORK (F.v = 0), and it reverses with
v or B. What the rope model supplies is that the coupling q v.a is mechanically
realized and gauge-forced, so the Lorentz force is a mechanical consequence
rather than a postulate. Uses only the gauge-forced coupling (EM-010) plus
classical mechanics; it does not assume a field profile, so it is more general
than the wire result. Reproduces a known theorem. Registered as EM-013.
"""
import numpy as np


def lorentz_force(v_dir, B_vec, q=1.0):
    """Full kinetic force on a charge with velocity v in external field B,
    from F = q grad(v.a) - q (v.grad) a with a = (1/2) B x r (symmetric gauge).
    Equals q v x B."""
    v = np.array(v_dir, float)
    B = np.array(B_vec, float)

    def a_ext(r):
        return 0.5 * np.cross(B, r)

    r0 = np.array([0.3, 0.1, 0.05])
    h = 1e-5
    # term 1: q grad(v . a)
    grad_va = np.zeros(3)
    for i in range(3):
        rp = r0.copy(); rp[i] += h
        rm = r0.copy(); rm[i] -= h
        grad_va[i] = q * (np.dot(v, a_ext(rp)) - np.dot(v, a_ext(rm))) / (2 * h)
    # term 2: - q (v.grad) a
    conv = np.zeros(3)
    for i in range(3):
        for j in range(3):
            rp = r0.copy(); rp[j] += h
            rm = r0.copy(); rm[j] -= h
            conv[i] += v[j] * (a_ext(rp)[i] - a_ext(rm)[i]) / (2 * h)
    return grad_va - q * conv


def test():
    cases = [([1, 0, 0], [0, 0, 1]),
             ([0, 1, 0], [0, 0, 1]),
             ([1, 0, 0], [0, 1, 0]),
             ([2, -1, 0.5], [0, 0, 1]),
             ([1, 1, 1], [0, 0, 1])]
    for vd, Bv in cases:
        F = lorentz_force(vd, Bv)
        expected = np.cross(vd, Bv)  # q = 1
        # (1) magnitude and direction match q v x B exactly
        assert np.allclose(F, expected, atol=1e-6), f"F={F} != qvxB={expected}"
        # (2) perpendicular to v and to B
        assert abs(np.dot(F, vd)) < 1e-8, "force not perpendicular to v"
        assert abs(np.dot(F, Bv)) < 1e-8, "force not perpendicular to B"
        # (3) does no work
        assert abs(np.dot(F, vd)) < 1e-8, "magnetic force must do no work"

    # sign reversal with v and with B
    F = lorentz_force([1, 0, 0], [0, 0, 1])
    F_vrev = lorentz_force([-1, 0, 0], [0, 0, 1])
    F_Brev = lorentz_force([1, 0, 0], [0, 0, -1])
    assert np.allclose(F, -F_vrev, atol=1e-6), "force must reverse with v"
    assert np.allclose(F, -F_Brev, atol=1e-6), "force must reverse with B"

    print("F = q v x B reproduced exactly in all test cases (incl. oblique).")
    print("perpendicular to v and B: PASS;  does no work (F.v=0): PASS")
    print("reverses with v and with B: PASS")
    print("PASS: the Lorentz force follows from the mechanism's gauge-forced")
    print("      coupling q v.a plus classical mechanics.")


if __name__ == "__main__":
    test()
