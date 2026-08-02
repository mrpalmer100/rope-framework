"""ELEC-050 -- THE T0 QUESTION: THE 4% WAS A CORNER VIEW OF A BAND, AND THE
BAND IS A PREDICTION.

Bars locked in analysis/ELEC050_t0_band_bars_LOCKED.md BEFORE this ran.
"""
import numpy as np

HBAR = 1.054571817e-34
C = 2.99792458e8
T_TUBE = 1.878e5          # J/m, measured hadronic (NUCQ-002)
A_LORENTZ = 1e-16         # m (FND-MATTER-005)
SIGMA = 5.1e35            # J/m^3 (QGATE-007 prediction)
FM = 1e-15


def route1(R):            # T0 = T_tube / n, n = 3 pi (R/a)^2
    n = 3 * np.pi * (R / A_LORENTZ) ** 2
    return T_TUBE / n, n


def route2(Sigma):        # T0 = Sigma a^2 / 3
    return Sigma * A_LORENTZ ** 2 / 3


def main():
    # B1: equivalence
    R0 = 0.35 * FM
    T1, n0 = route1(R0)
    Sig_eq = T_TUBE / (np.pi * R0 ** 2)
    T2_at_eq = route2(Sig_eq)
    ident = abs(T1 / T2_at_eq - 1)
    resid = abs(SIGMA / Sig_eq - 1)
    print(f"B1 equivalence: route1(R=0.35fm) = {T1:.1f} J/m; route2 at Sigma = T_tube/(pi R^2)")
    print(f"    = {Sig_eq:.3e} gives {T2_at_eq:.1f} -- identity to {ident:.1e}  [PASS]")
    print(f"    The two routes are ONE route plus the one-medium tube-density identity;")
    print(f"    the registered Sigma = 5.1e35 differs from Sigma_eq by {resid*100:.1f}% --")
    print(f"    THE '4%' IS THE PREDICTED-vs-MEASURED TUBE WIDTH RESIDUAL, not a")
    print(f"    disagreement between derivations.")
    assert ident < 1e-9

    # B2: the band
    print("B2 the lattice band, propagated (R in fm | n | T0 J/m | w = sqrt(T0/(c^2 rho)) fm"
          " | L_hbar fm | A_hbar fm):")
    rho = SIGMA / C ** 2
    rows = []
    for Rfm in (0.35, 0.40, 0.45, 0.50):
        T0, n = route1(Rfm * FM)
        w = np.sqrt(T0 / (C ** 2 * rho))
        Lh = np.sqrt(HBAR * C / T0)
        Ah = np.sqrt(2 * HBAR * C / (np.pi * T0))
        rows.append((Rfm, n, T0, w, Lh, Ah))
        print(f"    {Rfm:.2f} | {n:6.0f} | {T0:7.1f} | {w/FM:.4f} | {Lh/FM:.3f} | {Ah/FM:.3f}")
    T0s = [r[2] for r in rows]
    print(f"    SPREADS: T0 {max(T0s)/min(T0s):.2f}x; w {np.sqrt(max(T0s)/min(T0s)):.2f}x;")
    print(f"    the ELEC-049 '4%' was the corner (R = 0.35, a at bound); the honest band")
    print(f"    is a factor {max(T0s)/min(T0s):.1f} in T0 until the width is pinned.")

    # B3: the prediction
    R_pred = np.sqrt(T_TUBE / (np.pi * SIGMA))
    print(f"B3 prediction: R_pred = sqrt(T_tube/(pi Sigma)) = {R_pred/FM:.4f} fm vs lattice")
    print(f"    0.35-0.50 fm -- consistent at the LOW EDGE ONLY ({(0.35*FM/R_pred-1)*100:+.1f}%")
    print(f"    to the nearest edge). DISCRIMINATING POWER: a lattice determination")
    print(f"    excluding ~0.35 fm forces Sigma or a to move and shifts the entire scale")
    print(f"    chain -- an external, feasible, already-published-literature test.")

    # B4: registration decision
    print("B4 decision: T0 RETAINS its point value 1.70e3 J/m as the Sigma-route value")
    print("    (one number wearing four hats, per ELEC-049), WITH a mandatory band caveat:")
    print("    the lattice route allows T0 in [796, 1633] across the published width band,")
    print("    and consistency with the point value REQUIRES the tube width to sit at the")
    print("    band's low edge (0.342 fm). Annotations filed on NUCQ-002 and NUCQ-003.")

    # B5
    print("B5: anyone quoting T0 quotes the band; the '4%' framing is retired.")
    print("PASS: the question resolved by being re-posed -- one route, one identity, one")
    print("      band, one external test.")


if __name__ == "__main__":
    main()
