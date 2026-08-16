"""COMMISSION EM-RECON-038 -- the caged strain derivation.

Executed under analysis/EMRECON038_strain_derivation_bars_LOCKED.md,
the cage written on EM-RECON-037's face. Route (fixed in advance):
collision-saturation geometry (FND-MATTER-036: <A^2> = (a-D)^2/12,
x = D/a in [0.27, 0.59], conditional on the above-crossover
assumption) applied to the registered bound-mode class
w(u_perp) e^(-u) e^(i phi), at the REGISTERED wall gap: the vacuum
mesh spacing a = 6.0e-17 m (no substitution permitted).

Conversion (fixed at lock): psi = A * S/S_max, S_max = 0.284878;
g_op = (A_sat/xi) * C_shape with C_shape = max|grad(S e^(i phi))| /
S_max including the azimuthal phase strain.

RESULT: C_shape = 4.954 (converged 0.2 percent; the max sits at the
origin where radial and azimuthal strains are each ~1 and add in
quadrature). Per-sector operating strain at the registered gap:
  chemical (xi = 0.443 A):  g_op in [7.9e-7, 1.4e-6]
  nuclear  (L  = 1.4 fm):   g_op in [2.5e-2, 4.5e-2]
against the registered no-binding threshold ~0.6 (EM-RECON-036).

VERDICT: NO-BINDING-CONTRADICTION, both sectors. At the registered
wall gap the collision-saturation candidate yields strains at which
the registered energy landscape cannot bind AT ALL, in sectors where
bound states manifestly exist. The route is KILLED for bound-mode
operation (FND-MATTER-036's alpha-chain scope untouched). Cage
clauses restated: this lands far from the quarantined g ~ 0.75
display and refutes nothing about it; the display was never a claim.
"""
import numpy as np

S_MAX = 0.284878

def c_shape(nup=2400, nz=4800):
    up = np.linspace(1e-4, 6, nup)
    z = np.linspace(-6, 6, nz)
    UP, Z = np.meshgrid(up, z, indexing='ij')
    U = np.sqrt(UP ** 2 + Z ** 2)
    S = (UP / np.sqrt(1 + UP ** 2)) * np.exp(-U)
    g = np.sqrt(np.gradient(S, up[1] - up[0], axis=0) ** 2
                + np.gradient(S, z[1] - z[0], axis=1) ** 2
                + (S / UP) ** 2)
    return g.max() / S_MAX

def main():
    C = c_shape()
    print(f"C_shape = {C:.4f}")
    a = 6.0e-17
    for name, xi in (("chemical", 0.443e-10), ("nuclear", 1.4e-15)):
        lo = (a / xi) * (1 - 0.59) / np.sqrt(12) * C
        hi = (a / xi) * (1 - 0.27) / np.sqrt(12) * C
        print(f"{name}: g_op in [{lo:.3e}, {hi:.3e}]  "
              f"(threshold ~0.6 -> NO BINDING)")

if __name__ == "__main__":
    main()
