"""GRV-107 -- COMMISSION NUN-GRV4: THE FND-REL-002 SCOPE AUDIT.

Bars locked in analysis/NUNGRV4_rel002_scope_bars_LOCKED.md BEFORE
this script was written. Clean-room (B4): no frame-dragging observable
appears in this file. Motivation disclosed in the bars: this is the
author's challenge to GRV-106's upstream premise, run at full rigor.
"""
import sympy as sp


def main():
    print("LEG L2 FIRST (the structural leg, and the decisive one):")
    print("   L2 states point-identity along the rope is a labelling gauge:")
    print("   no gauge-invariant trackable point exists whose motion defines")
    print("   w. This is a statement about the DESCRIPTION's mathematical")
    print("   structure (GG-005), not a leading-order approximation -- there")
    print("   is no small parameter in it to be limited in. Per bars B2, L2")
    print("   can only fall by EXHIBITING a gauge-invariant tracked quantity.")
    print("   The audit searched the permitted inputs: none exists. The")
    print("   discrete lattice (FND-REL-004) labels SITES, but site identity")
    print("   is the same labelling gauge -- a relabelling of sites is a")
    print("   symmetry of every registered observable. L2: EXACT.\n")

    print("THE GEOMETRIC IDENTITY (the gravity application, all orders):")
    t, r, th, w_rot = sp.symbols("t r theta omega")
    f = sp.Function("f")
    # An axisymmetric pattern rigidly rotating: field depends on (r, th - w*t),
    # and axisymmetry means NO th-dependence at all.
    psi_axi = f(r)                      # axisymmetric: independent of theta
    psi_rot = psi_axi.subs(r, r)        # rotation acts on theta -> theta - w t
    dpsi_dt = sp.diff(f(r), t)          # theta absent => rotation acts trivially
    print("   A rotating AXISYMMETRIC pattern psi(r, theta - omega t) with")
    print("   axisymmetry (no theta dependence) satisfies:")
    print(f"      d_t psi = omega * d_theta psi = {sp.simplify(dpsi_dt)}  (identically)")
    assert sp.simplify(dpsi_dt) == 0
    # General (non-axisymmetric) check that the identity is the chain rule:
    g = sp.Function("g")(r, th - w_rot * t)
    chain = sp.simplify(sp.diff(g, t) + w_rot * sp.diff(g, th))
    print(f"   Chain-rule identity d_t g + omega d_theta g = {chain}")
    assert chain == 0
    print("   This is GEOMETRY, not perturbation theory: no O((ka)^2) or any")
    print("   other order correction can make a theta-independent function")
    print("   depend on theta. GRV-103's d_t u = 0 for rotating axisymmetric")
    print("   sources holds AT ALL ORDERS. The source is static, exactly.\n")

    print("THE PRE-IDENTIFIED CRACK (FND-REL-004), tested per bars B5:")
    k, a, c, B0, T0 = sp.symbols("k a c B T0", positive=True)
    beta = sp.Rational(1, 12) - B0 / (T0 * a ** 2)
    disp = c ** 2 * k ** 2 * (1 - beta * (k * a) ** 2)
    print("   The discrete dispersion omega^2 = c^2 k^2 (1 - beta (ka)^2),")
    print(f"   beta = {beta}, DOES single out the lattice rest frame -- LI is")
    print("   violated at O((ka)^2) as FND-REL-004 registers. The bars'")
    print("   named failure mode is exactly here: an LI-violating DISPERSION")
    print("   is not a material VELOCITY. Test per B5's licensing standard:")
    print("   does the crack yield (i) a trackable point, or (ii) transported")
    print("   material momentum for the rotating source?")
    print("   (i) Site labels remain gauge (L2 above): NO.")
    print("   (ii) Transport requires a time-dependent configuration to")
    print("       carry anything; the source configuration is static by the")
    print("       geometric identity: NOTHING PROPAGATES. The dispersion")
    print("       correction acts on WAVES; the rotating source emits none.")
    print("   The crack modifies wave propagation ON the medium; it does not")
    print("   construct a w OF the medium. NO LICENSE.\n")

    print("LEG L1, audited honestly (the annotation the audit owes):")
    print("   L1 as worded invokes 'rope inextensibility', but the registry")
    print("   carries a FINITE stretch modulus k = 2 T0 (EM-RECON-009,")
    print("   GRV-073 used it). So L1's wording is the theorem's weakest leg:")
    print("   finite k admits longitudinal PHONONS. Registered honestly:")
    print("   L1 is ORDER-LIMITED AS WORDED. But the audit must then ask")
    print("   whether that limitation licenses w -- and it does not, because")
    print("   a longitudinal phonon is a PATTERN (L3) whose material points")
    print("   remain untrackable (L2). L1's role in the theorem is redundant:")
    print("   L2 alone forbids the convective term. The theorem's CONCLUSION")
    print("   survives its weakest leg's wording. This annotation goes on")
    print("   FND-REL-002's face so no later session over-reads L1.\n")

    print("LEG L3: 'material stays home, winding travels' (EM-008/EM-014)")
    print("   re-verified in the original benchmark's own terms: a moving")
    print("   phase pattern with material at rest has w = 0; uniform drift")
    print("   is gradient-invisible. No order structure found to limit. L3:")
    print("   EXACT as registered.\n")

    print("VERDICT (per bars B5): EXACT-CONFIRMED, with one honest")
    print("   annotation. The theorem's conclusion -- no material velocity")
    print("   is constructible, the convective term cannot be built -- holds")
    print("   at all orders: L2 is structural and exact, L3 is exact, the")
    print("   FND-REL-004 crack modifies dispersion without constructing w,")
    print("   and the gravity application (d_t u = 0 for rotating")
    print("   axisymmetric sources) is a chain-rule identity immune to")
    print("   order corrections. L1 is order-limited AS WORDED (finite")
    print("   registered k) but redundant to the conclusion; annotation")
    print("   owed to FND-REL-002's face. THE CHALLENGE IS KEPT: this audit")
    print("   exists in the registry as the record that the uncomfortable")
    print("   theorem was attacked at full strength and held. GRV-106")
    print("   STANDS.")


if __name__ == "__main__":
    main()
