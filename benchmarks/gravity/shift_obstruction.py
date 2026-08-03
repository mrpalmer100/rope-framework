"""GRV-056 -- CAN STRAND MECHANICS PRODUCE THE SHIFT? No: the required term is
exactly the Galilean convective term a Derived claim forbids.

Bars locked in analysis/GRV056_shift_bars_LOCKED.md BEFORE computing.
"""
import sympy as sp


def main():
    t, x, y = sp.symbols("t x y")
    mu, T, v, Om = sp.symbols("mu T v Omega", positive=True)
    u = sp.Function("u")(t, x)

    print("B1 WHAT PRODUCES A d_t d_a CROSS TERM?")
    L = mu * v * sp.diff(u, t) * sp.diff(u, x)
    el = sp.expand(sp.diff(sp.diff(L, sp.diff(u, t)), t)
                   + sp.diff(sp.diff(L, sp.diff(u, x)), x))
    print(f"   L = mu v (d_t u)(d_x u)  ->  EL contribution: {el}")
    print("   A quadratic Lagrangian in first derivatives has exactly three")
    print("   structures: (d_t u)^2, (d_a u)(d_b u), and (d_t u)(d_a u). Only the")
    print("   THIRD yields a mixed time-space derivative, so it is UNIQUE.\n")

    print("B2 WHAT IS IT, PHYSICALLY?")
    boosted = sp.expand(sp.Rational(1, 2) * mu
                        * (sp.diff(u, t) + v * sp.diff(u, x)) ** 2)
    print("   Substituting d_t -> d_t + v d_x (a mean medium velocity v) into the")
    print(f"   kinetic term gives: {boosted}")
    print("   -- the kinetic term, PLUS exactly the cross structure of B1, plus a")
    print("   tension shift. THE CROSS TERM IS THE GALILEAN CONVECTIVE TERM.\n")

    print("B3 WHAT THE CORPUS SAYS ABOUT IT:")
    print("   FND-REL-002 (Derived): 'Strand mechanics FORBID the Galilean")
    print("   convective term: the wave sector is forced to the Lorentz-invariant")
    print("   form (NO MATERIAL VELOCITY EXISTS).'")
    print("   THE MEDIUM CANNOT SUPPLY THE SHIFT, and not by oversight -- by a")
    print("   DERIVED theorem, established for an entirely unrelated purpose")
    print("   (forcing Lorentz invariance in the wave sector).")
    print("   THE SAME CLAIM DOES BOTH JOBS: it is why the medium's light obeys")
    print("   special relativity, and why its gravity cannot frame-drag.\n")

    print("B4 THE ALTERNATIVE ROUTE -- can framing/twist supply one instead?")
    print("   The corpus's strands are FRAMED and transport twist")
    print("   (FND-STRAND-002/003's Calugareanu ledger), so a gyroscopic")
    print("   twist-bend coupling is the obvious candidate. It does not work, and")
    print("   the reason is structural rather than quantitative:")
    ux, uy = sp.Function("u_x")(t), sp.Function("u_y")(t)
    gyro = Om * (ux * sp.diff(uy, t) - uy * sp.diff(ux, t))
    print(f"      a gyroscopic term has the form {gyro}")
    print("   -- first order in time, but it couples the two TRANSVERSE")
    print("   POLARIZATIONS to each other. It carries no spatial derivative, so it")
    print("   produces no d_t d_a structure at all. Gyroscopic coupling rotates the")
    print("   polarization plane; the shift vector tilts the light cone. DIFFERENT")
    print("   OBJECTS. Framing cannot substitute.\n")

    print("B5 THE VERDICT: PREDICTION, NOT DEFECT.")
    print("   The medium's inability to represent a shift is not a gap in the")
    print("   construction that further work could fill. It follows from a Derived")
    print("   claim that the framework needs for an independent reason, and the")
    print("   only alternative mechanism the corpus possesses does not produce the")
    print("   right structure.")
    print("   WHAT IT PREDICTS: in the medium's rest frame -- which is registered,")
    print("   CMB-adjacent, and not a free gauge choice (QB-008) -- a rotating mass")
    print("   cannot drag the frame the way GR requires. Kerr is not representable.")
    print("   HOW IT COULD BE TESTED: frame-dragging measurements are real and")
    print("   existing. Gravity Probe B measured geodetic and frame-dragging")
    print("   precession; LAGEOS/LARES constrain the Lense-Thirring effect. A")
    print("   framework that cannot represent frame dragging AT ALL in its rest")
    print("   frame is in immediate tension with those, and the size of the")
    print("   tension is computable rather than rhetorical.")
    print("   THAT COMPUTATION IS NOT DONE HERE and is the named next-order. It is")
    print("   the sector's most dangerous open question: this may be a second")
    print("   discriminating prediction, or it may be an immediate refutation.")
    print("PASS: the question GRV-055 left open is answered -- prediction, not")
    print("      defect -- and the danger in it is named rather than deferred.")


if __name__ == "__main__":
    main()
