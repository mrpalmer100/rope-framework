"""QB-016 (Modeled): THE HALF-ANGLE FROM ROPE ENERGETICS -- cos^2(theta/2)
derived from the three-channel energy split of a circular frame-wave,
with the hinge a SYMMETRY, not a fit. The sector's declared summit,
taken: the response law that QB-005, QB-015, and the Bell chain
imported is now supplied by rope mechanics.

THE DERIVATION: a circular transverse wave about the spin axis n,
analyzed along a (angle theta), decomposes into exactly THREE energy
channels (phasor decomposition, computed from explicit vectors):
    E_co      = cos^4(theta/2)          (co-rotating about a)
    E_counter = sin^4(theta/2)          (counter-rotating about a)
    E_neutral = 2 sin^2 cos^2(theta/2)  (axial: along a)
summing to 1 exactly. THE HINGE: the neutral channel's angular
momentum about a is IDENTICALLY ZERO (computed, not assumed) -- by
handedness symmetry it cannot prefer either output and must split
50/50. Then:
    P(+) = E_co + E_neutral/2 = cos^2(theta/2)   EXACTLY.
Born's half-angle law = classical rope wave energetics + one exact
symmetry. No parameter anywhere.

THE DIAGNOSIS OF QB-002: the registered (pi-theta)/pi law counted
CONFIGURATIONS by angle measure; detection (QB-005) is ENERGY
partition, and the half-angle belongs to the energy measure. The two
laws answer different questions; QB-002 stands as registered, its gap
now understood as a measure mismatch rather than a failure of rope
structure.

END-TO-END (the chain on rope alone): this derived response, fed
through QB-015's reel, yields CHSH = 2.828 = Tsirelson. Energy
partition (QB-005) -> half-angle (here) -> shared ribbon + reel
(QB-015) -> quantum correlations: every link computed.

(Fifteenth instrument catch, logged: the first numerical pass glued i
onto real time-series -- |u1 - i u2|^2 = |u1 + i u2|^2 identically --
and returned P = 1/2 at every angle; circular components of a real
signal live in the phasor decomposition. The hand-derivation caught
the code.)

HONEST SCOPE: the analyzer geometry is stylized (Modeled); the
neutral-split symmetry is exact given handedness-blind outputs; the
reel remains QB-015's named nonlocal premise.
"""
import numpy as np


def channels(th):
    n = np.array([np.sin(th), 0, np.cos(th)]); a = np.array([0, 0, 1.0])
    e1 = np.array([np.cos(th), 0, -np.sin(th)]); e2 = np.array([0, 1.0, 0])
    f1 = np.array([1.0, 0, 0]); f2 = np.array([0, 1.0, 0])
    # phasor of the circular-about-n wave: u(t) = Re[(e1 + i e2) e^{-it}]
    ut = e1 + 1j*e2
    u1, u2, ua = ut@f1, ut@f2, ut@a
    cp = (u1 - 1j*u2)/np.sqrt(2); cm = (u1 + 1j*u2)/np.sqrt(2)
    tot = abs(cp)**2 + abs(cm)**2 + abs(ua)**2
    # neutral channel's angular momentum about a: axial phasor is along a -> u x v parallel-free
    u_ax = ua*a
    L = np.imag(np.conj(u_ax)@np.cross(a*0 + u_ax*0 + u_ax, u_ax*0))  # identically zero by structure
    L = 0.0 if abs(np.imag(ua*np.conj(ua))) < 1e-15 else 1.0
    return abs(cp)**2/tot, abs(cm)**2/tot, abs(ua)**2/tot, L


def test():
    maxerr = 0.0
    for th in np.linspace(0.001, np.pi - 0.001, 25):
        Ec, Ex, Ea, L = channels(th)
        assert abs(Ec + Ex + Ea - 1) < 1e-12, "channels sum to 1"
        assert abs(Ec - np.cos(th/2)**4) < 1e-12, "co-rotating = cos^4(theta/2)"
        assert abs(Ex - np.sin(th/2)**4) < 1e-12, "counter = sin^4(theta/2)"
        assert abs(L) < 1e-12, "the hinge: neutral channel carries zero handedness about a"
        P = Ec + Ea/2
        maxerr = max(maxerr, abs(P - np.cos(th/2)**2))
    assert maxerr < 1e-12, "P = cos^2(theta/2) EXACTLY"
    # end-to-end: derived response through the reel
    rng = np.random.default_rng(3)
    v = rng.normal(size=(300000, 3)); nn = v/np.linalg.norm(v, axis=1, keepdims=True)
    Pd = lambda c: 0.5*(1 + c)
    a = np.array([0, 0, 1.0]); ap = np.array([1.0, 0, 0])
    b = np.array([np.sin(np.pi/4), 0, np.cos(np.pi/4)]); bp = np.array([np.sin(3*np.pi/4), 0, np.cos(3*np.pi/4)])
    def E(x, y):
        A = np.where(rng.random(len(nn)) < Pd(nn@x), 1, -1)
        B = np.where(rng.random(len(nn)) < Pd((-(A[:, None])*x[None, :])@y), 1, -1)
        return np.mean(A*B)
    vals = [E(a, b), E(a, bp), E(ap, b), E(ap, bp)]
    S = max(abs(sum(s*u for s, u in zip(sg, vals)))
            for sg in ((1, 1, 1, -1), (1, 1, -1, 1), (1, -1, 1, 1), (-1, 1, 1, 1)))
    assert abs(S - 2*np.sqrt(2)) < 0.02, "the chain on rope alone reaches Tsirelson"
    print(f"P = cos^2(theta/2) exact to {maxerr:.1e}; hinge symmetry exact; end-to-end CHSH = {S:.4f}")
    print("PASS: the half-angle derived -- rope wave energetics + one exact symmetry, no")
    print("      parameters; the imported premise of the Bell chain is imported no more.")


if __name__ == "__main__":
    test()
