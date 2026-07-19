"""
rope_solver.particles  --  Canonical particle-sector quantities.

Charge as linking number, the coupling identification, and the higher-link
spectrum.  Every particle-physics number across the rope papers should come
from here.

KEY PRIOR RESULTS:
  - charge q = Lk (topological), confirmed by relaxation conservation.
  - model coupling kappa = alpha/(2 pi), via the Planck relation T0 L_Pl^2 = hbar c.
  - higher links (Lk>=2) exist, conserve topology, and cost SUB-linearly in
    charge (E ~ Lk^0.08): compact co-wound configs, not n copies.
  - the absolute electron mass is NOT one-loop (see rope_solver.spectrum);
    dimensional transmutation gives the right order but not a universal coeff.
"""
import numpy as np

ALPHA = 1.0 / 137.036


def kappa_from_alpha():
    """Model coupling kappa = alpha/(2 pi).

    Dimensional identification (rope_alpha_higher_links): the field self-energy
    carries alpha; the 2 pi is loop geometry; T0 L_Pl^2 = hbar c closes it.
    Honest caveat: at this coupling the soliton is compact (R < lambda_c),
    outside the thin-ring regime -- no numerical R* is claimed there.
    """
    return ALPHA / (2 * np.pi)


def dimensional_transmutation_b(mass_ratio):
    """Beta-function coefficient b for m = M_Pl exp(-2 pi /(b alpha)).

    Given mass_ratio = m / M_Pl (e.g. m_e/M_Pl), return the b that reproduces
    it.  For the electron b ~ 17; for mu, tau b differs (~18.6, 19.9), so the
    coefficient is NOT universal -- the absolute scale remains open.
    """
    S = -np.log(mass_ratio)
    return (2 * np.pi / S) / ALPHA


def charge_is_linking_number(C1, C2):
    """Return the topological charge q = Lk of a two-strand configuration."""
    from rope_solver.topology.linking import linking_number
    return linking_number(C1, C2)


def higher_link_energy_scaling(Lk_values, energies):
    """Fit E ~ Lk^p and return p.

    Prior result: p ~ 0.08 (strongly sub-linear) -- higher-charge solitons
    reuse rope structure rather than stacking copies.
    """
    Lk = np.asarray(Lk_values, float)
    E = np.asarray(energies, float)
    return float(np.polyfit(np.log(Lk), np.log(E), 1)[0])


# ---- lepton mass ratios via the Koide phase (CONJECTURE, see open_problems) --

GOLDEN_RATIO = (1 + 5**0.5) / 2


def quantum_dimension_su2k(j2, k):
    """Quantum dimension d_j = sin((2j+1)pi/(k+2)) / sin(pi/(k+2)) for SU(2)_k.

    j2 = 2j (so j2=1 means spin-1/2). RIGOROUS: standard Reshetikhin-Turaev
    TQFT. At k=3, d_{1/2} = 2cos(pi/5) = golden ratio exactly.
    """
    import numpy as np
    n = j2 + 1
    return np.sin(n * np.pi / (k + 2)) / np.sin(np.pi / (k + 2))


def koide_phase_coefficient():
    """The (3 + Phi) coefficient of phi = (3+Phi) theta_W.

    D = 3 * d_0 + 1 * d_{1/2} at CS level k=3.  The d_{1/2}=Phi part is
    rigorous; the 3+1 T-parity mode count is CONJECTURAL (the T-oddness of
    the fiber mode is unproven -- see open_problems 'koide-phase-t-parity').
    """
    return 3 * quantum_dimension_su2k(0, 3) + 1 * quantum_dimension_su2k(1, 3)


def lepton_mass_ratios(sin2_thetaW=0.23122):
    """Predicted (m_mu/m_e, m_tau/m_e, m_tau/m_mu) from Koide + phi=(3+Phi)theta_W.

    CONTINGENT on the supplied Weinberg angle. With the MEASURED value
    (default) the ratios match experiment to ~0.5%. With the rope's own
    sin^2 theta_W = 1/(3 sqrt2) the hypersensitivity makes them wildly wrong
    -- this is NOT yet a parameter-free prediction (see open_problems).
    Returns a dict of ratios.
    """
    import numpy as np
    theta_W = np.arcsin(np.sqrt(sin2_thetaW))
    phi = koide_phase_coefficient() * theta_W
    m = sorted(abs((1 + np.sqrt(2) * np.cos(phi + 2 * np.pi * k / 3))**2)
               for k in range(3))
    return {"mu/e": m[1] / m[0], "tau/e": m[2] / m[0], "tau/mu": m[2] / m[1]}


def chiral_central_charge(k):
    """Chiral central charge c = 3k/(k+2) of SU(2)_k Chern-Simons theory.

    RIGOROUS (textbook TQFT). c != 0 is exactly the statement that the theory
    breaks time reversal: T maps level +k to -k. For k=3, c = 9/5.

    This is the rigorous route to the T-oddness of the helical fiber mode in
    the Koide-phase derivation: the chiral framing phase exp(2 pi i c/24) it
    carries is T-odd because c != 0. It replaces the two FAILED prior arguments
    (helicity and mutual linking number, both T-even). See open_problems
    'koide-phase-t-parity': this upgrades the T-oddness from unproven to
    resting on a theorem, but does NOT close the full derivation (the j=1/2
    sector assignment and k=3 postulate remain).
    """
    return 3 * k / (k + 2)


