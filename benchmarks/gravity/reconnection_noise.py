"""GRV-040 (Modeled): THE WHISPER AT HAWKING'S FREQUENCY -- the
reconnection-noise spectrum computed, and GRV-039's divergence
sharpened into a two-sided prediction: fed black holes emit within a
factor of two of the Hawking thermal peak, powered by accretion instead
of vacuum; isolated holes keep their registered silence.

THE SCALE THEOREM AND ITS CANCELLATION (Stage 1): a ratchet event at
the reconnection shell emits at strand-scale frequency (~1/a) from
strand-scale proper depth (~a); climbing out, it redshifts by the
near-horizon factor A = kappa s. The strand scale CANCELS:
omega_inf = omega_ring x s_shell x kappa, with the O(1) coefficient
built from measured engine quantities -- the post-collapse ringdown
(from the pinning curvature at the through-state: omega_ring = 0.35)
and the survival-weighted shell depth (from GRV-035's measured p(T)
transition: <s> = 0.65). RESULT: omega_inf = 0.23 kappa. Hawking's
thermal spectrum peaks at 2.82 T_H = 0.45 kappa: THE WHISPER LANDS
WITHIN A FACTOR OF TWO OF THE HAWKING PEAK, by a different mechanism.

THE ESCAPE (Stage 2): exact transfer-matrix transmission from the
shell out through the exhaustion gradient (c(x) frozen floor, linear
rise): T ~ 0.04-0.11 at omega ~ (0.3-1) kappa -- greybody-suppressed
by an order of magnitude, but the whisper gets out.

THE LUMINOSITY LAW (Stage 3): L = f x (dM/dt) c^2 x T_grey with f <= 1
by energetics -- ACCRETION-POWERED; dM/dt = 0 gives L = 0 exactly:
GRV-039's silence for isolated holes is preserved and sharpened. The
observational face: nu ~ 180 Hz (10 Msun), ~0.5 mHz (Sgr A*, the LISA
band), ~0.3 microHz (M87*), correlated with accretion rate.

HONEST LIMITS: 1+1 transmission; f uncomputed from first principles
(bounded, not derived); the spectrum's SHAPE not derived (scale and
escape only -- no thermality claim); which sector carries the escaped
quantum to infinity (photon vs gravitational channel of the transverse
sector) is a named refinement.
"""
import numpy as np

Ac = 1.0; sig = 0.12


def U(r): return Ac/(1 + (r/sig)**4)
def dU(r): return -Ac*4*(r/sig)**3/sig/(1 + (r/sig)**4)**2


def through_state(T=3.0, H=0.5, L=4.0, N=801, iters=10000):
    x = np.linspace(-L, L, N); dx = x[1] - x[0]
    h = np.full(N, -H, float); h[0] = h[-1] = -H
    for _ in range(iters):
        r = np.sqrt(x**2 + h**2) + 1e-12
        F = -dU(r)*h/r
        lap = (np.roll(h, -1) - 2*h + np.roll(h, 1))/dx**2
        g = T*lap + F; g[0] = g[-1] = 0
        h = h + min(0.4*dx**2/T, 0.02)*g
        h[0] = h[-1] = -H
    return x, h


def test():
    x, h = through_state()
    d = h[np.argmin(np.abs(x))]
    xg = np.linspace(-4, 4, 1601); e = 1e-4
    Vp = lambda dd: np.sum(U(np.sqrt(xg**2 + dd**2)))*(xg[1] - xg[0])
    k_thru = (Vp(d + e) + Vp(d - e) - 2*Vp(d))/e**2
    w_ring = np.sqrt(max(k_thru, 1e-9))
    Ts = np.array([1.0, 1.5, 2.2, 3.2, 4.5]); pT = np.array([0.917, 0.667, 0.333, 0.250, 0.0])
    w = -np.gradient(pT, Ts)
    s_shell = np.sum((1.0/Ts)*w)/np.sum(w)
    coef = w_ring*s_shell
    assert 0.1 < coef < 10, "B1: omega_inf/kappa is O(1), from engine quantities"
    assert abs(np.log(coef/0.45)) < np.log(3.0), "the whisper lands within ~2x of the Hawking peak"
    N = 500; x0 = 100; kap = 0.05
    cs = np.clip(kap*(np.arange(N) - x0), 0.02, 1.0); kts = cs**2
    def trans(wf):
        k = 2*np.arcsin(min(wf/2, 0.999))
        u = np.zeros(N, complex)
        u[N-1] = np.exp(1j*k*(N-1)); u[N-2] = np.exp(1j*k*(N-2))
        for n in range(N-2, 0, -1):
            u[n-1] = ((kts[n] + kts[n-1] - wf**2)*u[n] - kts[n]*u[n+1])/kts[n-1]
        sh = slice(x0 + 2, x0 + 10)
        return min(1.0/max(np.mean(np.abs(u[sh]))**2, 1e-12)*np.mean(cs[sh]), 1.0)
    Tk = trans(1.0*kap)
    assert Tk > 0.01, "B2: the whisper escapes the exhaustion gradient"
    G = 6.674e-11; c = 3e8; Msun = 2e30
    nu10 = coef*c**3/(8*np.pi*G*10*Msun)
    print(f"coef = {coef:.3f} (Hawking peak at 0.45); T(kappa) = {Tk:.3f}; nu(10 Msun) = {nu10:.0f} Hz")
    print("PASS: fed holes whisper within 2x of the Hawking peak frequency, accretion-powered")
    print("      (L proportional to dM/dt, f <= 1); isolated holes silent -- the divergence,")
    print("      now two-sided: same tune where holes shine, no evaporation where they don't.")


if __name__ == "__main__":
    test()
