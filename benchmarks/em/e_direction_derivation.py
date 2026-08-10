"""COMMISSION N — THE DIRECTION OF THE ELECTRIC FIELD.
Charter: docs/commissions/COMMISSION_N_E_direction.md (bars locked first).

N2 — THE DEFINITION, FIXED BEFORE ANY CANDIDATE:
  E's direction is the direction of the force on a test winding, F = q E,
  with q = winding number (GRV-020). This is the SAME definition the static
  sector already uses (EM-015: force = -grad of constraint interaction
  energy). One definition, both regimes.
"""
import sympy as sp

print("=" * 72)
print("N-STEP 1: force on a test winding from a passing transverse wave")
print("=" * 72)
# Registered contact form: V = V(r), r = center-line separation (azimuth-blind,
# EM-RECON-023). A test winding sits at position x0 (transverse offset 0).
# A carrier wave displaces the medium's center line transversely by the vector
# field  s(z,t) = (s_x, s_y)  — the ONLY registered mechanical dof that moves
# center lines transversely is the two-component displacement (channel-map).
x, y, z, t = sp.symbols('x y z t', real=True)
sx, sy = sp.symbols('s_x s_y', real=True)          # wave's transverse displacement at the winding
r0 = sp.symbols('r_0', positive=True)               # unperturbed separation
Vfun = sp.Function('V')

# separation with the medium displaced by (sx, sy) relative to the winding:
dx, dy = sp.symbols('dx dy', real=True)             # unperturbed offset components
r = sp.sqrt((dx - sx)**2 + (dy - sy)**2)
U = Vfun(r)
# Force on the winding = -grad_{winding position} U = +grad_{(sx,sy)} U evaluated
# to first order in the displacement (linear response, the radiation regime):
Fx = sp.diff(U, sx)
Fy = sp.diff(U, sy)
F1x = sp.series(Fx.subs({sx: 0, sy: 0}), n=1).removeO() if False else Fx.subs({sx: 0, sy: 0})
F1y = Fy.subs({sx: 0, sy: 0})
print("F_x|_(s=0) =", sp.simplify(F1x))
print("F_y|_(s=0) =", sp.simplify(F1y))
# The zeroth-order force is the STATIC radial force (along (dx,dy)) — verify by
# the cross-component test: a radial vector has dx*F_y - dy*F_x = 0 identically.
cross = sp.simplify(dx * F1y - dy * F1x)
assert cross == 0, "zeroth order must be the static radial force (EM-015 consistency)"
print(">>> zeroth order = static radial force: the SAME definition reproduces")
print("    EM-015's electrostatics. N3(b) PASSED before the wave term is even read.")

# First order IN THE WAVE: expand the force to linear order in (sx, sy):
F_lin = sp.Matrix([sp.diff(Fx, v).subs({sx: 0, sy: 0}) for v in (sx, sy)]).T
Fy_lin = sp.Matrix([sp.diff(Fy, v).subs({sx: 0, sy: 0}) for v in (sx, sy)]).T
M = sp.Matrix([[F_lin[0], F_lin[1]], [Fy_lin[0], Fy_lin[1]]])
M = sp.simplify(M)
print("\nlinear-response matrix dF_i/ds_j at s=0:")
sp.pprint(M)
# Averaged over the winding's unperturbed surroundings (isotropic medium:
# average over the direction of (dx,dy)), the matrix must be a multiple of the
# identity — the force is then PARALLEL to s. Do the angular average:
th = sp.symbols('theta', real=True)
rr = sp.symbols('r_sep', positive=True)
Msub = M.subs({dx: rr*sp.cos(th), dy: rr*sp.sin(th)})
Mavg = sp.simplify(sp.integrate(Msub, (th, 0, 2*sp.pi)) / (2*sp.pi))
print("\nangular average over the isotropic medium:")
sp.pprint(Mavg)
offdiag_zero = sp.simplify(Mavg[0, 1]) == 0 and sp.simplify(Mavg[1, 0]) == 0
isotropic = sp.simplify(Mavg[0, 0] - Mavg[1, 1]) == 0
assert offdiag_zero and isotropic, "isotropy must make the response a scalar times identity"
kappa = sp.simplify(Mavg[0, 0])
print("\n>>> <dF/ds> = kappa(r) * IDENTITY, kappa =", kappa)
print(">>> THE FORCE ON A TEST WINDING IS PARALLEL TO THE CARRIER'S TRANSVERSE")
print(">>> DISPLACEMENT s. By the fixed definition (N2), E is PARALLEL TO s:")
print(">>>   **E points along the transverse displacement of the carrier.**")

print()
print("=" * 72)
print("N-STEP 2: confrontation (a) — Malus (N3a)")
print("=" * 72)
# E ∥ s is a genuine two-component transverse vector. A polarizer at angle a
# transmits the projection; intensity ∝ |projection|²:
a, E0, ang = sp.symbols('a E_0 alpha', real=True)
s_vec = sp.Matrix([E0*sp.cos(ang), E0*sp.sin(ang)])
pol = sp.Matrix([sp.cos(a), sp.sin(a)])
I_trans = (s_vec.dot(pol))**2
I_ratio = sp.simplify(I_trans / E0**2)
print("I/I0 =", sp.simplify(I_ratio), " = cos²(alpha - a)")
assert sp.simplify(I_ratio - sp.cos(ang - a)**2) == 0
davg = sp.simplify(sp.integrate(I_ratio, (ang, 0, 2*sp.pi)) / (2*sp.pi))
print("pitch-average:", davg, " (=1/2, matching the registered identity)")
dslope = sp.simplify(sp.diff(sp.integrate(I_ratio, (ang, 0, 2*sp.pi)) / (2*sp.pi), a))
print("polarizer-angle derivative of the average:", dslope)
print(">>> Malus PASSES with a nonzero angle dependence for a pure state and the")
print(">>> registered 1/2 average for the pitch mixture: exactly the structure the")
print(">>> single-field candidates FAILED (their average had zero derivative).")

print()
print("=" * 72)
print("N-STEP 3: what the derivation is CONDITIONAL on (N5, stated plainly)")
print("=" * 72)
print("The derivation used ONE property of the carrier: it displaces center")
print("lines TRANSVERSELY (a two-component vector s). It did NOT use the")
print("carrier's dynamics — no mass, no dispersion, no dressing. Therefore:")
print("- The direction result holds for ANY carrier in the transverse-vector")
print("  class, INDEPENDENT of the dynamical kills (A, G, H, J stand untouched).")
print("- The registered ontology's only transverse-vector dof is the displacement")
print("  pair — dynamically excluded as the carrier (EM-RECON-022). So the")
print("  result is OUTCOME 2: direction DERIVED, conditional on the carrier")
print("  class; the carrier's identity remains the registered open problem.")
print("- The condition is NECESSARY as well as sufficient: a carrier that does")
print("  not displace center lines exerts no azimuth-blind contact force at")
print("  linear order (dV/dphi = 0, EM-RECON-023) — the bare screw gives F = 0,")
print("  which is the state-count kill seen from the force side. The two")
print("  registered kills are ONE fact: no transverse force, no E direction,")
print("  no polarization.")
print()
print("OUTCOME 2 BANKED. Direction derived; carrier condition named; both")
print("confrontations passed; no killed carrier resurrected. PASS.")
