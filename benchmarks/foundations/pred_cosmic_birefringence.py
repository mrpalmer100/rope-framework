"""PRED-002 -- COSMIC BIREFRINGENCE: EB/EE = sin(4 beta)/2, FLAT IN MULTIPOLE.

Registers falsifiable_predictions P3, closing part of the traceability gap
ELEC-063 found. The DISCRIMINATING content is the flatness in l, not the number.
"""
import numpy as np

BETA_DEG = 0.342      # MEASURED, Eskilt & Komatsu 2022 (Phys. Rev. D 106, 063503)
BETA_ERR = 0.094


def eb_over_ee(beta_deg):
    return np.sin(4 * np.radians(beta_deg)) / 2


def main():
    val = eb_over_ee(BETA_DEG)
    print(f"beta = {BETA_DEG} +/- {BETA_ERR} deg (MEASURED input)")
    print(f"THE PREDICTION: EB/EE = sin(4 beta)/2 = {val:.5f}  (paper: 0.0119)")
    assert abs(val - 0.0119) < 5e-4

    print(f"   1-sigma band from beta alone: "
          f"[{eb_over_ee(BETA_DEG-BETA_ERR):.5f}, {eb_over_ee(BETA_DEG+BETA_ERR):.5f}]")

    print("\nTHE DISCRIMINATING CONTENT IS THE SHAPE, NOT THE NUMBER:")
    print("   the rope helix acts as a parity-odd Chern-Simons coupling with a")
    print("   multipole-INDEPENDENT rotation, so EB/EE is FLAT in l:")
    for l in (2, 30, 200, 1000, 3000):
        print(f"     l = {l:5d}:  EB/EE = {val:.5f}")
    print("   Many axion-like and early-dark-energy models instead give an")
    print("   l-DEPENDENT rotation (the birefringence accumulates differently across")
    print("   the recombination and reionization windows). FLATNESS IS THE ROPE-")
    print("   SPECIFIC SIGNATURE and is what a measurement can discriminate.")

    print("\nTHE FALSIFIER: LiteBIRD (launch ~2030s) is designed to the precision this")
    print("   requires. Killed if EB/EE is inconsistent with sin(4 beta)/2 at the")
    print("   measured beta, or if the ratio shows significant l-dependence.")
    print("   NOTE, honest: beta itself is measured, not derived, so this predicts a")
    print("   RELATION between two observables rather than an absolute number.")
    print("PASS: P3 recomputed from stated inputs and registered.")


if __name__ == "__main__":
    main()
