"""COMMISSION SAMEKH: realizations of GRANT-CANDIDATE-COH evaluated blind
per analysis/SAMEKH_coh_realization_bars_LOCKED.md. Every exponent is
derived numerically BEFORE comparison with the target -1/2."""
import numpy as np

print("== COMMISSION SAMEKH: realizing the coherent channel ==\n")
EPS = 1.0   # bare cross-sublattice cost unit (4 eps absorbed into scale)

def star_shift(N, v):
    """Ground shift of one state coupled off-diagonally to N degenerate
    states with element v (all at the same diagonal energy)."""
    H = np.zeros((N + 1, N + 1))
    H[0, 1:] = v
    H[1:, 0] = v
    return -np.min(np.linalg.eigvalsh(H))   # gain below the degenerate level

def rank1_gs(N, v):
    """Ground energy of N states coupled all-to-all with element -v."""
    H = -v * np.ones((N, N)) + v * np.eye(N)
    return np.min(np.linalg.eigvalsh(H))

Ns = [8, 32, 128, 512]

def exponent(vals):
    x = np.log(Ns); y = np.log(np.abs(vals))
    return np.polyfit(x, y, 1)[0]

# ---------------------------------------------------------------- R1
print("-- R1: star with bare cost (staggering = 4 eps - gain) --")
for tag, vfun in [("n-loc  v = 0.1", lambda N: 0.1),
                  ("n-vol  v = 1/N", lambda N: 1.0 / N)]:
    st = [4 * EPS - star_shift(N, vfun(N)) for N in Ns]
    print(f"   {tag}: staggering at N = {Ns}: {[f'{s:.4f}' for s in st]}")
print("   n-loc: gain = v sqrt(N) GROWS; staggering crosses zero and goes")
print("   negative (unbounded gain, unphysical) -> the bare cost survives")
print("   only if v sqrt(N) < 4 eps, and then staggering -> 4 eps = CONST.")
print("   n-vol: gain = v0/sqrt(N) -> 0; staggering -> 4 eps = CONST.")
print("   LEADING EXPONENT: 0 in both normalizations. R1 reproduces the")
print("   REFUTED A-independent form (NUC-024/027). Reaching -1/2 would")
print("   require 4 eps to cancel exactly: REFUSED per B2.\n")

# ---------------------------------------------------------------- R2
print("-- R2: rank-1 condensate blocking --")
for tag, vfun in [("n-loc  v = 0.1", lambda N: 0.1),
                  ("n-vol  v = 1/N", lambda N: 1.0 / N)]:
    st = [rank1_gs(N - 1, vfun(N)) - rank1_gs(N, vfun(N)) for N in Ns]
    e = exponent(st)
    print(f"   {tag}: staggering {[f'{s:.5f}' for s in st]}  exponent ~ {e:+.2f}")
print("   n-loc exponent 0 (the refuted form); n-vol exponent -1. Neither -1/2.\n")

# ---------------------------------------------------------------- R3
print("-- R3: degenerate seniority --")
def seniority_stag(Omega, G):
    E = lambda n, s: -(G / 4.0) * (n - s) * (2 * Omega - n - s + 2)
    n = Omega           # half filling
    return (E(n - 1, 1) + E(n + 1, 1)) / 2.0 - E(n, 0)
for tag, Gfun in [("n-loc  G = 0.1", lambda Om: 0.1),
                  ("n-vol  G = 1/Omega", lambda Om: 1.0 / Om)]:
    st = [seniority_stag(N, Gfun(N)) for N in Ns]
    e = exponent(st)
    print(f"   {tag}: staggering {[f'{s:.4f}' for s in st]}  exponent ~ {e:+.2f}")
print("   n-loc exponent +1, n-vol exponent 0 (the refuted form). Neither -1/2.\n")

# ---------------------------------------------------------------- R4
print("-- R4: pure off-diagonal (channel separation) --")
for tag, vfun in [("n-loc  v = 0.1", lambda N: 0.1),
                  ("n-vol  v = 1/N", lambda N: 1.0 / N)]:
    st = [star_shift(N, vfun(N)) for N in Ns]
    e = exponent(st)
    print(f"   {tag}: staggering {[f'{s:.5f}' for s in st]}  exponent ~ {e:+.2f}")
print("   n-loc: +1/2 (grows, unphysical as a cost). n-vol: -1/2 EXACTLY.")
print("   R4 + volume-normalized mediator is the UNIQUE surviving")
print("   realization, with no cancellation anywhere: the diagonal cost is")
print("   not deleted, it is RELOCATED to the asymmetry channel.\n")

# ---------------------------------------------------------------- B4
print("-- B4: the split confrontation (asymmetry must dilute as -1/3) --")
A_meas = np.array([16.0, 40.0, 80.0])
s_meas = np.array([5.22, 3.94, 2.84])          # NUC-020, MeV per |N-Z|
# amplitude-only fit at fixed exponent -1/3
amp = np.sum(s_meas * A_meas ** (-1.0 / 3.0)) / np.sum(A_meas ** (-2.0 / 3.0))
pred = amp * A_meas ** (-1.0 / 3.0)
frac = np.abs(pred - s_meas) / s_meas
print(f"   fitted amplitude: {amp:.2f} MeV; predictions {np.round(pred, 2)}")
print(f"   measured {s_meas}; fractional residuals {np.round(100*frac,1)} percent")
mx = np.max(frac) * 100
verdict = "CONSISTENT" if mx < 10 else ("TENSION" if mx <= 25 else "FAILS")
print(f"   max fractional residual {mx:.1f} percent  ->  VERDICT: {verdict}")
print(f"   (free-fit exponent from NUC-020, reported not fitted: -0.374)\n")

# ---------------------------------------------------------------- price
print("-- pricing the surviving realization --")
# staggering = v0 / sqrt(N), N = A/2, measured 24/sqrt(A):
# v0 / sqrt(A/2) = 24/sqrt(A)  ->  v0 = 24/sqrt(2) MeV
v0 = 24.0 / np.sqrt(2.0)
print(f"   v0 = {v0:.2f} MeV: the TOTAL two-vertex coherent coupling strength")
print("   (mediator vertex squared over mode stiffness, summed over the")
print("   mode volume). One number, unregistered, blocked on the mode")
print("   quantization normalization (QGATE) and the mode-nucleon vertex.")
print("   NOTE the R4 bonus: no root-extensive smooth component exists in")
print("   this realization (the hybridization acts only on the odd state),")
print("   so NUC-028's ABSORBED 24 sqrt(A) MeV shadow is NOT owed here.")
