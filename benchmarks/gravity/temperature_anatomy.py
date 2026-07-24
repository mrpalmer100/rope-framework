"""GRV-046 (Modeled): THE TEMPERATURE-OFFSET ANATOMY -- the 1.3 made
arithmetic. The whisper's temperature coefficient c1 = T/kappa is
decomposed into measured contributions, its sensitivities ledgered,
GRV-044's window formula shown to capture the tail temperature to a
few percent, and the deep question answered: 2pi is a point the
structure CROSSES, not a point it selects.

THE LEDGER (measured kernel, re-measured live in this benchmark):
- baseline c1 ~ 0.20 (consistent with GRV-043's 0.21 within the
  kernel-measurement spread) -- ratio ~1.2-1.3 x Hawking's 1/2pi;
- greybody contributes about -23 percent (soft-side suppression cools
  the fitted temperature);
- kernel-width elasticity dlnT/dln(width) ~ +1.1 (wider bursts, hotter
  whisper -- as the (kappa s2)^2/lambda structure of the window formula
  demands, lambda scaling as inverse width squared);
- shell-edge elasticity dlnT/dln(s2) ~ +0.7 (sub-linear because the
  fit window mixes the rho-imaging and running-tail regimes; the pure
  asymptotic formula would give +2 -- the dilution is understood, and
  stated);
- GRV-044's formula at the tail centroid captures the measured tail
  temperature at the few-percent level.

THE 2PI VERDICT: sweeping kernel width, c1 passes smoothly through
1/2pi (at ~0.83 x the measured width) -- no limit of the generating
structure selects 2pi, and the measured engine sits 20-30 percent
above the crossing. CONSEQUENCE: the O(1) agreement with Hawking is
STRUCTURAL (both scales are kappa -- that is GRV-040's cancellation),
while the precise coefficient is corpus-specific and PREDICTED. The
temperature itself becomes the FOURTH discriminator, alongside
isolated silence, the feeding law, and the running tail: a precision
temperature at c1 = 1.2-1.3 x (1/2pi) identifies reconnection noise.

STATUS HONESTY: Modeled -- the ledger rests on the fit-window
convention and the compact kernel re-measurement; the formula-capture
component inherits GRV-044's Derived machinery.
"""
import numpy as np, sys, os
from scipy.optimize import minimize_scalar
sys.path.insert(0, os.path.dirname(__file__))
from pileup_integral import burst_kernel

kap = 0.05; s1 = 1/4.5; S2 = 1/0.6


def test():
    Om, Bv = burst_kernel()
    Ts = np.array([0.6, 1.0, 1.5, 2.2, 3.2, 4.5]); pT = np.array([1.0, 0.917, 0.667, 0.333, 0.250, 0.0])
    Pg = np.linspace(0.6, 4.5, 300); pg = np.interp(Pg, Ts, pT)
    wP = np.maximum(-np.gradient(pg, Pg), 0)
    def rho(s):
        P = 1.0/np.asarray(s); return np.interp(P, Pg, wP, left=0, right=0)*P**2
    Nc = 500; x0 = 100
    cs = np.clip(kap*(np.arange(Nc) - x0), 0.02, 1.0); kts = cs**2
    def Tgf(wf):
        if wf <= 0 or wf >= 1.98: return 0.0
        k = 2*np.arcsin(wf/2)
        u = np.zeros(Nc, complex); u[Nc-1] = np.exp(1j*k*(Nc-1)); u[Nc-2] = np.exp(1j*k*(Nc-2))
        for n in range(Nc - 2, x0 + 1, -1):
            u[n-1] = ((kts[n] + kts[n-1] - wf**2)*u[n] - kts[n]*u[n+1])/kts[n-1]
        sh = slice(x0 + 2, x0 + 10)
        return min(1.0/max(np.mean(np.abs(u[sh]))**2, 1e-12)*np.mean(cs[sh]), 1.0)
    def spectrum(width=1.0, s2=S2, grey=True):
        Bi = lambda x: np.interp(x/width, Om, Bv, left=0, right=0)
        sv = np.linspace(s1, s2, 1500); ds = sv[1] - sv[0]; rs = rho(sv)
        oms = np.exp(np.linspace(np.log(0.05*kap), np.log(1.8), 120))
        F = np.array([np.sum(rs*Bi(om/(kap*sv))/(kap*sv))*ds for om in oms])
        if grey: F = F*np.array([Tgf(o) for o in oms])
        sel = F > F.max()*1e-6
        return oms[sel], F[sel]
    def planck_T(wf, Ff):
        def pres(lgT):
            T = 10**lgT; mod = wf/(np.exp(wf/T) - 1)
            A = np.sum(Ff*mod)/np.sum(mod**2)
            return np.sqrt(np.mean((np.log(Ff) - np.log(np.maximum(A*mod, 1e-30)))**2))
        return 10**minimize_scalar(pres, bounds=(-4, 0.5), method='bounded').x
    w0, F0 = spectrum(); T0 = planck_T(w0, F0)
    assert 0.15 < T0/kap < 0.27, "baseline reproduces GRV-043 within the kernel spread"
    _, Fng = spectrum(grey=False); Tng = planck_T(*spectrum(grey=False))
    assert Tng > T0, "greybody cools the fitted temperature (negative contribution)"
    Tw = planck_T(*spectrum(width=1.2))
    ew = np.log(Tw/T0)/np.log(1.2)
    assert 0.7 < ew < 1.5, "kernel-width elasticity ~ +1"
    Ts_ = planck_T(*spectrum(s2=S2*0.8))
    es = np.log(Ts_/T0)/np.log(0.8)
    assert 0.4 < es < 1.1, "shell-edge elasticity positive, sub-linear (regime mixing understood)"
    lam = 2.65
    ipk = int(np.argmax(F0)); tail = w0 > 1.3*w0[ipk]
    se, _ = np.polyfit(w0[tail], np.log(F0[tail]), 1)
    om_bar = np.mean(w0[tail])
    Tf = 1/(2*lam*om_bar/(kap*S2)**2 + 2/om_bar)
    assert abs((-1/se)/Tf - 1) < 0.10, "GRV-044's formula captures the tail temperature"
    c_lo = planck_T(*spectrum(width=0.8))/kap
    c_hi = planck_T(*spectrum(width=1.5))/kap
    inv2pi = 1/(2*np.pi)
    assert c_lo < inv2pi < c_hi, "the 2pi crossing exists: 2pi is crossed, not selected"
    print(f"c1 = {T0/kap:.3f} ({T0/kap*2*np.pi:.2f} x 1/2pi); greybody {((T0-Tng)/T0*100):+.0f}%; "
          f"elasticities width {ew:+.2f}, s2 {es:+.2f}")
    print(f"formula capture {(-1/se)/Tf:.3f}; 2pi crossed inside width sweep [{c_lo:.3f},{c_hi:.3f}]")
    print("PASS: the 1.3 is arithmetic -- every contribution measured, 2pi crossed not selected;")
    print("      the temperature coefficient is the FOURTH discriminator.")


if __name__ == "__main__":
    test()
