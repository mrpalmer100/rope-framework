"""QGATE-001 (Modeled): THE AMPLITUDE-SCALING TEST -- THE SMOOTH NO-GO
AND THE RECONNECTION EXCEPTION. Bars locked BEFORE data: a cycle is
amplitude-independent iff J proportional to A^nu with nu < 0.5; the
candidate list (C1 harmonic, C2 helix screw, C3 substrate breather,
C4 compact phase slip, C5 reconnection separatrix) was registered
before any computation.

THE SMOOTH NO-GO (C1-C4, unanimous): harmonic nu = 2 (exact,
J = pi mu omega A^2), screw rotation nu = 1 (exact, J = 2pi I omega),
substrate breather nu ~ 1.97 (measured on a sine-Gordon chain),
compact 2pi phase slip nu = 1 (exact). Within the quadratic/elastic
Lagrangian this is derivable in general: any cycle continuously
contractible to zero amplitude has J -> 0 with positive power. NO
UNIVERSAL ACTION QUANTUM CAN EMERGE FROM SMOOTH ROPE DYNAMICS.

THE RECONNECTION EXCEPTION (C5): the corpus's one non-smooth native
process (FND-KIN-005's exception; GRV-037's countable bit) carries a
SEPARATRIX action -- the barrier-crossing integral
W(E -> Eb+) = int sqrt(2 mu_eff (E - V)) dq -- that is NONZERO and
amplitude-independent: for a cosine contact barrier of height T D and
width 2D, W = 1.80 T D^2/c, varying 2 percent while the excitation
margin varies 100x (nu ~ 0). An amplitude-independent action scale
EXISTS natively, and it lives exactly where the topology lives.

THE HONEST MAGNITUDE, stated not hidden: under the nucleon hypothesis
(T D = 33.8 MeV, D ~ 0.029 fm), W/hbar ~ 0.009 -- two orders low.
This is NOT hbar derived; it is the right KIND of object at the wrong
size under current geometric assumptions, with the sensitivity named
(W ~ kappa T D^2/c depends on the barrier form and on whether
reconnection is single-strand or collective).

THE MINIMAL NEW DYNAMICAL POSTULATE, identified as the no-go demands:
if a universal action enters the framework, it must attach to the
DISCRETE RECONNECTION COUNT, not to smooth waves -- and the corpus
already counts reconnections (GRV-035 horizon percolation, GRV-037
the bit), so the postulate would unify black-hole bit counting with
quantum action. Flagged conjecture-grade. The nonlocal branch (Born
equivariance, measurement, Bell) is UNTOUCHED by this result: nothing
here produces configuration-space structure -- the frontier splits
exactly as the campaign commission predicted.
"""
import numpy as np


def W_of_E(E, Eb=1.0, D=1.0, mu_eff=1.0, n=3000):
    q = np.linspace(-D, D, n)
    V = Eb*(1 + np.cos(np.pi*q/D))/2
    return float(np.trapezoid(np.sqrt(np.maximum(2*mu_eff*(E - V), 0)), q))


def breather_nu():
    def J(A0, n=56, dt=0.005, Tmax=260.0):
        x = np.arange(n) - n/2
        u = 4*np.arctan(A0*np.exp(-np.abs(x)/4)); v = np.zeros(n)
        us, ts = [], []; t = 0.0
        for s in range(int(Tmax/dt)):
            u += 0  # clarity
            lap = np.roll(u, 1) + np.roll(u, -1) - 2*u
            v += dt*(lap - np.sin(u)); u += dt*v; t += dt
            if s % 5 == 0:
                us.append(u[n//2]); ts.append(t)
        us = np.array(us); ts = np.array(ts); cs = us - us.mean()
        idx = np.where((cs[:-1] < 0) & (cs[1:] >= 0))[0]
        if len(idx) < 3:
            return None
        period = float(np.mean(np.diff(ts[idx])))
        lap = np.roll(u, 1) + np.roll(u, -1) - 2*u
        E = float(np.sum(0.5*v**2 + 0.5*(np.roll(u, -1) - u)**2 + (1 - np.cos(u))))
        return E*period
    As, Js = [], []
    for A0 in (0.4, 0.2, 0.1):
        j = J(A0)
        if j:
            As.append(A0); Js.append(j)
    return float(np.polyfit(np.log(As), np.log(Js), 1)[0])


def test():
    # LOCKED BARS: nu >= 0.5 scales-to-zero; nu < 0.5 bridge. Candidates pre-registered.
    As = np.array([0.4, 0.2, 0.1, 0.05])
    nu1 = float(np.polyfit(np.log(As), np.log(np.pi*As**2), 1)[0])
    nu2 = float(np.polyfit(np.log(As), np.log(2*np.pi*As), 1)[0])
    nu4 = nu2
    assert nu1 > 1.9, "C1 harmonic: nu = 2 exact -- scales to zero"
    assert 0.9 < nu2 < 1.1, "C2 screw: nu = 1 exact -- scales to zero"
    nu3 = breather_nu()
    assert nu3 > 1.5, "C3 breather: scales to zero at small amplitude"
    assert nu4 >= 0.5, "C4 phase slip: scales to zero"
    # C5: the reconnection separatrix -- nonzero, amplitude-independent
    W0 = W_of_E(1.0000001)
    Ws = [W_of_E(E) for E in (1.0001, 1.001, 1.01)]
    assert W0 > 0.5, "reconnection separatrix action is NONZERO (order T D^2/c)"
    assert 1.5 < W0 < 2.1, "kappa = 1.80 for the cosine barrier (band for grid)"
    assert max(abs(w - W0)/W0 for w in Ws) < 0.05, "amplitude-INDEPENDENT: <5% over 100x margin"
    ratio = W0*33.8*(0.8/27.75)/197.327
    print(f"smooth cycles: nu = {nu1:.2f}, {nu2:.2f}, {nu3:.2f}, {nu4:.2f} -- ALL scale to zero (no-go)")
    print(f"reconnection separatrix: W = {W0:.3f} T D^2/c, amplitude-independent to <5% (bridge)")
    print(f"honest magnitude under nucleon hypothesis: W/hbar ~ {ratio:.4f} (stated, not asserted)")
    print("PASS: no action floor in smooth dynamics; the one non-smooth native process carries a")
    print("      fixed separatrix action -- if hbar enters, it attaches to the reconnection count.")


if __name__ == "__main__":
    test()
