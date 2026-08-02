"""ELEC-058 (self-caught unit error before registration: c tau0 was first
coded as c times a length; tau0 = 1.95 w/c so c tau0 = 1.95 w. The locked
assertion best > 1 caught it -- the bar failed loudly rather than passing a
wrong number) -- DOES THE BUNDLE ESCAPE SURVIVE AT SMALL STRAND SCALE?
THE RECRUITMENT SHORTFALL AS A FUNCTION OF THE ONE FREE LENGTH.

Bars locked in analysis/ELEC058_bundle_scaling_bars_LOCKED.md BEFORE this ran.
"""
import numpy as np

HBAR = 1.054571817e-34
C = 2.99792458e8
FM = 1e-15
T_TUBE = 1.878e5
R_TUBE = 0.407 * FM
A_LORENTZ = 1e-16
A_ELECTRON = 4.726e-21
R_HE4 = 1.2 * 4 ** (1 / 3) * FM
TAU0_IN_W = 1.95          # ELEC-047: traversal time SATURATES at ~1.9-2.0 w/c


def w(a):
    return a / np.sqrt(3)


def T0(a):
    return T_TUBE / (3 * np.pi * (R_TUBE / a) ** 2)


def main():
    print("B1 THE CAUSAL BUDGET'S SCALING (ELEC-047's recruitment):")
    print("   tau0 = 1.95 w/c is expressed IN UNITS OF w, so c tau0 / w = 1.95")
    print("   identically, and n_free = pi (c tau0/w)^2 = "
          f"{np.pi*TAU0_IN_W**2:.1f} AT EVERY a.")
    for a in (A_LORENTZ, 1e-18, A_ELECTRON):
        print(f"     a = {a:.2e}:  c tau0 = {TAU0_IN_W*w(a)/FM:.3e} fm, "
              f"n_free = {np.pi*TAU0_IN_W**2:.1f}")
    print("   THE TRAP AVOIDED: the naive '(1e-16/a)^2 raises the bound by 4.5e8'")
    print("   holds tau FIXED. It is not fixed -- ELEC-043's timescales are OBJECT")
    print("   timescales and the object rescales with a under one medium, while")
    print("   ELEC-047's tau0 is written in w directly. THE BUDGET IS INVARIANT.\n")

    print("B2 THE DEMAND'S SCALING (the target is NUCLEAR, set by QCD, fixed in metres):")
    T_need = 2 * np.pi * HBAR * C / R_HE4 ** 2
    print(f"   T_eff needed for one patch in He-4 = {T_need:.3e} J/m (a-independent)")
    print(f"   {'a (m)':>10} {'N=T_need/T0':>13} {'R_c=w sqrt(N)':>15} {'c tau0':>12}")
    for a in (A_LORENTZ, 1e-17, 1e-18, 1e-19, 1e-20, A_ELECTRON):
        N = T_need / T0(a)
        Rc = w(a) * np.sqrt(N)
        print(f"   {a:10.1e} {N:13.3e} {Rc/FM:14.4f}f {TAU0_IN_W*w(a)/FM:11.3e}f")
    N_b = T_need / T0(A_LORENTZ)
    Rc_b = w(A_LORENTZ) * np.sqrt(N_b)
    print(f"   R_c = w sqrt(N) with N ~ a^-2 gives R_c ~ a * (1/a) = CONSTANT = "
          f"{Rc_b/FM:.4f} fm.")
    print("   THE DEMAND IS A-INVARIANT (it is fixed by measured T_tube and the")
    print("   nuclear target), WHILE THE BUDGET c tau0 ~ a SHRINKS. Decisive asymmetry.\n")

    print("B3 THE VERDICT -- shortfall ratio R_c / (c tau0) across the allowed range:")
    worst = None
    for a in (A_LORENTZ, 1e-17, 1e-18, 1e-19, 1e-20, A_ELECTRON):
        N = T_need / T0(a)
        ratio = (w(a) * np.sqrt(N)) / (TAU0_IN_W * w(a))
        print(f"   a = {a:.2e}:  R_c/(c tau0) = {ratio:.3e}  "
              f"({'RECRUITABLE' if ratio <= 1 else 'shortfall'})")
        worst = ratio
    best = (w(A_LORENTZ) * np.sqrt(N_b)) / (TAU0_IN_W * w(A_LORENTZ))
    assert best > 1
    print(f"   THE RATIO GROWS AS 1/a: best case at the Lorentz CEILING is "
          f"{best:.2e},")
    print(f"   and at the electron-viable scale it is {worst:.2e} -- "
          f"{worst/best:.1e}x WORSE.")
    print("   THE ESCAPE DIES EVERYWHERE, AND DIES WORSE AT SMALL a. Bundling")
    print("   cannot trade strand count for scale: the geometry was never the")
    print("   obstruction, the causal recruitment always was.\n")

    print("B4 THE WHOLE-TUBE VARIANT (the proposal's strongest form):")
    L_tube = np.sqrt(2 * np.pi * HBAR * C / T_TUBE)
    n_tube = 3 * np.pi * (R_TUBE / A_ELECTRON) ** 2
    Rc_tube = w(A_ELECTRON) * np.sqrt(n_tube)
    print(f"   T_eff = T_tube = {T_TUBE:.3e} J/m (MEASURED, a-independent)")
    print(f"   -> L = {L_tube/FM:.3f} fm, which DOES satisfy the nuclear gate at any a.")
    print(f"   But recruiting the tube's {n_tube:.2e} strands needs coherence radius")
    print(f"   R_c = {Rc_tube/FM:.3f} fm against a causal reach of "
          f"{TAU0_IN_W*w(A_ELECTRON)/FM:.2e} fm:")
    print(f"   a shortfall of {Rc_tube/(TAU0_IN_W*w(A_ELECTRON)):.2e}.")
    print("   GEOMETRY FREE, RECRUITMENT NOT -- this is ELEC-047's finding restated")
    print("   at a new scale, not a new result, and is reported as such.\n")

    print("B5 CONSEQUENCE: ELEC-057's no-go is HARDENED, not narrowed. The bundle")
    print("   escape fails scale-invariantly in the budget and adversely in the")
    print("   demand, so no choice of the free length and no amount of bundling")
    print("   places both sectors alive at once. The fork stands: abandon the")
    print("   one-medium declaration, or retire the hbar sector.")
    print("PASS: the escape was tested at the scale that motivated it and did not")
    print("      survive; the reason is recruitment, exactly where it was before.")


if __name__ == "__main__":
    main()
