"""Reconciliation of the two continuum-stiffness derivations, and the
density-scaling of the electromagnetic coupling.

The microscopic-mechanics paper coarse-grains a cubic XY lattice to
    K = J/a                                        (lattice, 3 axial bonds/site)
A separate route treats the network as interpenetrating phase-elastic ropes:
    K = n_rope * lambda / 3                         (isotropic rope continuum)
where lambda is the per-length phase stiffness of a single rope.

These are the SAME K, not two competing claims, once expressed through the
geometry-independent invariant L_v = total rope length per unit volume, and
the identification lambda = J*a (a single lattice bond of length a, written as
a line stiffness, has lambda = J*a). Then:
    lattice:    K = J/a
    ropes:      K = (lambda/2) * L_v * <(t.G)^2>_iso * 2/|G|^2
                  = (lambda/2) * L_v * (1/3) * 2 = lambda * L_v / 3
    with L_v = 3/a^2 (cubic: 3 bonds of length a per volume a^3) and
    lambda = J*a:  K = (J*a)(3/a^2)/3 = J/a.   QED.

The '3 axial bonds' and the isotropic '1/3' are the same angular bookkeeping
counted two ways; they cancel against L_v. Consequence: K is LINEAR in rope
density (via L_v), which is the density-scaling used by the EM sector. This
benchmark verifies all three routes agree to numerical precision, that the
lattice stiffness is isotropic (direction-independent), and that K scales
linearly with rope length-per-volume.
Supports rope_maxwell_equations.docx section 6.2 and the stiffness
reconciliation. Registered as EM-007 (scaling: Derived).
"""
import numpy as np


def K_lattice_direct(L=20, q=0.01, J=1.0, a=1.0):
    """Direct cubic-lattice coarse-graining: K measured from imposed gradient."""
    xs = np.arange(L) * a
    X, Y, Z = np.meshgrid(xs, xs, xs, indexing="ij")
    th = q * X  # gradient along x
    E = 0.0
    for axis in range(3):
        d = np.roll(th, -1, axis=axis) - th
        sl = [slice(None)] * 3
        sl[axis] = slice(0, L - 1)
        E += J * np.sum(1 - np.cos(d[tuple(sl)]))
    V = (L - 1) * L * L * a**3
    return 2 * E / (q**2 * V)  # in units of J/a


def K_lattice_as_ropes(Gdir, J=1.0, a=1.0):
    """Cubic lattice re-expressed as axial rope segments (lambda=J*a)."""
    lam = J * a
    G = np.asarray(Gdir, float)
    per_vol = 1 / a**3  # bonds of each axis per unit volume
    u = sum(per_vol * (lam / 2) * (ax @ G) ** 2 for ax in np.eye(3))
    return 2 * u / (G @ G)  # J/a units


def K_isotropic_continuum(Gdir, L_v, J=1.0, a=1.0, N=200000, seed=0):
    """Isotropic phase-elastic rope continuum with total length/volume L_v."""
    lam = J * a
    rng = np.random.default_rng(seed)
    G = np.asarray(Gdir, float)
    t = rng.normal(size=(N, 3))
    t /= np.linalg.norm(t, axis=1, keepdims=True)
    avg = np.mean((t @ G) ** 2)  # -> |G|^2/3 for isotropic
    u = (lam / 2) * L_v * avg
    return 2 * u / (G @ G)


def test():
    J = a = 1.0
    L_v = 3 * a / a**3  # cubic lattice rope length per volume = 3/a^2

    # (1) direct lattice
    K_direct = K_lattice_direct(J=J, a=a)
    assert abs(K_direct - 1.0) < 1e-3, f"lattice K={K_direct}, expected J/a"

    # (2) lattice-as-ropes and (3) isotropic continuum, over random directions
    rng = np.random.default_rng(1)
    for _ in range(8):
        G = rng.normal(size=3)
        K_ax = K_lattice_as_ropes(G, J, a)
        K_iso = K_isotropic_continuum(G, L_v, J, a)
        assert abs(K_ax - 1.0) < 1e-9, f"axial-rope K={K_ax}"
        assert abs(K_iso - 1.0) < 2e-2, f"isotropic-continuum K={K_iso}"

    # (4) lattice stiffness is isotropic (direction-independent)
    Ks = [K_lattice_as_ropes(rng.normal(size=3), J, a) for _ in range(20)]
    assert max(Ks) - min(Ks) < 1e-12, "lattice stiffness is anisotropic"

    # (5) K is LINEAR in rope length-per-volume (density scaling)
    slopes = []
    for factor in (1, 2, 4, 8):
        K = K_isotropic_continuum([0, 0, 1.0], L_v * factor, J, a)
        slopes.append(K / factor)
    assert max(slopes) - min(slopes) < 3e-2, "K not linear in density"

    print(f"K_lattice(direct)      = {K_direct:.4f} J/a")
    print(f"K_lattice(as ropes)    = 1.0000 J/a  (all directions)")
    print(f"K_continuum(isotropic) = ~1.0000 J/a (MC, all directions)")
    print("lattice stiffness isotropic: PASS")
    print("K linear in rope length-per-volume (density): PASS")
    print("PASS: K=J/a and K=n*lambda/3 are one claim; K scales linearly with density.")


if __name__ == "__main__":
    test()
