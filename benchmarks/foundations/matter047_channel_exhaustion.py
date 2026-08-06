"""FND-MATTER-047: the channel-exhaustion session. Bars locked BEFORE
computing (analysis/MATTER047_channel_exhaustion_results.md):
(1) CHANNEL LIST, pre-committed from the parameter card -- every wave branch
a registered strand supports: TENSION (transverse, v = c), BENDING
(dispersive, priced by MATTER043), TORSION (v_t = sqrt(C/(mu r^2)), from the
registered C), LONGITUDINAL/STRETCH (v_L = c sqrt(k/T0), k DISPUTED on the
card), plus the mode-multiplicity dictionary factor D in [1e-2, 1e2].
No unregistered channels may be invented mid-session.
(2) INSTRUMENT: identical to MATTER043 (spectral weight k*v(k), tension
branch cut at 1/a, intra-strand branches cut at 1/r), stated per channel.
(3) The k-dispute discipline: the longitudinal channel's contribution is
UNKNOWN because k is disputed -- so the session computes the DEMAND (what
c_L/c the residual would require) and adjudicates only against a
pre-committed absurdity bound: a rescue demanding c_L > 1e10 c (an order
beyond any speed the corpus has ever used for its superluminal channel) is
declared dead; below that it would be flagged, not killed.
(4) VERDICT GRAMMAR, pre-committed: if the summed registered channels plus
D fall short of the residual by >10 orders, the conclusion is
CHANNEL EXHAUSTION -- the enhancement is not spectral-weight in origin
within the instrument class -- and the trichotomy is registered:
(i) sub-strand structure (Conjecture, no registered carrier),
(ii) a non-spectral collective mechanism (named open),
(iii) G as irreducible input (GRV-006's original verdict, never overturned).
(5) ONTOLOGY CLAUSE: under exhaustion, 'a_grav' is DEMOTED from a length to
a strength parameter -- MATTER041's 'two genuine micro-scales' is annotated:
the second 'scale' has no registered carrier and is shorthand for the
unfixed induced strength until a carrier exists. F-2SCALE's observable
content (the PVLAS discriminator) is unchanged by the rewording.
"""
import numpy as np

HBAR, C, G = 1.054571817e-34, 2.99792458e8, 6.67430e-11
A_M, T0_M, R = 6.0056e-17, 434.0, 9.4e-20
EH = C**4 / (16 * np.pi * G)
S_NEEDED = EH / (HBAR * C / A_M**2)          # 2.75e35 at the M-point
D_MAX = 1.0e2
CL_ABSURDITY = 1.0e10                        # pre-committed bound on c_L/c


def main():
    aor = A_M / R
    print(f"TARGET: S_needed = {S_NEEDED:.2e} at the M-point (a/r = {aor:.0f})")

    # Channel pricing (MATTER043 instrument)
    ch = {}
    ch['tension'] = 1.0
    ch['bending'] = (2 / 3) * aor**2                     # MATTER043, p = 2.000
    # torsion: v_t = sqrt(C/(mu r^2)); with C = G_sh pi r^4/2, G_sh ~ E/2.5,
    # E = k/(pi r^2), k ~ T0  =>  v_t/c = 1/sqrt(5)
    vt = 1 / np.sqrt(5)
    ch['torsion'] = vt * (2 / 3) * aor**2
    print("CHANNEL PRICES (same instrument, same cutoffs):")
    for k, v in ch.items():
        print(f"  {k:8s}: {v:.2e}")
    total = sum(ch.values())
    print(f"  SUM     : {total:.2e}  (x D_max {D_MAX:.0e} " 
          f"= {total * D_MAX:.2e} at the bracket's generous edge)")

    residual = S_NEEDED / (total * D_MAX)
    print(f"RESIDUAL after every priced channel AND the D bracket's edge: "
          f"{residual:.2e} ({np.log10(residual):.1f} orders)")

    # The longitudinal demand
    # adding a longitudinal channel (c_L/c)(2/3)(a/r)^2 must close
    # S_NEEDED (D at 1): the demand on c_L/c
    cl_needed = (S_NEEDED - total) / ((2 / 3) * aor**2)
    print(f"THE LONGITUDINAL DEMAND: closing the gap via the stretch branch")
    print(f"  requires c_L/c = {cl_needed:.2e} -- against the pre-committed")
    print(f"  absurdity bound of {CL_ABSURDITY:.0e} (an order beyond any speed")
    print(f"  the corpus has used), the rescue exceeds it by "
          f"{np.log10(cl_needed / CL_ABSURDITY):.1f} orders. DEAD, not flagged.")
    assert cl_needed > CL_ABSURDITY * 1e5

    # Verdict
    assert residual > 1e10
    print("VERDICT (pre-committed grammar): CHANNEL EXHAUSTION. Every wave")
    print("  branch a registered strand supports, priced by one instrument,")
    print("  summed, and multiplied by the dictionary bracket's generous")
    print("  edge, falls 28+ orders short. Within the instrument class, the")
    print("  induced-gravity enhancement IS NOT SPECTRAL-WEIGHT IN ORIGIN.")
    print("  THE TRICHOTOMY, registered:")
    print("  (i)   sub-strand structure -- Conjecture grade, NO registered")
    print("        carrier exists below r;")
    print("  (ii)  a non-spectral collective mechanism (topological or")
    print("        constraint-counting) -- named OPEN;")
    print("  (iii) G as irreducible input -- GRV-006's original verdict,")
    print("        which this campaign has now re-derived from the other")
    print("        direction and never overturned.")
    print("ONTOLOGY CLAUSE, triggered: 'a_grav' is DEMOTED from a length to")
    print("  the induced-STRENGTH parameter. MATTER041's 'two genuine")
    print("  micro-scales' is annotated: the second scale has no registered")
    print("  carrier; F-2SCALE's observable content (the PVLAS discriminator,")
    print("  36 orders between branches) is unchanged by the rewording.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
