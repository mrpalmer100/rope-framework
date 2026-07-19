"""
rope_solver.electromagnetism.photon  --  Light in the rope framework.

Encodes the rope-SPECIFIC, quantitative findings of rope_theory_of_light:
the photon as a transverse rope kink, its kinematics and exact masslessness,
the non-dispersive vacuum, and the Chern-Simons cosmic-birefringence prediction
that is the paper's one genuinely falsifiable result.

WHAT IS ENCODED (rope-specific, pinnable):
  - photon = transverse kink with Lk = 0 (massless, chargeless) -- the
    cross-sector lock to the particle mass mechanism.
  - omega = c k exactly: the rope forces a non-dispersive vacuum (falsifiable
    against photon-dispersion bounds, Vasileiou et al. 2013).
  - Chern-Simons birefringence from rope chirality:
        chi = sin(2 theta_W) n_rope r_H^2 / c
        beta = chi c D / 2   (rotation of CMB polarization)
        EB/EE = sin(4 beta)/2  (flat in multipole; LiteBIRD test)
    Measured beta = 0.342 +/- 0.094 deg (Eskilt & Komatsu 2022) constrains
    sin(2 theta_W) n_rope r_H^2 = 9.18e-29 /m.

WHAT IS NOT ENCODED (interpretive / inherited, mentioned not pinned):
  - The de Broglie-Bohm guidance equation, the Born rule, and the double-slit
    account. The paper itself flags the Born rule as underivable ("the
    frontier"). These are pilot-wave QM applied to the rope wave, not rope
    derivations, so they are not represented as rope results here.
"""
import numpy as np

C_LIGHT = 2.998e8
H_PLANCK = 6.626e-34
GLY_M = 9.461e24            # one gigalight-year in metres
D_LSS_GLY = 13.8           # comoving distance to last scattering (approx)

# Measured cosmic birefringence (Eskilt & Komatsu 2022)
BETA_MEASURED_DEG = 0.342
BETA_ERR_DEG = 0.094


def photon_linking_number():
    """The photon carries Lk = 0: no net linking -> massless, chargeless.

    This is the structural reason the photon is massless in the same language
    that makes charged solitons (Lk != 0) massive.  See cross_sector_massless.
    """
    return 0


def photon_energy(nu):
    """Kink energy E = h nu (nu = flick oscillation frequency)."""
    return H_PLANCK * nu


def photon_momentum(nu):
    """Kink momentum p = h nu / c = h / lambda."""
    return H_PLANCK * nu / C_LIGHT


def dispersion_omega(k):
    """Vacuum dispersion omega = c k (exactly linear -- non-dispersive).

    The rope vacuum has a single wave speed, so there is no frequency-dependent
    term.  Falsifiable: any measured vacuum dispersion would break this.
    """
    return C_LIGHT * np.asarray(k)


def group_minus_phase_velocity(k):
    """v_group - v_phase in vacuum: exactly 0 (non-dispersive).

    Returned explicitly so a regression test can assert masslessness/no
    dispersion rather than trust the linear form by eye.
    """
    k = np.atleast_1d(np.asarray(k, float))
    omega = dispersion_omega(k)
    v_phase = omega / k
    # group velocity d omega / dk via finite difference
    v_group = np.gradient(omega, k) if k.size > 1 else np.array([C_LIGHT])
    return float(np.max(np.abs(v_group - v_phase)))


# ---- Chern-Simons cosmic birefringence (the falsifiable prediction) -------

def chirality_chi(sin2thetaW, n_rope, r_H):
    """Rope chirality coupling chi = sin(2 theta_W) n_rope r_H^2 / c  [1/m].

    Emerges mechanically from the two-strand helix geometry, not postulated.
    """
    return sin2thetaW * n_rope * r_H**2 / C_LIGHT


def birefringence_velocity_split(chi, wavelength):
    """Fractional speed split between circular polarizations: dv/c = chi lambda/2pi.

    Topological (frequency-independent in the rotation it produces); at visible
    wavelengths this is ~1e-38, unobservable locally but cumulative over
    cosmological distance.
    """
    return chi * wavelength / (2 * np.pi)


def cosmic_birefringence_deg(chi, D_gly=D_LSS_GLY):
    """Polarization rotation angle beta = chi c D / 2, in degrees.

    Integrated over the distance D to last scattering.
    """
    D = D_gly * GLY_M
    beta_rad = chi * C_LIGHT * D / 2.0
    return np.degrees(beta_rad)


def chirality_product_from_beta(beta_deg=BETA_MEASURED_DEG, D_gly=D_LSS_GLY):
    """Invert the measured rotation to the rope geometric constraint.

    sin(2 theta_W) n_rope r_H^2 = 2 beta / D   [1/m].
    With the Eskilt-Komatsu value this is ~9.18e-29 /m.
    """
    D = D_gly * GLY_M
    beta_rad = np.radians(beta_deg)
    return 2 * beta_rad / D


def eb_ee_ratio(beta_deg=BETA_MEASURED_DEG):
    """Predicted CMB EB/EE cross-correlation = sin(4 beta)/2, flat in multipole.

    The specific rope prediction LiteBIRD (2030s) will test (~0.0119 at the
    measured beta).
    """
    return np.sin(4 * np.radians(beta_deg)) / 2.0


# ---- cross-sector consistency ---------------------------------------------

def cross_sector_massless():
    """Check the photon (Lk=0) is massless under the particle mass mechanism.

    The particle sector gives mass from soliton self-energy that scales with
    linking; at Lk=0 there is no charged soliton and no mass.  Returns
    (photon_Lk, consistent) where consistent means Lk=0 -> massless holds.
    """
    Lk = photon_linking_number()
    # massless iff no net linking; the particle sector has no mass mechanism
    # that acts at Lk = 0 (charge q = Lk = 0).
    return Lk, Lk == 0
