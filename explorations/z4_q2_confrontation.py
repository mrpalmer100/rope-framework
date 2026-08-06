"""COMMISSION Z, BRICK 4: THE q^2 CONFRONTATION.

QUESTION: can the q^2 winding slot in R* = J0/(pi^2 mu q^2 c) absorb the
chain's +178.8 ppm residual? The slot would need q^2 = 1.0001788
(q = 1.0000894) -- a CONTINUOUS dressing at the 1e-4 level.

REGISTERED PROVENANCE OF q (adjudicated, not scanned):
  - GG-006 (Derived, 288 downstream): charge IS the integer linking
    number; the linking/Chern math (GG-002/003) is intrinsically
    integer-valued. The electron: q = 1.
  - V Phase 2: the Z_2 double-cover factor settled at 1 (registered).
  - NUC-003 (flagged, unbuilt): fractional sub-knot windings 2/3, 1/3 --
    confined, observable totals integer, and DISCRETE in any case.
The registered value set for q^2 at the electron slot: {1} exactly, with
the nearest registered discrete alternatives (q=2 doubles: 4; sub-knot
fractions if the unbuilt layer existed: 4/9, 1/9) all O(1) away.

TEST T1 (structural): the slot is DISCRETE by Derived topology; the
residual requires a CONTINUOUS 1.0001788. Exhibit the mismatch
numerically: distance from every registered candidate to the required
value, in ppm.

TEST T2 (exactness of the committed ansatz): the solver's configuration
is f(r) e^{i chi} -- winding number computed symbolically from the phase
integral: (1/2pi) oint d(arg) = 1 EXACTLY, independent of f. No dressing
enters the topological index through the profile.

AFTER the verdict (display-and-refuse per corpus discipline): the
residual's magnitude confronted against the chain's OWN small parameters
(Omega = pi/x*, 1/x*, lam/Omega) -- observations displayed, adoption
refused, second predictions named.
"""
import numpy as np
import sympy as sp

PI=np.pi; XSTAR=float(np.exp(PI**2)); OMEGA=PI/XSTAR
ALPHA_INV=137.035999084; D_E=1.1051029
base=4*PI**3*D_E
delta_req=1-ALPHA_INV/base          # required continuous dressing on 1/alpha
q2_req=1+delta_req/(1-delta_req)    # q^2 needed if the slot absorbs it (1/alpha ~ 1/q^2... sign)
print("== T1: THE STRUCTURAL MISMATCH ==")
print(f"   residual to absorb: {delta_req*1e6:.1f} ppm  -> required q^2 = {1+delta_req:.7f} (continuous)")
cands={"q^2 = 1 (GG-006, electron)":1.0, "q^2 = 4 (q=2)":4.0,
       "q^2 = 4/9 (NUC-003 sub-knot, unbuilt)":4/9, "q^2 = 1/9 (NUC-003 sub-knot, unbuilt)":1/9}
for k,v in cands.items():
    d=(v/(1+delta_req)-1)
    print(f"   {k:40s} distance from required: {d*100:+11.2f} %")
print("   -> the registered value set is DISCRETE with O(1) spacing; the need is")
print("      1.8e-4 and CONTINUOUS. No registered or flagged structure can supply it.\n")

print("== T2: WINDING EXACTNESS OF THE COMMITTED ANSATZ (symbolic) ==")
chi=sp.symbols('chi', real=True)
# configuration components (f cos chi, f sin chi): winding = (1/2pi) oint d(atan2)
w=sp.integrate(sp.diff(sp.atan2(sp.sin(chi),sp.cos(chi)),chi),(chi,0,2*sp.pi))/(2*sp.pi)
print(f"   (1/2pi) oint d(arg) = {sp.nsimplify(w)}  -- integer, profile-independent. q = 1 EXACT.\n")

print("== VERDICT: the q^2 slot CANNOT absorb the residual. Ladder EXHAUSTED. ==\n")

print("== DISPLAY-AND-REFUSE: the residual vs the chain's own small parameters ==")
lam=1.0915e-4
delta=delta_req
obs={"Omega = pi/x*":OMEGA, "Omega * D_E":OMEGA*D_E, "Omega * D_req":OMEGA*(ALPHA_INV/(4*PI**3)),
     "1/x*":1/XSTAR, "lam":lam, "2(Omega-lam)":2*(OMEGA-lam)}
for k,v in obs.items():
    print(f"   delta = {delta:.4e} vs {k:14s} = {v:.4e}: ratio {delta/v:.4f}")
print("   OBSERVATION (displayed, NOT adopted): delta/(Omega D_E) = "
      f"{delta/(OMEGA*D_E):.4f} -- the residual equals Omega x D_E to 0.4 percent.")
print("   Omega is the chain's own rotation rate: a FIRST-ORDER-IN-Omega correction")
print("   to the construction (finite-rotation next order) is a mechanically natural")
print("   home. REFUSED under the second-prediction rule until the coefficient is")
print("   DERIVED from the construction's O(Omega) expansion. Named, not opened.")
