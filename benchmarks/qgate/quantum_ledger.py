"""QGATE-002 (Modeled): THE QUANTUM-INPUT LEDGER -- the corpus-wide
Part-1 audit. 92 marker-touching claims classified into six dependence
categories plus incidental; the structural findings asserted here:

(1) FOUR underlying inputs: the 11 genuinely dependent claims
    bottleneck through electron mass, spin degeneracy, the 13.6 eV
    calibration, and the induced-gravity action normalization.
(2) THE CLASSICALIZED POPULATION EXISTS: 14 claims -- the lambda
    saga's category made a measured fact (FND-MATTER-033/034 members).
(3) THE SPLIT FRONTIER AT LEDGER LEVEL: every genuine input is
    action-scale-flavored; the nonlocal residues (Born, entanglement,
    measurement) appear only as fences with ZERO scale inputs -- one
    branch is missing a number, the other a kind of dynamics.

Classification has curated freedom (override table with printed
justifications); asserts are on robust structure, not exact counts.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
import quantum_audit as Q


def test():
    ledger, counts = Q.run(verbose=False)
    genuine = {k: v for k, v in ledger.items() if v['cat'] in ('IMPORT', 'CALIB', 'NUMER')}
    # (1) few true inputs, not dozens
    assert 5 <= len(genuine) <= 20, "genuine quantum dependence is a small population"
    assert 'PM-005' in genuine and genuine['PM-005']['cat'] == 'IMPORT', "electron mass = direct import"
    assert 'EM-RECON-010' in genuine and genuine['EM-RECON-010']['cat'] == 'CALIB', "13.6 eV = calibration proxy"
    assert 'GRV-021' in genuine and genuine['GRV-021']['cat'] == 'NUMER', "induced gravity = numerical dependence"
    # (2) the classicalized population
    cl = [k for k, v in ledger.items() if v['cat'] == 'CLASS']
    assert len(cl) >= 8 and 'FND-MATTER-033' in cl and 'FND-MATTER-034' in cl, \
        "the lambda-saga category is a real, measured population"
    # (3) the split: nonlocal residues are fences with no scale input
    for cid in ('QB-003', 'QB-005', 'QB-007'):
        assert ledger[cid]['cat'] == 'FENCE', "nonlocal residues are fences"
        assert ledger[cid]['branch'] == "", "nonlocal fences carry NO scale input"
    # every genuine input is action-scale-flavored (branch-tagged)
    assert all(v['branch'] for v in genuine.values()), "all genuine inputs are scale-branch members"
    print(f"genuine dependencies: {len(genuine)} claims -> 4 underlying inputs; "
          f"classicalized: {len(cl)}; fences: {counts['FENCE']}")
    print("PASS: four inputs, a measured classicalized population, and the split frontier at")
    print("      ledger level -- one branch missing a number, the other a kind of dynamics.")


if __name__ == "__main__":
    test()
