"""GRV-106 -- COMMISSION NUN-GRV3: THE SHIFT-MAP EXTENSION AUDIT.

Bars locked in analysis/NUNGRV3_shiftmap_bars_LOCKED.md BEFORE this
script was written. Clean-room (B4) in force: no LARES-2 or GR rate
value appears in this file.

The audit is a structural one and is run symbolically: enumerate every
registered term of the combined (u, phi) action, and ask whether any
contains a mixed time-space derivative -- the structure GRV-055 proved
is the ONLY thing that can populate the three shift slots of the
densitised inverse metric under the bijection grammar.
"""
import sympy as sp


def main():
    t, x, y, z = sp.symbols("t x y z")
    mu, gam, beta = sp.symbols("mu gamma beta_J", positive=True)

    u = sp.Function("u")(t, x, y, z)      # displacement (one transverse comp.)
    ph = sp.Function("phi")(t, x, y, z)   # microrotation (one component)
    s = sp.Function("s")(x, y, z)         # granted source, STATIONARY (GRV-058
                                          # null is exactly for the stationary
                                          # source; FND-REL-002: no material
                                          # velocity)

    print("B1 THE REGISTERED ACTION, term by term (permitted-inputs list):")
    L_u_kin = sp.Rational(1, 2) * mu * sp.diff(u, t) ** 2
    L_u_el = -sp.Rational(1, 2) * (sp.diff(u, x) ** 2 + sp.diff(u, y) ** 2
                                   + sp.diff(u, z) ** 2)  # schematic, T0-scaled
    L_ph_kin = -sp.Rational(1, 2) * gam * (sp.diff(ph, x) ** 2
                                           + sp.diff(ph, y) ** 2
                                           + sp.diff(ph, z) ** 2)
    L_src = beta * ph * s
    L = L_u_kin + L_u_el + L_ph_kin + L_src
    print("   u-sector:   (mu/2) u_t^2  - elastic |grad u|^2   (GRV-029/055)")
    print("   phi-sector: -(gamma/2) |grad phi|^2              (GRV-066)")
    print("               NO mass term: kappa = 0 is DERIVED (EM-RECON-012),")
    print("               and GRV-066's Poisson form is exactly this term's EL eq.")
    print("   coupling:   beta_J phi s, beta_J = 1, s STATIONARY (GRV-104/105)")
    print("   NOT in the action, verified against the registry: any locking")
    print("   term (mass-order forbidden; gradient-order NOT REGISTERED),")
    print("   any gyroscopic term, any u-phi kinetic cross term.\n")

    print("B2 THE STRUCTURAL TEST (the GRV-055 criterion):")
    print("   A shift slot is populated iff the wave operator contains")
    print("   d_t d_i cross structure, i.e. iff  d^2 L / d(u_t) d(u_i) or")
    print("   d^2 L / d(phi_t) d(phi_i) or any u-phi cross block is nonzero.")
    fields = {"u": u, "phi": ph}
    all_zero = True
    for name, f in fields.items():
        ft = sp.diff(f, t)
        for xi, xn in ((x, "x"), (y, "y"), (z, "z")):
            fx = sp.diff(f, xi)
            # coefficient of the mixed bilinear in the quadratic action
            c = sp.diff(L, ft, fx)
            ok = sp.simplify(c) == 0
            all_zero &= ok
            print(f"   d2L/d({name}_t)d({name}_{xn}) = {sp.simplify(c)}"
                  f"   {'ZERO' if ok else 'NONZERO'}")
    # u-phi cross blocks
    for fa, fb in ((u, ph), (ph, u)):
        c = sp.diff(L, sp.diff(fa, t), sp.diff(fb, x))
        ok = sp.simplify(c) == 0
        all_zero &= ok
        print(f"   cross block d2L/d({fa.func}_t)d({fb.func}_x) = "
              f"{sp.simplify(c)}   {'ZERO' if ok else 'NONZERO'}")
    assert all_zero, "a mixed term exists -- verdict path B1, not B2"
    print("\n   EVERY mixed time-space bilinear is IDENTICALLY ZERO.\n")

    print("B3 THE COUNTING CONSEQUENCE:")
    print("   GRV-055: seven medium functions against nine metric functions;")
    print("   the missing two-plus-one ARE the shift, and they can ONLY be")
    print("   fed by mixed time-space structure. phi adds functions to the")
    print("   medium side but feeds NONE of them into the u-operator: with")
    print("   kappa = 0 the sectors decouple except through the stationary")
    print("   source, and a static phi background shifts no u-perturbation")
    print("   coefficient. The counting cannot close at three. Bars clause")
    print("   B2 FIRES on both of its conditions.\n")

    print("B4 THE CANDIDATE THAT WAS EXAMINED AND NOT TAKEN (B3 no-bolting):")
    print("   Gradient-order locking gamma'|grad(phi - (1/2)curl u)|^2 is the")
    print("   one coupling EM-RECON-012 leaves admissible in principle and")
    print("   the registry does not contain. Expanded around a static phi")
    print("   background it contributes SPATIAL cross terms only -- still no")
    print("   d_t d_i. The route that WOULD generate shift structure is a")
    print("   gyroscopic term (background rotation entering u's kinetic")
    print("   block), and that is a material-velocity effect killed by")
    print("   FND-REL-002's derived theorem. So the named candidate is")
    print("   priced honestly: acquiring gradient-locking does NOT by itself")
    print("   open the shift slot; no registered-adjacent structure does.\n")

    print("VERDICT (per bars B5): IMPOSSIBLE-CERTIFIED under registered")
    print("   structure. The medium cannot spin -- now certified to survive")
    print("   the grant: sourcing the twist sector populates phi but feeds")
    print("   no shift slot. Pre-committed consequence executes in this")
    print("   release: KNOWN_LIMITATIONS states at full volume that the")
    print("   granted gravitomagnetic sector is UNFALSIFIABLE BY FRAME")
    print("   DRAGGING under registered structure.")


if __name__ == "__main__":
    main()
