"""ELEC-069 -- IS THE WINDOW REACHABLE? The existence condition meets QB-008's
Bell-timing bound on the stiffness ratio.

Bars locked in analysis/ELEC069_soliton_window_bars_LOCKED.md BEFORE computing.
"""
import numpy as np
from scipy.integrate import quad

K_OVER_T0_MIN = 1.9e8      # QB-008, from Bell timing (one-sided: >=)


def integrals():
    f = lambda s: 1 / np.cosh(s)
    fp = lambda s: -np.sinh(s) / np.cosh(s) ** 2
    I1 = quad(lambda s: fp(s) ** 2, -40, 40)[0]
    I2 = quad(lambda s: fp(s) ** 4, -40, 40)[0]
    I3 = quad(lambda s: f(s) ** 2, -40, 40)[0]
    return I1, I2, I3


def main():
    I1, I2, I3 = integrals()
    geom = I1 ** 2 / (3 * I2 * I3)
    print("B1 PROFILE INTEGRALS (sech family):")
    print(f"   I1 = {I1:.4f}, I2 = {I2:.4f}, I3 = {I3:.4f}")
    print(f"   geometric factor I1^2/(3 I2 I3) = {geom:.4f}\n")

    print("B2 THE STEEPNESS BOUND. The window A^2 > 12 B C reduces, at large k and")
    print("   with ELEC-068's omega = c/L, to a pure constraint on Amp/L:")
    print("      (Amp/L)^2 < (T0/k) x I1^2/(3 I2 I3)")
    for kr in (K_OVER_T0_MIN, 1e9, 1e10, 1e12):
        s = np.sqrt(geom / kr)
        print(f"   k/T0 = {kr:8.1e}:  Amp/L < {s:.3e}")
    smax = np.sqrt(geom / K_OVER_T0_MIN)
    print(f"   At the registered minimum stiffness the object may be at most")
    print(f"   {smax:.2e} steep -- and since QB-008's bound is ONE-SIDED, any")
    print(f"   stiffer medium makes this WORSE.\n")

    print("B3 THE TENSION, and it is the session's real finding:")
    print("   ELEC-067 established that the fast-channel coupling strengthens with")
    print("   k and scales as the steepness squared, u' ~ -(1/2)(Amp/L)^2.")
    print("   This window shrinks as 1/sqrt(k) and caps the steepness.")
    print("   Evaluating the induced strain AT the maximum allowed steepness:")
    for kr in (K_OVER_T0_MIN, 1e10, 1e12):
        s = np.sqrt(geom / kr)
        print(f"   k/T0 = {kr:8.1e}: max Amp/L = {s:.2e} -> |u'| <= {0.5*s**2:.2e}")
    u_max = 0.5 * smax ** 2
    print(f"   THE TWO EFFECTS CANCEL AGAINST EACH OTHER EXACTLY IN k: the maximum")
    print(f"   induced strain is |u'| <= (1/2)(T0/k) x geom, falling as 1/k, so the")
    print(f"   stiffer the medium the STRONGER the vertex and the WEAKER the")
    print(f"   configuration it can bind. At the registered bound the induced")
    print(f"   longitudinal strain is at most {u_max:.1e}.\n")

    print("B4 THE VERDICT: THE WINDOW IS REACHABLE BUT SHALLOW.")
    print("   A stable dynamical soliton exists in this system for configurations")
    print("   flatter than Amp/L ~ 6e-5, and the corpus's own Bell-timing bound is")
    print("   what caps it. That is not a contradiction and not a kill: it is a")
    print("   quantitative shape constraint, and it is the first time this line has")
    print("   touched a registered number without breaking.")
    print("   BUT THE HONEST READING IS UNCOMFORTABLE: the binding mechanism is")
    print("   strongest where the object cannot exist, and the object exists where")
    print("   the binding is weakest. The stable solutions are barely-bound,")
    print("   barely-nonlinear objects, which is not obviously what an electron is.")
    assert smax < 1e-3

    print("\nB5 WHAT THIS IS NOT: the sech profile family is ASSUMED and the bound")
    print("   is family-dependent through I1^2/(3 I2 I3) -- a different profile")
    print("   moves it by an O(1) factor, not by orders. The model is 1+1 with a")
    print("   scalar stand-in. omega remains undetermined, so the SIZE is still")
    print("   unfixed even though the SHAPE is now constrained. No solution is")
    print("   constructed and no contact is made with any measured property.")
    print("PASS: the window is reachable, its cap computed from a registered")
    print("      experimental bound, and the awkward direction of the tension named.")


if __name__ == "__main__":
    main()
