"""QB-005 (Modeled, formerly Open): BORN AS ENERGY PARTITION -- three
theorems and one honest residue. The oldest structural open in the
quantum sector, moved: the SQUARE is derived from rope energetics, the
FRINGES are exact in one-quantum transmission, the STATISTICS follow
from a single named detector premise -- and the configuration where the
mechanism DEVIATES from Born is computed and registered as the
falsifiable residue.

(T1) THE SQUARE: a one-quantum packet dynamically split by a partial
     reflector; the classical field energy in each channel equals the
     amplitude-squared weight |c_i|^2 (verified 6.6e-4). The square in
     Born's rule is rope wave energetics, not a postulate.
(T2) THE FRINGES: exact monochromatic one-quantum transmission through
     mirror-patch-mirror: unitarity at 1e-14, visibility 0.75,
     Fabry-Perot model correlation 0.9997 -- with the phase a purely
     MECHANICAL quantity (tension-patch dispersion). Amplitude
     interference in detection probability, from rope mechanics.
     (Twelfth instrument catch, logged: two pulsed-packet generations
     failed for understood bandwidth/steady-state reasons; the
     monochromatic transfer matrix -- GRV-040's own tool -- was the
     right instrument.)
(T3) THE STATISTICS: one named mechanical premise -- a threshold
     detector fires at rate proportional to delivered quantum-share
     (linear detector response) -- and the exact competing-risk
     survival integral gives P(A) = |c_A|^2 at sub-percent for
     symmetric arrival. Born from energy partition.
(T4) THE RESIDUE, registered not hidden: SKEWED arrival (one path
     delayed) drives P toward the EARLY channel beyond its Born weight
     (+0.32 at the tested skew) -- standard QM gives Born regardless
     of timing. A falsifiable divergence, in principle testable by
     time-resolved single-quantum interferometry with fast detectors.

WALLS UNTOUCHED, stated at full volume: single-particle sector only;
QB-002's entanglement counting wall stands; the nonlocal
pilot-wave-substrate question is not addressed here.
"""
import numpy as np

N = 1200; m2 = 1e-6; k0 = 0.7


def build(ktvec):
    K = np.zeros((N, N))
    for n in range(N - 1):
        K[n, n] += ktvec[n]; K[n + 1, n + 1] += ktvec[n]
        K[n, n + 1] -= ktvec[n]; K[n + 1, n] -= ktvec[n]
    return K + np.eye(N)*m2


def test():
    x = np.arange(N)
    kt = np.ones(N - 1); kt[600] = 0.28
    w2, V = np.linalg.eigh(build(kt)); w = np.sqrt(np.maximum(w2, 1e-12))
    psi0 = np.exp(-((x - 350)/40.0)**2)*np.exp(1j*k0*x); psi0 /= np.linalg.norm(psi0)
    def ev(t): return V@(np.exp(-1j*w*t)*(V.T.conj()@psi0))
    psi = ev(520.0)
    PT = np.sum(np.abs(psi[610:])**2)
    u = np.real(V@((1/np.sqrt(2*w))*(V.T.conj()@psi)))
    p = -np.imag(V@(np.sqrt(w/2)*(V.T.conj()@psi)))
    def energy(a, b):
        return 0.5*np.sum(p[a:b]**2) + np.sum(0.5*kt[a:b-1]*(u[a+1:b] - u[a:b-1])**2)
    ET, Etot = energy(610, N - 1), energy(1, N - 1)
    assert abs(ET/Etot - PT) < 5e-3, "T1: channel energy = |amplitude|^2 (the square derived)"
    # T3/T4: survival-integral detection statistics
    det_A = slice(N - 90, N - 5); det_B = slice(5, 90)
    def firstwin(delayB, gamma=0.02, tmax=2600.0, nt=520):
        ts = np.linspace(0, tmax, nt); dt = ts[1] - ts[0]
        rA = np.zeros(nt); rB = np.zeros(nt)
        for i, t in enumerate(ts):
            rA[i] = gamma*np.sum(np.abs(ev(520.0 + t)[det_A])**2)
            rB[i] = gamma*np.sum(np.abs(ev(520.0 + t - delayB)[det_B])**2) if t >= delayB else 0.0
        S = np.exp(-np.cumsum(rA + rB)*dt)
        PA = np.sum(rA*S)*dt; PB = np.sum(rB*S)*dt
        return PA/(PA + PB)
    P_sym = firstwin(0.0)
    assert abs(P_sym - PT) < 0.02, "T3: Born from energy partition (symmetric arrival)"
    P_skew = firstwin(500.0)
    assert P_skew - PT > 0.1, "T4: the residue -- early channel favored beyond Born"
    # T2: exact monochromatic fringes
    om0 = 2*np.sin(k0/2)
    def trans(ktp):
        Nn = 400; kt2 = np.ones(Nn - 1); kt2[120] = 0.28; kt2[240] = 0.28
        kt2[161:201] = ktp
        uu = np.zeros(Nn, complex)
        uu[Nn-1] = np.exp(1j*k0*(Nn-1)); uu[Nn-2] = np.exp(1j*k0*(Nn-2))
        for n in range(Nn - 2, 0, -1):
            uu[n-1] = ((kt2[n] + kt2[n-1] - om0**2)*uu[n] - kt2[n]*uu[n+1])/kt2[n-1]
        M = np.array([[np.exp(1j*k0*5), np.exp(-1j*k0*5)], [np.exp(1j*k0*6), np.exp(-1j*k0*6)]])
        A, B = np.linalg.solve(M, [uu[5], uu[6]])
        return 1.0/abs(A)**2, abs(B)**2/abs(A)**2
    ds, Tv = [], []
    for ktp in np.linspace(1.0, 0.78, 12):
        kp = 2*np.arcsin(min(om0/(2*np.sqrt(ktp)), 0.999))
        T_, R_ = trans(ktp)
        assert abs(T_ + R_ - 1) < 1e-10, "T2: unitarity exact"
        ds.append((kp - k0)*40); Tv.append(T_)
    ds = np.array(ds); Tv = np.array(Tv)
    vis = (Tv.max() - Tv.min())/(Tv.max() + Tv.min())
    assert vis > 0.5, "T2: fringe visibility"
    best = 1e9; bc = 0
    for F in np.linspace(1, 15, 40):
        for p0 in np.linspace(0, np.pi, 80):
            mod = 1/(1 + F*np.sin(p0 + ds)**2)
            Amp = np.sum(Tv*mod)/np.sum(mod**2)
            r = np.sqrt(np.mean((Tv - Amp*mod)**2))
            if r < best:
                best = r; bc = np.corrcoef(Amp*mod, Tv)[0, 1]
    assert bc > 0.95, "T2: Fabry-Perot model correlation"
    print(f"T1: |E/Etot - |c|^2| = {abs(ET/Etot-PT):.1e}; T2: vis={vis:.2f}, corr={bc:.4f};")
    print(f"T3: P_sym={P_sym:.4f} vs Born {PT:.4f}; T4: skew P={P_skew:.4f} (+{P_skew-PT:.2f} residue)")
    print("PASS: the square from energetics, fringes exact, Born from one named premise --")
    print("      and the timing residue registered as the falsifiable divergence.")


if __name__ == "__main__":
    test()
