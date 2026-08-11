"""Commission XI — the independent-data confrontation, mechanically verified.

Source: Cea-Cosmai-Cuteri-Papa, PoS LATTICE2016 (arXiv:1701.03371) — Clem-ansatz
fits E(x_t) = (phi/2pi)(mu^2/alpha) K0(sqrt(mu^2 x_t^2 + alpha^2))/K1(alpha) to
connected-correlator profiles: SU(3) pure gauge and (2+1)-flavor HISQ QCD at
pion mass 160 MeV. DIFFERENT ensembles, era, and observable pipeline from the
verdict-bearing arXiv:2409.20168 dataset; SAME collaboration -> PARTIALLY
independent per bar I1. The fully-independent Bicudo-Cardoso determinations
were EXCLUDED per bar B2 (width-convention mapping ambiguous from published
values alone).

Conversion: the REGISTERED definition (ELEC-051/052 bars):
    R_eq = sqrt(2 <x^2>_{E^2}) = sqrt(2 * int r^3 E^2 dr / int r E^2 dr)
computed analytically on the source's own fitted profile. VALIDATION: the same
machinery reproduces the paper's own E-weighted sqrt(w^2) to 0.2% (0.411 vs
0.411; 0.457 vs 0.458), so the implementation is checked against the source
before the verdict quantity is computed. A first pass used a peak-normalized
uniform-cylinder definition by mistake (R_eq ~ 0.23 fm, -43%); caught by
checking against the registered bars file BEFORE any verdict was drawn —
recorded per house discipline.

Verdict (bars B3, reference R_eq = 0.402-0.407 fm):
  TIER 2 (SU(3) pure gauge, d=0.76 fm): R_eq = 0.388-0.402, mean 0.395 fm,
      -3.0% -> CONFIRMED (quenching caveat on the face).
  TIER 1 PARTIAL (full QCD, 160 MeV pion, d=0.76 fm): R_eq = 0.349-0.357,
      mean 0.353 fm, -13.2% -> TENSION band, BUT the kappa fit errors (~50%)
      span R_eq = 0.315-0.445, overlapping CONFIRMED; and the named candidate
      systematic is the pion mass (160 vs physical: lighter sea quarks widen
      the tube, and the physical-mass 2409 data sits exactly above).
  Propagated Sigma (T_tube/(pi R_eq^2)): tier-2 3.83e35 (in the pinned band's
      neighborhood); tier-1 partial 4.78e35 central with the kappa systematic
      spanning ~2.9-5.4e35 — consistent with the pinned band, not decisive.
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import k0, k1, kn

T_TUBE = 1.874e5
REF = (0.402, 0.407)
ROWS = {  # label: (lambda fm, kappa, paper's own sqrt(w^2) fm or None)
    "fullQCD_b6.743": (0.139, 0.264, 0.411),
    "fullQCD_b6.885": (0.147, 0.342, 0.411),
    "puregauge_b6.050_d0.76": (0.164, 0.348, 0.458),
    "puregauge_b6.195_d0.76": (0.173, 0.369, 0.476),
}


def alpha_from_kappa(kap):
    f = lambda a: (np.sqrt(2) / a) * np.sqrt(1 - (k0(a) / k1(a)) ** 2) - kap
    return brentq(f, 1e-3, 50)


def r_eq(lam, kap):
    a = alpha_from_kappa(kap)
    prof = lambda t: k0(np.sqrt(t * t + a * a)) ** 2
    m2 = quad(lambda t: prof(t) * t ** 3, 0, 80)[0]
    m0 = quad(lambda t: prof(t) * t, 0, 80)[0]
    return lam * np.sqrt(2 * m2 / m0)


def w_rms(lam, kap):  # the paper's E-weighted width, for validation
    a = alpha_from_kappa(kap)
    return np.sqrt(2 * a * lam ** 2 * kn(2, a) / k1(a))


def main():
    # Validation against the source's own published widths
    for key in ("fullQCD_b6.743", "puregauge_b6.050_d0.76"):
        lam, kap, w_tab = ROWS[key]
        assert abs(w_rms(lam, kap) / w_tab - 1) < 0.005, f"validation failed: {key}"
    # Tier-2 verdict: CONFIRMED
    t2 = [r_eq(*ROWS[k][:2]) for k in ROWS if "puregauge" in k]
    t2m = float(np.mean(t2))
    assert abs(t2m / REF[1] - 1) < 0.10, "tier-2 left the CONFIRMED band"
    # Tier-1 partial: TENSION band on central values, overlap with CONFIRMED under kappa systematic
    t1 = [r_eq(*ROWS[k][:2]) for k in ROWS if "fullQCD" in k]
    t1m = float(np.mean(t1))
    assert 0.10 < abs(t1m / REF[1] - 1) < 0.25, "tier-1 partial left the TENSION band"
    assert r_eq(0.139, 0.13) > REF[0] * 0.95, "kappa systematic no longer reaches CONFIRMED"
    # Propagated Sigma
    sig2 = T_TUBE / (np.pi * (t2m * 1e-15) ** 2)
    sig1 = T_TUBE / (np.pi * (t1m * 1e-15) ** 2)
    assert 3.5e35 < sig2 < 4.2e35 and 4.4e35 < sig1 < 5.2e35
    print(f"tier-2 R_eq = {t2m:.3f} fm ({t2m/REF[1]-1:+.1%}) -> Sigma = {sig2:.2e}  CONFIRMED")
    print(f"tier-1 partial R_eq = {t1m:.3f} fm ({t1m/REF[1]-1:+.1%}) -> Sigma = {sig1:.2e}  TENSION (kappa-systematic overlaps CONFIRMED)")
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
