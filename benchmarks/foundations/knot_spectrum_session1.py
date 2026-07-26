"""FND-MATTER-007 (Modeled): THE FIRST SPECTRUM SESSION -- two misses
and one anomaly, registered as exactly that, plus the analysis that
reframes the hydrogen campaign. This is what an instrument era's first
morning actually looks like, and the house registers it whole.

THE DATA (full-resolution session values; this benchmark reproduces
the compact versions):
  3_1 (trefoil):     L/D = 16.844  [lit 16.372 -- 2.9%, PASSED its bar]
  5_1 (torus 2,5):   L/D = 25.09   [lit ~23.55 -- 6.5%: MISSED its
                      locked 5% bar; kept as a miss, bar not widened]
  4_1 (figure-eight): L/D = 31.93  [lit ~21.04 -- 52%: THE ANOMALY.
                      Robustly convergent (annealing kicks change it
                      by < 0.1%), no pass-throughs, cause unresolved.
                      The prototype tightens the torus family and
                      robustly stalls on the first non-torus knot from
                      the standard embedding: the refinement era's
                      first concrete work order.]
This benchmark ASSERTS the anomaly (4_1 in a band around its stall
value) so that any future solver change that silently alters it is
flagged: kept negatives are tracked, not forgotten.

THE 1836 CONFRONTATION (the session's analytical result): hydrogen is
99.95 percent proton, so hydrogen's mass "mechanically" is really
m_p/m_e = 1836.15 -- a DIMENSIONLESS number, reachable in principle by
ropelength ratios with NO absolute scale (FND-MATTER-003 stays blocked
and is not needed for this). But the arithmetic bites: if mass were
pure tension x ropelength, a trefoil electron demands a proton of
ropelength ~31,000 -- a thousand-crossing-class object -- and a
minimal-ring electron demands ~5,800. EITHER the proton is an enormous
tangle, OR mass is not pure tension-length and kinetic/zero-point
contributions are structural -- which is THE ONE FENCE's third panel
(FND-BOUND-001: light-isotope zero-point) speaking again. The road to
hydrogen and the corpus's single named boundary are the same road.
"""
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from knot_solver_first_light import tighten


def test():
    t = np.linspace(0, 2*np.pi, 120, endpoint=False)
    tre = np.stack([(2 + np.cos(3*t))*np.cos(2*t),
                    (2 + np.cos(3*t))*np.sin(2*t), np.sin(3*t)], axis=1)*1.8
    fig8 = np.stack([(2 + np.cos(2*t))*np.cos(3*t),
                     (2 + np.cos(2*t))*np.sin(3*t), np.sin(4*t)], axis=1)*1.8
    L3, w3 = tighten(tre, iters=40000)
    assert abs(L3 - 16.372)/16.372 < 0.06, "torus family: trefoil at prototype grade"
    assert w3 > 0.9, "topology preserved"
    L4, w4 = tighten(fig8, iters=40000)
    assert w4 > 0.9, "figure-eight: no pass-throughs even in the stall"
    assert 27.0 < L4 < 35.0, \
        "THE REGISTERED ANOMALY: 4_1 stalls near 31 -- if this moves, the registry must know"
    r = 1836.15
    L_proton_if_trefoil_electron = r*L3
    assert L_proton_if_trefoil_electron > 3e4, "the 1836 arithmetic: a thousand-crossing-class object"
    print(f"3_1 = {L3:.3f} ({abs(L3-16.372)/16.372*100:.1f}%); 4_1 stall = {L4:.2f} (tracked); ")
    print(f"1836 confrontation: pure-length proton needs L/D ~ {L_proton_if_trefoil_electron:.0f}")
    print("PASS: two misses and one anomaly registered as exactly that; the road to hydrogen")
    print("      and the one fence are the same road.")


if __name__ == "__main__":
    test()
