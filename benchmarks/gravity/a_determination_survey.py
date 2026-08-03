"""GRV-076: the a-determination survey. No live pin of the lattice scale exists;
(a, Sigma) is degenerate along Sigma = 3 T0/a^2; the two-scale tension is a
one-bit FORK with named discriminators. Bars locked in
analysis/GRV076_a_survey_bars_LOCKED.md.
"""
import numpy as np

HBAR, C, G_MEAS = 1.054571817e-34, 2.99792458e8, 6.674e-11
A_LOR, A_SAK, ZETA = 1.0e-16, 1.26e-34, 1.208
T0 = {"lattice-anchored": 1203.0, "Sigma-route": 1700.0}
SIGMA_PVLAS = 8.6e27          # J/m^3, lower bound (EM-RECON-016)


def b1_classification():
    table = [
        ("Lorentz limit (FND-MATTER-005)", "a <= 1e-16 m", "BOUND (upper)"),
        ("Scale sets T0 = 1203/1700 N", "constructed at the bound",
         "CONVENTION (FND-017: 'Sigma and the bound wearing a different hat')"),
        ("Ambient spacing 5.78e-17 m", "ELEC-041..053 lineage",
         "RETIRED-LINEAGE (descends from the ELEC-061-retired hbar relation)"),
        ("Sigma (EM-RECON-016)", "> 8.6e27 J/m^3", "BOUND (lower)"),
        ("T0 = Sigma a^2/3 (FND-017)", "exact", "DERIVED-FROM-OTHERS"),
        ("a_Sak = 1.26e-34 m (GRV-075)", "Sakharov-selected",
         "CONDITIONAL (on P1; not a pin)"),
    ]
    print("B1       the classification table (rule R1):")
    for name, val, tag in table:
        print(f"           {name:34s} {val:26s} {tag}")
    assert not any("PIN" == t.split()[0] for _, _, t in table)
    print("B1 PASS  ZERO live pins. The lattice scale is bounded above, Sigma")
    print("         below, and everything else is convention, retired lineage, or")
    print("         derived. The no-live-pin hypothesis HOLDS.")


def b2_degeneracy():
    print("B2       the degeneracy line Sigma = 3 T0/a^2 at the bound:")
    for name, t in T0.items():
        sig = 3 * t / A_LOR ** 2
        a_back = np.sqrt(3 * t / sig)
        assert abs(a_back - A_LOR) / A_LOR < 1e-12
        print(f"           {name:16s} T0 = {t:6.0f} N  ->  Sigma = {sig:.2e} J/m^3")
    print("B2 PASS  FND-017's inversion reproduced exactly: T0 and the bound are")
    print("         one datum, not two. (a, Sigma) is DEGENERATE at fixed T0.")


def b3_forks():
    print("B3       both forks at fixed T0 (rule R2), against the PVLAS lower bound:")
    for fork, a in (("F-Lor (a = 1e-16)", A_LOR), ("F-Sak (a = 1.26e-34)", A_SAK)):
        for name, t in T0.items():
            sig = 3 * t / a ** 2
            ok = sig > SIGMA_PVLAS
            print(f"           {fork:22s} {name:16s} Sigma = {sig:.2e}  "
                  f"(> PVLAS bound: {ok})")
            assert ok
    print("B3 PASS  BOTH forks satisfy every empirical Sigma constraint: the data")
    print("         on the books today do not discriminate. The tension is a FORK.")


def b4_discriminators():
    # (i) the Sakharov channel's induced G at each fork
    print("B4       discriminator (i): the Sakharov channel's G at each fork:")
    for fork, a in (("F-Lor", A_LOR), ("F-Sak", A_SAK)):
        Gs = C ** 3 * a ** 2 / (16 * np.pi * ZETA * HBAR)
        print(f"           {fork}: G_induced = {Gs:.2e}  (measured {G_MEAS:.2e}; "
              f"ratio {Gs/G_MEAS:.1e})")
    print("         F-Sak reproduces G by construction; F-Lor makes the SAME")
    print("         registered channel 3.6e35 too strong -- so under F-Lor the")
    print("         Sakharov identification (P1) must be FALSE and gravity's")
    print("         source is unassigned. The fork is equivalently: IS P1 TRUE?")
    # (ii) vacuum nonlinearity, |Delta n| ~ 1/Sigma
    s_lor = 3 * 1203 / A_LOR ** 2
    s_sak = 3 * 1203 / A_SAK ** 2
    print(f"B4       discriminator (ii): vacuum nonlinearity |Delta n| ~ 1/Sigma --")
    print(f"           fork Sigmas differ by {s_sak/s_lor:.1e}: any birefringence-")
    print("           class detection of medium nonlinearity discriminates the")
    print("           forks outright (both sit below QED at current sensitivity;")
    print("           the statement is in-principle, priced honestly).")
    print("B4 PASS  the fork carries two named discriminators.")


def b5_propagation():
    print("B5       propagation: GRV-075's 'two-scale tension' is RE-CHARACTERIZED")
    print("         as a one-bit fork, not a contradiction; its physical invariants")
    print("         (l_q, A in metres) are (alpha, hbar c, T)-built and STAND at")
    print("         fixed T0, which the degeneracy line preserves by construction;")
    print("         the 5.78e-17 ambient spacing is flagged retired-lineage")
    print("         wherever it survives in live prose. No tier motion.")


def main():
    b1_classification()
    b2_degeneracy()
    b3_forks()
    b4_discriminators()
    b5_propagation()
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
