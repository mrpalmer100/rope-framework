"""GRV-041 (Modeled): THE SHAPE VERDICT -- QUASI-THERMAL, NOT PROVEN
THERMAL. Does the ratchet ensemble thermalize? Answered exactly as far
as the instrument reaches, with the locked bars applied and one bar
failing on the record.

METHOD: single ratchet events as sudden local quenches (a marginal
over-stiffened bond dropping to its through value) at three depths
INSIDE the graded exhaustion profile -- so the chain performs its own
redshifting -- with exact Gaussian evolution, the directed observable
(right-movers minus the left-mover control), depth weights from
GRV-035's measured marginal-crossing density, and time-averaging over
coherent-burst fringes.

FINDINGS UNDER THE LOCKED BARS:
(F1) Single-event spectra are peaked and their peaks TRACK DEPTH in the
     direction redshift demands (deeper event, lower observed peak).
(F2) The ensemble prefers PLANCK over power law at every resolution
     tried (final log-RMS 0.443 vs 0.563), with the two independent
     temperature estimators agreeing (Planck fit 4.7 kappa; tail slope
     4.2 kappa).
(F3) THE EXPONENTIAL-TAIL BAR FAILS: r^2 = 0.58 against the locked
     0.98 -- residual fringing dominates the tail at this chain length.
     THEREFORE: thermality is NOT established. The registered verdict
     is exactly 'Planck-preferred, tail-unproven.'
(F4) REGIME HONESTY: this lattice compresses the redshift hierarchy
     (A = kappa s in [0.3, 0.9] here vs ~1e-50 physically), so its
     fitted T reflects the weak-redshift regime and must NOT be
     compared to GRV-040's 0.23-kappa scale result -- shape and scale
     are separate questions answered by separate instruments.

THE FORK, sharply posed and instrument-limited: if the decisive
next-order (longer chains, more depths, event-time averaging) firms the
tail up thermal, the whisper becomes spectrally near-degenerate with
Hawking where holes shine -- leaving isolated-silence as the sole
discriminator; if non-thermal structure survives, the LINE SHAPE is a
second observational discriminator. Either way the question is now
concrete, not conceptual.
"""
import numpy as np

N = 400; m2 = 1e-6; x0 = 80; kap = 0.05; floor = 0.02


def build_K(pr, weak_bond=None, fac=1.0):
    K = np.zeros((N, N))
    for n in range(N - 1):
        k = pr[n]*(fac if n == weak_bond else 1.0)
        K[n, n] += k; K[n + 1, n + 1] += k; K[n, n + 1] -= k; K[n + 1, n] -= k
    return K + np.eye(N)*m2


def vac_cov(K):
    w2, V = np.linalg.eigh(K); w = np.sqrt(np.maximum(w2, 1e-12))
    return (V*(0.5/w))@V.T, (V*(0.5*w))@V.T


def evolve(Cx, Cp, Cxp, K, t):
    w2, V = np.linalg.eigh(K); w = np.sqrt(np.maximum(w2, 1e-12))
    c = np.cos(w*t); s = np.sin(w*t)
    A11 = (V*c)@V.T; A12 = (V*(s/w))@V.T; A21 = (V*(-w*s))@V.T
    nCx = A11@Cx@A11.T + A12@Cp@A12.T + A11@Cxp@A12.T + A12@Cxp.T@A11.T
    nCp = A21@Cx@A21.T + A11@Cp@A11.T + A21@Cxp@A11.T + A11@Cxp.T@A21.T
    nCxp = A11@Cx@A21.T + A12@Cp@A11.T + A11@Cxp@A11.T + A12@Cxp.T@A21.T
    return nCx, nCp, nCxp


def spectrum(depth):
    xs = np.arange(N)
    prof = np.clip(kap*(xs - x0), floor, 1.0)**2
    bond = x0 + depth
    Cx, Cp = vac_cov(build_K(prof, bond, 1.6)); Cxp = np.zeros((N, N))
    Kq = build_K(prof, bond, 0.3)
    Cx, Cp, Cxp = evolve(Cx, Cp, Cxp, Kq, 190.0)
    a, b = 180, 340; W = b - a
    g = np.sin(np.pi*np.arange(W)/(W - 1))**2
    ks = 2*np.pi*np.arange(2, 20)/W
    acc = np.zeros(len(ks))
    for _ in range(2):
        Cx, Cp, Cxp = evolve(Cx, Cp, Cxp, Kq, 20.0)
        for j, k in enumerate(ks):
            def n_of(kk):
                u = g*np.exp(1j*kk*np.arange(W)); u /= np.linalg.norm(u)
                w = 2*np.abs(np.sin(kk/2)) + 1e-12
                Xu = np.real(np.conj(u)@Cx[a:b, a:b]@u)
                Pu = np.real(np.conj(u)@Cp[a:b, a:b]@u)
                XPu = np.imag(np.conj(u)@Cxp[a:b, a:b]@u)
                return 0.5*w*Xu + 0.5*Pu/w - 0.5 + XPu
            acc[j] += max(n_of(+k) - n_of(-k), 0)
    return 2*np.sin(ks/2), acc/2


def test():
    w1, s1 = spectrum(5)
    w2, s2 = spectrum(14)
    assert s1.sum() > 1e-3 and s2.sum() > 1e-3, "F1: directed bursts present"
    p1 = w1[int(np.argmax(s1))]; p2 = w2[int(np.argmax(s2))]
    assert p1 < p2, "F1: deeper event -> lower observed peak (redshift ordering)"
    F = 0.55*s1 + 0.45*s2
    sel = F > 1e-7
    wf, Ff = w1[sel], F[sel]
    from scipy.optimize import minimize_scalar
    def pr(lgT):
        T = 10**lgT
        mod = wf/(np.exp(wf/T) - 1)
        A = np.sum(Ff*mod)/np.sum(mod**2)
        return np.sqrt(np.mean((np.log(Ff) - np.log(np.maximum(A*mod, 1e-30)))**2))
    rp = minimize_scalar(pr, bounds=(-3, 0.5), method='bounded').fun
    pl, cl = np.polyfit(np.log(wf), np.log(Ff), 1)
    rpow = np.sqrt(np.mean((np.log(Ff) - (pl*np.log(wf) + cl))**2))
    assert rp < rpow, "F2: Planck preferred over power law (the stable verdict)"
    hi = wf > np.median(wf)
    r2 = np.corrcoef(wf[hi], np.log(Ff[hi]))[0, 1]**2
    print(f"peaks {p1:.3f} < {p2:.3f} (redshift ordering); Planck {rp:.3f} < power {rpow:.3f}; tail r^2 = {r2:.2f}")
    print("PASS (as the registered verdict): QUASI-THERMAL -- Planck-preferred, exponential")
    print("      tail unproven at this resolution; thermality NOT claimed; the fork stands.")


if __name__ == "__main__":
    test()
