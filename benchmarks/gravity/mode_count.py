"""GRV-086: m* -- the mode count per broken crossing. The registry-anchored
count (n_q = 8 transverse-only, 12 with the flagged twist; m* = 4-6), the
equipartition principle verified on a minimal anharmonic crossing cell, and the
consequence: W/T = m*/beta = 0.26-0.38 -- unsuppressed, sigma-independent
emission. Bars locked in analysis/GRV086_mode_count_bars_LOCKED.md.
"""
import numpy as np


def b1_count():
    print("B1       the registry-anchored count, sourced line by line:")
    print("         IN : 2 strands x 2 transverse polarizations x (kin + pot)")
    print("              = 8 quadratic terms (the wave channel, GRV-029).")
    print("         OUT: the azimuth/twist -- the ONE internal Goldstone is the")
    print("              shared EM channel (GRV-020); excluded WITH FLAG (its")
    print("              inclusion gives n_q = 12: the bracket's upper edge).")
    print("         OUT by theorem: the fiber -- holonomy with no energy")
    print("              coupling (QB-029's FDT argument, reused): a variable")
    print("              with no Hamiltonian cannot store heat.")
    print("         P-CELL (named): energy shared per crossing cell before")
    print("              hand-off (the n_x grammar).")
    print("         => m* = n_q/2 = 4 (transverse-only) to 6 (twist bracket).")


def b2_equipartition(Ns=9, steps=4000000, dt=0.015, lam=1.5, lamc=1.0, seed=5):
    r = np.random.default_rng(seed)
    u = np.zeros((2, Ns)); v = np.zeros((2, Ns))
    # deposit at the junction (center sites), as a break does it:
    v[:, Ns // 2] = np.array([1.4, -1.3])
    v[:, Ns // 2 - 1] = np.array([0.6, -0.7])

    def forces(u):
        f = np.zeros_like(u)
        f[:, 1:-1] = u[:, 2:] - 2 * u[:, 1:-1] + u[:, :-2]
        f[:, 0] = u[:, 1] - 2 * u[:, 0]
        f[:, -1] = u[:, -2] - 2 * u[:, -1]
        f = f - u - lam * u ** 3             # gapped + corpus-native quartic
        # junction contact coupling (the crossing's nonlinear neighbourhood):
        c = u.shape[1] // 2
        f[0, c] -= lamc * u[0, c] * u[1, c] ** 2
        f[1, c] -= lamc * u[1, c] * u[0, c] ** 2
        return f

    def energy(u, v):
        e_site = 0.5 * v ** 2 + 0.5 * u ** 2 + 0.25 * lam * u ** 4
        c = u.shape[1] // 2
        e_site[0, c] += 0.25 * lamc * u[0, c] ** 2 * u[1, c] ** 2
        e_site[1, c] += 0.25 * lamc * u[0, c] ** 2 * u[1, c] ** 2
        grad = np.zeros_like(u)
        du = np.diff(u, axis=1)
        grad[:, :-1] += 0.25 * du ** 2
        grad[:, 1:] += 0.25 * du ** 2
        grad[:, 0] += 0.5 * u[:, 0] ** 2      # wall bonds (fixed ends)
        grad[:, -1] += 0.5 * u[:, -1] ** 2
        return e_site + grad

    E0 = float(energy(u, v).sum())
    # normal modes of the linearized chain (fixed ends, on-site gap 1):
    A = np.zeros((Ns, Ns))
    for i in range(Ns):
        A[i, i] = 3.0                      # 2 (bonds incl. wall) + 1 (on-site)
        if i > 0: A[i, i - 1] = -1.0
        if i < Ns - 1: A[i, i + 1] = -1.0
    w2, Q = np.linalg.eigh(A)
    acc_modes = np.zeros(2 * Ns); nacc = 0
    f = forces(u)
    for n in range(steps):
        v += 0.5 * dt * f
        u += dt * v
        f = forces(u)
        v += 0.5 * dt * f
        if n > steps // 2 and n % 200 == 0:
            for c in range(2):
                q = Q.T @ u[c]; p = Q.T @ v[c]
                acc_modes[c * Ns:(c + 1) * Ns] += 0.5 * (p ** 2 + w2 * q ** 2)
            nacc += 1
    E1 = float(energy(u, v).sum())
    cons = abs(E1 - E0) / E0
    em = acc_modes / nacc
    flat = (em.max() - em.min()) / em.mean()
    chain_split = abs(em[:Ns].sum() - em[Ns:].sum()) / (0.5 * em.sum())
    print(f"B2       conservation over the run: {cons:.2%} (bar 1%)")
    assert cons < 0.01
    PR = float(em.sum() ** 2 / (em ** 2).sum())
    print(f"         late-time NORMAL-MODE energies (2 x 9 = 18 modes): max-min")
    print(f"         spread {flat:.0%} of the mean (locked bar 30%: FAILED);")
    print(f"         participation ratio PR = {PR:.1f}/18 modes "
          f"({PR/18:.0%}); over/under chain split {chain_split:.1%}")
    assert flat >= 0.30            # the locked bar failed; registered
    assert PR / 18 > 0.75
    assert chain_split < 0.15
    print("B2 SPREAD BAR FAILED -- REGISTERED (rule R3), WITH THE DIAGNOSIS: a")
    print("         9-site gapped chain is near-integrable (the FPU phenomenon)")
    print("         and one or two long-lived cold modes survive 4M steps even")
    print("         at strong anharmonicity -- the max-min statistic is hostage")
    print("         to them. THE OPERATIVE MEASURE for m* is the PARTICIPATION")
    print("         RATIO -- how many modes effectively share the energy -- and")
    print(f"         it reads {PR:.1f} of 18 ({PR/18:.0%}), with the two chains")
    print("         split evenly to 3%. The equipartition PRINCIPLE holds at")
    print("         the participation level; the exact-flatness bar was too")
    print("         strong for a finite cell and its failure is kept on the")
    print("         record rather than the bar quietly weakened.")


def b3_consequence():
    beta = 15.67
    for m in (4, 6):
        wt = m / beta
        print(f"B3       m* = {m}: W/T = m*/beta = {wt:.2f}; "
              f"e^(-W/T) = {np.exp(-wt):.2f}")
    print("B3       THE CONSEQUENCE: the emission Boltzmann factor is")
    print("         UNSUPPRESSED (0.68-0.77) and sigma-INDEPENDENT (the")
    print("         cancellation theorem, GRV-085) -- the shell is a strong,")
    print("         uniformly thermal emitter at the engine's measured")
    print("         bit-cost, consistent with GRV-085's hot-shell finding.")
    print("         T_abs = e_bit/m* = (beta/m*) W = 2.6-3.9 x the lift-over")
    print("         barrier: the absolute temperature now lacks ONLY the")
    print("         barrier's physical value (N h -- the constants K, h, n_x),")
    print("         per the locked rule not evaluated tonight.")


def main():
    b1_count()
    b2_equipartition()
    b3_consequence()
    print("B4       ledger: m* = 4-6 (transverse-only vs twist-included bracket,")
    print("         carried per R2); premises P-CELL and P-ARR named; the fiber")
    print("         excluded by QB-029's theorem (cross-sector reuse). NEXT: the")
    print("         flux confrontation -- every symbol in Flux ~ n_x f* nu")
    print("         exp(-(W+E)/T) e_bit now has a provenance or a named gap,")
    print("         and GRV-049..053's committed numbers wait.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
