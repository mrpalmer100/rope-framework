"""EM-RECON-014: K_c derived, not argued. Bars locked first
(analysis/EMRECON017_Kc_bars_LOCKED.md): survival threshold K_c/k > 1
STRICT (K_c = k is marginal at the adjudicated k = 2T0); registered
inputs only; missing material ratios NAMED not invented.

STRUCTURE:
 B1  P-VOL kinematics: the exact width-strain map and the per-contact
     geometry (sympy).
 B2  The assembly selector: at coverage threshold, gaps have JUST closed
     (FND-MATTER-004 places matter AT threshold), so further densification
     has exactly one load path -- the contact zones. Below threshold the
     contact channel reads K_c = 0 (width grows into open gaps for free);
     at/above threshold the strain localizes where strands touch. The
     localization is derived from the threshold placement, not chosen
     (bar 5): 'at threshold' MEANS no free gap remains.
 B3  K_c(eps) computed from the registered contact form for crossing
     strands under P-VOL thickening, at crossing density 2/a per unit
     strand length.
 B4  The confrontation with the strict threshold, and the honest
     accounting of what is derived vs what reduces to a named ratio.
"""
import numpy as np
import sympy as sp

# ---------------- B1: P-VOL kinematics (exact) ----------------
print("== B1: P-VOL kinematics ==")
eps = sp.symbols('epsilon', real=True)
w0 = sp.symbols('w_0', positive=True)
w = w0 / sp.sqrt(1 + eps)
dw = sp.simplify(sp.diff(w, eps).subs(eps, 0))
print(f"   width under strain: w(eps) = w0/sqrt(1+eps); dw/deps|0 = {dw}")
print("   COMPRESSION (eps < 0) THICKENS: d(width)/d(-eps) = +w0/2.")
print("   Two contacting strands each thickening under bulk over-density")
print("   -eps close their center gap at rate d(gap)/d(-eps) = -w0 (both")
print("   widths grow; equivalently the contact range sigma_eff(eps) =")
print("   sigma0/sqrt(1+eps) in the registered finite-contact form).\n")

# ---------------- B2: the assembly selector ----------------
print("== B2: assembly at threshold (derived from placement, bar 5) ==")
print("   FND-MATTER-004 places matter AT the coverage threshold: the")
print("   configuration where free transverse gaps have JUST closed --")
print("   that is the threshold's definition. Below it, widening costs")
print("   nothing (K_c = 0, the registered pre-protector collapse);")
print("   at it, every further increment of over-density must be")
print("   accommodated where strands touch. The load path is the contact")
print("   set BY DEFINITION OF THE PLACEMENT, not by modeling choice.")
print("   Consequence: K_c is the contact-channel curvature evaluated at")
print("   the threshold configuration -- computed next.\n")

# ---------------- B3: K_c(eps) from the registered contact form ----------------
print("== B3: K_c from the registered contact form ==")
# Two crossing strands (perpendicular), center distance d at the crossing.
# Registered pair energy density along the crossing region integrates to
# a per-crossing energy: E_x(d) = integral Ac/(1+(r(s)/sigma)^4) ds along
# one strand, r(s) = sqrt(d^2 + s^2) (perpendicular crossing).
# Under P-VOL at bulk strain eps (eps < 0 over-density):
#   sigma(eps) = sigma0/sqrt(1+eps)   (thickening = growing range)
#   d fixed by the weave (transverse spacing set by routing, not eps).
# Per unit strand length: crossings at density 2/a (two transverse
# families, one crossing each per cell of size a).

def crossing_energy(d, sig, Ac=1.0, S=8.0, n=4001):
    s = np.linspace(-S, S, n)
    r = np.sqrt(d*d + s*s)
    return Ac * np.trapezoid(1.0/(1.0 + (r/sig)**4), s)

def Kc_over_unit(d0, sig0, eps0=0.0, h=1e-4):
    """d^2/deps^2 of the per-length contact energy at eps0 (finite diff),
    in units of Ac (energy per crossing) x (2/a) with a = 1."""
    def Etot(e):
        sig = sig0/np.sqrt(1.0 + e)
        return 2.0 * crossing_energy(d0, sig)     # 2 crossings per unit a
    return (Etot(eps0+h) - 2*Etot(eps0) + Etot(eps0-h)) / h**2

# The threshold configuration: contact 'just closed' = the crossing
# separation d0 sits at the onset of the contact form's rise. The
# registered form has its knee at d ~ sigma; we display K_c across the
# physically admissible band d0/sigma0 in [1, 3] (at threshold, standoff
# is at the knee; the exact d0/sigma0 at threshold is set by the coverage
# fraction f_c -- displayed as a band, not chosen).
print("   K_c per unit length, units Ac/a (a = 1), vs threshold standoff:")
print("   d0/sig0   K_c(eps=0)     K_c(eps=-0.05)  K_c(eps=-0.10)")
band = {}
for ratio in [1.0, 1.5, 2.0, 2.5, 3.0]:
    vals = [Kc_over_unit(ratio, 1.0, e) for e in (0.0, -0.05, -0.10)]
    band[ratio] = vals
    print(f"   {ratio:5.1f}   {vals[0]:12.5f}  {vals[1]:12.5f}  {vals[2]:12.5f}")
print("   K_c is FINITE and POSITIVE at eps -> 0 across the band (no")
print("   Hertz-type vanishing: the registered form is smooth and long-")
print("   ranged, so the channel is linearly stiff at onset), and")
print("   STIFFENS with over-density.\n")

# ---------------- B4: the confrontation ----------------
print("== B4: confrontation with the strict threshold (bar 1) ==")
print("   DERIVED IN FORM: K_c = C(d0/sig0) x (Ac/a), with C in")
print(f"   [{min(v[0] for v in band.values()):.3f}, {max(v[0] for v in band.values()):.3f}] across the admissible standoff band at eps = 0.")
print("   THE SURVIVAL CONDITION K_c > k = 2 T0 therefore reads:")
print("       Ac/(T0 a)  >  2 / C(d0/sig0)")
Cmin = min(v[0] for v in band.values()); Cmax = max(v[0] for v in band.values())
print(f"   i.e. Ac/(T0 a) > {2/Cmax:.2f} (loose standoff) .. {2/Cmin:.2f} (tight standoff).")
print("   THE MATERIAL RATIO Ac/(T0 a) -- the contact amplitude in tension")
print("   units -- IS NOT REGISTERED anywhere in the corpus (the engine's")
print("   Ac = 1, sigma = 0.12 are simulation units; FND-KIN-005 registers")
print("   the FORM, not the scale). Per bar 4 it is NAMED, its survival")
print("   threshold is COMPUTED above, and it is LEFT OPEN.")
print("\n   OUTCOME (c) of the bars: K_c derived IN FORM; the 'same-material'")
print("   O(k) argument is SUPERSEDED (K_c is set by the contact amplitude")
print("   Ac, not by the stretch modulus k -- the argued mechanism routed")
print("   through the wrong constant); survival reduces to ONE named,")
print("   unregistered material ratio with a computed threshold band.")
print("   The core's status: CONDITIONAL on Ac/(T0 a) exceeding a number")
print("   of order unity -- a precise open question where an argument")
print("   used to stand.")
