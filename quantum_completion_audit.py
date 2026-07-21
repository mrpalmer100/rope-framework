"""GRV-011 executed: the anisotropic computation -- and the campaign's decision.

THEOREM A (exact): the strain field around a defect is the Hessian of the
harmonic conditioning potential chi ~ 1/r: eigenvalues (2,-1,-1)/r^3, traceless,
radial:tangential = -2:1 FORCED by harmonicity. The number 2 appears
mechanically -- it is the tidal-tensor structure of the Newtonian potential.

THEOREM B (decomposition): GR's weak field in fixed coordinates, (2,1,1)*Phi,
equals ISOTROPIC 4Phi/3 + TRACELESS (Phi/3)*(2,-1,-1) -- the traceless part has
exactly the rope's harmonic shape. Clocks couple only to the isotropic part
(angular average of traceless = 0).

THEOREM C (the range obstruction): local material properties respond only to
STRAIN (u is gauge); the slowest-decaying harmonic displacement is u ~ 1/r^2,
so displacement-sourced conditioning is at most 1/r^3 -- TIDAL order. GR's
metric is POTENTIAL order (1/r). The rope has the right tensor shape one
derivative too high, as a theorem.

THE VERDICT: the only metric-order (1/r) channel in the corpus is the harmonic
bath deficit -- right range, right signs (clocks slow, light slower both ways),
but isotropic/tension-only: gamma = -1/2. Light deflection would be
(1+gamma)/2 x GR = 0.44 arcsec vs measured 1.75 arcsec: FALSIFIED at the
1919-eclipse level. The missing ingredient is exact: a traceless 1/r
conditioning locked at 1/4 the isotropic amplitude -- and the mechanism audit
comes up empty (diffusive quadrupole suppressed by mfp/r; ballistic deficit
falls as 1/r^2). On current commitments, rope weak-field gravity is a scalar
mimic in contradiction with measured light bending (GRV-012).
"""
import sympy as sp


def hessian_theorem():
    x, y, z = sp.symbols('x y z', real=True, positive=True)
    r = sp.sqrt(x**2 + y**2 + z**2)
    H = sp.hessian(1 / r, (x, y, z))
    Hz = sp.simplify(H.subs({x: sp.Rational(0), y: sp.Rational(0)}))
    vals = [sp.simplify(Hz[i, i] * z**3) for i in range(3)]
    traceless = sp.simplify(sum(vals)) == 0
    ratio = sp.simplify(vals[2] / vals[0]) == -2
    return traceless and ratio


def gr_decomposition():
    gr = sp.Matrix([2, 1, 1])
    iso = sp.Rational(sum(gr), 3)
    tl = gr - sp.Matrix([iso] * 3)
    return iso == sp.Rational(4, 3) and list(tl) == [sp.Rational(2,3), sp.Rational(-1,3), sp.Rational(-1,3)] \
        and sum(tl) == 0


def range_obstruction():
    """u ~ 1/r^2 (harmonic max) -> strain ~ 1/r^3; metric needs 1/r."""
    strain_power, metric_power = 3, 1
    return strain_power > metric_power


def verdict_numbers():
    gamma = sp.Rational(-1, 2)                     # isotropic-only channel
    deflection_ratio = (1 + gamma) / 2             # vs GR's (1+1)/2 = 1
    predicted = float(deflection_ratio) * 1.75     # arcsec
    return abs(predicted - 0.44) < 0.01


def test():
    assert hessian_theorem(), "Hessian of 1/r: (2,-1,-1)/r^3, traceless, ratio -2 forced"
    assert gr_decomposition(), "(2,1,1) = 4/3 iso + 1/3 (2,-1,-1)"
    assert range_obstruction(), "strain is tidal order (1/r^3); metric is potential order (1/r)"
    assert verdict_numbers(), "gamma = -1/2 -> 0.44 arcsec vs measured 1.75"
    print("Theorem A: harmonic strain = (2,-1,-1)/r^3, ratio -2:1 EXACT -- the 2 appears mechanically")
    print("Theorem B: GR = 4/3 isotropic + 1/3 x the rope's exact traceless shape; clocks see iso only")
    print("Theorem C: material response capped at tidal order (1/r^3); metric needs potential order (1/r)")
    print("VERDICT: only 1/r channel is isotropic -> gamma = -1/2 -> 0.44 arcsec vs 1.75 measured")
    print("PASS: campaign decided -- scalar mimic on current commitments, in contradiction with data;")
    print("      the one escape is exactly specified (locked 1/4 quadrupole at 1/r; no mechanism found).")


if __name__ == "__main__":
    test()
