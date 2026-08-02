"""ELEC-036 (Modeled): THE FORM-FACTOR PROBLEM, QUANTIFIED -- the sector's
gate stops being a hand-wave and becomes a trilemma with three numbers.

THE MEASUREMENT (verified before it is used): the charge form factor is
computed from the model's OWN Poisson source -- Gaussian-smeared samples
along the two curves, exactly the density that generates the field --
spherically averaged over 200 directions. F(0) = 1.000000 and the low-q
values track 1 - q^2<r^2>/6 to five decimals, so the instrument is
sound. Results: rms charge radius 0.9485 model units, F falling to 0.99
at q = 0.263, 0.87 at q = 1, 0.30 at q = 5.

CALIBRATED (ELEC-034): rms charge radius 21.16 fm; the form factor
departs by 1 percent at 2.32 MeV/c. Experiment sees no electron
structure to ~100 GeV/c. The discrepancy is 4.3e4 in momentum, 2.1e4
in size against a conservative 1e-3 fm bound.

THE TRILEMMA, each branch priced:
  A. Keep E = m_e c^2 and let the coupling float to fit the size: the
     required kappa is 7.0e-5 MeV fm, an effective coupling 2.1e4 times
     WEAKER than electromagnetism (alpha_eff ~ 3.5e-7). Consequence:
     the Poisson field in this functional would NOT be the EM field.
  B. Keep kappa = alpha hbar c and let the mass float: the object
     weighs 10.5 GeV, 2.1e4 electron masses. Not an electron.
  C. The medium-probe defense: the photon does not couple to this
     density. Stated precisely, this requires the coupling density to
     be pointlike to 1e-3 fm while the FIELD-SOURCE density has rms
     21 fm -- the two differing in extent by 2.1e4. In classical
     electrodynamics they are the same object, tied by Gauss's law, so
     branch C requires a new coupling mechanism the framework does not
     possess and cannot presently test.

WHAT THIS SETTLES: the two calibration anchors OVERDETERMINE the size,
and the resulting prediction fails by four orders. The framework must
give up an anchor, give up the electron identification, or supply a
coupling theory. No amount of further optimization touches this.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'ELEC036_state.npz')
    a = np.load(ROOT/'analysis'/'ELEC036_audit.npz')
    # B1: the instrument is verified
    Fq = s['Fq']
    assert Fq[0, 1] > 0.999 and Fq[-1, 1] < 0.4, "F falls monotonically over the probed range"
    r2 = float(s['r2'])
    q, F = Fq[1]
    assert abs(F - (1 - q*q*r2/6)) < 1e-4, "low-q expansion reproduces <r^2>: instrument sound"
    # B2: the discrepancy
    assert 15 < float(s['rms_fm']) < 30, "rms charge radius ~21 fm"
    assert float(a['fail']) > 1e4, "fails a 1e-3 fm bound by 2.1e4"
    # B3: the trilemma, each branch priced
    assert float(a['kap_ratio']) > 1e4, "branch A: coupling 2.1e4x weaker than EM"
    assert float(a['m_ratio']) > 1e4, "branch B: mass 2.1e4 m_e = 10.5 GeV"
    assert abs(float(a['kap_ratio']) - float(a['m_ratio']))/float(a['m_ratio']) < 0.01, \
        "A and B carry the SAME factor -- the anchors overdetermine one length"
    print(f"rms {float(s['rms_fm']):.2f} fm; 1% departure at {float(s['q1_fm'])*197.327:.2f} MeV/c; "
          f"fails by {float(a['fail']):.1e}; branch A alpha_eff/alpha = {1/float(a['kap_ratio']):.1e}; "
          f"branch B mass {float(a['m_ratio']):.1e} m_e")
    print("PASS: the gate is quantified -- the two anchors overdetermine the size and the")
    print("      prediction fails by four orders; the trilemma is explicit and priced.")


if __name__ == "__main__":
    test()
