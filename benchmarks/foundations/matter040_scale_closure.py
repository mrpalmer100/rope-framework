"""FND-MATTER-040: the scale closure. The FND-MATTER-039 pipeline executed
under the pre-committed bars: a from R2 (gravity route, eight Planck lengths),
T0 from R5 spending the campaign's ONE calibration on the electron mass
(ring identification GIVEN per FND-MATTER-007/009), l_q from R1 with no
freedom remaining, then Step 4: the l_q/a confrontation against the
pre-drafted grammar (order 1-100 reconciles; wild ratio with bands
propagated = REGISTERED TENSION). Bands: sqrt(D) in [0.1, 10] on a
(dictionary factor), ZPE factor in [1, 3] on the tension split.
Bars restated in analysis/MATTER040_scale_closure_results.md.
"""
import numpy as np

# Measured constants (CODATA-grade)
HBAR = 1.054571817e-34
C = 2.99792458e8
G = 6.67430e-11
ALPHA = 1 / 137.036
ME = 9.1093837015e-31

# Registered inputs
L_RING = 3.141                 # ring ropelength in units of a (FND-MATTER-007)
A_OVER_LP = 8.0                # GRV-095 adoption
SQRT_D_BAND = (0.1, 10.0)      # dictionary factor, pre-committed
ZPE_BAND = (1.0, 3.0)          # FND-MATTER-009's honest lever
GRAMMAR_WINDOW = (1.0, 100.0)  # Step-4 reconciliation window, pre-drafted

# Independent registered T0 anchors (J/m) -- the fingerprint set
T0_LATTICE = 1203.0            # ELEC-052/081 (QCD flux-tube, 1.3% recheck)
T0_SIGMA = 1700.0              # Sigma-route branch
T0_R1_QAREA = HBAR * C / 2.65e-28   # from the fork-invariant quantum area
T0_GRV074 = (9.63e42 / 2.0e39, 9.63e42 / 1.4e39)  # rigidity quantification

# Registered snap-action geometry (GRV-092/093)
BETA, RINGF, H_CORE = 35.4, 0.23, 1.87e-19
NQ_BAND = (1.1e-4, 4.6e-4)


def main():
    lp = np.sqrt(HBAR * G / C**3)
    a = A_OVER_LP * lp
    print(f"STEP 1  a = 8 l_P = {a:.4e} m  (band x/{{0.1,10}} from sqrt(D))")

    t0 = ME * C**2 / (L_RING * a)
    print(f"STEP 2  T0 = m_e c^2 / (L_ring a) = {t0:.4e} J/m")
    print("        THE ONE CALIBRATION SPENT: the electron mass, ring GIVEN.")

    lq = np.sqrt(4 * np.pi * ALPHA * HBAR * C / t0)
    print(f"STEP 3  l_q = sqrt(4 pi alpha hbar c / T0) = {lq:.4e} m")

    ratio = lq / a
    # band propagation: a -> a*f (f in sqrt(D) band) forces T0 -> T0/f,
    # l_q -> l_q*sqrt(f); ZPE z in [1,3] lowers the tension term: T0 -> T0/z,
    # l_q -> l_q*sqrt(z). ratio = ratio0 * sqrt(z/f).
    lo = ratio * np.sqrt(ZPE_BAND[0] / SQRT_D_BAND[1])
    hi = ratio * np.sqrt(ZPE_BAND[1] / SQRT_D_BAND[0])
    print(f"STEP 4  l_q/a = {ratio:.3e}, full band [{lo:.2e}, {hi:.2e}]")
    inside = (lo <= GRAMMAR_WINDOW[1]) and (hi >= GRAMMAR_WINDOW[0])
    assert not inside, "grammar window unexpectedly reached"
    orders_clear = np.log10(lo / GRAMMAR_WINDOW[1])
    print(f"        VERDICT (pre-drafted grammar): REGISTERED TENSION -- the")
    print(f"        band's LOW edge clears the 1-100 window by "
          f"{orders_clear:.1f} orders.")
    print("        No permitted band reconciles the gravity and matter routes.")

    # THE FINGERPRINT: which commitment carries the mismatch
    anchors = {
        "R1 quantum-area T0": T0_R1_QAREA,
        "lattice-anchored T0": T0_LATTICE,
        "Sigma-route T0": T0_SIGMA,
        "GRV-074 rigidity T0 (mid)": np.mean(T0_GRV074),
    }
    print("FINGERPRINT  four independent registered T0 anchors:")
    for k, v in anchors.items():
        print(f"         {k}: {v:.3e} J/m  (closure T0 / anchor = "
              f"{t0 / v:.1e})")
    spread = max(anchors.values()) / min(anchors.values())
    gap = t0 / np.median(list(anchors.values()))
    assert spread < 1e2 and gap > 1e15
    print(f"         The anchors cluster within {spread:.0f}x of each other;")
    print(f"         the closure T0 sits {gap:.1e} above the cluster. The")
    print("         mismatch fingers ONE commitment: R2's identification of")
    print("         the induced-gravity cutoff with THE mesh scale a. The")
    print("         registry's own conjecture note (GRV G-investigation)")
    print("         already reserved that a_grav need NOT equal the mesh")
    print("         spacing -- the tension lands exactly on that reservation.")

    # DIVIDEND: n_q on both branches (h-scaling ambiguity flagged)
    for label, a_b, lq_b in (("closure branch", a, lq),
                             ("EM branch", 1.0e-16, 1.39e-15)):
        nqs = [4 * np.pi * ALPHA * (3 * BETA / (RINGF * chi))
               * (a_b * H_CORE / lq_b**2) for chi in (3.0, 1.0)]
        ok = nqs[0] <= NQ_BAND[1] and nqs[1] >= NQ_BAND[0]
        print(f"DIVIDEND n_q [{label}]: {nqs[0]:.1e}..{nqs[1]:.1e} vs band "
              f"{NQ_BAND[0]:.1e}..{NQ_BAND[1]:.1e} -> "
              f"{'inside' if ok else 'MISS (below)'}")

    # DIAGNOSTIC (no calibration spent): EM branch predicts m_e blind
    m_pred = T0_LATTICE * L_RING * 1.0e-16 / C**2
    print(f"DIAGNOSTIC  EM-branch blind mass: T0 L a / c^2 = {m_pred:.3e} kg "
          f"= {m_pred / ME:.2f} m_e")
    assert 3 < m_pred / ME < 7
    print("         Factor 4.6 from the measured electron mass with NO")
    print("         calibration spent -- just outside the ZPE bar of 2-3.")
    print("         Registered as the whisper, not the win.")

    # ELEC-084 unlock: P23 epoch and P25 location, branch-conditional
    tau_mix_units = 175.0        # STRAND-018, intensive
    for label, a_b in (("EM branch", 1.0e-16), ("closure branch", a)):
        t_unit = a_b / C
        print(f"UNLOCK  [{label}] P23 epoch ~ tau_mix a/c = "
              f"{tau_mix_units * t_unit:.2e} s ; P25 location ~ c/a = "
              f"{C / a_b:.2e} Hz (hbar c/a = "
              f"{HBAR * C / a_b / 1.602e-10:.3g} GeV)")
    print("        Conversions are BRANCH-CONDITIONAL until the tension")
    print("        resolves; the naive dictionary (time unit a/c) is flagged.")
    print("ALL BARS PASS -- verdict: REGISTERED TENSION, culprit fingered.")


if __name__ == "__main__":
    main()
