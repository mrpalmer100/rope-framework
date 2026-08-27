"""COMMISSION SWEEP-PATH (FND-136, 2026-08-18) -- the fine-weave
path-factor tightening. Executed under analysis/SWEEPPATH_bars_LOCKED.md.

SHIN8's leg-1 arithmetic verbatim, with the path factor moved from
reading B (axial cos = cos psi) to the load-bearing reading A
(axial cos = sin psi, BLOCH-L Leg 0 isotropy control). Direction
pre-disclosed: coverage DOWN, headroom UNCHANGED.
"""
import math

ok = True
print("COMMISSION SWEEP-PATH -- the fine-weave path-factor tightening\n")

# ---- angles, SHIN8's own registered inputs (same physical psi pair) ----
c1sq_B = 4.1888 / (2 * math.pi)          # cos^2 psi_1 = 2/3
c2sq_B = 1.6239 / (2 * math.pi)          # cos^2 psi_2 = 0.25845
s1sq, s2sq = 1 - c1sq_B, 1 - c2sq_B      # sin^2 psi_1 = 1/3, sin^2 psi_2

print("LEG 1 -- THE IDENTITY CONTROL (swap-invariant, stated on the face)")
ident = 2 / (s1sq * s2sq)
e = abs(ident - 8.091) / 8.091
print(f"  2/(sin^2 psi_1 sin^2 psi_2) = {ident:.4f} vs registered 8.091  "
      f"rel {e:.1e}  [{'PASS' if e < 5e-5 else 'HALT'}]")
print("  The identity uses sin^2 of BOTH angles and is invariant under the")
print("  sin<->cos convention swap. That invariance is exactly why the")
print("  earlier convention sweep cleared this file while the path factor")
print("  six lines below it -- which is NOT swap-invariant -- went unread.")
ok &= e < 5e-5
if not ok:
    raise SystemExit(1)

print("\nLEG 2 -- THE COVERAGE RECOMPUTE (SHIN8 leg-1 verbatim, path moved)")
path_B = 1 / (math.sqrt(c1sq_B) * math.sqrt(c2sq_B))
path_A = 1 / (math.sqrt(s1sq) * math.sqrt(s2sq))
print(f"  path, reading B (as run):        {path_B:.4f}")
print(f"  path, reading A (load-bearing):  {path_A:.4f}   "
      f"(ratio {path_A/path_B:.4f})")
a = 1.0e-16; af = 2.2140e-22; slend = 0.355
n_lo, n_hi = 4.6e9, 1.3e10
fv_B = [n * (af / a) ** 2 * math.pi * slend ** 2 * path_B for n in (n_lo, n_hi)]
fv_A = [n * (af / a) ** 2 * math.pi * slend ** 2 * path_A for n in (n_lo, n_hi)]
print(f"  coverage as registered (B): [{fv_B[0]*100:.2f}%, {fv_B[1]*100:.2f}%]")
print(f"  coverage under reading A:   [{fv_A[0]*100:.2f}%, {fv_A[1]*100:.2f}%]")
hr = [af / (a / math.sqrt(n)) for n in (n_hi, n_lo)]
print(f"  packing headroom [{hr[0]:.3f}, {hr[1]:.3f}] -- UNCHANGED "
      "(no path factor in the ratio)")
a1 = fv_A[1] < 0.10
a2 = af < a / math.sqrt(n_hi)
print(f"  SHIN8 assertion 1 (f < 10%):        [{'PASS' if a1 else 'FAIL'}]")
print(f"  SHIN8 assertion 2 (headroom < 1):   [{'PASS' if a2 else 'FAIL'}]")
ok &= a1 and a2
ratio_ok = all(abs(A / B_ - path_A / path_B) < 1e-12
               for A, B_ in zip(fv_A, fv_B))
print(f"  coverage moved by exactly path_A/path_B:  "
      f"[{'PASS' if ratio_ok else 'FAIL'}]")
ok &= ratio_ok

print("\nLEG 3 -- THE QUOTE SWEEP (live occurrences of the reading-B factor)")
print("  1. SHIN8 results doc line 'path factor 1/(cos psi_1 cos psi_2) =")
print("     2.409' -- HISTORY, stands; the correction attaches by name")
print("     (this claim + the registry's path-factor rule).")
print("  2. energy_bill.py two-level bracket -- ALREADY SUPERSEDED in value")
print("     by the composite build; disposition annotate-only, done there.")
print("  3. No other live quote found by the registry grep (overview and")
print("     handoff copies are generated/superseded text).")

print("\nVERDICT:", "TIGHTENED" if ok else "NOT as pre-registered")
print("  f_{c,f} <= [%.2f%%, %.2f%%] at the ceilings under the load-bearing" %
      (fv_A[0] * 100, fv_A[1] * 100))
print("  reading, DOWN from the registered [2.15%, 6.08%]; packing headroom")
print("  unchanged; both SHIN8 assertions pass with more margin. The")
print("  spacing-separated-fiber picture SHARPENS.")
raise SystemExit(0 if ok else 1)
