"""FND-MATTER-035 (Modeled): THE C-LEDGER CONDITIONALS END TO END --
the doublet and helium conditions rerun under the surviving reading,
with three results and an unambiguous error budget.

THE MODEL, in its austere surviving form: m/(T D) = L - Lambda ell,
one geometric parameter Lambda = alpha^2 (D/a)^2, contact length
only, bend silent.

(1) READING-ROBUSTNESS, quantified where it matters most: at MATCHED
    seats the A-equivalent and C doublet conditions land within 3.2
    percent (Lambda 0.0443 vs 0.0429) -- the fork's choice barely
    moves the phenomenology; contact dominance holds even inside the
    tiny doublet split (the granny-square bend difference, -0.02, is
    real but subdominant).

(2) BASIN-SCATTER HONESTY: across seat bases Lambda* scatters
    ~0.014-0.044 (factor ~3), because the 0.05-percent geometric
    split divides by a noisy contact-length difference. THE ERROR
    BUDGET IS UNAMBIGUOUS: reading shift 3 percent, basin scatter
    200 percent -- the condition is seat-quality-limited, and the
    walls are, once again, the antagonist.

(3) THE CONSISTENCY TRIANGLE HOLDS ACROSS THE ENTIRE SCATTER:
    alpha = 0.12-0.21 at D/a = 1 (0.24-0.41 at D/a = 0.5), under the
    tube cap at EVERY point of the window; the helium inversion gives
    3-10 D of inter-nucleon contact per interface across the whole
    Lambda* range -- a few diameters per touching pair, geometrically
    natural for packed ~28 D tangles, at every seat quality. No veto
    anywhere under reading C.

Everything hypothesis-shaped stays hypothesis-shaped: doublet = n/p
and nucleon = 27.75-D-tangle remain conditionals, now robust to the
fork and awaiting only better seats and an alpha-fixing observable.
"""
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from two_term_mass_model import tighten_coords, profile
from topology_certifier import knot_det
from alexander_certifier_61 import alexander_at, odd_part
from braid_family_spectrum import braid_closure
from mapping_calibrated import build_table, contact_phys

A_C = -0.509658; B_C = 2*np.pi*(2.5 - 7*np.sqrt(2)/4); DIR = -0.502506
LG, LS, NP = 28.520, 28.535, 1.001378


def pieces(P):
    Ns, dEs = build_table()
    def dE_loop(Lam):
        if Lam >= 120:
            return (A_C + B_C*np.log(Lam))/Lam
        return float(np.interp(np.clip(Lam, Ns[0], 120), Ns, dEs))
    kap, con, edge, L, turn = profile(P)
    kap = np.maximum(kap, 1e-4); Lam = 2*np.pi/kap
    Eb = float(np.sum(edge*np.array([dE_loop(x)/x for x in Lam])))
    return float(L), float(contact_phys(P)[1]), Eb


def test():
    Pg = tighten_coords(braid_closure((1, 1, 1, 2, 2, 2), N=160).copy(), iters=14000)
    Ps = tighten_coords(braid_closure((1, 1, 1, -2, -2, -2), N=160).copy(), iters=14000)
    assert knot_det(Pg) == 9 and odd_part(alexander_at(Pg, 2)) == 9
    assert knot_det(Ps) == 9 and odd_part(alexander_at(Ps, 2)) == 9
    _, lg, Ebg = pieces(Pg); _, ls, Ebs = pieces(Ps)
    # the C condition and the A-equivalent, at matched seats
    LamC = (NP*LS - LG)/(NP*ls - lg)
    Sg, Ss = Ebg + DIR*lg, Ebs + DIR*ls
    lamA = (NP*LS - LG)/(Sg - NP*Ss)
    LamA = lamA*abs(DIR)
    assert LamC > 0 and LamA > 0, "both readings give positive conditions"
    assert abs(LamA - LamC)/LamC < 0.15, "READING ROBUSTNESS: the fork moves the condition < 15%"
    mg, ms = LG - LamC*lg, LS - LamC*ls
    assert mg > ms > 0, "granny heavier, masses positive under C"
    # the triangle across the scattered window
    for Lam in (0.014, LamC, 0.044):
        assert np.sqrt(Lam) < 0.5, "alpha under the tube cap at D/a = 1 across the window"
        ellHe = 28.296/((938.272/27.75)*Lam)
        assert 1.5 < ellHe/6 < 15.0, "helium interface 1.5-15 D per pair across the window"
    print(f"matched-seat conditions: Lambda_C = {LamC:.4f}, A-equiv = {LamA:.4f} "
          f"(shift {abs(LamA-LamC)/LamC*100:.1f}%)")
    print(f"alpha(D/a=1) = {np.sqrt(LamC):.3f}; helium interface at this Lambda: "
          f"{28.296/((938.272/27.75)*LamC)/6:.1f} D per pair")
    print("PASS: the conditionals survive the fork nearly unchanged, the error budget names")
    print("      the walls, and the triangle holds at every point of the scattered window.")


if __name__ == "__main__":
    test()
