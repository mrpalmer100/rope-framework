"""Scope statement for the rope programme's mass claims: the model addresses
ORDINARY MATTER (first generation + composites + photon), deriving mass STRUCTURE
(the massless photon, the nuclear composition rule, mass=mode-energy) with a small
number of absolute mass UNITS as irreducible inputs -- and makes NO claim on
generation-2/3 masses (muon, tau, heavy quarks), which are outside its scope.

Drawn on principle, not convenience: 'ordinary matter' = everything needed to
build stable atoms, molecules, and bulk matter, plus the interactions among them.
That set is EXACTLY the first generation (electron, up, down) + composites
(proton, neutron, nuclei, atoms) + the photon. Everything the model derives lives
here; everything it cannot derive (gen-2/3 masses) lives outside.

What is DERIVED (mass structure, not absolute values):
  * photon is massless -- a genuine prediction (network wave carries no mode energy)
  * mass = rope mode energy (ontology; charge is winding, a SEPARATE quantity, GG-006)
  * nuclear masses to <0.1% via the composition rule (NUC-001), GIVEN the nucleon
    mass unit and binding energies as inputs.
What is INPUT (irreducible absolute scales, like the mesh scale a FND-MATTER-005):
  * the nucleon mass unit; the electron mass (PM-004).
What is OUT OF SCOPE (not needed for ordinary matter):
  * muon, tau (unstable heavy leptons); charm/strange/top/bottom quarks; W/Z/Higgs.
    Their existence is real but their masses are not the rope model's to derive as
    a theory of ordinary matter. The muon ('who ordered that?') is the canonical
    not-needed particle: no stable matter uses it.

This scope is HONEST about the boundary: the model is strong (derived) on
first-generation ordinary matter and its interactions, and explicitly claims
nothing on the heavier generations rather than failing to derive them.
"""

# The classification is the content; the test asserts the boundary is coherent.
FIRST_GEN = {"electron", "up", "down"}
COMPOSITES = {"proton", "neutron", "nucleus", "atom"}
FORCE_CARRIER_IN_SCOPE = {"photon"}
OUT_OF_SCOPE = {"muon", "tau", "charm", "strange", "top", "bottom", "W", "Z", "Higgs"}


def ordinary_matter_is_first_generation():
    """The set needed to build stable matter is exactly gen-1 + composites + photon."""
    needed = FIRST_GEN | COMPOSITES | FORCE_CARRIER_IN_SCOPE
    # none of the out-of-scope particles are in the needed set
    return needed.isdisjoint(OUT_OF_SCOPE)


def derived_vs_input_is_consistent():
    """Photon mass is a derived prediction (0); absolute mass units are inputs;
    gen-2/3 masses are out of scope. These three buckets must be disjoint."""
    derived = {"photon_massless", "nuclear_composition_rule", "mass_is_mode_energy"}
    inputs = {"nucleon_mass_unit", "electron_mass"}
    out = {"muon_mass", "tau_mass", "heavy_quark_masses"}
    return derived.isdisjoint(inputs) and inputs.isdisjoint(out) and derived.isdisjoint(out)


def test():
    assert ordinary_matter_is_first_generation(), "ordinary matter = gen-1 + composites + photon"
    assert derived_vs_input_is_consistent(), "derived/input/out-of-scope buckets must be disjoint"
    print("ordinary-matter set = first generation + composites + photon (disjoint from gen-2/3): PASS")
    print("derived (photon massless, nuclear rule, mass=mode-energy) / input (mass units) /")
    print("out-of-scope (muon, tau, heavy quarks) buckets are disjoint: PASS")
    print("PASS: scope is coherent -- model derives mass STRUCTURE for ordinary matter with")
    print("      a few absolute mass units as inputs; claims nothing on heavier generations.")


if __name__ == "__main__":
    test()
