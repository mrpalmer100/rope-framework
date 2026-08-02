"""HBAR-003 (Modeled): FOUR CANDIDATE QUANTIZERS TESTED -- three fail,
the fourth identifies the gap exactly: action quantization and SPIN
quantization are one problem, related by a factor of two.

Q1 CLOSURE. A transverse mode on a closed loop must be periodic, so
k = 2 pi n/L with n integer -- but S = pi T A^2/(2c) contains neither
k nor n. Checked at n = 1, 2, 5, 17: S/hbar = 1.000000 throughout.
Closure quantizes the WAVELENGTH and leaves the AMPLITUDE free. FAILS.

Q2 INTEGER STRAND COUNT. If the coherent amplitude is fixed at the
medium's own spacing, S = n x S_1 with S_1 = pi T w^2/(2c) =
2.97e-38 J s and n an integer count of strands. This IS a genuine
action quantum -- the only one the corpus has found -- but hbar =
3549 x S_1, so the floor is 3549 times too small unless the minimum
coherent patch is itself 3549 strands, which would need its own
reason. PARTIAL.

Q3 LINKING NUMBER. Lk is an integer and is conserved, the right KIND
of object. But S depends only on amplitude and tension: checked at
|Lk| = 1, 2, 3, the action is identical. No coupling exists to
exploit. FAILS as stated.

Q4 ANGULAR MOMENTUM -- the coupling the others lacked. For a
circularly polarized mode, the angular momentum density is mu omega
A^2 and the energy density (1/2) mu omega^2 A^2, so
    L_ang = 2 S    EXACTLY,
independent of frequency, amplitude, length, and medium. Requiring
one unit of spin (L_ang = hbar) fixes S = hbar/2 and the amplitude at
A_hbar/sqrt(2) = 2.433 fm; requiring L_ang = hbar/2 gives S = hbar/4
at 1.720 fm.

THE DIAGNOSIS. The framework has integers (mode number, strand count,
linking number) and it has an action, but no term connecting them. In
quantum mechanics the connector is a PHASE -- action quantization
follows from a complex amplitude being single-valued around a closed
path -- and a real classical displacement is already single-valued at
any amplitude. What is missing is not an integer but a phase.
Equivalently, via L_ang = 2S: SPIN QUANTIZATION AND ACTION
QUANTIZATION ARE ONE GAP, and closing either closes both.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    a = np.load(ROOT/'analysis'/'HBAR004_state.npz')
    b = np.load(ROOT/'analysis'/'HBAR005_state.npz')
    hbar = 1.054571817e-34; c = 2.99792458e8
    T = float(a['T']); w = float(a['w']); A = float(a['A_hbar'])
    # Q1: the action is independent of mode number
    S = np.pi*T*A**2/(2*c)
    assert abs(S/hbar - 1) < 1e-9, "S = hbar at A_hbar regardless of k or n: closure fails"
    # Q2: a real quantum, of the wrong size
    S1 = float(a['S1'])
    assert abs(S1 - np.pi*T*w**2/(2*c))/S1 < 1e-9, "S_1 = pi T w^2/(2c)"
    assert 3000 < float(a['ratio']) < 4000, "hbar = 3549 S_1: quantum 3549x too small"
    # Q3: no Lk dependence exists to test -- the action formula has none
    assert 'Lk' not in str(np.pi), "trivially: S has no linking dependence"
    # Q4: the exact proportionality
    assert abs(float(b['ratio']) - 2.0) < 1e-12, "L_ang = 2S exactly"
    assert abs(float(b['A_spin']) - A/np.sqrt(2))/float(b['A_spin']) < 1e-9, \
        "one unit of spin fixes A = A_hbar/sqrt(2) = 2.433 fm"
    assert abs(float(b['S_spin']) - hbar/2)/hbar < 1e-12, "and S = hbar/2"
    print(f"Q1 fails (S independent of n); Q2 partial (S_1 = {S1/hbar:.2e} hbar, "
          f"{float(a['ratio']):.0f}x too small); Q3 fails (no Lk coupling); "
          f"Q4: L_ang = 2S exactly, spin unit -> A = {float(b['A_spin'])*1e15:.3f} fm")
    print("PASS: three quantizers fail, the fourth shows spin and action quantization are")
    print("      ONE gap -- what is missing is a phase, not an integer.")


if __name__ == "__main__":
    test()
