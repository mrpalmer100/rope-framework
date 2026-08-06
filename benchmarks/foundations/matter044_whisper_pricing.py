"""FND-MATTER-044: the whisper-pricing session. Bars locked BEFORE computing
(analysis/MATTER044_whisper_pricing_results.md):
(1) THE QUESTION: is the 4.6 factor (matter-route T0 vs lattice T0) a tension
or an accounting artifact? m_e is NOT touched (the single calibration stands
as spent; this session re-USES its pinned combination T0*a = m_e c^2/L, no
new fit). (2) THE MOVE, named in advance: solve the m_e-pinned combination
JOINTLY with FND-017's Derived invariance T0 = Sigma a^2/3, anchored on
Sigma_lattice (the corpus's registered 'one open number', QCD flux-tube,
ELEC-081) -- replacing the card's bound-SATURATION adoption of a with a
measurement-consistent point. Zero adjustable choices. (3) SUCCESS CRITERION,
pre-committed: pricing succeeds iff every pairwise EM-sector comparison lands
within the ZPE bar (factor 3), with identity de-duplication enforced (the
T0-vs-R1 and l_q-vs-registered comparisons are ONE fact in two units and are
counted once). (4) The Lorentz bound must remain satisfied. (5) Residuals
that are INVARIANT along the m_e constraint must be proven so and displayed
as the sector's genuine remainders, not absorbed. (6) Failure is reportable:
if comparisons exceed the bar, the whisper is registered as a standing
tension instead.
"""
import numpy as np

HBAR, C = 1.054571817e-34, 2.99792458e8
ALPHA, ME = 1 / 137.036, 9.1093837015e-31
L_RING = 3.141
SIGMA_LAT = 3.61e35            # J/m^3, the registered anchor (ELEC-052/081)
A_CARD, T0_LAT = 1.0e-16, 1203.0
L_Q_REG = 1.39e-15
T0_GRV074_MID = 5847.0
LORENTZ_BOUND = 1.0e-16
BETA, RINGF, H_CORE = 35.4, 0.23, 1.87e-19
NQ_BAND = (1.1e-4, 4.6e-4)
ZPE_BAR = 3.0


def main():
    pinned = ME * C**2 / L_RING                    # T0*a, the m_e combination
    print(f"THE PINNED COMBINATION (spent calibration, re-used not re-fit):")
    print(f"  T0*a = m_e c^2 / L = {pinned:.4e} J")

    # Joint solve with FND-017: Sigma a^3 / 3 = T0*a
    a = (3 * pinned / SIGMA_LAT) ** (1 / 3)
    t0 = SIGMA_LAT * a**2 / 3
    assert abs(t0 * a / pinned - 1) < 1e-12
    print(f"THE M-POINT (joint solution, zero adjustable choices):")
    print(f"  a  = {a:.4e} m")
    print(f"  T0 = {t0:.1f} J/m")
    assert a < LORENTZ_BOUND
    print(f"  Lorentz bound: a = {a/1e-16:.2f}e-16 m < 1e-16 m -- SATISFIED")
    print(f"  with {100*(1 - a/LORENTZ_BOUND):.0f}% margin. The mesh no longer")
    print("  SATURATES the bound; it sits below it. The saturation was the")
    print("  card's adoption, not a measurement, and it is what priced-in the")
    print("  4.6.")

    # The pricing: 4.6 factors along the constraint surface
    f_a = A_CARD / a
    f_t = T0_LAT / t0
    print(f"THE PRICING: 4.6 = {f_a:.2f} (length) x {f_t:.2f} (tension),")
    print(f"  product {f_a * f_t:.2f} -- the whisper was ONE mismatch")
    print("  distributed as TWO in-band factors by holding a at saturation.")

    # Pairwise comparisons, identity-deduplicated
    lq = np.sqrt(4 * np.pi * ALPHA * HBAR * C / t0)
    f_lq = lq / L_Q_REG
    print("PAIRWISE COMPARISONS (ZPE bar = 3; identities counted once):")
    comps = {"a vs card adoption": f_a, "T0 vs lattice anchor": f_t,
             "l_q vs registered": f_lq}
    for k, v in comps.items():
        print(f"  {k}: factor {v:.2f}  [{'inside' if v <= ZPE_BAR else 'OUTSIDE'}]")
        assert v <= ZPE_BAR
    print(f"  (T0 vs the R1 quantum-area anchor = l_q ratio squared = "
          f"{f_lq**2:.2f} -- the SAME fact in tension units; deduplicated, "
          f"not double-counted.)")
    ratio = lq / a
    print(f"  l_q/a = {ratio:.1f} -- still inside the 1-100 window "
          f"(was 33.4 at the card point).")
    assert 1 <= ratio <= 100
    f_rig = T0_GRV074_MID / t0
    print(f"  GRV-074 rigidity: factor {f_rig:.1f} (improved from 22.4; still")
    print("  FLAGGED -- the rigidity audit keeps its rank).")

    # The invariance proof: n_q along the m_e constraint
    # n_q proportional to a * h / l_q^2 ; l_q^2 = 4 pi alpha hbar c / T0
    # => n_q proportional to a * T0 * h = pinned * h : INVARIANT under the joint solve.
    nqs = [4 * np.pi * ALPHA * (3 * BETA / (RINGF * chi))
           * (a * H_CORE / lq**2) for chi in (3.0, 1.0)]
    print(f"THE INVARIANT RESIDUAL: n_q = {nqs[0]:.1e}..{nqs[1]:.1e} vs band")
    print(f"  {NQ_BAND[0]:.1e}..{NQ_BAND[1]:.1e} -- IDENTICAL to the card-point")
    print("  value, PROVEN: n_q tracks a*T0*h = (m_e c^2/L)*h, which the m_e")
    print("  constraint pins. No point on the constraint surface moves it.")
    print("  n_q is therefore the EM sector's sharpest genuine residual")
    print("  (1.5x below band at nearest edges), and it interrogates the one")
    print("  quantity this session cannot: the core thickness h.")
    assert abs(nqs[1] - 7.12e-5) / 7.12e-5 < 0.02

    print("VERDICT: THE WHISPER IS PRICED. Every pairwise EM comparison lands")
    print("  inside the ZPE bar with zero adjustable choices, using only the")
    print("  Derived invariance and the already-spent calibration. The 4.6")
    print("  was bound-saturation accounting, not physics. The M-POINT")
    print("  (a = 6.0e-17 m, T0 = 434 J/m) is proposed as the card's")
    print("  m_e-consistent mesh point (card sync flagged as a docs task;")
    print("  ELEC-052's adoption is superseded-not-erased).")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
