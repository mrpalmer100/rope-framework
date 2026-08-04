"""FND-STRAND-023 (Modeled): EXCLUSIVITY AT THE THERMAL POINT -- the priced
grid was null, the stop-clause was honored, and the null's arithmetic
retro-diagnoses both stopped sessions: the delocalized-global-mode
idealization of "one photon" dilutes as 1/N and was SUB-THERMAL per site
at every committed energy. The click channel is fed by LOCAL energy
density; the corrected redesign (split localized packet, intensive-priced)
is fully specified.

Bars (analysis/STRAND023_thermal_exclusivity_bars_LOCKED.md); results with
the dilution arithmetic and the refined (fifth) pricing lesson
(analysis/STRAND023_thermal_exclusivity_results.md); data archived
(analysis/STRAND023_thermal_data.json).

This benchmark pins: the silent baseline (0/48), the priced-grid null
(0/120), and the dilution arithmetic (per-site injected KE < T/2 at every
committed point).
"""
import json
import os

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, '..', '..', 'analysis',
                    'STRAND023_thermal_data.json')


def test():
    d = json.load(open(DATA))
    b = d['base']['0.0_0.3_190']
    assert b['fire'] == 0 and b['S'] == 48, "B0: thermal baseline silent"
    N, T = 96, 0.40
    tot = 0
    for k, v in d['cal'].items():
        assert v['fire'] == 0, f"priced grid null at {k}"
        tot += v['S']
        A = float(k.split('_')[0])
        per_site = A*A/4
        assert per_site < T/2, \
            "dilution: every committed point sub-thermal per site"
        assert abs(v['Einj'] - A*A*N/4) < 0.05
    assert tot == 120, tot
    print("B0: 0/48 baseline. Priced grid: 0/120 across E = 1..16.")
    print("Dilution pinned: per-site injected KE = A^2/4 < T/2 = 0.20 at every")
    print("committed energy (5%..83% of thermal).")
    print("PASS (the record IS the result): stop-clause honored; the")
    print("      delocalized-mode idealization, not the physics, guaranteed the")
    print("      null; local density feeds the click; the split-packet redesign")
    print("      is specified with intensive pricing.")


if __name__ == "__main__":
    test()
