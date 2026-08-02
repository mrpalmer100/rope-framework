"""ELEC-064 -- THE T1 AUDIT: the same treatment PRED-002 got, applied to the rest.

Bars locked in analysis/ELEC064_t1_audit_bars_LOCKED.md BEFORE the audit.
"""
import os
import yaml

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")

AUDIT = [
 ("GRV-039", "DEMOTE -> T2", [
   "DISTINCTIVE: YES, genuinely. Standard physics predicts steady Hawking",
   "evaporation; this predicts the horizon goes quiet after formation. The",
   "divergence is real and sign-definite.",
   "CHECKABLE: NO, on the conditional-population test (D2). Hawking radiation",
   "has never been observed from any astrophysical black hole -- T_H for a",
   "stellar-mass hole is ~1e-8 K, unobservably far below the CMB. The only",
   "channel where evaporation is observable is a terminal burst from a ~1e15 g",
   "primordial hole, and NO SUCH OBJECT IS KNOWN TO EXIST. A non-detection is",
   "already fully explained by PBH abundance limits, so it cannot discriminate.",
   "The prediction is conditional on an unestablished population."]),
 ("GRV-040", "KEEP T1 (the strongest entry)", [
   "DISTINCTIVE: YES. A whisper at omega = 0.23 kappa, within a factor of two",
   "of the Hawking thermal peak but by a DIFFERENT mechanism, with the strand",
   "scale cancelling out of the frequency.",
   "CHECKABLE: this is the one that escapes GRV-039's problem, because the",
   "companion claims make it ACCRETION-POWERED rather than thermal -- the",
   "luminosity is not set by T_H. That decouples it from the unobservability",
   "that kills the evaporation channel.",
   "CAVEAT, stated: the claim's own status (GRV-044 Derived, GRV-040-043",
   "Modeled) shows the accretion normalisation is registered as an OPEN",
   "question. Until a flux is committed, this is T1 on shape but its",
   "detectability is unquantified."]),
 ("HBAR-010", "DEMOTE -> T4, AND A DEPENDENCY ERROR IN ELEC-061", [
   "DEPENDENCY HYGIENE (D1) FAILS. This claim's chain runs through HBAR-006",
   "(it is in depends_on, and the argument opens 'HBAR-006 established",
   "hbar c = N^2 T w^2 so with T a strand property hbar ~ w^2'). HBAR-006 was",
   "CLOSED by ELEC-061. ELEC-061's classification recorded HBAR-010 as",
   "SURVIVES because it 'never involved the patch' -- that was WRONG: it does",
   "not use the patch as a length, but it uses the retired relation hbar ~ w^2",
   "as its premise. Under the surviving standing-wave form S = pi T A^2/(2c),",
   "hbar scales with the AMPLITUDE, not the strand spacing, so the comoving-",
   "medium exclusion does not follow as stated.",
   "WHAT SURVIVES ANYWAY: the CONCLUSION is robust for a different reason --",
   "any medium property tied to expansion would drag a dimensionless constant,",
   "and the corpus needs a rigid substrate regardless. But that makes it a",
   "CONSTRAINT the framework must satisfy, not a prediction it makes.",
   "DISTINCTIVE: NO. 'The medium's rest frame is the CMB frame' has no",
   "committed observable: 'any medium-coupled observable' is not an",
   "instrument, and no medium-coupled observable is specified anywhere."]),
 ("QGATE-007/010", "DEMOTE -> T2, on the unbuilt-model test", [
   "THE INVERTED PAYOFF CUTS BOTH WAYS (D3). The branch that SUPPORTS the",
   "framework is a QED-like polarimetry result -- but QED already predicts",
   "QED, so that outcome discriminates nothing. The branch that would",
   "DISCRIMINATE is a non-(4,7) photon quartic from a non-spinor rope electron.",
   "QGATE-010 states in its own text that the electron model is NOT BUILT",
   "(PM-005: mass an input, structure unbuilt).",
   "So the discriminating branch cannot currently be predicted, only",
   "specified. This is an ACCEPTANCE TEST, which the claim itself says, and",
   "an acceptance test is not a prediction.",
   "WHAT IT REMAINS: a genuine and valuable standing commitment -- if the",
   "electron is ever built and comes out non-spinor, the framework is dead.",
   "That is worth keeping, at T2."]),
 ("PRED-001", "DEMOTE -> T3", [
   "DISTINCTIVE: NO, on the observable. 58.47 meV sits just above the normal-",
   "ordering minimum near 59 meV, and the claim's own note concedes that 'a",
   "confirming measurement would be weak evidence since the floor is where any",
   "normal-ordering scenario lands'. Minimal-NO is the generic expectation of",
   "a large class of models, so a measurement there does not select this one.",
   "FALSIFIABLE: YES, strongly -- inverted ordering or a sum away from 58-59",
   "meV kills it. But asymmetric falsifiability without discriminating",
   "confirmation is T3 under the locked criteria, not T1.",
   "AND the pi/12 offset is an INPUT, which the claim states."]),
 ("PRED-003", "KEEP T1", [
   "Audited in depth this session (PRED-003-CONF, -META, -J1713): distinctive",
   "(no standard physics ties alpha and G drift by -2), checkable NOW,",
   "confronted, survived at 1.74 sigma, with a named system, a named",
   "systematic, a threshold and a date (~2027-2030). Unchanged."]),
]


