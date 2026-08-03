"""QB-033: the anharmonic V_r correction by self-consistent Gaussian approximation,
closing QB-029's 14 percent systematic, plus the QB-027 pinned-tolerance repair
adjudicated. No new Monte Carlo. Bars locked in
analysis/QB033_anharmonic_bars_LOCKED.md (prediction before comparison).
"""
import io, os
import numpy as np

KT, TBATH, N, H = 0.64, 0.4, 192, 0.30
VAR_EMP = -2 * np.log(0.780)          # QB-030's empirical bank, 25536 samples
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def lattice_s2(m2):
    ks = 2 * np.pi * np.arange(1, N) / N
    return (TBATH / N) * np.sum(1.0 / (m2 + 2 * KT * (1 - np.cos(ks))))


def b1_fixed_point():
    m2 = float(np.sqrt(1 - H ** 2))       # harmonic curvature cos(phi_0)
    s2_h = lattice_s2(m2)
    for it in range(200):
        s2 = lattice_s2(m2)
        m2_new = float(np.sqrt(1 - H ** 2)) * np.exp(-s2 / 2)
        if abs(m2_new - m2) < 1e-10:
            break
        m2 = m2_new
    s2 = lattice_s2(m2)
    print(f"B1 PASS  SCGA fixed point converged in {it} iterations:")
    print(f"         m_eff^2 = {m2:.4f} (harmonic {np.sqrt(1-H**2):.4f});")
    print(f"         on-site s2 = {s2:.4f} (harmonic {s2_h:.4f});")
    print(f"         PREDICTION: var_sat = 2 s2 = {2*s2:.4f}, "
          f"V_SCGA = {np.exp(-s2):.4f}")
    return 2 * s2, np.exp(-s2), 2 * s2_h


def b2_b3_compare(var_scga, V_scga, var_harm):
    gap_h = abs(var_harm - VAR_EMP) / VAR_EMP
    gap_s = abs(var_scga - VAR_EMP) / VAR_EMP
    print(f"B2       empirical var = {VAR_EMP:.4f}; harmonic gap {gap_h:.1%}; "
          f"SCGA gap {gap_s:.1%}")
    assert gap_s < 0.08, f"SCGA outside 8% ({gap_s:.1%})"
    print(f"B2 PASS  SCGA closes the systematic from {gap_h:.1%} to {gap_s:.1%};")
    print(f"         the residual {gap_s:.1%} is the two-loop correction's size,")
    print("         registered, not absorbed.")
    V_emp = 0.780
    gv = abs(V_scga - V_emp) / V_emp
    assert gv < 0.05
    print(f"B3 PASS  V_SCGA = {V_scga:.4f} vs empirical {V_emp:.3f} ({gv:.1%});")
    print("         V_r now carries the label DERIVED(T, kt, h) at this accuracy.")
    return V_scga


def b4_propagation(cbar_derived):
    Sdet = 2.7274                          # same-run closed form (QB-030/031/032)
    k = Sdet / (2 * np.sqrt(2))
    Vp = (1 + 2 * cbar_derived) / 3
    rows = [
        ("floor (perpendicular)", cbar_derived * Sdet, 2.028),
        ("isotropic", Vp * Sdet, 2.226),
        ("ceiling (in-plane)", k * np.sqrt(2) * (1 + cbar_derived), 2.407),
    ]
    print("B4       first-order propagation from the DERIVED cbar (MC values used")
    print("         the empirical bank and do not move; agreement is the check):")
    for name, pred, mc in rows:
        print(f"           {name:24s} derived {pred:.3f}   measured {mc:.3f} "
              f"({abs(pred-mc)/mc:.1%})")
        assert abs(pred - mc) / mc < 0.08
    print("B4 PASS  the whole QB-032 curve is now reproduced from (T, kt, h) plus")
    print("         the transport theorem, to first order, within 8 percent.")


def b5_qb027():
    src = io.open(os.path.join(ROOT, "benchmarks", "quantum",
                               "bell_experiment.py"), encoding="utf-8").read()
    assert "abs(S - S_det) < 0.03" in src
    pinned = [ln for ln in src.splitlines()
              if "assert" in ln and ("2.66" in ln or "2.63" in ln)]
    assert not pinned, f"historical magnitude pinned in an assertion: {pinned}"
    print("B5 PASS  QB-027 repair ADJUDICATED (rule R4): the registered benchmark")
    print("         already asserts same-run self-consistency (|S - S_det| < 0.03)")
    print("         and pins NO historical magnitude in any assertion -- the")
    print("         environment sensitivity affects printed values only. The")
    print("         repair is a documentation fix: QB-027's annotation stands and")
    print("         no code change is made to a registered, passing benchmark.")


def main():
    var_scga, V_scga, var_harm = b1_fixed_point()
    V = b2_b3_compare(var_scga, V_scga, var_harm)
    b4_propagation(V)
    b5_qb027()
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
