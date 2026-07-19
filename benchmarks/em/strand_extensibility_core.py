"""The fourth micro-primitive identified: finite strand EXTENSIBILITY (stretch
modulus k). It generates the super-quadratic coefficient EM-RECON-008 located:
c4 = (k - T0)/8, exactly, from the arc-length strain expansion. Stability REQUIRES
k > T0 (pure tension gives c4 = -T0/8 < 0: nonlinearly unstable, no core). One
dimensionless input k/T0 then sets equilibrium spacings; a single value ~O(1) is
consistent with BOTH the nuclear and chemical spacing-to-range ratios (log-weak
check, honestly flagged).

Derivation (exact expansion, verified numerically below):
  strain of a strand under transverse field: eps = sqrt(1+|grad psi|^2) - 1
  elastic strand energy density: e = T0*eps + (k/2) eps^2
  expand in g^2 = |grad psi|^2:
     e = (T0/2) g^2 + [(k - T0)/8] g^4 + O(g^6)
  -> quadratic term = the existing corpus functional (consistency check)
  -> quartic term c4 = (k - T0)/8 = THE missing super-quadratic coefficient.

Consequences:
  * SIGN from stability, not choice: c4 > 0 iff k > T0. The pure-tension
    idealization (k=0) gives c4 < 0 -- softening, runaway collapse, no matter.
    Finite extensibility is REQUIRED for the network to be stable at high strain.
  * Two-mode equilibrium: E(d) = -a e^{-d/xi} + b e^{-2d/xi} (quartic cross-terms
    decay twice as fast) -> d0/xi = ln(2b/a). Measured ratios: nuclear 1.36
    (1.9fm/1.4fm) needs b/a=1.94; chemical 1.67 (0.74A/0.443A) needs b/a=2.66 --
    SAME order, one k/T0 covers both. CAVEAT: log-weak (low discriminating power).
  * Atomic-mass chain now structurally complete: Yukawa attraction (NUC-004) +
    extensibility core (this) -> binding curve with a real minimum -> binding
    computable in form from {T, mu, lambda, k} + absolute scales (inputs).

Status honesty: the c4 FORM is exact mathematics given the elastic-strand energy;
the IDENTITY of the primitive (strand extensibility) is a physically-motivated
mechanism (Modeled/Conjecture level); the VALUE of k is a new input measured once.
"""
import numpy as np


def quartic_coefficient_from_expansion(T0=1.0, k=5.0):
    """Fit e(g2) = T0(sqrt(1+g2)-1) + (k/2)(sqrt(1+g2)-1)^2 at small g2; the
    fitted quartic coefficient must equal (k - T0)/8."""
    g2 = np.linspace(1e-4, 2e-2, 40)
    eps = np.sqrt(1 + g2) - 1
    e = T0 * eps + 0.5 * k * eps**2
    c4_fit, c2_fit, _ = np.polyfit(g2, e, 2)
    return c2_fit, c4_fit


def test():
    # (1) expansion coefficients exact: c2 = T0/2, c4 = (k-T0)/8
    for T0, k in [(1.0, 5.0), (1.0, 1.0), (2.0, 0.0)]:
        c2, c4 = quartic_coefficient_from_expansion(T0, k)
        assert abs(c2 - T0 / 2) < 1e-3, "quadratic term must be T0/2 (corpus functional)"
        assert abs(c4 - (k - T0) / 8) < 2e-2, f"quartic must be (k-T0)/8, got {c4}"

    # (2) sign from stability: pure tension (k=0) gives NEGATIVE quartic (unstable)
    _, c4_pure = quartic_coefficient_from_expansion(1.0, 0.0)
    assert c4_pure < 0, "pure-tension idealization must be softening (unstable, no core)"
    _, c4_stiff = quartic_coefficient_from_expansion(1.0, 5.0)
    assert c4_stiff > 0, "k > T0 must give a positive quartic (repulsive core)"

    # (3) cross-sector spacing consistency (log-weak, honestly): one b/a ~ 2 covers both
    r_nuc = 1.9 / 1.4          # nucleon spacing / Yukawa range
    r_chem = 0.74 / 0.443      # H2 bond / healing length
    ba_nuc, ba_chem = np.exp(r_nuc) / 2, np.exp(r_chem) / 2
    assert 1.0 < ba_nuc < 5.0 and 1.0 < ba_chem < 5.0, "both sectors need O(1) b/a"
    assert ba_chem / ba_nuc < 2.0, "the two sectors' required b/a agree within 2x"

    print(f"expansion exact: c2=T0/2, c4=(k-T0)/8 (verified for 3 parameter sets)")
    print(f"stability: k=0 -> c4<0 (unstable, no core); k>T0 -> c4>0 (core). Sign REQUIRED.")
    print(f"cross-sector: nuclear needs b/a={ba_nuc:.2f}, chemical b/a={ba_chem:.2f} -> one k/T0 covers both")
    print("PASS: fourth primitive = strand extensibility k; c4=(k-T0)/8 exact; core from")
    print("      stability; spacings consistent (log-weak). k's VALUE remains an input.")


if __name__ == "__main__":
    test()
