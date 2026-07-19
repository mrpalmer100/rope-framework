"""NUC-008 (Modeled; partial, misses registered with a cross-sector diagnosis):
STATE-LABELED capacity -- the NUC-007 next-order executed blind. Each nucleon
carries one of four spin-isospin labels; a strong bond requires UNLIKE labels
with at most one strong bond per partner-label (mode orthogonality); labels
are chosen by energy maximization (seeded hill-climb, verified against
exhaustive search at A = 8).

WHAT PASSES:
(B1) Be-8 RECOVERED -- the primary target: B/A local maximum at A = 8
     (7.516 vs 7.074 at A = 7 and 9). The second tetrahedron completes its six
     strong bonds because its four members carry all four labels, exactly as
     the NUC-007 diagnosis predicted. QUALIFICATION: recovered as an
     alpha-structured local maximum in B/A, NOT as a stable bound nucleus --
     physical Be-8 is slightly unbound (~92 keV above two alphas), far below
     this model's resolution.
(B4) The A = 4 peak and A = 5 dip survive.
(B6) BONUS, derived WITHIN the adopted capacity rule (the rule is a model
     postulate, not yet derived from rope dynamics): the SEMF SYMMETRY-ENERGY SIGN. At fixed geometry,
     balanced label populations strictly beat asymmetric ones
     (2,2,2,2) > (3,3,1,1) > (4,4,0,0) -- unlike-label bonding makes N = Z
     energetically preferred. Direction derived; coefficient not claimed.
(+)  Model-data correlation improves over the state-blind model:
     r = 0.978 vs 0.954.
(B3) A = 16 > A = 15 passes but is flagged WEAK EVIDENCE: it rides a rising
     baseline rather than demonstrating alpha structure.

THE REGISTERED MISSES, one diagnosis:
(B2, B5) A = 12 is not a local maximum and A = 13-16 overbind on a
     monotonically rising baseline toward an overdeep bulk (~12.4 MeV vs the
     real ~8.8 saturation). DIAGNOSIS, CONVERGING ACROSS SECTORS: a classical
     bond-counting model has NO KINETIC-ENERGY COST for compactness -- the
     same zero-point/Fermi omission already registered for the light-isotope
     residuals (NUC-005/006 caveats) reappears here as the rising baseline on
     which the alpha ripple rides. Secondary suspect at A = 12: max-compact
     fcc filling may not represent C-12's known alpha-triangle cluster
     geometry. NAMED NEXT-ORDER: a mode-kinetic (zero-point) penalty term --
     the classical corpus's single most repeated missing ingredient, now
     located in three places at once.
"""
import numpy as np
from itertools import product, permutations

_pts = sorted(((i, j, k) for i, j, k in product(range(-4, 5), repeat=3)
               if (i + j + k) % 2 == 0),
              key=lambda p: (p[0]**2 + p[1]**2 + p[2]**2, p))
_pts = [np.array(p, float) for p in _pts]
NN = 1.5


def compact_fill(A):
    cl = [_pts[0]]
    while len(cl) < A:
        best, bk = None, None
        for s in _pts[1:200]:
            if any(np.array_equal(s, c) for c in cl):
                continue
            k = sum(1 for c in cl if np.linalg.norm(s - c) < NN)
            key = (-k, s @ s, tuple(s))
            if bk is None or key < bk:
                bk, best = key, s
        cl.append(best)
    return cl


def edges(A):
    C = compact_fill(A)
    return [(i, j) for i in range(A) for j in range(i + 1, A)
            if np.linalg.norm(C[i] - C[j]) < NN]


def score(labels, E, lam):
    used = [set() for _ in range(len(labels))]
    s = r = 0
    for i, j in E:
        li, lj = labels[i], labels[j]
        if li != lj and lj not in used[i] and li not in used[j]:
            s += 1; used[i].add(lj); used[j].add(li)
        else:
            r += 1
    return s + lam*r


