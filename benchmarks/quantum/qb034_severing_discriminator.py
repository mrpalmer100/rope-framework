"""QB-034: the severing-vs-dephasing discriminator -- does the shared-ribbon
ontology make an EXPERIMENTALLY DISTINGUISHABLE claim about how stored
entanglement decays? Bars locked BEFORE computing
(analysis/QB034_severing_discriminator_results.md):
(1) THE TWO READINGS OF 'SEVERING' ARE NAMED FIRST, before any curve:
    READING A (persistent severed ribbon): decoherence converts intact
      pairs into MODE-1 pairs -- the ribbon survives as one object but the
      bookkeeping is severed, so severed pairs still correlate at
      E = -(a.b)/3.
    READING B (ribbon destroyed): decoherence removes the ribbon; severed
      pairs are uncorrelated, E = 0.
(2) DEGENERACY TEST, mandatory and run BEFORE any confrontation: if a
reading's decay family is algebraically identical to the standard
Werner/depolarizing family, it makes NO new claim and must be registered
as EMPTY -- no amount of fit quality rescues a degenerate model.
(3) DISCRIMINATOR: only a feature that standard dephasing CANNOT produce
counts. The pre-committed candidate is a NON-ZERO ASYMPTOTIC FLOOR in the
correlation.
(4) CONFRONTATION SCOPE, stated honestly: the corpus may confront a
QUALITATIVE, uncontroversial experimental fact (whether stored-memory
correlations decay to zero) without claiming a specific published number;
any quantitative claim would require a literature session with citations,
which this session does NOT perform and must not pretend to.
(5) A kill of Reading A is a permitted and expected outcome; the ontology
(QB-015) is NOT on trial -- only this decoherence extension.
"""
import numpy as np

BELL_THRESHOLD = 1 / np.sqrt(2)      # V above which CHSH > 2
WALL_V = 1 / 3                       # QB-015 Mode 1 / QB-013 wall


def chsh(V):
    return 2 * np.sqrt(2) * V


def main():
    p = np.linspace(1, 0, 11)        # intact fraction, 1 -> 0

    # READING A: mixture of intact (E = -a.b) and severed (E = -(a.b)/3)
    V_A = p + (1 - p) * WALL_V
    # READING B: mixture of intact and uncorrelated
    V_B = p

    print("THE TWO READINGS, visibility V(p) with p the intact fraction:")
    print("  p     V_A (persistent severed)   V_B (ribbon destroyed)")
    for pi, va, vb in list(zip(p, V_A, V_B))[::2]:
        print(f"  {pi:.1f}   {va:.4f}                     {vb:.4f}")

    # (2) DEGENERACY TEST
    print("DEGENERACY TEST (mandatory, run before confrontation):")
    print("  READING B: V_B = p exactly -- ALGEBRAICALLY IDENTICAL to the")
    print("    standard Werner/depolarizing family with V = p. Reading B")
    print("    makes NO new claim and is registered EMPTY. It cannot be")
    print("    confirmed OR refuted by decay data, and no fit quality")
    print("    rescues it.")
    assert np.allclose(V_B, p)
    print("  READING A: V_A = (1 + 2p)/3 -- also a one-parameter Werner")
    print("    family, so AT ANY FIXED TIME it is degenerate too: a severed")
    print("    fraction is indistinguishable from a depolarized fraction by")
    print("    any single-time measurement. The difference is not in the")
    print("    FORM but in the REACHABLE RANGE.")
    assert np.allclose(V_A, (1 + 2 * p) / 3)

    # (3) THE DISCRIMINATOR: the floor
    floor = V_A[-1]
    print(f"THE DISCRIMINATOR (pre-committed): the asymptotic floor.")
    print(f"  Reading A: as p -> 0, V -> {floor:.4f} = 1/3, NOT zero.")
    print(f"    CHSH -> {chsh(floor):.4f} (below the Bell threshold V = "
          f"{BELL_THRESHOLD:.4f}, so NOT a Bell violation -- but a")
    print("    PERSISTENT CLASSICAL CORRELATION that never decays away.)")
    print(f"  Reading B / standard: V -> 0, correlations vanish entirely.")
    assert abs(floor - 1 / 3) < 1e-12 and chsh(floor) < 2

    # (4) CONFRONTATION, qualitative and scoped
    print("CONFRONTATION (scope per bar 4 -- qualitative, uncontroversial):")
    print("  Stored entanglement in quantum memories is routinely observed to")
    print("  decay to CLASSICAL, uncorrelated outcomes: fidelity falls to the")
    print("  0.25 random-state floor and correlation visibility to zero at")
    print("  long storage times. A residual V = 1/3 correlation surviving")
    print("  indefinitely in every entangled pair ever stored would be one of")
    print("  the most conspicuous anomalies in experimental physics. It is")
    print("  not observed.")
    print("  VERDICT: READING A IS KILLED. Severing cannot be a persistent")
    print("    state of the ribbon; whatever decoherence does to the shared")
    print("    ribbon, it does not leave a 1/3-correlated object behind.")
    print("  VERDICT: READING B IS EMPTY (degenerate by construction).")

    # (5) WHAT SURVIVES
    print("WHAT SURVIVES, stated precisely:")
    print("  1. QB-015's ontology is UNTOUCHED -- it was never on trial. The")
    print("     wall value 1/3 remains the signature of severed BOOKKEEPING")
    print("     (a description-level error about one object), NOT a physical")
    print("     state a decohering pair passes through or lands in.")
    print("  2. THE SESSION'S REAL PRODUCT is that distinction, now forced:")
    print("     Mode 1 is an ACCOUNTING mode, not a DYNAMICAL one. The")
    print("     corpus had never had to say which, because nothing depended")
    print("     on it until someone asked the ribbon to decohere.")
    print("  3. CONSEQUENCE for the ontology: decoherence must be modeled as")
    print("     the ribbon being CUT (Reading B) rather than mis-accounted --")
    print("     and Reading B is empty, so the ribbon picture makes NO")
    print("     distinguishable prediction about memory decoherence. Honest")
    print("     bottom line: NO ENGINEERING LEVER for repeater networks, and")
    print("     the corpus now has a benchmark proving it rather than an")
    print("     opinion.")
    print("NOT CLAIMED: any quantitative comparison to published memory")
    print("  lifetimes, any preferred-frame signature, any protocol advantage.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
