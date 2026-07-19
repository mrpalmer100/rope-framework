"""
rope_solver.electromagnetism.magnetism  --  Magnetism in the rope framework.

Encodes the rope-SPECIFIC, derived findings of rope_theory_of_magnetism (Section
4.5 and the 2026 microscopic work): magnetism as the surrounding network's
boundary-forced phase winding, obtained NOT as textbook reproduction but as a
candidate derivation from the rope ontology.

WHAT IS ENCODED (rope-specific, derived or pinnable):
  - Ampere's law from boundary phase-continuity: circ(A)=2*pi*Lk  (the enclosed
    current is the enclosed strand-linking number).
  - Energy minimization selecting the unique minimal exterior texture.
  - The dipole 1/r^3 law as the field-energy cross term (given the functional).
  - The energy functional FORM as EFT-constrained (uniquely selected in class).
  - The coefficient chain, derived to rope-medium primitives:
        J = T^2/kappa (EXACT, endpoint mechanics) -> K = 2J/a -> c = kappa a/(2T^2)
  - The Maxwell-vs-superfluid PHASE criterion: beta_eff = 2T^2/kappa > beta_c.
  - The cross-sector PREDICTION: correlated alpha-G variation (d ln alpha = -2 d ln G).

STATUS: the measurable content of magnetostatics is derived from boundary
continuity + energy minimization + the forced Hopf structure; the coefficient is
"derived to rope-medium primitives, not derived from nothing". See
open_problems 'EM-P2-linking-inheritance', 'em-energy-coefficient-c',
'alpha-G-correlated-variation'.
"""

import numpy as np

def ampere_flux_from_boundary_linking(Lk):
    """Ampere-level magnetism DERIVED from boundary phase-continuity (EM-P2, 2026).

    If the surrounding network's Hopf fiber phase must join the charged rope's
    internal winding continuously at the tube surface, a continuous phase field
    cannot jump its integer winding across the boundary. Hence the exterior
    fiber-phase winding around the tube equals the interior self-linking Lk
    (= charge), so by Stokes the circulation of the connection A around any
    enclosing loop is 2*pi*Lk and the B-flux through the tube is 2*pi*Lk.

    Returns (circ_A, flux_B), both = 2*pi*Lk. This is Ampere's law with
    enclosed current = enclosed linking number, obtained from CONTINUITY rather
    than postulated. Caveat: continuity fixes the flux (all measurable near-wire
    magnetism) but not the full 3D bulk Hopf integer uniquely; see open_problems
    'EM-P2-linking-inheritance'.
    """
    import numpy as np
    circ_A = 2.0 * np.pi * Lk
    flux_B = circ_A  # Stokes: circulation of A = flux of curl A = flux of B
    return circ_A, flux_B


def minimal_texture_energy_selects_ampere(Lk, extra_hopf_units=(0, 1, 2)):
    """Energy minimization removes the bulk-texture ambiguity (EM-P2, 2026).

    Given the boundary winding fixed to Lk (from phase-continuity), candidate
    exterior textures differ by extra bulk Hopf knottedness. Each extra unit
    adds a strictly positive Vakulenko-Kapitanskii energy floor (~|H|^{3/4}),
    so the energy minimizer carries NO extra bulk knots -> a unique minimal
    texture -> the standard Ampere field with circ(A)=2*pi*Lk.

    NOTE (corrected): the minimal texture for a straight wire has BULK Hopf
    number 0, not Lk; Lk is the BOUNDARY winding number (which sets the flux).
    Returns list of (extra_hopf_units, energy_per_length); the minimum is at 0.
    Assumes the standard Dirichlet+Faddeev energy form. See open_problems
    'EM-P2-linking-inheritance'.
    """
    import numpy as np
    r_in, r_out = 1.0, 50.0
    base = 2*np.pi*Lk**2*np.log(r_out/r_in)
    c_VK = 16*np.pi**2*(3/16)**(3/8)
    return [(h, base + c_VK*abs(h)**0.75) for h in extra_hopf_units]


