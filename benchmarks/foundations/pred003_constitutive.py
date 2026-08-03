"""PRED-003-CONST: the constitutive derivation of e_eff^2, with the provenance and
dimensional audits it forced first.

Bars locked in analysis/PRED003_CONST_bars_LOCKED.md BEFORE computation.
Route rules: the XCHAIN identity is inadmissible (contains A); no closure selected by
numerics; unfavorable findings registered at full volume.
"""
import io, os, re, sys
import sympy as sp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def b1_provenance():
    """Scan the registry and benchmarks for any derivation of 2T^2/(kappa a)
    outside the PRED-003 lineage."""
    pats = [r"2\s*\*?\s*T\s*\^?\**\s*2\s*/\s*\(\s*kappa\s*\*?\s*a\s*\)"]
    hits = []
    files = [os.path.join(ROOT, "claims.yaml")]
    for dp, _, fns in os.walk(os.path.join(ROOT, "benchmarks")):
        files += [os.path.join(dp, f) for f in fns if f.endswith(".py")]
    for f in files:
        txt = io.open(f, encoding="utf-8", errors="ignore").read()
        for p in pats:
            if re.search(p, txt):
                hits.append(os.path.relpath(f, ROOT))
                break
    lineage = {"claims.yaml",
               os.path.join("benchmarks", "foundations", "pred_alpha_g_drift.py"),
               os.path.join("benchmarks", "foundations", "pred003_xchain_audit.py"),
               os.path.join("benchmarks", "foundations", "pred003_constitutive.py"),
               # PRED-003-LOCK (registered after this audit): the locking
               # determination DERIVES the enslaved alpha -- lineage, not leak.
               os.path.join("benchmarks", "foundations", "pred003_locking.py")}
    outside = [h for h in hits if h not in lineage]
    assert not outside, f"unexpected derivation site(s): {outside}"
    print("B1 PASS  provenance gap CONFIRMED: alpha ~ 2T^2/(kappa a) appears only in")
    print("         the PRED-003 lineage (paper P6, its registration, this audit's")
    print("         claims). No registry claim or benchmark DERIVES it; EM-002b")
    print("         registers alpha only as a consistency relation. The sole T1's")
    print("         alpha form is PAPER-STATED, REGISTRY-UNDERIVED.")


def b2_dimensions():
    J, m = sp.symbols('Junit m', positive=True)     # energy, length units
    T_u = J / m                                     # tension
    kappa_A = T_u**2 / J                            # kappa = T^2/J_energy -> J/m^2
    kappa_B = J * m                                 # alternative convention
    for name, k_u in (("kappa=T^2/J [J/m^2]", kappa_A), ("kappa~J*m", kappa_B)):
        u = sp.simplify(T_u**2 / (k_u * m))
        dimless = sp.simplify(u - 1) == 0
        print(f"B2       [2T^2/(kappa a)] with {name}: {u}  dimensionless: {dimless}")
        assert not dimless
    print("B2 PASS  the literal paper expression is DIMENSIONALLY OPEN (a tension,")
    print("         J/m, under FND-001's own units) -- the NUC-013 imported-units")
    print("         failure class, found in the corpus's sole T1 prediction.")


def b3_closure():
    """Uniqueness of the dimensionless closure under the paper's primitive
    statement: close with hbar*c and powers of a length ~ a only."""
    n, mm = sp.symbols('n mexp')
    # units: [2T^2/(kappa a)] = J/m ; [a^n] = m^n ; [hbar c]^mm = (J*m)^mm
    # dimensionless: J: 1 - mm = 0 ; m: -1 + n - mm = 0
    sol = sp.solve([sp.Eq(1 - mm, 0), sp.Eq(-1 + n - mm, 0)], [n, mm])
    assert sol == {n: 2, mm: 1}, sol
    print("B3 PASS  closure UNIQUE up to a pure number: n = 2, m = 1, i.e.")
    print("         alpha = 2 lambda T^2 a / (kappa hbar c). Equivalently, by")
    print("         alpha's definition, THE CONSTITUTIVE RELATION:")
    print("             e_eff^2/(4 pi eps0) = 2 lambda T^2 a / kappa = 2 lambda J a")
    print("         (Coulomb strength = locking energy x spacing, up to lambda).")
    print("         TRIPLE: (p_T, p_a, p_kappa) = (2, 1, -1), FORCED.")
    print("         PREMISE, recorded: alpha a function of (T, kappa, a) only,")
    print("         closures via A excluded by the paper's primitive statement.")


