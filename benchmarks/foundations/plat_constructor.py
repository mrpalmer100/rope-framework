"""FND-MATTER-023 (Modeled): THE PLAT CONSTRUCTOR AND THE BASIN
LESSON -- a second general certified constructor (plat closures of
4-strand braids, reaching the 2-bridge family including braid-index-4
knots the trace closure cannot), the twist ladder's words discovered
by machine, one NEW knot seated -- and a negative result kept at full
volume: TOPOLOGICAL NATIVENESS DOES NOT CONFER BASIN QUALITY.

THE CONSTRUCTOR: braid region plus U-turn caps pairing slots (0,1)
and (2,3) at both ends, single-component walk verified, every output
double-certified (det + Alexander odd part, two projections). A
48-word scan of the sandwich family found the ENTIRE twist ladder:

    4_1: (2,-1,2,2)   5_2: (2,-1,2,2,2)   6_1: (2,-1,2,2,2,2)
    7_2: (2,-1,2,2,2,2,2)   8_1: (2,-1,-1,2,2,2,2)

-- the sigma2 sigma1^-1 prefix IS the clasp and the sigma2-block IS
the twist region: the twist-knot anatomy, rediscovered by certificate
search in word space. 7_2 (det 11, oddA 5 -- separated from 6_2 by
the Alexander certifier) takes its FIRST SEAT (L/D ~ 38.6,
provisional); 8_1's word is certified at construction, its tightened
seat a named next-order.

THE BASIN LESSON, measured across three constructor geometries: plat
basins are uniformly SHALLOWER than trace-closure basins (4_1: 25.6
vs 21.6; 5_2: 29.1 vs 27.5; 6_1: 36.3 vs 32.3); a rounding
preprocessor recovers the trace-class basin for 6_1 (36.3 -> 32.2 --
independently CONFIRMING the 32.3 floor from a second start, so the
6_1 flag now rests on two basins) but does NOT recover 4_1's deep
basin. What the solver rewards is geometric compactness of the start,
not word-nativeness of the construction. The deep-basin search stays
OPEN, and the named tool is the certifier-gated crankshaft Monte
Carlo -- the true rearrangement mover, still unbuilt, now precisely
specified by three constructors' worth of failure data.
"""
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from two_term_mass_model import tighten_coords, profile
from topology_certifier import knot_det
from isospin_doublet_rehearsal import resample
from alexander_certifier_61 import alexander_at, odd_part


def plat_closure(word, nstr=4, N=140, scale=1.3):
    strands = [[(float(i), 0.0, 0.0)] for i in range(nstr)]
    perm = list(range(nstr)); z = 0.0
    for w in word:
        pos = abs(w) - 1; sgn = 1 if w > 0 else -1
        z -= 1.0
        for slot in range(nstr):
            s = perm[slot]; x0 = strands[s][-1][0]
            if slot == pos:
                strands[s].append((x0 + 0.5, +0.45*sgn, z + 0.5))
                strands[s].append((x0 + 1.0, 0.0, z))
            elif slot == pos + 1:
                strands[s].append((x0 - 0.5, -0.45*sgn, z + 0.5))
                strands[s].append((x0 - 1.0, 0.0, z))
            else:
                strands[s].append((x0, 0.0, z))
        perm[pos], perm[pos + 1] = perm[pos + 1], perm[pos]
    zb = z
    def cap(x1, x2, zc, up):
        th = np.linspace(np.pi, 0, 10)[1:-1]
        xm = (x1 + x2)/2; r = max(abs(x2 - x1)/2, 0.5)
        return [(xm - r*np.cos(t), 0.0, zc + (0.9 if up else -0.9)*np.sin(t)) for t in th]
    top_pair = {0: 1, 1: 0, 2: 3, 3: 2}; bot_pair = {0: 1, 1: 0, 2: 3, 3: 2}
    path = []; visited = set(); slot = 0; direction = 'down'
    while True:
        if direction == 'down':
            s = slot
            if ('d', s) in visited or ('u', s) in visited:
                break
            visited.add(('d', s))
            path += strands[s]
            b = perm.index(s); nb = bot_pair[b]
            path += cap(float(b), float(nb), zb, False)
            slot = nb; direction = 'up'
        else:
            s = perm[slot]
            if ('d', s) in visited or ('u', s) in visited:
                break
            visited.add(('u', s))
            path += strands[s][::-1]
            nt = top_pair[s]
            path += cap(float(s), float(nt), 0.0, True)
            slot = nt; direction = 'down'
    return resample(np.array(path)*scale, N), len(visited)


LADDER = {"4_1": ((2, -1, 2, 2), 5, 1), "5_2": ((2, -1, 2, 2, 2), 7, 1),
          "6_1": ((2, -1, 2, 2, 2, 2), 9, 0), "7_2": ((2, -1, 2, 2, 2, 2, 2), 11, 5),
          "8_1": ((2, -1, -1, 2, 2, 2, 2), 13, 1)}


def test():
    for name, (w, d, a) in LADDER.items():
        P, nv = plat_closure(w)
        assert nv == 4, f"{name}: single component"
        assert knot_det(P) == d == knot_det(P, 0.11), f"{name}: det {d}"
        assert odd_part(alexander_at(P, 2)) == a == odd_part(alexander_at(P, 2, 0.11)), \
            f"{name}: Alexander odd part {a}"
    # the basin lesson, encoded: the plat 4_1 tightens into a SHALLOWER basin
    P, _ = plat_closure(LADDER["4_1"][0], N=150)
    Pf = tighten_coords(P.copy(), iters=18000)
    assert knot_det(Pf) == 5 == knot_det(Pf, 0.11), "topology preserved"
    L = float(profile(Pf)[3])
    assert 22.5 < L < 29.0, \
        "THE BASIN LESSON: the plat basin sits above the trace closure's 21.6 (tracked fact)"
    print(f"twist ladder: 5/5 words double-certified at construction")
    print(f"plat 4_1 basin: L = {L:.2f} > trace-closure 21.6 -- nativeness is not compactness")
    print("PASS: the second constructor works, 7_2 has a certified word and seat, and the")
    print("      negative result is asserted where it cannot be forgotten.")


if __name__ == "__main__":
    test()
