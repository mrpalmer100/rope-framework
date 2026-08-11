"""Commission PSI — why strand count follows the Casimir: the derivation,
its retrodictions, and the Conjecture-grade kappa_pack lower bound.

THE CHAIN (premises graded in the bars file):
  P1 (assumption, then measured): mesh linear at tube strains.
  P2 (new transcription): linearity => strain field = Green(geometry) x
     charge => ensemble energy density u_D(r) = C_D * u_1(r) with a
     charge-independent shape u_1 set by the medium.
  P3 (registered EM, assumed chromo): u ~ strain^2.
  P4 (registered): nu = u/T0.
  => n_D/n_f = C_D/C_f (the recruitment rule, DERIVED), same profile
     shape (rho_R = 1), same penetration length lambda.

RETRODICTIONS (all data already in context, labeled as such):
  - adjoint/fundamental density ratio: C_8/C_3 = 2.25 vs measured 2.25(2),
    constant across the profile as the shape-factorization demands;
  - rho_R = 1 (UPSILON/PHI) -- the vacuum-packing failure EXPLAINED:
    radius is medium geometry, density is charge;
  - lambda-universality across representations (Lisbon).

THE BOUND (B3, Conjecture grade): analytic leading nonlinearity =>
  delta_D = eps_f (C_D/C_f - 1), eps_f = u_f/Sigma_vac.
  Bali <= 5% at C_D/C_f = 6  => eps_f <= 1%  => kappa_pack >= ~100.
  Continuum ~1% reading      => kappa_pack >= ~500.
  FALSIFIABLE FORM: resolved CS violations must be one-signed and linear
  in the Casimir, or P1's measurement and this bound fall together.

CONSEQUENCE (named, not computed): Sigma_vac >= ~3.6e37 J/m^3 under the
bound; every vacuum-facing number is FROZEN pending the re-solve
commission; the corpus quotes Sigma_eff only until then.
"""
CASIMIR_RATIO = {"6": 2.5, "8": 2.25, "10": 4.5, "15a": 4.0, "27": 6.0, "15s": 7.0}
MEASURED_DENSITY_RATIO_ADJ = (2.25, 0.02)
CS_BOUND, CS_CONTINUUM = 0.05, 0.01
SIGMA_EFF = 3.61e35


def main():
    # Retrodiction: derived density ratio = Casimir ratio, adjoint point
    pred = CASIMIR_RATIO["8"]
    v, e = MEASURED_DENSITY_RATIO_ADJ
    assert abs(pred - v) <= 2 * e
    # The bound arithmetic (worst representation drives it)
    cmax = max(CASIMIR_RATIO.values())
    eps_f_5 = CS_BOUND / (cmax - 1)
    eps_f_1 = CS_CONTINUUM / (cmax - 1)
    k5, k1 = 1 / eps_f_5, 1 / eps_f_1
    assert 90 < k5 < 130 and 450 < k1 < 650
    # Falsifiable form: violations linear in C -> ordering fixed
    deltas = {r: eps_f_5 * (c - 1) for r, c in CASIMIR_RATIO.items()}
    order = sorted(deltas, key=deltas.get)
    assert order[0] == "8" and order[-1] == "15s"
    print(f"retrodiction: adjoint density ratio {pred} vs {v}({e}) OK")
    print(f"kappa_pack >= {k5:.0f} (5% CS bound) / >= {k1:.0f} (continuum 1%)")
    print(f"Sigma_vac >= {k5*SIGMA_EFF:.1e} J/m^3 under the Conjecture-grade bound")
    print("predicted CS-violation ordering (one-signed, linear in C):",
          " < ".join(order))
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
