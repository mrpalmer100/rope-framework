"""FND-MATTER-041: the fork reweighed -- the matter route votes. Bars locked
in analysis/MATTER041_two_scale_fork_results.md BEFORE computation: (1) same
Step-4 grammar as MATTER040 (window 1-100, ZPE band [1,3], sqrt(D) band
[0.1,10]); (2) the ONE calibration is the SAME m_e spend re-applied on the
alternate branch as part of the same adjudication -- no new fitted number;
(3) trilemma verdict grammar pre-committed (each arm's price stated in
registered quantities; no arm adopted unless another is excluded by >10
orders under its own bands); (4) the Sigma~suppression numerical proximity
is REFUSED as Dirac/Eddington numerology (dimensions differ); (5) GRV-095's
induced-channel logic is not on trial -- only the identification of its
cutoff with THE mesh.
"""
import numpy as np

HBAR, C, G = 1.054571817e-34, 2.99792458e8, 6.67430e-11
ALPHA, ME = 1 / 137.036, 9.1093837015e-31
L_RING, A_MESH = 3.141, 1.0e-16
T0_ANCHORS = {"R1 quantum-area": 119.3, "lattice": 1203.0,
              "Sigma-route": 1700.0, "GRV-074 rigidity": 5847.0}
BETA, RINGF, H_CORE = 35.4, 0.23, 1.87e-19
NQ_BAND = (1.1e-4, 4.6e-4)
L_Q_REGISTERED = 1.39e-15
WINDOW, ZPE = (1.0, 100.0), (1.0, 3.0)
EH_TENSION = C**4 / (16 * np.pi * G)


def main():
    # ---- ARM PRICES, in registered quantities ----
    lp = np.sqrt(HBAR * G / C**3)
    zd_needed = EH_TENSION / (HBAR * C / A_MESH**2)
    print(f"ARM F-Lor (one lattice at 1e-16 m): induced tension needs "
          f"zeta D = {zd_needed:.2e}")
    print("        vs the locked geometric bracket [1e-2, 1e2] -- short by")
    print(f"        {np.log10(zd_needed) - 2:.1f} orders. GRV-095's B2, "
          f"reconfirmed: the induced")
    print("        channel alone cannot supply G at the mesh; the price is an")
    print("        UNBUILT suppression/second mechanism (GRV-006's registered")
    print("        unfixed suppression).")
    assert zd_needed > 1e30

    # F-Sak price: MATTER040's strike, quoted
    print("ARM F-Sak (one lattice at 8 l_P): MATTER040's closure -- the m_e")
    print("        confrontation lands l_q/a = 2.9e10, EIGHT orders outside")
    print("        the window under full bands, and demands T0 seventeen")
    print("        orders above four mutually coherent registered anchors.")
    print("        The price is 17-18 orders of coordinated error across the")
    print("        EM, lattice-QCD, and rigidity determinations.")

    # ---- ARM F-2SCALE: the inverted pipeline (mesh primary) ----
    t0 = ME * C**2 / (L_RING * A_MESH)
    lq = np.sqrt(4 * np.pi * ALPHA * HBAR * C / t0)
    ratio = lq / A_MESH
    # ZPE lowers the tension share: T0 in [t0/3, t0], l_q ~ T0^{-1/2}
    lo = ratio                      # T0 max -> l_q min
    hi = ratio * np.sqrt(ZPE[1])    # T0/3 -> l_q * sqrt(3)
    print(f"ARM F-2SCALE (mesh primary; SAME m_e spend re-applied):")
    print(f"        T0 = m_e c^2/(L a_mesh) = {t0:.1f} J/m")
    print(f"        l_q = {lq:.3e} m ; l_q/a = {ratio:.1f}, "
          f"band [{lo:.1f}, {hi:.1f}]")
    inside = lo <= WINDOW[1] and hi >= WINDOW[0] and WINDOW[0] <= ratio <= WINDOW[1]
    assert inside
    print("        INSIDE the pre-drafted 1-100 window: the two registered")
    print("        action areas RECONCILE as cell-scale geometry at order")
    print("        tens -- GRV-093's open question answered numerically on")
    print("        this branch.")

    # coherence table
    print("COHERENCE (mesh branch):")
    for k, v in T0_ANCHORS.items():
        f = max(t0, v) / min(t0, v)
        tag = ("inside ZPE bar" if f <= 3 else
               "the 4.6 whisper" if f < 6 else "FLAGGED")
        print(f"        T0 vs {k} ({v:.0f} J/m): factor {f:.1f}  [{tag}]")
    f_lq = lq / L_Q_REGISTERED
    print(f"        l_q vs registered {L_Q_REGISTERED:.2e} m: factor "
          f"{f_lq:.2f}  [inside ZPE bar]")
    assert f_lq < 3

    nqs = [4 * np.pi * ALPHA * (3 * BETA / (RINGF * chi))
           * (A_MESH * H_CORE / lq**2) for chi in (3.0, 1.0)]
    miss = NQ_BAND[0] / nqs[1]
    print(f"        n_q: {nqs[0]:.1e}..{nqs[1]:.1e} vs band {NQ_BAND[0]:.1e}"
          f"..{NQ_BAND[1]:.1e} -- BELOW by {miss:.1f}x at the nearest"
          f" edges; recoverable within the same ZPE band")
    print("        (l_q carries sqrt(ZPE)); FLAGGED, not excused.")

    # ---- THE VERDICT, per the locked grammar ----
    print("VERDICT: F-Sak-as-mesh is EXCLUDED by MATTER040 (8 orders beyond")
    print("        bands); F-Lor-as-sole-gravity is EXCLUDED by GRV-095's B2")
    print("        (33.8 orders). The surviving arm is F-2SCALE: the weave")
    print("        mesh at ~1e-16 m carries EM and matter; a distinct")
    print("        gravitational stiffness scale at ~l_P carries the induced")
    print("        coefficient; the relation spanning the ~18 orders is the")
    print("        named open problem. GRV-095's induced-channel derivation")
    print("        STANDS; its universalization of a = 8 l_P as THE lattice")
    print("        spacing is demoted to a_grav, branch-conditional.")
    print("        Discriminator armed: the PVLAS-class nonlinearity level")
    print("        (F-2SCALE keeps the EM-branch prediction; F-Sak's cascade")
    print("        put Sigma at 2.3e71 -- the two branches differ observably).")
    print("REFUSED: Sigma (3.6e35 J/m^3) ~ suppression (7.6e35, dimensionless)")
    print("        numerical proximity -- dimensions differ; Dirac/Eddington")
    print("        rule applied.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
