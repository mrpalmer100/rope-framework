"""HBAR-002 (Modeled): THE COHERENCE MECHANISM IS AVAILABLE AT NATURAL
STRENGTH -- AND IT DOES NOT SELECT THE SCALE. The coupling problem is
solved; the quantization problem is exposed and open.

THE MODEL. Strands as a 2D lattice, spacing w, tension T, linear
density mu = T/c^2, with nearest-neighbour transverse coupling
kappa_c (N/m^2):
    mu u_tt = T u_xx + kappa_c [u(i+1)+u(i-1)+u(j+1)+u(j-1) - 4u]
giving omega^2 = c^2 k_par^2 + c_perp^2 k_perp^2 with an INTER-STRAND
wave speed c_perp = w sqrt(kappa_c/mu).

THE COUPLING REQUIREMENT, derived. For n strands to move as one,
transverse information must cross the coherent region within the
mode's period. HBAR-001 measured that ratio as exactly 1/2, so
c_perp >= c/2, giving
    kappa_c = T/(4 w^2) = 1.274e35 N/m^2 = Sigma/4
where Sigma = T/w^2 is the lattice tension energy density. THE
REQUIRED COUPLING IS ONE QUARTER OF THE MEDIUM'S OWN TENSION DENSITY
-- an order-unity fraction, so the mechanism needs NO fine-tuning and
is exactly what a woven mesh would supply. (Note, flagged: the
numerical agreement of T/w^2 with the registered Sigma is a TAUTOLOGY,
since w was defined by w^2 = mu/rho and QGATE-009 already registers
Sigma = rho c^2 as an identity. Not an independent check.)

THE NEGATIVE, and it is the session's real content. With c_perp = c/2
the dispersion makes EVERY mode coherent over its own wavelength --
there is no preferred scale. The family of modes carrying exactly
hbar is a CONTINUUM:
    R = 0.86 fm  -> n = 222,   amplitude 4.00 w,  S = hbar
    R = 3.44 fm  -> n = 3549,  amplitude 1.00 w,  S = hbar
    R = 13.8 fm  -> n = 56784, amplitude 0.25 w,  S = hbar
because n = (R/w)^2 and A' = A_hbar/sqrt(n) conspire so that
n pi T A'^2/(2c) = pi T A_hbar^2/(2c) = hbar identically.

WHAT THIS MEANS FOR HBAR-001: its 3.441 fm did not fall out of the
physics. It followed from the assumption A' = w (the largest
crossing-free amplitude), which is now exposed as that claim's
load-bearing input rather than a derived result. The self-consistency
HBAR-001 celebrated -- coherent radius equalling A_hbar -- is a
consequence of that choice, not evidence for it.

THE GAP, NAMED PRECISELY: the standing-wave route explains why hbar
has the MAGNITUDE it does given T, and it does not explain why action
should come in DISCRETE units at all. Scale, yes; quantization, no.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'HBAR003_state.npz')
    hbar = 1.054571817e-34; c = 2.99792458e8
    T = float(s['T']); w = float(s['w'])
    # the coupling requirement
    assert abs(float(s['kap_req']) - T/(4*w*w))/float(s['kap_req']) < 1e-9, "kappa_c = T/(4w^2)"
    assert abs(float(s['ratio']) - 0.25) < 1e-6, "exactly Sigma/4: an order-unity fraction"
    assert 0.01 < float(s['ratio']) < 1.0, "no fine-tuning required"
    # the tautology flag
    assert abs(float(s['Sigma_calc'])/float(s['Sigma_reg']) - 1) < 0.02, \
        "T/w^2 matches registered Sigma -- but by identity, not independently"
    # THE NEGATIVE: a continuum of modes all carry hbar
    A = float(s['A_hbar'])
    for f in (0.25, 1.0, 4.0):
        R = f*A; n = (R/w)**2; Ap = A/np.sqrt(n)
        S = n*np.pi*T*Ap**2/(2*c)
        assert abs(S/hbar - 1) < 1e-9, f"S = hbar at R = {f}A too: the scale is NOT selected"
    print(f"kappa_c {float(s['kap_req']):.3e} N/m^2 = Sigma/{1/float(s['ratio']):.0f}; "
          f"c_perp = c/2; and S = hbar for every R in the family (checked at 0.25A, A, 4A)")
    print("PASS: the coupling exists at natural strength (no fine-tuning); the scale is NOT")
    print("      selected -- HBAR-001's 3.44 fm rested on its amplitude cap, now exposed.")


if __name__ == "__main__":
    test()
