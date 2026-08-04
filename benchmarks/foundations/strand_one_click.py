"""FND-STRAND-022 (Modeled): ONE QUANTUM, ONE CLICK -- NO-VERDICT on the
exclusivity bars (the calibration missed its bracket and the pre-committed
alibi clause caught the FIRE observable measuring transient overshoots),
plus one registrable finding: CONCENTRATION, NOT ENERGY, IS THE CLICK'S
BOTTLENECK -- a delocalized coherent excitation produced 1 genuine
nucleation in 240 runs at injected energies up to ~twelve kink-pair costs,
cold, while the same engine nucleates readily at thermal temperature.

Bars (analysis/STRAND022_one_click_bars_LOCKED.md); results with the
audit table and two new standing-rule lessons (calibration-bracket
pricing; persistence-defined thresholds with paired instruments)
(analysis/STRAND022_one_click_results.md); data archived
(analysis/STRAND022_one_click_data.json). The redesign (thermal-point
coincidence design, concentration-scarcity hypothesis barred) is named.

This benchmark refits the archived record and pins: the silent control,
the committed-grid null, the transient-vs-genuine audit at the extension
points, and the single genuine nucleation.
"""
import json
import os

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, '..', '..', 'analysis',
                    'STRAND022_one_click_data.json')


def test():
    d = json.load(open(DATA))
    c = d['control']['0.0_170']
    assert c['fired'] == 0 and c['S'] == 48, "B0: cold point silent"
    cal = d['cal']
    committed = ['0.1', '0.14', '0.18', '0.22', '0.26', '0.3', '0.36']
    for a in committed:
        (k, v), = [(k, v) for k, v in cal.items() if k.split('_')[0] == a]
        assert v['fired'] == 0, f"committed grid null at A={a}"
    tot_runs = sum(v['S'] for v in cal.values())
    tot_fire = sum(v['fired'] for v in cal.values())
    tot_nuc = sum(sum(1 for x in v['nev'] if x >= 1) for v in cal.values())
    assert tot_runs == 240 and tot_fire == 23 and tot_nuc == 1, \
        (tot_runs, tot_fire, tot_nuc)
    v10 = [v for k, v in cal.items() if k.split('_')[0] == '1.0'][0]
    nuc10 = sum(1 for x in v10['nev'] if x >= 1)
    assert v10['fired'] >= 20 and nuc10 <= 1, \
        "the audit: barred fires are transient overshoots, not clicks"
    print(f"B0: 0/48 thermal fires. Committed grid: 0 fires to E = 3.1.")
    print(f"Audit: {tot_fire} barred fires across 240 runs; genuine nucleations: {tot_nuc}.")
    print(f"At E = 24 (~12 pair costs): {v10['fired']}/24 transient crossings, {nuc10} click.")
    print("PASS (the record IS the result): NO-VERDICT on exclusivity by the")
    print("      pre-committed audit; the registrable finding stands --")
    print("      concentration, not energy, is the click's bottleneck.")


if __name__ == "__main__":
    test()
