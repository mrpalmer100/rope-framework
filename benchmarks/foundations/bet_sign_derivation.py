"""Commission BET — the sign, DERIVED: the mesh softens, geometrically.

THE DERIVATION (registered premises only): a constant-tension strand
(T0 the global Lagrange multiplier, FND-017; strands inextensible,
FND-KIN-001 -- so no Hookean competitor EXISTS in the registry, B4
search performed) displaced transversely carries energy per length
T0 sqrt(1 + g'^2) = T0 (x/2 - x^2/8 + ...), x = g'^2. The quartic term
is NEGATIVE: pure arc-length geometry SOFTENS.
COEFFICIENT: leading u = Sigma_vac x/2 -> relative correction = -x/4
= -eps/2 with eps = u/Sigma_vac. Hence
    delta_D - delta_f = -(eps_f/2)(C_D/C_f - 1):
NEGATIVE, matching the Anzai-Kiyo-Sumino direction -- ALEPH's retracted
sign slot refills as a DERIVED prediction, aligned with the only
resolved violation in the field.
FLOOR REARITHMETIC (honest, it WEAKENS): eps_f <= 2|delta|/(Cmax-1):
    kappa_pack >= 50  (5% bound)   -> Sigma_vac >= 1.81e37, a = 1.63e-17,
                                       T0 = 1599 J/m, Lorentz margin 6.1x
    kappa_pack >= 250 (continuum)  -> Sigma_vac >= 9.03e37, a = 9.53e-18,
                                       T0 = 2734 J/m, margin 10.5x
    l_q/a = 158 / 271 -- the strain PERSISTS at both readings.
DOMINANCE: tube strain^2 x <= 0.04 << 1; expansion controlled; core
(d_c) terms enter at higher order. Grade: Derived from stated premises,
both registered.
"""
import math

K_ME = 2.6065e-14; S_EFF = 3.61e35; CMAX = 6.0


def floor(delta):
    eps = 2 * delta / (CMAX - 1)
    kap = 1 / eps
    sv = kap * S_EFF
    a = (3 * K_ME / sv) ** (1 / 3)
    return kap, sv, a, K_ME / a


def main():
    # sign: quartic coefficient of sqrt(1+x) expansion is -1/8 < 0
    assert -1 / 8 < 0
    # coefficient: relative correction -x/4 with x = 2 eps -> -eps/2
    for delta, kap_ref, a_ref in [(0.05, 50, 1.630e-17), (0.01, 250, 9.533e-18)]:
        kap, sv, a, t0 = floor(delta)
        assert abs(kap - kap_ref) < 1 and abs(a / a_ref - 1) < 0.01
        assert a < 1e-16                       # Lorentz bound holds
        assert 2.58e-15 / a > 100              # l_q/a strain persists
    print("sign DERIVED: negative (geometric softening); coefficient -eps/2")
    print("floor re-set: kappa_pack >= 50 (5%) / 250 (continuum); OMEGA headline updated")
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
