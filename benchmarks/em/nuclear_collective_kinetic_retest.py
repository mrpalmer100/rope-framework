"""NUC-023 (Modeled): THE COLLECTIVE RE-TEST FAILS -- NUC-010's
refutation STANDS, and NUC-022's insight is bounded to quantities that
enter as DIFFERENCES rather than absolutes.

THE TEST. NUC-022 showed that collective (shared-ladder) exclusion
gives the quadratic asymmetry that per-nucleon exclusion cannot, and
suggested NUC-010's refuted kinetic diagnosis failed for the same
per-nucleon reason. The cheapest check: re-run NUC-010's light-nucleus
fit with a COLLECTIVE mode ladder in place of the per-nucleon kappa
z^(2/3).

AN IMPLEMENTATION ERROR, CAUGHT AND FIXED. The first attempt used a
hard-walled box, whose zero-point gives E_kin/A = 52-119 MeV against
the Fermi-gas value of 23. Nucleons sit in a finite well, so kinetic
energy must be measured from the well bottom. Corrected, the ladder
behaves properly: E_kin/A = 0 at A = 4 (a closed shell), 23.55 at
A = 8, 23.96 at 12, 22.25 at 16 -- bracketing the continuum 23.0 and
showing genuine shell structure.

THE RESULT, AND IT IS NEGATIVE:
    no kinetic term (baseline)              RMS 0.888 MeV
    PER-NUCLEON kappa z^(2/3) [NUC-010]     RMS 2.000  (2.25x worse)
    COLLECTIVE ladder, zero-point removed   RMS 19.450 (21.9x worse)
The collective version beats the baseline on ZERO of fifteen nuclei.
NUC-010'S REFUTATION STANDS.

WHY, AND THIS IS THE USEFUL PART. E_kin/A jumps from 0 at A <= 4 (the
first shell is closed) to 23.5 at A >= 5. Calibrating eps on He-4 --
where the collective kinetic cost is exactly zero -- means eps absorbs
no kinetic energy, and every heavier nucleus then pays 23 MeV per
nucleon with no compensating rise in bond count. The absolute kinetic
energy is three times the net binding, so any error in it dominates.

THE SCOPE OF NUC-022, NOW BOUNDED. Collective exclusion rescues the
ASYMMETRY because that quantity is a DIFFERENCE between configurations
at fixed A, where the large absolute kinetic energy cancels and only
the imbalance cost survives. It does NOT rescue the binding baseline,
which needs the ABSOLUTE kinetic energy -- a quantity three times
larger than the answer being computed. COLLECTIVE TREATMENT HELPS
WHERE KINETIC ENERGY ENTERS AS A DIFFERENCE AND HURTS WHERE IT ENTERS
AS AN ABSOLUTE.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'NUCK002_state.npz')
    rn, rl, rc = float(s['r_none']), float(s['r_local']), float(s['r_coll'])
    # the baseline and the per-nucleon result are unchanged
    assert abs(rn - 0.888) < 0.01, "baseline RMS 0.888 MeV"
    assert abs(rl - 2.000) < 0.01, "NUC-010's per-nucleon term: 2.25x worse, reproduced"
    # the collective version is worse still
    assert rc > rl > rn, "collective is worse than per-nucleon, which is worse than nothing"
    assert rc/rn > 10, "21.9x worse than baseline"
    assert int(s['better']) == 0, "beats the baseline on ZERO of fifteen nuclei"
    # the ladder itself is now physically sensible (the fix worked)
    ek = s['ekin']
    assert abs(ek[2]) < 1e-9, "A = 4 is a closed shell: zero kinetic cost"
    assert 20 < ek[6] < 26, "A = 8 gives 23.6 MeV/nucleon, bracketing the Fermi-gas 23.0"
    assert ek.max() < 30, "no hard-box zero-point blow-up after the fix"
    # and the failure mechanism: a step at the shell closure
    assert ek[6] - ek[2] > 20, "E_kin/A jumps by 23 MeV between A = 4 and A = 8"
    print(f"RMS: baseline {rn:.3f}, per-nucleon {rl:.3f} ({rl/rn:.2f}x), collective {rc:.3f} "
          f"({rc/rn:.1f}x); wins {int(s['better'])}/15; E_kin/A jumps 0 -> {ek[6]:.1f} at the shell")
    print("PASS: the collective re-test FAILS -- NUC-010 stands, and NUC-022's insight is")
    print("      bounded to differences, not absolutes.")


if __name__ == "__main__":
    test()
