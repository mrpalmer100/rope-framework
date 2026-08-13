"""COMMISSION SHIN7 -- bending-cost pricing (closed-form arithmetic).
Executed under analysis/SHIN7_kb_pricing_bars_LOCKED.md."""
import numpy as np

# locked inputs
MARGIN = 6.1                    # tight floor (kappa50)
SPEND = None                    # computed from derived angles below
u = 1/3
v = (15 + 2*np.sqrt(30))/35
sin2p1 = 2*np.sqrt(2)/3
sin2p2 = 2*np.sqrt(v*(1-v))
spend = 1.0/(u*v)               # 1/sin^2(psi_eff) = 1/(sin^2psi1 sin^2psi2)
eps = MARGIN/spend - 1.0

# curvature at worst case p = a_f (units a_f = 1, T0_f = 1)
k1 = np.pi*sin2p1
k2 = np.pi*sin2p2
ktot = k1 + k2
Tf = spend                      # compensated tension in T0_f units

# P1 static bound
C1_Tf = 2*eps/ktot**2           # kb <= C1_Tf * T_f a_f^2
# P2 dispersive bound
k = np.pi/2                     # 2pi/lambda_min, lambda_min = 4 a_f
C2_Tf = 2*eps/k**2

C_Tf = min(C1_Tf, C2_Tf)
C_T0 = C_Tf*Tf                  # in T0_f units
slender = np.sqrt(C_T0)         # r_s/a_f under kb ~ T0_f r_s^2

print("SHIN7 -- kb pricing at derived angles, worst case p = a_f")
print(f"  spend = {spend:.4f}x  headroom eps = {eps:.4f}")
print(f"  kappa_1 = {k1:.4f}/a_f  kappa_2 = {k2:.4f}/a_f  kappa_tot = {ktot:.4f}/a_f")
print(f"  P1 static:     kb <= {C1_Tf:.5f} T_f a_f^2 = {C1_Tf*Tf:.5f} T0_f a_f^2")
print(f"  P2 dispersive: kb <= {C2_Tf:.5f} T_f a_f^2 = {C2_Tf*Tf:.5f} T0_f a_f^2")
print(f"  BINDING (P1): kb <= {C_T0:.5f} T0_f a_f^2")
print(f"  slenderness reading: r_s/a_f <= {slender:.4f}")
print("  VERDICT: bound registered; slenderness condition",
      "CONSISTENT with spacing-separated fibers" if slender > 0.1 else "TIGHT, filed")
