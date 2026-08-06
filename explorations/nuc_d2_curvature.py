"""
COMMISSION NUC-D2: the curvature term (2026-08-06 session).
Primary: expand the finite-range coordination deficit to O(1/R) analytically,
extract the A^(1/3) curvature coefficient BLIND (before comparing to -7.1),
then run the joint closure in the registered harness.
"""
import numpy as np, sys
from pathlib import Path
ROOT = Path("/home/claude/rope5/rope")
sys.path.insert(0, str(ROOT / "explorations"))
sys.path.insert(0, str(ROOT / "benchmarks" / "em"))
import nuc_a_asymmetry as na
import nuc_c_coulomb as nc
from atomic_mass_predictor import B_EXP
import nuc_d_surface as nd  # noqa: F401  (runs baseline; kernel + constants)

RHO0, A_D = nc.RHO0, nc.A_D
R_C = (3*12/(4*np.pi*RHO0))**(1/3)
ETA = 0.5763

print("\n"+"="*72)
print("D2-1: EXACT LEPTODERMOUS EXPANSION OF THE KERNEL DEFICIT (analytic)")
print("="*72)
# Sharp uniform ball, top-hat kernel range r_c. Pair count:
#   pairs = (rho^2/2) * Int_{s<r_c} 4 pi s^2 V_ov(s) ds,
#   V_ov(s) = (4pi/3)R^3 - pi R^2 s + (pi/12) s^3   (ball covariogram, EXACT)
# => pairs = 6A - (rho^2/2) pi^2 R^2 r_c^4 + (rho^2/2)(pi^2/18) r_c^6
# => D(A) = 6A - pairs = c2 A^(2/3) + c0, with NO A^(1/3) TERM:
#   the ball covariogram has terms s^0, s^1, s^3 -- no s^2 -- so the deficit
#   series has powers (r_c/R)^4 ~ A^(2/3) and (r_c/R)^6 ~ A^0 and NOTHING
#   between. c1 (curvature) = 0 IDENTICALLY.
c2 = (9/32)*12**(4/3)   # from (rho^2/2) pi^2 R^2 r_c^4 with z=12 normalization
c0 = -(1/64)*144
print(f"analytic: D(A) = {c2:.4f} A^(2/3) + 0*A^(1/3) + ({c0:.3f})")
print("THEOREM (holds for ANY isotropic bond weight w(s)): the uniform-ball")
print("pair-distance density p(s) = 3s^2/R^3 - (9/4)s^3/R^4 + (3/16)s^5/R^6")
print("contains NO s^4 term, so Int w(s)p(s)ds has A^1, A^(2/3), A^0 pieces")
print("only. The kernel's leptodermous expansion TERMINATES: curvature = 0.")

print("\n-- numerical confirmation (fit the package's own D_sharp(A)) --")
As = np.array([16,24,40,60,80,100,120,140,160,180,208,238,280,340,400])
Dn = np.array([nd.surface_deficit(int(A), "sharp") for A in As])
M = np.vstack([As**(2/3), As**(1/3), np.ones_like(As, float)]).T
coef, *_ = np.linalg.lstsq(M, Dn, rcond=None)
res = Dn - M@coef
print(f"   fit: c2={coef[0]:.4f}  c1={coef[1]:.4f}  c0={coef[2]:.3f}  "
      f"(fit rms {np.sqrt((res**2).mean()):.2e})")
print(f"   analytic c2={c2:.4f}, c1=0, c0={c0:.3f} -> "
      f"{'MATCH' if abs(coef[0]-c2)<0.05 and abs(coef[1])<0.05 else 'MISMATCH'}")

print("\n-- weight-independence check (two non-flat bond weights) --")
def weighted_deficit(A, w):
    """pairs with isotropic weight w(s), sharp ball, exact covariogram."""
    R = (3*A/(4*np.pi*RHO0))**(1/3)
    s = np.linspace(1e-6, R_C, 4000)
    Vov = (4*np.pi/3)*R**3 - np.pi*R**2*s + (np.pi/12)*s**3
    pairs = (RHO0**2/2)*np.trapezoid(4*np.pi*s**2*Vov*w(s), s)
    bulk = (RHO0**2/2)*(4*np.pi/3)*R**3*np.trapezoid(4*np.pi*s**2*w(s), s)
    return bulk - pairs      # deficit in the weight's own bulk units
