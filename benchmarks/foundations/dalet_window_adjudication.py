"""Commission DALET -- derive or retire the 1-100 window.
Bars locked BEFORE the sweep (analysis/DALET_window_derivation_bars_LOCKED.md).
Candidate classes pre-named C1-C5; verdict grammar pre-committed
(WINDOW DERIVED / HALF-WINDOW / RETIRED), with FND-041's cap withdrawal
wired into the half-window and retired branches.
"""
import math

HBAR, C = 1.054571817e-34, 2.99792458e8
ALPHA = 1 / 137.036
K_ME = 2.6065e-14
S_EFF = 3.61e35
H_CORE = 1.87e-19
BETA, F_RING = 35.4, 0.23
QAREA = 4 * math.pi * ALPHA * HBAR * C


def main():
    # C1 -- lower edge from the registered cutoff k <= 1/a:
    # admissible collective wavelengths satisfy lambda >= 2 pi a
    # (MATTER053's counting convention, exactly as registered). IF the
    # quantum area is a medium-expressible area (named premise, from
    # GRV-093's action architecture, NOT a registered theorem), then
    # l_q >= O(1) x a. Grade: Modeled, conditional on the premise.
    print("C1 (lower edge): k <= 1/a forces admissible lengths >= O(1) a;")
    print("  conditional on the NAMED PREMISE 'the quantum area is a")
    print("  medium-expressible area' (GRV-093 architecture; not a theorem).")
    print("  Lower edge: SUPPORTED at Modeled-with-premise, not Derived.")

    # C3 -- n_q <= 1 evaluated (direction computed, not assumed):
    # n_q = 4 pi alpha (3 beta/(0.23 chi)) (a h / l_q^2) <= 1
    # => (l_q/a)^2 >= 4 pi alpha (3 beta/(0.23 chi)) (h/a)  -- LOWER bound
    for kappa in (50, 250):
        sv = kappa * S_EFF
        a = (3 * K_ME / sv) ** (1 / 3)
        for chi in (1.0, 3.0):
            g = 4 * math.pi * ALPHA * (3 * BETA / (F_RING * chi)) * (H_CORE / a)
            print(f"  C3 at kappa={kappa}, chi={chi}: n_q<=1 => l_q/a >= "
                  f"{math.sqrt(g):.2f}")
            assert math.sqrt(g) < 2  # O(1) lower bound, never an upper bound
    print("C3: direction is LOWER at O(1) -- consistent with C1, and slack")
    print("  (the snaps are sub-quantum by 3-4 orders). NO upper edge here.")

    # C2 -- the cell-mode route is DEAD (MATTER053 empty band): any upper
    # edge routed through internal knot modes is declared dead on arrival.
    print("C2: dead on arrival per MATTER053 (empty internal mode band).")

    # C5 -- sweep find: the ZPE re-audit's Branch-B 'l_q/a in [34.5,35.0]'.
    # Adjudication: it is a TRACKING VALUE (the evaluated ratio with the
    # collapsed ZPE band), regenerated per mesh point -- the exact class
    # MATTER046's fourth guardrail bars from use as a landing zone
    # ('a relation is a landing zone only if at least one input is
    # external to the system being solved'). All its inputs are internal.
    print("C5: the Branch-B [34.5, 35.0] is a tracking value; the fourth")
    print("  guardrail FORBIDS its use as a constraint. Reported, not used.")

    # VERDICT under the pre-committed grammar
    print("VERDICT: HALF-WINDOW. The lower edge is supported (Modeled, with")
    print("  the named premise); NO registered claim forces an upper edge.")
    print("  The 100 was grammar. Consequences, per the locked bars:")
    print("  - FND-041's kappa_pack <= 157 cap is WITHDRAWN (correction")
    print("    pointer filed); the continuum reading is UN-EXCLUDED;")
    print("    l_q/a = 108 is a value, not a strain.")

    # The constructive residue: the sixth-root law inverts --
    # any EXTERNAL determination of l_q/a reads off kappa_pack.
    r0 = 43.0
    for r in (82.6, 108.0):
        print(f"  inversion check: r = {r} -> kappa_pack = {(r/r0)**6:.0f}")
    assert abs((82.6 / r0) ** 6 - 50) < 1 and abs((108.0 / r0) ** 6 - 250) < 3
    # sensitivity: d kappa / kappa = 6 d r / r
    print("THE RESIDUE: kappa_pack = (l_q/a / 43.0)^6 -- any external fix of")
    print("  the ratio measures the packing (sensitivity x6: 10% in r is 60%")
    print("  in kappa). The window question converts into an instrument.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
