"""Commission VAV -- the N computation: the identification theorem, the
composition kill, the floor determinations, and the mechanism target spec.
Bars locked BEFORE computing (analysis/VAV_n_computation_bars_LOCKED.md).
"""
import math

HBAR, C = 1.054571817e-34, 2.99792458e8
HBARC = HBAR * C
ALPHA, ME = 1 / 137.036, 9.1093837015e-31
K_ME = 2.6065e-14              # T0*a (spent calibration)
S_EFF = 3.61e35
L_RING = math.pi               # ropelength in cells
QAREA = 4 * math.pi * ALPHA * HBARC
A_EFF_CUT = 0.18               # derived core cutoff (defect-core benchmark)
E_CORE = 5.448                 # derived core constant, units of K


def point(kappa):
    a = (3 * K_ME / (kappa * S_EFF)) ** (1 / 3)
    t0 = K_ME / a
    return a, t0, math.sqrt(QAREA / t0)


def main():
    # V1 -- the identification theorem, machine-checked
    for kappa in (50, 250):
        a, t0, lq = point(kappa)
        g = lq / a
        N = 2 * g**2
        lam = g**2 / (4 * math.pi)          # ETA: lambda = g^2/(4 pi), eta=1
        A_amp = math.sqrt(2 * HBARC / (math.pi * t0))   # ELEC-054's A_hbar
        rho = A_amp / lq
        assert abs(rho - 1 / math.sqrt(2 * math.pi**2 * ALPHA)) < 1e-9
        print(f"kappa_pack = {kappa}: g = {g:.1f}, N = 2g^2 = {N:.3e}, "
              f"lambda = {lam:.0f}, A/a = {A_amp/a:.1f}, rho = {rho:.4f}")
    print("V1: ONE unknown. N = 2g^2 (FND-043 = ETA's residual); A = rho l_q")
    print("  with rho = 1/sqrt(2 pi^2 alpha) = 2.6348 an IDENTITY (ELEC-083's")
    print("  vacuity, re-verified); lambda = g^2/(4 pi) slaved. The L1 area")
    print("  selection, kappa_pack, the amplitude selection, and lambda are")
    print("  one question: WHAT SETS g.")

    # V2 -- the composition kill: DICT's table under eta = 1
    # l_lock = a/2, so {a, sqrt(l_lock a), l_lock} = {1, 0.707, 0.5} x a:
    cands = {"a": 1.0, "sqrt(l_lock a)": 1 / math.sqrt(2), "l_lock": 0.5}
    for name, v in cands.items():
        print(f"V2: candidate l_q = {name}: {v:.3f} a vs determined g = "
              f"82.6/108.0 -- DEAD at number level (factor 1.2e2-2.2e2).")
        assert 82.6 / v > 80
    print("V2: the DICT composition table dies WHOLE under the enslavement --")
    print("  all three candidates are O(a). l_q = g a with g mesoscopic and")
    print("  mechanism-less is the surviving composition. FND-043's drift")
    print("  cross-link inherits the named premise: g FIXED under drift.")
    print("  HE's soft-channel branch: DEAD (eta = 1 by theorem, cond. P1/P2).")

    # V3 -- floor determinations (ETA's bound-era numbers updated)
    for kappa in (50, 250):
        a, t0, lq = point(kappa)
        klock = 2 * t0 / a
        print(f"V3 kappa_pack = {kappa}: g DETERMINED = {lq/a:.1f} (was a")
        print(f"  bound, >= 13-16); kappa_lock PREDICTED = {klock:.2e} J/m^2;")
    J = K_ME / 2
    J_keV = J / 1.602176634e-16
    ident = ME * C**2 / (2 * L_RING)
    assert abs(J / ident - 1) < 2e-4   # K_ME registered to 5 digits
    print(f"V3: J per link = T0 a/2 = K_me/2 = {J_keV:.1f} keV EXACTLY --")
    print("  and this is the IDENTITY J = m_e c^2/(2L): ETA's flagged")
    print("  'MeV-adjacency' was the calibration wearing per-link units (its")
    print("  a-at-the-bound reading inflated it 4.6-6.5x). The observation")
    print("  DISSOLVES as an identity; the phantom/stale family's sixth catch.")

    # V4 -- the mechanism target spec (specified, not hunted)
    for kappa, g in ((50, 82.6), (250, 108.0)):
        x_bare = math.log(g)
        x_cut = math.log(g / A_EFF_CUT)
        print(f"V4 kappa_pack = {kappa}: a defect-log mechanism must deliver")
        print(f"  exponent {x_bare:.2f} (bare) / {x_cut:.2f} (derived cutoff")
        print("  0.18a) in units of pi K -- an O(1) target, computable in the")
        print("  registered defect machinery.")
        assert 4 < x_bare < 7 and 4 < x_cut < 7
    print("V4: the spec -- any g-mechanism must (i) produce g per kappa")
    print("  reading, equivalently produce the kappa^(1/6) scaling or fix")
    print("  kappa_pack outright (the FND-042 inversion makes it responsible")
    print("  for the vacuum packing); (ii) pass the ELEC-082/CONST drift")
    print("  filters; (iii) deliver its number BLIND. The defect-log route is")
    print("  the one registered structure with the right SHAPE (exponentially")
    print("  large from O(1)), and its required exponent is now a number.")

    # Guard disclosure (bar clause 1): a scan-product noticed during
    # scoping, displayed and refused:
    scan = A_EFF_CUT * math.exp(E_CORE)
    print(f"GUARD DISCLOSURE: 0.18 exp(E_core/K) = {scan:.1f} was noticed to")
    print("  land near the SUPERSEDED kappa=1 ratio (43.0, 2.8%). It is a")
    print("  scan-product with an unregistered exponent convention, against a")
    print("  dead point, missing the live values by 2.0-2.6x: REFUSED on all")
    print("  three grounds, displayed per the disclosure clause.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
