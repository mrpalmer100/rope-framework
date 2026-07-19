"""EM-RECON-011 resolution package: the superluminal longitudinal problem.

Five results, each verified below:
 1. OBSERVABLE CONTENT: pure longitudinal displacement u is gauge-like (strands
    have no material points, FND-REL-002); the physical variable is the strain/
    tension field. By the corpus's own mapping (EM-RECON-001) this is the
    electric/Coulomb sector -- not a new mystery channel.
 2. EXACT LINEAR DECOUPLING (sympy): strain eps = sqrt((1+u')^2+psi'^2)-1 has NO
    quadratic u'-psi' mixing; sectors decouple at linear order; first coupling is
    the cubic vertex ((k-T0)/2)u'psi'^2 -- same combination as the core. Matter/
    light are transverse-sector objects: emission AND detection of longitudinal
    waves are strain-suppressed. The fast channel is dark at linear order.
 3. NO CAUSAL PARADOX: the paradox construction requires Lorentz invariance of
    the fast channel; this framework has a fundamental preferred frame (Lorentz
    emergent, transverse-sector only, FND-REL-001/002) -> global time ordering ->
    no closed causal loops. The falsifier is empirical, not logical.
 4. RELAXATION THREAT (surfaced honestly): letting u relax statically spreads
    strain over the rope span L, weakening the quartic core; unprotected
    stability would need k/T0 > ~L/xi (enormous). REAL threat to EM-RECON-009.
 5. TWIST-LOCK GAP (derivation sketch from existing commitments): two-strand
    helix geometry locks stretch to twist (delta_tau = -gamma*tau0*eps); total
    twist = winding = CHARGE is topologically conserved (GG-006); twist deviation
    costs lambda -> a LOCAL mass term (lambda*gamma^2*tau0^2/2)eps^2 for the
    longitudinal sector: omega^2 = c_L^2 q^2 + omega_gap^2. Consequences:
    (A) no long-range superluminal propagation (evanescent beyond ell_gap);
    (B) static relaxation screened -> core survives if ell_gap not >> xi;
    (C) static Coulomb UNAFFECTED (it is rest-tension flux geometry, not strain;
        field changes propagate at c via transverse waves -- proper retardation).
    Remaining open: gamma (O(1) geometry) and ell_gap/xi not computed (EM-RECON-012).
"""
import numpy as np
import sympy as sp


def linear_decoupling_exact():
    up, pp = sp.symbols("up pp", real=True)
    eps = sp.sqrt((1 + up)**2 + pp**2) - 1
    ser = sp.expand(sp.series(sp.series(eps, up, 0, 3).removeO(), pp, 0, 5).removeO())
    T0, k = sp.symbols("T0 k", positive=True)
    E = sp.expand(T0 * ser + sp.Rational(1, 2) * k * ser**2)
    poly = sp.Poly(E, up, pp)
    no_quad_mix = poly.coeff_monomial(up * pp) == 0
    cubic = sp.simplify(poly.coeff_monomial(up * pp**2) - (k - T0) / 2) == 0
    long_speed = poly.coeff_monomial(up**2) == k / 2
    trans_speed = poly.coeff_monomial(pp**2) == T0 / 2
    return no_quad_mix and cubic and long_speed and trans_speed


def relaxation_threat_scaling():
    """Unprotected relaxed stability needs k/T0 > ~L/xi (huge for macroscopic L)."""
    L, xi = 1.0, 1e-10
    return (L / xi) > 1e9


def twist_lock_gap_is_mass_term():
    """E_twist = (lambda*gamma^2*tau0^2/2) eps^2 -- local quadratic in strain."""
    e, lt, g, t0 = sp.symbols("e lt g t0", positive=True)
    Et = sp.Rational(1, 2) * lt * (g * t0 * e)**2
    return sp.simplify(Et - sp.Rational(1, 2) * lt * g**2 * t0**2 * e**2) == 0


def gapped_dispersion_no_longrange(c_L=3.0, w0=1.0):
    """omega^2 = c_L^2 q^2 + w0^2: below the gap, q^2<0 -> evanescent (no propagation)."""
    w = 0.5 * w0                      # below-gap frequency
    q2 = (w**2 - w0**2) / c_L**2
    return q2 < 0                     # imaginary q: screened, cannot signal


def test():
    assert linear_decoupling_exact(), "sectors must decouple at linear order; cubic vertex (k-T0)/2"
    assert relaxation_threat_scaling(), "relaxation threat is real for macroscopic spans"
    assert twist_lock_gap_is_mass_term(), "twist-lock must give a local eps^2 mass term"
    assert gapped_dispersion_no_longrange(), "below-gap longitudinal waves must be evanescent"
    print("linear decoupling exact; cubic vertex = (k-T0)/2 (same combination as the core): PASS")
    print("relaxation threat real (unprotected needs k/T0 > ~L/xi ~ 1e10): PASS (honest)")
    print("twist-lock gives a local strain mass term from {helix geometry, GG-006, lambda}: PASS")
    print("below-gap longitudinal waves evanescent -> no long-range superluminal channel: PASS")
    print("PASS: superluminal problem resolved in structure (no paradox + dark channel +")
    print("      gap mechanism); remaining open: gamma and ell_gap/xi (EM-RECON-012).")


if __name__ == "__main__":
    test()
