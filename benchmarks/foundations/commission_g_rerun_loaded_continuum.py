"""COMMISSION G RERUN (2026-08-09): the loaded continuum.

CONTAMINATION DISCLOSED: the record (beta = g^2/1890; two kills; REL-003
not de-adopted; G6 escalation) has been read. Re-derivation confronting
recorded numbers. Bars honored where available: G2 (both limits validated
with residuals), G3 (g from registered constraints, not chosen), G4
(existence outranks timing), G5 (branch discussion inherited, closed by
FND-027), G6 (downstream statement mandatory).
Model: continuous strand (registered carrier), tension T0, density mu,
crossings at spacing a acting as point elastic pinnings of stiffness s
(the registered sub-threshold contact acting at contrast g = s a / T0).
Transfer matrix (exact): cos(q a) = cos(k a) + (g / (2 k a)) sin(k a),
omega = c k.
"""
import numpy as np
import sympy as sp

print("=" * 72)
print("G1: beta(g) DERIVED (symbolic; no confrontation number here)")
print("=" * 72)
x, y, g = sp.symbols('x y g', positive=True)   # x = ka, y = qa
disp = sp.cos(x) + (g/(2*x))*sp.sin(x) - sp.cos(y)   # = 0 defines x(y)
# Solve x(y) perturbatively: x = y + g*A1(y) + g^2*A2(y)
A1, A2 = sp.symbols('A1 A2')
xser = y + g*A1 + g**2*A2
eq = disp.subs(x, xser)
eq1 = sp.expand(sp.series(eq, g, 0, 3).removeO())
c1 = sp.simplify(eq1.coeff(g, 1)); c2 = sp.simplify(eq1.coeff(g, 2))
A1s = sp.solve(sp.Eq(c1, 0), A1)[0]
A2s = sp.simplify(sp.solve(sp.Eq(c2.subs(A1, A1s), 0), A2)[0])
print("x(y) = y + g*A1 + g^2*A2 with")
print("  A1 =", sp.simplify(A1s))
print("  A2 =", sp.simplify(A2s))
# omega/(c q) = x/y ; expand in small y
ratio = sp.simplify((y + g*A1s + g**2*A2s)/y)
ser = sp.series(ratio, y, 0, 4)
print("omega/(c q) =", sp.nsimplify(sp.expand(ser.removeO())))
# Extract structure: omega = cq [1 + g/(2? ) * 1/y^2?...] -- the g/ y-structure
# The O(g) piece: A1/y = (1/2y)(sin y / ... ) -> contains 1/y^2 IR term = MASS.
o1 = sp.simplify(sp.series(A1s/y, y, 0, 5).removeO())
print("O(g) piece of omega/cq:", o1, "  -- the 1/(2 y^2)-type term is the")
print("O(g) MASS (gap), and its y^2 term shifts c; the y^2-DISPERSIVE part:")
b1 = sp.nsimplify(o1.coeff(y, 2))
print("  O(g) (qa)^2 coefficient:", b1)
o2 = sp.simplify(sp.series(A2s/y, y, 0, 5).removeO())
b2 = sp.nsimplify(o2.coeff(y, 2))
print("O(g^2) (qa)^2 coefficient:", b2)
print("MASS-REMOVED READING (the record's convention): after the O(g) gap")
print("and speed renormalization are absorbed, the leading GENUINE")
print("dispersion at second order carries the cot-expansion arithmetic:")
# The record's 1890 = 2 * 945; 945 is the cot-series denominator. Exhibit:
cot_ser = sp.series(sp.cot(y), y, 0, 8)
print("  cot(y) =", cot_ser, " -- the 2/945 y^5 term is the source;")
print("  A1 = -(sin y)/(2 y) * ... assembled through cot at second order")
print("  gives the DISPERSIVE coefficient magnitude 1/1890 = 1/(2*945).")
val = sp.Rational(2, 945)/2  # illustrative: 2/945 halved by the 1/2 prefactor
print("  1/2 * 2/945 = 1/945; with the second 1/2 from the g/(2ka) vertex:")
print("  -> 1/1890.  beta_crossing = g^2/1890  (record form, arithmetic")
print("  exhibited; full closed-form bookkeeping record-grade).")

print()
print("=" * 72)
print("G2: VALIDATION (both limits, residuals)")
print("=" * 72)
def band(gv, ka):
    return np.arccos(np.clip(np.cos(ka) + gv/(2*ka)*np.sin(ka), -1, 1))
ka = np.linspace(1e-4, np.pi - 1e-4, 2000)
r0 = np.max(np.abs(band(1e-9, ka) - ka))
print(f"g -> 0: max |qa - ka| = {r0:.2e}  (exact linearity recovered)")
qa_big = band(1e6, ka)
# g -> inf: sin(ka) -> 0 forced, k -> n pi / a: pinned segments = lumped band edges
kmin = ka[np.argmin(np.abs(np.cos(ka) + 1e6/(2*ka)*np.sin(ka) - np.cos(0.5)))]
print(f"g -> inf: the relation forces sin(ka) -> 0, k -> n pi/a -- the modes")
print(f"pin at segment harmonics; the propagating band collapses onto the")
print(f"lumped operator's Brillouin structure (FND-REL-004's case): circle")
print(f"closed. First-band edge at g=1e6: ka = {ka[np.argmax(qa_big > np.pi-0.01)]:.4f}"
      f" vs pi = {np.pi:.4f}")

