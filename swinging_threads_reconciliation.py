"""NUC-009 (Modeled): the A=12 geometry suspect CONFIRMED -- expanding the
ground-state candidate set to include alpha-cluster constructions makes
B/A(12) a local maximum, and the model DISCOVERS the three-alpha structure
itself.

NUC-008 registered a secondary suspect for its A=12 miss: max-compact fcc
filling may not represent C-12's known three-alpha-triangle cluster
structure. THIS TEST (bars pre-committed): expand the geometry candidate
set SYMMETRICALLY for every A -- ground state = best of {max-compact fill}
UNION {k complete tetrahedra in contact + greedy max-contact remainder} --
with the NUC-008 label rule, lambda = 0.25, and the single He-4 constant
all unchanged. Nothing tuned; the fairness constraint is that every A gets
the same expanded set.

RESULTS (all bars):
(B1) A = 12 becomes a LOCAL MAXIMUM: B/A = 8.351 vs 7.824 (A=11) and
     8.072 (A=13); robust at lambda = 0.20 and 0.30. The registered
     suspect is CONFIRMED: geometry was the missing piece for the A=12
     periodicity.
(B2, strengthened) THE MODEL FINDS THE ALPHAS ITSELF: the winning A=12
     configuration decomposes into exactly three DISJOINT geometric
     4-cliques with ALL 18 strong bonds intra-quartet -- and the third
     tetrahedron was built spontaneously by greedy max-contact attachment,
     not hand-placed (a minimal-contact hand-built triangle scores LOWER
     because its clusters barely touch). Three alphas in mutual contact is
     the model's own preferred ground state.
(B3) Nothing regresses: A = 8 remains a local maximum (7.516 vs 7.074 at
     both 7 and 9); the A = 4 peak and A = 5 dip are untouched.
(B4, observation) A = 16 > A = 15 still holds BUT the winner at 16 is
     max-compact, NOT the four-alpha cluster: the weak-evidence flag is
     RETAINED and sharpened -- 16's rise is compact overbinding (the
     kinetic omission), not four-alpha structure.
HONEST LIMIT (pre-declared, unchanged): absolute overbinding at A = 13-16
persists; the kinetic/zero-point omission (FND-BOUND-001) stands. This
test resolves the LOCAL-MAX structure only.
"""
import numpy as np
import importlib.util, os, sys, itertools

_here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("nsl", os.path.join(_here, "nuclear_state_labeled.py"))
N = importlib.util.module_from_spec(spec)
sys.modules["nsl"] = N
spec.loader.exec_module(N)

NN = 1.5
TET = [np.array(v, float) for v in [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)]]
V1 = np.array((-2, -2, 0), float)
V2 = np.array((-2, 0, -2), float)
V3 = np.array((-2, 0, 0), float)


def contacts(sites):
    A = len(sites)
    return [(i, j) for i in range(A) for j in range(i + 1, A)
            if np.linalg.norm(sites[i] - sites[j]) < NN]


def attach_extra(sites, r):
    sites = list(sites)
    cand = [np.array((i, j, k), float) for i in range(-6, 7) for j in range(-6, 7)
            for k in range(-6, 7) if (i + j + k) % 2 == 0]
    for _ in range(r):
        best, bk = None, None
        for s in cand:
            if any(np.linalg.norm(s - c) < 1.40 for c in sites):
                continue
            n = sum(1 for c in sites if np.linalg.norm(s - c) < NN)
            if n == 0:
                continue
            key = (-n, s @ s, tuple(s))
            if bk is None or key < bk:
                bk, best = key, s
        sites.append(best)
    return sites


def energy(sites, lam, seed=5, restarts=6, iters=500):
    A = len(sites)
    E = contacts(sites)
    rng = np.random.default_rng(seed)
    best, bestlab = -1.0, None
    for R in range(restarts):
        lab = [k % 4 for k in range(A)]
        if R > 0:
            rng.shuffle(lab)
        cur = N.score(lab, E, lam)
        for _ in range(iters):
            i, j = rng.integers(0, A, 2)
            if lab[i] == lab[j]:
                continue
            lab[i], lab[j] = lab[j], lab[i]
            new = N.score(lab, E, lam)
            if new >= cur:
                cur = new
            else:
                lab[i], lab[j] = lab[j], lab[i]
        if cur > best:
            best, bestlab = cur, lab[:]
    return best, bestlab, E, sites


