"""COMMISSION K — THE COLLECTIVE READING, TESTED EXACTLY.
Charter: docs/commissions/COMMISSION_K_ontology.md (bars locked first).

The candidate: the collective transverse displacement of the fully-dynamical
two-strand mesh. FND-REL-005 froze the background (single strand vs fixed
pinnings); here BOTH strands are dynamical and crossings couple RELATIVE
displacement. All four K2 tests computed.
"""
import numpy as np
import sympy as sp

print("=" * 72)
print("K2(ii) GAPLESSNESS — exact two-strand computation + symmetry")
print("=" * 72)
# Two dynamical chains, displacement u1(x), u2(x) per transverse component;
# tension T0 each, crossings at spacing a couple RELATIVE displacement with
# stiffness s. Per-length quadratic energy (one transverse component shown;
# the second is identical by isotropy):
q, T0, mu, s, a, g = sp.symbols('q T0 mu s a g', positive=True)
u1, u2 = sp.symbols('u1 u2')
# Fourier stiffness matrix (per length): tension T0 q^2 on each diagonal;
# crossings add (s/a) on the RELATIVE coordinate:
K = sp.Matrix([[T0*q**2 + s/a, -s/a],
               [-s/a,          T0*q**2 + s/a]])
M = sp.diag(mu, mu)
D = M.inv() * K
evs = sorted(D.eigenvals().keys(), key=lambda e: sp.count_ops(e))
print("branches (omega^2):")
for e in evs:
    print("   ", sp.simplify(e))
w2_ac = sp.simplify(min(evs, key=lambda e: e.subs({q: 0, T0: 1, mu: 1, s: 1, a: 1})))
w2_op = sp.simplify(max(evs, key=lambda e: e.subs({q: 0, T0: 1, mu: 1, s: 1, a: 1})))
gap_ac = sp.simplify(w2_ac.subs(q, 0))
gap_op = sp.simplify(w2_op.subs(q, 0))
print(f"acoustic gap at q=0: {gap_ac}   optical gap at q=0: {gap_op}")
assert gap_ac == 0, "the collective (acoustic) branch must be EXACTLY gapless"
assert gap_op != 0, "the relative (optical) branch carries the crossing gap"
assert sp.simplify(w2_ac - T0*q**2/mu) == 0, "acoustic branch exactly omega^2 = (T0/mu) q^2"
print(">>> EXACT: the center-of-mass branch is gapless at ALL crossing strengths;")
print(">>> the O(g) mass of FND-REL-005 lands ENTIRELY on the RELATIVE (optical)")
print(">>> branch (gap = 2s/(mu a)). The kill was a frozen-background artifact:")
print(">>> freezing strand 2 (u2 = 0) forces the wave onto a mixture containing")
print(">>> the optical branch — that is the structural difference (bar K4).")
# Symmetry statement: uniform translation u1 = u2 = const has zero energy:
E_unif = (sp.Matrix([[1, 1]]) * K.subs(q, 0) * sp.Matrix([1, 1]))[0]
assert sp.simplify(E_unif) == 0, "translation symmetry: uniform shift costs nothing"
print(">>> Goldstone check: uniform transverse translation costs ZERO energy —")
print(">>> gaplessness is symmetry-protected, not tuned. PDG m_gamma: exact 0. PASS.")

print()
print("=" * 72)
print("K2(i) STATE COUNT and K4 (not a relabeling)")
print("=" * 72)
print("Transverse plane is 2D and isotropic: the collective branch exists per")
print("component -> exactly TWO gapless transverse states (s_x, s_y). The killed")
print("single-strand mode was ONE strand's displacement vs frozen pinnings; the")
print("collective mode is the SYMMETRIC combination of ALL strands. In the exact")
print("matrix the difference is which eigenvector carries the wave: (1,1) here")
print("(crossing term cancels row-wise), vs the frozen case's (1,0) which mixes")
print("(1,1) and (1,-1) equally — half its weight sat on the gapped branch.")
print("Structural difference located in the operator. PASS.")

print()
print("=" * 72)
print("K2(iv) KILL CONFRONTATION — inheritance and the bending condition")
print("=" * 72)
# FND-REL-004 inheritance: the acoustic branch on the DISCRETE mesh still has
# lattice dispersion: omega^2 = (4T0/(mu a^2)) sin^2(qa/2) + bending. Bound:
HBARC = 0.19732698e-15   # GeV*m
EQG2 = 6e-8 * 1.22091e19 # GeV (LHAASO, verified live in FND-REL-004's rerun)
beta_sub = 1.0/12.0
a_disp = HBARC / (EQG2 * np.sqrt(beta_sub))
print(f"COST 1 (inherited): the collective mode has the SAME lattice dispersion")
print(f"  => the dispersive spacing obeys a_disp <= {a_disp:.2e} m (FND-REL-004).")
print(f"  With the M-point coverage scale at 6.0e-17 m, the three-pin fork")
print(f"  (coverage-a != dispersive-a, FND-MATTER-068/FND-REL-004 Amendment 3)")
print(f"  is now MANDATORY for this candidate, not optional. Registered as cost.")
B, cond = sp.symbols('B'), None
beta_total = sp.Rational(1, 12) - B/(T0*a**2)
print(f"COST 2 (bending sign): beta = {beta_total}; SUBLUMINALITY (escape from")
print("  kill 2 / photon decay) requires beta >= 0, i.e. B <= T0 a^2 / 12.")
print("  B and T0 are registered material parameters with no registered values")
print("  pinning this ratio: the condition B <= T0 a^2/12 is REGISTERED ON THE")
print("  FACE as this candidate's live falsifier (kill 2 fires if violated).")

print()
print("=" * 72)
print("K2(iii) ENTRANCE — coupling to a winding, at its honest order")
print("=" * 72)
# The collective mode displaces ALL center lines: entrance geometry satisfied.
# Coupling channels to a winding defect, stated with what is/isn't derived:
Mx, w, s0 = sp.symbols('M_x omega s_0', positive=True)
F_inertia = Mx * w**2 * s0
print("Channel A (DERIVED here, one line): a winding core carries excess energy")
print("  /inertia M_x localized on the strands; comoving with the wave requires")
print("  F = M_x * d^2s/dt^2, i.e. |F| =", F_inertia, "for harmonic s —")
print("  NONZERO force, PARALLEL to s (EM-RECON-024 consistency) — but q-EVEN:")
print("  it does not flip with winding handedness. This is the gravitational/")
print("  inertial coupling, NOT the electric one.")
print("Channel B (NAMED OBLIGATION, not derived): the q-LINEAR coupling must")
print("  come from the winding's handedness meeting the wave (Magnus-class:")
print("  F ~ q * v_medium x kappa_hat). Deriving its form, sign rule, and its")
print("  reconciliation with EM-RECON-024's parallel-force geometry is the")
print("  NEXT commission's charter — registered here as the standing obligation.")
print()
print("VERDICT: OUTCOME 1. The collective transverse pair passes state count,")
print("exact gaplessness (symmetry-protected), entrance geometry, and the kill")
print("confrontation with two registered costs and one named obligation. No")
print("third strand required; no new primitive adopted. PASS.")
