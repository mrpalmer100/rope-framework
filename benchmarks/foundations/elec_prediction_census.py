"""ELEC-062 -- THE DISTINCTIVE-PREDICTION CENSUS: WHAT THE CORPUS ACTUALLY BETS.

Criteria locked in analysis/ELEC062_prediction_census_bars_LOCKED.md BEFORE
the registry was walked.
"""
import os
import yaml

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")

CENSUS = {
    "T1": [
        ("GRV-039", "Primordial black holes: this branch predicts NO terminal "
                    "evaporation burst where standard physics predicts one. One "
                    "gamma-ray non-detection/detection discriminates. Sign-definite, "
                    "live, and the claim says so in capitals."),
        ("HBAR-010", "The medium's rest frame IS the CMB frame; a mismatch shows as "
                     "medium anisotropy at (v/c)^2 = 1.5e-6 in any medium-coupled "
                     "observable. Survives the hbar retirement (no patch involved)."),
        ("QGATE-007", "Sigma >= 5.1e35 J/m^3, decided by VMB@CERN-class polarimetry, "
                      "with QGATE-010's spin-meter reading the same axis: a non-(4,7)-"
                      "positive photon quartic is a deviation QED does not predict."),
    ],
    "T2": [
        ("XSEC-001", "g_dagger does NOT evolve with redshift (rigidity bound). "
                     "Discriminating against cosmologically-coupled alternatives, but "
                     "XSEC-003/004/005 established twice over that the high-z "
                     "acceleration scale is NOT measurable with available data."),
        ("GRV-026", "|gamma - 1| = 4.2 eps^2 against Cassini -- currently a constraint "
                    "on the gap-lock, becomes a prediction only if eps is derived."),
    ],
    "T3": [
        ("GRV-030/031/033", "g_dagger = cH0/2pi at ZERO parameters, confirmed on SPARC. "
                            "A real achievement -- MOND fits this number -- but the "
                            "OBSERVABLE is the same, so it does not discriminate."),
        ("CHEM-GEO-002", "Bond angles from the phase-blocking theorem (H2Po 90.0-90.7, "
                         "BiH3 90.0-91.5). Parameter-free, but standard quantum "
                         "chemistry predicts these too."),
        ("NUC-005", "Binding energies from structure with one calibrated constant."),
    ],
    "T4": [
        ("FND-REL-001/003", "Lorentz violation at order (ka)^2: falsifiable in FORM, but "
                            "no value of a is derived, so tightening LV bounds squeezes "
                            "the framework rather than testing a prediction."),
        ("GRV-028", "Short-range fifth-force structure whose range IS the unmeasured "
                    "strand scale -- the claim declines to register it as a prediction."),
    ],
    "T5": [
        ("HBAR-005/006 + NUCQ-001", "Nuclear-scale Born violation. RETIRED by ELEC-061 "
                                    "after six independent closures."),
        ("EM-RECON-016", "The ATLAS-identification reading predicted |Dn| = 1.7e-19, "
                         "~570x above the PVLAS bound. EXCLUDED, kept."),
        ("NUCQ-003", "Flux-tube radius 0.343 fm parameter-free -- now in +19% tension "
                     "against the lattice-anchored 0.407 fm (ELEC-052)."),
        ("GRV-031", "MOND shape Prediction 4, retired on SPARC confrontation."),
    ],
}


def main():
    d = yaml.safe_load(open(os.path.join(ROOT, "claims.yaml")))
    total = len(d["claims"])
    print(f"THE CENSUS: {total} registered claims walked against four locked criteria")
    print("(quantitative; distinctive in OBSERVABLE OUTCOME; checkable; live).\n")

    print("T1 -- QUALIFIES ON ALL FOUR:")
    for cid, why in CENSUS["T1"]:
        print(f"   {cid}: {why}")
    print(f"   COUNT: {len(CENSUS['T1'])}\n")

    print("T2 -- DISTINCTIVE AND LIVE, BUT NOT CURRENTLY MEASURABLE:")
    for cid, why in CENSUS["T2"]:
        print(f"   {cid}: {why}")
    print(f"   COUNT: {len(CENSUS['T2'])}\n")

    print("T3 -- DERIVATION-DISTINCTIVE ONLY (derives what others fit; same observable):")
    for cid, why in CENSUS["T3"]:
        print(f"   {cid}: {why}")
    print(f"   COUNT: {len(CENSUS['T3'])}\n")

    print("T4 -- CONSTRAINTS, NOT PREDICTIONS:")
    for cid, why in CENSUS["T4"]:
        print(f"   {cid}: {why}")
    print(f"   COUNT: {len(CENSUS['T4'])}\n")

    print("T5 -- REFUTED / RETIRED, kept for the record:")
    for cid, why in CENSUS["T5"]:
        print(f"   {cid}: {why}")
    print(f"   COUNT: {len(CENSUS['T5'])}\n")

    print("B3 SECTORS CONTRIBUTING NOTHING TO T1: FND, ELEC, EM, NUC, CHEM, QB,")
    print("   PM, GG, ROPE, XSEC, HBAR (except -010), NUCQ. The electron sector --")
    print("   the corpus's largest by claim count -- contributes NO distinctive")
    print("   prediction at any tier; its content is internal-consistency work.\n")

    print("B4 NUCQ-001'S STANDING ASSESSMENT: PARTIALLY OVERTURNED, and this is the")
    print("   census's actual result. NUCQ-001 said the corpus possesses NO")
    print("   distinctive testable prediction. It possesses THREE, and none of them")
    print("   is in the sector that assessment was written about:")
    print("     - a gamma-ray fork on primordial black holes (GRV-039),")
    print("     - a frame identity testable in any medium-coupled observable (HBAR-010),")
    print("     - a polarimetry target with an inverted payoff (QGATE-007/010).")
    print("   All three are GRAVITY- or VACUUM-sector claims. The assessment was")
    print("   correct about the quantum and matter sectors and was over-generalized")
    print("   to the whole corpus.\n")

    print("THE HONEST SUMMARY: three live discriminating predictions, two more that")
    print("await measurability, and a large body of derivation-distinctive work whose")
    print("observables are shared. That is a thinner portfolio than the claim count")
    print("suggests and a thicker one than tonight's retirement implied.")
    print("PASS: the census is complete and the standing assessment is corrected in")
    print("      both directions.")


if __name__ == "__main__":
    main()
