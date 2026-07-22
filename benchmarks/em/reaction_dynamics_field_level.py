"""CHEM-DYN-002 (Modeled): the activation barrier survives the DERIVED
functional -- field-level confirmation of CHEM-DYN-001.

THE QUESTION (pre-committed): CHEM-DYN-001 derived barrier existence using
exponential-hopping ANSATZ amplitudes t = e^{-x}. Does the barrier survive
when the amplitudes are COMPUTED from the frozen mode-overlap functional
(EM-RECON-006, mode_overlap_harness.py) -- real grid integrals of the
declared mode profiles -- with everything else inherited unchanged?

THE ANSWER -- yes, and the ansatz was faithful:
(B1) EXISTENCE: coherent-rule barrier = +0.0122 De with field amplitudes
     (ansatz: 0.0142). Positive across +-20% anchor jitter (0.006-0.022 De).
(B2) SYMMETRY: homonuclear saddle exactly symmetric, |r1 - r2| = 0.
(B3) FIDELITY: field/ansatz barrier ratio 0.86 (within the factor-5 bar);
     below the measured H+H2 ratio 0.0885 as the coherent lower edge must be.
     The field shape's heavier-than-exponential tail slightly LOWERS the
     barrier; structure unchanged. Incoherent limit 0.502 (ansatz 0.50).
     The parameter-free bracket [0.0122, 0.502] still contains 0.0885;
     log-midpoint 0.078 (12% from measured) recorded as OBSERVATION ONLY.
(B4) HAMMOND, field-level: weakened partner (0.6x) puts the saddle with the
     forming strong bond LONG and the breaking weak bond unstretched --
     early TS for the exothermic direction, now from computed amplitudes.

INHERITED STRUCTURE (declared, per the harness's located derivation
boundary): the t^2 pair repulsion and third-body contact are CHEM-DYN-001's
CORE-CONDITIONAL structure -- the repulsive core is not fixed at
superposition order. The NEW, derived ingredient is the amplitude SHAPE
t(r) = |A(r)| from the frozen functional. Nothing tuned to any target.

WHAT REMAINS OPEN (unchanged): the coherence fraction (where between the
brackets the physical system sits) and true kinetics -- rates, transition
dynamics, tunneling -- the hbar-layer (FND-BOUND-001).
"""
import numpy as np
import importlib.util, os, sys

_here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("moh", os.path.join(_here, "mode_overlap_harness.py"))
H = importlib.util.module_from_spec(spec)
sys.modules["moh"] = H
spec.loader.exec_module(H)

Z = np.array([0., 0., 1.])
D0_XI = 0.741/0.443     # corpus anchor d0 in xi units


def amp_table(n=64, npts=19):
    rs = np.linspace(1.0, 9.0, npts)
    ts = np.array([abs(H.cross_amplitude(np.array([0., 0., r]), Z, +1, Z, +1, n=n))
                   for r in rs])
    return rs, ts


def test():
    rs, ts = amp_table()
    def that_at(anchor):
        tA = np.interp(anchor, rs, ts)
        return lambda r: np.interp(r, rs, ts)/tA
    that = that_at(D0_XI)
    RS = np.linspace(1.05, 8.0, 281)

    def E_coh(t, r1, r2):
        a, b = t(r1), t(r2)
        return -2*np.sqrt(a*a + b*b) + a*a + b*b + t(r1 + r2)**2

    def endpoint(E):
        return min(E(r, 8.5) for r in RS)

    def minimax(E):
        best, loc = -np.inf, None
        for u in np.linspace(-2.5, 2.5, 141):
            vals = [(E(r, r - u), r, r - u) for r in RS if 1.05 < (r - u) < 8.0]
            m = min(vals)
            if m[0] > best:
                best, loc = m[0], (m[1], m[2])
        return best, loc

    Ec = lambda a, b: E_coh(that, a, b)
    barrier = minimax(Ec)[0] - endpoint(Ec)
    _, loc = minimax(Ec)
    # B1: existence
    assert barrier > 0, f"field-level coherent barrier positive: {barrier:.4f} De"
    # B2: symmetry
    assert abs(loc[0] - loc[1]) < 0.05, "homonuclear saddle symmetric"
    # B3: fidelity to the ansatz and position vs data
    assert 0.2 < barrier/0.0142 < 5.0, "within factor 5 of the ansatz value"
    assert barrier < 0.0885, "coherent limit stays below the measured ratio (lower bracket edge)"
    def E_inc(r1, r2):
        a, b = that(r1), that(r2)
        return -2*max(a, b) + a*a + b*b + that(r1 + r2)**2
    b_inc = minimax(E_inc)[0] - endpoint(E_inc)
    assert 0.4 < b_inc < 0.6, "incoherent limit ~0.50 De (shape-insensitive, as expected)"
    assert barrier < 0.0885 < b_inc, "parameter-free bracket still contains the measured ratio"
    # B4: Hammond with computed amplitudes
    def E_het(r1, r2, rr=0.6):
        a, b = that(r1), rr*that(r2)
        return -2*np.sqrt(a*a + b*b) + a*a + rr*that(r2)**2 + that(r1 + r2)**2
    _, loch = minimax(lambda x, y: E_het(x, y))
    assert loch[0] > D0_XI + 1.0 and loch[1] < D0_XI + 0.3, \
        "early TS: forming strong bond long, breaking weak bond unstretched"
    # robustness: anchor jitter +-20%
    for dj in (D0_XI*0.8, D0_XI*1.2):
        tj = that_at(dj)
        Ej = lambda a, b: E_coh(tj, a, b)
        bj = minimax(Ej)[0] - endpoint(Ej)
        assert bj > 0, f"barrier sign robust at d0/xi = {dj:.2f}"
    mid = np.sqrt(barrier*b_inc)
    print(f"B1 field-level barrier = {barrier:.4f} De (ansatz 0.0142) -- THE ANSATZ SURVIVES THE FUNCTIONAL")
    print(f"B2 saddle symmetric at ({loc[0]:.2f},{loc[1]:.2f}) xi")
    print(f"B3 bracket [{barrier:.4f}, {b_inc:.3f}] contains measured 0.0885; log-mid {mid:.3f} (observation)")
    print(f"B4 Hammond field-level: saddle ({loch[0]:.2f}, {loch[1]:.2f}) xi -- early TS")
    print(f"robust: positive barrier at d0/xi anchor +-20%")
    print("PASS: barrier existence is a property of the derived functional, not the ansatz.")


if __name__ == "__main__":
    test()
