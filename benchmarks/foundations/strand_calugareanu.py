"""FND-STRAND-003 (Modeled): THE CALUGAREANU LEDGER ON LITERAL STRANDS,
AND SUPERCOILING -- Phase 2b: the strand does what no lattice could.

(B1) THE LEDGER AS A DYNAMICAL IDENTITY: a closed strand initialized with
     Lk = 3 entirely in twist (Wr = 0) is morphed through a strongly
     chiral deformation while its material frames are parallel-transported
     step by step. Twist is measured FROM THE FRAMES and writhe FROM THE
     GAUSS SELF-INTEGRAL -- two independent computations, neither told
     about the other -- and their sum stays 3 to < 5e-3 while the writhe
     swings to order 0.5: geometry visibly absorbs twist, the ledger
     never blinks. Link = Twist + Writhe holds dynamically on the engine.
(B2) SUPERCOILING: along a chiral buckling family off the flat twisted
     circle, the total energy (bend + twist-via-the-reduction
     2 pi^2 kt (Lk - Wr)^2 / L) has its minimum AT the circle for small
     twist stiffness and OFF the circle for large -- the plectonemic
     instability: above threshold, the strand buys writhe with bend to
     shed twist. The threshold is bracketed and scales as the classical
     Michell picture requires (larger kt/kb -> buckled).
"""
import numpy as np


def tangents(X):
    d = np.roll(X, -1, 0) - X
    return d/np.linalg.norm(d, axis=1, keepdims=True)


def writhe(X):
    N = len(X)
    t = tangents(X); m = 0.5*(X + np.roll(X, -1, 0))
    seg = np.linalg.norm(np.roll(X, -1, 0) - X, axis=1)
    R = m[:, None, :] - m[None, :, :]
    r = np.linalg.norm(R, axis=2) + 1e-12
    cr = np.cross(t[:, None, :], t[None, :, :])
    integ = np.sum(cr*R, axis=2)/r**3*(seg[:, None]*seg[None, :])
    idx = np.arange(N)
    for off in (-1, 0, 1):
        integ[idx, (idx + off) % N] = 0
    return np.sum(integ)/(4*np.pi)


def rot_between(a, b):
    v = np.cross(a, b); s = np.linalg.norm(v); c = a@b
    if s < 1e-12:
        return np.eye(3)
    vx = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    return np.eye(3) + vx + vx@vx*((1 - c)/s**2)


def twist_from_frames(X, U):
    N = len(X); t = tangents(X); tot = 0.0
    for i in range(N):
        j = (i + 1) % N
        ut = rot_between(t[i], t[j])@U[i]
        ut -= (ut@t[j])*t[j]; ut /= np.linalg.norm(ut)
        u2 = U[j] - (U[j]@t[j])*t[j]; u2 /= np.linalg.norm(u2)
        tot += np.arctan2(np.cross(ut, u2)@t[j], ut@u2)
    return tot/(2*np.pi)


def shape(th, a):
    return np.stack([(1 + 0.5*a*np.cos(2*th))*np.cos(th),
                     (1 + 0.5*a*np.cos(2*th))*np.sin(th),
                     0.6*a*np.sin(2*th)], 1)


def bend_energy(X):
    lap = np.roll(X, -1, 0) - 2*X + np.roll(X, 1, 0)
    return 0.5*np.sum(lap**2)


def test():
    N = 96
    th = np.linspace(0, 2*np.pi, N, endpoint=False)
    X = shape(th, 0.0)
    t0 = tangents(X)
    U = np.zeros((N, 3))
    for i in range(N):
        e = np.array([0, 0, 1.0]); e -= (e@t0[i])*t0[i]; e /= np.linalg.norm(e)
        ang = 3*2*np.pi*i/N
        U[i] = np.cos(ang)*e + np.sin(ang)*np.cross(t0[i], e)
    assert abs(twist_from_frames(X, U) - 3) < 1e-6 and abs(writhe(X)) < 1e-6
    # B1: strong chiral morph, ledger tracked
    devs = []; Wrs = []
    steps = 240
    for s in range(1, steps + 1):
        told = tangents(X)
        X = shape(th, 0.9*s/steps)
        tnew = tangents(X)
        for i in range(N):
            U[i] = rot_between(told[i], tnew[i])@U[i]
            U[i] -= (U[i]@tnew[i])*tnew[i]; U[i] /= np.linalg.norm(U[i])
        if s % 40 == 0:
            Tw = twist_from_frames(X, U); Wr = writhe(X)
            devs.append(abs(Tw + Wr - 3.0)); Wrs.append(Wr)
    assert max(devs) < 5e-3, "Lk = Tw + Wr holds through the morph (independent measurements)"
    assert abs(Wrs[-1]) > 0.3, "writhe visibly absorbs twist (order 0.5 exchanged)"
    # B2: supercoiling energetics along the family
    Lk = 3.0
    aa = np.linspace(0, 0.9, 19)
    def total(a, kt, kb=1.0):
        X2 = shape(th, a)
        L = np.sum(np.linalg.norm(np.roll(X2, -1, 0) - X2, axis=1))
        return kb*bend_energy(X2) + 2*np.pi**2*kt*(Lk - writhe(X2))**2/L
    def argmin_a(kt):
        return aa[int(np.argmin([total(a, kt) for a in aa]))]
    a_low, a_high = argmin_a(0.0005), argmin_a(0.02)
    assert a_low < 0.06, "below threshold: the flat twisted circle is the minimum"
    assert a_high > 0.3, "above threshold: the minimum moves off-circle -- supercoiling"
    print(f"B1 ledger: max |Lk-3| = {max(devs):.1e} while Wr swings to {Wrs[-1]:+.3f}")
    print(f"B2 supercoiling: minimizer a = {a_low:.2f} (low kt) -> {a_high:.2f} (high kt)")
    print("PASS: Link = Twist + Writhe holds dynamically on literal strands, and the strand")
    print("      sheds twist into writhe above threshold -- physics no lattice could express.")


if __name__ == "__main__":
    test()
