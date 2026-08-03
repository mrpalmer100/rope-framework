"""GRV-069 -- COLLECTIVE_ROTATION_MODE_UNSCREENED: GRV-068's verdict corrected,
and the pole-residue test attempted.

Bars locked in analysis/GRV069_residue_bars_LOCKED.md BEFORE computing.
"""
import sympy as sp


def main():
    a, b = sp.symbols("a b", real=True)

    print("B1 THE CORRECTIONS, executed:\n")
    print("   C1 'STEP 4 PASSES' IS WITHDRAWN. A vanishing determinant at k = 0")
    print("      does not prove a localized angular-momentum source produces a")
    print("      long-range field. The decisive object is the POLE RESIDUE")
    print("         (O_g^dagger v0)(v0^dagger S_J).")
    print("      A zero mode can exist and remain invisible if the source is")
    print("      orthogonal to it, if the metric observable projects only onto")
    print("      the massive mode, if derivative couplings cancel the 1/k^2 pole,")
    print("      or if the zero mode is a rigid global symmetry rather than a")
    print("      locally excitable field. GRV-068 checked none of these.")
    print("   C2 THE (2,1) EIGENVECTOR IS COORDINATE-DEPENDENT -- it moves with")
    print("      normalisation, with what u denotes, with kinetic coefficients and")
    print("      with Fourier conventions. THE INVARIANT STATEMENT is that the")
    print("      gapless mode has VANISHING RELATIVE ROTATION:")
    print("         eta = phi - (1/2) curl u = 0,  i.e.  Omega_macro = phi.")
    print("      That is what should be quoted, and it is what GRV-068 should have")
    print("      written.")
    print("   C3 'ANGULAR MOMENTUM IS TOTAL ROTATION THEREFORE IT EXCITES THE")
    print("      MASSLESS MODE' IS AN INFERENCE, NOT A DERIVATION. A source")
    print("      carrying J could couple to macrorotation, microrotation, their")
    print("      difference, a curl, or a parity-odd combination.")
    print("   RESTATED NAME: COLLECTIVE_ROTATION_MODE_UNSCREENED.\n")

    print("B2 THE SOURCE RESIDUE, attempted:")
    print("   Most general linear rotational source:")
    print("      L_source = J . ( a Omega_macro + b phi )")
    print("   On the gapless mode Omega_macro = phi = X, so")
    print("      v0^dagger S_J  ~  J . (a + b) X")
    print(f"   VANISHES IFF a + b = 0, i.e. L ~ J.(Omega - phi) = J.eta -- the")
    print("   source coupling PURELY to the relative rotation.")
    print("   THE PHYSICAL READING OF THAT CASE: a rigidly rotating body has")
    print("   eta = 0 identically, so on the a = -b line a rigid rotation sources")
    print("   NOTHING AT ALL -- not a weak field, none. That is a strong and")
    print("   peculiar property for a matter coupling to have.")
    print("   STATUS: the residue is nonzero EXCEPT on a single tuned line, and")
    print("   that line has an odd physical reading. NOT DERIVED.\n")

    print("B3 THE METRIC RESIDUE, attempted:")
    print("   GRV-029's bijection maps the wave operator's coefficient functions")
    print("   to the metric, and GRV-060 identified the shift as entering through")
    print("   the mixed d_t d_a term whose coefficient is the TWIST DENSITY -- a")
    print("   gradient of phi. So O_g projects onto the phi component, and the")
    print("   gapless mode has phi = Omega_macro, nonzero on it.")
    print("   O_g^dagger v0 = 0 would require the metric map to be blind to phi")
    print("   entirely, contradicting GRV-060's identified coupling.")
    print("   STATUS: nonzero unless the corpus's own identified coupling is")
    print("   wrong. NOT DERIVED -- the map's coefficients are not computed.\n")

    print("B4 STATUS OF EACH RESIDUE, stated without inflation:")
    rows = [("massless eigenvalue lambda_0 ~ c k^2", "ESTABLISHED",
             "GRV-068's diagonalisation, for any kappa"),
            ("source residue v0^dagger S_J", "GENERIC, NOT DERIVED",
             "nonzero except on the tuned line a + b = 0"),
            ("metric residue O_g^dagger v0", "GENERIC, NOT DERIVED",
             "nonzero unless the metric map ignores phi")]
    for n, s, w in rows:
        print(f"   {n:38s} {s:22s} {w}")
    print("   'GENERICALLY NONZERO' IS NOT 'NONZERO'. Two of the three factors in")
    print("   the residue are arguments about what would be strange, not")
    print("   computations. The route is REOPENED, not established.\n")

    print("B5 WHAT MUST BE DERIVED BEFORE THE AMPLITUDE QUESTION IS WELL POSED:")
    print("   (1) the source coefficients a and b, from the strand action rather")
    print("       than assumed -- how matter's angular momentum couples to the")
    print("       medium's macrorotation and microrotation separately;")
    print("   (2) the metric map O_g, i.e. the coefficient with which the twist")
    print("       density enters g_0i;")
    print("   (3) only then GRV-062's G-free ratio, and only then 37.2 mas/yr.")
    print("   AND THE PARITY-ODD SECTOR remains outstanding: a parity-odd term")
    print("   need not gap the collective rotational mode if overall rotational")
    print("   symmetry survives, but it can split helicities, rotate the source")
    print("   projection, alter sign and coefficient, and mix the sectors at")
    print("   finite k. Parity-even analysis can establish that a massless")
    print("   channel EXISTS; it cannot fix the terrestrial coefficient.")
    print("PASS: the verdict is corrected, the invariant characterisation")
    print("      replaces the coordinate-dependent one, and both residues are")
    print("      reported as generic rather than derived.")


if __name__ == "__main__":
    main()
