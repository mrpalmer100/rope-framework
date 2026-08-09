"""EM-RECON-018: the threshold standoff derived from the registered
coverage fraction; the survival band narrowed. Bars locked first
(analysis/EMRECON018_standoff_bars_LOCKED.md)."""
import numpy as np

FC = 0.309                 # registered percolation coverage (window 0.073-0.348)
print("== EM-RECON-018: the standoff refinement ==\n")

# --- width/spacing from coverage counting (3 families of width-w strands) ---
w_over_a = np.sqrt(4.0 * FC / (3.0 * np.pi))
print(f"   coverage counting: 3 x pi w^2/(4 a^2) = f_c  ->  w/a = {w_over_a:.4f}")
for fc in (0.073, 0.348):
    print(f"     sensitivity: f_c = {fc}: w/a = {np.sqrt(4*fc/(3*np.pi)):.4f}")
print("   sigma_0 = w (the interpenetration scale: surfaces interact at")
print("   center distance ~ one width; the contact form's knee IS the")
print("   touching condition).\n")

# --- the admissible standoff readings (enumerated, both carried) ---
r1 = 1.0                         # in-family: touching neighbors, d0 = w = sigma0
r2 = 1.0 / (2.0 * w_over_a)      # cross-family: half-spacing offset, d0 = a/2
print(f"   reading A (in-family touching):      d0/sigma0 = {r1:.3f}")
print(f"   reading B (cross-family a/2 offset): d0/sigma0 = {r2:.3f}\n")

# --- C(d0/sigma0) reused from EM-RECON-017's computation ---
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
print(f"\n   REFINED BAND: [{lo:.2f}, {hi:.2f}]   (was [0.40, 3.00] -- an")
print(f"   {(3.00-0.40)/(hi-lo):.0f}-fold narrowing). The coverage threshold FORCES the")
print("   standoff into the contact form's knee region; the tight-standoff")
print("   tail of the old band was never physically accessible.\n")

# --- confrontation with FND-029 (sealed until here, bar 3) ---
print("-- confrontation with FND-029's displayed estimates (not adopted) --")
EB, T0A = 4.716, 0.16268
mb_max_lo = EB / (hi * T0A)     # most demanding threshold
mb_max_hi = EB / (lo * T0A)     # least demanding
print(f"   survival in multiplicity terms (L1 = 1): m_b < {mb_max_lo:.0f} .. {mb_max_hi:.0f}")
for name, mb in [("single pair", 1.0), ("surface line ~22", 22.0),
                 ("contact patch ~63", 63.0), ("full section ~498", 498.0)]:
    r = EB / (mb * T0A)
    verdict = "SURVIVES" if r > hi else ("FAILS" if r < lo else "IN-BAND")
    print(f"   m_b = {name:20s}: ratio {r:7.2f}  vs [{lo:.2f}, {hi:.2f}]  {verdict}")
print("\n   The refinement CONVERTS the picture: the survival question is now")
print("   m_b <~ 60-70 strand pairs per bundle bond (at L1 = 1; the L1")
print("   factor-3 band widens this to ~20-200). The line and patch")
print("   geometries survive; only full-cross-section contact fails.")
print("   All still awaits w -- but the target the width must hit is now")
print("   an order of magnitude sharper.")