for lab, w in (("linear taper w=1-s/r_c", lambda s: 1-s/R_C),
               ("gaussian w=exp(-(s/r_c)^2)", lambda s: np.exp(-(s/R_C)**2))):
    Dw = np.array([weighted_deficit(int(A), w) for A in As])
    cw, *_ = np.linalg.lstsq(M, Dw, rcond=None)
    print(f"   {lab}: c1 = {cw[1]:+.4f}  (curvature {'ABSENT' if abs(cw[1])<0.02*abs(cw[0]) else 'PRESENT'})")

print("\n"+"="*72)
print("D2-2: WHAT THE TABLE NEEDS (loaded only after D2-1 committed)")
print("="*72)
eps = 2.724   # the registered sharp-kernel/B2 calibration (reproduced above)
print(f"target missing shape: -7.1 A^(1/3) in energy = c1_needed = 7.1/eps "
      f"= {7.1/eps:.2f} in deficit units; DERIVED c1 = 0. The kernel's O(1/R)")
print("CANNOT supply the curvature term -- not by magnitude, by exact zero.")

print("\n"+"="*72)
print("D2-3: JOINT CLOSURE (charter prescription, executed as chartered)")
print("="*72)
print("Derived curvature = 0 -> the joint surface+curvature model IS NUC-D's")
print("model. S1/S2 unchanged: rms 11.9, heavy 1.05%, S2 1.8 (baseline")
print("reproduced above). The charter's ~4-5 MeV closure is NOT reached.")
print("Control (their diagnostic, reproduced): subtract the named shape")
A0, Z0, B0 = B_EXP["Ca-40"]
EC = {}
def ECf(A,Z):
    if (A,Z) not in EC: EC[(A,Z)] = nc.corrected_EC(A,Z,1-ETA)
    return EC[(A,Z)]
Ds = {}
def Dsh(A):
    if A not in Ds: Ds[A] = nd.surface_deficit(A,"sharp")
    return Ds[A]
nucs = na.load_table()
e = ETA**2
eps_cal = (B0 + ECf(A0,Z0))/(6*A0 - Dsh(A0))
aA = 16.6 + 6*eps_cal*(1-e)/(3+e)
def B(A,Z,shape=False):
    b = eps_cal*(6*A - Dsh(A)) - ECf(A,Z) - aA*(A-2*Z)**2/A
    if shape: b += 3.1*A**(2/3) - 0.25*A - 7.1*A**(1/3)
    return b
for lab, sh in (("baseline", False), ("baseline + named shape (control)", True)):
    R = np.array([B(A,Z,sh)-Be for _,A,Z,Be in nucs])
    Be = np.array([b for *_, b in nucs]); Aa = np.array([a for _,a,_,_ in nucs],float)
    hv = Aa>150
    print(f"   [{lab}] S1 rms {np.sqrt((R**2).mean()):.1f}, heavy "
          f"{np.mean(np.abs(R[hv]/Be[hv]))*100:.2f}%")

print("\n"+"="*72)
print("D2-4: LEAD PROBE -- does profile-curvature coupling carry the shape?")
print("="*72)
print("(The registered no-go killed the DOUBLE-SMEAR for the SURFACE magnitude.")
print(" Here we only ask whether the profile+kernel deficit CONTAINS an A^(1/3)")
print(" term of the right scale -- a pointer to where curvature physics lives,")
print(" not a model. Stamped LEAD if yes.)")
Dd = np.array([nd.surface_deficit(int(A),"diffuse") for A in As])
cd, *_ = np.linalg.lstsq(M, Dd, rcond=None)
print(f"   diffuse+kernel fit: c2={cd[0]:.3f}  c1={cd[1]:+.3f}  c0={cd[2]:.2f}")
print(f"   c1 x eps = {cd[1]*eps:+.2f} MeV vs needed -7.1 MeV")
print("   (sign and scale reported as found; verdict in the results doc)")
print("\nD2 COMPUTATIONS COMPLETE.")

# --- Appended after review: exact-deficit baseline, sign-settled residual,
#     grid-convergence audit, and the lead's second-prediction run are in the
#     session transcript; consolidated results in COMMISSION_NUC_D2_results.md
