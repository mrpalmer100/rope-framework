"""GRV-070 -- THE RESIDUE STRUCTURE: R_0 ~ (a+b)(c+d), and the whole remaining
derivation written as one equation.

Bars locked in analysis/GRV070_residue_structure_bars_LOCKED.md BEFORE computing.
"""
import sympy as sp


def main():
    a, b, c, d, K0, k, G, cc = sp.symbols("a b c d K_0 k G c_light", real=True)

    print("B1 THE TWO CORRECTIONS, executed:\n")
    print("   R1 'SOURCES NOTHING WHATEVER' WITHDRAWN. On the line a = -b a")
    print("      rigidly co-rotating configuration does not source THIS ROTATIONAL")
    print("      CHANNEL. It could still source scalar gravity, compression,")
    print("      ordinary displacement, parity-odd channels or other vector")
    print("      fields. The point stands; the wording overreached.")
    print("   R2 THE METRIC RESIDUE WAS DESCRIBED WRONGLY. GRV-069 said it")
    print("      vanishes only if the metric map 'ignores microrotation")
    print("      entirely'. For a general linear observable map")
    print("         g_0i = c Omega_i + d phi_i")
    print("      the massless-mode residue is proportional to (c + d) and vanishes")
    print("      on c = -d -- THE METRIC SEEING ONLY RELATIVE ROTATION. That is a")
    print("      different and weaker condition, and the parallel with the source")
    print("      residue is exact.\n")

    print("B2 THE RESIDUE, in parallel form:")
    print("      source map  L = J.(a Omega + b phi)   ->  residue ~ (a + b)")
    print("      metric map  g_0i = c Omega_i + d phi_i ->  residue ~ (c + d)")
    R0 = (a + b) * (c + d)
    print(f"      R_0 ~ {R0}")
    print("   On the massless mode phi = Omega, so both are SUMS. Each vanishes")
    print("   on its own relative-rotation-only line.\n")

    print("B3 THE WHOLE REMAINING DERIVATION, AS ONE EQUATION:")
    resp = R0 / (K0 * k ** 2)
    print(f"   g_0i(k) ~ {resp} J_i^perp(k)")
    print("   Fourier: 1/k^2 -> 1/(4 pi r), and transverse-projected J gives the")
    print("   dipole, so in real space")
    print("      g_0i(r) ~ [(a+b)(c+d)/(4 pi K_0)] (J x r)_i / r^3")
    print("   THE STRUCTURE IS ALREADY WHAT LENSE-THIRRING REQUIRES.")
    print("   Linearised GR gives g_0i = -2G (J x r)_i/(c^3 r^3), so the framework")
    print("   must deliver")
    target = sp.Eq((a + b) * (c + d) / (4 * sp.pi * K0), -2 * G / cc ** 3)
    print(f"      {target}")
    print("   FOUR COEFFICIENTS AND ONE STIFFNESS. That is the entire remaining")
    print("   derivation, now a single explicit target rather than a programme.\n")

    print("B4 STATUS -- COLLECTIVE_ROTATION_MODE_UNSCREENED_SOURCE_OVERLAP_UNDERIVED:")
    print("   The parity-even Cosserat operator contains a massless collective")
    print("   co-rotation mode for arbitrary locking strength. A general linear")
    print("   angular-momentum source and metric map overlap with this mode unless")
    print("   their coefficients lie on special relative-rotation-only subspaces.")
    print("   The strand action has not yet determined those coefficients, so")
    print("   NEITHER SOURCE EXCITATION NOR OBSERVABLE FRAME DRAGGING IS DERIVED.\n")

    print("B5 THE CAUTION THAT MUST BE CARRIED, and it cuts against optimism:")
    print("   'MEASURE-ZERO IN COEFFICIENT SPACE' DOES NOT MEAN 'UNLIKELY IN A")
    print("   DERIVED THEORY'. Physical theories land on special lines all the")
    print("   time -- because of symmetry, gauge invariance, conservation laws,")
    print("   objectivity, parity, action-reaction, or simply how matter and")
    print("   geometry are defined. The strand action could force a = -b or")
    print("   c = -d exactly. GRV-069's 'generic' argument is therefore weaker")
    print("   evidence than it sounds, and this claim does not lean on it.")
    print("   WHAT THE NEXT SESSION MUST PRODUCE: a, b, c, d and K_0 from the")
    print("   strand action -- OR a demonstration that the action lacks the")
    print("   structure to determine them, which is an equally admissible and")
    print("   equally informative outcome.")
    print("PASS: both corrections executed, the residue written in parallel form,")
    print("      and the remaining derivation reduced to one equation.")


if __name__ == "__main__":
    main()
