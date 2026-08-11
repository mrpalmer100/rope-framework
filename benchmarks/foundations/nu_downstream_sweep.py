"""Commission NU — the downstream re-evaluation sweep at the pinned Sigma.

Re-runs every registered formula conditioned on Sigma = 5.10e35 at the pinned
lattice band 3.61-3.70e35 J/m^3 (Commission MU / FND-030 draft), at BOTH band
edges per locked bar B5. Fails if any verdict class recorded below drifts.

Verdict ledger (locked classes: UNCHANGED / SHIFTED / FLIPPED / DEAD):
  S1(1) fence            SHIFTED   25x -> 17.5-17.9x nuclear (eases, fence stands)
  S1(2) wave speed       UNCHANGED magnitude-blind identity
  S1(3) Schwinger sep    UNCHANGED 1.5e5x Schwinger >= 100x bar (B2 passes)
  S1(4) tension chain    UNCHANGED M-point T0 = 433-444 J/m brackets card's 434
  S1(5) mesh Delta_n     SHIFTED   5e-34 -> 6.9-7.1e-34; still 1.4e8x below VMB goal
  S1(6) proton/vacuum    SHIFTED   11.9% -> 16.4-16.8%; below the 30% escalation bar
  S2    kappa_0          SHIFTED-RESOLVED: registered bound 26-50 traced to the DEAD
                         Schwinger-form Sigma band; at pinned Sigma the one-number
                         lock RESOLVES: kappa_0 = 1.66-1.68e-4 m^3/(s C),
                         rho = 4.0-4.1e18 kg/m^3 (floor 4.5e7 holds by 11 orders)
  S3    Ledger B         UNCHANGED w = a/sqrt(3) at the Lorentz bound is
                         Sigma-insensitive (5.77e-17 both branches); M-point
                         w = 3.46e-17 already on the card; ELEC-058's
                         scale-invariance keeps every re-based death dead
  S4    QGATE-008 chain  DEAD-CONFIRMED: the antecedent's Sigma >= 5.1e35 clause
                         now fails on its own terms at the pinned band -- a second,
                         independent death of a chain ELEC-047 already killed;
                         threshold test UNCHANGED (mesh 2.4e11x below PVLAS,
                         still deep in the large-Sigma regime)
"""
import math

C = 2.99792458e8
EPS0 = 8.8541878128e-12
E_SCHW = 1.32e18
RHO_NUC = 2.3e17
BAND = (3.61e35, 3.70e35)
OLD = 5.10e35
A_M = 6.0e-17
MP_PROTON = 1.67262192e-27
R_PROTON = 0.84e-15


def main():
    for S in BAND:
        rho = S / C ** 2
        assert 17.0 < rho / RHO_NUC < 18.5          # S1(1)
        assert math.sqrt(S / EPS0) / E_SCHW >= 100  # S1(3), bar B2 (actual ~1.5e5)
        assert abs(S * A_M ** 2 / 3 - 438.6) < 6    # S1(4) T0 in 433-444
        dn = 5e-34 * OLD / S
        assert dn < 1e-25 / 1e7                      # S1(5) >= 1e7x below VMB goal
        u_p = MP_PROTON * C ** 2 / ((4 / 3) * math.pi * R_PROTON ** 3)
        assert u_p / S < 0.30                        # S1(6) below escalation bar (B3)
        k0 = C / math.sqrt(EPS0 * S)
        assert 1.6e-4 < k0 < 1.7e-4                  # S2 resolved value
        assert rho >= 4.5e7                          # S2 EM-RECON-029 floor
        assert dn < 1.7e-22 / 1e10                   # S4 threshold: large-Sigma regime
    # S2 provenance: the registered 26-50 bound reproduces from the dead band
    assert 25 < C / math.sqrt(EPS0 * 1.5e25) < 27
    assert 49 < C / math.sqrt(EPS0 * 4.0e24) < 52
    # S3: Lorentz-bound w is Sigma-insensitive; M-point w on the card
    assert abs(9.999e-17 / math.sqrt(3) - 5.773e-17) < 1e-20
    assert abs(A_M / math.sqrt(3) - 3.464e-17) < 1e-20
    # S4: the pinned band fails the old antecedent
    assert BAND[1] < OLD
    print("ALL CHECKS PASS — sweep verdicts as recorded in the ledger above.")


if __name__ == "__main__":
    main()
