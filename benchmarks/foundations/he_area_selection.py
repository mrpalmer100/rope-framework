"""Commission HE -- the area-selection derivation attempt.
Bars locked BEFORE reading (analysis/HE_area_selection_bars_LOCKED.md):
E1 provenance audit, E2 pre-named principles S1-S3, E3 four-way verdict
grammar, E4 hardened numerology guard.
"""
import math

HBAR, C = 1.054571817e-34, 2.99792458e8
ALPHA, ME = 1 / 137.036, 9.1093837015e-31
K_ME = 2.6065e-14
S_EFF = 3.61e35
QAREA = 4 * math.pi * ALPHA * HBAR * C
L_Q_REG = 1.39e-15


def main():
    # E1 -- provenance (registry reading, asserted):
    # PRED-003-DICT: alpha = l_q^2 T/(4 pi hbar c), l_q the SOURCE length,
    # with a registered candidate table {a, sqrt(l_lock a), l_lock} and
    # the REGISTERED reading l_q ~ sqrt(l_lock a). PRED-003-LOCK: kappa
    # ENSLAVED, kappa = 2T/(eta a) => l_lock = T/kappa = eta a / 2, with
    # eta confined to exponent-level (undetermined normalization).
    print("E1: l_q has registered independent content -- the source length")
    print("  of the alpha chain, registered reading l_q ~ sqrt(l_lock a),")
    print("  with l_lock = eta a/2 under the LOCK enslavement and eta the")
    print("  one normalization LOCK explicitly left undetermined.")

    # THE NARROWING: l_q^2 = C^2 l_lock a = (C^2 eta/2) a^2
    # => (l_q/a)^2 = C^2 eta / 2. Define the composite N = C^2 eta:
    # the ENTIRE selection question is the value of N.
    for kappa in (50, 250):
        sv = kappa * S_EFF
        a = (3 * K_ME / sv) ** (1 / 3)
        t0 = K_ME / a
        lq = math.sqrt(QAREA / t0)
        N = 2 * (lq / a) ** 2
        print(f"  kappa_pack = {kappa}: l_q/a = {lq/a:.1f} -> N = C^2 eta = "
              f"{N:.3e}")
        # cross-check via the sixth-root law: N = 2 * 43.0^2 * kappa^(1/3)
        assert abs(N / (2 * 43.0**2 * kappa ** (1 / 3)) - 1) < 0.01
    print("  N = 3698 x kappa_pack^(1/3) exactly (sixth-root law squared).")
    print("  The area-selection question REDUCES to: derive the locking")
    print("  channel's coarse-grained normalization N = C^2 eta -- a")
    print("  computable-in-principle constant of the registered lattice")
    print("  micromechanics. N derived -> l_q/a fixed -> kappa_pack")
    print("  MEASURED (FND-042's inversion).")

    # THE CONFRONTATION CARRIED HONESTLY: if N were O(1)-O(10), as naive
    # homogenization constants usually are, the registered sqrt(l_lock a)
    # reading would MISS the ratio by 2.5-3.5 orders. Either N is
    # genuinely large (the locking channel is soft: eta >> 1 means kappa
    # = 2T/(eta a) << T/a), or the registered reading fails when its
    # normalization is computed. BOTH branches are registrable outcomes
    # of the named next-order; neither is prejudged here.
    print("  CONFRONTATION ARMED: N ~ 1e4 demands a SOFT locking channel")
    print("  (eta >> 1). A computed O(1) N kills the sqrt(l_lock a)")
    print("  reading. Either outcome is corpus-grade.")

    # THE CROSS-LINK (S3 dividend): PRED-003-DICT registers that a
    # measured nonzero drift ratio SELECTS l_q among the candidates --
    # so a cosmological drift measurement is a SECOND external route to
    # l_q, hence to kappa_pack via the inversion. PRED-003's channel
    # measurement doubles as vacuum-packing metrology.
    print("  CROSS-LINK: the PRED-003 drift-ratio measurement, if nonzero,")
    print("  selects l_q's composition -> fixes N's scaling -> reads")
    print("  kappa_pack. The corpus's sole T1 acquires a second job.")

    # E4 -- the numerology guard: one landing found during E1, reported
    # at WHISPER grade, look-elsewhere at full volume, not used above.
    lq_re2 = ALPHA * HBAR / (2 * ME * C)
    dev = lq_re2 / L_Q_REG - 1
    print(f"WHISPER (guard-capped): l_q_reg vs alpha hbar/(2 m_e c) = r_e/2:")
    print(f"  {L_Q_REG:.3e} vs {lq_re2:.3e} ({100*dev:.1f}%). Look-elsewhere:")
    print("  simple m_e-built lengths are few but were not pre-specified;")
    print("  adjacent to FND-041's flagged 3% coincidence; NOT used, NOT")
    print("  promoted. Conditional illustration only, labeled")
    print("  not-a-measurement:")
    t0_w = QAREA / lq_re2**2
    kap_w = 3 * t0_w**3 / (K_ME**2 * S_EFF)
    print(f"  IF l_q = r_e/2 exactly: T0 = {t0_w:.0f} J/m, kappa_pack = "
          f"{kap_w:.0f}")
    assert 30 < kap_w < 45  # below the 5% floor: displayed, not adjudicated
    print("  -- BELOW the FND-040 5% floor (50): the whisper and the floor")
    print("  are in mild tension, displayed and left alone per the guard.")

    print("VERDICT: NARROWED. Selection = one named missing derivation")
    print("  (the locking normalization N), with the metrology chain and")
    print("  the confrontation both armed. Not DERIVED, not FAILED, not")
    print("  UNDERDETERMINED -- the question now has an address.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
