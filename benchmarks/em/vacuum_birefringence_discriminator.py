"""The completed discriminator (the 'bounded follow-up' of EM-RECON-014) and its
confrontation with PVLAS -- the chain's 'real numbers meeting real data' leg.

DERIVED (exact, given the field mapping): expanding the single-invariant rope
quartic c4*(|g|^2)^2 around a static background g_B (the rope realization of an
external B field, g_B = c*B*sqrt(eps0/SIGMA) by the EM-RECON-014 energy
identification):
    T_eff(par)  = T0 + 12 c4 g_B^2,   T_eff(perp) = T0 + 4 c4 g_B^2
  => ANISOTROPY RATIO dn_par : dn_perp = 3 : 1     [QED Euler-Heisenberg: 7 : 4]
  => SIGN: c4 > 0 (required for the core) stiffens -> light SPEEDS UP -> Dn < 0
                                                     [QED: Dn > 0]
  A DOUBLE qualitative discriminator. Magnitude:
    |Dn| = (1/2)(k/T0 - 1) * eps0 c^2 B^2 / SIGMA

CONFRONTATION (PVLAS final: Dn = (12 +/- 17)e-23 at B = 2.5 T; QED predicts
+2.5e-23): at the ATLAS-identification SIGMA = 1.5e25 J/m^3 and k/T0 = 2, the
rope prediction is |Dn| = 1.7e-19 -- ~570x ABOVE the PVLAS 1-sigma bound
(2.9e-22). THE IDENTIFICATION IS EXCLUDED. New bound:
    SIGMA > (k/T0 - 1) * 8.6e27 J/m^3     [supersedes the ATLAS bound by ~10^3]
so the rope nonlinearity onset is >= ~24x the Schwinger field, and the ATLAS
light-by-light events are genuine QED, not the rope quartic.

LIVE TEST: at the new bound, the rope Dn (~2.9e-22) still EXCEEDS QED's
(+2.5e-23) and has the OPPOSITE SIGN -- so PVLAS-class experiments improving
toward QED sensitivity move through decisive territory: they either detect a
NEGATIVE Dn with 3:1 anisotropy (rope), or push SIGMA up another order and
confirm QED's +7:4 (rope quartic subdominant). Either way, decided by
experiment, not preference.

Caveats (flagged): the mapping of static B to a same-invariant transverse
gradient is the load-bearing step; the RATIO (exactly 3) holds given that
mapping, the MAGNITUDE is O(1)-uncertain under mapping variants, and the SIGN
(stiffening) is robust since c4 > 0 is required by the core.
"""
import numpy as np
import sympy as sp

EPS0, C = 8.854e-12, 2.998e8
B_PVLAS = 2.5
DN_PVLAS_1SIG = 29e-23          # (12+17)e-23
DN_QED = 2.5e-23


def anisotropy_is_3_to_1():
    Bb, d1, d2, c4 = sp.symbols('B d1 d2 c4', positive=True)
    quart = sp.expand(c4 * ((Bb + d1)**2 + d2**2)**2)
    p = sp.Poly(quart, d1, d2)
    return sp.simplify(p.coeff_monomial(d1**2) / p.coeff_monomial(d2**2) - 3) == 0


def rope_dn(Sigma, k_over_T0, B=B_PVLAS):
    return 0.5 * (k_over_T0 - 1) * EPS0 * C**2 * B**2 / Sigma


def test():
    assert anisotropy_is_3_to_1(), "single-invariant quartic must give exactly 3:1"
    # exclusion of the ATLAS identification
    dn_ident = rope_dn(1.5e25, 2.0)
    factor = dn_ident / DN_PVLAS_1SIG
    assert 400 < factor < 800, f"identification overshoots PVLAS by ~570x, got {factor:.0f}"
    # new bound
    Sig_min = 0.5 * 1.0 * EPS0 * C**2 * B_PVLAS**2 / DN_PVLAS_1SIG   # k/T0 = 2
    assert 7e27 < Sig_min < 1e28, f"new bound ~8.6e27, got {Sig_min:.2e}"
    # live-test window: at the bound, rope |Dn| still exceeds QED's
    assert rope_dn(Sig_min, 2.0) > DN_QED, "decisive window between current bound and QED sensitivity"
    # onset shift
    onset_ratio = np.sqrt(Sig_min / (EPS0 * (1.32e18)**2))
    assert 20 < onset_ratio < 30, "onset >= ~24x Schwinger"
    print("anisotropy ratio: exactly 3:1 (sympy), sign NEGATIVE (stiffening)  [QED: 7:4, positive]")
    print(f"identification SIGMA=1.5e25 predicts |Dn| = {dn_ident:.1e} vs PVLAS bound 2.9e-22: EXCLUDED (~{factor:.0f}x over)")
    print(f"new bound: SIGMA > {Sig_min:.1e} J/m^3 (k/T0=2) -- supersedes the ATLAS bound ~600x; onset >= ~24x Schwinger")
    print(f"live window: rope |Dn| at the bound ({rope_dn(Sig_min,2.0):.1e}) > QED ({DN_QED:.1e}), opposite sign")
    print("PASS: discriminator computed; PVLAS excludes the identification; decisive window ahead.")


if __name__ == "__main__":
    test()