def dipole_interaction_from_field_energy(m1, m2, sep):
    """Dipole-dipole interaction as the field-energy cross term (EM-P2, 2026).

    GIVEN the continuum rope-energy functional E = (1/2)*integral B^2, the
    interaction energy of two magnets is the cross term integral B1.B2 dV,
    which equals the standard dipole law (mu0/4pi units set to 1):
        U = [m1.m2 - 3 (m1.rhat)(m2.rhat)] / r^3.
    Reproduces both the 1/r^3 distance law and the angular factor (attraction
    head-to-tail, repulsion side-by-side, zero in the T-configuration).
    Conditional on the energy-functional assumption of Section 4.5; its FORM
    is EFT-constrained (see energy_functional_form_is_forced) but its
    coefficient is not derived. Returns U.
    """
    import numpy as np
    m1 = np.asarray(m1, float); m2 = np.asarray(m2, float); sep = np.asarray(sep, float)
    r = np.linalg.norm(sep); rhat = sep / r
    return (np.dot(m1, m2) - 3*np.dot(m1, rhat)*np.dot(m2, rhat)) / r**3


def energy_functional_form_is_forced():
    """Continuum energy FORM (1/2)|curl A|^2 is EFT-constrained (EM-P2, 2026).

    Any effective energy density that is (a) rotationally invariant, (b) gauge
    invariant [Hopf fibre = unobservable overall phase], and (c) quadratic in
    first derivatives must reduce at leading order to c|curl A|^2 = c|B|^2:
    div A is pure gauge, and the identity |grad A|^2 = |div A|^2 + |curl A|^2
    (up to a boundary term) leaves |curl A|^2 as the only gauge-invariant bulk
    term. Positivity c>0 follows from tension being restoring; the absence of a
    mass term m^2|A|^2 (giving short-range Yukawa instead of 1/r^3) follows from
    gauge invariance. EFT-CONSTRAINED (uniquely selected within the class of
    local, gauge-invariant, rotationally-invariant quadratic energies), NOT
    microscopically derived by coarse-graining; coefficient c not fixed.
    """
    return "c*|curl A|^2 (= c*|B|^2), c>0, no mass term"


def em_coefficient_from_stiffness(K):
    """EM energy coefficient c from the microscopic rope stiffness K (2026).

    Coarse-graining a microscopic rope (Frank) elasticity gives the orientation-
    angle energy (K/2)|grad theta|^2 (XY / superfluid-stiffness form), where K is
    a computable combination of the tension/bend/twist moduli. In 3D this is DUAL
    to a gauge theory (1/2K)|curl A'|^2, so the EM field-energy coefficient is
        c = 1/K.
    Thus c is a physical rope-medium modulus, not a free EFT constant. CAVEAT:
    reproducing Maxwell (and the 1/r^3 dipole law) requires the network to realize
    the DUAL/Maxwell phase (physical B ~ curl A'); the alternative superfluid phase
    (physical field ~ grad theta) gives logarithmic, not dipole, defect forces.
    That phase selection is the remaining open question. Returns c = 1/K.
    """
    if K <= 0:
        raise ValueError("stiffness K must be positive")
    return 1.0 / K


def realizes_maxwell_phase(defect_core_energy, condensation_threshold):
    """Does the rope network sit in the Maxwell (massless-photon) phase? (2026)

    The coarse-grained rope network is a 3D XY / compact-U(1) system. Long-range
    Maxwell magnetism = the deconfined COULOMB phase, where the (dual) photon is
    massless. That phase is realized iff vortex/monopole defects do NOT condense,
    i.e. the defect core energy is above the monopole-condensation threshold
    (the ropes resist making defects). Below threshold, monopoles condense, the
    photon acquires a mass, and magnetism becomes short-range (Yukawa) -- not
    observed. Near threshold the theory predicts a small photon mass: a
    falsifiable deviation from Maxwell.

    Returns dict with the phase and a crude 'margin' (how far above threshold).
    NOTE: whether a given microscopic rope model is above threshold has NOT been
    computed from first principles; observation (massless photon) implies it is.
    See open_problems 'em-energy-coefficient-c'.
    """
    above = defect_core_energy > condensation_threshold
    margin = defect_core_energy - condensation_threshold
    return {
        "phase": "Maxwell (Coulomb, massless photon)" if above
                 else "confined (photon massive, short-range) -- NOT observed",
        "long_range_magnetism": bool(above),
        "margin_above_threshold": margin,
    }


