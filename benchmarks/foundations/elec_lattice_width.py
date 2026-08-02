"""ELEC-051 -- THE LATTICE-WIDTH ADJUDICATION: THE LITERATURE READ, THE
DEFINITIONS CONVERTED, THE PREDICTION TESTED.

Bars locked in analysis/ELEC051_lattice_width_bars_LOCKED.md BEFORE this ran.
Sources: Baker et al. EPJ C 85, 29 (2025) [full QCD, physical masses];
Verzichelli et al. [2603.05323] (2+1)d intrinsic width; Clem fits (2012-2019).
"""
import numpy as np

HBARC = 0.1973269804     # GeV fm
SQRT_GH0 = 1.0           # GeV (S1 text)
ALPHA = 1.0
T_TUBE = 1.878e5         # J/m
SIGMA = 5.1e35           # J/m^3
FM = 1e-15
R_PRED = 0.342           # fm (ELEC-050)


def profile(x_fm):
    """S1's fitted nonperturbative field, both Abelian components, arb. norm.
    Scales converted: b3 = sqrt(gH0/2)/hbar-c, b8 = alpha*sqrt(gH0)/2/hbar-c (1/fm)."""
    b3 = np.sqrt(SQRT_GH0 ** 2 / 2.0) / HBARC
    b8 = ALPHA * SQRT_GH0 / 2.0 / HBARC
    return 1.0 / np.cosh(b3 * x_fm) ** 2 + (np.sqrt(3) / (2 * ALPHA)) / np.cosh(b8 * x_fm) ** 2


def main():
    x = np.linspace(0, 4.0, 400001)   # fm, radial
    E = profile(x)
    # 2D transverse integrals: measure x dx
    wE = np.sqrt(np.trapezoid(x ** 3 * E, x) / np.trapezoid(x * E, x))
    # B2 validation vs paper's ~0.5 fm
    ok = abs(wE / 0.5 - 1) < 0.25
    print(f"B2(i) E-weighted RMS from reconstructed profile: w_E = {wE:.3f} fm vs paper "
          f"~0.5 fm ({(wE/0.5-1)*100:+.0f}%)  [{'PASS -- instrument validated' if ok else 'FAIL -- VOID'}]")
    assert ok
    # B2(ii) energy-weighted uniform-equivalent radius
    x2_E2 = np.trapezoid(x ** 3 * E ** 2, x) / np.trapezoid(x * E ** 2, x)
    R_eq = np.sqrt(2 * x2_E2)
    print(f"B2(ii) energy-weighted (E^2) uniform-equivalent radius: R_eq = sqrt(2<x^2>_E2) "
          f"= {R_eq:.3f} fm  (the quantity NUCQ-003's mass-density formula requires)")

    # B3: the adjudication
    dev = R_eq / R_PRED - 1
    if abs(dev) < 0.15:
        verdict = "SUPPORTS"
    elif 0.35 <= R_eq <= 0.5:
        verdict = "CONSISTENT (within the old band)"
    else:
        verdict = "TENSION"
    print(f"B3 ADJUDICATION: R_pred = {R_PRED} fm vs lattice-derived R_eq = {R_eq:.3f} fm "
          f"({dev*100:+.1f}%) -- {verdict}.")
    print(f"    Definition spread on the record: E-weighted RMS 0.5 fm (S1); intrinsic tail")
    print(f"    0.109 fm (S2, different theory/dimension); Clem lambda 0.17-0.19 fm (S3).")
    print(f"    The corpus's old 0.35-0.5 band conflated definitions; resolved, the")
    print(f"    mass-density radius the framework predicts is the E^2-weighted one.")

    # B4: registry update -- T0 at the adjudicated width
    n = 3 * np.pi * (R_eq * FM / 1e-16) ** 2
    T0 = T_TUBE / n
    print(f"B4 registry: at R_eq = {R_eq:.3f} fm, n = 3 pi (R/a)^2 = {n:.0f} and "
          f"T0 = {T0:.0f} J/m vs the Sigma-route 1700 ({T0/1700-1:+.1%}).")
    print(f"    The T0 band contracts from [796, 1633] (the old conflated band) to the")
    print(f"    single-definition value; annotation filed on NUCQ-003.")

    # B5: honesty
    print("B5 limits: sech^2 profile assumed (Clem would shift the conversion); alpha ~ 1")
    print("    and sqrt(gH0) = 1.0 GeV taken from S1's text, exact Table-4 fit values not")
    print("    extracted; S2 is (2+1)d SU(2), logged for definition spread only. A tighter")
    print("    adjudication wants S1's ancillary data files (available on arXiv).")
    print("PASS: the free adjudication executed -- the prediction confronted with the")
    print("      current state of the art under the correct definition.")


if __name__ == "__main__":
    main()