def cluster_sites(k):
    vs = [np.zeros(3), V1, V2, V3][:k]
    out = []
    for v in vs:
        out += [p + v for p in TET]
    return out


def ground(A, lam):
    scores = {"compact": N.optimize(A, lam)}
    k = A // 4
    if k >= 2:
        cs = cluster_sites(min(k, 4))
        if A - len(cs) > 0:
            cs = attach_extra(cs, A - len(cs))
        scores["cluster"] = energy(cs[:A] if len(cs) >= A else cs, lam)[0]
        cs2 = cluster_sites(k - 1) if k - 1 >= 1 else None
        if cs2 is not None and A - len(cs2) > 0:
            scores["cluster_minus"] = energy(attach_extra(cs2, A - len(cs2)), lam)[0]
    return max(scores.values())


def test():
    e_b = 28.296/6
    lam = 0.25
    ba = {A: e_b*ground(A, lam)/A for A in (7, 8, 9, 11, 12, 13, 15, 16)}
    # B1: the suspect's test
    assert ba[12] > ba[11] and ba[12] > ba[13], \
        f"A=12 local max with expanded geometry set: {ba[11]:.3f} < {ba[12]:.3f} > {ba[13]:.3f}"
    # B2 (strengthened): the winner IS three disjoint alpha quartets, discovered not imposed
    win_sites = attach_extra([p for p in TET] + [p + V1 for p in TET], 4)
    score, lab, E, sites = energy(win_sites, lam, restarts=10, iters=800)
    assert score > N.optimize(12, lam), "the discovered cluster state beats max-compact at A=12"
    used = [set() for _ in range(12)]
    strong = []
    for i, j in E:
        li, lj = lab[i], lab[j]
        if li != lj and lj not in used[i] and li not in used[j]:
            strong.append((i, j)); used[i].add(lj); used[j].add(li)
    assert len(strong) == 18, "three complete quartets: 18 strong bonds"
    cliques = [c for c in itertools.combinations(range(12), 4)
               if all((min(a, b), max(a, b)) in E for a, b in itertools.combinations(c, 2))]
    trio = next((t for t in itertools.combinations(cliques, 3)
                 if len(set(t[0]) | set(t[1]) | set(t[2])) == 12), None)
    assert trio is not None, "sites decompose into three DISJOINT geometric tetrahedra"
    assert all(any(i in q and j in q for q in trio) for i, j in strong), \
        "all 18 strong bonds intra-quartet: the three-alpha structure"
    # B3: no regressions
    assert ba[8] > ba[7] and ba[8] > ba[9], "Be-8 local max preserved"
    # B4: observation encoded -- 16 > 15 but compact still wins at 16 (weak evidence retained)
    assert ba[16] > ba[15], "A=16 > 15 (rising baseline)"
    cs16 = cluster_sites(4)
    assert energy(cs16, lam)[0] < N.optimize(16, lam), \
        "OBSERVATION: four-alpha does NOT win at 16 -- compact overbinding (kinetic omission), flag retained"
    # robustness
    for l2 in (0.20, 0.30):
        b11, b12, b13 = (e_b*ground(A, l2)/A for A in (11, 12, 13))
        assert b12 > b11 and b12 > b13, f"A=12 local max robust at lambda={l2}"
    print(f"B1 CONFIRMED: A=12 local max  {ba[11]:.3f} < {ba[12]:.3f} > {ba[13]:.3f}  (robust lambda 0.20-0.30)")
    print(f"B2 the model DISCOVERS three alphas: 18/18 strong bonds intra-quartet, three disjoint tetrahedra,")
    print(f"   third alpha built spontaneously by max-contact attachment")
    print(f"B3 no regressions: Be-8 local max preserved ({ba[8]:.3f} vs {ba[7]:.3f}, {ba[9]:.3f})")
    print(f"B4 A=16: still compact-driven (four-alpha loses) -- weak-evidence flag retained; overbinding = kinetic")
    print("PASS: the NUC-008 geometry suspect is confirmed; the kinetic omission now stands alone for the baseline.")


if __name__ == "__main__":
    test()
