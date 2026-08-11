"""Commission PHI — bounding the packing factor: the verdict HARDENS, the
ceiling is priced, and additivity violation gets its first measured number.

B1 THE ROUTES: the finite-T route (1702.03454) is STRUCTURALLY UNAVAILABLE
   for the adjoint width below Tc -- non-singlet Polyakov loops vanish below
   Tc, and above Tc the paper's own central result is that flux tubes do not
   exist. The zero-T hybrid Wilson-loop route (PRD 81 034504) delivers.
B2 THE VERDICT: the PRD states the glueball (adjoint) and meson tubes are
   "compatible with an identical shape ... but with a different density"
   at the Casimir factor 9/4 (constant across the mediator profile,
   2.25(2)/2.24(6) in the companion proceedings) -> rho_R = 1.0 within
   errors -> kappa_rel = (9/4)/rho_R^2 = 2.25 -> UPSILON's BROKEN verdict
   HARDENS with peer-reviewed data: tube strands compress by 2.25x without
   the radius moving. Caveats: beta = 6.2, separation ~0.58 fm, no numeric
   width errors published -> rho_R precision is the ~few-percent class of
   the constant-ratio fit, not a dedicated width analysis.
B3 THE ABSOLUTE CEILING (registered d_c = 1.87e-19 m hard core, close
   packing vs vacuum areal density 3/a^2): kappa_pack <= 1.1e5 (Lorentz-
   bound a) or 4.0e4 (M-point a). Stated plainly: uselessly weak.
BONUS, REGISTERED: the measured SUPER-ADDITIVITY -- the adjoint string
   tension is 1.125x the sum of two fundamental strings (Bali Casimir
   scaling read through the fusion picture), i.e. delta_fusion = +12.5% at
   kappa_rel = 2.25. The E_x inter-strand channel now has one empirical
   calibration point (kappa, delta) = (2.25, +0.125) plus the anchor
   (1, 0). PLAUSIBILITY NOTE (Conjecture-grade, NOT a bound): if delta and
   compression grow together and the fundamental tube is the LESS
   compressed of the pair, the fundamental's own delta -- and hence
   |Sigma_vac/Sigma_eff - 1| -- is plausibly sub-25%; measuring kappa_fund
   remains the named open target.
"""
import math

D_C = 1.87e-19
CASIMIR = 9 / 4
DELTA_FUSION = CASIMIR / 2 - 1          # +0.125


def ceiling(a):
    return (a / D_C) ** 2 * 2 / (3 * math.sqrt(3))


def main():
    assert abs(DELTA_FUSION - 0.125) < 1e-12
    kappa_rel = CASIMIR / 1.0 ** 2
    assert abs(kappa_rel - 2.25) < 1e-12
    c1, c2 = ceiling(1e-16), ceiling(6e-17)
    assert 1.0e5 < c1 < 1.2e5 and 3.5e4 < c2 < 4.5e4
    print(f"kappa_rel = {kappa_rel} (HARDENS); delta_fusion = {DELTA_FUSION:+.1%}")
    print(f"absolute ceilings: {c1:.1e} (Lorentz a), {c2:.1e} (M-point a) -- weak, stated")
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
