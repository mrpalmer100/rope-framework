"""FND-STRAND-024 (Modeled): THE SPLIT PACKET -- a split quantum clicks
NOTHING, closing one-click exclusivity trivially at the classical level and
converting it into the corpus's sharpest measured LIMIT: the funneling step
(reassembly of a split quantum's energy at one absorption site, the 50/50
single-arm clicking of real photons) is NOT performed by any classical
local dynamics in this engine.

Bars (analysis/STRAND024_split_packet_bars_LOCKED.md); results with the
logged deviation, the letter-fail/purpose-pass alibi, and the sixth lesson
plus the two-stage-gate rule (analysis/STRAND024_split_packet_results.md);
data archived (analysis/STRAND024_split_packet_data.json).

Pins: the threshold sigmoid (0/24, 3/24, 15/24, 24/24 at V = 0.9..2.1);
the headline nulls (half-packet 0/48; one-quantum split 0/64 either lobe);
the interaction ensemble consistent with independence (rho ~ 0.7, wide CI,
no branch verdict); the two-full alibi at the independence rate from
realized marginals.
"""
import json
import os

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, '..', '..', 'analysis',
                    'STRAND024_split_packet_data.json')


def _pool(d, mode):
    A = B = dbl = S = 0
    for v in d.get(mode, {}).items():
        pass
    for v in d.get(mode, {}).values():
        A += v['A']; B += v['B']; dbl += v['double']; S += v['S']
    return A, B, dbl, S


def test():
    d = json.load(open(DATA))
    sig = {0.9: 0, 1.2: 3, 1.6: 15, 2.1: 24}
    for k, v in d['fullcal'].items():
        V = float(k.split('_')[0])
        assert v['A'] == sig[V], f"sigmoid pinned at V={V}"
    A, B, dbl, S = _pool(d, 'single')
    assert S == 48 and A + B == 0, "half-packet single lobe: 0/48"
    A, B, dbl, S = _pool(d, 'split_1q')
    assert S == 64 and A + B + dbl == 0, "one-quantum split: 0/64 either lobe"
    A, B, dbl, S = _pool(d, 'split_int')
    pA, pB = A/S, B/S
    rho = (dbl/S)/(pA*pB)
    assert S == 128 and dbl == 2, (S, dbl)
    assert 0.3 < rho < 1.5, f"interaction consistent with independence, got {rho:.2f}"
    A2, B2, d2, S2 = _pool(d, 'twofull')
    ind = (A2/S2)*(B2/S2)
    assert S2 == 64 and abs(d2/S2 - ind) < 0.06, \
        "two-full doubles at the independence rate from realized marginals"
    print(f"sigmoid: 0/24 3/24 15/24 24/24 -- threshold certified; V50 = 1.50")
    print(f"HEADLINE: half-packet 0/48; one-quantum split 0/64 either lobe")
    print(f"interaction: rho = {rho:.2f} (wide CI) -- consistent with independence")
    print(f"two-full: doubles {d2}/{S2} vs independence {ind:.3f} -- purpose pass")
    print("PASS: exclusivity closed trivially at the classical level; the")
    print("      funneling step registered as the measured classicality limit --")
    print("      where genuine quantumness must enter the detection story.")


if __name__ == "__main__":
    test()
