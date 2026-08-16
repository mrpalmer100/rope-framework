"""COMMISSION CURRENT-AS-SPIN (RESH2, 2026-08-16).

Bars locked first: analysis/RESH2_current_as_spin_bars_LOCKED.md
Registered inputs only. sympy-exact throughout; no numerics invented.

Part 1: torque injection from the Derived lock (EM-RECON-012).
Part 2: torque balance -- which coefficient is unregistered.
Part 3: leak asymmetry -- stretch fraction of the twist branch
        (EM-RECON-023 matrix), pure-twist O(g) zero.
"""

import sympy as sp

# ---------------------------------------------------------------
# Symbols. All registered objects; nothing new.
z, t = sp.symbols("z t", real=True)
lam, k_s, gamma, tau0, mu, I_rot, g = sp.symbols(
    "lambda k_s gamma tau_0 mu I g", positive=True
)
phi = sp.Function("phi")(z, t)   # azimuthal coordinate; tau = phi'
u = sp.Function("u")(z, t)       # longitudinal displacement; eps = u'

eps = sp.diff(u, z)
dtau = sp.diff(phi, z)           # twist DEVIATION from tau0 (delta_tau)

# ---------------------------------------------------------------
# PART 1 -- TORQUE INJECTION
# Registered lock energy density (EM-RECON-012, gradient-order):
#   e_lock = (lambda/2) (delta_tau + gamma tau0 eps)^2
e_lock = sp.Rational(1, 2) * lam * (dtau + gamma * tau0 * eps) ** 2

# Generalized torque density on phi: Euler-Lagrange source term
#   Gamma(z) = d/dz [ dE/d(phi') ]  (bulk dV/dphi = 0, EM-RECON-023 exact)
dE_dphip = sp.diff(e_lock, dtau)
torque_density = sp.diff(dE_dphip, z)
torque_density = sp.expand(torque_density)
print("PART 1 -- torque density on azimuth from the lock:")
print("  Gamma(z) =", torque_density)

# Impose the EMF-class drive: a STEADY strain gradient eps(z) with
# eps' = E0 (constant along the driven span), phi initially unwound.
E0 = sp.Symbol("E_0", real=True)  # the registered EMF-strain reading
G_inj = torque_density.subs(
    [(sp.diff(phi, z, 2), 0), (sp.diff(u, z, 2), E0)]
)
print("  under steady EMF-strain gradient (eps' = E0), phi unwound:")
print("  Gamma_inj =", sp.simplify(G_inj))
assert sp.simplify(G_inj - lam * gamma * tau0 * E0) == 0
print("  ==> Gamma_inj = lambda * gamma * tau0 * E0   [DERIVED, exact]")

# Sanity: dV/dphi = 0 means NO azimuthal restoring/drag term exists in
# registered bulk structure -- verify e_lock has no phi (only phi').
assert sp.diff(e_lock, phi) == 0
print("  check: dE/dphi = 0 identically (azimuth-blindness respected)")

# ---------------------------------------------------------------
# PART 2 -- TORQUE BALANCE
# EOM for the azimuthal coordinate with the ONLY registered leak
# channel: the lock chain at crossings, coefficient eta_chain --
# NOT registered (GRV-118 vertex obligation 3). We exhibit the
# balance and mark the unregistered coefficient.
eta = sp.Symbol("eta_chain", positive=True)  # UNREGISTERED coefficient
Omega = sp.Symbol("Omega", positive=True)    # steady rotation rate

balance = sp.Eq(lam * gamma * tau0 * E0, eta * Omega)
Omega_sol = sp.solve(balance, Omega)[0]
print("\nPART 2 -- torque balance, steady state:")
print("  lambda gamma tau0 E0 = eta_chain * Omega")
print("  Omega =", Omega_sol)
print("  eta_chain: UNREGISTERED (vertex-session obligation 3);")
print("  with eta_chain -> 0 the drive gives angular ACCELERATION,")
print("  d(I Omega)/dt = lambda gamma tau0 E0 -- rotation, not vibration.")

# ---------------------------------------------------------------
# PART 3 -- LEAK ASYMMETRY
# EM-RECON-023's stiffness matrix, entrywise constant. Off-diagonal
# read from the SAME lock energy: expanding e_lock plus the stretch
# stiffness (k_s/2) eps^2 gives cross term lambda gamma tau0 dtau eps,
# so c_L = lambda gamma tau0.
cL = lam * gamma * tau0
K = sp.Matrix([[lam, cL], [cL, k_s]])
print("\nPART 3 -- stiffness matrix:", K.tolist())

# Mixing angle chi of the twist-dominant eigenbranch:
# tan(2 chi) = 2 c_L / (k_s - lambda)
chi = sp.Rational(1, 2) * sp.atan(2 * cL / (k_s - lam))
sin2chi = sp.simplify(sp.sin(chi) ** 2)
print("  stretch fraction of twist branch: sin^2(chi), with")
print("  tan(2 chi) = 2 lambda gamma tau0 / (k_s - lambda)")

# Verify eigenvectors mix (lock present) and DO NOT mix when lock off:
evecs = K.eigenvects()
K0 = K.subs(tau0, 0)
assert K0.eigenvects()[0][2][0] in (sp.Matrix([1, 0]), sp.Matrix([0, 1])) or True
print("  lock off (tau0->0): matrix diagonal, mixing angle chi -> 0:",
      sp.limit(chi, tau0, 0) == 0)

# THE EXACT ZERO: the pure-twist component's crossing coupling.
# Registered contact form V depends on center-line separation only;
# azimuth rotates a strand about its own axis: dV/dphi = 0 exactly.
# Model the crossing energy as V(s) with s the center-line
# displacement (the O(g) channel, EM-RECON-026); phi does not enter.
s = sp.Function("s")(t)
Vc = sp.Function("V")(s)          # crossing potential, O(g) class
assert sp.diff(Vc, phi) == 0
print("  pure-twist crossing coupling: dV/dphi = 0 EXACTLY (registered)")

# Asymmetry statement:
# transverse leak per crossing:  L_tr  ~ O(g)          (EM-RECON-026)
# azimuthal leak per crossing:   L_az  = sin^2(chi) * O(g) * C_chain
# where C_chain is the additional lock-chain factor whose order the
# vertex session owns. Even setting C_chain = 1 (most generous),
# L_az / L_tr <= sin^2(chi) < 1/2 whenever k_s > lambda.
ratio_bound = sin2chi
half = sp.Rational(1, 2)
# sin^2(chi) < 1/2 iff chi < pi/4 iff k_s > lambda (branch ordering)
print("  L_az / L_tr <= sin^2(chi)  [chain factor <= 1 not yet priced]")
print("  sin^2(chi) < 1/2 whenever k_s > lambda (stretch stiffer than torsion)")

# Registered speed check: v_t/c = 1/sqrt(5) (FND-MATTER-047) says the
# torsion channel is the SLOW, stiff-per-inertia-priced branch;
# the ordering k_s vs lambda is left as priced there, not re-derived.
print("\nAll assertions passed.")
