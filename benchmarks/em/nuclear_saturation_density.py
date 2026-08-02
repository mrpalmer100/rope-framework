"""NUC-017 (Modeled): THE CONTACT PICTURE AND NUCLEAR SATURATION --
it fails at the charge radius, is consistent at the confinement radius,
and demands a testable nucleon bundle radius of 1.013 fm.

THE TEST. NUC-002 identifies the strong force as bundle CONTACT. If
nuclear matter is nucleons in contact on a close-packed lattice, its
density follows from the nucleon size alone -- no energy scale, no
fitted constant. That is the contact picture's one genuinely
parameter-free prediction, and it has never been checked.

THE RESULT AT THE CHARGE RADIUS -- A FAILURE. With R = 0.8414 fm,
contact spacing 1.683 fm gives rho = 0.2968 fm^-3 against the observed
0.170: 1.75x TOO DENSE. Equivalently, at the observed density and the
charge radius, nucleons fill only 42.4 percent of the nuclear volume --
below random close packing (64 percent) and far below fcc (74 percent).
NUCLEAR MATTER IS NOT A LATTICE OF TOUCHING CHARGE DISTRIBUTIONS.

THE RESULT AT THE CONFINEMENT RADIUS -- CONSISTENT, NOT SHARP. MIT-bag
fits to hadron spectroscopy give a nucleon radius of 0.8-1.1 fm, which
maps to rho = 0.13-0.35 fm^-3, a band 2.6x wide containing the observed
0.170. The agreement at R = 1.0 fm (ratio 1.04) is real but sits at the
centre of a wide band: A CONSISTENCY CHECK, NOT A PREDICTION TO FOUR
PERCENT.

WHAT THE MODEL DEMANDS, AND IT IS TESTABLE. A close-packed contact
lattice at the observed density requires R_contact = 1.013 fm, which is
21 percent above the proton charge radius. In a rope-bundle picture
that is not absurd -- contact happens at the BUNDLE BOUNDARY, not where
the charge sits -- but it is a commitment the framework now carries and
can be checked against any independent determination of the bundle
radius.

AND IT CORRECTS AN INPUT. NUC-005 takes the spacing as d0 ~ 1.9 fm; the
observed saturation spacing is 2.026 fm, so that input is 6 percent low.
Since a_V ~ 6 eps and eps depends on spacing through the Yukawa, a
6 percent spacing error is not negligible for an ABSOLUTE energy scale
quoted to 3 percent.

WHAT THE PICTURE CANNOT DO. It cannot predict saturation from
ENERGETICS. A purely attractive bond model with a hard core collapses
to contact; there is no interior minimum. The observed 42 percent
packing fraction says nuclear matter is held apart by something the
model does not contain -- which is the same conclusion NUC-010 reached
about the kinetic term, arrived at from geometry instead.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'NUCV001_state.npz')
    # the charge-radius failure
    assert abs(float(s['rho_charge'])/float(s['rho_obs']) - 1.75) < 0.05, \
        "contact at the charge radius is 1.75x too dense"
    assert 0.40 < float(s['f_charge']) < 0.45, "42.4 percent packing: not close-packed"
    assert float(s['f_charge']) < 0.64, "below RANDOM close packing, let alone fcc"
    # the confinement-radius band is wide
    band = s['band']
    assert band[0] < float(s['rho_obs']) < band[1], "the observed density lies inside the band"
    assert band[1]/band[0] > 2, "but the band is 2.6x wide: consistency, not a sharp test"
    # the testable demand
    Re = float(s['R_eff'])
    assert abs(Re - 1.013) < 0.01, "the model demands R_contact = 1.013 fm"
    assert Re/float(s['R_charge']) > 1.15, "21 percent above the charge radius"
    # and the corrected input
    assert abs(float(s['nuc005_d0'])/float(s['d_obs']) - 1) > 0.04, \
        "NUC-005's d0 = 1.9 fm is 6 percent below the observed 2.026"
    print(f"charge radius -> rho {float(s['rho_charge']):.4f} vs {float(s['rho_obs']):.3f} "
          f"({float(s['rho_charge'])/float(s['rho_obs']):.2f}x, packing {float(s['f_charge'])*100:.0f}%); "
          f"bag band {band[0]:.3f}-{band[1]:.3f}; demanded R_contact {Re:.3f} fm")
    print("PASS: contact fails at the charge radius, is consistent at the confinement")
    print("      radius within a wide band, and demands a 1.013 fm bundle radius.")


if __name__ == "__main__":
    test()
