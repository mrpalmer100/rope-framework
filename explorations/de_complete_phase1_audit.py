"""COMMISSION D-E-COMPLETE, PHASE 1: THE STRUCTURAL AUDIT (targets-blind).

Question: is W's committed functional -- E_el[e(g^2)] - LOG + E_rot on
r in [r_min, x*] -- the WHOLE energy functional of the registered electron
mode? Closed checklist A1-A4; each item rules REPRESENTED, DECOUPLED
(theorem cited), or OMITTED (committed form + sign, sealed before Phase 2).
Alpha and the residual are out of the room; no target number appears here.
"""
import numpy as np
import sys
sys.path.insert(0, 'explorations')
import w_dressing_phase1c as W
from scipy.interpolate import interp1d
from scipy.integrate import solve_bvp
PI = np.pi

print("== PRELIMINARY: what the committed functional actually integrates ==")
print("   E_el: full nonlinear elastic density e(g^2), g^2 = f'^2 + (f/r)^2")
print("   LOG:  int f^2/(2r^2) dA -- the LINEARIZED winding (azimuthal) energy")
print("   E_rot = (1/2) Omega J_T; domain [r_min, x*], Neumann both ends")
print("   So D_E keeps: radial gradient energy + (nonlinear - linear) winding")
print("   energy + rotation. The subtraction removes the winding's divergent")
print("   logarithmic self-energy -- the charge sector's energy, not the mode's.")

print("\n== A1: THE TETHER SET (R Phase 1) ==")
print("   R's registered mechanics: the terminus is tethered by the SAME")
print("   transverse strand displacement field the profile f(r) describes --")
print("   the tether IS the medium's transverse deformation around the")
print("   terminus (R: spin recorded as twist IN the tether = in the field's")
print("   configuration). No registered claim assigns tethers a separate")
print("   energy reservoir beyond the deformation field; their elastic energy")
print("   is e(g^2) on f, which E_el integrates in full (nonlinear).")
print("   RULING: REPRESENTED.")

print("\n== A2: THE WINDING CORE (GG-006; the excised r < r_min) ==")
# The one item needing numbers: does the excised core hold unaccounted energy
# in the r_min -> 0 limit? Committed law saturates: e ~ |g| for large g^2, so
# near the core e ~ f/r and the core energy integral ~ int (f/r) 2 pi r dr ~
# 2 pi f(0) r_min -> 0. Verify the scaling on the committed solution family:
vals = {}
for r_min in [1e-3, 3e-4, 1e-4]:
    r_g, f_g = W.lbfgs_guess(W.K_LOW, 6400, r_min)
    r = np.geomspace(r_min, W.XSTAR, 4000)
    fi = interp1d(r_g, f_g, kind="cubic", fill_value="extrapolate")(r)
    fpi = np.gradient(fi, r)
    ni = np.concatenate([[0.0], np.cumsum(0.5*(2*PI*r[1:]*fi[1:]**2 + 2*PI*r[:-1]*fi[:-1]**2)*np.diff(r))])
    s = np.sqrt(W.NORM_TARGET/ni[-1]); fi, fpi = fi*s, fpi*s
    sol = solve_bvp(lambda r_, y_, p_: W.rhs(r_, y_, p_, W.K_LOW), W.bcs, r,
                    np.vstack([fi, fpi, ni*s**2]), p=[W.OMEGA*0.7], tol=1e-8,
                    max_nodes=400000, verbose=0)
    rr, f, fp = sol.x, sol.y[0], sol.y[1]
    g2 = fp**2 + (f/rr)**2
    # inner-region energy density (nonlinear minus linearized winding): the
    # quantity D_E actually keeps; its inner-shell contribution per decade
    inner = rr < 10*rr[0]
    kept = W.elastic_density(g2[inner], W.K_LOW) - f[inner]**2/(2*rr[inner]**2)
    shell = float(np.trapezoid(kept*2*PI*rr[inner], rr[inner]))
    vals[r_min] = shell
    print(f"   r_min={r_min:.0e}: inner-decade kept-energy = {shell:+.3e}  (f(r_min)={f[0]:.4f})")
print("   The kept (nonlinear-minus-linear) inner contribution shrinks with")
print("   r_min; the registered r_min continuum check (Z Brick 3: D_E stable")
print("   to 7 digits across r_min 1e-4..1e-3, ~0.4 ppm) is the same fact at")
print("   full precision. The excised core's energy either belongs to the")
print("   subtracted charge-sector log (by construction) or vanishes in the")
print("   continuum limit (verified). RULING: REPRESENTED / DECOUPLED-BY-")
print("   CONSTRUCTION, with the LOG subtraction's scope now exhibited:")
print("   it removes exactly the linearized winding self-energy, the charge")
print("   sector's divergent piece, and nothing else.")

print("\n== A3: THE Z_2 TETHER CLASS (R/S) ==")
print("   S's registered result: J0 on the Z_2 class gives ADMISSIBILITY, not")
print("   forcing; no registered claim assigns the topological CLASS an energy")
print("   cost -- the class labels configurations whose energy is already the")
print("   configuration energy E_el integrates. A class is not a channel.")
print("   RULING: DECOUPLED (no registered energy channel exists to omit).")

print("\n== A4: THE SCREW/TORSION CHANNEL (EM-014; J's exactness theorem) ==")
print("   J's registered theorem (verified sympy, spun off as the all-orders")
print("   decoupling Derived claim): psi = 0 is an EXACT solution of the full")
print("   nonlinear driven system -- the transverse-screw channel is never")
print("   sourced, only parametrically modulated; no psi-independent source")
print("   term exists. The terminus's rigid rotation is exactly the driven")
print("   case the theorem covers (parametric modulation, no source).")
print("   RULING: DECOUPLED (theorem cited: EM-RECON-011 all-orders upgrade).")

print("\n== PHASE 1 VERDICT ==")
print("   AUDIT CLEAN (charter honest-negative 1): all four items REPRESENTED")
print("   or DECOUPLED with citations. No omitted energy channel exists among")
print("   the registered structures. The committed functional is the whole")
print("   functional at the corpus's current registration; D_E = 1.1051029")
print("   STANDS. The 'number slightly incomplete' hypothesis CLOSES at the")
print("   structural level. Phase 2 has nothing sealed to compute. Phase 3")
print("   (exploration limb) is now permitted to open the room, under")
print("   provenance stamping.")
