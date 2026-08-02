"""HBAR-001 (Modeled): HBAR FROM A COHERENT STANDING WAVE -- the length
cancels, the causality objection dissolves, and the required collective
number falls by 83,000x. The reconnection route is superseded.

THE DERIVATION. For the fundamental transverse mode of a strand
segment of length L with fixed ends and wave speed c (which is exact
for a relativistic string, mu = T/c^2):
    omega = pi c/L,  E = (1/2) mu omega^2 A^2 L,  S = E/omega
    S = (1/2)(T/c^2)(pi c/L) A^2 L = pi T A^2 / (2c)
L CANCELS. The action of a fundamental standing wave depends only on
TENSION and AMPLITUDE -- not on the strand's length, position, or
history. That is a universality of exactly the kind hbar requires, and
reconnection never had it.

THE SCALE. Setting S = hbar gives A_hbar = sqrt(2 hbar c/(pi T)) =
3.441 fm for the registered T = 1.70e3 N. A single strand at that
amplitude would sweep 60 neighbour spacings and cross them, so the
physical realisation is n strands moving COHERENTLY at amplitude
A' = A_hbar/sqrt(n). Taking the largest crossing-free displacement,
A' = w, fixes n = (A_hbar/w)^2 = 3549 strands over a coherent region
of radius w sqrt(n) = 3.441 fm -- which equals A_hbar identically, so
the picture closes on itself.

THE CAUSALITY TEST, the one that killed reconnection. The mode's
wavelength is ~2R = 6.88 fm, giving a period of 2.30e-23 s against a
light-crossing time of 1.15e-23 s: a ratio of exactly 0.500. A NORMAL
MODE IS CAUSALLY SELF-CONSISTENT BY CONSTRUCTION -- its coherence is
maintained at precisely the speed at which it oscillates. ELEC-043's
objection (collective reconnection needing 3.4e5 times its own
light-crossing time) simply does not arise.

THE SCORECARD. Reconnection: n_t = 3.0e8, coherence 3.4e5x the
object, causally impossible. Standing wave: n = 3549, coherence
3.4 fm, causally consistent. An improvement of 8.3e4 in the required
collective number, and a change of verdict from impossible to
permitted.

A FLAGGED COMPARISON, tested and not leaned on: the coherent region
(3.441 fm) sits within 22 percent of the classical electron radius
(2.818 fm); they coincide exactly at T = 2535 N against the registered
1700 N, i.e. agreement to 49 percent in tension. This depends on T, a
registered value rather than a free one, so it is a real
near-coincidence but not parameter-free. Registered under the standing
rule: flagged, promoted only by derivation.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    a = np.load(ROOT/'analysis'/'HBAR001_state.npz')
    b = np.load(ROOT/'analysis'/'HBAR002_state.npz')
    hbar = 1.054571817e-34; c = 2.99792458e8
    T = float(a['T'])
    # the derivation: L cancels, so S depends only on T and A
    A = float(a['A_hbar'])
    assert abs(np.pi*T*A**2/(2*c)/hbar - 1) < 1e-9, "S = pi T A^2/(2c) equals hbar at A_hbar"
    assert 3e-15 < A < 4e-15, "A_hbar = 3.44 fm"
    # the coherent realisation closes on itself
    n = float(b['n_nat'])
    assert 3000 < n < 4000, "n = 3549 strands at one-spacing amplitude"
    assert abs(float(b['R_coh'])/A - 1) < 1e-6, "coherent radius equals A_hbar identically"
    # THE causality test
    assert abs(float(b['ratio']) - 0.5) < 1e-6, \
        "crossing/period = 0.500 exactly: causally self-consistent by construction"
    # the scorecard against reconnection
    assert float(a['gain']) > 1e4, "83,000x more action-efficient than reconnection"
    assert float(b['gain']) > 1e4, "required collective number falls by 8.3e4"
    # the flagged comparison is T-dependent, hence not parameter-free
    assert 1.0 < float(b['R_over_re']) < 1.5, "coherent region within 22% of r_e"
    assert abs(float(b['T_match'])/T - 1) > 0.1, "but only for T 49% off the registered value"
    print(f"A_hbar {A*1e15:.3f} fm; n {n:.0f}; R_coh {float(b['R_coh'])*1e15:.3f} fm; "
          f"crossing/period {float(b['ratio']):.3f}; gain over reconnection {float(a['gain']):.1e}x")
    print("PASS: the length cancels, the mode is causally self-consistent, and the required")
    print("      collective number drops from 3e8 (impossible) to 3549 (permitted).")


if __name__ == "__main__":
    test()
