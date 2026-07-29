"""QGATE-003 (Modeled): THE CROSS-SECTOR TRANSFER TEST (the campaign
commission's QGATE-004; its 003, amplitude scaling, was executed
inside QGATE-001). The surviving normalization -- the reconnection
separatrix W = 1.80 T D^2/c -- applied UNCHANGED to the residues the
ledger identified, no per-sector retuning permitted.

THE HONEST FORM OF THE TEST: back-compute the demanded action
normalization from each sector's quantum residue as the framework
represents it, and ask whether the sectors demand the SAME number. A
candidate failing every sector by the same factor survives the
universality gate with one renormalization; sector-scattered demands
kill it outright.

THE VERDICT -- UNIFORM: matter (the 13.6 eV / Bohr chain) demands
S/W = 112.4; chemistry demands the same BY INHERITANCE (flagged: its
agreement tests chain consistency, not independence -- though the H2
vibration's 16 percent transfer with no retune is real internal
evidence); nuclear -- a GENUINELY INDEPENDENT inversion, Fermi motion
through the framework's own nucleon mass m = TD x 27.75 -- demands
S/W = 107.4. Common factor 111, spread 4.6 percent. Two different
physical residues, two different inversion routes, one number.

THE COLLECTIVE-RECONNECTION PREDICTION (registered as prediction, not
result): one renormalization serves all -- n_t ~ 111 strands
reconnecting collectively, and with tube coverage f_c = 0.309
(FND-MATTER-038) that fixes D/w = sqrt(n_t/f_c) ~ 19. A tube of ~111
constituents at width ratio ~19 makes W_collective = hbar across
matter, chemistry, AND nuclear simultaneously with zero per-sector
retuning. Unverified; the verification path is a tube-census
computation (does the corpus's own bundle machinery, FND-MATTER-004
applied at the tube level, independently deliver ~111?).

GRAVITY: recorded PENDING -- the induced coefficient is itself the
open quantity (GRV-021); no number fabricated. Numerological
adjacencies (111 vs 137) deliberately NOT invoked.
"""
import numpy as np


def test():
    TD, D, kappa, hc = 33.8, 0.8/27.75, 1.801, 197.327
    W = kappa*TD*D
    assert 0.007 < W/hc < 0.011, "W_rec ~ 0.009 hbar (QGATE-001 reproduced)"
    S1 = hc                                   # matter: Bohr chain
    m_N = TD*27.75; S3 = np.sqrt(2*m_N*35.0)/1.36   # nuclear: independent Fermi inversion
    r = np.array([S1/W, S1/W, S3/W])          # chemistry inherits S1 (flagged in docstring)
    mean = r.mean(); spread = (r.max() - r.min())/mean
    assert spread < 0.10, "UNIFORM demand: sectors agree within 10% -- no scattered demands"
    assert 95 < mean < 130, "common factor ~111"
    assert abs(S3/hc - 1.0) < 0.10, "nuclear inversion independently lands on ~hbar (0.955)"
    n_t = mean; fc = 0.309; Dw = np.sqrt(n_t/fc)
    assert 16 < Dw < 22, "the structural prediction: D/w ~ 19 at f_c = 0.309"
    print(f"demanded S/W: matter {S1/W:.1f}, chemistry {S1/W:.1f} (inherited), nuclear {S3/W:.1f}")
    print(f"common factor {mean:.0f}, spread {spread*100:.1f}% -- UNIFORM; prediction: n_t ~ {n_t:.0f}, D/w ~ {Dw:.1f}")
    print("PASS: the candidate fails every sector by the SAME factor -- universality survives;")
    print("      one collective renormalization would serve three sectors with zero retuning.")


if __name__ == "__main__":
    test()
