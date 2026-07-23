"""CHEM-DYN-005 (Modeled): the entrance-corrected bracket restated, the
first quantitative coherence statement (an INFERENCE, labeled), and
catalysis robust on the corrected surface.

(A) THE BRACKET RESTATED: the entrance term on the incoherent (max-rule)
    surface with indicator occupancy weights gives X = 0.525 De (the max
    rule stays entrance-insensitive at its scale, as its shape-insensitivity
    predicted). Restated bracket [0.0791, 0.525] contains the measured
    0.0885. THE HEADLINE: the inferred incoherent admixture
        f = (0.0885 - 0.0791)/(0.525 - 0.0791) = 2.1 percent
    -- the H+H2 crossing runs ~98 percent COHERENT. Stated as an INFERENCE
    from the bracket geometry, not a derivation; the coherence-fraction
    derivation remains the registered open problem.
(B) CATALYSIS ON THE CORRECTED SURFACE: capacity donation as a third
    coherent channel kappa present throughout (the physical pre-complex --
    knob-free: no localization function). Barrier from the pre-complex
    decreases monotonically (0.0791 -> 0.0337 across kappa 0..0.6); the
    surface stays symmetric to machine precision (catalyst returned
    exactly); kappa = 0 reproduces CHEM-DYN-004's 0.0791.
"""
import numpy as np
import importlib.util, os, sys

_here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("moh", os.path.join(_here, "mode_overlap_harness.py"))
H = importlib.util.module_from_spec(spec)
sys.modules["moh"] = H
spec.loader.exec_module(H)

Z = np.array([0., 0., 1.])
D0 = 0.741/0.443


def test():
    rs = np.linspace(1.0, 9.0, 19)
    ts = np.array([abs(H.cross_amplitude(np.array([0., 0., r]), Z, +1, Z, +1, n=64)) for r in rs])
    tA = np.interp(D0, rs, ts)
    that = lambda r: np.interp(r, rs, ts)/tA
    RS = np.linspace(1.05, 8.0, 281)

    def ent(r1, r2, wBC):
        return wBC*that(r1 + r2/2)**2 + (1 - wBC)*that(r2 + r1/2)**2

    def minimax(E):
        best = -np.inf
        for u in np.linspace(-2.5, 2.5, 141):
            m = min(E(r, r - u) for r in RS if 1.05 < (r - u) < 8.0)
            best = max(best, m)
        return best

    # (A) incoherent edge with indicator weights
    def E_inc(r1, r2):
        a, b = that(r1), that(r2)
        return -2*max(a, b) + a*a + b*b + that(r1 + r2)**2 + ent(r1, r2, 1.0 if b > a else 0.0)
    X = minimax(E_inc) - min(E_inc(8.5, r) for r in RS)
    coh = 0.0791
    assert 0.45 < X < 0.60, "incoherent edge ~0.53 (entrance-insensitive at its scale)"
    assert coh < 0.0885 < X, "restated bracket [0.0791, X] contains the measured ratio"
    f = (0.0885 - coh)/(X - coh)
    assert 0.0 < f < 0.2, "inferred incoherent admixture small: predominantly coherent crossing"
    # (B) catalysis with the pre-complex third channel
    def barrier_cat(k):
        def E(r1, r2):
            a, b = that(r1), that(r2)
            return (-2*np.sqrt(a*a + b*b + k*k) + a*a + b*b + that(r1 + r2)**2
                    + ent(r1, r2, b*b/(a*a + b*b)))
        s = minimax(E)
        reac = min(E(8.5, r) for r in RS)
        prod = min(E(r, 8.5) for r in RS)
        assert abs(reac - prod) < 1e-12, "surface exactly symmetric: catalyst returned"
        return s - reac
    ks = (0.0, 0.15, 0.3, 0.45, 0.6)
    bs = [barrier_cat(k) for k in ks]
    assert abs(bs[0] - 0.0791) < 0.002, "kappa = 0 reproduces CHEM-DYN-004"
    assert all(bs[i] > bs[i + 1] for i in range(len(bs) - 1)), "capacity donation lowers the barrier monotonically"
    print(f"(A) incoherent edge X = {X:.4f}; bracket [0.0791, {X:.3f}] contains 0.0885")
    print(f"    INFERRED incoherent admixture f = {f:.3f} ({f:.1%}) -- the crossing runs ~98% coherent")
    print(f"    (an inference from bracket geometry; the derivation remains the registered open problem)")
    print(f"(B) catalysis on the corrected surface: {[round(b,4) for b in bs]} across kappa {ks}")
    print(f"    monotone; catalyst returned to machine precision; kappa=0 consistent with CHEM-DYN-004")
    print("PASS: the bracket is restated, the coherence fraction has its first number, and the")
    print("      catalysis mechanism survives the entrance correction intact.")


if __name__ == "__main__":
    test()