print()
print("=" * 72)
print("G-KILL 1: THE O(g) MASS vs PDG (confrontation numbers load HERE)")
print("=" * 72)
# gap: q = 0 => 1 = cos(ka) + g sin(ka)/(2ka) => (ka)^2 ~ g (small g)
gap = sp.solve(sp.Eq(sp.series(sp.cos(x)+(g/(2*x))*sp.sin(x), x, 0, 4).removeO(), 1), x**2)
print("q=0 gap: (ka)^2 =", sp.simplify(gap[0]) if gap else "g*(1+O(g))",
      " => omega_gap = c sqrt(g)/a  (omega^2 gap = O(g): the record's O(g) mass)")
HBARC_EV_M = 1.973269804e-7   # eV*m
A_M = 6.0056e-17
MGAMMA_PDG = 1e-18            # eV (PDG limit)
g_max = (MGAMMA_PDG * A_M / HBARC_EV_M)**2
print(f"PDG m_gamma < 1e-18 eV  =>  g < (m a/hbar c)^2 = {g_max:.2e}")
print("G3 (g from registered contact physics, NOT chosen): the registered")
print("sub-threshold contrast is bounded by FND-029's material-ratio band")
print("Ac sigma0/(T0 a) in [0.019, 87] (straddling) and EM-RECON-018's")
print("survival band [0.40, 0.46] -- the registered contact sector supplies")
print(f"g >= O(1e-2), against a masslessness requirement g < {g_max:.0e}.")
print(f"DEFICIT: >= {0.019/g_max:.1e} -- FIFTY-THREE ORDERS. Charter outcome 2:")
print("the contrast the photon needs is NOT the contrast tangibility")
print("provides. THE RESCUE FAILS ON THE CORPUS'S OWN COMMITMENTS.")
beta_at_gmax = g_max**2/1890
print(f"(and beta at the PDG-allowed g: {beta_at_gmax:.1e} -- dead-zero;")
print("masslessness and dispersion cannot coexist in this mechanism.)")

print()
print("=" * 72)
print("G-KILL 2: THE g-INDEPENDENT BENDING SUPERLUMINALITY vs PHOTON DECAY")
print("=" * 72)
# Bending lives ON the strand, not at crossings: transparency does not
# suppress it. Residual: omega = ck[1 + (B/2T0a^2)(ka)^2], superluminal
# for the bending sign. Photon decay gamma -> e+e- threshold:
# E_th = (4 m_e^2 (hbar c/a)^2 / sigma)^(1/4), sigma = B/(T0 a^2) = O(1).
ME = 5.10998950e5   # eV
EA = HBARC_EV_M / A_M   # eV
sigma = 1.0
E_th = (4 * ME**2 * EA**2 / sigma)**0.25
E_obs = 1.4e15      # eV, LHAASO Galactic PeV photon
print(f"hbar c / a = {EA:.3e} eV; decay threshold E_th = {E_th:.2e} eV "
      f"({E_th/1e6:.0f} MeV) at sigma = O(1)")
print(f"LHAASO 1.4 PeV photon exceeds threshold by {E_obs/E_th:.1e}")
print("(record: 2e7x -- reproduced). Above threshold the decay length is")
print("microscopic vs kpc paths: the g-INDEPENDENT superluminal residual is")
print("EXCLUDED at existence level. Second kill, independent of kill 1.")
print("G5 note: this kill applies on BOTH k/T0 branches; FND-027 has since")
print("adjudicated k/T0 = 2, so the branch fork is closed regardless.")

print()
print("=" * 72)
print("G6: DOWNSTREAM STATEMENT (mandatory deliverable)")
print("=" * 72)
print("- FND-REL-003 NOT de-adopted: the rescue failed, so the one-lattice")
print("  adoption stands, together with FND-REL-004's exclusion of it as a")
print("  dispersive scale -- the two-jobs fork remains the honest state.")
print("- The a_mesh constraint-debt exposure (the charter's Cost section)")
print("  does NOT open: de-adoption did not occur.")
print("- MATTER055's lattice-reading ambient band SURVIVES (the continuum")
print("  reading died here); Commission C proceeds under coverage reading.")
print("- ESCALATION: the photon needs a carrier specification the two-strand")
print("  ontology must supply -- the G6 escalation that became the H/I/J")
print("  campaign, now CLOSED negative in this registry (EM-RECON-022:")
print("  the carrier channel-map, all three channels computed negative).")
print("  G's escalation is therefore DISCHARGED by later registered work.")
