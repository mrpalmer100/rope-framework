"""CHEM-HB-003 (Modeled; PARTIAL RESULT, pre-committed bar FAILED): the
registered fix for CHEM-HB-002 -- derive the lone-pair dipole from
CHEM-GEO-001's occupied lobes (charge = the atom's bonding delta, radius = xi,
NO free parameter) and re-run the three dimers blind. Pre-committed pass
condition: N enters the 0.05-0.5 eV band AND the F/O order flips, nothing else
breaking. OUTCOME: HALF met, and reported as such. N-H...N: 0.031 -> 0.056 eV,
ENTERS BAND (nitrogen's single lone pair points at the donor H; the omission
CHEM-HB-002 diagnosed is repaired). O: 0.152 -> 0.226 vs 0.217, now near-exact.
BUT F-H...F: 0.313 -> 1.141 eV, WORSE -- fluorine's THREE lone pairs and
largest delta amplify exactly the atom already overshooting, so the F/O order
does NOT flip (worsens). BAR FAILED. No parameter tuned to force it (the fix
was specified parameter-free in advance; a radius/splitting knob could force
the flip and is REFUSED). WHAT IT TEACHES: point-charge lone pairs at close
range scale as (n_lp * delta / r): monotonic in delta, so they cannot correct
an ordering the same delta got backwards -- the F/O inversion is not a missing
monopole term but a genuine SHORT-RANGE structure effect (Pauli/overlap
saturation at the tight F...F 2.72 A contact) that a purely electrostatic
model of any point-charge arrangement will keep missing. Registered as a
sharper, still-open discrepancy.
"""
import numpy as np

K = 14.3996
ATOMS = dict(F=dict(dchi=1.78, xi=0.64), O=dict(dchi=1.24, xi=0.66), N=dict(dchi=0.84, xi=0.71))
MEAS = dict(O=0.217, F=0.199, N=0.130)


def delta(dchi):
    return 1 - np.exp(-dchi**2/4)


def water(d, xi, D):
    r, th = 0.958, np.deg2rad(104.5)
    don = [(np.array([0,0,0.]),-2*d),(np.array([r,0,0.]),d),(np.array([r*np.cos(th),0,r*np.sin(th)]),d)]
    acc = [(np.array([D,0,0.]),-2*d+2*d),
           (np.array([D+r*np.cos(th/2), r*np.sin(th/2),0]),d),(np.array([D+r*np.cos(th/2),-r*np.sin(th/2),0]),d),
           (np.array([D-xi*0.5,0, xi*0.87]),-d),(np.array([D-xi*0.5,0,-xi*0.87]),-d)]
    return -sum(K*q1*q2/np.linalg.norm(p1-p2) for p1,q1 in don for p2,q2 in acc)


def hf(d, xi, D):
    r, tilt = 0.917, np.deg2rad(63)
    don = [(np.array([0,0,0.]),-d),(np.array([r,0,0.]),d)]
    acc = [(np.array([D,0,0.]),-d+d),(np.array([D+r*np.cos(tilt),r*np.sin(tilt),0]),d),(np.array([D-xi,0,0.]),-d)]
    return -sum(K*q1*q2/np.linalg.norm(p1-p2) for p1,q1 in don for p2,q2 in acc)


def nh3(d, xi, D):
    r = 1.012; b, c = 0.802, 0.523
    don = [(np.array([0,0,0.]),-3*d),(np.array([r,0,0.]),d),
           (np.array([-0.287*r,b*r,c*r]),d),(np.array([-0.287*r,-b*r,c*r]),d)]
    ah = [(np.array([D,0,0.])+r*np.array([0.375,0.927*np.cos(p),0.927*np.sin(p)]),d)
          for p in (0,2*np.pi/3,4*np.pi/3)]
    acc = [(np.array([D,0,0.]),-3*d+d)]+ah+[(np.array([D-xi,0,0.]),-d)]
    return -sum(K*q1*q2/np.linalg.norm(p1-p2) for p1,q1 in don for p2,q2 in acc)


def test():
    m = dict(O=water(delta(ATOMS['O']['dchi']),ATOMS['O']['xi'],2.98),
             F=hf(delta(ATOMS['F']['dchi']),ATOMS['F']['xi'],2.72),
             N=nh3(delta(ATOMS['N']['dchi']),ATOMS['N']['xi'],3.26))
    # HALF-MET, machine-encoded:
    assert 0.05 < m['N'] < 0.5, "PASS half: N enters band with derived lone pair"
    assert abs(m['O'] - MEAS['O']) < 0.05, "O near-exact"
    assert m['F'] > 0.5, "BAR FAILED (encoded): F overshoots -- 3 lone pairs x largest delta"
    assert m['F'] > m['O'], "F/O flip did NOT occur (worsened): the inversion is short-range, not monopole"
    print(f"with derived lone pairs (eV): O {m['O']:.3f}  F {m['F']:.3f}  N {m['N']:.3f}")
    print(f"measured (eV):                O {MEAS['O']:.3f}  F {MEAS['F']:.3f}  N {MEAS['N']:.3f}")
    print("HALF the bar met: N enters band (fix worked for its target), O near-exact;")
    print("F/O flip FAILED -- F overshoots (3 lone pairs, largest delta). No knob applied.")
    print("DIAGNOSIS: point-charge lone pairs are monotonic in delta, so cannot flip an")
    print("order the same delta got backwards. The F/O inversion is short-range structure")
    print("(overlap/Pauli saturation at the 2.72 A contact), not a missing monopole term.")
    print("PASS: partial fix + failed bar both on the books; discrepancy sharpened, still open.")


if __name__ == "__main__":
    test()
