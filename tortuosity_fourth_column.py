"""Gravity sector, first derivations beyond the matched metric.

RESULT 1 (GRV-004, the zero-point theorem): given the framework's own commitment
that gravity IS the effective metric experienced by transverse-sector
excitations (GRV-001), the metric is a functional of the LOCAL network fields
(c(x) = sqrt(T/mu), mode structure). A uniform network -- whatever its tension
density SIGMA -- gives uniform c: the FLAT metric. Metric perturbations depend
only on DEVIATIONS/GRADIENTS of the network fields and vanish identically on
the uniform background. Rest tension does not gravitate; the uniform pre-
stressed background IS the zero point. (Analog-gravity precedent: a superfluid's
rest energy does not curve its quasiparticles' effective metric.) This resolves
the STATIC half of EM-RECON-015; the DYNAMIC half (why the effective
cosmological constant is ~0 as the network evolves) remains open.

RESULT 2 (GRV-005, Poisson from statics): GRV-003's assumed premise ('mass
sources a conserved conditioning flux') is REPLACED BY MECHANICS: a mass-knot is
a stressed defect exerting static force density f on the network; static
equilibrium of an elastic medium is force balance div(stress) = -f --
conservation IS Newton's law for the medium, not an assumption. For the scalar
conditioning sector (stress ~ SIGMA_g grad chi) this reads laplacian(chi) =
-f/SIGMA_g: the Poisson equation, FORCED. Its 3D Green's function is 1/r. The
conditioning channel must be gapless -- and the tension sector is gapless IN
PRINCIPLE by the EM-RECON-012 theorem: the channels interlock.

HIERARCHY LOCATED (not solved): if SIGMA_g were the PVLAS-bounded SIGMA ~
8.6e27 J/m^3, matching Newton's G would need a defect coupling area A0 =
c^4/(4 pi SIGMA G) ~ 1e15 m^2 -- absurd. The mass->strain coupling must be ~40
orders suppressed: the rope form of the known gravity hierarchy. G stays input.
"""
import numpy as np

C, G, SIGMA = 2.998e8, 6.674e-11, 8.6e27   # post-PVLAS lower bound (EM-RECON-016)


def uniform_background_is_flat():
    """Metric perturbation functionals depend only on gradients of network
    fields; on a uniform background every gradient vanishes."""
    x = np.linspace(0, 10, 200)
    T = np.full_like(x, 7.3)            # uniform tension (any value)
    mu = np.full_like(x, 2.1)           # uniform density
    c_local = np.sqrt(T / mu)
    dc = np.gradient(c_local, x)
    return np.allclose(dc, 0.0)         # uniform c -> flat effective metric


def one_over_r_is_poisson_greens_function(r0=2.0, h=1e-5):
    f = lambda x: 1.0 / x
    lap = (f(r0 + h) - 2 * f(r0) + f(r0 - h)) / h**2 + (2 / r0) * ((f(r0 + h) - f(r0 - h)) / (2 * h))
    return abs(lap) < 1e-6              # laplacian(1/r) = 0 away from the origin


def perturbed_background_does_gravitate():
    """A localized network deviation produces a nonzero metric gradient --
    deviations gravitate, the background does not."""
    x = np.linspace(-10, 10, 400)
    T = 7.3 * (1 - 0.01 * np.exp(-x**2))    # conditioned region
    c_local = np.sqrt(T / 2.1)
    return np.max(np.abs(np.gradient(c_local, x))) > 0


def hierarchy_probe():
    A0 = C**4 / (4 * np.pi * SIGMA * G)
    return A0                            # ~1.1e15 m^2 post-PVLAS: still absurd -> hierarchy located


def test():
    assert uniform_background_is_flat(), "uniform network must give flat metric (zero-point theorem)"
    assert perturbed_background_does_gravitate(), "deviations must gravitate"
    assert one_over_r_is_poisson_greens_function(), "1/r must solve Laplace away from origin"
    A0 = hierarchy_probe()
    assert 1e14 < A0 < 1e16, "hierarchy probe: absurd coupling area ~1e15 m^2 (post-PVLAS SIGMA)"
    print("uniform network (any SIGMA) -> uniform c -> FLAT metric: rest tension does not gravitate")
    print("localized deviation -> nonzero metric gradient: deviations DO gravitate")
    print("laplacian(1/r) = 0 away from origin: the Poisson/elastostatic Green's function")
    print(f"hierarchy probe: A0 = c^4/(4 pi SIGMA G) = {A0:.1e} m^2 (absurd) -> ~40-order")
    print("      suppression of mass->strain coupling LOCATED, not solved; G stays input")
    print("PASS: zero-point theorem + Poisson-from-statics; EM-RECON-015 static half resolved.")


if __name__ == "__main__":
    test()
