"""Commission TET -- the lattice confrontation of the kappa_pack pin.
Bars locked BEFORE reading (analysis/TET_lattice_confrontation_bars_LOCKED.md):
admissibility rules A1-A4, the inversion arithmetic, the four-way verdict
grammar, and the sign clause. Sources cited in the results file; this
benchmark performs the pre-committed arithmetic on the numbers as found.
"""

CF, CA = 4 / 3, 3.0
RATIO = CA / CF          # 2.25, adjoint/fundamental Casimir ratio
PRED = {50: -0.0125, 250: -0.0025}   # CHET forward predictions


def floor_from_bound(b):
    return (RATIO - 1) / (2 * b)


def main():
    print("A1/A4 REGIME: the admissible window is the confining regime")
    print("  below adjoint screening; Bali's determination spans exactly")
    print("  r <= 1 fm, inside it. Short-distance data T3-firewalled out.")

    # The primary admissible bound: Bali PRD 62, 114503 (2000),
    # continuum-extrapolated, 8 representations: violations > 5% excluded
    # for r up to 1 fm.
    b_primary = 0.05
    fl = floor_from_bound(b_primary)
    print(f"PRIMARY BOUND (Bali 2000, stated): |delta| <= {b_primary:.0%}")
    print(f"  -> kappa_pack >= {fl:.1f} (pin inversion).")
    assert abs(fl - 12.5) < 0.01
    for k, p in PRED.items():
        assert abs(p) < b_primary
        print(f"  forward prediction at kappa = {k} ({p:+.2%}): INSIDE the "
              "bound.")
    print("  The data-derived floor (12.5) sits BELOW the CS-bound floor")
    print("  (50): the existing hard bound is consistent with both readings")
    print("  and tightens nothing. Both floor readings SURVIVE.")

    # The indicative (secondary-source) characterization: continuum
    # violations at the ~1% statistical level (Shevchenko-Simonov's
    # reading of Bali's extrapolation). NOT adopted as a bound (A3: the
    # primary paper states 5%); displayed with its would-be consequence.
    b_indic = 0.01
    print(f"INDICATIVE LEVEL (~{b_indic:.0%}, secondary characterization,")
    print(f"  NOT adopted per A3): would imply kappa_pack >= "
          f"{floor_from_bound(b_indic):.1f} -- ABOVE the 5% CS floor.")
    print("  A primary determination at this precision is exactly the")
    print("  measurement the pin awaits.")

    # The decision table for future data (pre-committed arithmetic):
    print("DECISION TABLE (admissible SU(3) adjoint bound b -> floor):")
    for b in (0.05, 0.02, 0.0125, 0.01, 0.005, 0.0025):
        note = ""
        if b <= 0.0125:
            note = "  <- excludes/decides kappa = 50 reading"
        if b <= 0.0025:
            note = "  <- reaches the continuum reading: full tower test"
        print(f"  b = {b:.2%} -> kappa_pack >= {floor_from_bound(b):.0f}{note}")

    # THE ADJACENT TENSION (sign clause, carried at full volume):
    # SU(N>=4) k-string tensions favor the sine law, which sits ABOVE
    # antisymmetric-Casimir -- a POSITIVE deviation at few-percent
    # precision (SU(6): sine/Casimir - 1 = +8.3% vs 2% errors).
    import math
    N, k = 6, 2
    cas = k * (N - k) / (N - 1)
    sine = math.sin(k * math.pi / N) / math.sin(math.pi / N)
    dev = sine / cas - 1
    print(f"ADJACENT TENSION (SU(6) k=2): sine/Casimir = {sine:.3f}/{cas:.3f}"
          f" = {dev:+.1%} vs ~2% errors -- a resolved POSITIVE deviation.")
    print("  SCOPE ADJUDICATION: FND-037/040 are SU(3)/QCD-anchored (the")
    print("  medium's Sigma_eff is the SU(3) flux tube) and SU(3) HAS no")
    print("  independent k-strings (sigma_2 = sigma_1 by conjugacy), so the")
    print("  k-string data cannot confront the registered claims WITHOUT an")
    print("  N-universality premise the registry never adopted. The tension")
    print("  is REGISTERED AT FLAG GRADE with the premise named: if the")
    print("  softening mechanism is claimed for all SU(N), the sine-law")
    print("  positivity contradicts the derived sign; if it is SU(3)-scoped,")
    print("  the data is silent. The scope question is now load-bearing and")
    print("  OPEN. (4D results also sit between sine and Casimir per the")
    print("  survey literature -- the k-string sector is itself contested.)")

    print("VERDICT (per the locked grammar): CONSISTENT-AND-ARMED for the")
    print("  SU(3) pin, with the precision demand registered (0.5-1.25%")
    print("  decides the 5% floor; 0.25% reaches the continuum reading),")
    print("  PLUS the adjacent k-string sign tension carried at flag grade")
    print("  with the N-universality scope question named.")
    print("ALL BARS ADJUDICATED")


if __name__ == "__main__":
    main()
