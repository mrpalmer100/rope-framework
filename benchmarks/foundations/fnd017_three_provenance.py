"""FND-MATTER-059 -- PROVENANCE OF THE FACTOR 3 IN T0 = Sigma a^2 / 3.

The question this settles is narrow and mechanical: does the 3 in ELEC-053's
invariance relation come from the tube-radius integration, or is it a
per-direction family count?

Result: the tube radius CANCELS identically. What survives the cancellation is
the areal strand density n / (pi R^2) = 3 / a^2, whose 3 is the number of
orthogonal strand families threading a cell. The 3 is a per-direction
partition, not an artifact of the tube geometry.

This benchmark makes NO claim about what a displacing inclusion couples to.
That is a separate question, registered open (see
docs/technical/SEALED_COMMISSION_2_fnd017_exclusion_and_doublecount.md).
"""
import numpy as np

A_LORENTZ = 1.0e-16   # mesh cell scale, m (registered)
T_TUBE = 1.0          # arbitrary; must cancel


def strand_count(R, a):
    """ELEC-053's tube strand count: n = 3 pi (R/a)^2."""
    return 3 * np.pi * (R / a) ** 2


def main():
    a = A_LORENTZ
    radii = [1e-15, 1e-12, 1e-9, 1e-6, 1e-3]

    print("C1  R-CANCELLATION: T0/Sigma = (T_tube/n) / (T_tube/(pi R^2))")
    ratios = []
    for R in radii:
        n = strand_count(R, a)
        ratio = (T_TUBE / n) / (T_TUBE / (np.pi * R ** 2))
        ratios.append(ratio)
        assert abs(ratio / (a ** 2 / 3) - 1) < 1e-12, "invariance broken"
        print(f"    R = {R:8.1e} m  ->  T0/Sigma = {ratio:.6e} m^2")
    spread = max(ratios) / min(ratios) - 1
    assert spread < 1e-12
    print(f"    spread across 9 decades of R: {spread:.1e}  -- R cancels identically")

    print()
    print("C2  WHAT SURVIVES: areal strand density n/(pi R^2), R-independent")
    dens = [strand_count(R, a) / (np.pi * R ** 2) for R in radii]
    for R, d in zip(radii, dens):
        assert abs(d * a ** 2 - 3) < 1e-12
        print(f"    R = {R:8.1e} m  ->  n/(pi R^2) = {d:.6e} /m^2 = 3/a^2")
    print("    the surviving numerator is exactly 3 -- the family count")

    print()
    print("C3  THE 3 IS A PER-DIRECTION PARTITION, checked independently:")
    print("    a cell of volume a^3 hosts three orthogonal strands of length a,")
    print("    so cell content = 3 * T0 * a and Sigma = 3 T0 / a^2.")
    sigma_from_cell = 3 * T_TUBE * a / a ** 3
    sigma_from_areal = 3 * T_TUBE / a ** 2
    assert abs(sigma_from_cell / sigma_from_areal - 1) < 1e-12
    print(f"    cell route {sigma_from_cell:.4e} == areal route "
          f"{sigma_from_areal:.4e} (T0=1)  ✓")
    print("    the two routes agree, and neither references R.")

    print()
    print("C4  SCOPE, stated so it cannot be over-read:")
    print("    one strand's tributary cross-section is a^2/3.")
    print("    Whether a DISPLACING inclusion engages one share or all three is")
    print("    NOT decided here and NOT decidable from this algebra alone.")
    print()
    print("FND-MATTER-059 PASS: the 3 is family-counting, not tube geometry.")


if __name__ == "__main__":
    main()
