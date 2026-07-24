"""QB-015 (Modeled): THE SHARED-RIBBON SINGLET -- Mark's conjecture:
entanglement as two knots on ONE ribbon. The model reproduces BOTH the
registered wall and the quantum correlations exactly, with the entire
difference isolated to a single mechanical premise: whether the
bookkeeping honors the ribbon being one object.

THE MODEL: the singlet is one shared ribbon with zero total twist --
the frames at its two ends anti-rigid (n at A, -n at B), n uniform.
Each end detects via QB-005's energy-partition Born response at the
belt-trick half-angle: P(+|setting s, frame f) = cos^2(angle(s,f)/2).

MODE 1 -- SEVERED BOOKKEEPING (the ends treated as independent
responders, exactly the structure of every model in QB-013's class):
    E(a,b) = -(a.b)/3,  CHSH = 2 sqrt(2)/3 = 0.9428
LANDING EXACTLY ON THE REGISTERED WALL. The wall is thereby EXPLAINED:
the measured B = -1/3 pinning is the signature of severed-strand
accounting -- of treating one object as two.

MODE 2 -- THE REEL (the one named new premise): measurement at A
projects the shared frame onto +/-a; the ribbon being ONE object, the
B end is thereby reoriented to the anti-rigid -(outcome)a. Then:
    E(a,b) = -a.b exactly,  CHSH = 2 sqrt(2) = Tsirelson
and NO-SIGNALING holds identically: B's marginal is 1/2 for every a
(the reel carries bookkeeping, not signal).

HONESTY AT FULL VOLUME: Bell's theorem is NOT evaded -- the reel IS
the nonlocal element, named as such; what the ribbon supplies is an
ONTOLOGY for it (the 'spooky action' as ordinary rigidity of a shared
topological object, GRV-045's conserved frame currency). The
half-angle response is IMPORTED (motivated by QB-005's energy
partition and the belt-trick), not derived from counting -- QB-002's
(pi-theta)/pi counting gap stands exactly where it stood. Status
Modeled; the wall (QB-013) stands as the now-EXPLAINED theorem about
reel-free models.

(Fourteenth instrument catch, logged: the first CHSH harness used a
sign combination that cancels for this geometry -- caught by internal
inconsistency, exact E-curves cannot give zero CHSH.)
"""
import numpy as np


def born_p(c): return 0.5*(1 + c)


def E_mode1(a, b, n, rng):
    pA = born_p(n@a); pB = born_p(-(n@b))
    A = np.where(rng.random(len(n)) < pA, 1, -1)
    B = np.where(rng.random(len(n)) < pB, 1, -1)
    return np.mean(A*B), np.mean(B)


def E_mode2(a, b, n, rng):
    pA = born_p(n@a)
    A = np.where(rng.random(len(n)) < pA, 1, -1)
    frameB = -(A[:, None])*a[None, :]
    B = np.where(rng.random(len(n)) < born_p(frameB@b), 1, -1)
    return np.mean(A*B), np.mean(B)


def chsh(Ef, n, rng):
    a = np.array([0, 0, 1.0]); ap = np.array([1.0, 0, 0])
    b = np.array([np.sin(np.pi/4), 0, np.cos(np.pi/4)])
    bp = np.array([np.sin(3*np.pi/4), 0, np.cos(3*np.pi/4)])
    E = lambda x, y: Ef(x, y, n, rng)[0]
    vals = [E(a, b), E(a, bp), E(ap, b), E(ap, bp)]
    best = 0.0
    for s in ((1,1,1,-1),(1,1,-1,1),(1,-1,1,1),(-1,1,1,1)):
        best = max(best, abs(sum(si*vi for si, vi in zip(s, vals))))
    return best


def test():
    rng = np.random.default_rng(7)
    v = rng.normal(size=(400000, 3)); n = v/np.linalg.norm(v, axis=1, keepdims=True)
    for th in (0.0, np.pi/3, np.pi/2, 2*np.pi/3, np.pi):
        a = np.array([0, 0, 1.0]); b = np.array([np.sin(th), 0, np.cos(th)])
        e1, m1 = E_mode1(a, b, n, rng)
        e2, m2 = E_mode2(a, b, n, rng)
        assert abs(e1 - (-np.cos(th)/3)) < 0.01, "mode 1: E = -(a.b)/3 (the wall's law)"
        assert abs(e2 - (-np.cos(th))) < 0.01, "mode 2: E = -a.b (the quantum law)"
        assert abs(m1) < 0.01 and abs(m2) < 0.01, "no-signaling: flat marginals, both modes"
    S1 = chsh(E_mode1, n, rng); S2 = chsh(E_mode2, n, rng)
    assert abs(S1 - 2*np.sqrt(2)/3) < 0.02, "mode 1 CHSH = 0.9428: EXACTLY the registered wall"
    assert abs(S2 - 2*np.sqrt(2)) < 0.02, "mode 2 CHSH = Tsirelson"
    print(f"mode 1 (severed): CHSH = {S1:.4f}  [wall: {2*np.sqrt(2)/3:.4f}]")
    print(f"mode 2 (reel):    CHSH = {S2:.4f}  [Tsirelson: {2*np.sqrt(2):.4f}]")
    print("PASS: one ribbon, two bookkeepings -- the wall explained (severed accounting) and")
    print("      the quantum law reached (the reel), no-signaling exact in both; Bell honored,")
    print("      the nonlocality given an ontology: the rigidity of one shared object.")


if __name__ == "__main__":
    test()
