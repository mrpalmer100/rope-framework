"""GRV-077: the load-share premise derived. Exact static conservation of a
directional-tension medium (mu = T/c^2) gives ZERO longitudinal support demand and
transverse support e a_proper/c^2 -- GRV-038's P1, with the transverse-only
sharpening. Bars locked in analysis/GRV077_load_share_bars_LOCKED.md.
"""
import sympy as sp


def b2_b3_conservation():
    # Static diagonal metric, strand along x: g = diag(-alpha(x,y,z)^2, 1, 1, 1)
    t, x, y, z, c = sp.symbols('t x y z c', positive=True)
    alpha = sp.Function('alpha', positive=True)(x, y, z)
    e = sp.Function('e', positive=True)(x, y, z)
    g = sp.diag(-alpha**2, 1, 1, 1)
    ginv = g.inv()
    X = [t, x, y, z]

    def christoffel(g, ginv, X):
        n = 4
        Gam = [[[sp.simplify(sp.Rational(1, 2) * sum(
            ginv[l, m] * (sp.diff(g[m, i], X[j]) + sp.diff(g[m, j], X[i])
                          - sp.diff(g[i, j], X[m])) for m in range(n)))
            for j in range(n)] for i in range(n)] for l in range(n)]
        return Gam

    Gam = christoffel(g, ginv, X)

    # Directional tension medium, strand axis = x:
    # T^0_0 = -e ; T^x_x = p_par ; T^y_y = T^z_z = p_perp ; plus an external
    # contact-force density F_nu supplied by the crossings.
    p_par, p_perp = sp.symbols('p_par p_perp')
    Tmix = sp.diag(-e, p_par, p_perp, p_perp)   # T^mu_nu, mixed

    def div_T(nu):
        # (1/sqrt-g) d_mu(sqrt-g T^mu_nu) - Gam^l_{nu mu} T^mu_l
        sg = alpha  # sqrt(-det g)
        expr = sum(sp.diff(sg * Tmix[m, nu], X[m]) for m in range(4)) / sg
        expr -= sum(Gam[l][nu][m] * Tmix[m, l] for l in range(4) for m in range(4))
        return sp.simplify(expr)

    # Required contact force density F_j = div_T(j) (statics: div T = F)
    F = [div_T(j) for j in range(4)]
    assert sp.simplify(F[0]) == 0                       # stationarity
    # Uniform-e inspection isolates the gravitational load (pressure gradients
    # belong to the medium's internal statics, not the support question):
    Fx = sp.simplify(F[1].subs(e, sp.Symbol('e0')))
    Fy = sp.simplify(F[2].subs(e, sp.Symbol('e0')))
    e0 = sp.Symbol('e0')
    lx, ly = sp.diff(sp.log(alpha), x), sp.diff(sp.log(alpha), y)
    assert sp.simplify(Fx - (e0 + p_par) * lx) == 0
    assert sp.simplify(Fy - (e0 + p_perp) * ly) == 0
    print("B2 PASS  exact covariant conservation (machine Christoffels, no")
    print("         weak-field shortcut): the required contact-force density is")
    print("         F_j = (e + p_j) d_j ln alpha, per principal direction, from")
    print("         one calculation.")
    # The registered closure: p_par = -e (mu = T/c^2), p_perp = 0
    Fx_r = sp.simplify(Fx.subs(p_par, -e0))
    Fy_r = sp.simplify(Fy.subs(p_perp, 0))
    assert Fx_r == 0
    assert sp.simplify(Fy_r - e0 * ly) == 0
    print("B3 PASS  THE THEOREM: with p_par = -e (line energy = tension, the")
    print("         registered identity) and p_perp = 0, the longitudinal support")
    print("         demand VANISHES IDENTICALLY and the transverse demand is")
    print("         f_perp = e a_proper/c^2 (a_proper = c^2 grad_perp ln alpha):")
    print("         every strand element bears load proportional to LOCAL PROPER")
    print("         ACCELERATION, transverse-only -- GRV-038's P1, derived, with")
    print("         the transverse-only sharpening (exactly the component a")
    print("         crossing's pressing can supply).")


def b4_rindler():
    s, c, e, nx, K = sp.symbols('s c e n_x K', positive=True)
    a_proper = c**2 / s                      # near-horizon proper acceleration
    pressing = (e * a_proper / c**2) / nx    # per-crossing share
    assert sp.simplify(pressing - e / (nx * s)) == 0
    print("B4 PASS  the Rindler check: pressing per crossing = e/(n_x s) --")
    print("         GRV-038's K c^2/s form recovered with the load factor now")
    print("         derived; K keeps only the O(1) crossing geometry (P2').")


def main():
    print("B1       stress from registered identities only: e = mu c^2 per")
    print("         strand with mu = T/c^2 (line energy = tension; the identity")
    print("         QGATE-005's additivity chain used), hence p_par = -e; strands")
    print("         at rest push nothing sideways: p_perp = 0.")
    b2_b3_conservation()
    b4_rindler()
    print("B5       propagation: GRV-038's P1 is DISCHARGED-GIVEN-STATICITY; the")
    print("         pressing -> area-law -> whisper chain now rests on (P1')")
    print("         staticity itself (GRV-034's frozen-star reading) and (P2') the")
    print("         O(1) crossing geometry -- both named. The longitudinal null")
    print("         result is NOTED as consistent with tension exhaustion")
    print("         (GRV-034) and not extended. The tensor-coefficient session")
    print("         (the fork's internal test) is re-queued: it requires the")
    print("         GRV-024/025 instrument's normalization conventions read in")
    print("         full, which this session's budget did not cover.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
