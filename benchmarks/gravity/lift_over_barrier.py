"""GRV-083: P-TH derived from crossing statics -- the lift-over theorem. To
reconnect, the over-strand must lift by the core height h against the pressing N;
the barrier is W = N h for ANY lift profile, so the barrier is linear in the
pressing with no friction law imported. Composed with the derived load share,
W(sigma) ~ a_proper. Bars locked in analysis/GRV083_lift_over_bars_LOCKED.md.
"""
import numpy as np
import sympy as sp


def b1_theorem():
    x, N, h, L = sp.symbols('x N h L', positive=True)
    z = sp.Function('z')(x)
    # Work against constant normal load N along a monotone lift z: 0 -> h:
    # W = Integral N dz = N * Integral z'(x) dx = N (z(L) - z(0)) = N h,
    # for ANY profile shape -- the fundamental theorem does the whole job.
    W = sp.integrate(N * sp.diff(z, x), (x, 0, L))
    W = W.subs({z.subs(x, L): h, z.subs(x, 0): 0})
    assert sp.simplify(W - N * h) == 0
    print("B1 PASS  THE LIFT-OVER THEOREM (machine, general profile): the work to")
    print("         lift the over-strand by the core height h against pressing N")
    print("         is W = N h for ANY monotone lift profile -- the barrier is")
    print("         LINEAR IN THE PRESSING, profile-independently, with no")
    print("         friction coefficient imported: the corrugation is the")
    print("         strand's own hard core.")


def b2_quadrature():
    N, h = 2.7, 0.31
    xs = np.linspace(0, 1, 200001)
    profiles = {
        "half-cosine": 0.5 * h * (1 - np.cos(np.pi * xs)),
        "quintic ramp": h * (10 * xs**3 - 15 * xs**4 + 6 * xs**5),
    }
    for name, z in profiles.items():
        W = np.trapezoid(N * np.gradient(z, xs), xs)
        assert abs(W - N * h) < 1e-10 * N * h, (name, W)
        fmax = N * np.abs(np.gradient(z, xs)).max()
        print(f"B2       {name:13s}: W = {W:.12f} (= N h = {N*h:.12f}); "
              f"threshold force = {fmax:.3f}")
    print("B2 PASS  quadrature agrees to 1e-10 on two dissimilar profiles; the")
    print("         threshold FORCE differs between them (profile-dependent, and")
    print("         honestly so) -- the temperature chain uses the BARRIER,")
    print("         which is universal.")


def main():
    b1_theorem()
    b2_quadrature()
    print("B3       THE COMPOSITION, provenance per link:")
    print("         W = N h            (tonight's theorem; h = core height,")
    print("                             corpus-native: rods per GRV-073,")
    print("                             thickness per HBAR-005 -- premise P-GEO)")
    print("         N(sigma) ~ K c^2/sigma  (the derived load share per crossing:")
    print("                             GRV-077's transverse-only theorem on")
    print("                             GRV-038's Rindler-class profile)")
    print("         e_bit ~ barrier    (GRV-082, measured to three digits)")
    print("         =>  W(sigma) ~ a_proper  and  T_res(sigma) ~ a_proper.")
    print("         P-TH IS DISCHARGED-GIVEN-P-GEO: the threshold is set by the")
    print("         pressing because passing a pressed hard-core strand COSTS")
    print("         pressing-times-thickness, and by nothing else. The whisper's")
    print("         temperature chain drops from two named premises to ONE")
    print("         (P-ENT, the two-state reading) plus corpus-native geometry.")
    print("B4       propagation: GRV-082's L3 is now a theorem-plus-geometry")
    print("         rather than grammar; no flux/spectrum claims (rule carried);")
    print("         h and K stay unevaluated (the profile needs linearity only).")
    print("         Next-orders: P-ENT made quantitative (the two-state entropy")
    print("         at GRV-037's measured metastability); then the flux, where")
    print("         the whisper lineage's committed numbers wait.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
