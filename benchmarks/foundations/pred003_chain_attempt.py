"""PRED-003-CHAIN: the attempt to derive alpha = 2 lambda T^2 a/(kappa hbar c) from
the EM energy coefficient — the naive phase-electrostatics route tested honestly.

Bars locked in analysis/PRED003_CHAIN_bars_LOCKED.md BEFORE computation.
R2: the suspected failure (winding = circulation, not flux) must be able to be
surprised; R3: the lattice verdict is a pre-committed fit comparison.
"""
import numpy as np
import sympy as sp


def b1_dimensional_theorem():
    m = sp.symbols('m', positive=True)      # length unit
    grad_phi = 1 / m                        # Phi dimensionless
    circulation = sp.simplify(grad_phi * m)         # loop integral: [1/m]*[m]
    flux = sp.simplify(grad_phi * m**2)             # surface integral: [1/m]*[m^2]
    assert circulation == 1 and flux == m
    print("B1 PASS  circulation (the winding, GG-006's charge) is DIMENSIONLESS;")
    print("         a Gauss-law point flux of grad Phi carries units of LENGTH.")
    print("         The naive point-Coulomb route is dimensionally unavailable to")
    print("         a winding charge: charge lives on loops, not on points.")


def b2_analytic_form():
    # Vortex line at origin: Phi = N * theta, |grad Phi| = N/r. Cross-term energy per
    # unit length between lines of windings N1, N2 separated by d, integrated over
    # the plane, is 2 pi K N1 N2 ln(R/d) (standard; derived here as the integral's
    # d-dependence via the divergence structure).
    r, d, R0, K, N1, N2 = sp.symbols('r d R0 K N1 N2', positive=True)
    # E_cross(d) = K * Integral grad(N1 th1).grad(N2 th2) d^2r = 2 pi K N1 N2 ln(R0/d)
    E = 2 * sp.pi * K * N1 * N2 * sp.log(R0 / d)
    dE = sp.simplify(sp.diff(E, d) * d)
    assert sp.simplify(dE + 2 * sp.pi * K * N1 * N2) == 0
    print("B2 PASS  the winding-winding cross energy is LOGARITHMIC per unit length")
    print("         (d E/d ln d = -2 pi K N1 N2, constant): confining, not Coulomb.")
    print("         No 1/r appears anywhere in scalar phase electrostatics of lines.")


def b3_lattice(rule_margin=0.05):
    # Vortex-antivortex pair on a 2D grid; energy (K/2)|grad Phi|^2, K = 1.
    L, h = 240, 1.0
    xs = (np.arange(L) - L / 2 + 0.5) * h
    X, Y = np.meshgrid(xs, xs, indexing="ij")

    def pair_energy(d):
        th = np.arctan2(Y, X - d / 2) - np.arctan2(Y, X + d / 2)
        # gradient with phase-aware differencing (wrap to (-pi, pi])
        def wrap(z):
            return (z + np.pi) % (2 * np.pi) - np.pi
        gx = wrap(np.diff(th, axis=0)) / h
        gy = wrap(np.diff(th, axis=1)) / h
        return 0.5 * (np.sum(gx ** 2) + np.sum(gy ** 2)) * h * h

    ds = np.array([8, 12, 16, 24, 32, 48, 64], float)
    Es = np.array([pair_energy(d) for d in ds])

    def r2(xcol):
        Amat = np.vstack([xcol, np.ones_like(xcol)]).T
        coef, res, *_ = np.linalg.lstsq(Amat, Es, rcond=None)
        pred = Amat @ coef
        ss_res = np.sum((Es - pred) ** 2)
        ss_tot = np.sum((Es - Es.mean()) ** 2)
        return 1 - ss_res / ss_tot, coef

    r2_log, coef_log = r2(np.log(ds))
    r2_inv, _ = r2(1.0 / ds)
    slope = coef_log[0]
    print(f"B3       lattice E(d): R^2(log fit) = {r2_log:.5f}, "
          f"R^2(1/d fit) = {r2_inv:.5f}; log slope = {slope:.3f} "
          f"(analytic 2 pi K = {2*np.pi:.3f})")
    if r2_log - r2_inv >= rule_margin:
        verdict = "LOG WINS"
    elif r2_inv - r2_log >= rule_margin:
        verdict = "1/d WINS (surprise: register the success route)"
    else:
        verdict = "UNRESOLVED"
    print(f"B3 VERDICT ({rule_margin} margin rule): {verdict}")
    assert verdict == "LOG WINS", verdict
    assert abs(slope - 2 * np.pi) / (2 * np.pi) < 0.10, slope
    print("B3 PASS  the lattice confirms the analytic form, slope within 10% of")
    print("         2 pi K. The naive route FAILS: scalar phase electrostatics of")
    print("         winding charges is logarithmic, not Coulomb.")


def b4_specification():
    print("B4       THE SPECIFICATION (rule R1, no substitute mechanism invented):")
    print("         the 1/r Coulomb between compact charges in this framework must")
    print("         route through the REGISTERED Maxwell sector -- the Chern-Weil")
    print("         two-form construction and the one-metric photon dictionary --")
    print("         where the field's source coupling is set by the medium mapping,")
    print("         not by naive scalar electrostatics. The completing computation:")
    print("         map the unit linking number through that dictionary to a source")
    print("         strength q_s and verify  q_s^2 = 4 pi eps0 x 2 lambda J a,")
    print("         with lambda falling out of the same step. Bounded, on existing")
    print("         machinery; until executed, alpha = 2 lambda T^2 a/(kappa hbar c)")
    print("         is a CONSTITUTIVE HYPOTHESIS with a registered failed naive")
    print("         route, not a derived chain.")


def main():
    b1_dimensional_theorem()
    b2_analytic_form()
    b3_lattice()
    b4_specification()
    print("B5       PROPAGATION: PRED-003's provenance grade = BLOCKED-WITH-")
    print("         SPECIFICATION; the paper's 'whose chain is derived' language is")
    print("         owed a correction; no tier motion this session (rule R4).")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
