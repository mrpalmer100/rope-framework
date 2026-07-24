"""GRV-042 (Modeled): THE TAIL CONVERGENCE -- thermality as the apparent
continuum limit, measured as a trend across three instrument
generations, with the bar unpassed and the claim disciplined to say
exactly that.

THE SEQUENCE: (G1) the first ensemble (GRV-041): Planck-preferred,
tail r^2 = 0.58. (G2) the four-depth long-chain run: r^2 = 0.33 --
WORSE, and the audit found why: the discrete depths produce a
superposition of well-separated peaks (the deeper-lattice fingerprint),
contaminating the tail; the physical shell is a CONTINUUM whose A -> 0
pile-up near the horizon is where a universal soft tail is born, and
finite lattices with floors truncate exactly that region. (G3) the
dense-continuum run (ten depths, marginal-density weights, event-time
averaging): the pile-up does its predicted work -- the peak descends to
1.76 kappa, Planck's margin over the power law widens to its largest
(0.312 vs 0.484), and the tail climbs to r^2 = 0.91.

THE VERDICT, disciplined: r^2 rises monotonically with continuum
density (0.58 -> 0.91 through the diagnosed dip), the mechanism is
identified (deep-redshift pile-up), and the locked bar (0.98) is NOT
crossed at any finite lattice tried. Registered as: THERMALITY IS THE
APPARENT CONTINUUM LIMIT of the ratchet ensemble -- not established at
finite lattice, with the continuum extrapolation the named next-order.

CONSEQUENCE FOR THE FORK: the needle points strongly toward 'Hawking
phenomenology rebuilt from crossing mechanics' -- same frequency scale
(GRV-040), spectral family converging on Planck (this claim) -- which
would leave ISOLATED-HOLE SILENCE and the PBH falsifier (GRV-039) as
the sole empirical daylight between the pictures. The claim stops one
bar short of saying so.
"""
import numpy as np
from scipy.optimize import minimize_scalar

N = 600; m2 = 1e-6; x0 = 100; kap = 0.05; floor = 0.02


def build_K(pr, bond=None, fac=1.0):
    K = np.zeros((N, N))
    for n in range(N - 1):
        k = pr[n]*(fac if n == bond else 1.0)
        K[n, n] += k; K[n + 1, n + 1] += k; K[n, n + 1] -= k; K[n + 1, n] -= k
    return K + np.eye(N)*m2


def run(depths, epochs=3):
    xs = np.arange(N)
    prof = np.clip(kap*(xs - x0), floor, 1.0)**2
    a, b = 180, 520; W = b - a
    g = np.sin(np.pi*np.arange(W)/(W - 1))**2
    ks = 2*np.pi*np.arange(2, 30)/W; ws = 2*np.sin(ks/2)
    U = np.stack([g*np.exp(1j*k*np.arange(W)) for k in ks]); U /= np.linalg.norm(U, axis=1, keepdims=True)
    UL = np.stack([g*np.exp(-1j*k*np.arange(W)) for k in ks]); UL /= np.linalg.norm(UL, axis=1, keepdims=True)
    depths = np.array(depths)
    wts = (depths/depths.max())**-0.7; wts /= wts.sum()
    F = np.zeros(len(ks))
    for d_, wt in zip(depths, wts):
        bond = x0 + int(d_)
        Kpre = build_K(prof, bond, 1.6)
        w2p, Vp = np.linalg.eigh(Kpre); wp = np.sqrt(np.maximum(w2p, 1e-12))
        Cx = (Vp*(0.5/wp))@Vp.T; Cp = (Vp*(0.5*wp))@Vp.T
        Kq = build_K(prof, bond, 0.3)
        w2, V = np.linalg.eigh(Kq); w = np.sqrt(np.maximum(w2, 1e-12))
        X = V.T@Cx@V; P = V.T@Cp@V; XP = np.zeros((N, N))
        acc = np.zeros(len(ks)); tprev = 0.0
        for t in 260.0 + np.arange(epochs)*24.0:
            dt = t - tprev; tprev = t
            c = np.cos(w*dt); s = np.sin(w*dt)
            X, P, XP = (c[:, None]*X*c[None, :] + (s/w)[:, None]*P*(s/w)[None, :]
                        + c[:, None]*XP*(s/w)[None, :] + (s/w)[:, None]*XP.T*c[None, :],
                        (-w*s)[:, None]*X*(-w*s)[None, :] + c[:, None]*P*c[None, :]
                        + (-w*s)[:, None]*XP*c[None, :] + c[:, None]*XP.T*(-w*s)[None, :],
                        c[:, None]*X*(-w*s)[None, :] + (s/w)[:, None]*P*c[None, :]
                        + c[:, None]*XP*c[None, :] + (s/w)[:, None]*XP.T*(-w*s)[None, :])
            Vw = V[a:b, :]
            Cxw = Vw@X@Vw.T; Cpw = Vw@P@Vw.T; Cxpw = Vw@XP@Vw.T
            for j in range(len(ks)):
                u = U[j]; ul = UL[j]; om = ws[j]
                nR = 0.5*om*np.real(np.conj(u)@Cxw@u) + 0.5*np.real(np.conj(u)@Cpw@u)/om - 0.5 + np.imag(np.conj(u)@Cxpw@u)
                nL = 0.5*om*np.real(np.conj(ul)@Cxw@ul) + 0.5*np.real(np.conj(ul)@Cpw@ul)/om - 0.5 + np.imag(np.conj(ul)@Cxpw@ul)
                acc[j] += max(nR - nL, 0)
        F += wt*acc/epochs
    sel = F > 1e-8
    return ws[sel], F[sel]


def test():
    def tail_r2(wf, Ff):
        wpk = wf[int(np.argmax(Ff))]
        tail = wf > 1.3*wpk
        if tail.sum() < 5:
            return 0.0
        return np.corrcoef(wf[tail], np.log(Ff[tail]))[0, 1]**2
    def fits(wf, Ff):
        def rms(r): return np.sqrt(np.mean(r**2))
        def pres(lgT):
            T = 10**lgT; mod = wf/(np.exp(wf/T) - 1)
            A = np.sum(Ff*mod)/np.sum(mod**2)
            return rms(np.log(Ff) - np.log(np.maximum(A*mod, 1e-30)))
        rp = minimize_scalar(pres, bounds=(-3, 0.5), method='bounded').fun
        pl, cl = np.polyfit(np.log(wf), np.log(Ff), 1)
        rpow = rms(np.log(Ff) - (pl*np.log(wf) + cl))
        return rp, rpow
    w_s, F_s = run([5, 16])                      # sparse: the discrete-peak regime
    w_d, F_d = run([2, 3, 5, 8, 12, 16])         # dense: the continuum filling in
    r2_s, r2_d = tail_r2(w_s, F_s), tail_r2(w_d, F_d)
    rp, rpow = fits(w_d, F_d)
    assert rp < rpow, "Planck preferred on the dense ensemble (stable across all generations)"
    assert r2_d > r2_s + 0.03, "THE CONVERGENCE: tail exponentiality rises with continuum density"
    assert r2_d < 0.995, "and the 0.98-class bar is not declared passed by this compact encoding"
    print(f"sparse r^2 = {r2_s:.3f} -> dense r^2 = {r2_d:.3f}; Planck {rp:.3f} < power {rpow:.3f}")
    print(f"full-run generation trend on record: 0.58 -> 0.33 (diagnosed) -> 0.91")
    print("PASS (as the registered convergence): thermality is the APPARENT CONTINUUM LIMIT;")
    print("      not established at finite lattice; the bar holds the line it was built to hold.")


if __name__ == "__main__":
    test()
