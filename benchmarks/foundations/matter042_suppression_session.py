"""FND-MATTER-042: the suppression session. What sets a_grav/a_mesh ~ 1e-18?
Bars locked BEFORE the sweep (analysis/MATTER042_suppression_results.md):
(1) TARGETS: the length ratio S_L = a_mesh/a_grav and the stiffness
enhancement S = EH/(hbar c/a_mesh^2); any identity between them is logged as
identity, never as evidence. (2) LEAD #1 (GRV-093's fork lever = the same
17-18 orders) is tested for identity FIRST; if it is an identity it is
registered as a guardrail and killed as a lead. (3) CANDIDATE CRITERIA,
pre-committed: a candidate is loggable only if (i) built solely from
registered dimensionless quantities, (ii) matches within a factor of 3,
(iii) carries a stated power-counting rationale, (iv) makes a tracking
prediction (if the registered inputs move, the relation must move with
them). (4) HIGH-POWER CAVEAT, pre-committed: any candidate with power >= 6
is automatically down-weighted -- a 2x convention ambiguity becomes 2^n --
and its convention sensitivity must be computed and displayed. (5) Failed
candidates are listed, not hidden. (6) Permitted outcome includes THE NULL:
suppression stays unfixed (GRV-006 restated at the fork's new location).
"""
import numpy as np

HBAR, C, G = 1.054571817e-34, 2.99792458e8, 6.67430e-11
ALPHA = 1 / 137.036
A_MESH, A_GRAV = 1.0e-16, 1.2930e-34
R_OVER_A = 9.4e-4              # card thinness ratio (radius convention)
DC = 1.87e-19                  # measured strand thickness (HBAR-005)
GAMMA_OVER_T0 = 3.5e-7         # couple-stress/tension, card (lattice branch)
MP_ME = 1836.15
MATCH_BAR = 3.0

EH = C**4 / (16 * np.pi * G)
S_L = A_MESH / A_GRAV
S = EH / (HBAR * C / A_MESH**2)


def check(name, value, target, rationale, high_power=False, conv=None):
    f = max(value, target) / min(value, target)
    ok = f <= MATCH_BAR
    tag = "PASS" if ok else "FAIL"
    if ok and high_power:
        tag = "PASS (DOWN-WEIGHTED: high power)"
    line = f"  {name}: {value:.2e} vs target {target:.2e} -> factor {f:.2f}  [{tag}]"
    if conv:
        line += f"  convention sensitivity: {conv}"
    print(line)
    print(f"      rationale: {rationale}")
    return ok


def main():
    print(f"TARGETS  S_L = a_mesh/a_grav = {S_L:.3e}")
    print(f"         S   = EH/(hbar c/a^2) = {S:.3e}   (stiffness ENHANCEMENT:")
    print("         gravity's rigidity is enormous, so G is small -- the sign")
    print("         of the problem stated correctly.)")

    # LEAD #1: the fork-lever 'coincidence' tested for identity
    # n_q = 4 pi alpha (3 beta/0.23 chi)(a h / l_q^2); l_q and h fork-invariant
    # => lever(n_q) = a_ratio = S_L exactly. IDENTITY.
    lever = S_L  # by linearity in a
    print("LEAD #1  GRV-093's fork lever vs S_L: n_q is LINEAR in a with l_q")
    print("         fork-invariant, so lever == a-ratio == S_L BY CONSTRUCTION.")
    print("         VERDICT: IDENTITY -- registered as a guardrail (like R3/R8),")
    print("         killed as a lead. One geometric ratio, one appearance,")
    print("         two bookkeepings.")

    print("THE SWEEP (criteria pre-committed; failures displayed):")
    results = {}
    results['alpha^-8'] = check(
        "alpha^-8", ALPHA**-8, S_L,
        "no mechanism counts eight alpha vertices in a stiffness; swept as due diligence")
    results['(m_p/m_e)^6'] = check(
        "(m_p/m_e)^6", MP_ME**6, S_L,
        "mass-ratio powers; no vacuum-sector mechanism")
    results['(gamma/T0)^-6'] = check(
        "(gamma/T0)^-6", GAMMA_OVER_T0**-6, S,
        "six couple-stress rigidity ratios; the mechanically motivated route", True)
    conv6 = f"radius vs diameter shifts by 2^6 = {2**6}"
    conv12 = f"radius vs diameter shifts by 2^12 = {2**12}"
    results['(a/r)^6 vs S_L'] = check(
        "(a/r)^6", R_OVER_A**-6, S_L,
        "a_grav = a (r/a)^6 x O(2): triaxial bending power-counting, NAMED NOT DERIVED",
        True, conv6)
    results['(a/r)^12 vs S'] = check(
        "(a/r)^12", R_OVER_A**-12, S,
        "the squared form of the same candidate", True, conv12)
    results['(a/d_c)^12'] = check(
        "(a/d_c)^12", (A_MESH / DC)**12, S,
        "the SAME candidate under the diameter convention -- displayed to expose sensitivity",
        True)
    # coverage-count N^{3/2} refused on category grounds, not numerics:
    print("  N_coverage^(3/2) (~1e18): numerically near S_L but REFUSED on")
    print("      category grounds -- N is an atom-bound-structure count")
    print("      (FND-MATTER-004), not a vacuum-sector constant.")

    assert not results['alpha^-8'] and not results['(m_p/m_e)^6']
    assert not results['(gamma/T0)^-6'] and not results['(a/d_c)^12']
    assert results['(a/r)^6 vs S_L'] and results['(a/r)^12 vs S']

    print("VERDICT (per the locked grammar):")
    print("  1. THE NULL STANDS AS THE REGISTERED STATE: the enhancement is")
    print("     UNFIXED -- GRV-006's underdetermination, restated at the")
    print("     fork's new location. Equivalent registered reading: EH/T0 =")
    print(f"     {EH/260.7:.1e} strand-tensions -- the load-sharing count GRV-006")
    print("     showed no commitment selects.")
    print("  2. ONE candidate survives the criteria and is logged at")
    print("     CONJECTURE, HEAVILY CAVEATED: a_grav = a_mesh (r/a)^6 x O(2).")
    print("     It passes the factor-3 bar ONLY under the radius convention")
    print("     (diameter fails by ~1500x), and a twelfth power converts any")
    print("     O(2) into 4e3 -- by the pre-committed high-power rule the")
    print("     NUMERICAL match is weak evidence BY CONSTRUCTION. What is")
    print("     registered is the RELATION with its tracking falsifier: if")
    print("     r/a or a_mesh moves under future measurement, a_grav must")
    print("     track as the sixth power, with no new freedom.")
    print("  3. The triaxial-bending rationale is NAMED, NOT DERIVED; the")
    print("     mechanically motivated (gamma/T0)^-6 route FAILS by 720x,")
    print("     which is a strike AGAINST the candidate's mechanism, displayed.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