def em_coefficient_microscopic(strand_tension, bond_stiffness, rope_spacing):
    """EM energy coefficient c from microscopic rope primitives (2026).

    Coarse-graining a lattice-XY orientation-locking model gives K = 3J/a with
    J the per-link orientation-locking energy; computing J from shared-atom bond
    strain gives J = T^2/kappa (T = strand tension, kappa = shared-atom bond
    stiffness). Hence:
        K = 2 T^2 / (kappa a),    c = 1/K = kappa a / (2 T^2),
        beta_eff ~ K a = 2 T^2 / kappa   (dual coupling for the phase question).
    The Maxwell (Coulomb) phase requires beta_eff > beta_c ~ 1, i.e. T^2 > kappa/2
    -- stiff, high-tension ropes, consistent with the gravity sector's tension T.
    Returns dict(K, c, beta_eff, maxwell_phase). STATUS: 'derived to rope-medium
    primitives; not derived from nothing'. J = T^2/kappa is now EXACT from endpoint
    mechanics (harmonic regime); the coefficient rests on substrate primitives
    T, kappa, a, constrained by observation only in combination. See open_problems
    'em-energy-coefficient-c'.
    """
    T, kappa, a = strand_tension, bond_stiffness, rope_spacing
    if T <= 0 or kappa <= 0 or a <= 0:
        raise ValueError("T, kappa, a must be positive")
    J = T**2 / kappa
    # Coefficient corrected (2026-07-04) from K = 3J/a to K = 2J/a per the
    # Microscopic Mechanics Factor-of-Three Audit: direct coarse-graining
    # (analytic + lattice simulation) gives K = J/a (scalar) or 2J/a (two-mode
    # director). The factor 3 was not reproducible and is withdrawn.
    K = 2*J / a
    c = 1.0 / K
    beta_eff = K * a  # = 2 T^2/kappa
    return {"J": J, "K": K, "c": c, "beta_eff": beta_eff,
            "maxwell_phase": beta_eff > 1.01}


def locking_energy_from_endpoint_mechanics(F, kappa, dtheta):
    """Exact misalignment (locking) energy from endpoint force-balance (2026).

    A shared atom pulled by two rope imbalance-forces of magnitude F at relative
    angle dtheta, held by a harmonic bond of stiffness kappa, minimized over the
    atom position, gives EXACTLY:
        E(dtheta) - E(0) = (F^2/kappa) * (1 - cos dtheta).
    So the XY locking form is exact (not assumed) and J = F^2/kappa = T^2/kappa
    exactly in the harmonic regime (F = strand tension T). Anharmonic bond terms
    add small force-dependent corrections ~ g F^4 (cos^4(dtheta/2)-1)/kappa^4.
    Returns the misalignment energy. See open_problems 'em-energy-coefficient-c'.
    """
    import numpy as np
    if kappa <= 0:
        raise ValueError("kappa must be positive")
    return (F**2 / kappa) * (1 - np.cos(dtheta))


def alpha_G_covariation_exponent(channel="tension"):
    """Scale-free prediction: correlated drift of alpha and G (2026).

    With alpha ~ 2 T^2/(kappa a) (EM coefficient) and G ~ 1/(T a) (natural rope
    gravity-rigidity scaling), a drift in a shared primitive forces alpha and G
    to co-vary in a fixed, scale-free ratio R = dln(alpha)/dln(G):
        tension T drift   -> R = -2   (alpha_dot/alpha = -2 G_dot/G)
        spacing a drift   -> R = +1
        kappa drift       -> G fixed, alpha moves (R -> infinite)
    Forced (not tuned) and falsifiable against varying-constants data. CAVEAT:
    the number depends on G ~ 1/(T a), the gravity relation NOT yet derived to
    the EM sector's rigor; the STRUCTURE (fixed-ratio co-variation) is robust,
    the NUMBER is provisional. See open_problems 'alpha-G-correlated-variation'.
    """
    return {"tension": -2.0, "spacing": 1.0, "kappa": float("inf")}[channel]
