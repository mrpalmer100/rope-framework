"""COMMISSION NUN: the 1/sqrt(A) dilution of NUC-021's fixed
cross-sublattice cost, prosecuted blind per
analysis/NUN_dilution_bars_LOCKED.md. Channels D1-D4 enumerated at lock;
each exponent derived BEFORE comparison with the target."""
import numpy as np

print("== COMMISSION NUN: the dilution ==\n")
rng = np.random.default_rng(7)

# ----------------------------------------------------------------------
# D1: classical smearing. Bond energy bilinear in fractional occupations.
# Defect amplitude 1/M on each of M foreign-sublattice sites; every such
# site has 4 same-label cross-sublattice neighbours at full occupancy.
# Cost = sum over bonds of f_site x f_neighbour x eps.
print("-- D1: classical smearing --")
for M in [1, 4, 16, 64, 256]:
    cost = M * (1.0 / M) * 4 * 1.0   # M sites x amplitude 1/M x 4 bonds x occ 1
    print(f"   M = {M:4d}: cost = {cost:.6f} eps")
print("   EXPONENT: 0 exactly. Bilinear bond energy is LINEAR in the defect")
print("   occupation, so smearing redistributes the cost without reducing it.\n")

# ----------------------------------------------------------------------
# D2: defect-band delocalization. The misplaced label hops on its foreign
# sublattice (fcc sublattice = simple cubic connectivity via reconnection,
# amplitude t UNREGISTERED). Diagonal cost 4 eps; band E(k) = 4 eps
# - 2t sum cos(k_i a). Band bottom: 4 eps - 6t, A-INDEPENDENT. Finite-size
# correction: lowest available nonzero k ~ pi/L, L ~ A^(1/3):
# E - E_min ~ t (k a)^2 ~ A^(-2/3). Exponent is t-independent; only the
# exponent is used per B1.
print("-- D2: defect-band delocalization --")
for A in [16, 64, 256, 1024]:
    L = A ** (1.0 / 3.0)
    corr = (np.pi / L) ** 2
    print(f"   A = {A:5d}: finite-size correction ~ {corr:.4f} t  (~ A^-2/3)")
print("   EXPONENT of the diluting piece: -2/3 (quadratic band bottom).")
print("   The FIXED part (4 eps - 6t) does not dilute at all; the exponent")
print("   -2/3 governs only the finite-size remainder. Neither piece is -1/2.\n")

# ----------------------------------------------------------------------
# D3: elastic screening. Ambient labels polarize: cost -> cost/(1 + chi)
# with chi a local response. Multiplicative, A-independent renormalization.
print("-- D3: elastic screening --")
print("   The polarization cloud is LOCAL (registered interactions are")
print("   nearest-neighbour); a local cloud renormalizes the cost by an")
print("   A-independent factor. EXPONENT: 0.\n")

# ----------------------------------------------------------------------
# B2: the geometric no-go.
print("-- B2: the geometric exponent set --")
print("   Local energy on a compact 3D droplet: A^1, A^(2/3), A^(1/3), A^0.")
print("   1/2 is NOT in the set: 1/3 < 1/2 < 2/3, strictly between curvature")
print("   and surface. NO term of a local/geometric expansion carries A^(1/2).")
print("   Consequence: D1-D3 (all local) CANNOT produce the -1/2 dilution,")
print("   consistent with their derived exponents (0, -2/3, 0).\n")

# ----------------------------------------------------------------------
# D4: coherent collective sharing. If an energy component is carried by an
# amplitude summed coherently over N participating pair-states with fixed
# per-state coupling v, degenerate coupling of one state to N gives
# E_coh(N) = v sqrt(N) (coherent enhancement). Blocking one participant
# (the odd nucleon) costs the discrete derivative.
print("-- D4: coherent collective sharing --")
print("   E_coh(N) = c sqrt(N); staggering = E(N) - E(N-1) ~ c/(2 sqrt(N)).")
for N in [8, 32, 128, 512]:
    c = 1.0
    stag = c * (np.sqrt(N) - np.sqrt(N - 1))
    print(f"   N = {N:4d}: staggering = {stag:.5f}  vs c/(2 sqrt N) = {c/(2*np.sqrt(N)):.5f}")
print("   EXPONENT: -1/2 EXACTLY, and it is the ONLY enumerated channel that")
print("   produces it. Root-extensivity (E ~ sqrt(N)) is the signature of")
print("   coherent amplitude addition and is NON-LOCAL by the B2 no-go.\n")

# ----------------------------------------------------------------------
# B3: the equivalence, run as arithmetic.
# NUC-027's preferred form: staggering = 24/sqrt(A) MeV. Participants are
# pairs, N = A/2. c/(2 sqrt(A/2)) = 24/sqrt(A)  ->  c = 48/sqrt(2) = 33.94 MeV.
print("-- B3: pricing the coherent channel from the measured staggering --")
c_s = 24.0
c_coh = 2.0 * c_s / np.sqrt(2.0)
print(f"   staggering 24/sqrt(A) MeV with N = A/2  ->  c = {c_coh:.2f} MeV")
print(f"   implied smooth component: E_coh(A) = c sqrt(A/2) = {c_coh/np.sqrt(2):.2f} sqrt(A) MeV")
k_smooth = c_coh / np.sqrt(2.0)
for A in [56, 120, 208]:
    print(f"     A = {A}: E_coh = {k_smooth*np.sqrt(A):.0f} MeV")
print()

# ----------------------------------------------------------------------
# B4: absorbability confrontation. Can k sqrt(A) hide inside the droplet
# basis over the physical table range?
print("-- B4: absorbability of the priced sqrt(A) term --")
A = np.arange(16, 251, dtype=float)
target = k_smooth * np.sqrt(A)
basis = np.vstack([A, A ** (2.0/3.0), A ** (1.0/3.0), np.ones_like(A)]).T
coef, *_ = np.linalg.lstsq(basis, target, rcond=None)
resid = target - basis @ coef
mx = np.max(np.abs(resid))
print(f"   projection coefficients on [A, A^2/3, A^1/3, 1]: {np.round(coef, 3)}")
print(f"   max |residual| over A in [16, 250]: {mx:.3f} MeV")
verdict = "ABSORBED" if mx < 3.0 else ("EXCLUDED" if mx > 10.0 else "TENSION")
print(f"   VERDICT (locked grammar): {verdict}")
print("   Interpretation is fixed by the bar: ABSORBED means the priced")
print("   smooth component hides inside refitted droplet coefficients at")
print("   SEMF-level scatter; the staggering, not the smooth surface, is")
print("   where the channel is visible. Shifts it would induce:")
print(f"     a_V by {coef[0]:+.3f} MeV, a_S by {coef[1]:+.3f} MeV.")
