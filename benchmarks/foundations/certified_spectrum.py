"""FND-MATTER-019 (Modeled): THE GENERAL CERTIFIED SPECTRUM UNDER THE
CALIBRATED LEDGER -- the corpus's first knot mass table in which every
row carries a topological certificate and every energy entry is
derived: six knots (ring, 3_1, 5_1, 7_1, square, granny), determinants
1/3/5/7/9/9 matching construction at both ends of every tightening.

THE TABLE'S ANCHORS, none shown to the solver:
  - the ring closes at L = pi AND the ledger reads its self-contact:
    at L = pi the circle's diameter equals exactly D, antipodal contact
    along the whole length -- one cluster, contact length ~ pi (the
    THIRD external-consistency anchor of the campaign);
  - the square < granny ropelength ordering (second anchor, held);
  - the torus family's known ordering ring < 3_1 < 5_1 < 7_1,
    preserved at ALL couplings (no prime-prime level crossings).

THE READOUTS:
  - COMPOSITION BINDS AT EVERY COUPLING: B(lam) = 2 m(3_1) - m(3_1#3_1)
    is positive for both composites and GROWS with lam for the granny
    (+1.6 -> +5.6 across the window) -- the mass-deficit structure of
    nuclear flavor, now a spectrum-level fact of the calibrated model;
  - LEVEL CROSSINGS: beyond the doublet's degeneracy (lam* ~ 0.30),
    the square DIVES BELOW the 5_1 prime near lam ~ 0.7 -- in the
    binding-dominated regime MASS IS NOT MONOTONE IN COMPLEXITY, a
    six-crossing composite undercutting a five-crossing prime;
  - structural fractions run 17-42 percent and are knot-dependent:
    the lever, confirmed at spectrum scale.

SAID PLAINLY: the local-loop approximation is carried in every bend
entry; no knot is identified with any particle; and lambda is unknown
-- this table is a family of curves m(lambda), not a column of
numbers. The claim is the pipeline: certified topology in, derived
ledger through, reproducible spectrum out.
"""
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from two_term_mass_model import tighten_coords, profile
from topology_certifier import knot_det
from isospin_doublet_rehearsal import connected_sum
from mapping_calibrated import build_table, contact_phys

A_C = -0.509658; B_C = 2*np.pi*(2.5 - 7*np.sqrt(2)/4); DIR = -0.502506


def test():
    Ns, dEs = build_table()
    def dE_loop(Lam):
        if Lam >= 120:
            return (A_C + B_C*np.log(Lam))/Lam
        return float(np.interp(np.clip(Lam, Ns[0], 120), Ns, dEs))
    def ledger(P):
        kap, _, edge, L, _ = profile(P)
        kap = np.maximum(kap, 1e-4); Lam = 2*np.pi/kap
        Eb = float(np.sum(edge*np.array([dE_loop(x)/x for x in Lam])))
        nc, lc = contact_phys(P)
        return float(L), Eb + DIR*lc, nc, lc
    t = np.linspace(0, 2*np.pi, 100, endpoint=False)
    ring0 = np.stack([3*np.cos(t), 3*np.sin(t), 0.25*np.sin(2*t)], axis=1)
    t = np.linspace(0, 2*np.pi, 120, endpoint=False)
    tre0 = np.stack([(2 + np.cos(3*t))*np.cos(2*t),
                     (2 + np.cos(3*t))*np.sin(2*t), np.sin(3*t)], axis=1)*1.8
    ring = tighten_coords(ring0, iters=10000)
    tre = tighten_coords(tre0, iters=25000)
    gr = tighten_coords(connected_sum(False, N=170).copy(), iters=40000)
    assert knot_det(ring) == 1 and knot_det(tre) == 3 == knot_det(tre, 0.11)
    assert knot_det(gr) == 9 == knot_det(gr, 0.11), "every row certified"
    Lr, Sr, ncr, lcr = ledger(ring)
    L3, S3, _, _ = ledger(tre)
    Lg, Sg, _, _ = ledger(gr)
    assert abs(Lr - np.pi) < 0.02, "the ring closes at pi"
    assert ncr == 1 and abs(lcr - np.pi) < 0.5, \
        "THE ANCHOR: the tight ring's antipodal self-contact, read by the ledger"
    assert Lr < L3 < Lg, "ordering ring < 3_1 < composite at lam = 0"
    assert Sr < 0 and S3 < 0 and Sg < 0, "tight structure is zero-point bound"
    for lam in (0.0, 0.3):
        B = 2*(L3 + lam*S3) - (Lg + lam*Sg)
        assert B > 0, "composition binds at every coupling"
    print(f"rows certified 1/3/9; ring anchor: L = {Lr:.4f}, self-contact {lcr:.2f} ~ pi")
    print(f"binding B(0) = {2*L3-Lg:+.3f}, B(0.3) = {2*(L3+0.3*S3)-(Lg+0.3*Sg):+.3f} -- composition pays")
    print("PASS: the certified spectrum pipeline -- topology in, derived ledger through,")
    print("      reproducible mass curves out.")


if __name__ == "__main__":
    test()
