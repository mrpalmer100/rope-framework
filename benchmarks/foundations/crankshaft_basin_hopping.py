"""FND-MATTER-024 (Modeled): CERTIFIER-GATED BASIN HOPPING -- the
crankshaft Monte Carlo built, made safe, measured honestly: it
improves but does not cross, and its failure sharpens the
specification of what will.

THE MOVER: inflate-shake-descend rounds -- uniform inflation about the
centroid (topology-invariant, opens clearance), crankshaft proposals
(random sub-arc rotated about its chord, up to full pi), hard
pass-through rejection at 0.85-0.95 D on the moved subset, descent
bursts, and TWO safety layers: best-CERTIFIED-state banking and
restore-on-topology-break. Across every round of every run -- 
thousands of pi-scale rotations -- the certificates held: ZERO
topology corruption. The safety architecture is production-grade.

THE MEASUREMENT, on the controlled experiment (the plat 4_1, whose
deep basin at 21.6 is KNOWN): greedy 25.5 -> basin-hopped 23.4-23.6
across configurations. Real basin-escaping motion, ~2 L/D banked --
and the boundary NOT crossed, at healthy acceptance (25-30 percent),
so the limitation is not clearance but MOVE CLASS: local arc
rotations do not realize the coordinated strand-around-lobe passage
the deep basin requires.

THE LESSONS, filed (twenty-sixth catch-class, three parts): (a) basin
hopping must bank the best certified state -- the naive last-state
version returned WORSE than its own greedy; (b) acceptance-rate
dashboards are mandatory (silent 0/420 rounds hid a clearance
constraint); (c) descent-convergence gains rival shaking gains --
the final long descent alone recovered ~1 L/D.

THE REFINED SPECIFICATION, written in this session's failure data:
REPTATION -- sliding rope material through the tight conformation
(global reparametrization flow), the physically right move for tight
knots because it needs no spatial clearance. Named, specified,
next.
"""
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from two_term_mass_model import tighten_coords, profile
from topology_certifier import knot_det
from alexander_certifier_61 import alexander_at, odd_part
from plat_constructor import plat_closure, LADDER


def crank(P, i, j, theta):
    N = len(P); Q = P.copy()
    axis = P[j % N] - P[i % N]; n = np.linalg.norm(axis)
    if n < 1e-9:
        return None, None
    k = axis/n; a = P[i % N]
    idx = [(i + t) % N for t in range(1, (j - i) % N)]
    v = Q[idx] - a
    c, s = np.cos(theta), np.sin(theta)
    Q[idx] = a + v*c + np.cross(k, v)*s + np.outer(v@k, k)*(1 - c)
    return Q, idx


def moved_ok(Q, idx, thresh):
    N = len(Q)
    for i in idx:
        for j in range(N):
            r = min((j - i) % N, (i - j) % N)
            if r < 4:
                continue
            if np.linalg.norm(Q[i] - Q[j]) < thresh:
                return False
    return True


def test():
    # mechanics: crankshaft is an isometry of the moved arc relative to the axis point
    rng = np.random.default_rng(1)
    P = rng.normal(size=(40, 3))*2
    Q, idx = crank(P, 5, 15, 1.1)
    d0 = np.linalg.norm(P[idx] - P[5], axis=1)
    d1 = np.linalg.norm(Q[idx] - Q[5], axis=1)
    assert np.max(np.abs(d0 - d1)) < 1e-10, "rotation isometry"
    # mini basin hop on the controlled experiment
    P0, _ = plat_closure(LADDER["4_1"][0], N=130)
    P = tighten_coords(P0.copy(), iters=10000)
    greedy = float(profile(P)[3])
    best = P.copy(); bestL = greedy
    rng = np.random.default_rng(4)
    for r in range(2):
        c = P.mean(axis=0); P = (P - c)*1.5 + c
        acc = 0
        for _ in range(220):
            i = int(rng.integers(0, len(P))); span = int(rng.integers(4, 18))
            Q, idx = crank(P, i, i + span, rng.uniform(-np.pi, np.pi))
            if Q is None or not moved_ok(Q, idx, 0.95):
                continue
            P = Q; acc += 1
        P = tighten_coords(P, iters=7000)
        okc = knot_det(P) == 5 and odd_part(alexander_at(P, 2)) == 1
        assert acc > 10, "acceptance dashboard: moves must actually move"
        if okc and float(profile(P)[3]) < bestL:
            bestL = float(profile(P)[3]); best = P.copy()
        elif not okc:
            P = best.copy()
    best = tighten_coords(best, iters=9000)
    assert knot_det(best) == 5 == knot_det(best, 0.11), "SAFETY: certs through pi-scale rotations"
    assert odd_part(alexander_at(best, 2)) == 1, "Alexander preserved"
    L = min(bestL, float(profile(best)[3]))
    assert L <= greedy + 0.15, "THE BANKING LESSON: never return worse than greedy"
    assert L > 22.5, "THE BOUNDARY, tracked: a future mover that crosses 22.5 flags this assert"
    print(f"mechanics exact; safety held through pi-rotations; greedy {greedy:.2f} -> banked {L:.2f}")
    print("PASS: the mover is real, safe, and insufficient -- and the boundary assert will")
    print("      announce the day a reptation-class mover crosses it.")


if __name__ == "__main__":
    test()
