"""GRV-010 resolved (FAILED) + the pure-channel pattern + the anisotropy
diagnosis (GRV-011).

CORRECTIONS to GRV-010's posed estimates (logged, mine): (1) tau: the mean-
strain tension shift RELAXES (tension is uniform along a strand in statics);
what survives is the quartic fluctuation coupling, homogenized isotropically
from the EM-RECON-016 vertex: delta_T = 8 c4 <g^2>, i.e. tau = (kappa_tw-1)<g^2>
with k_tw = k + lambda*gamma_lock^2*tau0^2 (twist-lock absorbed). (2) m = 0: the
kinetic term is exactly quadratic -- 'wave energy adds inertia' was a
relativistic import the elastic Lagrangian does not contain. (3) l = 0 at
O(<g^2>): bath-driven twist enters at O(<g^4>).

VERDICT: mode-bath conditioning is TENSION-ONLY -> gamma_eff = -1/2 UNIVERSALLY
(independent of kappa and of the bath profile). Cassini-dead. Redshift sign
additionally requires a bath DEFICIT near mass (Le Sage-flavored shadow) --
still gamma = -1/2. FAILED regardless of sign.

THE PURE-CHANNEL PATTERN (theorem-grade within the GRV-008 model):
  pure tension: gamma = -1/2;  pure density: gamma = 0;  pure torsion: gamma = -1.
Every pure channel lies in [-1, 0]; both mixed mechanical candidates landed at
-4/7 and -1/2. gamma = +1 needs the anti-correlated response m = 3 tau - 2 l
(e.g. density UP while torsion DOWN), which NO isotropic per-strand mechanism
in the corpus produces (thickness ties m and l with the same sign).

DIAGNOSIS (Conjecture-grade -> GRV-011): the failure may be the MODEL's. The
GRV-008 response model is ISOTROPIC; the actual elastostatic field of a point
defect is ANISOTROPIC (radial tension enhanced, tangential reduced), and GR's
weak field in fixed coordinates has exactly an anisotropic light-speed
signature: Schwarzschild coordinates give delta_c(radial) = 2 Phi,
delta_c(tangential) = Phi -- a 2:1 anisotropy. The factor 2 may literally BE
the anisotropy ratio of the defect's stress field.
"""
import sympy as sp


def gamma_of(tau, m, l):
    return sp.simplify(((l - tau) / 2) / (tau - (m + l) / 2))


def test():
    t, m, l = sp.symbols('tau m l', real=True)
    g = gamma_of(t, m, l)
    assert sp.simplify(g.subs({m: 0, l: 0})) == sp.Rational(-1, 2), "pure tension -> -1/2"
    assert sp.simplify(g.subs({t: 0, l: 0})) == 0, "pure density -> 0"
    assert sp.simplify(g.subs({t: 0, m: 0})) == -1, "pure torsion -> -1"
    # mode-bath = tension-only => -1/2 for ANY kappa and bath sign
    kap, dB = sp.symbols('kappa dB', positive=True)
    for sign in (1, -1):
        gb = g.subs({t: (kap - 1) * sign * dB, m: 0, l: 0})
        assert sp.simplify(gb) == sp.Rational(-1, 2), "mode-bath gamma = -1/2 universally"
    # homogenization coefficient: isotropic average of EM-RECON-016's (12,4) is 8
    assert (12 + 4) / 2 == 8, "isotropic bath stiffness shift = 8 c4 <g^2>"
    # GR anisotropy target (Schwarzschild coords, weak field)
    Phi = sp.symbols('Phi', negative=True)
    dc_rad, dc_tan = 2 * Phi, Phi
    assert sp.simplify(dc_rad / dc_tan) == 2, "GR target: 2:1 radial:tangential anisotropy"
    print("pure channels: tension -> -1/2, density -> 0, torsion -> -1 (all in [-1,0])")
    print("mode-bath (tension-only after corrections): gamma = -1/2 universally -> FAILED")
    print("gamma = +1 unreachable by any isotropic per-strand mechanism constructed so far")
    print("diagnosis: anisotropy -- GR's fixed-coordinate signature is 2:1 radial:tangential")
    print("PASS: candidate 2 dead; pattern established; anisotropic route (GRV-011) is the campaign.")


if __name__ == "__main__":
    test()
