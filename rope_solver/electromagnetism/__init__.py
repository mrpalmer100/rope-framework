"""
rope_solver.electromagnetism  --  Canonical EM sector of the rope theory.

This module makes executable the EM sector the rope programme derives
(rope_topological_maxwell, rope_maxwell_equations, rope_gem_equations), and
pushes two steps further:

  (a) the structural constant relations (eps0, mu0, Z0) as identities the rope
      model must satisfy, with the impedance Z0 = mu0 c expressed in rope form;
  (b) the cross-sector consistency conditions that tie EM to gravity and to the
      particle sector -- the same alpha must appear in the soliton coupling
      (kappa = alpha/2pi) and the EM fine structure (alpha = e^2 Z0 / 2h), and
      the EM wave speed must equal the gravitational wave speed (one rope, one
      speed).

WHAT IS GENUINELY ROPE-SPECIFIC (derived, not inherited):
  - charge quantization q = Lk: integer charge is topological (linking number),
    not imposed. Lives in rope_solver.topology; surfaced here as charge().
  - the single wave speed for EM and gravity: both propagate in one rope, so
    c_EM = c_GW is a consequence, not two separate postulates.

WHAT IS INHERITED FROM THE BUNDLE IDENTIFICATION (flagged honestly):
  - Dirac quantization e*g = 2*pi*n*hbar follows from identifying the physical
    EM U(1) bundle with the Hopf bundle of the winding-number field, then
    applying standard Chern-Weil. Given that identification (which the papers
    assert), it is automatic. We include it as a derived consequence, not a new
    independent result.

The four Maxwell equations themselves are derived structurally in the papers
(Bianchi identity -> homogeneous pair; Chern-Weil + Helmholtz in d=3 ->
inhomogeneous pair). Their derivation is symbolic/topological, not a numerical
field solve; maxwell_structure() records the derivation chain and the d=3
dependence rather than re-solving Maxwell on a grid (which would only reproduce
textbook EM and prove nothing about the rope theory).
"""
import numpy as np

# CODATA-ish reference values, single source of truth for this module.
C_LIGHT = 2.998e8
MU0 = 4 * np.pi * 1e-7
EPS0 = 1.0 / (MU0 * C_LIGHT**2)
E_CHARGE = 1.602e-19
H_PLANCK = 6.626e-34
HBAR = H_PLANCK / (2 * np.pi)
ALPHA = 1.0 / 137.036


def eps0_from_structure():
    """Vacuum permittivity from the structural identity eps0 = 1/(mu0 c^2).

    In the rope model c^2 = T0/mu_rope and the EM constants satisfy
    eps0 mu0 = 1/c^2, so eps0 is fixed once mu0 and c are.  Returns the SI
    value as a consistency check against 8.854e-12 F/m.
    """
    return 1.0 / (MU0 * C_LIGHT**2)


def impedance_of_free_space():
    """Vacuum impedance Z0 = sqrt(mu0/eps0) = mu0 c.

    A structural consequence of c^2 = 1/(eps0 mu0): the rope model predicts
    Z0 = mu0 c with no extra input.  Returns ohms (SI: 376.730).
    """
    return MU0 * C_LIGHT


def alpha_from_impedance():
    """Fine-structure constant from EM constants: alpha = e^2 Z0 / (2 h).

    Equivalent to alpha = e^2/(4 pi eps0 hbar c).  This is the EM-sector
    expression for alpha; it MUST equal the soliton-coupling alpha used in
    rope_solver.particles (kappa = alpha/2pi).  See consistency_with_particles.
    """
    return E_CHARGE**2 * impedance_of_free_space() / (2 * H_PLANCK)


def charge(C1, C2):
    """Quantized electric charge q = Lk (topological).

    Integer charge is a linking number, not an imposed quantum number.
    Delegates to the canonical linking-number implementation.
    """
    from rope_solver.topology.linking import linking_number
    return linking_number(C1, C2)


def dirac_quantization_n(e_charge, g_charge):
    """Dirac integer n = e*g/(2*pi*hbar) for electric e and magnetic g charges.

    Follows from identifying the EM U(1) bundle with the Hopf bundle
    (first Chern number 1) and requiring bundle consistency over S^2.
    INHERITED from the bundle identification, not an independent rope result.
    Returns n; bundle consistency requires n to be an integer.
    """
    return e_charge * g_charge / (2 * np.pi * HBAR)


