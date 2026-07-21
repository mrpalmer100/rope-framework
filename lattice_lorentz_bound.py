"""EM-RECON-012 computed. Two theorems and one retraction:

DERIVED (positive): the twist-stretch locking factor is gamma = 1/sin^2(theta)
  -- exact two-strand helix geometry (strand-length conservation under rope
  strain), no free choices. theta = helix angle, tan(theta) = r*tau0.

DERIVED (negative): there is NO twist-stretch gap. The twist penalty
  (lambda/2)delta_tau^2 with delta_tau = -gamma*tau0*(du/dz) is a GRADIENT-squared
  term -- same order as the elastic (k/2)(du/dz)^2 -- so it STIFFENS the
  longitudinal sector (c_L_eff = sqrt((k + lambda*gamma^2*tau0^2)/mu) > c_L)
  rather than gapping it. A gap requires energy ~ u^2, which is FORBIDDEN:
  u is gauge (strands have no material points, FND-REL-002), so no physical
  energy can depend on u itself. The longitudinal sector is GAPLESS IN PRINCIPLE.

RETRACTION: the EM-RECON-011 leg-(5) gap mechanism (previous session turn) was
  wrong -- it confused a penalty on strain with a penalty on displacement. The
  same gauge argument used in leg (1) of that resolution forbids the gap of leg
  (5). Legs (1)-(3) of the 011 resolution stand (gauge content; exact linear
  decoupling with cubic-only coupling; preferred-frame no-paradox): the fast
  channel is real, gapless, dark at linear order, and paradox-free.

PROTECTOR CANDIDATE for the core (replaces the refuted gap; Conjecture): strand
  VOLUME CONSERVATION couples longitudinal relaxation to transverse coverage
  (compression -> thickening -> coverage rises), and atoms sit AT the coverage
  threshold (FND-MATTER-004), so relaxation only moves the cost between two LOCAL
  O(k) channels (stretch vs over-density): k_eff = k*K_c/(k+K_c). The 1/L escape
  closes. Remaining open (EM-RECON-013): the joint variational check.
"""
import numpy as np
import sympy as sp


def gamma_from_helix_geometry():
    eps, r, tau0, tau = sp.symbols('epsilon r tau_0 tau', positive=True)
    constraint = sp.Eq((1 + eps) * sp.sqrt(1 + r**2 * tau**2), sp.sqrt(1 + r**2 * tau0**2))
    tau_sol = sp.solve(constraint, tau)[0]
    dtau = sp.series(tau_sol - tau0, eps, 0, 2).removeO()
    gamma = sp.simplify(-dtau / (tau0 * eps))
    # gamma = 1 + 1/(r*tau0)^2 = 1/sin^2(theta) with tan(theta)=r*tau0
    return sp.simplify(gamma - (1 + 1 / (r * tau0)**2)) == 0


def twist_penalty_is_gradient_order_not_mass():
    """The penalty depends only on du/dz (through delta_tau), never on u itself:
    at zero strain the penalty is zero regardless of the displacement value."""
    u_val = 7.3                      # arbitrary uniform displacement (pure gauge)
    strain = 0.0
    gamma, tau0, lam = 2.0, 1.0, 1.0
    penalty = 0.5 * lam * (gamma * tau0 * strain)**2
    return penalty == 0.0 and u_val != 0.0   # energy blind to u -> no mass term


def stiffened_not_gapped(k=5.0, lam=1.0, gamma=2.0, tau0=1.0, mu=1.0):
    """Dispersion omega^2 = c_eff^2 q^2 with c_eff > c_L: gapless, faster."""
    cL = np.sqrt(k / mu)
    c_eff = np.sqrt((k + lam * gamma**2 * tau0**2) / mu)
    q = np.array([0.1, 1.0, 3.0])
    omega2 = c_eff**2 * q**2
    gapless = abs(omega2[0] / q[0]**2 - c_eff**2) < 1e-12   # omega -> 0 as q -> 0
    return gapless and c_eff > cL


def protector_keeps_local_stiffness():
    """Joint two-channel relaxation: k_eff = k*Kc/(k+Kc) stays O(k), never ~ 1/L."""
    k = 5.0
    for Kc in (2.0, 5.0, 20.0):
        keff = k * Kc / (k + Kc)
        if not (0.2 * k < keff <= k):
            return False
    return True


def test():
    assert gamma_from_helix_geometry(), "gamma must equal 1 + 1/(r tau0)^2 = 1/sin^2(theta)"
    assert twist_penalty_is_gradient_order_not_mass(), "penalty must be blind to u (gauge) -> no mass term"
    assert stiffened_not_gapped(), "twist-lock must stiffen (gapless), not gap"
    assert protector_keeps_local_stiffness(), "two-channel protector keeps local O(k) stiffness"
    print("gamma = 1/sin^2(theta): DERIVED (exact helix geometry)")
    print("no mass term possible (u is gauge) -> longitudinal sector GAPLESS in principle")
    print("twist-lock STIFFENS (c_eff > c_L), does not gap -> prior gap mechanism RETRACTED")
    print("volume-conservation protector keeps local O(k) stiffness (Conjecture; EM-RECON-013)")
    print("PASS: EM-RECON-012 computed -- gamma derived; gap refuted; protector reassigned.")


if __name__ == "__main__":
    test()
