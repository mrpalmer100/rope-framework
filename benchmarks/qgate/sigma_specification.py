"""QGATE-018 -- SPECIFYING THE SIGMA EXPERIMENT: the named arbiter tests the
BRANCH, not the VALUE, and cannot decide between the registered candidates.

Bars locked in analysis/QGATE018_sigma_spec_bars_LOCKED.md BEFORE computing.
"""
import numpy as np

DN_MESH_REF = 5e-34      # QGATE-009, at Sigma = 5.1e35
S_FRAME, S_LATT = 5.10e35, 3.61e35
DN_QED = 2.5e-23         # at 2.5 T (QGATE-010: corpus gives 2.48e-23)
PVLAS_1SIG = 17e-23
VMB_GOAL = 1e-25


def main():
    C = DN_MESH_REF * S_FRAME
    dn = {"Sigma-route (framework)": C / S_FRAME,
          "lattice-anchored": C / S_LATT}
    print("B1 THE MESH SIGNAL for each registered candidate")
    print("   (taking Delta_n_mesh ~ 1/Sigma: a stiffer medium is less nonlinear)")
    for lab, v in dn.items():
        print(f"   {lab:26s} Delta_n = {v:.3e}")
    diff = dn["lattice-anchored"] - dn["Sigma-route (framework)"]
    print(f"   DIFFERENCE between candidates: {diff:.2e}\n")

    print("B2 THE SENSITIVITY REQUIRED")
    print(f"   QED / matter-sector signal at 2.5 T : {DN_QED:.2e}")
    print(f"   PVLAS 1-sigma achieved              : {PVLAS_1SIG:.2e} "
          f"({PVLAS_1SIG/DN_QED:.1f}x above the QED signal)")
    print(f"   VMB@CERN design goal                : {VMB_GOAL:.1e}")
    print(f"   to SEE the mesh at all              : {dn['Sigma-route (framework)']:.1e}"
          f"  -> {PVLAS_1SIG/dn['Sigma-route (framework)']:.1e}x beyond PVLAS,"
          f" {VMB_GOAL/dn['Sigma-route (framework)']:.1e}x beyond VMB@CERN")
    print(f"   to DISCRIMINATE the candidates      : {diff:.1e}"
          f"  -> {PVLAS_1SIG/diff:.1e}x beyond PVLAS,"
          f" {VMB_GOAL/diff:.1e}x beyond VMB@CERN\n")

    print("B3 THE VERDICT, and it is not the one the corpus has been implying:")
    print("   QGATE-007/010 IS NOT A DECIDER FOR SIGMA'S VALUE. Resolving the 28%")
    print("   between the registered candidates needs a birefringence sensitivity")
    print("   roughly 5e8 times beyond even VMB@CERN's design goal. That is not a")
    print("   hard experiment; it is not an experiment.")
    print("   WHAT THE AXIS CAN DO, and it is real:")
    print("     - TEST THE BRANCH. If Sigma were SMALL the mesh nonlinearity would")
    print("       be visible, and PVLAS already excludes that regime -- EM-RECON-016")
    print("       records the ATLAS-identification value excluded by ~570x. The axis")
    print("       is a threshold test on Sigma, and it has already been passed.")
    print("     - TEST THE MATTER SECTOR. QGATE-010's spin-meter reading stands:")
    print("       a non-spinor rope electron would give a (1,3)-negative quartic")
    print("       instead of QED's (4,7)-positive, at the measurable 1e-23 scale.")
    print("       That is a genuine near-term test -- of the ELECTRON's internal")
    print("       class, NOT of Sigma.")
    print("   THE CORPUS HAS BEEN CONFLATING THESE. The polarimetry axis was")
    print("   registered as the arbiter for Sigma; it is the arbiter for the")
    print("   electron's spin class and a threshold test for Sigma's branch.\n")

    print("B4 WHAT WOULD DECIDE SIGMA'S VALUE?")
    print("   Nothing currently registered. The lattice-anchored candidate came")
    print("   from a COMPUTATION on published QCD data (ELEC-052), not from an")
    print("   experiment on the vacuum, and the framework candidate came from an")
    print("   internal consistency argument. The honest position is that the two")
    print("   differ by a calculation, and the way to settle them is a better")
    print("   calculation -- specifically, the ancillary-data flux-tube analysis")
    print("   already done in ELEC-052, extended or independently repeated.")
    print("   NO VACUUM EXPERIMENT IN REACH SEPARATES THEM.\n")

    print("B5 SCALING ASSUMPTION: Delta_n_mesh ~ 1/Sigma. Under 1/Sigma^2 the")
    print("   difference falls further and the verdict strengthens; the mesh signal")
    print("   would have to scale as Sigma^+1 -- a SOFTER medium being LESS")
    print("   nonlinear -- to reverse it, which is unphysical. THE VERDICT IS")
    print("   ROBUST to the scaling choice.")
    assert PVLAS_1SIG / diff > 1e10
    print("PASS: the specification is written, and its content is that the named")
    print("      arbiter does not arbitrate the quantity it was named for.")


if __name__ == "__main__":
    main()
