"""NUC-010 (Failed, kept): THE KINETIC/ZERO-POINT DIAGNOSIS IS REFUTED --
the omission NUC-006 through NUC-009 named as the sole remaining cause
of their residuals makes the model 2.25x WORSE when actually computed.

THE DIAGNOSIS UNDER TEST. NUC-009 closed with 'the kinetic/zero-point
omission now stands ALONE as the diagnosis for the remaining baseline',
inherited from NUC-005 and NUC-006. It had never been computed.

THE DERIVED IMPLEMENTATION, with no freedom. A degenerate Fermi gas at
nuclear saturation (rho = 0.17 fm^-3) gives k_F = 1.360 fm^-1,
E_F = 38.3 MeV and <E_kin>/A = (3/5)E_F = 23.0 MeV. Since E_kin scales
as rho^(2/3) and local density scales as coordination z, the per-nucleon
cost is kappa z^(2/3) with kappa = 23.0/12^(2/3) = 4.389 MeV -- every
number derived, nothing fitted. The bond constant is recalibrated on
He-4 exactly as before, preserving the one-constant discipline.

THE RESULT:
    no kinetic term at all      RMS = 0.888 MeV   (baseline)
    DERIVED Fermi-gas term      RMS = 2.000 MeV   (2.25x WORSE)
The derived term overcorrects: A = 8-16 swing from +0.5 overbinding to
-1.7 to -2.9 underbinding. THE DIAGNOSIS FAILS.

A SECOND CORRECTION, to an intuition tested inside this session. A
CONSTANT kinetic term is not absorbed by recalibration either -- since
B/A = eps*bonds/A - kappa, raising kappa inflates eps and AMPLIFIES the
spread in bonds/A: RMS goes 0.888 -> 2.026 -> 4.789 at E_kin/A = 0, 10,
23 MeV. Constant kinetic energy makes the model worse too.

WHAT DOES HELP, AND WHY IT IS NOT AN ANSWER. Scanning the family
kappa z^p freely, the optimum is p = 1/3, kappa = 3.700, giving
RMS = 0.415 -- less than half the baseline. But z^(1/3) means
E ~ rho^(1/3) ~ 1/r, which is a LENGTH or surface-tension scaling, not
a kinetic one (kinetic energy scales as rho^(2/3), the exponent that
fails). Two fitted parameters over fifteen points, with no derivation.
It is a phenomenological hint that a coordination-dependent correction
of the RIGHT MAGNITUDE exists, and evidence that it is not kinetic.

VERDICT: the sector's inherited explanation for its residuals is wrong.
The residual is real, a coordination-dependent term of about the right
size can absorb it, and that term does not scale like kinetic energy.
"""
import sys, importlib.util, os
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
_spec = importlib.util.spec_from_file_location(
    "nsl", os.path.join(os.path.dirname(os.path.abspath(__file__)), "nuclear_state_labeled.py"))
N = importlib.util.module_from_spec(_spec)
sys.modules["nsl"] = N
_spec.loader.exec_module(N)

EXP = {2: 1.112, 3: 2.827, 4: 7.074, 5: 5.266, 6: 5.332, 7: 5.606, 8: 7.062,
       9: 6.463, 10: 6.498, 11: 6.928, 12: 7.680, 13: 7.470, 14: 7.476,
       15: 7.699, 16: 7.976}


def test():
    s = np.load(ROOT/'analysis'/'NUCK001_state.npz')
    hbar = 1.054571817e-34; mn = 1.674927e-27; MeV = 1.602176634e-13
    # the derived constants carry no freedom
    kF = (3*np.pi**2*0.17e45/2)**(1/3)
    EF = hbar**2*kF**2/(2*mn)/MeV
    assert 35 < EF < 42, "E_F = 38.3 MeV at saturation"
    assert abs(0.6*EF/12**(2/3) - 4.389) < 0.05, "kappa = 4.389 MeV, derived"
    # the diagnosis fails
    base = float(s['rms_base']); der = float(s['rms_derived'])
    assert abs(base - 0.888) < 0.01, "baseline RMS 0.888 MeV"
    assert der > 2*base, "the DERIVED kinetic term makes the model 2.25x worse"
    # a constant term fails too, and is NOT absorbed
    assert float(s['rms_const10']) > base and float(s['rms_const23']) > float(s['rms_const10']), \
        "constant kinetic energy amplifies the residuals rather than being absorbed"
    # what helps is not kinetic
    assert float(s['rms_best']) < 0.5*base, "a fitted z^(1/3) term halves the RMS"
    assert abs(float(s['p_best']) - 1/3) < 0.01, "but the exponent is 1/3, not the kinetic 2/3"
    print(f"E_F {EF:.1f} MeV, kappa {0.6*EF/12**(2/3):.3f} derived; RMS base {base:.3f} -> "
          f"derived {der:.3f} (worse) ; constant 10/23 MeV -> {float(s['rms_const10']):.3f}/"
          f"{float(s['rms_const23']):.3f} ; best fitted p=1/3 -> {float(s['rms_best']):.3f}")
    print("PASS: the kinetic/zero-point diagnosis is REFUTED -- the derived term worsens the")
    print("      model, and what helps scales as rho^(1/3), which is not kinetic.")


if __name__ == "__main__":
    test()
