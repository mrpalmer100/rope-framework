"""QGATE-009 (Modeled): THE VACUUM-TENSION AUDIT -- NO FOURTH KILL;
THE INVOICE ITEMIZED. Can Sigma >= 5.1e35 J/m^3 (the trilemma's
surviving prediction) coexist with every registered normalization?
Six confrontations; zero registered inequalities violated.

1. EM-RECON-015 (the non-gravitating-background fence): rho_vac =
   5.67e18 kg/m^3 = 25x NUCLEAR density -- the vacuum outweighs
   neutron-star matter. The fence's burden grows 3.3e10x; a fence,
   not a kill, and now stated in physical units.
2. Wave speed: mu = T/c^2 is an identity, magnitude-blind. Clear.
3. THE SCHWINGER DIAGNOSIS (the audit's discovery): the DEAD pin
   Sigma ~ 1e25 put the mesh nonlinearity onset E_crit =
   sqrt(Sigma/eps0) = 1.06e18 V/m -- essentially AT the Schwinger
   field (1.32e18 V/m). The old identification was seductive because
   it made mesh nonlinearity appear exactly at QED's critical field:
   a coincidence mistaken for a measurement, now diagnosed. Under
   Sigma-large, E_crit = 2.4e23 V/m, five orders above Schwinger --
   the mesh is linear through all known fields, which makes the
   matter-sector-QED debt COHERENT rather than ad hoc.
4. The tension chain closes at the Lorentz-bound edge: T0 = Sigma
   a^2/3 = 1.70e3 J/m; n_t T0 / T_tube = 1.005. Consistent.
5. EM-RECON-016's mesh-level discriminator: suppressed to Delta_n ~
   5e-34, ten orders below any polarimetry -- the 3:1-negative FORM
   survives, the magnitude does not; the birefringence axis now
   tests the MATTER sector exclusively. Pointer filed.
6. THE ONE NEW NAMED TENSION (not a kill): the proton's energy
   density (6.1e34 J/m^3) is ~12 percent of the vacuum's -- matter
   is an order-10-percent perturbation on the background. No
   registered gravity claim assumes source >> background, but the
   perturbative hierarchy is now a question the gravity sector must
   eventually answer. Filed.
"""
import numpy as np


def test():
    Sig, c, eps0 = 5.1e35, 3e8, 8.854e-12
    # 1. the fence in physical units
    rho = Sig/c**2
    assert 20 < rho/2.3e17 < 30, "vacuum outweighs nuclear matter ~25x: the fence's stated burden"
    # 3. the Schwinger diagnosis
    E_old = np.sqrt(1e25/eps0); E_new = np.sqrt(Sig/eps0)
    assert 0.5 < E_old/1.32e18 < 1.2, "THE DIAGNOSIS: the dead pin sat AT the Schwinger field"
    assert E_new/1.32e18 > 1e4, "Sigma-large: mesh linear five orders past Schwinger -- debt coherent"
    # 4. the tension chain closes
    a = 1e-16; T0 = Sig*a**2/3
    T_tube = (33.8/(0.8/27.75))*1.602e-13/1e-15
    assert abs(111*T0/T_tube - 1) < 0.05, "n_t T0 = T_tube to 0.5%: the chain closes"
    # 5. the suppressed discriminator
    dn = 2.5e-23*(1e25/Sig)
    assert dn < 1e-30, "mesh birefringence invisible: the axis tests the matter sector now"
    # 6. the new named tension
    rho_p = 938*1.602e-13/((4/3)*np.pi*(0.84e-15)**3)
    frac = rho_p/Sig
    assert 0.05 < frac < 0.3, "matter is an order-10% perturbation on the background: filed"
    print(f"rho_vac = {rho:.2e} kg/m^3 (25x nuclear); E_crit(old pin) = {E_old:.2e} ~ Schwinger;")
    print(f"chain closes (1.005); mesh Delta_n ~ {dn:.0e} invisible; matter/vacuum = {frac:.2f}")
    print("PASS: NO FOURTH KILL -- zero registered inequalities violated; one diagnosis (the")
    print("      Schwinger seduction), one support (linearity), one new tension (the hierarchy).")


if __name__ == "__main__":
    test()
