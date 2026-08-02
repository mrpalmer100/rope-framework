"""ELEC-046 -- QGATE-008'S FUNNEL RE-RUN AT THE DERIVED ELEMENTARY ACTION.

Bars locked in analysis/ELEC046_funnel_rerun_bars_LOCKED.md BEFORE this ran.
Replaces the old normalization (kappa = 1.80, tube-level T*D) with ELEC-045's
derived W1 = (pi/(4 sqrt3)) T_s w^2/c and asks whether the chain heals (one
collective number across the funnel's sectors AND the electron sector) or
stays broken between 111 and ~500.

Structural honesty (declared in the locked bars): the matter/chemistry legs
demand hbar by construction; the funnel's only independent legs are the
nuclear Fermi inversion S3 and the single-action consistency itself.
"""
import numpy as np

HBAR = 1.054571817e-34
C = 2.99792458e8
KAPPA3D = np.pi / (4 * np.sqrt(3))          # ELEC-045, closed form
T_S = 1.70e3                                 # J/m (ELEC-040)
# [ELEC-049 SUPERSESSION NOTE] The w = 2.87e-16 m below was a promotion error
# (Ledger A, never registered); adjudicated spacing is w = 5.78e-17 m. This file
# is preserved AS RUN because registered claims pin its arithmetic; ELEC-048's
# two-ledger test shows every verdict survives re-basing. Do not update silently.
W_SP = 2.87e-16                              # m   (ELEC-040)


def main():
    # B1: regression -- the old funnel verbatim (transfer_test.py constants)
    TD, D, kappa_old, hc = 33.8, 0.8 / 27.75, 1.801, 197.327
    W_old = kappa_old * TD * D
    S1 = hc
    m_N = TD * 27.75
    S3 = np.sqrt(2 * m_N * 35.0) / 1.36
    old = np.array([S1 / W_old, S1 / W_old, S3 / W_old])
    spread_old = (old.max() - old.min()) / old.mean()
    b1 = spread_old < 0.10 and 95 < old.mean() < 130
    print(f"B1 regression: old demands {old.round(1)}, common {old.mean():.0f}, "
          f"spread {spread_old*100:.1f}%  [{'PASS' if b1 else 'FAIL -- VOID'}]")
    assert b1, "B1 FAIL"

    # B2: the new universal elementary action and recomputed demands
    W1 = KAPPA3D * T_S * W_SP ** 2 / C       # J s
    nt_universal = HBAR / W1
    S_ratio = np.array([1.0, 1.0, S3 / hc])  # sector residues in units of hbar (unchanged)
    new = S_ratio * nt_universal
    spread_new = (new.max() - new.min()) / new.mean()
    b2 = spread_new < 0.10
    print(f"B2 new action: W1 = {W1:.3e} J s = {W1/HBAR:.3e} hbar; universal demand "
          f"n_t = {nt_universal:.0f}")
    print(f"    sector demands: matter {new[0]:.0f} (hbar by construction), chemistry "
          f"{new[1]:.0f} (inherited), nuclear {new[2]:.0f} (independent)  "
          f"spread {spread_new*100:.1f}%  [{'PASS' if b2 else 'FAIL AND KEPT'}]")

    # B3: THE DECIDER -- funnel's independent leg vs the electron sector's demand
    nt_electron = HBAR / W1                  # ELEC-045's closure demand, same W1
    nt_nuclear = new[2]
    ratio = nt_nuclear / nt_electron
    b3 = 0.5 <= ratio <= 2.0
    print(f"B3 decider: nuclear demands n_t = {nt_nuclear:.0f}, electron sector demands "
          f"n_t = {nt_electron:.0f} (ratio {ratio:.3f})  "
          f"[{'PASS -- THE CHAIN HEALS: one elementary action, one collective number' if b3 else 'FAIL AND KEPT -- the chain stays broken'}]")
    print(f"    Read honestly: the electron demand IS hbar/W1 and the nuclear demand is "
          f"S3/W1 with S3 = {S3/hc:.3f} hbar computed independently of W -- the decider's "
          f"content is (a) S3's independent landing near hbar and (b) ONE action now "
          f"serving both places the old chain carried 111 and 2.95e8.")

    # B4: what dissolves, what replaces
    Rc = np.sqrt(nt_universal) * W_SP
    tau = Rc / C
    print(f"B4 dissolved: D/w = 19 (was derived FROM n_t = 111; dies with it).")
    print(f"    Replacement observables: coherence radius R_c = sqrt(n_t) w = "
          f"{np.sqrt(nt_universal):.1f} w = {Rc:.2e} m; event duration {tau:.2e} s.")
    print(f"    ELEC-043 causality bill at the new n_t: pre-correlation over "
          f"{np.sqrt(nt_universal):.0f} strand spacings (vs 1.7e4 that killed 2.95e8, "
          f"vs 10.5 at the dead 111 cell).")

    # B5: falsifiability guard
    print("B5 guard: n_t ~ %.0f is a CONSISTENCY, not a derivation, until an independent "
          "registered mechanism produces it. Named verification: the weave-reservoir / "
          "FND-MATTER-004 bundle census at coherence radius %.0f w. The claim stays Modeled "
          "with this sentence load-bearing." % (nt_universal, np.sqrt(nt_universal)))
    assert b2 and b3
    print("PASS: the funnel re-run at the derived action -- the demands move 111 -> "
          f"{nt_universal:.0f} coherently and the two-normalization inconsistency is retired.")


if __name__ == "__main__":
    main()
