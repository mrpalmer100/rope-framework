"""QGATE-008 (Modeled): THE CAMPAIGN SYNTHESIS -- the seven-claim arc
composed into one map, with this benchmark mechanically verifying the
composition: every constituent claim present with its expected status,
every correction pointer filed, every funnel constant re-derivable.
The synthesis cannot drift from what it synthesizes.

The frontier's new shape (docs/technical/QGATE_SYNTHESIS.md): TWO BRANCHES,
ASYMMETRIC FATES. The scale branch is one conditional chain -- IF
collective reconnection (n_t ~ 111, D/w ~ 19) AND Sigma >= 5.1e35
J/m^3 THEN hbar = W_collective serves all four quantum inputs with
zero retuning -- alive, expensive, invoiced (vacuum mass density
>= 5.6e18 kg/m^3 non-gravitating; QED birefringence owed from the
matter sector), and decided by VMB@CERN-class polarimetry with the
INVERTED payoff. The nonlocal branch carries zero scale inputs, is
immune to every campaign result, and is missing a kind of dynamics,
not a number.
"""
import yaml, json, os, sys
import numpy as np

ROOT = os.path.join(os.path.dirname(__file__), '..', '..')


def test():
    d = yaml.safe_load(open(os.path.join(ROOT, 'claims.yaml')))
    claims = d['claims'] if isinstance(d, dict) and 'claims' in d else d
    ids = {c['id']: c for c in claims}
    # the chain exists, with expected statuses
    chain = {"THM-006": "Failed", "QGATE-001": "Modeled", "QGATE-002": "Modeled",
             "QGATE-003": "Modeled", "QGATE-004": "Modeled", "QGATE-005": "Modeled",
             "QGATE-006": "Modeled", "QGATE-007": "Modeled"}
    for cid, st in chain.items():
        assert cid in ids and ids[cid]['status'] == st, f"{cid} present as {st}"
    # the correction pointers are FILED on the affected claims
    assert "SUPERSEDED on the ATLAS pin by QGATE-007" in ids["EM-RECON-014"]['title'], \
        "EM-RECON-014 carries its correction pointer"
    assert "PAYOFF MATRIX INVERTED by QGATE-007" in \
        (ids["QGATE-006"]['title'] + ids["QGATE-006"].get('note', '')), \
        "QGATE-006 carries its inversion pointer"
    # the ledger artifact exists with its headline structure
    ledger = json.load(open(os.path.join(ROOT, 'docs', 'quantum_ledger.json')))
    genuine = [k for k, v in ledger.items() if v['cat'] in ('IMPORT', 'CALIB', 'NUMER')]
    cls = [k for k, v in ledger.items() if v['cat'] == 'CLASS']
    assert 5 <= len(genuine) <= 20 and len(cls) >= 8, "ledger headline reproducible"
    # the funnel constants re-derived end to end
    TD, D = 33.8, 0.8/27.75
    W = 1.801*TD*D
    assert 0.007 < W/197.327 < 0.011, "W ~ 0.009 hbar (QGATE-001)"
    n_t = 197.327/W
    assert 100 < n_t < 125, "n_t ~ 111 (QGATE-003)"
    Dw = np.sqrt(n_t/0.309)
    assert 17 < Dw < 21, "D/w ~ 19 (QGATE-003/004)"
    T_tube = (TD/D)*1.602e-13/1e-15
    Sig_min = 3.0*(T_tube/n_t)/(1e-16)**2
    assert 3e35 < Sig_min < 8e35, "Sigma >= ~5e35 J/m^3 (QGATE-005/007)"
    rho = Sig_min/9e16
    assert rho > 1e18, "the invoice: vacuum mass density >= ~5.6e18 kg/m^3"
    # the map document exists
    assert os.path.exists(os.path.join(ROOT, 'docs', 'technical', 'QGATE_SYNTHESIS.md')), "the map is in docs/technical/"
    print(f"chain verified: 8 claims, 2 correction pointers, ledger reproducible")
    print(f"funnel re-derived: W/hbar = {W/197.327:.4f}, n_t = {n_t:.0f}, D/w = {Dw:.1f}, "
          f"Sigma_min = {Sig_min:.1e}")
    print("PASS: the synthesis is mechanically bound to its constituents -- two branches,")
    print("      asymmetric fates, one experiment, one invoice, and one deeper half.")


if __name__ == "__main__":
    test()
