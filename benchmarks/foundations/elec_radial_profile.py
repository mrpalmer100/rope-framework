"""ELEC-073 -- THE 3D RADIAL PROFILE SOLVED: a cusped, scale-free family whose
size and energy are fixed only by the field excursion.

Bars locked in analysis/ELEC073_profile_bars_LOCKED.md BEFORE computing.
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

F = lambda p: p - p ** 3 / 2 + 3 * p ** 5 / 8
Fp = lambda p: 1 - 1.5 * p ** 2 + 15 * p ** 4 / 8
G = lambda y: brentq(lambda p: F(p) - y, 0, 1e6)
dens = lambda p: p ** 2 / 2 - p ** 4 / 8 + p ** 6 / 16


def main():
    print("B1 MONOTONICITY of F(p) = p - p^3/2 + 3p^5/8:")
    m = float(np.min(Fp(np.linspace(0, 20, 200001))))
    print(f"   min F'(p) over p in [0,20] = {m:.4f}")
    assert m > 0
    print("   F' > 0 EVERYWHERE (its discriminant is negative), so F is strictly")
    print("   increasing and the first integral r^2 F(p) = C defines p(r)")
    print("   uniquely. The analysis may proceed.\n")

    print("B2 THE PROFILE -- the question ELEC-072 asked:")
    print("   with x = r/sqrt(C), the first integral reads F(p) = 1/x^2, so p(x)")
    print("   is UNIVERSAL and C only sets the scale.")
    print("      x          p(x)      p*x^(2/5)")
    for x in (1e-4, 1e-3, 1e-2, 1e-1, 1.0, 10.0):
        p = G(1 / x ** 2)
        print(f"      {x:8.0e}  {p:10.4f}   {p*x**0.4:8.4f}")
    print("   p ~ x^(-2/5) at small x: THE SLOPE DIVERGES AT THE ORIGIN.")
    print("   A sech profile has p -> 0 at its centre. THE TRUE PROFILE IS CUSPED,")
    print("   and the sech family assumed in ELEC-069 is NOT close to it.")
    print("   CONSEQUENCE, stated rather than buried: ELEC-069's steepness bound")
    print("   Amp/L < 5.84e-5 was computed with sech integrals I1, I2, I3. Those")
    print("   integrals are wrong for this profile, so that NUMBER is wrong -- the")
    print("   bound's existence and its 1/sqrt(k) scaling survive, its coefficient")
    print("   does not.\n")

    print("B3 FINITENESS:")
    I_psi = quad(lambda x: G(1 / x ** 2), 1e-8, 300, limit=600)[0]
    I_E = quad(lambda x: dens(G(1 / x ** 2)) * x ** 2, 1e-8, 300, limit=600)[0]
    print(f"   excursion integral  int_0^inf G(1/x^2) dx      = {I_psi:.5f}")
    print(f"   energy integral     int_0^inf dens(p) x^2 dx   = {I_E:.5f}")
    print("   BOTH CONVERGE. The cusp is integrable: p ~ x^(-2/5) gives a finite")
    print("   excursion, and the energy density's x^2 measure tames it further.")
    print("   THE SOLUTION HAS FINITE ENERGY AND FINITE FIELD EXCURSION.\n")

    print("B4 WHAT FIXES THE SCALE:")
    print("   The equation contains NO LENGTH, so solutions form a one-parameter")
    print("   family in C, and rescaling r -> sqrt(C) x gives")
    print(f"      excursion  Delta = sqrt(C) x {I_psi:.4f}")
    print(f"      energy     E     = 4 pi T0 C^(3/2) x {I_E:.4f}")
    print("   Eliminating C:")
    print(f"      E = 4 pi T0 ({I_E:.4f}/{I_psi:.4f}^3) Delta^3 "
          f"= {4*np.pi*I_E/I_psi**3:.4f} T0 Delta^3")
    print(f"      size r ~ sqrt(C) = Delta/{I_psi:.4f}")
    print("   SO SIZE IS LINEAR IN THE FIELD EXCURSION AND ENERGY IS CUBIC IN IT.")
    print("   NOTHING IN THIS MODEL FIXES Delta. The corpus's own candidate is")
    print("   EM-001: charge is the topological linking number, integer-quantised.")
    print("   IF the excursion is set by winding, Delta ~ N, then")
    print("      size ~ N   and   mass ~ N^3,")
    print("   which is a structural prediction the framework does not currently")
    print("   make and which is checkable in principle against any doubly-charged")
    print("   elementary object. NO SUCH OBJECT IS KNOWN, so this is untested and")
    print("   is registered as structure, not as a prediction.\n")

    print("B5 WHAT THIS IS NOT: a radial scalar model with the transverse field as")
    print("   a stand-in. No topology is imposed -- the winding connection in B4 is")
    print("   a suggestion, not a computation. No time dependence, no charge, no")
    print("   spin, no contact with the measured electron. The profile solved here")
    print("   is the profile of THIS toy, and its cusp may well be an artifact of")
    print("   truncating the strain expansion at sixth order.")
    print("PASS: the Euler-Lagrange equation is solved exactly, the sech assumption")
    print("      is refuted, and the scale question is reduced to one number.")


if __name__ == "__main__":
    main()
