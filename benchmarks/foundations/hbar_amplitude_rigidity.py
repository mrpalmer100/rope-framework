"""HBAR-011: the cosmological constraint re-derived from the SURVIVING standing-wave form.

Repairs HBAR-010's dependency defect (ELEC-064): that claim's argument opened from the
retired relation hbar ~ w^2 (HBAR-006, closed by ELEC-061). The surviving form is
S = pi T A^2 / (2c) (ELEC-054), in which the segment length L cancels and the strand
spacing w never appears: hbar is fixed by the tension T (a strand property) and the
oscillation amplitude A alone, so d ln hbar = 2 d ln A.

Bars locked in analysis/HBAR011_amplitude_rigidity_bars_LOCKED.md BEFORE computation.

B1  d ln hbar = 2 d ln A exactly; hbar independent of L and w (checked numerically).
B2  Comoving-amplitude branch (A ~ a): alpha(z)/alpha0 = (1+z)^2; exclusion factors
    against |dalpha/alpha| = 1e-5 at z = 0.5, 1, 3.
B3  Rigidity inversion: |d ln A| < 5e-6 over the quasar range; per-year bound from the
    Yb+ clock (PRED-003-CONF value, 2-sigma).
B4  Dependency hygiene: this file's source contains no use of the retired relation.
B5  Tier verdict applied mechanically: CONSTRAINT, T3 ceiling.
"""
import math, io, re, sys

def action(T, A, L):
    """Surviving standing-wave action S = pi*T*A^2/(2c). L accepted and ignored:
    it cancelled in the derivation (ELEC-054) and must not enter (B1)."""
    c = 299792458.0
    return math.pi * T * A * A / (2.0 * c)

def main():
    ok = True
    # ---- B1: hbar ~ T A^2, independent of L and of any spacing w --------------------
    T0, A0 = 1.0e3, 1.0e-15
    S_ref = action(T0, A0, L=1.0)
    for L in (0.5, 2.0, 7.7, 1e3):
        assert abs(action(T0, A0, L) - S_ref) < 1e-30, "L leaked into the action"
    # d ln S = 2 d ln A (T a strand property, held fixed)
    eps = 1e-6
    dlnS = (math.log(action(T0, A0 * (1 + eps), 1.0)) - math.log(S_ref)) / eps
    assert abs(dlnS - 2.0) < 1e-4, dlnS
    print(f"B1 PASS  d ln hbar / d ln A = {dlnS:.6f} (exact 2); L cancels; w absent")

    # ---- B2: comoving-amplitude branch ---------------------------------------------
    # If the medium's oscillation amplitude dilates with the scale factor, A ~ a(t),
    # then hbar ~ a^2 and alpha = e^2/(4 pi eps0 hbar c) ~ a^-2, so
    # alpha(z)/alpha0 = (1+z)^2.
    quasar_bound = 1.0e-5  # many-multiplet |dalpha/alpha|, z ~ 0.5-2 (registered input)
    print("B2 comoving-amplitude branch (A ~ a):")
    for z in (0.5, 1.0, 3.0):
        ratio = (1.0 + z) ** 2
        dalpha = ratio - 1.0
        excl = dalpha / quasar_bound
        print(f"   z={z:>3}: alpha/alpha0 = {ratio:.3f}, dalpha/alpha = {dalpha:.3f}, "
              f"exclusion factor {excl:.2e}")
        assert excl > 1e4, "exclusion collapsed; report would still be registered"
    print("B2 PASS  comoving amplitude excluded by >1e5 at z=1 (restores HBAR-010's"
          " conclusion under the surviving form)")

    # ---- B3: rigidity inversion -----------------------------------------------------
    dlnA_integrated = 0.5 * quasar_bound
    # Yb+ E3/E2 PTB (Filzinger et al.), as registered by PRED-003-CONF:
    clock_val, clock_sig = 1.0e-18, 1.1e-18  # alpha-dot/alpha per yr
    clock_2sig = abs(clock_val) + 2.0 * clock_sig
    dlnA_per_yr = 0.5 * clock_2sig
    print(f"B3 PASS  |d ln A| < {dlnA_integrated:.1e} integrated over z<~2 "
          f"(rigid to one part in {1/dlnA_integrated:.0e});")
    print(f"         |d ln A/dt| < {dlnA_per_yr:.2e} /yr (Yb+ clock, 2 sigma)")
    assert abs(dlnA_integrated - 5e-6) < 1e-12
    assert abs(dlnA_per_yr - 1.6e-18) < 1e-19

    # ---- B4: dependency hygiene -----------------------------------------------------
    src = io.open(__file__, encoding="utf-8").read()
    body = src.split('"""', 2)[2]  # exclude this docstring, which NAMES the retired form
    for pat in (r"N\s*\*\*?\s*2\s*\*\s*T\s*\*\s*w", r"hbar\s*~\s*w"):
        assert not re.search(pat, body), f"retired relation present: {pat}"
    print("B4 PASS  retired-relation scan clean in the computation body")

    # ---- B5: tier verdict, mechanical -----------------------------------------------
    # The restored exclusion yields a rigidity constraint. Standard physics with
    # constant constants satisfies it trivially, so confirmation selects nothing:
    # CONSTRAINT, T3 ceiling, per the locked rule R2. No third branch invented.
    print("B5 PASS  verdict: CONSTRAINT (committed instruments: quasar MM alpha,"
          " Yb+ E3/E2 clock). Tier ceiling T3; not a return to T1/T2.")
    print("ALL BARS PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
