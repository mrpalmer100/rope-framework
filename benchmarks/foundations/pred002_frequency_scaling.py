"""THE ROPE'S FREQUENCY SCALING: the derivation PRED-002-CONF named, and it
forks -- one branch is excluded by 19 orders, the other is a postulate.

Bars locked in analysis/PRED002_FREQ_bars_LOCKED.md BEFORE computing.
"""
import numpy as np

C = 2.99792458e8
NU0 = 150e9
A_STRAND = 5.774e-17      # w = a/sqrt(3), ELEC-053
L_HUBBLE = 1.3e26
BETA_OBS = np.radians(0.3)
N_MEAS, N_ERR = -0.35, 0.48   # Eskilt 2022, all Planck maps, near full sky


def main():
    om = 2 * np.pi * NU0
    psi = 0.5 * om ** 2 * A_STRAND / C ** 2
    total = psi * L_HUBBLE
    print("B1 WHICH ROUTE? The rope medium HAS a structural chirality length,")
    print(f"   w = {A_STRAND:.3e} m. Material optical activity (R2) then gives")
    print(f"   rotation ~ omega^2 w / 2c^2 = {psi:.3e} rad/m at 150 GHz,")
    print(f"   i.e. {total:.3e} rad over a Hubble path against an observed")
    print(f"   {BETA_OBS:.3e} rad.")
    print(f"   OVERSHOOT: {total/BETA_OBS:.2e} -- nineteen orders of magnitude.")
    print("   R2 IS EXCLUDED ON MAGNITUDE ALONE, before any frequency test.")
    assert total / BETA_OBS > 1e15

    print("\nB2 THE n TEST against Eskilt 2022 "
          f"(n = {N_MEAS} +{N_ERR}, Planck DR4 all maps):")
    for n, lab in ((2, "R2 material chiral medium"),
                   (0, "R1 topological / axion-like"),
                   (-2, "Faraday rotation")):
        s = abs(n - N_MEAS) / N_ERR
        print(f"   n = {n:+d}  {lab:30s} {s:4.2f} sigma  "
              f"{'EXCLUDED' if s > 3 else 'allowed'}")
    print("   So the two exclusions AGREE: the material route fails on frequency")
    print("   scaling at 4.9 sigma AND on magnitude by 7e18. Only n = 0 survives.")

    print("\nB3 THE VERDICT AND THE DEBT:")
    print("   PRED-002 keeps n = 0 and its confirmed flatness stands. But the route")
    print("   that delivers n = 0 is the TOPOLOGICAL one, in which the rotation is")
    print("   set by a field excursion rather than by the medium's structure -- and")
    print("   the framework has not shown that its helix produces such a coupling.")
    print("   THE DEBT, stated plainly: a medium with a structural length of 5.8e-17 m")
    print("   must somehow rotate polarization in a way that DOES NOT reference that")
    print("   length, since referencing it overshoots by nineteen orders. That")
    print("   suppression is unexplained, and it is the same suppression the axion")
    print("   gets for free by being a field rather than a structure.")

    print("\nB4 NO RESCUE BY FIAT:")
    print("   Adopting n = 0 because it matches the data would be exactly the move")
    print("   the corpus refused when it closed the gauge branch")
    print("   (ROPE-SOURCE-AUDIT-002: 'reopening would require a genuinely new and")
    print("   explicitly labelled postulate'). If the rope's birefringence is")
    print("   topological, THAT IS A POSTULATE and must be registered as one, with")
    print("   the 19-order suppression as its price.")
    print("   CONSEQUENCE FOR THE CENSUS: PRED-002 remains T3, and its route to T1")
    print("   is now known to be BLOCKED rather than merely unexplored -- the")
    print("   discriminating observable exists, the framework's natural answer for it")
    print("   is excluded, and the surviving answer is indistinguishable from the")
    print("   axion by construction.")
    print("\nPASS: the named derivation was done and it closed a door rather than")
    print("      opening one, which is the informative outcome.")


if __name__ == "__main__":
    main()
