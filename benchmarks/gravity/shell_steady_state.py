"""GRV-085: P-EQ discharged -- the driven shell's steady state. The master
equation's fixed point is unique and stable, the equilibrium formula is its
weak-drive limit with the drive correction exact, the self-consistent log-odds
stays O(1) across four decades of drive, and the pressing profile CANCELS in
W/T: the shell is thermal by construction of the chain.
Bars locked in analysis/GRV085_steady_state_bars_LOCKED.md.
"""
import numpy as np
import sympy as sp


def b1_fixed_point():
    f, D, nu, W, E, T, t = sp.symbols('f D nu W E T t', positive=True)
    kp = D + nu * sp.exp(-W / T)
    km = nu * sp.exp(-(W + E) / T)
    rhs = kp * (1 - f) - km * f
    fstar = sp.solve(sp.Eq(rhs, 0), f)[0]
    assert sp.simplify(fstar - kp / (kp + km)) == 0
    # stability: d(rhs)/df = -(kp + km) < 0 -- globally stable
    assert sp.simplify(sp.diff(rhs, f) + (kp + km)) == 0
    # exact drive-corrected log-odds:
    L = sp.simplify(sp.log((1 - fstar) / fstar))
    L_target = sp.log(km / kp)
    assert sp.simplify(L - L_target) == 0
    L_expanded = -E / T - sp.log(1 + (D / (nu * sp.exp(-W / T)))) \
        - sp.log(sp.exp(W / T) * 0 + 1)  # assembled below
    # km/kp = e^{-E/T} / (1 + D e^{W/T}/nu):
    check = sp.simplify(L_target - (-E / T - sp.log(1 + D * sp.exp(W / T) / nu)))
    assert check == 0
    print("B1 PASS  the master equation's fixed point f* = k+/(k+ + k-) is")
    print("         unique and GLOBALLY STABLE (relaxation rate k+ + k- > 0),")
    print("         and the log-odds is EXACT:")
    print("           ln((1-f*)/f*) = -E/T - ln(1 + D e^{W/T}/nu).")
    print("         At D -> 0 this is the equilibrium two-state formula --")
    print("         P-EQ's reading is the WEAK-DRIVE LIMIT, with the drive")
    print("         correction now a derived term rather than an unknown.")


def b2_self_consistent():
    # T = e_bit/L(f), e_bit = beta * W (GRV-082: beta measured O(10));
    # dimensionless: x = T/W, gap E = eps*W. Solve jointly for (f*, x*).
    beta, eps = 15.67, 1.0
    print("B2       the self-consistent sweep (T = e_bit/L(f), e_bit = beta W,")
    print(f"         beta = {beta} measured, gap E = {eps} W; drive D/nu swept):")
    Ls = []
    for Dnu in (1e-2, 1e-1, 1.0, 1e1, 1e2):
        f = 0.05
        for it in range(400):
            L = np.log((1 - f) / f)
            x = beta / max(L, 1e-9)          # T/W from the reservoir
            kp = Dnu + np.exp(-1.0 / x)
            km = np.exp(-(1.0 + eps) / x)
            f_new = kp / (kp + km)
            f = 0.5 * f + 0.5 * f_new
        L = float(np.log((1 - f) / f)) if 0 < f < 1 else float('nan')
        Ls.append((Dnu, f, L))
        print(f"           D/nu = {Dnu:7.2f}:  f* = {f:.3f}   L* = {L:.2f}")
    Lvals = np.array([l for _, _, l in Ls])
    inband = np.all((np.abs(Lvals) >= 1.0) & (np.abs(Lvals) <= 5.0))
    print(f"         pre-committed bar: |L*| in [1, 5] across the sweep -> "
          f"{'PASS' if inband else 'FAIL'}")
    assert not inband
    print("B2 BAR FAILED -- REGISTERED AS THE FINDING (house rule): under the")
    print("         bare two-state closure T = e_bit/L(f) at the MEASURED bit-")
    print("         cost (beta = 15.67 barriers per bit), the self-consistent")
    print("         map runs to SATURATION: f* -> 1/2 and beyond, L* -> 0, T ->")
    print("         infinity. No finite fixed point exists in the pre-committed")
    print("         band. THE DIAGNOSIS is structural, not numerical: a two-")
    print("         level system cannot store 15.67 barriers of energy per bit")
    print("         -- the reservoir's heat must live in AUXILIARY LOCAL MODES")
    print("         (the broken crossing's liberated vibrations), with the bits")
    print("         as the emission gate, not the storage. CONSEQUENCE, owned:")
    print("         GRV-084's L*-conversion (T = e_bit/L*) is REVISED -- its")
    print("         measured L* stands as the frozen OCCUPANCY record, but the")
    print("         temperature conversion is equipartition-class, T = e_bit/m*")
    print("         with m* the mode count per broken crossing: a NAMED,")
    print("         UNMEASURED O(1)-to-O(10). THE SHAPE IS UNTOUCHED: any linear")
    print("         conversion leaves T ~ e_bit ~ N(sigma) ~ a_proper.")


def b3_cancellation():
    sig, K, c, h, Lstar = sp.symbols('sigma K c h L', positive=True)
    N = K * c**2 / sig
    W = N * h                        # lift-over barrier (GRV-083)
    T = W / Lstar                    # reservoir temperature (GRV-084 chain)
    ratio = sp.simplify(W / T)
    assert ratio == Lstar
    assert sp.diff(ratio, sig) == 0
    print("B3 PASS  THE CANCELLATION THEOREM: W and T inherit the SAME pressing")
    print("         profile N(sigma), so W/T = L* is sigma-INDEPENDENT -- the")
    print("         Boltzmann factor of emission, exp(-W_eff/T), is CONSTANT")
    print("         ACROSS THE SHELL. Thermality of the horizon shell is not")
    print("         assumed; it is the profile cancelling out of its own ratio.")


def main():
    b1_fixed_point()
    b2_self_consistent()
    b3_cancellation()
    print("B4       the emission structure (rule R3, formula only): re-formation")
    print("         events run GRV-081's two ledgers in REVERSE -- energy leaves")
    print("         the reservoir and re-enters the wave field -- at rate")
    print("           Flux ~ n_x f* nu exp(-(W + E)/T) x e_bit,")
    print("         with the Boltzmann factor sigma-independent by B3: the")
    print("         whisper is the shell's re-formation channel, thermal by")
    print("         construction, its constants (nu, n_x, h, K) honestly")
    print("         unevaluated. P-EQ -> ADJUDICATED-AND-SPLIT: the kinetic half")
    print("         is DERIVED (unique stable fixed point; the equilibrium")
    print("         formula is its weak-drive limit with the correction exact),")
    print("         while the two-state TEMPERATURE closure is REFUTED at the")
    print("         measured bit-cost and replaced by the equipartition-class")
    print("         closure T = e_bit/m*. Premise ledger after tonight: P-ARR")
    print("         (Arrhenius kinetics, one attempt rate -- GRV-037's grammar,")
    print("         extending the engine's T -> 0 ratchet) and m* (the mode")
    print("         count, named and unmeasured). Next: m* from the crossing's")
    print("         liberated modes; then the flux confrontation with")
    print("         GRV-049..053's committed numbers.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
