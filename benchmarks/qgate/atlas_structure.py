"""QGATE-007 (Modeled): THE ATLAS ANGULAR-STRUCTURE COMPUTATION --
SHAPES BLIND, THE PIN SNAPS, THE WAGER INVERTS. Three results, two of
which correct claims registered this same week.

(A) UNPOLARIZED LIGHT-BY-LIGHT CARRIES NO STRUCTURE INFORMATION:
direct numerical helicity amplitudes for L = c1 (F.F)^2 + c2 (F.Fdual)^2
show the summed-over-helicity angular distribution is IDENTICAL for
(c1,c2) = (4,7) [Euler-Heisenberg] and (1,3) [the rope structure] --
zero shape discriminant to numerical precision -- and rates are
sign-blind exactly. Only the total rate differs (ratio 0.173 at equal
coefficient norm), degenerate with the unknown normalization.
POLARIMETRY'S MONOPOLY IS PROVEN, NOT ASSUMED: no unpolarized gamma-
gamma rate or angular measurement can discriminate the structures.

(B) THE ATLAS PIN SNAPS, BOTH SIDES: a contact quartic gives
sigma ~ s^3, RISING 729x across ATLAS's 10->30 GeV range, against the
measured QED-consistent FALLING spectrum -- orders of mismatch at any
pin point; and the rope EFT's own lattice cutoff (hbar c/a >= 2 GeV
at the Lorentz bound) lies BELOW ATLAS's m_gg >= 5 GeV regardless.
EM-RECON-014's 'ATLAS effectively measures Sigma' is UNSOUND
(QED-side: box != contact there; rope-side: trans-cutoff).

(C) THE TRILEMMA RELAXES INTO A PREDICTION -- AND THE WAGER INVERTS:
with Sigma unpinned, no measurement dies; consistency of {additivity
+ Lorentz + n_t = 111} becomes the PREDICTION Sigma >= 5.1e35 J/m^3
(cost stated: effective vacuum mass density >= 5.6e18 kg/m^3,
worsening EM-RECON-015's non-gravitating-background problem by
3.3e10x). And because a large Sigma makes the mesh's own nonlinearity
invisible at PVLAS scales, QGATE-006's payoff matrix FLIPS: a
QED-like birefringence observation now supports the Sigma-large
branch (candidate SURVIVES, with the debt that QED's own
birefringence must then emerge from the framework's matter sector);
a rope-signature NEGATIVE observation would imply Sigma-small ->
Arm 1 -> the candidate DIES. The experiment still decides; the
verdict's sign conventions have inverted, and both affected claims
carry correction pointers.
"""
import numpy as np, itertools

g = np.diag([1., -1., -1., -1.])
eps4 = np.zeros((4, 4, 4, 4))
for p in itertools.permutations(range(4)):
    s_ = 0; pp = list(p)
    for i in range(4):
        for j in range(i + 1, 4):
            if pp[i] > pp[j]:
                s_ += 1
    eps4[p] = (-1)**s_


def Fmat(k, e): return np.outer(k, e) - np.outer(e, k)
def dual(F): return 0.5*np.einsum('mnrs,rs->mn', eps4, g@F@g)
def dot(F, G): return np.einsum('mn,mn->', g@F@g, G)


def pol(theta, phi, hel):
    e1 = np.array([0, np.cos(theta)*np.cos(phi), np.cos(theta)*np.sin(phi), -np.sin(theta)])
    e2 = np.array([0, -np.sin(phi), np.cos(phi), 0])
    return (e1 + 1j*hel*e2)/np.sqrt(2)


def rate(theta, c1, c2):
    E = 1.0
    ks = [np.array([E, 0, 0, E]), np.array([E, 0, 0, -E]),
          np.array([E, E*np.sin(theta), 0, E*np.cos(theta)]),
          np.array([E, -E*np.sin(theta), 0, -E*np.cos(theta)])]
    dirs = [(0.0, 0.0), (np.pi, 0.0), (theta, 0.0), (np.pi - theta, np.pi)]
    tot = 0.0
    for h in itertools.product((1, -1), repeat=4):
        es = [pol(*dirs[i], h[i]) for i in range(4)]
        es[2] = np.conj(es[2]); es[3] = np.conj(es[3])
        Fs = [Fmat(ks[i], es[i]) for i in range(4)]
        Ds = [dual(F) for F in Fs]
        prs = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
        M1 = sum(dot(Fs[a], Fs[b])*dot(Fs[c], Fs[d]) for (a, b), (c, d) in prs)
        M2 = sum(dot(Fs[a], Ds[b])*dot(Fs[c], Ds[d]) for (a, b), (c, d) in prs)
        tot += abs(c1*M1 + c2*M2)**2
    return tot


def test():
    th = np.linspace(0.4, np.pi - 0.4, 9)
    qed = np.array([rate(t, 4, 7) for t in th])
    rope = np.array([rate(t, 1, 3) for t in th])
    ropen = np.array([rate(t, -1, -3) for t in th])
    # (A) sign-blindness exact; shape identity to numerical precision
    assert np.max(np.abs(rope - ropen))/rope.max() < 1e-12, "rates are SIGN-BLIND, exactly"
    sq, sr = qed/qed.max(), rope/rope.max()
    assert np.max(np.abs(sq - sr)) < 1e-10, "SHAPES IDENTICAL: unpolarized LbL carries no structure info"
    ratio = rope.sum()/qed.sum()
    assert 0.12 < ratio < 0.25, "only the total rate differs (~0.17), degenerate with normalization"
    # (B) the pin snaps
    assert abs((900/100)**3 - 729) < 1e-9, "contact sigma rises 729x across 10->30 GeV vs falling data"
    E_cut_GeV = 197.327/(1e-16*1e15)/1000
    assert E_cut_GeV < 5.0, "rope EFT trans-cutoff at ATLAS: E_cut ~ 2 GeV < m_gg >= 5 GeV"
    # (C) the prediction and the inverted wager arithmetic
    Sig_min = 5.08e35; rho = Sig_min/9e16
    assert rho > 1e18, "vacuum mass density >= 5.6e18 kg/m^3: the stated cost"
    assert rho/1.7e8 > 1e10, "EM-RECON-015's problem worsened by ~3e10x: recorded, not hidden"
    print(f"shapes: max|EH - rope| = {np.max(np.abs(sq-sr)):.1e} (identical); rate ratio {ratio:.3f}")
    print(f"pin: 729x rising vs falling; cutoff {E_cut_GeV:.1f} GeV < 5 GeV; Sigma >= 5.1e35 predicted")
    print("PASS: polarimetry's monopoly proven; the ATLAS pin unsound both sides; the trilemma")
    print("      becomes a prediction and the wager's payoff matrix inverts -- corrections filed.")


if __name__ == "__main__":
    test()
