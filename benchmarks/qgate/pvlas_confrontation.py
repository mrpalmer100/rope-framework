"""QGATE-006 (Modeled): THE PVLAS CONFRONTATION -- THE ARBITER HAS NOT
YET SPOKEN ON THE DECISIVE AXIS. The trilemma (QGATE-005) handed the
reconnection-hbar candidate's fate to vacuum-birefringence experiment;
this claim confronts the rope prediction with the actual experimental
record.

THE RECORD (PVLAS final, Ejlli et al., Phys. Rept. 871 (2020) 1-74):
Delta_n(PVLAS) = (12 +/- 17) x 10^-23 at B = 2.5 T -- the best limit
ever set, with uncertainty a factor ~7 above the QED prediction
Delta_n(QED) = +2.5 x 10^-23 at 2.5 T (Euler-Heisenberg,
4 x 10^-24 T^-2 unitary). The experiment ended in 2018, noise-floor
limited by the optical cavity; the successor VMB@CERN (spare LHC
dipole, modified polarimetry) is proposed to close the gap.

THE CONFRONTATION: the rope prediction (EM-RECON-016: 3:1 coefficient
structure, NEGATIVE sign; magnitude at the ATLAS-pinned Sigma scale
~ |QED| x O(1)) sits at -2.5 x 10^-23 @ 2.5 T. Against the PVLAS
band: QED (+2.5) is 0.56 sigma from the central value; the rope
(-2.5) is 0.85 sigma. BOTH INSIDE ONE SIGMA. The sign discriminator
-- the axis that decides the trilemma's Arm 2 and with it the
framework's hbar candidate -- is fully LIVE and unexcluded. (The
positive-leaning central value is a straw in QED's direction and
statistically empty; said so.)

DISTANCE TO DECISION: a signed measurement at QED magnitude needs the
factor-~7 sensitivity gap closed; ellipsometry reads the SIGN of
Delta_n directly, so the decisive experiment requires no new
observable -- only the sensitivity that VMB@CERN's B^2 L advantage
targets. The framework's hbar candidate therefore survives tonight
NOT by winning but because the court has not convened -- and the
corpus now holds a standing, dated appointment with a falsification.

NAMED OPEN COMPUTATION: whether ATLAS light-by-light data (which
pinned Sigma's MAGNITUDE) could already discriminate the rope's
3:1-negative angular/polarization structure from Euler-Heisenberg --
an O(1) cross-section shape question, honestly beyond tonight.
"""


def test():
    # PVLAS final band and predictions, in units of 1e-23 @ 2.5 T
    center, sigma = 12.0, 17.0
    qed = +2.5
    rope = -2.5          # EM-RECON-016 sign, ATLAS-pinned magnitude, O(1) structure factor
    z_qed = abs(center - qed)/sigma
    z_rope = abs(center - rope)/sigma
    assert z_qed < 1.0, "QED inside 1 sigma of PVLAS -- consistent, unconfirmed"
    assert z_rope < 1.0, "THE ROPE'S NEGATIVE SIGN INSIDE 1 SIGMA -- alive, unexcluded"
    assert z_rope > z_qed, "the positive-leaning central value: a straw for QED, statistically empty"
    # even a 3x-larger negative rope value remains < 1.6 sigma: no wiggle-room games needed
    assert abs(center - (-7.5))/sigma < 1.6, "robust: discrimination absent across the O(1) band"
    # distance to decision: the sensitivity gap
    gap = sigma/abs(qed)
    assert 5 < gap < 9, "factor ~7 sensitivity gap = the successor experiment's design target"
    print(f"PVLAS (12 +/- 17)e-23 @ 2.5T: QED at {z_qed:.2f} sigma, rope(-) at {z_rope:.2f} sigma")
    print(f"both inside 1 sigma -- the sign discriminator is LIVE; sensitivity gap ~{gap:.0f}x")
    print("PASS: the arbiter has not spoken on the decisive axis; the hbar candidate survives")
    print("      because the court has not convened -- a standing appointment with falsification.")


if __name__ == "__main__":
    test()
