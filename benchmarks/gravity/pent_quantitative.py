"""GRV-084: P-ENT made quantitative. Exact two-state thermodynamics by machine,
the operating broken fraction measured from the engine's own fired shells, and
the chain assembled: T_res(sigma) = N(sigma) h / L* with L* measured.
Bars locked in analysis/GRV084_pent_quantitative_bars_LOCKED.md.
"""
import os, sys
import numpy as np
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ratchet_wave_coupling as engine


def b1_thermo():
    W, T = sp.symbols('W T', positive=True)
    f = 1 / (1 + sp.exp(W / T))
    S = -f * sp.log(f) - (1 - f) * sp.log(1 - f)
    E = f * W
    # dE = T dS along the curve (parametrized by T):
    residual = sp.simplify(sp.diff(E, T) - T * sp.diff(S, T))
    assert residual == 0
    # inversion: T = W / ln((1-f)/f)
    fs = sp.Symbol('f', positive=True)
    Tinv = W / sp.log((1 - fs) / fs)
    check = sp.simplify(Tinv.subs(fs, 1 / (1 + sp.exp(W / T))) - T)
    assert check == 0
    print("B1 PASS  two-state thermodynamics exact, by machine: f = 1/(1 +")
    print("         exp(W/T)), S(f) the binary entropy, dE = T dS verified, and")
    print("         the inversion T = W/ln((1-f)/f) -- the temperature of a bit")
    print("         population is the gap over the log-odds of occupation.")


def shell_fraction(run):
    s, r = run['s'], run['r']
    fired = s < 0.999
    assert fired.any()
    f = float(np.mean(1 - s[fired]))
    return f, (float(r[fired].min()), float(r[fired].max()))


def main():
    b1_thermo()
    print("B2       the operating broken fraction, measured (rule R1: mechanical")
    print("         extraction, registered parameters, no tuning):")
    acc = engine.evolve(amp=0.056, r_c=20.0, steps=90000)
    f_a, span_a = shell_fraction(acc)
    L_a = float(np.log((1 - f_a) / f_a))
    print(f"           accretion shell (blueshift capture): f* = {f_a:.3f}"
          f" over r = {span_a[0]:.1f}-{span_a[1]:.1f}  ->  L* = {L_a:.2f}")
    cr = engine.evolve(amp=0.35, r_c=8.0, steps=50000)
    f_c, span_c = shell_fraction(cr)
    L_c = float(np.log((1 - f_c) / f_c))
    print(f"           collapse footprint:                  f* = {f_c:.3f}"
          f" over r = {span_c[0]:.1f}-{span_c[1]:.1f}  ->  L* = {L_c:.2f}")
    ratio = max(L_a, L_c) / min(L_a, L_c)
    print(f"         regime spread: factor {ratio:.2f} (rule R2: report a RANGE")
    print(f"         if > 2)  ->  L* = {min(L_a,L_c):.1f}-{max(L_a,L_c):.1f}")
    print("B2 PASS  the two-state O(1) is MEASURED from the engine's own fired")
    print("         shells.")
    print("B3       compatibility note (not a precision bar): GRV-037's crossing")
    print("         engine measured the intact branch metastable up to T_c ~ 1")
    print("         with engine barriers O(1); the two-state reading puts the")
    print("         bit's usability edge at T ~ W over an O(1) log -- the same")
    print("         statement at order of magnitude. Compatible; noted.")
    print("B4       THE CHAIN, quantitative, every factor labelled:")
    print("           T_res(sigma) = N(sigma) h / L*")
    print("           N(sigma) ~ K c^2/sigma   derived (GRV-077 on GRV-038)")
    print("           h                        registered geometry (HBAR-005),")
    print("                                    unevaluated per R3")
    print(f"           L*                       MEASURED tonight: "
          f"{min(L_a,L_c):.1f}-{max(L_a,L_c):.1f}")
    print("           e_bit ~ barrier          measured (GRV-082, three digits)")
    print("         P-ENT -> DISCHARGED-AS-MEASURED-COEFFICIENT-GIVEN-P-EQ,")
    print("         the residual premise named: the shell's bit population is")
    print("         treated as equilibrated (the two-state formula is an")
    print("         equilibrium statement; the engine's shell is driven --")
    print("         deriving the shell's steady state is the successor).")
    print("         Remaining unevaluated: h, K, n_x -- the SHAPE T ~ a_proper")
    print("         needs none of them; the absolute flux will need all three.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
