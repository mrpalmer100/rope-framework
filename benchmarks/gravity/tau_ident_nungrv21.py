"""COMMISSION TAU-IDENT (NUN-GRV21, 2026-08-16).

Bars: analysis/NUNGRV21_tau_ident_bars_LOCKED.md (locked first;
clean-room ordering: derivation before comparison).
"""

import math

# ---------------- B1: identity reading (recorded, not computed) ----
print("B1 -- IDENTITY: registered SHIN windings are FINE-pitch by text")
print("  (FND-086: p in [a_f, lambda/4], worst case p = a_f;")
print("   FND-091: kappa = (pi/p) sin 2psi -> 2.962/a_f, 2.751/a_f;")
print("   GRV-112 corrected by FND-126: tau_1 = 2.0944/a_f). No registered winding at the")
print("  strand radius exists. VERDICT: DISTINCT-CERTIFIED; GRV-127")
print("  upheld; the transplant stays demoted.\n")

# ---------------- B2: the fine-route computation -------------------
# Registered inputs (every factor sourced):
T0 = 1.203e3          # N (GRV-073 chain; k = 2 T0 rider via FND-114)
# FND-127 (2026-08-17): the projection ratio 8.091 is superseded in form;
# the dynamical mapping (FND-126) returns 9 exactly at the adjudicated
# k/T0 = 2 (FND-114 rider carried unchanged).
kf_over_T0f = 9.0     # dynamical fine stiffness ratio (was projection 8.091)
nu = 0.25             # GRV-073's chain: E/G = 2(1+nu) = 2.5
# SWEEP-TAU (2026-08-17): FND-126 corrected the psi convention.
# Corrected torsions: tau_1 = 2.0944/a_f, tau_2 = 4.6593/a_f.
# BRANCH = 'MAX' (bounding, proposed default) or 'L1' (level-1 pinned).
BRANCH = 'MAX'
tau1_coeff = {'MAX': 4.6593, 'L1': 2.0944}[BRANCH]   # was 4.1888 (inverted)
slender = 0.355       # r_s <= 0.355 a_f (FND-091, registered CEILING)
E_PeV = 1.400e15 * 1.602176634e-19   # J (FND-083 fine-mesh ceiling)
hc = 1.98644586e-25   # J m
lam_PeV = hc / E_PeV
af_max = lam_PeV / 4.0                # FND-086 over-resolution ceiling
print(f"B2 -- lambda_PeV = {lam_PeV:.4e} m; a_f ceiling = {af_max:.4e} m")

# Per sub-strand: (G I_p)_f = [k_f/(pi r_s^2)/(2(1+nu))] * pi r_s^4/2
#              = k_f r_s^2 / (4 (1+nu))
# lambda_sub = (G I_p)_f * |tau_1| = k_f r_s^2 tau1_coeff / (4(1+nu) a_f)
# Redistribution: k_f = kf_over_T0f * T0f = kf_over_T0f * T0 / n_sub
# Coherent sum over n_sub sub-strands (BOUNDING case):
#   lambda_strand = n_sub * lambda_sub  ->  n_sub CANCELS:
#   lambda_strand = kf_over_T0f * T0 * r_s^2 * tau1_coeff / (4(1+nu) a_f)
# r_s ceiling: r_s = slender * a_f  ->  lambda_strand <= C * T0 * a_f
C = kf_over_T0f * slender**2 * tau1_coeff / (4 * (1 + nu))
print(f"  n_sub CANCELS exactly (redistribution T0_f = T0/n_sub against")
print(f"  the coherent n_sub sum). lambda_strand <= C * T0 * a_f with")
print(f"  C = {kf_over_T0f} * 0.355^2 * {tau1_coeff} / (4*1.25) = {C:.4f}  [branch {BRANCH}, dynamical k_f]")
lam_max = C * T0 * af_max
print(f"  lambda_strand <= {lam_max:.3e} J   [UPPER BOUND, every factor")
print(f"  registered; coherence and slenderness both bound-preserving]")

# Lambda_nat under the surviving T-branch closure (GRV-125's registered
# coefficients; R_0 = 1 per GRV-126):
a = 1.0e-16; c = 2.998e8; G = 6.674e-11
mu = T0 / c**2
kT = 1.0 / (a * mu**2 * c**3)
Lam_nat_max = kT * lam_max * c**3 / (2 * G)
chi_req_min = 1.0 / Lam_nat_max
print(f"\n  Lambda_nat <= {Lam_nat_max:.2e}   (T-branch, R_0 = 1)")
print(f"  chi_required >= {chi_req_min:.2e}  for GR-strength dragging")
print(f"  GATE: Lambda_nat is LINEAR in a_f (the n_sub cancellation")
print(f"  removed the second fine unknown): the gate ledger improves")
print(f"  from {{(G I_p)_f, a_f}} to {{a_f}} alone.")

# ---------------- B3: comparison leg (opened last) -----------------
print("\nB3 -- COMPARISON (opened only now, per bars):")
tr_lo, tr_hi = 2.60e-17, 4.50e-17
print(f"  demoted transplant band: [{tr_lo:.2e}, {tr_hi:.2e}] J")
print(f"  fine-route ceiling:       {lam_max:.2e} J")
print(f"  ratio: transplant / ceiling = {tr_lo/lam_max:.0f}-{tr_hi/lam_max:.0f}x")
print("  THE COINCIDENCE ADJUDICATED: class-level, not object-level.")
print("  Both expressions are (medium stiffness) x (O(1) winding")
print("  geometry) x (a structural length), which is why they land")
print("  within ~2 orders -- but the registered object is 114-197x")
print("  BELOW the transplant band at the a_f ceiling, and falls")
print("  linearly as a_f falls. The 1e37 / 1e-37 point values do NOT")
print("  resurrect; what registers instead is the corpus's first")
print("  UPPER BOUND on the frame-dragging natural scale.")
# attribution-consistency point (demand, not measurement):
lam_needed = 2.6e-17 * 6e18 / 1.09e37   # lambda giving Lambda_nat ~ 6e18
af_needed = lam_needed / (C * T0)
print(f"\n  the birefringence-attribution CONSISTENCY point (Lambda_nat")
print(f"  ~ 6e18) sits at a_f ~ {af_needed:.1e} m -- sixteen orders below")
print(f"  the PeV ceiling (m ~ {af_max/af_needed:.0e}). Not excluded, not")
print(f"  favored: a named, quantified demand on the m-suspension.")
print("\nAll printed quantities are bounds/demands; condition 4 unchanged.")
