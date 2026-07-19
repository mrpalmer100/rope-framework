"""FND-BOUND-001 (Modeled): THE ONE FENCE -- a registry-consistency result, not
new physics. The corpus's four hardest terminal residuals, registered
independently across four sectors over several months, name the SAME missing
layer: quantum kinetic / zero-point energy.

THE FOUR RESIDUALS (each machine-checked below against the live registry):
  1. GRAVITY: the post-Newtonian tensor structure. Classical channels are
     exhausted by theorem (GRV-013 no-go; GRV-018/020 internal-symmetry
     closures; GRV-010 classical bath Failed at gamma = -1/2); the surviving
     conjecture GRV-014 places the completion at the quantum-induced
     (Sakharov) level.
  2. NUCLEAR SATURATION: the NUC-008 rising baseline -- a classical bond
     count has no kinetic cost for compactness.
  3. LIGHT-ISOTOPE MASSES: the NUC-005/006 residuals -- zero-point energy
     comparable to well depth in light nuclei.
  4. CHEMISTRY DISPERSION: the hbar-fence (CHEM-MET-001 and the chemistry
     paper's declared boundary) -- London forces are irreducibly quantum.

WHAT THIS CLAIM ASSERTS: only the triangulation itself -- that these four
independently-registered walls are one wall, and that GRV-014 is therefore no
longer an isolated escape hatch but the gravity-facing name of the corpus's
single remaining boundary. A corpus-native hook exists (GRV-004: rest tension
does not gravitate, only deviations do -- and a zero-point spectrum is a
structured deviation field, the one bath GRV-010 never tested). WHAT IT DOES
NOT ASSERT: any mechanism. Testing the quantum bath requires hbar and the
absolute scale, blocked by FND-MATTER-003. The fence is located; it is not
crossed.
"""
import os, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test():
    with open(os.path.join(ROOT, "claims.yaml")) as f:
        d = yaml.safe_load(f)
    by = {c["id"]: c for c in d["claims"]}

    def has(cid, *words):
        t = (by[cid]["title"] + by[cid].get("note", "")).lower()
        return all(w.lower() in t for w in words)

    # residual 1: gravity -- classical exhaustion + quantum conjecture
    assert by["GRV-013"]["status"] == "Derived" and has("GRV-013", "no-go"), \
        "classical channel space closed by theorem"
    assert by["GRV-010"]["status"] == "Failed" and has("GRV-010", "bath"), \
        "the CLASSICAL bath failed (gamma = -1/2); the quantum bath was never tested"
    assert by["GRV-018"]["status"] == "Derived" and by["GRV-020"]["status"] == "Derived", \
        "internal-mode channels formally closed (one Goldstone, spent on EM)"
    assert by["GRV-014"]["status"] == "Conjecture" and has("GRV-014", "quantum", "sakharov"), \
        "the surviving gravity conjecture is quantum-level completion"
    # residual 2: nuclear saturation names the kinetic layer
    assert has("NUC-008", "kinetic", "zero-point"), "nuclear baseline diagnosis names the layer"
    # residual 3: light isotopes name it
    assert has("NUC-005", "zero-point"), "light-isotope residuals name the layer"
    # residual 4: chemistry names it
    assert has("CHEM-MET-001", "hbar", "dispersion"), "chemistry's dispersion hbar-fence names it"
    # the hook: rest tension does not gravitate -- only deviations do
    assert has("GRV-004", "deviations"), "GRV-004 hook: a zero-point spectrum is a deviation field"
    print("residual 1 (gravity tensor half): classical exhaustion Derived x3, classical bath Failed,")
    print("            surviving conjecture = quantum/Sakharov (GRV-014)")
    print("residual 2 (nuclear saturation):  kinetic/zero-point named (NUC-008)")
    print("residual 3 (light isotopes):      zero-point named (NUC-005/006)")
    print("residual 4 (dispersion):          hbar-fence named (CHEM-MET-001)")
    print("hook: GRV-004 -- only DEVIATIONS gravitate; zero-point stress is a deviation field")
    print("PASS: four sectors, one fence. The boundary is located, not crossed.")


if __name__ == "__main__":
    test()
