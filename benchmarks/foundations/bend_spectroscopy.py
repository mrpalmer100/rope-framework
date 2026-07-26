"""FND-MATTER-011 (Modeled): BEND SPECTROSCOPY -- THE QUADRATIC GUESS
REFUTED, AND THE MEASURED LAW REGISTERED IN ITS PLACE. The conditioning
map's curvature term (kappa^2, a named choice in FND-MATTER-009) was
put to the engine with a boundary-free instrument, and the engine said
no: the bend cost is real, positive, and SOFTER than quadratic.

THE INSTRUMENT (nineteenth catch first: clamped-arc spectroscopy at
1e-4 signal levels is boundary-contaminated -- ends of a curved arc
differ geometrically from a straight chain's ends, polluting both the
kappa-scaling and extensivity; the fix is the closed loop): a
pre-tensioned CIRCLE (uniform kappa = 2 pi / L, no ends, dead loads
holding equilibrium -- constant forces do not enter the Hessian)
against a PERIODIC straight chain of equal length, bond count, and
tension, zero modes matched and dropped on both sides. Geometric
stiffness (T/d transverse to each stretched bond) carries the
curvature into the spectrum through the rotation of bond frames.

THE MEASUREMENT:
  SIGN: positive at every size -- bends COST zero-point energy.
  THE REFUTATION: if dE = c kappa^2 L, then c must be size-independent;
    measured c drifts 66 percent across L = 100..400 (0.0055 -> 0.0111,
    monotone). The quadratic law FAILS its 5 percent bar by an order
    of magnitude and is refuted as the leading form.
  THE MEASURED SCALING: dE tracks L^(-1/2) across a 4x size range
    (ratio 0.50 for L 100 -> 400), i.e. with L = 2 pi / kappa the
    effective exponent of dE vs kappa drifts through ~1.4-1.6 --
    consistent with an approach to kappa^(3/2), NOT kappa^2.
  THE THEORY DEBT, registered: the mechanism of the anomalous exponent
    (transverse-longitudinal mixing near k ~ kappa is the suspect) is
    UNIDENTIFIED; deriving it is the entry's named sequel.

CONSEQUENCE: the two-term mass model's curvature term is corrected in
kind -- the contact term is derived (FND-MATTER-010), the curvature
term is now MEASURED-but-unexplained, and the table's fractions await
a rerun under the measured law (the lever's existence is unaffected:
it rests on FND-MATTER-008's saturation, independently established).
"""
import numpy as np


def zp_loop(Nn, circle, k=1.0, a0=0.5, d=1.0):
    if circle:
        R = Nn*d/(2*np.pi)
        th = np.arange(Nn)*2*np.pi/Nn
        pos = np.stack([R*np.cos(th), R*np.sin(th)], axis=1)
    else:
        pos = np.stack([np.arange(Nn)*d, np.zeros(Nn)], axis=1)
    H = np.zeros((2*Nn, 2*Nn))
    for i in range(Nn):
        j = (i + 1) % Nn
        rij = np.array([d, 0.0]) if (not circle and j == 0) else pos[j] - pos[i]
        dist = np.linalg.norm(rij); nh = rij/dist
        Tn = k*(dist - a0)
        Kb = k*np.outer(nh, nh) + (Tn/dist)*(np.eye(2) - np.outer(nh, nh))
        for (a, b, s) in ((i, i, 1), (j, j, 1), (i, j, -1), (j, i, -1)):
            H[2*a:2*a+2, 2*b:2*b+2] += s*Kb
    w2 = np.sort(np.linalg.eigvalsh(H))
    assert w2[0] > -1e-8, "stability under tension"
    return 0.5*np.sum(np.sqrt(np.maximum(w2[3:], 0)))


def test():
    sizes = (100, 200, 400)
    dEs = []
    for Nn in sizes:
        dE = zp_loop(Nn, True) - zp_loop(Nn, False)
        assert dE > 0, "sign: bends cost zero-point energy"
        dEs.append(dE)
    cs = [dEs[i]/((2*np.pi/sizes[i])**2*sizes[i]) for i in range(3)]
    spread = (max(cs) - min(cs))/np.mean(cs)
    assert spread > 0.30, \
        "THE REFUTATION, tracked: the quadratic law fails -- if this passes 5%, the map changed"
    r = dEs[2]/dEs[0]
    assert 0.38 < r < 0.62, "the measured scaling: dE ~ L^(-1/2) across a 4x range"
    print(f"sign positive; kappa^2 coefficient spread = {spread*100:.0f}% (refuted);")
    print(f"dE(L=400)/dE(L=100) = {r:.3f} [L^-1/2 predicts 0.500]")
    print("PASS: the quadratic guess refuted, the measured law registered, the mechanism")
    print("      registered as theory debt -- the map is corrected by its own instrument.")


if __name__ == "__main__":
    test()
