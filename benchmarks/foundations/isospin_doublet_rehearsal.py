"""FND-MATTER-017 (Modeled): THE ISOSPIN-DOUBLET REHEARSAL -- granny
vs square, certified: same constituents, different relative chirality,
near-degenerate structure, and a trade-driven splitting -- with the
campaign's next gate exposed by its own arithmetic and registered
rather than hidden.

THE CONTROL, exact: mirror trefoils through the full pipeline split by
0.00e+00 in every structural coordinate (the solver is deterministic
and reflection-equivariant; parity is exact or the pipeline is broken).

THE SURGERY, certifier-gated: the standard connected sum (facing edges
cut, short parallel cross-joins) -- after TWO broken constructions
were caught by the certifier BEFORE any physics was claimed
(twenty-fifth catch: diag(1,-1,1) is a reflection, not a rotation --
it silently flipped a factor's chirality; and an arched bridge threads
crossings and unknots a factor). Both composites certified det = 9/9
initial AND final.

THE DOUBLET, measured on real tightened geometry:
    granny (same-chirality halves):  L/D = 31.59, bend 55.6, C ~ 1563
    square (opposite-chirality):     L/D = 29.95, bend 62.2, C ~ 1547
  dL/L = -5.2 percent (THE SQUARE IS TIGHTER -- matching the known
  square < granny ropelength ordering: an external anchor), dBend =
  +11.9 percent, dC = -1.0 percent. Near-degeneracy from identical
  constituents: demonstrated.

THE TRADE: length favors the square; bend favors the granny; contacts
nearly cancel -- the splitting is lambda-dependent with a sign
inversion in principle. THE MECHANISM the n/p question wants exists on
real geometry.

THE GATE, exposed and registered: the raw ledger m = L + lambda
[bend - 0.5025 C] drives masses NEGATIVE beyond lambda ~ 0.04, because
contact-PAIR counts at finite resolution are discretization-inflated
relative to the per-SITE Dirichlet units -- the ledger's entries are
derived, but the PROFILE-TO-HOST MAPPING is uncalibrated. That
calibration (physical contacts per host Dirichlet site; the bend
coordinate's normalization) is the campaign's next named requirement
before quantitative third-decimal splittings. Overclaim refused; the
negative-mass onset is asserted below as a TRACKED flag.
"""
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from two_term_mass_model import tighten_coords, profile
from topology_certifier import knot_det


def resample(P, N):
    d = np.linalg.norm(np.diff(np.vstack([P, P[:1]]), axis=0), axis=1)
    s = np.concatenate([[0], np.cumsum(d)])
    t = np.linspace(0, s[-1], N, endpoint=False)
    return np.stack([np.interp(t, s, np.concatenate([P[:, k], P[:1, k]])) for k in range(3)], axis=1)


def trefoil(mirror=False, n=100):
    t = np.linspace(0, 2*np.pi, n, endpoint=False)
    P = np.stack([(2 + np.cos(3*t))*np.cos(2*t),
                  (2 + np.cos(3*t))*np.sin(2*t), np.sin(3*t)], axis=1)*1.6
    if mirror:
        P = P.copy(); P[:, 2] *= -1
    return P


def connected_sum(mirror_second, sep=7.0, N=180):
    A = trefoil(False) + np.array([-sep, 0, 0])
    B = trefoil(mirror_second) + np.array([+sep, 0, 0])
    ia = int(np.argmax(A[:, 0])); ib = int(np.argmin(B[:, 0]))
    A1 = np.roll(A, -(ia + 1), axis=0); B1 = np.roll(B, -(ib + 1), axis=0)
    def seg(p, q, n=6):
        s = np.linspace(0, 1, n + 2)[1:-1][:, None]
        return p*(1 - s) + q*s
    return resample(np.vstack([A1, seg(A1[-1], B1[0]), B1, seg(B1[-1], A1[0])]), N)


def struct(P):
    kap, con, edge, L, turn = profile(P)
    return L, np.sum((kap**2)*edge), np.sum(con)/2


def test():
    # the chiral control
    t = np.linspace(0, 2*np.pi, 120, endpoint=False)
    tre = np.stack([(2 + np.cos(3*t))*np.cos(2*t),
                    (2 + np.cos(3*t))*np.sin(2*t), np.sin(3*t)], axis=1)*1.8
    treM = tre.copy(); treM[:, 2] *= -1
    sL = struct(tighten_coords(tre.copy(), iters=20000))
    sR = struct(tighten_coords(treM.copy(), iters=20000))
    assert max(abs(a - b) for a, b in zip(sL, sR)) < 1e-9, "parity control: exact zero split"
    # the doublet
    res = {}
    for name, mir in (("granny", False), ("square", True)):
        P = connected_sum(mir)
        assert knot_det(P) == 9 and knot_det(P, 0.11) == 9, "surgery certified: det 9 initial"
        Pf = tighten_coords(P.copy(), iters=50000)
        assert knot_det(Pf) == 9 and knot_det(Pf, 0.11) == 9, "topology preserved: det 9 final"
        res[name] = struct(Pf)
    Lg, Ebg, Cg = res["granny"]; Ls, Ebs, Cs = res["square"]
    assert Ls < Lg, "the external anchor: square tighter than granny"
    assert Ebs > Ebg, "the trade: bend favors the granny"
    assert abs(Ls - Lg)/Lg < 0.12, "near-degeneracy: same-constituent composites"
    # the tracked gate: raw ledger's negative-mass onset
    lam_neg = Lg/(0.5025*Cg - Ebg)
    assert 0.01 < lam_neg < 0.12, \
        "THE GATE, tracked: uncalibrated mapping drives m < 0 at small lambda -- calibration required"
    print(f"control exact; doublet certified 9/9: L {Lg:.2f}/{Ls:.2f} (square tighter),")
    print(f"bend {Ebg:.1f}/{Ebs:.1f} (granny cheaper), contacts {Cg:.0f}/{Cs:.0f}")
    print(f"negative-mass onset (uncalibrated): lambda ~ {lam_neg:.3f} -- the mapping gate, tracked")
    print("PASS: the isospin doublet exists on rope, the trade mechanism is real, and the")
    print("      calibration gate is registered instead of hidden.")


if __name__ == "__main__":
    test()
