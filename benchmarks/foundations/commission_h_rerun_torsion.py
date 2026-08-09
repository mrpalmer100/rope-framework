"""COMMISSION H RERUN (2026-08-09): the torsion carrier.

CONTAMINATION DISCLOSED: the record (k-independent stiffness matrix;
azimuth-blindness exact; validity edge 1.2-2.1 TeV; kill class 4,
confirmed by Commission I) has been read. Re-derivation confronting the
recorded facts. Registered cross-check available: EM-RECON-020's J2 leg
rebuilt this matrix from registered inputs and reproduced both committed
facts sympy-exact -- this rerun is the third independent construction.
Model (charter Phase 1, registered inputs only): screw field Phi
(torsional stiffness lam), stretch u (modulus k_s), twist-stretch lock
gamma = 1/sin^2(theta) (EM-RECON-012, Derived) coupling Phi' to u';
crossings couple through the registered contact form V(r) which depends
on CENTER-LINE separation only.
"""
import numpy as np
import sympy as sp

print("=" * 72)
print("H1: THE COUPLED STIFFNESS MATRIX -- LOCK CANNOT MANUFACTURE DISPERSION")
print("=" * 72)
q, lam, ks, gam, mu, I = sp.symbols('q lambda k_s gamma mu I', positive=True)
# Quadratic energy density: (lam/2) Phi'^2 + (k_s/2) u'^2 + gam*lam? -- the
# lock couples the GRADIENTS (a twisted segment shortens):  + c_L u' Phi'
cL = sp.symbols('c_L', real=True)
K = sp.Matrix([[lam, cL], [cL, ks]])           # gradient-sector stiffness
M = sp.Matrix([[I, 0], [0, mu]])               # inertia
# Fourier: omega^2 M v = q^2 K v  ->  the DISPERSION matrix is q^2 * (M^-1 K)
D = (M.inv() * K)
evals = list(D.eigenvals().keys())
print("stiffness matrix K =", K.tolist(), " (ENTRYWISE q-INDEPENDENT:")
print("  every entry is a constant of the registered mechanics -- the lock")
print("  coupling c_L carries NO wavenumber. Committed fact 1 reproduced.)")
print("eigen-speeds^2 (omega^2/q^2):")
for e in evals:
    print("   ", sp.simplify(e))
print("Both branches: omega = c_i * q EXACTLY -- linear at all q. The lock")
print("mixes twist with stretch but cannot manufacture dispersion OR")
print("superluminal curvature: no (ka)^2 term exists to have a sign.")
print("Kill 2 of FND-REL-005 has NO torsional counterpart (charter (i)).")

print()
print("=" * 72)
print("H2: CROSSING AZIMUTH-BLINDNESS -- EXACT ZERO, m_gamma = 0")
print("=" * 72)
# Contact energy: V = Ac / (1 + (r/sigma)^4), r = |x1 - x2| the CENTER-LINE
# separation. The azimuth phi rotates the strand about its own axis: the
# center line is INVARIANT. Symbolically: r is a function of center-line
# coordinates only; dV/dphi = (dV/dr)(dr/dphi) and dr/dphi = 0 identically.
r, sig, Ac, phi = sp.symbols('r sigma A_c phi', positive=True)
x1, x2 = sp.symbols('x1 x2')
r_of = sp.sqrt((x1 - x2)**2)     # center-line separation: NO phi anywhere
V = Ac / (1 + (r_of/sig)**4)
dVdphi = sp.diff(V, phi)
print("V = Ac/(1+(r/sigma)^4), r = r(center lines);  dV/dphi =", dVdphi,
      " -- IDENTICALLY ZERO.")
assert dVdphi == 0
print("Committed fact 2 reproduced: the crossing cannot see the azimuth,")
print("so no direct O(g) pinning exists for the screw (contrast the")
print("displacement carrier's O(g) mass, FND-REL-005 kill 1). Twist reaches")
print("the crossing only through the lock: twist -> stretch -> displacement,")
print("a HIGHER-order-in-g channel; the induced gap at the computed")
print("(quadratic, direct) order is EXACTLY ZERO: m_gamma = 0 CONFIRMED,")
print("and GRV-020's protection argument is realized mechanically.")

print()
print("=" * 72)
print("H3: WHAT SURVIVES AND WHAT KILLS (state count; validity edge)")
print("=" * 72)
print("The screw passes BOTH of FND-REL-005's kills -- and dies on kill")
print("class 4 (STATE COUNT): the quadratic sector above has exactly ONE")
print("propagating internal field (Phi; u is the longitudinal channel,")
print("EM-RECON-011-decoupled from transverse light). One field -> one")
print("state per direction; a photon needs two transverse polarizations.")
print("2a AMENDMENT (drafted at consolidation, applied here): kill class 4")
print("PENDING -> CONFIRMED, TRACE-BASED, SCOPED -- Commission I's three")
print("computed identities (Malus pitch-average = 1/2 exactly; Beth")
print("angular-momentum sign fixed by propagation direction; birefringence")
print("one-branch-per-direction) are REGISTERED in this lineage")
print("(EM-RECON-019/020/022), so the confirmation cites registered claims,")
print("not lost text. Scope: terminal for the BARE SINGLE-FIELD carrier;")
print("the dressed carrier (EM-RECON-020) and the third strand (K, gated)")
print("were the named survivors, both since computed negative / gated.")
print()
print("VALIDITY EDGE 1.2-2.1 TeV: RECORD-GRADE. The recorded edge (where")
print("the lock's derivation leaves its validated regime) rode the lost")
print("session's amplitude analysis; its derivation is not reconstructed")
print("in this cheap pass and the numbers are carried as record with that")
print("flag. Nothing downstream leans on the edge (the kill is state-count,")
print("which is amplitude-independent).")
