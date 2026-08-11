"""Commission OMICRON — the fully-independent check: converter, ARMED and waiting.

STATUS: COMPLETED 2026-08-10. The convention question was answered first
(session OMICRON part 1), the data arrived via the arXiv source package, and
the confrontation ran under the pre-locked rules. VERDICT LEDGER:
  R=4a (0.393 fm, least quantum-widened): R_eq = 0.391 fm, -4.0% -> CONFIRMED
  R=6a (0.590 fm): R_eq = 0.473 +/- 0.030 fm, +16.2% -> TENSION (1-sigma edge
      touches the CONFIRMED boundary at 0.448)
  R=8a (0.787 fm): R_eq = 0.502 +/- 0.233 fm, +23.4% -> TENSION, statistically
      empty (the nu error +/-20 swallows the verdict)
  The excess GROWS one-signed with R -- which is the paper's own headline
  result (logarithmic quantum widening of the TOTAL width). The corpus
  reference 0.402-0.407 fm is an intrinsic-width-class quantity (d-stable in
  ELEC-052); the Lisbon total width contains the widening by construction.
  The least-widened point agrees at -4%. NOT a wound; a located definitional
  refinement (intrinsic vs total width), pre-named in this file's caveat
  before the data was seen.

THE CONVENTION, established from the paper's own captions and companion text
(session 2026-08-10):
  - The Lisbon group measures the SQUARED field components (E^2, B^2) via
    plaquette correlators and computes flux-tube widths as
        w^2 = <r^2>  with the LAGRANGIAN DENSITY as probability distribution
    (Fig. 11 of 1302.3633; stated explicitly in the companion 1702.03454).
  - The Lagrangian density is an E^2-class weight, i.e. the same weighting
    class as the registered ELEC-052 definition R_eq = sqrt(2 <x^2>_{E^2}).
  - Therefore the mapping is EXACT and parameter-free:
        R_eq = sqrt(2) * sqrt(<r^2>)  =  sqrt(2 * w^2)
    No profile ansatz, no lambda, no guessed normalization — the ambiguity
    that excluded this source is gone. (Their lambda ~ 0.22-0.24 fm remains
    unusable alone: it is the far-tail parameter of a convolution ansatz and
    underdetermines <r^2>; it is NOT used.)
  - Caveat carried: their w^2 contains the quantum-widening (log R) growth
    and, if taken from the finite-T companion, a temperature systematic; the
    locked bar B3 requires the T = 0 paper's value at the R nearest 0.7 fm.

INPUT WANTED: w^2 [fm^2] (with error) at R nearest 0.7 fm from Fig. 11 /
its table in PRD 88, 054504 — hand-download route, same as ELEC-052's
ancillary files.
"""
import math

REF = (0.402, 0.407)      # registered R_eq band, fm
T_TUBE = 1.874e5          # J/m
XI_TIER2_SAME_GROUP = 0.395  # fm, Commission XI pure-gauge value (secondary comparison)

# DATA IN HAND (2026-08-10): reconstructed EXACTLY from the arXiv source
# package (arXiv-1302_3633v1), better than digitizing Fig. 11 -- the paper's own
# closed-form width from its fitted convolution ansatz (Eq. "width"):
#     sqrt(<r^2>) = sqrt( 3/2 lambda^2 + 2 lambda nu^2/(lambda + 2 nu) )
# with (lambda, nu) per R from tab:fit (mediator plane, ACTION density,
# longitudinal component), lattice spacing a = 0.0983737 fm (beta = 6.0, 32^4,
# 1100 configs). w^2 = <r^2> below in fm^2; errors MC-propagated from the
# table's (uncorrelated approx, stated).
A_LATTICE = 0.0983737
FIT_TABLE = {  # R[a]: (lambda[a], dlam, nu[a], dnu)
    4: (2.165, 0.033, 0.877, 3.335),
    6: (2.379, 0.156, 2.040, 0.365),
    8: (2.052, 0.201, 4.092, 20.22),
    10: (2.088, 0.536, 5.306, 36.43),
}


def w_rms_lat(lam, nu):
    return math.sqrt(1.5 * lam ** 2 + 2 * lam * nu ** 2 / (lam + 2 * nu))


W2_TABLE = {R * A_LATTICE: ((w_rms_lat(l, n) * A_LATTICE) ** 2, None)
            for R, (l, _, n, _) in FIT_TABLE.items()}


def confront(r_source_fm, w2, err=0.0):
    r_eq = math.sqrt(2 * w2)
    dev = r_eq / REF[1] - 1
    band = ("CONFIRMED" if abs(dev) <= 0.10 else
            "TENSION" if abs(dev) <= 0.25 else "CONTRADICTED")
    sigma = T_TUBE / (math.pi * (r_eq * 1e-15) ** 2)
    print(f"R={r_source_fm} fm: w^2={w2}({err}) fm^2 -> R_eq={r_eq:.3f} fm "
          f"({dev:+.1%}) -> {band}; Sigma={sigma:.2e} J/m^3; "
          f"vs XI same-group tier-2 {r_eq/XI_TIER2_SAME_GROUP-1:+.1%}")
    return band


def main():
    if not W2_TABLE:
        print("OMICRON converter ARMED: mapping R_eq = sqrt(2 w^2) derived and")
        print("locked; awaiting the PRD 88 054504 Fig. 11 values (hand-download).")
        print("Per bar B5 the exclusion is registered as PENDING DATA, not permanent:")
        print("the convention ambiguity that forced XI's exclusion is resolved.")
        return
    for r, (w2, err) in sorted(W2_TABLE.items()):
        confront(r, w2, err)


if __name__ == "__main__":
    main()
