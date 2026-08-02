"""XSEC-004 (Modeled): THE REPLICATION FAILS TO REPLICATE -- and the
reason weakens XSEC-003. Two samples at the same redshift disagree by
more than the effect either was meant to measure.

THE ATTEMPT. KROSS (Harrison et al. 2017, MNRAS 467, 1965; VizieR
J/MNRAS/467/1965), 586 galaxies at z = 0.6-1.0, reduced by a different
collaboration with a different beam-smearing treatment -- exactly the
independence XSEC-003 was missing. After quality cuts (no AGN, no
irregular flag, no extrapolated velocity, quality <= 2, inclination >=
25 deg, rotation-dominated) 303 galaxies remain at <z> = 0.85.

THE PROBLEM, found before any conclusion was drawn. KROSS publishes
STELLAR masses only (H-band, fixed M/L) and velocities that are
inclination- and beam-corrected but NOT asymmetric-drift corrected.
Both must therefore be supplied by assumption, and g_dagger is
sensitive to both:
    mu_gas    no drift corr    full drift corr
      0.0        2.41e-10         7.42e-10
      0.5        1.78e-10         4.97e-10
      1.0        1.29e-10         3.36e-10
      1.5        9.33e-11         2.70e-10
The range across defensible treatments is a factor of 8.0, while the
A-versus-B separation being tested at this redshift is a factor of
1.61. THE ASSUMPTION SPREAD EXCEEDS THE SIGNAL FIVEFOLD. KROSS cannot
discriminate the hypotheses, and any value quoted from it would be a
statement about the assumed baryon budget.

THE SAMPLES ALSO DISAGREE PHYSICALLY. At the same redshift, RC100
(z < 1.2, n = 32) has median fDM = 0.395 while KROSS (n = 303) has
0.668 under a central treatment. KROSS discs are far more
dark-matter dominated. Part of this is selection -- RC100 chose
massive, large, high-S/N discs -- but the difference is large.

THE FINDING THAT MATTERS MOST, and it is about XSEC-003 rather than
KROSS. RC100's Table B1 lists log M* and log M_baryon SEPARATELY, and
they differ in both directions, because M_baryon is a FITTED PARAMETER
of the rotation-curve model. RC100's g_bar is therefore not
independent of its g_obs, and the RAR test on RC100 is PARTLY
CIRCULAR. KROSS's photometric stellar mass is genuinely independent of
the kinematics but is cruder and omits gas entirely. NEITHER SAMPLE
SUPPORTS A CLEAN TEST.

CONSEQUENCE FOR THE CORPUS: XSEC-003's 7.4 sigma exclusion of
hypothesis B should be read as a statement about RC100's fitted
baryonic masses, not as an independent measurement of the acceleration
scale at high redshift. The prediction is NOT confirmed. It is also
not refuted -- KROSS's central treatments straddle both hypotheses.
The question is reopened.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'XSEC005_state.npz')
    assert int(s['n_kross']) > 250, "303 galaxies after quality cuts"
    assert abs(float(s['zz']) - 0.85) < 0.05, "<z> = 0.85, matching RC100's lowest bin"
    # the sensitivity exceeds the signal
    spread = float(s['spread']); E = float(s['E'])
    assert spread > 5, "assumption spread is a factor 8"
    assert 1.5 < E < 1.7, "the A-vs-B separation is a factor 1.61"
    assert spread > 3*E, "THE SPREAD EXCEEDS THE SIGNAL: KROSS cannot discriminate"
    # the grid straddles both hypotheses
    g = s['grid']
    vals = g[:, 1:].ravel()
    assert vals.min() < float(s['base']), "some treatments fall below hypothesis A"
    assert vals.max() > float(s['base'])*E*2, "others sit far above hypothesis B"
    # the samples disagree physically
    assert float(s['fk_med']) - float(s['fr_lo']) > 0.2, \
        "KROSS fDM 0.668 vs RC100 0.395 at the same redshift"
    print(f"n={int(s['n_kross'])} at <z>={float(s['zz']):.2f}; g_dagger range "
          f"{float(s['lo']):.2e}-{float(s['hi']):.2e} (factor {spread:.1f}) vs signal {E:.2f}; "
          f"fDM {float(s['fr_lo']):.3f} (RC100) vs {float(s['fk_med']):.3f} (KROSS)")
    print("PASS: the replication cannot discriminate -- assumptions outweigh the effect 5:1,")
    print("      and RC100's fitted baryonic masses make XSEC-003 partly circular.")


if __name__ == "__main__":
    test()