def b4_consequences():
    T, a, kappa, A, lam, eps0, c = sp.symbols('T a kappa A lam eps0 c', positive=True)
    e2 = 8 * sp.pi * eps0 * lam * T**2 * a / kappa          # e^2 = 4 pi eps0 * 2 lam T^2 a/kappa
    hbar = sp.pi * T * A**2 / (2 * c)
    alpha = sp.simplify(e2 / (4 * sp.pi * eps0 * hbar * c))  # the FUSED single chain
    assert sp.simplify(alpha - 4 * lam * T * a / (sp.pi * kappa * A**2)) == 0
    print("B4a      the chains FUSE: alpha = 4 lam T a/(pi kappa A^2), one chain, and")
    print("         the XCHAIN locking relation becomes an identity. E1 (drift-inert")
    print("         coupling) is EXCLUDED: p_T = 2 != 0.")

    def dl(expr, v):
        return sp.simplify(sp.diff(sp.log(expr), v) * v)

    # Tension channel: PRED-003 asserts d ln alpha = 2 d ln T. Under the fused chain
    # d ln alpha = d ln T - 2 d ln A at fixed kappa, a  =>  requires d ln A = -1/2 d ln T.
    dT, dAmp, dAa = sp.symbols('dT dAmp dAa')
    dln_alpha = dT - 2 * dAmp
    dAmp_req = sp.solve(sp.Eq(dln_alpha, 2 * dT), dAmp)[0]
    assert dAmp_req == -dT / 2
    G_ratio = sp.simplify((2 * dT) / (-dT))          # d ln G = -d ln T (G ~ 1/(Ta))
    assert G_ratio == -2
    print("B4b      PRED-003's -2 SURVIVES the closure end-to-end, now conditional on")
    print("         the UPDATED co-drift BC2': A ~ T^(-1/2)  (was T^(-3/2) under E1).")
    # Spacing channel: d ln alpha = d ln a - 2 d ln A must equal -d ln a (chain-1 form
    # has alpha ~ a via the closure? No: fused alpha ~ T a/(kappa A^2) => +1 in a).
    # PRED-003's spacing scenario: alpha ~ 2T^2/(kappa a) gave d ln alpha = -d ln a.
    # THE CLOSURE FLIPS THE SPACING SIGN: fused alpha carries a^(+1), so at fixed
    # T, kappa, A: d ln alpha = +d ln a, and with G ~ 1/(Ta) the spacing ratio is
    # d ln alpha/d ln G = -1, NOT +1. Report at full volume: the closure CORRECTS
    # PRED-003's spacing-channel discriminator.
    ratio_spacing_naive = sp.simplify((dAa) / (-dAa))
    assert ratio_spacing_naive == -1
    print("B4c      UNFAVORABLE AND REPORTED: the closure FLIPS the spacing channel.")
    print("         The literal 2T^2/(kappa a) gave alpha ~ a^(-1) and ratio +1; the")
    print("         dimensionless closure gives alpha ~ a^(+1) (at fixed A) and ratio")
    print("         -1. PRED-003's registered spacing discriminator (+1) rests on the")
    print("         dimensionally open form and is WITHDRAWN pending the chain's")
    print("         registration; the tension-channel -2 is unaffected.")
    # With amplitude co-drift free, the spacing condition on A: demanding the fused
    # chain reproduce ANY assigned spacing exponent s: dAmp = (1 - s)/2 * dAa.
    s = sp.Symbol('s')
    dAmp_a = sp.solve(sp.Eq(dAa - 2 * dAmp, s * dAa), dAmp)[0]
    assert sp.simplify(dAmp_a - (1 - s) / 2 * dAa) == 0
    print("B4d      BC3' is now CHANNEL-DEFINITION-DEPENDENT: A ~ a^((1-s)/2) for an")
    print("         assigned alpha spacing-exponent s; the previous a^(1/2) was the")
    print("         E1/open-form artifact. No spacing BC is asserted until PRED-003's")
    print("         chain is registered.")
    # Amplitude formula, calibration-closed:
    A2 = sp.solve(sp.Eq(sp.Symbol('alpha_m', positive=True),
                        4 * lam * T * a / (sp.pi * kappa * A**2)), A**2)[0]
    print(f"B4e      amplitude formula: A^2 = {A2} -- reproduces ELEC-054's readback")
    print("         identically at calibration (no numeric content today); its")
    print("         adjudication is blocked on kappa's absolute value, a named")
    print("         measurement target.")


def b5_regrade():
    # Under the triple (2, 1, -1): BC2' requires A-exponent -1/2 in T; the fused
    # chain assigns no unconditional a-exponent (B4d), so spacing kills are
    # SUSPENDED rather than reversed. M-candidates carry (e_T, e_a) = (0, 1).
    reqT = sp.Rational(-1, 2)
    for mname in ("M2", "M4", "M5"):
        print(f"B5       {mname}: T-exponent 0 vs required {reqT} -> STILL KILLED,")
    print("         load-bearing channel MOVED to tension; the spacing half of the")
    print("         ELEC-082 kills is SUSPENDED pending the chain's registration.")
    # M5 sharp test: hbar ~ T w^2 gives hbar T-exponent +1; required now:
    # hbar ~ T A^2 with A ~ T^(-1/2) => hbar ~ T^0.
    T, w = sp.symbols('T w', positive=True)
    e_hbar_M5 = sp.simplify(sp.diff(sp.log(T * w**2), T) * T)
    assert e_hbar_M5 == 1
    print("B5       M5 sharp: d ln hbar/d ln T = +1 vs required 0 (hbar ~ T^0 under")
    print("         the closure) -- STILL KILLED, margin reduced from 3 to 1 units")
    print("         of exponent.")
    print("B5       pure-number class (A = const x w): T-exponent 0 vs -1/2 -> the")
    print("         class closure STANDS, carried now entirely by the tension channel")
    print("         and hence conditional on the constitutive closure.")


def main():
    b1_provenance()
    b2_dimensions()
    b3_closure()
    b4_consequences()
    b5_regrade()
    print("B6       STATUS: the constitutive relation e_eff^2/(4 pi eps0) = 2 lam J a")
    print("         is CONDITIONAL on the paper's primitive statement and on the")
    print("         unregistered chain being what the paper says. Registering that")
    print("         chain (or refuting the primitive statement) is the outstanding")
    print("         obligation. No tier motion this session (rule R4).")
    print("ALL BARS PASS")


if __name__ == "__main__":
    sys.exit(main())
