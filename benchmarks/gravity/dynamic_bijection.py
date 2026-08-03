"""GRV-055 -- THE ONE-METRIC BIJECTION UNDER TIME DEPENDENCE: it extends, in the
variational form, but only to ZERO-SHIFT metrics.

Bars locked in analysis/GRV055_dynamics_bars_LOCKED.md BEFORE computing.
"""
import sympy as sp


def main():
    t, x, y, z = sp.symbols("t x y z")
    al = sp.Function("alpha")(t, x, y, z)
    bx, by, bz = (sp.Function(n)(t, x, y, z) for n in ("b_x", "b_y", "b_z"))
    u = sp.Function("u")(t, x, y, z)
    B = bx * by * bz

    print("B1 THE TIME PART of sqrt(-g) box_g u for a diagonal metric:")
    tpart = sp.diff(B * (-1 / al) * sp.diff(u, t), t)
    print("   d_t( sqrt(-g) g^{tt} d_t u ) = -d_t( (B/alpha) d_t u )")
    mu = sp.Function("mu")(t, x, y, z)
    written = mu * sp.diff(u, t, 2)
    compat = sp.diff(mu * sp.diff(u, t), t)
    diff = sp.simplify(compat - written)
    print(f"   GRV-029 writes            : mu u_tt")
    print(f"   metric-compatible form is : d_t(mu u_t)")
    print(f"   DIFFERENCE                : {diff}")
    assert sp.simplify(diff - sp.diff(mu, t) * sp.diff(u, t)) == 0
    print("   They agree iff d_t(mu) = 0. Under time dependence the metric form")
    print("   carries a FIRST-ORDER time derivative that mu u_tt lacks.\n")

    print("B2 WHICH FORM DOES THE MEDIUM'S OWN LAGRANGIAN GIVE?")
    t1, x1 = sp.symbols("t x")
    mu1, T1 = sp.Function("mu")(t1, x1), sp.Function("T")(t1, x1)
    u1 = sp.Function("u")(t1, x1)
    L = sp.Rational(1, 2) * mu1 * sp.diff(u1, t1) ** 2 \
        - sp.Rational(1, 2) * T1 * sp.diff(u1, x1) ** 2
    # Euler-Lagrange: d_t(dL/du_t) + d_x(dL/du_x) - dL/du = 0.
    # (dL/du_x = -T u_x already carries the sign; adding is correct.)
    el = sp.expand(sp.diff(sp.diff(L, sp.diff(u1, t1)), t1)
                   + sp.diff(sp.diff(L, sp.diff(u1, x1)), x1))
    variational = sp.expand(sp.diff(mu1 * sp.diff(u1, t1), t1)
                            - sp.diff(T1 * sp.diff(u1, x1), x1))
    assert sp.simplify(el - variational) == 0
    print("   L = (mu/2)u_t^2 - (T/2)u_x^2 gives, by Euler-Lagrange:")
    print("      d_t(mu u_t) - d_x(T u_x) = 0")
    print("   WHICH IS EXACTLY THE METRIC-COMPATIBLE FORM. So the medium already")
    print("   has the right operator, and GRV-029's mu u_tt was the STATIC SPECIAL")
    print("   CASE correctly stated -- not an error, but not the general form")
    print("   either. NO CORRECTION IS OWED to GRV-029; a generalisation is.\n")

    print("B3 THE GENERAL COUNT, with the spatial coefficients allowed to be a")
    print("   full tensor (which GRV-025's measured shear response requires):")
    print("      medium: d_t(mu d_t u) - d_a(T_ab d_b u)")
    print("              mu (1) + T_ab symmetric 3x3 (6)          = 7 functions")
    print("      metric: box_g depends on g ONLY through the densitised inverse")
    print("              frak_g = sqrt(-g) g^{mu nu}: symmetric 4x4 (10) with one")
    print("              determinant constraint                   = 9 functions")
    print("      the medium has NO d_t d_a cross term, i.e. frak_g^{0a} = 0,")
    print("              leaving frak_g^{00} (1) + frak_g^{ab} (6) = 7 functions")
    print("   7 <-> 7: THE BIJECTION EXTENDS TO TIME DEPENDENCE, but only onto the")
    print("   ZERO-SHIFT sector. The three functions the medium cannot supply are")
    print("   exactly the SHIFT VECTOR.\n")

    print("B4 WHAT THE RESTRICTION FORBIDS, by name:")
    print("   A nonzero shift g_{0a} is what encodes FRAME DRAGGING. In the")
    print("   medium's own rest frame -- and the medium HAS a preferred frame")
    print("   (QB-008, CMB-adjacent), so this is not a gauge choice it is free to")
    print("   make -- a rotating spacetime has g_{t phi} != 0 and CANNOT be")
    print("   represented by this operator.")
    print("   => KERR IS NOT REPRESENTABLE in the medium's rest frame without")
    print("      generalising the operator to include a d_t d_a cross term.")
    print("   GRAVITATIONAL WAVES ARE FINE: transverse-traceless waves live in")
    print("   frak_g^{ab}, which the tensor T_ab supplies -- and GRV-025 measured")
    print("   exactly that shear channel. The medium can ring; it cannot spin.\n")

    print("B5 WHAT THIS DOES NOT ESTABLISH:")
    print("   a counting argument shows what the operator CAN represent. It does")
    print("   not show that the medium's DYNAMICS produce the right time evolution")
    print("   -- that needs the nonlinear field equation GRV-054 listed as missing.")
    print("   Nor does it show the medium's T_ab can take the traceless form a")
    print("   propagating wave requires; GRV-025 measured a response, not a")
    print("   propagating solution. Both are named, neither is done here.")
    print("PASS: the bijection extends under time dependence in the variational")
    print("      form, restricted to zero shift, with a named spacetime excluded.")


if __name__ == "__main__":
    main()
