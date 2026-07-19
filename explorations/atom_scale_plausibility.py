"""Reproducible numbers for the hydrogen-atom plausibility sketch.

THIS IS A PLAUSIBILITY EXPLORATION, NOT A DERIVATION OR A VALIDATED CLAIM.
It shows that ONE explicit assumption set lands in the right ballpark for the
Bohr radius and is consistent with sensible mass ratios. The rope count N and
the microstructure scale a are CHOSEN (tuned), not derived. See
explorations/atom_scale_plausibility.md and claim FND-MATTER-003 for why a real
derivation is currently blocked.
"""
import numpy as np

# --- measured targets ---
a0 = 5.29e-11        # Bohr radius (m)
m_p_over_m_e = 1836  # proton/electron mass ratio
c = 2.998e8

# --- EXPLICIT ASSUMPTIONS (chosen for plausibility, NOT derived) ---
A1_a = 1e-16         # rope microstructure scale, at the Lorentz-violation bound
# Packing law from the star geometry (FND-MATTER-002): R = a*sqrt(N/4pi).
# A2: choose N so that R = a0 (this is the tuning; N is not independently fixed).
A2_N = 4 * np.pi * (a0 / A1_a) ** 2


def report():
    print("HYDROGEN ATOM PLAUSIBILITY SKETCH -- numbers")
    print("=" * 60)
    print("ASSUMPTIONS (explicit, chosen, NOT derived):")
    print(f"  A1: rope microstructure scale a = {A1_a:.0e} m (Lorentz bound)")
    print(f"  A2: rope count chosen so R = a0  ->  N = 4pi(a0/a)^2 = {A2_N:.2e}")
    print()
    R = A1_a * np.sqrt(A2_N / (4 * np.pi))
    print("RADIUS CHECK (by construction, but inputs are sane):")
    print(f"  R = a*sqrt(N/4pi) = {R:.2e} m   vs Bohr a0 = {a0:.2e} m")
    print()
    print("MASS-RATIO PLAUSIBILITY (ratios need no absolute scale):")
    for law, need in [("mass ~ N", m_p_over_m_e),
                      ("mass ~ sqrt(N)", m_p_over_m_e ** 2),
                      ("mass ~ N^2", np.sqrt(m_p_over_m_e))]:
        print(f"  if {law:14s}: need N_p/N_e ~ {need:.3g}  (sensible-ish)")
    print()
    print("HONEST LIMITS:")
    print("  * N and a are TUNED, not derived (one target, two free inputs).")
    print("  * Absolute mass is NOT checkable without fixing T, kappa, a.")
    print("  * Derivation is BLOCKED (FND-MATTER-003): charge fixes winding (=1),")
    print("    not the packing count N (~1e12); no independent handle on N.")


if __name__ == "__main__":
    report()
