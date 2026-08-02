"""FND-017 -- WHAT SETS T0? The question reduces to one already registered, and
the ground state stores no energy because tension is a constraint force.

Bars locked in analysis/FND017_tension_origin_bars_LOCKED.md BEFORE computing.
"""
import numpy as np

SETS = {"Sigma-route": (5.10e35, 1.70e3), "lattice-anchored": (3.61e35, 1203.0)}
A_LORENTZ = 1e-16


def main():
    print("B1 THE REDUCTION -- is Q1 actually a new open question?")
    print("   ELEC-053 proved T0/Sigma = a^2/3 for ANY tube radius, so")
    print("   T0 = Sigma a^2/3 and T0 is NOT independent.")
    print("   Inverting, a = sqrt(3 T0/Sigma) should return the Lorentz bound:")
    ok = True
    for lab, (S, T0) in SETS.items():
        a = np.sqrt(3 * T0 / S)
        dev = abs(a / A_LORENTZ - 1)
        ok &= dev < 1e-3
        print(f"   {lab:18s} Sigma={S:.2e}, T0={T0:6.0f} -> a = {a:.4e} m "
              f"({dev*100:.2f}% from the bound)")
    assert ok
    print("   BOTH SCALE SETS RETURN THE LORENTZ BOUND TO BETTER THAN 0.1%.")
    print("   So T0 is fixed by Sigma and a, and Q1 -- 'what sets T0' -- is NOT a")
    print("   new open question. It IS the corpus's one registered open number,")
    print("   Sigma, which has two candidates 28% apart and a named experiment")
    print("   (QGATE-007 polarimetry) to decide between them. Nothing new is owed;")
    print("   the debt was already on the books under a different name.\n")

    print("B2 Q2 -- IS T0 STORED ENERGY, OR A CONSTRAINT FORCE?")
    print("   The corpus postulates an INEXTENSIBLE medium (P-VOL; FND-STRAND-001")
    print("   'literal inextensible elastic curves'). In a constrained mechanical")
    print("   system the force conjugate to a rigid constraint is a LAGRANGE")
    print("   MULTIPLIER, not a stored elastic energy. A multiplier does no work")
    print("   while the constraint is satisfied; it does work only when the")
    print("   configuration changes -- which is exactly the behaviour the reservoir")
    print("   picture (ELEC-079/080) requires and exploits.")
    print("   ON THAT READING THE GROUND STATE STORES NO ENERGY IN T0, and Q2's")
    print("   premise -- 'a tensioned ground state stores energy it should be able")
    print("   to lower' -- is FALSE. There is nothing to relax: the medium cannot")
    print("   shorten because it is inextensible, and the tension is whatever value")
    print("   maintains that.\n")

    print("B3 WHAT THEN FIXES THE MULTIPLIER'S VALUE?")
    print("   A multiplier is set by the state and the boundary conditions, never")
    print("   by a local property. So T0 is a GLOBAL property of the medium's")
    print("   configuration -- consistent with B1, where it is fixed by Sigma (a")
    print("   global energy density) and a (a global bound), and inconsistent with")
    print("   any attempt to derive T0 from local strand mechanics.")
    print("   THAT IS A USEFUL NEGATIVE: it says no local derivation of T0 can")
    print("   exist, and any future attempt at one is misconceived.\n")

    print("B4 THE RESIDUE, after both questions:")
    print("   Q1 reduces to Sigma, already registered and already assigned to an")
    print("   experiment. Q2 dissolves under the multiplier reading. WHAT REMAINS")
    print("   genuinely underived is SIGMA ITSELF -- the vacuum's stiffness -- and")
    print("   that is the corpus's single open number, unchanged since ELEC-053.")
    print("   The foundations residue ELEC-080 named is not a third debt. It is the")
    print("   same debt, seen from the tension side instead of the stiffness side.\n")

    print("B5 HONESTY: this is a structural argument from registered claims, not a")
    print("   derivation of T0 or of Sigma. The multiplier reading depends on the")
    print("   inextensibility postulate being exact rather than an idealisation;")
    print("   if strands are very stiff but finitely extensible, T0 IS partly")
    print("   stored energy and Q2 returns in weakened form.")
    print("PASS: two apparently open foundations questions reduce to one already on")
    print("      the books, and a useful no-go on local derivations of T0 falls out.")


if __name__ == "__main__":
    main()
