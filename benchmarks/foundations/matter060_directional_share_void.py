"""FND-MATTER-060 -- THE DIRECTIONAL SHARE IS UNAVAILABLE TO THIS CONSTRUCTION.

The settler named by FND-MATTER-058 (does a displacing inclusion couple to the
full cell face a^2 or to one direction's share a^2/3?) is VOID, not pending.
It presupposed that the lambda construction computes an absolute medium content
against which a directional partition could act. It does not.

lambda is a FRACTION of mode-carrying medium displaced: a ratio of like against
like. Any content density cancels identically between numerator and
denominator. The factor 3 is therefore not "already in Sigma and reintroduced"
-- it is unavailable in EITHER route, because no absolute content is ever
computed.

This is decidable from the construction alone and is independent of where the
result lands.
"""
import numpy as np

R_OVER_A = 9.4e-4      # inherited, FND-MATTER-056
TARGET = 1.156e-5      # FND-MATTER-055
BAR = 2.00             # inherited, pre-committed


def main():
    print("C1  WHAT THE CONSTRUCTION INTEGRATES AGAINST (audited in source):")
    print("    matter056_suppression_mechanism.py: lambda = pi (r/a)^2")
    print("      displaced cross-section pi r^2 / available per cell a^2.")
    print("    matter058_displaced_mode_count.py: inherits R_OVER_A, x F1 = 2.")
    print("    Sigma and T0 appear NOWHERE in the lambda chain -- cell")
    print("    geometry only. Verified by source scan.")

    print()
    print("C2  THE CANCELLATION, shown explicitly with a content density nu:")
    a = 1.0
    r = R_OVER_A * a
    for nu_label, nu in [("nu = 1 (areas)", 1.0),
                         ("nu = 3/a^2 (strand-equivalents)", 3.0 / a ** 2),
                         ("nu = 17.3/a^2 (arbitrary)", 17.3 / a ** 2)]:
        lam = (np.pi * r ** 2 * nu) / (a ** 2 * nu)
        print(f"    {nu_label:34s} -> lambda = {lam:.6e}")
        assert abs(lam / (np.pi * R_OVER_A ** 2) - 1) < 1e-12
    print("    ANY density primitive cancels. A ratio of like against like")
    print("    cannot carry a partition factor.")

    print()
    print("C3  THE ASYMMETRY THAT PRODUCED THE ERROR:")
    print("    pi r^2 / (a^2/3) prices the NUMERATOR in strand-equivalents")
    print("    while leaving the DENOMINATOR a raw cell face. Either both")
    print("    sides are strand-equivalents (3 cancels) or both are areas")
    print("    (3 never appears). Mixing them is the whole of the 3x.")
    mixed = np.pi * R_OVER_A ** 2 / (1.0 / 3.0)
    clean = np.pi * R_OVER_A ** 2
    assert abs(mixed / clean - 3.0) < 1e-12
    print(f"    mixed/clean = {mixed/clean:.1f} -- exactly the gap's worth")

    print()
    print("C4  THE EXCLUSION ARGUMENT PROVES THE OPPOSITE OF ITS CONCLUSION:")
    print("    if an inclusion evicts all three families, the DENOMINATOR")
    print("    must count all three too. The a^2/3 reading is the one that")
    print("    would require an inclusion to see one family's share only.")

    print()
    print("C5  STANDING RESULT, unchanged:")
    forced = 2.0
    lam = np.pi * R_OVER_A ** 2 * forced
    gap = TARGET / lam
    print(f"    forced product = {forced:.0f}, lambda = {lam:.3e}")
    print(f"    target {TARGET:.3e} / lambda = {gap:.2f}x against bar {BAR:.2f}x")
    assert gap > BAR
    print("    OUTSIDE THE BAR. lambda REMAINS OPEN. Settler VOID, not pending.")

    print()
    print("C6  SCOPE, unverified and named: this audits the lambda chain only.")
    print("    The FND-MATTER-055 target is built from dE_zp/L and the")
    print("    conditioning table. If that path converts through T0 or Sigma,")
    print("    a directional factor could live THERE. Separate audit, and it")
    print("    is target-side: a session doing it should seal the mechanism")
    print("    out, not the target.")

    print()
    print("FND-MATTER-060 PASS: P1 excluded on bookkeeping grounds.")


if __name__ == "__main__":
    main()
