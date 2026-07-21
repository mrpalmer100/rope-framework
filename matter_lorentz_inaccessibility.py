"""CHEM-MET-001 next-order item 1 (Modeled; closed form Derived): the
SELF-CONSISTENT METALLIC SPACING. Dividing the metal's tail-core equilibrium
by the dimer's kills both unknown amplitudes and yields the closed form
    Delta = xi*w/(xi - w) * ln(lam_eff * z / g),
with g the band prefactor (alkali sqrt(z)/2; halogen 5 sqrt(z)/6) and lam_eff
the contact-ANISOTROPY multiplicity (alkali 1: empty shell, bare-core contact
in both geometries; halogen ~5-7: isotropic packing meets the lone-pair lobes
the dimer's oriented sigma-touch avoids).
DERIVED STRUCTURE: (1) metals pack LOOSER than their dimers because core
contacts scale with z while band gain scales with sqrt(z); (2) Delta ~ ln z
only; (3) Delta proportional to core width w.
TEST 1 (one-calibration cross-prediction, Li <-> Na, w ~ ionic-radius rule
declared): +14.4% / -13.0%, inside the 16% tier; inferred widths order with
ionic radii. TEST 2 (halogen closure sharpened): lam_eff = 1 leaves Cl
metallic (DISCLOSED: self-consistency alone insufficient); derived threshold
lam* = 2.77; the lone-pair lobe count supplies ~5-7 > lam*: subcritical,
Cl2 molecular -- the prior session's assumed contact scale upgraded to a
MULTIPLICITY INEQUALITY (structural count > derived threshold).
"""
import numpy as np


LN_ALK = np.log(2*np.sqrt(8.0))
XI = dict(Li=1.336, Na=1.540, Cl=0.995)
D_MEAS = dict(Li=0.367, Na=0.581)
R_ION = dict(Li=0.76, Na=1.02)


def delta_closed(w, xi, lam_z_over_g):
    return (xi*w/(xi - w))*np.log(lam_z_over_g)


def calibrate_w(el):
    # invert Delta = xi*w/(xi-w)*LN for w
    xi, D = XI[el], D_MEAS[el]
    r = D/LN_ALK
    return r*xi/(xi + r)


def sign_and_scaling():
    ok = all(delta_closed(0.25, 1.5, 2*np.sqrt(z)) > 0 for z in (2, 4, 8, 12))
    mono = np.all(np.diff([delta_closed(0.25, 1.5, 2*np.sqrt(z)) for z in (2, 4, 8, 12)]) > 0)
    width = delta_closed(0.30, 1.5, 2*np.sqrt(8.)) > delta_closed(0.15, 1.5, 2*np.sqrt(8.))
    return ok and mono and width


def cross_predict():
    errs = {}
    for src, dst in (("Na", "Li"), ("Li", "Na")):
        w_src = calibrate_w(src)
        w_dst = w_src*R_ION[dst]/R_ION[src]
        pred = delta_closed(w_dst, XI[dst], 2*np.sqrt(8.))
        errs[dst] = (pred - D_MEAS[dst])/D_MEAS[dst]
    return errs


def halogen():
    w = calibrate_w("Na")           # Ne-core width shared: declared
    g = 5*np.sqrt(8.)/6
    def D_of(lam):
        dd = delta_closed(w, XI["Cl"], lam*8/g)
        return g*np.exp(-dd/XI["Cl"])
    lam_star = np.exp(XI["Cl"]*np.log(g)*(1/w - 1/XI["Cl"]))*g/8
    return D_of(1.0), lam_star, D_of(6.0)


def test():
    assert sign_and_scaling(), "sign (looser than dimer), ln-z monotonicity, width law"
    errs = cross_predict()
    assert all(abs(e) < 0.16 for e in errs.values()), "cross-prediction inside 16% tier"
    w_li, w_na = calibrate_w("Li"), calibrate_w("Na")
    assert w_li < w_na, "inferred core widths order with ionic radii"
    D1, lam_star, D6 = halogen()
    assert D1 > 1.0, "DISCLOSED: self-consistency alone leaves the halogen metallic"
    assert 2.0 < lam_star < 4.0, "derived threshold lam* ~ 2.8"
    assert D6 < 1.0, "lone-pair lobe count (~6) exceeds threshold: subcritical, molecular"
    print(f"closed form: Delta = xi*w/(xi-w) ln(lam z/g); metals looser than dimers (z vs sqrt(z))")
    print(f"cross-prediction: Li {errs['Li']*100:+.1f}%, Na {errs['Na']*100:+.1f}% (16% tier); w orders with ionic radii")
    print(f"halogen: D(lam=1) = {D1:.2f} > 1 disclosed; lam* = {lam_star:.2f}; D(lam=6) = {D6:.2f} < 1: Cl2 molecular")
    print("PASS: spacing derived from the tail-core balance; factor 3 upgraded to a multiplicity inequality.")


if __name__ == "__main__":
    test()
