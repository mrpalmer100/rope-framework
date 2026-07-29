"""QGATE-004 (Modeled): THE TUBE CENSUS -- UNDERDETERMINED BY ONE
RATIO, WITH THE SOLIDITY GATE PASSED. Does the corpus's own bundle
machinery independently deliver the n_t ~ 111 that QGATE-003's
uniform demand predicts?

THE MACHINERY'S ANSWER: a one-parameter family, not a number --
n_t = f_c (D/w)^2 with f_c = 0.309 (FND-MATTER-038). A registry-wide
search finds NO independent constraint on the constituent width w or
the ratio D/w: n_t = 111 is UNCONFIRMED AND UNFALSIFIED, the demanded
point (D/w = 19.0, w ~ 1.5e-3 fm) sitting inside the allowed family
and conflicting with nothing registered (ambient Lorentz bound
a <= 0.1 fm untouched).

THE CENSUS'S REAL FINDING -- A KILL LINE WAS LIVE AND GOT CLEARED:
FND-STRAND-004's solidity criterion (bundles solid iff internal
surface gap <~ 1.5 sigma) is n_t-INDEPENDENT at coverage onset: the
gap is w(1/sqrt(f_c) - 1), fixed by f_c alone. Solidity therefore
fails for f_c < 1/(1+1.5)^2 = 0.160 -- INSIDE the window
[0.073, 0.348] that FND-MATTER-037 demanded. Half the allowed window
was lethal to the internal-bundle picture, and the percolation
measurement (0.309) landed in the surviving half: gap = 0.80 sigma,
solid, headroom 1.88. Two thresholds measured in different sectors
for different reasons cohere where they could have collided.

THE BOTTLENECK, NAMED: one quantity -- the constituent width w.
Candidate routes already in the registry: the strand-engine sigma
physics (FND-STRAND sector); the vacuum-tension chain (EM-RECON-014's
field-strain calibration and EM-RECON-015's Sigma ~ 1e25 J/m^3, which
tie field normalization to strand density); or any second observable
demanding the same D/w.
"""
import numpy as np


def test():
    fc = 0.309
    # the family and the demanded point (QGATE-003)
    n_demand = 111.0
    Dw = np.sqrt(n_demand/fc)
    assert 18 < Dw < 20, "demand locates at D/w ~ 19 in the family"
    D = 0.8/27.75; w = D/Dw
    assert w < 0.1, "w far below the ambient Lorentz bound: no conflict"
    # THE SOLIDITY CROSS-CHECK: n_t-independent at onset
    gap = 1/np.sqrt(fc) - 1
    assert gap < 1.5, "SOLIDITY GATE PASSED: onset-tube gap 0.80 sigma < 1.5 sigma"
    assert 1.7 < 1.5/gap < 2.1, "headroom factor ~1.9 (nontrivial, not saturated)"
    # the kill line was LIVE inside 037's demanded window
    fc_kill = 1/(1 + 1.5)**2
    assert 0.073 < fc_kill < 0.348, "the kill line sits INSIDE the demanded window [0.073, 0.348]"
    assert fc > fc_kill, "the percolation measurement landed in the SURVIVING half"
    print(f"family: n_t = {fc} (D/w)^2; demand -> D/w = {Dw:.1f}, w = {w*1e3:.2f}e-3 fm (no conflicts)")
    print(f"solidity gate: gap = {gap:.3f} sigma < 1.5 (headroom {1.5/gap:.2f}); kill line f_c = {fc_kill:.3f}")
    print(f"measured f_c = {fc}: the surviving half of a window that was half-lethal")
    print("PASS: underdetermined by exactly one ratio (w, the named bottleneck); unfalsified;")
    print("      and the one live cross-check -- solidity vs percolation -- coheres nontrivially.")


if __name__ == "__main__":
    test()
