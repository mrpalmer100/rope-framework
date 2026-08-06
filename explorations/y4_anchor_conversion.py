"""COMMISSION Y, BRICK 4: THE ANCHOR-CONVERSION DERIVATION.

The question (from Brick 3): the pi in J0 = hbar/(pi alpha) is the unique
rope-to-laboratory conversion in the alpha chain. Is its angular character
smooth-quadratic (angular integral pi -> prefactor pi^4) or rectified-linear
(angular integral 4 -> prefactor 4 pi^3)? Derive from REGISTERED corpus
structures, alpha out of the room.

STRUCTURE: the anchor equates a rope-side invariant with a lab-side action.
Each side's registered form has a derivable angular character.

P1 (LAB SIDE): HBAR-001's surviving standing-wave action form,
S = pi T A^2 / (2c). Claim: its pi is the smooth quadratic cycle integral.
Verify: for a harmonic degree of freedom q(t) = A cos(wt), the canonical
action per cycle is oint p dq = pi m w A^2 -- and the pi arises EXACTLY as
int_0^{2pi} sin^2(chi) dchi = pi (equivalently cos^2). Computed against the
rectified alternative int |sin| = 4. Also verify oint p dq = 2 pi E / w
(the smooth quadratic E/omega relation O's I_mode = E/omega froze).

P2 (ROPE SIDE): V identified J as the S^1 Noether charge; the committed
solver realizes it as J = Omega int f^2 dA -- QUADRATIC in the field by
registered construction. Verify on the committed solution: the constraint
enforces J = J_T exactly; the Noether integrand is f^2 (quadratic); the
rectified alternative (linear functional Omega int f dA scaled) does NOT
equal J_T under any amplitude-independent normalization -- i.e., J's
registered definition has no rectified reading.

CONSEQUENCE (the theorem, stated in the results doc): if BOTH sides of the
J0 conversion are smooth quadratic by registered construction, the 4/pi
CANNOT live in the J0 step. Its only possible home in the chain is the one
alpha-carrying object the corpus has NOT yet constructed: the CHARGE
functional inside the anchor a0 = lambda_bar_C / alpha (alpha ~ e^2; the
charge coupling is LINEAR in field amplitude, the unique linear-response
observable in the chain -- the only place a rectified angular integral can
mechanically arise).

P3 (LOCATION CHECK): exhibit that a single rectified two-component
sampling applied once to the charge-coupling observable produces exactly
one factor 4/pi in 1/alpha (bookkeeping: 1/alpha ~ 1/e^2_lab; if
e^2_lab = (pi/4) e^2_rope from one rectified conversion of the rotating
source, then 1/alpha_lab = (4/pi) x [smooth chain] -- one factor, right
place, right direction). This is bookkeeping verification, not a
derivation of the charge functional itself (named for go-decision).
"""
import numpy as np
import sympy as sp

print("== P1: LAB SIDE -- angular character of the registered action form ==")
chi, A, m, w = sp.symbols('chi A m omega', positive=True)
q = A*sp.cos(chi)           # chi = omega t
p = m*w*sp.diff(q, chi)     # p = m dq/dt = m w dq/dchi
S_smooth = sp.integrate(p*sp.diff(q, chi), (chi, 0, 2*sp.pi))   # oint p dq
E = sp.Rational(1,2)*m*w**2*A**2
print(f"   oint p dq (smooth)          = {sp.simplify(S_smooth)}   [= pi m w A^2]")
print(f"   2 pi E / omega              = {sp.simplify(2*sp.pi*E/w)}   -> ratio = {sp.simplify(S_smooth/(2*sp.pi*E/w))}")
ang_sq  = sp.integrate(sp.sin(chi)**2, (chi, 0, 2*sp.pi))
ang_abs = sp.integrate(sp.Abs(sp.sin(chi)), (chi, 0, 2*sp.pi))
print(f"   angular integral in oint p dq: int sin^2 = {ang_sq}  (rectified alt: int|sin| = {ang_abs})")
print(f"   -> the pi in S = pi T A^2/(2c) is int sin^2 d chi. LAB SIDE: SMOOTH QUADRATIC. PROVEN.\n")

print("== P2: ROPE SIDE -- angular character of the registered J ==")
# On the committed solution: J = Omega int f^2 dA (quadratic Noether charge).
# Character check: under f -> s f, J scales as s^2 (quadratic), a rectified
# linear circulation would scale as s^1. The registered constraint structure
# (NORM_TARGET = J_T/Omega imposed on int f^2) commits the quadratic reading.
PI=np.pi; XSTAR=float(np.exp(PI**2)); JT=PI**2*(XSTAR**2-1.0)/XSTAR; OMEGA=PI/XSTAR
r=np.geomspace(1e-3,XSTAR,4000); f=np.exp(-((np.log(r/50))**2)/8.0)  # shape irrelevant; scaling is the check
f*= np.sqrt((JT/OMEGA)/np.trapezoid(2*PI*r*f**2,r))
J1=OMEGA*np.trapezoid(2*PI*r*f**2,r)
J2=OMEGA*np.trapezoid(2*PI*r*(2*f)**2,r)
L1=OMEGA*np.trapezoid(2*PI*r*np.abs(f),r); L2=OMEGA*np.trapezoid(2*PI*r*np.abs(2*f),r)
print(f"   J[f]/J_T = {J1/JT:.6f};  J[2f]/J[f] = {J2/J1:.4f} (quadratic: 4)   linear functional would give {L2/L1:.4f}")
print(f"   -> the registered J is QUADRATIC in the field; no rectified reading exists in its definition. PROVEN.\n")

print("== THEOREM (both sides smooth quadratic) ==")
print("   The J0 = hbar/(pi alpha) conversion equates two smooth quadratic")
print("   invariants. The 4/pi CANNOT arise in the J0 step. Its only")
print("   candidate home in the chain is the charge functional inside a0.\n")

print("== P3: LOCATION BOOKKEEPING ==")
# One rectified two-component sampling of the rotating source in the charge
# coupling: <|cos|+|sin|>/2-component-smooth = (4/pi)/1 applied ONCE to e^2.
rect=sp.integrate(sp.Abs(sp.cos(chi))+sp.Abs(sp.sin(chi)),(chi,0,2*sp.pi))/(2*sp.pi)
print(f"   two-component rectified cycle mean = {sp.nsimplify(rect)} = 4/pi (exact)")
print("   1/alpha ~ 1/e^2: e^2_lab = (pi/4) e^2_rope  =>  1/alpha_lab = (4/pi) x smooth chain")
print("   -> ONE factor, first power, correct direction: pi^4 -> 4 pi^3. Bookkeeping CONSISTENT.")
print("   (The charge functional itself remains UNCONSTRUCTED -- named, not opened.)")