def main():
    n = len(yaml.safe_load(open(os.path.join(ROOT, "claims.yaml")))["claims"])
    print(f"THE T1 AUDIT ({n} claims in registry; criteria from ELEC-062, unrelaxed,")
    print("plus dependency hygiene, the conditional-population test, and the")
    print("unbuilt-model test locked in advance)\n")
    for cid, verdict, lines in AUDIT:
        print(f"--- {cid}: {verdict}")
        for l in lines:
            print(f"    {l}")
        print()
    kept = [a[0] for a in AUDIT if a[1].startswith("KEEP")]
    print(f"B2 THE CORRECTED T1 LIST: {kept} -- COUNT {len(kept)}.")
    print("   Down from the seven standing at the start of this audit, and from")
    print("   the eight ELEC-063 reported. Every demotion is on a criterion that")
    print("   was locked before the entry was examined.")
    assert len(kept) == 2

    print("\nB3 CORRECTIONS OWED:")
    print("   ELEC-061: its classification of HBAR-010 as SURVIVES rested on")
    print("   'never involved the patch'. HBAR-010 does not use the patch but DOES")
    print("   use HBAR-006's retired relation hbar ~ w^2 as its premise. The")
    print("   classification rule (does the result survive deleting the mesoscopic")
    print("   identification?) was applied too narrowly.")
    print("   ELEC-062/063: the T1 count is corrected from eight to TWO.")

    print("\nB4 WHAT THE CORPUS IS LEFT BETTING, without softening:")
    print("   TWO live discriminating predictions.")
    print("   - PRED-003, the alpha-G drift ratio: testable now, confronted,")
    print("     surviving, with a decision expected 2027-2030.")
    print("   - GRV-040, the whisper at 0.23 kappa: distinctive in mechanism and")
    print("     frequency, accretion-powered so not thermally suppressed, but with")
    print("     an uncommitted flux -- its detectability is the open question.")
    print("   Everything else is a constraint the framework must satisfy, a")
    print("   specification awaiting a model it has not built, a prediction")
    print("   conditional on objects not known to exist, or a correct result whose")
    print("   observable is shared with standard physics.")
    print("   THE SINGLE HIGHEST-VALUE MOVE now visible: commit a flux for GRV-040.")
    print("   It is the only entry whose promotion depends on work the corpus can do")
    print("   rather than on an experiment or a model it lacks.")


if __name__ == "__main__":
    main()
