"""ROPE PARAMETER CARD VERIFIER: recomputes every relation in
docs/ROPE_PARAMETERS.md and fails if the card drifts.

This exists so the card cannot silently rot the way docs/STATE_OF_THE_PROGRAMME
did (stale by 259 claims before anyone noticed, 1 Aug 2026).
"""
import numpy as np

C_LIGHT = 2.99792458e8
D_C = 1.87e-19          # HBAR-005 strand thickness, m
K_OVER_T0 = 2.0         # EM-RECON-009 stability, GRV-009 evaluation
POISSON = 2.5           # G ~ E/2(1+nu), nu ~ 0.25 -- IMPORTED, unregistered
A_LORENTZ = 1.0e-16

# Sigma PINNED per FND-030 (Commission MU); Sigma-route retained as HISTORICAL
# provenance only -- its 5.10e35 rests on the dead n_t = 111 and is demoted.
SIGMA_PINNED = (3.61e35, 3.70e35)
KAPPA0_CARD = (1.66e-4, 1.68e-4)   # kappa_0 = c/sqrt(eps0 Sigma), FND-031
EPS0 = 8.8541878128e-12
BRANCHES = {"lattice-anchored": (1203.0, 3.61e35),
            "Sigma-route (HISTORICAL, demoted FND-030)": (1700.0, 5.10e35)}

CARD = {  # values as printed in docs/ROPE_PARAMETERS.md
    "Sigma-route (HISTORICAL, demoted FND-030)": dict(a=1.000e-16, w=5.774e-17, mu=1.892e-14,
                        C=5.95e-36, gamma=5.95e-4, E=1.24e41, G=4.95e40),
    "lattice-anchored": dict(a=9.999e-17, w=5.773e-17, mu=1.339e-14,
                             C=4.21e-36, gamma=4.21e-4, E=8.76e40, G=3.50e40),
}


def derive(T0, Sigma):
    a = np.sqrt(3 * T0 / Sigma)
    w = a / np.sqrt(3)
    mu = T0 / C_LIGHT ** 2
    r = D_C / 2
    k = K_OVER_T0 * T0
    E = k / (np.pi * r ** 2)
    G = E / POISSON
    Cc = G * np.pi * r ** 4 / 2
    gamma = Cc / a ** 2
    return dict(a=a, w=w, mu=mu, C=Cc, gamma=gamma, E=E, G=G)


def main():
    print("ROPE PARAMETER CARD -- verifying docs/ROPE_PARAMETERS.md\n")
    worst = 0.0
    for br, (T0, Sigma) in BRANCHES.items():
        d = derive(T0, Sigma)
        print(f"{br}:  T0 = {T0:.0f} J/m,  Sigma = {Sigma:.3e} J/m^3")
        for key, val in d.items():
            card = CARD[br][key]
            dev = abs(val / card - 1)
            worst = max(worst, dev)
            flag = "ok" if dev < 0.01 else "DRIFT"
            print(f"   {key:6s} = {val:.4e}   card {card:.4e}   "
                  f"({dev*100:.2f}%) {flag}")
        # invariants
        assert abs(d["w"] / d["a"] - 1 / np.sqrt(3)) < 1e-12, "w = a/sqrt3 broken"
        assert abs(np.sqrt(T0 / d["mu"]) / C_LIGHT - 1) < 1e-9, "c = sqrt(T0/mu) broken"
        assert abs(d["a"] / A_LORENTZ - 1) < 1e-3, "a must land on the Lorentz bound"
        print(f"   invariants: w/a = 1/sqrt3 EXACT; sqrt(T0/mu) = c; "
              f"a on the bound to {abs(d['a']/A_LORENTZ-1)*100:.2f}%\n")

    # branch-independent ratios
    g = {br: derive(*v) for br, v in BRANCHES.items()}
    ratios = [g[br]["gamma"] / BRANCHES[br][0] for br in BRANCHES]
    spread = abs(ratios[0] / ratios[1] - 1)
    print(f"BRANCH-INDEPENDENT: gamma/T0 = {ratios[0]:.3e} and {ratios[1]:.3e}, "
          f"agreeing to {spread*100:.4f}%")
    assert spread < 1e-3, "gamma/T0 must be branch-independent"
    r = D_C / 2
    print(f"THE THINNESS RATIO: r/a = {r/A_LORENTZ:.2e}, "
          f"(r/a)^2 = {(r/A_LORENTZ)**2:.2e}")
    print("   -- which is why gamma/T0 is ~3.5e-7 and not order unity.")
    # THE PINNED SIGMA AND kappa_0 (FND-030/031): fail if the branch structure
    # is resurrected or the pinned values drift.
    lat_sigma = BRANCHES["lattice-anchored"][1]
    assert SIGMA_PINNED[0] <= lat_sigma <= SIGMA_PINNED[1], "lattice Sigma outside pinned band"
    for S, k_card in zip(SIGMA_PINNED, reversed(KAPPA0_CARD)):
        k0 = C_LIGHT / np.sqrt(EPS0 * S)
        assert abs(k0 / k_card - 1) < 0.01, f"kappa_0 drift at Sigma={S:.2e}"
    print(f"PINNED: Sigma in [{SIGMA_PINNED[0]:.2e}, {SIGMA_PINNED[1]:.2e}] J/m^3; "
          f"kappa_0 = {C_LIGHT/np.sqrt(EPS0*SIGMA_PINNED[1]):.3e}"
          f"-{C_LIGHT/np.sqrt(EPS0*SIGMA_PINNED[0]):.3e} m^3/(s C)")
    assert worst < 0.01, f"card drifted by {worst*100:.2f}%"
    print(f"\nPASS: every card value reproduced to within {worst*100:.2f}%.")


if __name__ == "__main__":
    main()

# v3.16.2: the vacuum tower (conditional on FND-037). Fails if the kappa_pack=1
# conflation resurfaces as the vacuum value or the floor/table drifts.
KAPPA_FLOOR = (50, 250)
K_ME = 2.6065e-14
for kap, a_ref, t0_ref in [(1, 6.006e-17, 434.0), (50, 1.630e-17, 1599), (250, 9.533e-18, 2734)]:
    sv = kap * 3.61e35
    a_k = (3 * K_ME / sv) ** (1 / 3)
    assert abs(a_k / a_ref - 1) < 0.01 and abs((K_ME / a_k) / t0_ref - 1) < 0.01
    assert a_k < 1e-16
print(f"VACUUM TOWER: kappa_pack floor {KAPPA_FLOOR} verified; M-point(kappa) table reproduced")
