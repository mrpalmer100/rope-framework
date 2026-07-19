"""
rope_solver.gravity  --  Canonical weak-field / PPN observables.

Every gravity number cited across the rope papers (gamma, beta, Mercury
perihelion, light deflection, Shapiro/Cassini, Nordtvedt) must come from here,
so no two papers can quote inconsistent values.

The rope effective metric (rope_effective_metric, rope_nonlinear_action) is, in
isotropic form:
    g_tt = -[(2 - psi)/psi]^2 ,   g_ij = psi^4 delta_ij ,   psi = 1 + r_s/(4r)
which is exactly isotropic Schwarzschild.  Its PPN parameters are therefore
gamma = beta = 1, and the classical tests take their GR values.  This module
computes them from the metric expansion rather than asserting them, so a
regression test can catch any drift.
"""
import numpy as np

# Physical constants (SI), single source of truth for the package.
G = 6.674e-11
C_LIGHT = 2.998e8
M_SUN = 1.989e30
AU = 1.496e11


def ppn_parameters():
    """Return (gamma, beta) of the rope effective metric.

    Derived from the isotropic metric expansion:
      -g_tt = 1 - 2U + 2*beta*U^2 + ...        (U = GM/rc^2)
       g_ij = (1 + 2*gamma*U) delta_ij + ...
    For psi = 1 + U (isotropic), g_tt = -[(2-psi)/psi]^2, g_ij = psi^4.
    """
    import sympy as sp
    # PPN potential u = GM/(r c^2). The ISOTROPIC conformal factor is
    # psi = 1 + u/2 (the factor of 1/2 is essential: isotropic Schwarzschild
    # is g_tt=-[(1-m/2r)/(1+m/2r)]^2, g_ij=(1+m/2r)^4 with m=GM/c^2).
    u = sp.symbols("u", positive=True)
    psi = 1 + u / 2
    g_tt = -((2 - psi) / psi)**2          # = -[(1 - u/2)/(1 + u/2)]^2
    g_ij = psi**4
    # PPN: -g_tt = 1 - 2u + 2*beta*u^2 + ... ;  g_ij = 1 + 2*gamma*u + ...
    minus_gtt = sp.series(-g_tt, u, 0, 3).removeO()
    beta = sp.nsimplify(minus_gtt.coeff(u, 2) / 2)
    gij = sp.series(g_ij, u, 0, 2).removeO()
    gamma = sp.nsimplify(gij.coeff(u, 1) / 2)
    return float(gamma), float(beta)


def mercury_perihelion_arcsec_per_century():
    """Perihelion advance of Mercury (arcsec/century) from PPN.

    Delta phi = (2 + 2 gamma - beta)/3 * 6 pi GM / (a (1-e^2) c^2) per orbit.
    """
    gamma, beta = ppn_parameters()
    a = 0.387 * AU
    e = 0.2056
    factor = (2 + 2 * gamma - beta) / 3.0
    per_orbit = factor * 6 * np.pi * G * M_SUN / (a * (1 - e**2) * C_LIGHT**2)
    arcsec = np.degrees(per_orbit) * 3600
    orbits_per_century = 100 * 365.25 / 87.969
    return arcsec * orbits_per_century


def light_deflection_arcsec():
    """Solar limb light deflection (arcsec): (1+gamma)/2 * 4GM/(R_sun c^2)."""
    gamma, _ = ppn_parameters()
    R_sun = 6.96e8
    rad = (1 + gamma) / 2.0 * 4 * G * M_SUN / (R_sun * C_LIGHT**2)
    return np.degrees(rad) * 3600


def nordtvedt_eta():
    """Nordtvedt parameter eta = 4 beta - gamma - 3 (zero in GR and here)."""
    gamma, beta = ppn_parameters()
    return 4 * beta - gamma - 3


def shapiro_gamma():
    """The gamma that sets Shapiro/Cassini time delay (Cassini: gamma-1 ~ 2e-5)."""
    gamma, _ = ppn_parameters()
    return gamma


# ---- cosmic closure relation (G source; see open_problems) ------------------

def cosmic_closure_ratio(H0_km_s_Mpc=70.0, G=6.674e-11, c=2.998e8):
    """Mach/Dirac closure ratio  G M / (R c^2)  for the observable universe.

    With R = c/H0 (Hubble radius) and M = critical-density mass inside the
    Hubble volume, this returns 1/2 exactly: the observable universe sits at
    its own Schwarzschild radius. This is the POSITIVE result behind the
    expansion-tension idea for the origin of G (open_problems
    'absolute-G-cosmic-tension'): G, R, M, c are locked as G = (1/2) R c^2 / M.

    It does NOT yield G's absolute value, because the mass M is itself defined
    through G (critical density carries G); every G-free route to a cosmic mass
    fails at the count/rate/ratio -> mass step. So this ratio is a consistency
    relation, not a derivation of G.
    """
    import numpy as np
    Mpc = 3.086e22
    H0 = H0_km_s_Mpc * 1000.0 / Mpc
    R = c / H0
    rho_c = 3.0 * H0**2 / (8.0 * np.pi * G)
    M = rho_c * (4.0 / 3.0) * np.pi * R**3
    return G * M / (R * c**2)
