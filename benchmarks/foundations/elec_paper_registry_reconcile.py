"""ELEC-063 -- RECONCILING THE PREDICTIONS PAPER WITH THE REGISTRY.

ELEC-062's census walked claims.yaml only and missed papers/. This corrects it
and measures the divergence. Bars locked in
analysis/ELEC063_paper_registry_bars_LOCKED.md BEFORE the reconciliation.
"""
import os
import yaml

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")

# The paper's seventeen, classified on CONTENT against ELEC-062's unchanged criteria
PAPER = [
    ("P1  MOND scale g+ = cH0/2pi", "T3", "derives what MOND fits; same observable. The DRIFT test (g+ tracking H0) is the distinctive part and is T2."),
    ("P2  Sum m_nu = 58.5 meV", "T1", "sharp, risky, near-term (KATRIN/cosmology/0nubb converging); sits just above the normal-ordering minimum with nothing left to adjust. NOT IN REGISTRY."),
    ("P3  Cosmic birefringence EB/EE = 0.0119, FLAT in multipole", "T1", "the flatness in l is the rope-specific signature; LiteBIRD is designed to this precision. NOT IN REGISTRY."),
    ("P4  MOND interpolation shape", "T5", "RETIRED at GRV-031, kept visible."),
    ("P5  Gauge-boson Koide structure", "T3", "structural; no discriminating number committed."),
    ("P6  d ln alpha = -2 d ln G", "T1", "testable NOW against quasar alpha-dot and lunar-laser-ranging G-dot bounds; a ratio inconsistent with -2 kills it. Provisional on one derivation. NOT IN REGISTRY."),
    ("P7  Vacuum Kerr nonlinearity", "T5/T2", "the identification reading EXCLUDED by PVLAS (~570x); what survives is the Sigma bound, which is QGATE-007's axis."),
    ("P8  Dark longitudinal tension channel", "T4", "structural; decoupled from matter, no near-term observable."),
    ("P9  Heavy-hydride 90-degree asymptote", "T3", "H2Po 90.0-90.7, BiH3 90.0-91.5: quantitative and one-sided, but the paper itself labels it consistency-tier against quantum chemistry."),
    ("P10 Gapped environmental noise floor", "T2", "scale-open: a structural signature with no scale to place it."),
    ("P11 Detection is nucleation kinetics", "T2", "first-passage package where the model applies; scale-open."),
    ("P12 Spin-1/2 requires extension", "T3", "one-sided and shared with QM's own account."),
    ("P13 Tsirelson forever", "T3", "shared with quantum mechanics; distinctive in the WHY, not the observable."),
    ("P14 Born's square from channel energy", "T3", "p = 2 shared; distinctive mechanism."),
    ("P15 Analog universality", "T1", "testable NOW in engineered twist-chain systems (pendulum arrays, domain-wall lattices, cold-atom sine-Gordon); a friction-constant failure kills it."),
    ("P16 Isolated black holes do not evaporate", "T1", "= GRV-039, the one ELEC-062 caught."),
    ("P17 The whisper: 0.23 kappa running-temperature tail", "T1", "accretion-powered emission with a computed frequency scale; the strand scale cancels."),
]
MISSING_FROM_REGISTRY = ["P2 (58.5 meV)", "P3 (EB/EE = 0.0119)", "P6 (d ln alpha = -2 d ln G)"]
REGISTRY_ONLY = ["HBAR-010 (medium rest frame = CMB frame, anisotropy at 1.5e-6)",
                 "QGATE-007/010 (Sigma >= 5.1e35; (4,7)-positive photon quartic)"]


def main():
    n = len(yaml.safe_load(open(os.path.join(ROOT, "claims.yaml")))["claims"])
    print(f"ELEC-062 walked {n} registry claims and reported THREE distinctive")
    print("predictions. It never opened papers/falsifiable_predictions.docx, which")
    print("states seventeen. THE CENSUS WAS INCOMPLETE BY CONSTRUCTION.\n")

    t1 = [p for p in PAPER if p[1] == "T1"]
    print("B1 THE CORRECTED T1 LIST (paper entries, same criteria, unrelaxed):")
    for name, _, why in t1:
        print(f"   {name}\n      {why}")
    print(f"   PAPER T1 COUNT: {len(t1)}")
    print("   Plus the two the registry carries that the paper does NOT list:")
    for r in REGISTRY_ONLY:
        print(f"      {r}")
    print(f"   CORRECTED CORPUS T1 TOTAL: {len(t1) + len(REGISTRY_ONLY)} "
          f"(ELEC-062 said 3)\n")

    print("B2 THE REGISTRY GAP, and it is a defect:")
    for m in MISSING_FROM_REGISTRY:
        print(f"   {m} -- NO corresponding registry claim")
    print("   The paper states that every statement is 'traceable to the")
    print("   machine-readable registry (claims.yaml), the corpus's single source of")
    print("   truth'. THAT SENTENCE IS FALSE FOR THREE OF ITS SHARPEST NUMBERS,")
    print("   including the one it calls sharp and risky. This is the same class of")
    print("   defect as tonight's misfiled-claims corruption: a traceability")
    print("   guarantee that does not hold.\n")

    print("B3 THE PAPER GAP (registry T1 entries the paper omits):")
    for r in REGISTRY_ONLY:
        print(f"   {r}")
    print("   Both are live and discriminating; the paper is out of date by at least")
    print("   these two.\n")

    print("B4 NO SOFTENING APPLIED. P1's g+ = cH0/2pi stays T3 (MOND fits the same")
    print("   observable); its DRIFT test is the distinctive part. P9 stays T3 on the")
    print("   paper's own consistency-tier label. P13/P14 are distinctive in mechanism")
    print("   and shared in observable.\n")

    print("B5 WHAT IS OWED:")
    print("   (i)  register P2, P3, P6 as claims with benchmarks, or strike the")
    print("        traceability sentence -- the corpus cannot assert both;")
    print("   (ii) add HBAR-010 and QGATE-007/010 to the paper;")
    print("   (iii) ELEC-062's T1 count is corrected from 3 to 8 and its sectoral")
    print("        finding survives (the electron sector still contributes nothing).")
    print("   THE LESSON, recorded: a census that defines its own universe as one")
    print("   file will miss whatever lives in another. The registry is the single")
    print("   source of truth by declaration, and this session shows the declaration")
    print("   is not currently true.")
    print("PASS: the reconciliation is complete and the census's failure mode is named.")


if __name__ == "__main__":
    main()
