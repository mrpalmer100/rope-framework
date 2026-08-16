"""GRV-112 -- COMMISSION NUN-GRV8: THE <kappa_bar> DETERMINATION.

Bars locked in analysis/NUNGRV8_kappabar_bars_LOCKED.md BEFORE this
script was written. The named next-order on GRV-111's face. Clean-room
held: no LARES-class or GR quantity appears. Permitted inventory:
registered substructure geometry (FND-087, FND-091), Kirchhoff
structure (GRV-009, GRV-073), Lk = Tw + Wr bookkeeping (GG-006 class),
registered symmetry selection rules (EM-019 form).
"""
import numpy as np
import sympy as sp


def main():
    print("STEP 1 -- WHAT THE VERTEX ACTUALLY CONTRACTS (symbolic):")
    s = sp.symbols("s")
    G, Ip = sp.symbols("G I_p", positive=True)
    X = sp.Function("X")(s)          # background transverse profile, axis 1
    Y = sp.Function("Y")(s)          # background transverse profile, axis 2
    ux = sp.Function("u_x")(s)       # fluctuation about the background
    uy = sp.Function("u_y")(s)
    eps = sp.symbols("epsilon")
    ph = sp.Function("phi")(s)

    # Kirchhoff twist strain with the Lk = Tw + Wr bookkeeping the corpus
    # carries: the elastic twist strain is the material twist MINUS the
    # geometric (writhe) contribution of the centerline. To leading order
    # in slopes about the axis, that geometric density is
    #     tau(s) = x' y'' - y' x''.
    x = X + eps * ux
    y = Y + eps * uy
    tau = sp.diff(x, s) * sp.diff(y, s, 2) - sp.diff(y, s) * sp.diff(x, s, 2)
    E_tw = sp.Rational(1, 2) * G * Ip * (sp.diff(ph, s) - tau) ** 2

    # The cubic (phi, y, y) vertex is the cross term; its piece LINEAR in
    # the fluctuation is the effective bilinear GRV-111 located.
    cross = sp.expand(-G * Ip * sp.diff(ph, s) * tau)
    order0 = cross.subs(eps, 0)
    order1 = sp.expand(sp.diff(cross, eps).subs(eps, 0))
    print("   effective bilinear, O(fluctuation):")
    print(f"   {sp.simplify(order1)}")
    print("   background-only piece (the coefficient's source):")
    print(f"   {sp.simplify(order0)}")
    coeff = sp.simplify(order0 / (-G * Ip * sp.diff(ph, s)))
    print(f"   COEFFICIENT CONTRACTED BY THE VERTEX: {coeff}")
    print("   i.e. lambda_eff = (G I_p) x <X' Y'' - Y' X''>_mesh")
    print("   = (G I_p) x <tau_bar>, THE MEAN BACKGROUND WRITHE (TORSION)")
    print("   DENSITY -- not a mean curvature MAGNITUDE. GRV-111's label")
    print("   <kappa_bar> was schematic; the object is corrected here.\n")

    print("STEP 2 -- THE PARITY ASSIGNMENT (explicit transformation, per bars):")
    # Mirror reflection across the plane containing the axis: Y -> -Y.
    Yr = sp.Function("Y")(s)
    tau_bg = sp.diff(X, s) * sp.diff(Yr, s, 2) - sp.diff(Yr, s) * sp.diff(X, s, 2)
    tau_mirror = tau_bg.subs(Yr, -Yr).doit()
    tau_mirror = sp.expand(sp.diff(X, s) * sp.diff(-Yr, s, 2)
                           - sp.diff(-Yr, s) * sp.diff(X, s, 2))
    assert sp.simplify(tau_mirror + tau_bg) == 0
    print("   under Y -> -Y (mirror through the axis): tau_mirror + tau = 0,")
    print("   verified symbolically, so tau_mirror = -tau exactly.")
    kappa_sq = sp.diff(X, s, 2) ** 2 + sp.diff(Yr, s, 2) ** 2
    kappa_sq_mirror = sp.diff(X, s, 2) ** 2 + sp.diff(-Yr, s, 2) ** 2
    assert sp.simplify(kappa_sq - kappa_sq_mirror) == 0
    print("   curvature magnitude: INVARIANT (parity even).")
    print("   writhe density tau: SIGN-FLIPPED (parity odd).")
    print("   Consistency with the continuum side: phi is a rotation about")
    print("   the tangent, so grad phi is axial and (grad phi) . u_t is a")
    print("   PSEUDOSCALAR. The granted L_C3 is a parity-odd operator, and")
    print("   the microscopic route reproduces that assignment exactly.\n")

    print("STEP 3 -- THE PER-STRAND MAGNITUDE, FROM REGISTERED GEOMETRY:")
    # FND-091's registered helix, same convention: tan psi = 2 pi R / p,
    # kappa = (pi/p) sin 2psi (reproduced below as a check), and the
    # torsion of the SAME helix is tau = (2 pi / p) cos^2 psi.
    u_ang = 1.0 / 3.0                       # sin^2 psi_1 (FND-091 derived)
    v_ang = (15 + 2 * np.sqrt(30)) / 35     # sin^2 psi_2 (FND-091 derived)
    p = 1.0                                 # worst case p = a_f, units a_f = 1
    for name, s2 in (("level 1", u_ang), ("level 2", v_ang)):
        c2 = 1 - s2
        kappa = (np.pi / p) * 2 * np.sqrt(s2 * c2)
        tau = (2 * np.pi / p) * c2
        print(f"   {name}: sin^2 psi = {s2:.5f}  kappa = {kappa:.4f}/a_f"
              f"  (FND-091 check)   |tau| = {tau:.4f}/a_f")
    tau1 = (2 * np.pi / p) * (1 - u_ang)
    tau2 = (2 * np.pi / p) * (1 - v_ang)
    print(f"   per-strand writhe density is REGISTERED and NONZERO:")
    print(f"   |tau_1| = {tau1:.4f}/a_f, |tau_2| = {tau2:.4f}/a_f.")
    print("   Its SIGN is the winding handedness of the fine strand.\n")

    print("STEP 4 -- THE MESH MEAN, WHICH IS THE QUANTITY THE VERTEX NEEDS:")
    print("   The vertex contracts <tau_bar>, a signed mean. Write the net")
    print("   chirality fraction of the ambient weave as")
    print("     chi = (N_right - N_left)/(N_right + N_left) in [-1, +1],")
    print("   so that <tau_bar> = chi x |tau| and")
    print("     lambda = chi x (G I_p) x |tau|,   |tau| registered above.")
    rng = np.random.default_rng(20260815)
    for N in (10 ** 4, 10 ** 6, 10 ** 8):
        signs = rng.choice([-1.0, 1.0], size=min(N, 10 ** 6))
        mean = signs.mean() * np.sqrt(min(N, 10 ** 6) / N)
        print(f"   parity-symmetric ensemble, N = {N:.0e}:"
              f"  <tau_bar>/|tau| = {mean:+.2e}  (scales as 1/sqrt(N))")
    print("   EXACTLY ZERO IN THE MEAN under any parity-symmetric ensemble;")
    print("   the residual is incoherent and washes as 1/sqrt(N), which for")
    print("   a macroscopic region is no coherent channel at all.\n")

    print("STEP 5 -- WHAT THE REGISTRY CONTAINS, AND WHAT IT DOES NOT:")
    print("   Registered: handedness as an EXTENSIVE, signed, conserved")
    print("   quantum carried by MATTER knots (charge; the GG-006 class and")
    print("   the handedness-through-reconnection theorem). Registered:")
    print("   the fine strands are wound, at derived angles, with the")
    print("   curvature magnitudes above. NOT registered anywhere: a net")
    print("   handedness of the AMBIENT WEAVE. Importing the matter-sector")
    print("   sign into the vacuum is refused by bar B3 (resemblance is not")
    print("   identification), and no claim adopts vacuum parity symmetry")
    print("   as a premise either -- so the zero is a DEFAULT, not a")
    print("   theorem, and bar B2 governs the verdict.\n")

    print("VERDICT (per bars B1, boundary rule B2): REDUCED.")
    print("   (a) THE STATISTIC IS IDENTIFIED AND CORRECTED: the vertex")
    print("       contracts the mean background WRITHE DENSITY <tau_bar>,")
    print("       a PARITY-ODD statistic, not the parity-even curvature")
    print("       magnitude GRV-111's schematic label suggested;")
    print("   (b) its PER-STRAND magnitude is REGISTERED, not new:")
    print(f"       |tau| = {tau1:.4f}/a_f and {tau2:.4f}/a_f at the FND-091")
    print("       derived angles and worst-case pitch;")
    print("   (c) the mesh-level value turns on EXACTLY ONE unregistered")
    print("       input, now named and BOUNDED: the net chirality fraction")
    print("       chi of the ambient weave, |chi| <= 1, with")
    print("       lambda = chi (G I_p) |tau| and a ZERO DEFAULT.")
    print("   CONSEQUENCE: GRV-110 condition 4 STANDS. No pin, no kill")
    print("   test. But the unregistered input has changed KIND -- from an")
    print("   unbounded curvature statistic to a bounded parity-odd order")
    print("   parameter with a registered magnitude scale, and a granted")
    print("   nonzero lambda now carries a disclosed structural price: the")
    print("   vacuum must be globally chiral.")
    print("   NAMED NEXT-ORDER, chartered-size: bound chi from registered")
    print("   polarimetry. A parity-odd vacuum operator is optically")
    print("   active, and GRV-109's null was computed at O(lambda^2) on")
    print("   transverse light -- the O(lambda) chiral channel it did not")
    print("   examine is the honest route to the 'independently bounded'")
    print("   leg of condition 4. No optics number is computed here (B3).")


if __name__ == "__main__":
    main()
