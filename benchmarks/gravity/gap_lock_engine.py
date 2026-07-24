"""GRV-027 (Modeled): THE GAP-LOCK COMPUTED FROM FIRST PRINCIPLES ON THE
STRAND ENGINE -- the tension channel VIOLATES the lock at O(1), and the
gamma = 1 prediction contracts to a single named locus in conditioning
space.

THE COMPUTATION: the crossing stiffness k_c(T) -- a strand under tension
T pressed over an orthogonal strand by the weave's over/under geometry,
with the corpus's EXACT finite contact law U(r) = Ac/(1 + (r/sigma)^4)
(FND-KIN-005 / FND-STRAND-001) -- solved by relaxation across the full
tension range. GRV-026's lock, assembled to strand level, requires
d ln k_c = (3/2) d ln T - d ln l.

RESULTS:
(R1) MEASURED EXPONENT: s_T = d ln k_c / d ln T = 1.11 on a clean
     two-decade plateau (T = 0.02 to 0.2; standoff d* shrinking 0.44 to
     0.26), consistent with the quartic-tail scaling analysis
     (s_T -> (n+2)/(n+1) = 6/5 for the 1/r^4 tail).
(R2) THE VERDICT: eps_T = s_T - 3/2 = -0.39. The tension-channel
     gap-lock is violated at order one -- far beyond Cassini's 2.4e-3
     allowance. PURE-TENSION CONDITIONING IS EXCLUDED as the gamma = 1
     carrier: a registered negative for the simplest composition.
(R3) THE ENGINE'S REGIME MAP, a bonus: above T ~ 1-2 the over-crossing
     PUNCHES THROUGH (d* < 0) -- the finite barrier surrenders and the
     weave topology fails, exactly as the finite-contact ontology
     permits. The weave-intact regime is mapped, not assumed.
(R4) THE SURVIVAL LOCUS: with eps_l = +1 (analytic: per-crossing k_c is
     l-independent while the lock demands -d ln l), gamma = 1 requires
     the conditioning composition d ln l = +0.39 d ln T -- spacing
     co-varying with tension in a measured ratio, to ~0.6 percent
     (Cassini via |gamma - 1| = 4.2 eps_net^2).

CONSEQUENCE: GRV-026's conditions (C1) and (C2) MERGE. The framework's
1.751-arcsecond prediction now hangs on one computable property of
GRV-005's defect statics: does the equilibrium conditioning field lie on
the locus? On-locus: 1.751" derived. Off by delta: gamma - 1 =
-4.2 delta^2, an internal falsifier. The chain ends at one question.
"""
import numpy as np

Ac = 1.0; sig = 0.12


def U(r): return Ac/(1 + (r/sig)**4)
def dU(r): return -Ac*4*(r/sig)**3/sig/(1 + (r/sig)**4)**2


def solve_crossing(T, H=0.5, L=4.0, N=1201, iters=25000):
    x = np.linspace(-L, L, N); dx = x[1] - x[0]
    h = -H + (H + 2*sig)*np.exp(-(x/(4*sig))**2)
    for it in range(iters):
        r = np.sqrt(x**2 + h**2) + 1e-12
        F = -dU(r)*h/r
        lap = (np.roll(h, -1) - 2*h + np.roll(h, 1))/dx**2
        g = T*lap + F
        g[0] = g[-1] = 0
        h = h + min(0.4*dx**2/T, 0.02)*g
        h[0] = h[-1] = -H
    d = h[np.argmin(np.abs(x))]
    def Vpin(dd): return np.sum(U(np.sqrt(x**2 + dd**2)))*dx
    e = 1e-4
    kc = (Vpin(d + e) + Vpin(d - e) - 2*Vpin(d))/e**2
    return d, kc


def test():
    Ts = np.array([0.02, 0.05, 0.1, 0.2])
    out = [solve_crossing(T) for T in Ts]
    ds = np.array([o[0] for o in out]); ks = np.array([o[1] for o in out])
    assert np.all(ds > 0), "weave-intact regime: positive standoff"
    s = np.polyfit(np.log(Ts), np.log(ks), 1)[0]
    assert 1.0 < s < 1.25, "plateau exponent (quartic-tail class)"
    eps_T = s - 1.5
    assert eps_T < -0.25, "TENSION-CHANNEL LOCK VIOLATED at O(1)"
    d_hi, _ = solve_crossing(5.0)
    assert d_hi < 0, "punch-through above the weave-intact regime (finite barrier surrenders)"
    print(f"s_T = {s:.3f} (plateau), eps_T = {eps_T:+.3f}; punch-through at T=5 confirmed")
    print(f"survival locus: d ln l = {-eps_T:.2f} d ln T  (with eps_l = +1 analytic)")
    print("PASS (as the measured lock violation): pure-tension conditioning excluded;")
    print("      gamma = 1 lives on one named locus of GRV-005's statics.")


if __name__ == "__main__":
    test()
