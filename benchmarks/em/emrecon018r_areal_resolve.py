"""EM-RECON-018-R: the standoff refinement RE-SOLVED under FND-068's
corrected areal convention (pi, not 3 pi). Bars locked first
(analysis/EMRECON018R_resolve_bars_LOCKED.md). Machinery reused verbatim
from benchmarks/em/emrecon018_standoff_refinement.py; only the coverage
coefficient changes, per the locked charter."""
import numpy as np

FC = 0.309  # registered areal coverage threshold (FND-MATTER-038; window 0.073-0.348)
print("== EM-RECON-018-R: the areal re-solve ==\n")

# --- B1: corrected coverage counting (a plane is pierced by ONE family) ---
w_over_a = np.sqrt(4.0 * FC / np.pi)
w_over_a_old = np.sqrt(4.0 * FC / (3.0 * np.pi))
print(f"   corrected counting: pi w^2/(4 a^2) = f_c  ->  w/a = {w_over_a:.4f}")
print(f"   (superseded volume-fraction value: {w_over_a_old:.4f}; factor sqrt(3) = {w_over_a/w_over_a_old:.4f})")
for fc in (0.073, 0.348):
    print(f"     sensitivity: f_c = {fc}: w/a = {np.sqrt(4*fc/np.pi):.4f}")
print("   sigma_0 = w unchanged (the interpenetration identification is")
print("   convention-independent).\n")

# --- B2: the two admissible standoff readings, both carried ---
r1 = 1.0                          # reading A: in-family touching, d0 = w = sigma0
r2 = 1.0 / (2.0 * w_over_a)       # reading B: cross-family half-spacing, d0 = a/2
print(f"   reading A (in-family touching):      d0/sigma0 = {r1:.3f}  (unchanged)")
print(f"   reading B (cross-family a/2 offset): d0/sigma0 = {r2:.3f}  (was 1.381)")
if r2 < 1.0:
    print("   REPORTED PER B2: reading B now sits BELOW touching separation --")
    print("   under the wider strand the half-spacing offset is closer than one")
    print("   contact range. Geometric interpretation question carried, not")
    print("   resolved; the reading is carried per the locked bar.\n")

# --- C(d0/sigma0), reused verbatim from EM-RECON-017 ---
def crossing_energy(d, sig, Ac=1.0, S=8.0, n=4001):
    s = np.linspace(-S, S, n)
    r = np.sqrt(d*d + s*s)
    return Ac * np.trapezoid(1.0/(1.0 + (r/sig)**4), s)

def C_of(ratio, h=1e-4):
    def Etot(e):
        sig = 1.0/np.sqrt(1.0 + e)
        return 2.0 * crossing_energy(ratio, sig)
    return (Etot(h) - 2*Etot(0.0) + Etot(-h)) / h**2

CA, CB = C_of(r1), C_of(r2)
print(f"   C(A) = {CA:.3f}   C(B) = {CB:.3f}")
tA, tB = 2.0/CA, 2.0/CB
lo, hi = min(tA, tB), max(tA, tB)
print(f"   survival threshold on E_x/(T0 a): reading A {tA:.3f}, reading B {tB:.3f}")
print(f"\n   RE-SOLVED BAND: [{lo:.3f}, {hi:.3f}]   (supersedes [0.40, 0.46])")
print(f"   band width vs superseded: {(hi-lo):.3f} vs 0.063\n")

# --- B3: confrontation with FND-029's displayed estimates (not adopted) ---
print("-- confrontation with FND-029's displayed estimates (not adopted) --")
EB, T0A = 4.716, 0.16268
mb_max_lo = EB / (hi * T0A)
mb_max_hi = EB / (lo * T0A)
print(f"   survival in multiplicity terms (L1 = 1): m_b < {mb_max_lo:.0f} .. {mb_max_hi:.0f}")
print(f"   (factor-3 L1 band widens this to roughly {mb_max_lo/3:.0f} .. {mb_max_hi*3:.0f})")
for name, mb in [("single pair", 1.0), ("surface line ~22", 22.0),
                 ("contact patch ~63", 63.0), ("full section ~498", 498.0)]:
    r = EB / (mb * T0A)
    verdict = "SURVIVES" if r > hi else ("FAILS" if r < lo else "IN-BAND")
    print(f"   m_b = {name:20s}: ratio {r:7.2f}  vs [{lo:.3f}, {hi:.3f}]  {verdict}")

# --- W1 value propagation (FND-066: w must carry its a) ---
print("\n-- W1 (vacuum-mesh strand width) under the corrected ratio, per a --")
print("   a values recovered from FND-066's registered W1 values at the")
print("   superseded ratio 0.3621 (0.0362 / 0.0059 / 0.0035 fm):")
for label, w_old_fm in [("Lorentz-bound a", 0.0362),
                        ("FND-040 re-solve reading 1", 0.0059),
                        ("FND-040 re-solve reading 2", 0.0035)]:
    a_fm = w_old_fm / w_over_a_old
    w_new_fm = w_over_a * a_fm
    print(f"   {label:26s}: a = {a_fm:.4f} fm -> W1 = {w_new_fm:.4f} fm (was {w_old_fm:.4f})")
print("\n   Every W1 value scales by sqrt(3) = 1.732; the factor-of-ten spread")
print("   across a values (FND-066) is unchanged and its refusal stands.")