def wave_speed_squared(T0, mu_rope):
    """EM (and gravitational) wave speed squared c^2 = T0/mu_rope.

    One rope carries both EM and gravitational waves, so this single speed
    serves both sectors -- the origin of c_EM = c_GW.
    """
    return T0 / mu_rope


def maxwell_structure():
    """Return the derivation chain of the four Maxwell equations (as recorded).

    Structural/topological derivation (rope_topological_maxwell), not a grid
    solve.  Each entry: (equation, origin).
    """
    return [
        ("div B = 0", "Bianchi identity dF=0 (homogeneous)"),
        ("curl E = -dB/dt", "Bianchi identity dF=0 (homogeneous)"),
        ("div E = rho/eps0", "Chern-Weil theorem (first Chern class = charge)"),
        ("curl B = mu0 J + mu0 eps0 dE/dt",
         "Chern-Weil + Helmholtz decomposition in d=3 (axiom A1)"),
    ]


def d3_is_essential():
    """Why d=3 is required (Helmholtz: div-free field = curl only in d=3).

    Returns a short structural statement; the Ampere-Maxwell law fails to
    follow in d=2 (div-free = gradient) or d=4 (needs extra topology).
    """
    return ("Ampere-Maxwell uses Helmholtz decomposition (div-free = curl), "
            "which holds universally only in d=3; axiom A1 (d=3) enters here.")


# ---- cross-sector consistency (the inter-paper guarantees) ----------------

def consistency_with_particles(rel_tol=1e-3):
    """Check the EM-sector alpha equals the particle-sector soliton alpha.

    alpha_from_impedance() (EM) must match the alpha behind kappa=alpha/2pi
    (particles).  Returns (alpha_em, alpha_particles, consistent).
    """
    from rope_solver.particles import ALPHA as ALPHA_P
    a_em = alpha_from_impedance()
    return a_em, ALPHA_P, abs(a_em - ALPHA_P) / ALPHA_P < rel_tol


def consistency_with_gravity(rel_tol=1e-9):
    """Check c_EM equals c used in the gravity sector (one rope, one speed).

    Returns (c_em, c_gravity, consistent).
    """
    from rope_solver.gravity import C_LIGHT as C_GRAV
    return C_LIGHT, C_GRAV, abs(C_LIGHT - C_GRAV) / C_GRAV < rel_tol


def consistency_with_chemistry(rel_tol=1e-3):
    """Check the atomic-mode equation uses the SAME eps0 as the EM sector.

    The rope chemistry paper builds the hydrogen mode equation on the Coulomb
    tension field V(r) = -e^2/(4 pi eps0 r).  That eps0 must be identical to
    the EM sector's, or the two papers would quote inconsistent atomic energies.
    Returns (E1_eV, consistent): the hydrogen ground-state energy computed from
    THIS module's eps0, and whether it matches the standard -13.6 eV.

    NOTE: -13.6 eV is standard quantum chemistry, NOT a rope-specific result.
    This is a cross-sector CONSISTENCY check (one eps0 across sectors), not a
    claim that the rope theory derives the hydrogen spectrum.
    """
    m_e = 9.109e-31
    E1_J = m_e * E_CHARGE**4 / (2 * HBAR**2 * (4 * np.pi * EPS0)**2)
    E1_eV = -E1_J / E_CHARGE
    return E1_eV, abs(E1_eV - (-13.6)) / 13.6 < rel_tol


# Magnetism sub-topic (rope_theory_of_magnetism) -- see magnetism.py
from rope_solver.electromagnetism.magnetism import (  # noqa: E402,F401
    ampere_flux_from_boundary_linking,
    minimal_texture_energy_selects_ampere,
    dipole_interaction_from_field_energy,
    energy_functional_form_is_forced,
    em_coefficient_from_stiffness,
    realizes_maxwell_phase,
    em_coefficient_microscopic,
    locking_energy_from_endpoint_mechanics,
    alpha_G_covariation_exponent,
)
