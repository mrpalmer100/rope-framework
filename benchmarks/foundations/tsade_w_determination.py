"""COMMISSION TSADE: the w determination, executed per
analysis/TSADE_w_determination_bars_LOCKED.md. Candidates and census
order fixed at lock; every verdict recorded before the next census runs."""
import numpy as np

print("== COMMISSION TSADE: the w determination ==\n")

W_OVER_A = 0.6272                    # EM-RECON-030, vacuum-mesh ratio (W1)
W_LAT = (0.0395, 0.0565)             # fm, ELEC-050 constituent band (D-b)
R_LAT = (0.35, 0.50)                 # fm, published lattice flux-tube width band
N_HBAR = 111                         # QGATE-003's collective-hbar demand
A_LORENTZ = 0.100                    # fm  (1e-16 m, FND-MATTER-005 bound)
A_MPOINT = 0.060056                  # fm  (6.0056e-17 m, the M-point)
A_FND040 = (0.0163, 0.0097)          # fm, the two re-solved kappa_pack readings

# ---------------------------------------------------------------- Q2 D-a
print("-- D-a: the one-medium inversion (CONDITIONAL on one-medium) --")
a_lo, a_hi = W_LAT[0] / W_OVER_A, W_LAT[1] / W_OVER_A
print(f"   a = w/0.6272 with w in [{W_LAT[0]}, {W_LAT[1]}] fm")
print(f"   ->  a in [{a_lo:.4f}, {a_hi:.4f}] fm  =  [{a_lo*1e-15:.2e}, {a_hi*1e-15:.2e}] m\n")

# ---------------------------------------------------------------- C1
print("-- C1: the Lorentz bound --")
ok = a_hi <= A_LORENTZ
print(f"   inverted band [{a_lo:.4f}, {a_hi:.4f}] fm vs bound a <= {A_LORENTZ} fm: "
      f"{'SATISFIED (entire band under the bound)' if ok else 'VIOLATED'}")
print(f"   margin at the top edge: {A_LORENTZ/a_hi:.2f}x\n")

# resemblance displays (per the locked rule: displayed, refused as evidence)
print("-- resemblance displays (FND-070 rule: adjacency is NOT evidence) --")
print(f"   inverted low edge {a_lo:.4f} fm vs M-point {A_MPOINT:.4f} fm: "
      f"{100*abs(a_lo-A_MPOINT)/A_MPOINT:.1f} percent apart. DISPLAYED, REFUSED.")
w_at_bound = W_OVER_A * A_LORENTZ
print(f"   one-medium w at the Lorentz bound: {w_at_bound:.4f} fm vs lattice top "
      f"edge {W_LAT[1]} fm: {100*abs(w_at_bound-W_LAT[1])/W_LAT[1]:.0f} percent apart. "
      f"DISPLAYED, REFUSED.\n")

# conflict register (reported, not resolved)
print("-- conflict register --")
for af in A_FND040:
    factor = a_lo / af
    print(f"   FND-040 re-solved a = {af:.4f} fm is EXCLUDED by the inverted band "
          f"(low edge {factor:.1f}x above it) UNDER ONE-MEDIUM. Registered as a")
print("   conflict for adjudication; this commission does not pick between a")
print("   readings. Either one-medium falls, or the kappa_pack-floor readings do.\n")

# ---------------------------------------------------------------- C2
print("-- C2: the hbar census (corrected reading n_t = pi R^2/a^2) --")
corners = [(R, a) for R in R_LAT for a in (a_lo, a_hi)]
nvals = [np.pi * R * R / (a * a) for R, a in corners]
print(f"   n_t across (R, a) corners: [{min(nvals):.0f}, {max(nvals):.0f}]  "
      f"(demand: {N_HBAR})")
contains = min(nvals) <= N_HBAR <= max(nvals)
print(f"   demand inside the census range: {contains}")
# the exact-111 locus: R = a sqrt(111/pi); intersect R with the lattice band
ratio = np.sqrt(N_HBAR / np.pi)
a_max_111 = R_LAT[1] / ratio          # largest a with R still in lattice band
a_min_111 = max(a_lo, R_LAT[0] / ratio)
a_hi_narrow = min(a_hi, a_max_111)
print(f"   exact-111 locus: R = {ratio:.3f} a; with R in [{R_LAT[0]}, {R_LAT[1]}] fm")
print(f"   the a-band consistent with n_t = 111: [{a_min_111:.4f}, {a_hi_narrow:.4f}] fm")
w_lo_n = W_OVER_A * a_min_111
w_hi_n = W_OVER_A * a_hi_narrow
print(f"   CENSUS OUTPUT (adopted per lock): w NARROWS to "
      f"[{w_lo_n:.4f}, {w_hi_n:.4f}] fm\n")

# ---------------------------------------------------------------- C3
print("-- C3: reconnection window vs matter-stability survival --")
g_rec = (0.082, 0.265)               # FND-072 demanded window (ka = 1)
g_surv = (0.395, 0.460)              # EM-RECON-030 survival threshold band
gap = g_surv[0] / g_rec[1]
print(f"   reconnection demands per-pair g in [{g_rec[0]}, {g_rec[1]}];")
print(f"   survival demands the SAME ratio g >= [{g_surv[0]}, {g_surv[1]}].")
print(f"   DISJOINT at ka = 1: minimum gap factor {gap:.2f}x")
print(f"   conversion allowance: two independent L1-class bands (factor 3 each,")
print(f"   direction-neutral) plus FND-072's reported ka sensitivity.")
covered = gap <= 3.0
print(f"   gap within a SINGLE conversion band: {covered}")
print(f"   VERDICT for C3: NAMED TENSION, coverable -- registered, not resolved.")
print(f"   (At FND-072's reported ka = 2-3 the windows overlap outright; the")
print(f"   encounter-spectrum derivation owns the resolution.)\n")

# ---------------------------------------------------------------- verdict
print("-- VERDICT (locked grammar): CONDITIONALLY-DETERMINED --")
print(f"   Under one-medium: w = [{w_lo_n:.4f}, {w_hi_n:.4f}] fm,")
print(f"   a = [{a_min_111:.4f}, {a_hi_narrow:.4f}] fm = "
      f"[{a_min_111*1e-15:.2e}, {a_hi_narrow*1e-15:.2e}] m,")
print(f"   n_t = 111 achievable inside; Lorentz bound satisfied with margin;")
print(f"   C3 tension named and assigned. Unconditional determination is")
print(f"   blocked on exactly one item: PROSECUTING ONE-MEDIUM.")
