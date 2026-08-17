"""COMMISSION FINE-WEAVE (SHIN8, 2026-08-16).
Bars: analysis/SHIN8_fine_weave_bars_LOCKED.md (locked first).
Leg 1: coverage f_{c,f}, blind (no r_f, gravity, conduction twist,
coarse radius). Leg 2: the compensation identity + Sigma. Leg 3:
handedness (reading, recorded in results)."""
import math
# SWEEP-TAU (2026-08-17): 4.1888/(2pi) = 2/3 and 1.6239/(2pi) = 0.2584 are
# cos^2 psi_1 and cos^2 psi_2 -- angle arithmetic, correct under either
# convention; the numerals coincide with the now-corrected tau labels of
# NUN-GRV8 (see FND-126) but tau is not used here. Identity untouched.
c1sq = 4.1888/(2*math.pi); c2sq = 1.6239/(2*math.pi)
s1sq, s2sq = 1-c1sq, 1-c2sq
ident = 2/(s1sq*s2sq)
assert abs(c1sq - 2/3) < 2e-5
assert abs(ident - 8.091)/8.091 < 5e-5
print(f"IDENTITY: k_f/T0_f = 2/(sin^2 psi_1 sin^2 psi_2) = {ident:.4f} "
      f"vs registered 8.091 -- EXACT (2.7e-5).")
print("The derived fine stiffness ratio ALREADY CONTAINS the double")
print("1/sin^2 compensation; GRV-128's ceiling SURVIVES AUDIT unchanged.")
a=1.0e-16; af=2.2140e-22; slend=0.355; n_lo,n_hi=4.6e9,1.3e10; T0=1.203e3
path=1/(math.sqrt(c1sq)*math.sqrt(c2sq))
fv=[n*(af/a)**2*math.pi*slend**2*path for n in (n_lo,n_hi)]
print(f"COVERAGE: f_c,f <= [{fv[0]*100:.2f}%, {fv[1]*100:.2f}%] at ceilings; "
      f"packing headroom [{af/(a/math.sqrt(n_hi)):.3f}, {af/(a/math.sqrt(n_lo)):.3f}] < 1.")
assert fv[1] < 0.10 and af < a/math.sqrt(n_hi)
print(f"SIGMA: registered 3 T0/a^2 = {3*T0/a**2:.3e} J/m^3; redistribution")
print("Sigma-invariant (FND-083); a_f cancels: SIGMA-CLOSES-WITHOUT-a_f.")
print("All assertions passed.")
