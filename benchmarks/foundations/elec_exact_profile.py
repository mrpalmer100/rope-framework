"""ELEC-074 -- THE EXACT PROFILE: the cusp was an artifact and the object has a
HARD CORE, but the scaling relations survive.

Bars locked in analysis/ELEC074_exact_profile_bars_LOCKED.md BEFORE computing.
"""
import numpy as np
from scipy.integrate import quad

F_exact = lambda p: p / np.sqrt(1 + p ** 2)
F_trunc = lambda p: p - p ** 3 / 2 + 3 * p ** 5 / 8
p_of_x = lambda x: (1 / x ** 2) / np.sqrt(1 - 1 / x ** 4)   # x = r/sqrt(C), x > 1


def main():
    print("B1 BOUNDEDNESS -- the difference the truncation hid:")
    for p in (1, 10, 100, 1000):
        print(f"   p={p:5d}:  F_exact={F_exact(p):.6f}   F_trunc={F_trunc(p):.3e}")
    print("   F_exact = p/sqrt(1+p^2) is BOUNDED with sup F = 1; the sixth-order")
    print("   F = p - p^3/2 + 3p^5/8 is UNBOUNDED and diverges as p^5.")
    print("   The first integral r^2 F(p) = C therefore has a solution for ALL r > 0")
    print("   in the truncation but ONLY FOR r^2 >= C exactly.")
    print("   THE FIELD EXISTS ONLY OUTSIDE r0 = sqrt(C): a HARD CORE.\n")

    print("B2 THE PROFILE, exactly: with x = r/sqrt(C), p(x) = x^-2 / sqrt(1 - x^-4)")
    print("      x           p(x)")
    for x in (1.0001, 1.01, 1.1, 2.0, 10.0):
        print(f"      {x:9.4f}  {p_of_x(x):12.4f}")
    print("   p diverges as (x-1)^(-1/2) at the CORE BOUNDARY, not at the origin.")
    print("   ELEC-073's CUSP AT THE ORIGIN (p ~ x^(-2/5)) IS AN ARTIFACT of the")
    print("   sixth-order truncation, exactly as that claim suspected. The exact")
    print("   object is not cusped -- it is hollow, with a boundary at finite")
    print("   radius inside which the description does not reach.\n")

    I_psi = quad(p_of_x, 1 + 1e-12, 400, limit=800)[0]
    dens = lambda x: (np.sqrt(1 + p_of_x(x) ** 2) - 1) * x ** 2
    I_E = quad(dens, 1 + 1e-12, 400, limit=800)[0]
    print("B3 CONVERGENCE with the singularity moved to finite radius:")
    print(f"   excursion integral = {I_psi:.5f}   (p ~ (x-1)^(-1/2) is integrable)")
    print(f"   energy integral    = {I_E:.5f}")
    assert np.isfinite(I_psi) and np.isfinite(I_E)
    print("   BOTH FINITE. The hard core does not cost infinite energy.\n")

    print("B4 THE SCALING RELATIONS:")
    E_coef = 4 * np.pi * I_E / I_psi ** 3
    print(f"   Delta = sqrt(C) x {I_psi:.4f},  E = 4 pi T0 C^(3/2) x {I_E:.4f}")
    print(f"   => r0 = Delta/{I_psi:.4f} = {1/I_psi:.4f} Delta")
    print(f"   => E  = {E_coef:.4f} T0 Delta^3")
    print("   SIZE STILL LINEAR IN THE EXCURSION, ENERGY STILL CUBIC. ELEC-073's")
    print("   SCALING RELATIONS SURVIVE THE CORRECTION; only the coefficients move")
    print(f"   (E: 0.4328 -> {E_coef:.4f} T0 Delta^3, a factor {E_coef/0.4328:.2f}).")
    print("   THE TRUNCATION WAS WRONG ABOUT SHAPE AND RIGHT ABOUT SCALING, which")
    print("   is worth knowing: the exponents came from dimensional structure that")
    print("   the truncation preserved, the profile from dynamics it did not.\n")

    print("B5 SCOPE, unchanged from ELEC-073 and not improved by exactness:")
    print("   this is an exact solution of a SCALAR TOY in the lab parametrization.")
    print("   No charge, no spin, no topology imposed, no time dependence, no")
    print("   contact with the measured electron. What the hard core MEANS -- and")
    print("   whether a region the continuum description cannot enter is physical")
    print("   or signals the breakdown of the continuum itself at the strand scale")
    print("   -- is not addressed here and is the obvious next question.")
    print("PASS: the cusp is refuted as an artifact, the exact profile is hollow")
    print("      with a hard core, and the scaling relations survive intact.")


if __name__ == "__main__":
    main()
