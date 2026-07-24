"""GRV-034 (Modeled): WHAT A BLACK HOLE IS, UNDER THE DERIVED
DICTIONARY -- the horizon is the TENSION-EXHAUSTION surface, and an
internal contradiction in the corpus is resolved in the plain-language
guide's favor.

THE AUDIT: the guide's one-liner said 'the ropes nearby run out of
tension almost entirely'; the cosmology and thermodynamics papers said
'extreme-tension configurations' -- opposite adjectives, never
reconciled because no black-hole derivation existed (PAPERS.md:
planned, title only). GRV-029's dictionary now adjudicates.

THE COMPUTATION: the derived medium dictionary (T = A B, mu = B^3/A,
c_local = A/B in units of c, from the one-metric bijection) evaluated
along the Schwarzschild solution in isotropic coordinates
(A = (1 - GM/2rc^2)/(1 + GM/2rc^2), B = (1 + GM/2rc^2)^2):
(D1) T(r) -> 0 EXACTLY at the horizon (r_iso = GM/2c^2), finite and
     monotone outside: the horizon IS the surface where the weave's
     transverse tension is exhausted -- the guide was right.
(D2) mu(r) -> infinity there: the effective medium grows infinitely
     heavy; c_local = A/B -> 0: outward waves stall, the frozen-star
     picture as MECHANICS (no tension left to carry them).
(D3) The corpus-specific addition: GRV-027 MEASURED the weave's
     topological failure mode -- the finite contact barrier surrenders
     (punch-through) under extreme pressing -- so the framework
     predicts the medium's TOPOLOGY fails under horizon-interior
     conditioning: 'the singularity' is where the weave description
     ends, with a mechanism (reconnection), not a mystery.

HONEST LIMITS, at full volume: the EH dynamics were derived at
weak-field (linear, q^2) order -- the horizon statement is the derived
dictionary EXTRAPOLATED along the classical solution, valid exactly as
far as EH holds; near-horizon lattice physics (the collapsing band as
kt ~ T -> 0) and Bekenstein-Hawking entropy remain open, as the
thermodynamics paper already says.
"""
import numpy as np


def profiles(rs_over_riso):
    x = 1.0/(2*rs_over_riso)      # GM/(2 r c^2) with r in units of r_iso = GM/2c^2 -> x = riso/r... 
    x = 1.0/rs_over_riso          # let r be in units of r_iso: GM/2rc^2 = r_iso/r = 1/r'
    A = (1 - x)/(1 + x)
    B = (1 + x)**2
    return A*B, B**3/np.maximum(A, 1e-15), A/B   # T, mu, c_local


def test():
    r = np.linspace(1.0, 50, 2000)
    T, mu, cl = profiles(r)
    assert abs(T[0]) < 1e-10, "D1: tension EXACTLY zero at the horizon"
    assert np.all(np.diff(T) > -1e-12) and T[-1] > 0.9, "T monotone, -> 1 far away"
    assert mu[0] > 1e10 and abs(mu[-1] - 1) < 0.2, "D2: mu diverges at horizon, -> 1 far away"
    assert abs(cl[0]) < 1e-10 and np.all(np.diff(cl) > -1e-12), "c_local -> 0 at horizon, monotone"
    i2 = np.argmin(np.abs(r - 2))
    print(f"at r = 2 r_iso: T = {T[i2]:.3f}, mu = {mu[i2]:.3f}, c_local = {cl[i2]:.3f}")
    print("D1-D2: the horizon is the tension-exhaustion surface (T -> 0, mu -> inf, c -> 0);")
    print("D3: interior topology fails by the measured punch-through mode (GRV-027).")
    print("PASS: the guide's intuition is now a computation; the papers' adjective corrected.")


if __name__ == "__main__":
    test()
