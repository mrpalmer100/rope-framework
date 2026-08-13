"""COMMISSION RESH -- T2 discrimination push.
Executed under analysis/RESH_discrimination_push_bars_LOCKED.md."""
import sympy as sp
import numpy as np

print("HALF 1 -- symbolic checks on the registered functional")
k, T0, Kc, f, g = sp.symbols('k T0 K_c f gp', positive=True)
# Q1 machine check: FND-040's coefficient from T0*sqrt(1+g'^2), no K_c
E = T0*sp.sqrt(1+g**2)
ser = sp.series(E, g, 0, 6).removeO()
c4_040 = sp.simplify(ser.coeff(g, 4))
print(f"  Q1: quartic of T0 sqrt(1+g'^2) = {c4_040}  (K_c present: {Kc in c4_040.free_symbols})")
# Q3 checks on BET3's functional
c4 = (k*(Kc + f*k)/(Kc + k) - T0)/8
corner = sp.limit(sp.limit(c4, f, 0), Kc, 0)
print(f"  Q3a: f->0, K_c->0 corner = {corner}  (matches -T0/8: {sp.simplify(corner + T0/8) == 0})")
c4_uni = sp.simplify(c4.subs(f, 1))
print(f"  Q3b: f=1 branch = {c4_uni}, d/dK_c = {sp.simplify(sp.diff(c4_uni, Kc))}")
c4_f0 = sp.simplify(sp.limit(c4, f, 0))
print(f"  Q3c: f->0, K_c finite = {c4_f0}  (K_c retained: {Kc in c4_f0.free_symbols})")

print("\nHALF 2 -- SU(6) decision bands (locked arithmetic)")
def band(N, kk):
    C = kk*(N-kk)/(N-1)
    sine = np.sin(np.pi*kk/N)/np.sin(np.pi/N)
    vals = {kp: C*(1 - (1/(2*kp))*(C-1)) for kp in (50, 250)}
    lo, hi = min(vals.values()), max(vals.values())
    e = 0.02*sine   # the registered ~2 percent error scale, for reporting only
    print(f"  SU({N}) k={kk}: Casimir {C:.4f}; softened band [{lo:.4f}, {hi:.4f}]; sine {sine:.4f}")
    print(f"    SELECTS-ROPE: x in [{lo:.4f}-1e, {hi:.4f}+1e] AND (sine - x)/e >= 3")
    print(f"    KILLS: (x - {hi:.4f})/e >= 3")
    print(f"    at the registered ~2 percent error scale e ~ {e:.3f}: kill threshold x >= {hi+3*e:.3f}; "
          f"sine at {sine:.4f} {'KILLS' if sine >= hi+3*e else 'does not yet kill'} if confirmed at that precision")
    return lo, hi, sine
band(6, 2)
band(6, 3)
print("\n  Casimir-pin table (FND-047, restated): -1.25 percent decides the 5 percent floor;")
print("  -0.25 percent reaches the continuum reading; Bali bound kappa_pack >= 12.5 tightens neither.")