def optimize(A, lam, seed=5, restarts=6, iters=400):
    E = edges(A); rng = np.random.default_rng(seed)
    best = -1.0
    for R in range(restarts):
        lab = [k % 4 for k in range(A)]
        if R > 0:
            rng.shuffle(lab)
        cur = score(lab, E, lam)
        for _ in range(iters):
            i, j = rng.integers(0, A, 2)
            if lab[i] == lab[j]:
                continue
            lab[i], lab[j] = lab[j], lab[i]
            new = score(lab, E, lam)
            if new >= cur:
                cur = new
            else:
                lab[i], lab[j] = lab[j], lab[i]
        best = max(best, cur)
    return best


def test():
    lam = 0.25
    e_b = 28.296/6
    # optimizer sanity: hill-climb matches exhaustive at A=8
    E8 = edges(8)
    base = [k % 4 for k in range(8)]
    ex = max(score(list(p), E8, lam) for p in set(permutations(base)))
    hc = optimize(8, lam)
    assert abs(ex - hc) < 1e-9, "hill-climb reaches the exhaustive optimum at A=8"
    data = {2:1.112,3:2.827,4:7.074,5:5.481,6:5.332,7:5.606,8:7.062,9:6.463,
            10:6.475,11:6.928,12:7.680,13:7.470,14:7.476,15:7.699,16:7.976}
    m = {A: e_b*optimize(A, lam)/A for A in range(2, 17)}
    # B4 survives
    assert m[4] > max(m[3], m[5], m[6]) and m[5] < m[4], "alpha peak + A=5 dip survive labeling"
    # B1: the primary target
    assert m[8] > m[7] and m[8] > m[9], "Be-8 RECOVERED: local max at A=8 (the NUC-007 diagnosis confirmed)"
    # correlation improvement over state-blind
    arr_m = np.array([m[A] for A in range(2, 17)])
    arr_d = np.array([data[A] for A in range(2, 17)])
    r = np.corrcoef(arr_m, arr_d)[0, 1]
    assert r > 0.97, "state labels improve the one-constant model (r = 0.978 vs 0.954)"
    # B3 passes but is weak evidence (rising baseline) -- asserted with that reading
    assert m[16] > m[15], "A=16 > 15 (flagged: rides the rising baseline; weak evidence for alpha structure)"
    # B6: symmetry-energy sign
    def best_pops(pops):
        b = sum([[k]*n for k, n in enumerate(pops)], [])
        return max(score(list(p), E8, lam) for p in set(permutations(b)))
    s_sym, s_a1, s_a2 = best_pops([2,2,2,2]), best_pops([3,3,1,1]), best_pops([4,4,0,0])
    assert s_sym > s_a1 > s_a2, "SYMMETRY-ENERGY SIGN DERIVED: balanced populations strictly preferred"
    # B2/B5: THE REGISTERED MISSES (asserted so they cannot be forgotten)
    assert not (m[12] > m[11] and m[12] > m[13]), \
        "MISS (registered): A=12 not a local max -- rising baseline (no kinetic cost) + geometry suspect"
    assert m[13] > m[12], "MISS (registered): 13-16 overbind on the kinetic-free rising baseline"
    print(f"B1 Be-8 RECOVERED: {m[8]:.3f} > {m[7]:.3f}, {m[9]:.3f}  (the state-labeling prediction confirmed)")
    print(f"B4 peak/dip survive: {m[4]:.2f} peak, {m[5]:.2f} dip")
    print(f"B6 SYMMETRY SIGN: {e_b*s_sym/8:.2f} > {e_b*s_a1/8:.2f} > {e_b*s_a2/8:.2f} (N=Z preferred, derived)")
    print(f"correlation r = {r:.3f} (state-blind was 0.954)")
    print(f"MISSES registered: A=12 periodicity; 13-16 rising baseline -- diagnosis: no kinetic/zero-point")
    print(f"cost in a classical bond count; the SAME omission named in NUC-005/006 light-isotope residuals.")
    print("PASS: primary target recovered; symmetry sign derived; remaining misses share one named cause.")


if __name__ == "__main__":
    test()
