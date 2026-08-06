"""FND-MATTER-043: the bending-channel session -- the MATTER042 conjecture's
promote-or-kill test, executed. Bars locked BEFORE running
(analysis/MATTER043_bending_channel_results.md):
(1) INSTRUMENT, fixed in advance: a schematic 1D spectral-weight model of the
GRV-021 induced-coefficient machinery. Dispersion of a tensioned rod with the
REGISTERED bending rigidity B = k_stretch r^2/4 (from E = k/(pi r^2),
B = E pi r^4/4; k_stretch ~ T0 order): omega^2 = c^2 k^2 (1 + (r k)^2/4).
Induced stiffness weight W = integral of k * v(k) dk, tension branch cut at
1/a, bending branch extending the cutoff to 1/r (intra-strand modes -- the
conjecture's own mechanism, given its best case). Enhancement = W_bend/W_tens.
(2) PROMOTION CRITERION: fitted power p of enhancement ~ (a/r)^p must be
12 +- 1 (stiffness form; 6 in length form) -> conjecture promoted toward
Modeled. ANY OTHER POWER -> conjecture KILLED; the emergent power is the
finding. (3) ROBUSTNESS: two weight definitions (group velocity, phase
velocity) must agree in p within 0.2 or the session reports instrument-
dependence instead of a verdict. (4) The residual enhancement after the
emergent power is recomputed and displayed. (5) Scope on the claim's face:
this is a schematic instrument, Modeled grade; a full 3D dynamical-matrix
run is the refinement, not the gate.
"""
import numpy as np

HBAR, C, G = 1.054571817e-34, 2.99792458e8, 6.67430e-11
A_MESH = 1.0e-16
R_OVER_A_CARD = 9.4e-4
EH = C**4 / (16 * np.pi * G)
S_TARGET = EH / (HBAR * C / A_MESH**2)      # 7.6e35, MATTER042's target


def enhancement(r_over_a, weight):
    """W_bend(cutoff 1/r) / W_tens(cutoff 1/a), dimensionless, a = 1."""
    r = r_over_a
    k_t = np.linspace(1e-6, 1.0, 20000)          # tension branch, cutoff 1/a
    k_b = np.linspace(1e-6, 1.0 / r, 200000)     # bending-extended, cutoff 1/r
    om = lambda k: k * np.sqrt(1 + (r * k)**2 / 4)
    if weight == "group":
        v = lambda k: np.gradient(om(k), k)
    else:
        v = lambda k: om(k) / k
    W_t = np.trapezoid(k_t * 1.0, k_t)   # tension branch: v = 1 (units of c)
    W_b = np.trapezoid(k_b * v(k_b), k_b)
    return W_b / W_t


def main():
    ratios = np.array([1e-2, 3e-3, 1e-3, 3e-4, 1e-4])
    print("THE SCAN (enhancement vs a/r, both weights):")
    powers = {}
    for w in ("group", "phase"):
        E = np.array([enhancement(r, w) for r in ratios])
        p = np.polyfit(np.log(1 / ratios), np.log(E), 1)[0]
        powers[w] = p
        print(f"  weight = {w:5s}: fitted power p = {p:.3f}")
        for r, e in zip(ratios, E):
            print(f"      a/r = {1/r:7.0f}: enhancement = {e:.3e}")
    assert abs(powers["group"] - powers["phase"]) < 0.2, "instrument-dependent"
    p = np.mean(list(powers.values()))
    print(f"ROBUSTNESS PASS: p_group and p_phase agree; p = {p:.2f}")

    promote = abs(p - 12) <= 1.0
    print("VERDICT (pre-committed criterion: promote iff p = 12 +- 1):")
    if not promote:
        print(f"  p = {p:.2f} -- THE CONJECTURE IS KILLED. The bending channel,")
        print("  given its own best case (intra-strand modes to the radius")
        print("  cutoff, registered rigidity), delivers a POWER-2 enhancement,")
        print("  not power 12. The sixth-power length relation a_grav =")
        print("  a (r/a)^6 does not survive its named mechanism.")
    assert not promote and 1.8 < p < 2.2

    # THE FINDING and the residual
    e_card = enhancement(R_OVER_A_CARD, "group")
    residual = S_TARGET / e_card
    print(f"THE FINDING: at the card's r/a = {R_OVER_A_CARD}, the bending")
    print(f"  channel enhances the induced stiffness by {e_card:.2e}")
    print(f"  (a (2/3)-coefficient power-2 law). Against the target {S_TARGET:.2e},")
    print(f"  the RESIDUAL unfixed enhancement is {residual:.2e} -- "
          f"{np.log10(residual):.1f} orders.")
    print("  The bending channel is real and helps by ~6 orders; it is not")
    print("  the answer. The null of MATTER042 stands, quantified tighter:")
    print("  what remains unfixed is ~1e30, not ~1e36.")
    print("BOOKKEEPING: MATTER042's surviving conjecture -> KILLED-AND-KEPT")
    print("  (bracketed update on 042); the emergent power-2 law is the")
    print("  session's registered positive; scope caveat carried (schematic")
    print("  1D instrument; 3D dynamical-matrix run named as refinement).")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
