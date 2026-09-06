"""TRIPLE-DUTY Leg 1 (R1) -- F_bend(s) from the FND-130 object with s, kb, R, b FREE.
Clean room: 1/3, 3/2 not entered. v2: symbolic vs discrete gradient at off-target s."""
import sympy as sp, numpy as np, sys
sys.path.insert(0,'benchmarks/foundations')
s, kb, R, b, T = sp.symbols('s k_b R b T', positive=True)
# FND-130 force density (sympy-derived there, identity-checked): f_n(inward) = kappa [T + kb (tau^2 - kappa^2/2)]
g2 = R**2 + b**2; kap = R/g2; tau = b/g2
F_bend_Rb = sp.simplify(kap*kb*(tau**2 - kap**2/2))            # the kb part, general helix (R, b free)
# express via s = sin^2 psi = axial cosine^2 = b^2/(R^2+b^2)  (reading A)
F_bend_s = sp.simplify(F_bend_Rb.subs(b, sp.sqrt(s*g2)) )       # not closed in s alone; do it properly:
# tau^2 - kappa^2/2 = (b^2 - R^2/2)/g2^2 ; with b^2 = s g2, R^2 = (1-s) g2:
dev = sp.simplify(((s*g2) - (1-s)*g2/2)/g2**2)
print("tau^2 - kappa^2/2 =", sp.factor(dev), "   (general R, b; s = b^2/(R^2+b^2))")
F_gen = sp.factor(kap*kb*dev)
print("F_bend (general) =", F_gen)
# worst-case pitch p = a_f = 1 (FND-130's exhibited form): kappa = 2 pi sqrt(s(1-s)), tau = 2 pi s
kap_s = 2*sp.pi*sp.sqrt(s*(1-s)); tau_s = 2*sp.pi*s
F_s = sp.factor(sp.simplify(kap_s*kb*(tau_s**2 - kap_s**2/2)))
print("F_bend(s) at p = a_f =", F_s)
q, r = sp.div(sp.expand(F_s/(kb*4*sp.pi**3*sp.sqrt(s*(1-s)))), 3*s-1, s)
print("division by (3s-1): quotient", sp.factor(q), " remainder", r)
cof = sp.factor(F_s/(3*s-1))
print("cofactor F_bend/(3s-1) =", cof, "  zeros on (0,1):", sp.solve(sp.Eq(cof/kb,0), s), " poles: none (polynomial x sqrt)")
# v2: symbolic vs discrete energy gradient at three off-target s (the FND-130 numeric control, away from the magic angle)
from maint_equilibrium import fd_normal_force
for sv in (0.25, 0.40, 0.50):
    kv = 2*np.pi*np.sqrt(sv*(1-sv)); tv = 2*np.pi*sv
    fn_num = fd_normal_force(sv); fn_an = kv*(1.0 + (tv**2 - kv**2/2))
    print(f"v2  s={sv}: numeric f_n {fn_num:.6f}  analytic {fn_an:.6f}  rel err {abs(fn_num-fn_an)/abs(fn_an)*100:.4f}%")