def breaks_time_reversal(k):
    """True iff SU(2)_k Chern-Simons breaks time reversal (chiral c != 0)."""
    return abs(chiral_central_charge(k)) > 1e-12


def knot_euclidean_action_planck_units():
    """The rope knot's natural Euclidean action, in Planck units.

    S_E ~ M_Pl c L_Pl / hbar = 1 exactly (Planck units). RIGOROUS structural
    result: a simple knot (Hopf link, crossing number 2) has O(1) action, so
    it gives an M_Pl-scale mass. The electron's exp(-51.5) suppression therefore
    CANNOT be internal to the knot -- it must come from coupling to the
    cosmological background. See open_problems 'electron-absolute-mass'.
    """
    return 1.0


def mass_suppression_is_internal():
    """Can the electron mass suppression come from the knot itself? No.

    Returns False: the knot action is O(1) and its topology O(1) complexity,
    insufficient for exp(-51.5). The suppression is provably external (the
    knot-cosmos coupling). This is a structural finding, not a fit.
    """
    return False


# ---- tension beta function (mass-scale route, closed: see open_problems) -----

def luscher_critical_scale_planck(D=4):
    """Scale where the worldsheet effective tension vanishes, in Planck units.

    T_eff(R) = T_0 - (D-2)*pi/(24 R^2) = 0  =>  R_crit = sqrt((D-2)pi/24).
    POWER-LAW running (Luscher/Alvarez) gives an O(1) critical scale, NOT an
    exponential hierarchy. For D=4: R_crit ~ 0.51 L_Pl. This is why worldsheet
    tension running cannot produce the electron mass scale.
    """
    import numpy as np
    return np.sqrt((D - 2) * np.pi / 24.0)


def wzw_beta_function(k):
    """Beta function of the rope's SU(2)_k WZW-type dimensionless sector.

    Returns 0.0 exactly: WZW models are conformal fixed points (beta = 0). A
    theory at a fixed point does NOT run logarithmically, so it CANNOT generate
    an exponential mass hierarchy by dimensional transmutation. This closes the
    dimensional-transmutation route for the absolute mass scale "by structure"
    (not merely "b isn't universal"). See open_problems 'mass-tension-beta'.
    """
    return 0.0


def dimensional_transmutation_works():
    """Can the rope generate the mass hierarchy by running its own coupling? No.

    The tension running is power-law (luscher_critical_scale_planck -> O(1)) and
    the dimensionless sector is at a conformal fixed point (wzw_beta_function=0).
    Neither runs logarithmically, so dimensional transmutation cannot produce
    the exp(-51.5) electron suppression. The scale must come from EXPLICIT
    conformal-symmetry breaking (the cosmological/IR scale), not internal running.
    """
    return False


def hubble_planck_mass_exponent(H0_km_s_Mpc=70.0, two_pi_convention=False):
    """Required exponent p in m_e = M_Pl * (m_H / M_Pl)**p.

    p = ln(M_Pl/m_e) / ln(M_Pl/m_H) with m_H = hbar*H0/c^2 (or /2pi if
    two_pi_convention). Numerically p ~ 0.3674, but note the IR-mass
    CONVENTION shifts p by ~1.3% -- far more than the H0 uncertainty
    (~0.06%) -- so any claimed coincidence sharper than ~1% in p is
    convention noise. Hypersensitivity: d(ln m)/dp ~ 140, so predicting
    m_e to 15% requires p to <0.1%. See open_problems
    'electron-absolute-mass' (Fable-5 pass, 2026).
    """
    import numpy as np
    me, MPl = 9.1093837015e-31, 2.176434e-8
    hbar, c, Mpc = 1.054571817e-34, 2.99792458e8, 3.086e22
    H0 = H0_km_s_Mpc * 1000.0 / Mpc
    mH = hbar * H0 / c**2 / (2.0 * np.pi if two_pi_convention else 1.0)
    return np.log(MPl / me) / np.log(MPl / mH)


def su2k3_dressing_scan():
    """Scan the SU(2)_3 CFT's natural pure numbers against the required p.

    Tests whether IR dressing of the knot mass operator by the framework's
    own conformal data (primary weights h_j = j(j+1)/5, dimensions 2h,
    central-charge combos, simple rationals) can supply the exponent p.
    Returns (min_gap_percent, best_name). Result: minimum gap ~2% vs the
    <0.1% hypersensitivity bar -- anomalous-dimension dressing by the
    framework's own CFT spectrum is CLOSED as the mass mechanism. (1/e at
    0.14% is excluded separately: it holds under only one IR convention,
    fails the 2pi convention by 1.4%, and has no mechanism.)
    """
    p = hubble_planck_mass_exponent()
    cands = {"h_1/2": 3/20, "h_1": 2/5, "h_3/2": 3/4, "D_1/2": 0.3,
             "D_1": 0.8, "c/5": 0.36, "c/24": 1.8/24, "D_3/2_over_4": 0.375,
             "1/(k+2)": 0.2, "k/(k+2)": 0.6, "1/3": 1/3, "3/8": 0.375}
    gaps = {k: abs(v - p)/p*100 for k, v in cands.items()}
    best = min(gaps, key=gaps.get)
    return gaps[best], best
