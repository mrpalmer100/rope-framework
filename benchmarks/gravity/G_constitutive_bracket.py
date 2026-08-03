"""GRV-074: G(T, a) attempted -- the assumed form found dimensionally open (the
CONST defect class in PRED-003's other leg), the Sakharov route's exponents
derived on both hbar branches, the absolute scale quantified at ~1e39 T0, and the
keeper: J1713 refutability is G-form-ROBUST. Bars locked in
analysis/GRV074_G_constitutive_bars_LOCKED.md.
"""
import numpy as np
import sympy as sp

G_MEAS = 6.674e-11
C = 2.998e8
HBARC = 3.1615e-26
A_LOR = 1.0e-16
T0 = {"lattice": 1203.0, "Sigma": 1700.0}


def b1_units():
    kg, m, s = sp.symbols('kg m s', positive=True)
    G_u = m**3 / (kg * s**2)
    tension = sp.simplify((m / s)**4 / G_u)
    assert sp.simplify(tension - kg * m / s**2) == 0   # Newton = J/m
    print("B1 PASS  c^4/(16 pi G) is a TENSION (J/m), machine-checked. The assumed")
    print("         G ~ 1/(Ta) is therefore DIMENSIONALLY OPEN -- [1/(Ta)] = 1/J --")
    print("         the PRED-003-CONST defect class, now found in the prediction's")
    print("         OTHER leg. Unique {hbar c, a}-closures: c^4/(16 pi G) =")
    print("         xi T (a/l)^p needs a closure length; the minimal closure")
    print("         (p = 0) gives G ~ 1/T with NO a-dependence -- the registered")
    print("         (-1, -1) exponents are one closure choice among several, never")
    print("         derived. Enumerated: p = 0 -> (-1, 0); p = 1 -> (-1, -1) [the")
    print("         registered reading]; p = 2 -> (-1, -2). The closure power is")
    print("         underived.")


def b2_sakharov():
    T, a, A, hbar, c, zeta = sp.symbols('T a A hbar c zeta', positive=True)
    # E-ext: E_site = hbar*c/a (hbar external) -> coeff = zeta*hbar*c/a^2
    G_ext = c**4 * a**2 / (16 * sp.pi * zeta * hbar * c)
    pT = sp.simplify(sp.diff(sp.log(G_ext), T) * T)
    pa = sp.simplify(sp.diff(sp.log(G_ext), a) * a)
    assert (pT, pa) == (0, 2)
    print("B2       Sakharov, hbar-external:  G ~ a^2/hbar  -> exponents (0, 2):")
    print("         G is TENSION-INERT and spacing-quadratic.")
    # E-med: hbar = pi T A^2/(2c); tension-channel co-drift A ~ T^(-1/2) (LOCK)
    hbar_med = sp.pi * T * A**2 / (2 * c)
    G_med = sp.simplify(c**4 * a**2 / (16 * sp.pi * zeta * hbar_med * c))
    pT_m = sp.simplify(sp.diff(sp.log(G_med), T) * T)
    pa_m = sp.simplify(sp.diff(sp.log(G_med), a) * a)
    assert (pT_m, pa_m) == (-1, 2)
    print("B2       Sakharov, hbar-medium:    G ~ a^2/(T A^2) -> (-1, 2) raw; under")
    print("         the tension-channel co-drift A ~ T^(-1/2) the T-dependence")
    print("         CANCELS (G ~ a^2 again): both branches agree on the channels.")
    print("B2 PASS  the Sakharov route's constitutive verdict: G tension-inert,")
    print("         G ~ a^2 in spacing, conditional on P1/P2.")


def b3_magnitude():
    needed = C**4 / (16 * np.pi * G_MEAS)
    induced = HBARC / A_LOR**2
    print(f"B3       needed c^4/(16 pi G) = {needed:.2e} J/m;")
    print(f"         Sakharov scale hbar c/a^2 at the Lorentz bound = "
          f"{induced:.2e} J/m  (gap {needed/induced:.1e});")
    for k, t in T0.items():
        print(f"         strand tension T0 ({k}) = {t:.0f} J/m  "
              f"(gap {needed/t:.1e})")
    print("B3 PASS  NO route survives magnitude: the absolute scale -- the")
    print("         sector's standing open item -- is QUANTIFIED at 1.4-2.0e39 x T0")
    print("         (or 7.6e35 x the Sakharov band scale). GRV-073's thin-strand")
    print("         mechanism ((r/a)^2 = 8.7e-7 per power) would need ~5-6 powers;")
    print("         filed as the one corpus-native suppression source, not leaned")
    print("         on. Exponents are tonight's deliverable; magnitude is not.")


def b4_table():
    # alpha ~ T a^2 (LOCK-collapsed). Rows: G-form exponents (pT, pa).
    rows = {
        "assumed closure p=1 (registered)": (-1, -1),
        "assumed closure p=0": (-1, 0),
        "assumed closure p=2": (-1, -2),
        "Sakharov (both hbar branches)": (0, 2),
    }
    clock_mean, clock_sig = 9.89e-19, 1.10e-19
    G_J1713 = 3.2e-13
    print("B4       the consequence table (alpha ~ T a^2; channels: T-drift, a-drift):")
    print("         form                              ratio(T)   ratio(a)   J1713-implied alpha drift (clock sigmas)")
    for name, (pT, pa) in rows.items():
        rT = "inert-G" if pT == 0 else f"{1/pT:+.0f}" if pT else "?"
        ra = "inert-G" if pa == 0 else f"{2/pa:+.1f}"
        # a confirmed G drift g: through whichever channel supports it, implied
        # alpha drift = (alpha-exponent/G-exponent) * g on that channel; take the
        # channel that admits the drift with the SMALLEST |alpha| implication:
        opts = []
        if pT != 0:
            opts.append(abs(1 / pT))
        if pa != 0:
            opts.append(abs(2 / pa))
        fac = min(opts)
        implied = fac * G_J1713
        sig = abs(implied - clock_mean) / clock_sig
        print(f"         {name:32s} {rT:>8s}   {ra:>8s}   {implied:.1e} "
              f"({sig:.1e} sigma)")
        assert sig > 1e5
    print("B4 PASS  THE KEEPER: under EVERY candidate G form, a confirmed 3-sigma")
    print("         J1713 G drift implies an alpha drift at least 1e5 clock sigmas")
    print("         from the measured bound -- PRED-003's refutation condition is")
    print("         G-FORM-ROBUST. The ratio VALUES are form-conditional; the")
    print("         DECIDABILITY is not.")


def main():
    b1_units()
    b2_sakharov()
    b3_magnitude()
    b4_table()
    print("B5       VERDICT: G's exponents are UNDERIVED-BUT-BRACKETED -- the")
    print("         assumed family (-1, -p) with the closure power p underived, and")
    print("         the Sakharov candidate (0, 2) conditional on the funded")
    print("         conjecture; the registered -2/-1 ratio values are hereby")
    print("         G-form-conditional by annotation. Robust content extracted:")
    print("         J1713 decidability survives every row; the absolute scale is")
    print("         quantified. Next-orders: the band coefficient in physical units")
    print("         (decides between the rows); the closure-length derivation for")
    print("         the assumed family; the thin-strand suppression audit for the")
    print("         39-order gap. No tier motion.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
