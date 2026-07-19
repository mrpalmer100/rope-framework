"""QB-010 (Modeled): BOHMIAN ADJACENCY -- the cornered limb's territory is
occupied, viable, and the remaining gap is machine-localized to ONE structural
question: which space the budget lives in.

(i) EXISTENCE PROOF (literature): the QB-008/009 limb -- preferred frame,
    instantaneous influence, wave guiding discrete outcomes -- is de Broglie-
    Bohm territory (de Broglie 1927; Bohm 1952, Phys. Rev. 85, 166 & 180).
    dBB reproduces ALL of quantum mechanics in equilibrium (Durr-Goldstein-
    Zanghi 1992), including g2 = 0 AND CHSH = 2*sqrt(2). The territory is
    proven habitable. Priority is Bohm's, not ours.
(ii) THE GAP, MACHINE-LOCALIZED (this file): run the IDENTICAL first-arrival
    race twice. Physical-space per-particle budgets (the QB-009 toy, honest
    mesh ontology): S ~ sqrt(2). Grant the configuration-space joint object
    (rates from the entangled psi's joint intensities -- Bohm's home, imported
    not derived): the SAME race gives S ~ 2*sqrt(2). One change, quantum gap
    crossed: the deficit is not the race mechanics but WHERE the intensities
    live. The summit question 'can a mesh-native shared budget push S past 2'
    is therefore exactly 'can configuration-space guidance emerge from
    physical-space mesh mechanics' -- a recognized open problem in Bohmian
    foundations itself (cf. Norsen 2010, the theory of exclusively local
    beables, which attempts and only partially achieves it).
(iii) THE LEDGER, both directions. Bohm has, we lack: entanglement (the
    config-space wavefunction), equilibrium analysis, seven decades of
    development. The mesh has, Bohm lacks: DERIVED indivisibility (dBB
    postulates point particles; QB-007a derives all-or-nothing from
    topology), an independently-motivated preferred foliation (relativistic
    dBB needs one unexplained; the mesh/CMB frame has independent physical
    content and a quantified mechanical demand, K_L/K_T >= 1.9e8), and the
    contamination-structure match of g2 (QB-009).
"""
import numpy as np


def chsh_physical_space(rng, n=200000):
    """QB-009's honest toy: per-particle budgets, shared polarization HV."""
    lam = rng.uniform(0, np.pi, n)
    def outcome(setting):
        return np.where(rng.random(n) < np.cos(lam - setting)**2, 1, -1)
    a, ap, b, bp = 0.0, np.pi/4, np.pi/8, 3*np.pi/8
    E = lambda s1, s2: np.mean(outcome(s1)*outcome(s2))
    return abs(E(a, b) - E(a, bp) + E(ap, b) + E(ap, bp))


def chsh_configuration_space(rng, n=200000):
    """Same race, but rates from the JOINT intensities of the entangled state
    (imported, not derived -- the diagnostic, and the honest circularity)."""
    a, ap, b, bp = 0.0, np.pi/4, np.pi/8, 3*np.pi/8
    def E(s1, s2):
        d = s1 - s2
        rates = np.array([0.5*np.cos(d)**2, 0.5*np.sin(d)**2,   # ++, +-
                          0.5*np.sin(d)**2, 0.5*np.cos(d)**2])  # -+, --
        t = rng.exponential(1.0/np.maximum(rates, 1e-300), (n, 4))
        w = np.argmin(t, axis=1)                                 # first arrival on the JOINT space
        val = np.array([1, -1, -1, 1])
        return np.mean(val[w])
    return abs(E(a, b) - E(a, bp) + E(ap, b) + E(ap, bp))


def test():
    rng = np.random.default_rng(11)
    S_phys = chsh_physical_space(rng)
    S_conf = chsh_configuration_space(rng)
    assert S_phys < 2.0, "physical-space budget: below the classical bound (the honest toy)"
    assert abs(S_phys - np.sqrt(2)) < 0.05, "and specifically at the Malus-LHV value sqrt(2)"
    assert S_conf > 2.0, "configuration-space budget: CROSSES the classical bound"
    assert abs(S_conf - 2*np.sqrt(2)) < 0.05, "and lands on the quantum value 2*sqrt(2)"
    print(f"identical race mechanism, one structural change:")
    print(f"  budget in PHYSICAL space (per-particle, mesh-honest):   S = {S_phys:.3f}  (sqrt(2) = 1.414)")
    print(f"  budget on CONFIGURATION space (joint psi, imported):    S = {S_conf:.3f}  (2sqrt(2) = 2.828)")
    print(f"GAP LOCALIZED: the deficit is not the race -- it is which space the budget lives in.")
    print(f"The summit question is exactly: can configuration-space guidance EMERGE from mesh mechanics.")
    print("PASS: adjacency registered; existence proof cited; gap machine-localized; ledger stated.")


if __name__ == "__main__":
    test()
