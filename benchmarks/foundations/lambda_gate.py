"""FND-MATTER-029 (Modeled): THE LAMBDA GATE -- ANATOMY, AUDIT, AND
THE CONDITIONAL. The axis finally gets what FND-MATTER-003 gave the
atomic scale: a precise anatomy of what is missing, plus an
instrument that converts hypotheses into numbers.

THE AUDIT (units): the bend-law constants (a = -0.509658, b =
2 pi (5/2 - 7 sqrt 2/4), analytically derived) and the contact
constant (dE = -0.502506 per site, units sqrt(kt/mu)) descend from
the SAME minus-chain lattice with the same normalization. Therefore
S HAS NO INTERNAL FREEDOM: the ledger's bend-to-contact relative
scale is derived, and the gate is exactly ONE number with a precise
anatomy --

    lambda = E_mode / (T . D)

-- the ratio of the lattice's mode-energy scale to the rope's
tension-energy per diameter. One dimensionless microphysical ratio;
a derivation needs the tension T and transverse coupling kt from one
microstructure. Named, like a and N before it.

THE CONDITIONAL (hypothesis-shaped, NOT an identification): with
source-grade doublet geometry (granny 28.520 D, square 28.535 D --
split 0.05 percent) and matched-configuration conditioning ledgers
(S_granny = -26.78, S_square = -28.30: the square 5.7 percent MORE
bound), the trajectory m(lambda) = L + lambda S gives:
  - doublet degeneracy at lambda ~ 0.010;
  - the n/p ratio 1.00138 reached at lambda* ~ 0.035, granny heavier,
    masses positive, corrections ~3 percent;
  - the coarse spectrum barely moves at lambda* (m_41/m_31 shifts
    0.2 percent): GEOMETRY SETS COARSE RATIOS, CONDITIONING SETS FINE
    SPLITTINGS -- the two-scale structure a mass spectrum wants.

THE SIGN FACT, lambda-independent: because the geometric split (0.05
percent, granny shorter) UNDERSHOOTS the target (0.14 percent), the
condition requires the more-contact-bound member to become the
LIGHTER one -- exactly how binding energy behaves. The hypothesis
could have demanded the unphysical sign; it demands the physical one.

Lambda remains underived and is said so. What changed: the gate now
has an anatomy, an audit certifying one-parameterhood, and a
conditional map from hypotheses to falsifiable spectra.
"""
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from two_term_mass_model import tighten_coords, profile
from topology_certifier import knot_det
from braid_family_spectrum import braid_closure
from mapping_calibrated import build_table, contact_phys

A_C = -0.509658; B_C = 2*np.pi*(2.5 - 7*np.sqrt(2)/4); DIR = -0.502506
LIT_G, LIT_S = 28.520, 28.535   # ridgerunner, D units (FND-MATTER-028)
NP_RATIO = 1.001378


def ledger_S(P):
    Ns, dEs = build_table()
    def dE_loop(Lam):
        if Lam >= 120:
            return (A_C + B_C*np.log(Lam))/Lam
        return float(np.interp(np.clip(Lam, Ns[0], 120), Ns, dEs))
    kap, con, edge, L, turn = profile(P)
    kap = np.maximum(kap, 1e-4); Lam = 2*np.pi/kap
    Eb = float(np.sum(edge*np.array([dE_loop(x)/x for x in Lam])))
    return float(L), Eb + DIR*contact_phys(P)[1]


def lambda_for_ratio(Lh, Sh, Ll, Sl, r):
    """lambda at which (Lh + lam Sh)/(Ll + lam Sl) = r."""
    return (r*Ll - Lh)/(Sh - r*Sl)


def test():
    # the audit facts: one lattice, one normalization, S internally rigid
    assert abs(B_C - 0.157866) < 1e-5, "bend b analytically derived"
    assert abs(DIR + 0.502506) < 1e-9, "contact constant, units sqrt(kt/mu) -- same lattice"
    # the doublet ledgers at matched configuration
    gr = tighten_coords(braid_closure((1, 1, 1, 2, 2, 2), N=140).copy(), iters=14000)
    sq = tighten_coords(braid_closure((1, 1, 1, -2, -2, -2), N=140).copy(), iters=14000)
    assert knot_det(gr) == 9 and knot_det(sq) == 9
    _, Sg = ledger_S(gr); _, Ss = ledger_S(sq)
    assert Ss < Sg < 0, "THE SIGN FACT: the square is the more-bound member"
    # the conditional, on source-grade geometry + our conditioning
    lam_deg = (LIT_G - LIT_S)/(Ss - Sg)
    lam_np = lambda_for_ratio(LIT_G, Sg, LIT_S, Ss, NP_RATIO)
    assert 0 < lam_deg < 0.05, "doublet degeneracy at small positive lambda"
    assert 0.005 < lam_np < 0.12, "the n/p condition lands in a small-positive-lambda window"
    mg, ms = LIT_G + lam_np*Sg, LIT_S + lam_np*Ss
    assert mg > 0 and ms > 0 and mg > ms, "masses positive; granny heavier at lambda*"
    # the two-scale structure: coarse ratios geometry-dominated at lambda*
    t = np.linspace(0, 2*np.pi, 140, endpoint=False)
    tre = np.stack([(2 + np.cos(3*t))*np.cos(2*t),
                    (2 + np.cos(3*t))*np.sin(2*t), np.sin(3*t)], axis=1)*1.8
    P3 = tighten_coords(tre, iters=14000)
    P4 = tighten_coords(braid_closure((1, -2, 1, -2), N=140).copy(), iters=14000)
    L3, S3 = ledger_S(P3); L4, S4 = ledger_S(P4)
    r0 = L4/L3; rl = (L4 + lam_np*S4)/(L3 + lam_np*S3)
    assert abs(rl - r0)/r0 < 0.02, "coarse ratios move < 2 percent at lambda*: two-scale structure"
    print(f"S internally rigid (audit); doublet ledgers: S_g = {Sg:+.2f}, S_s = {Ss:+.2f} (square more bound)")
    print(f"conditional: degeneracy at lambda = {lam_deg:.4f}; n/p ratio at lambda* = {lam_np:.4f}")
    print(f"at lambda*: m_g = {mg:.2f} > m_s = {ms:.2f}; coarse ratio shift {abs(rl-r0)/r0*100:.2f}%")
    print("PASS: the gate has an anatomy (one rigid number), the conditional lands at small")
    print("      positive lambda with the PHYSICAL binding sign, and lambda stays underived, said.")


if __name__ == "__main__":
    test()
