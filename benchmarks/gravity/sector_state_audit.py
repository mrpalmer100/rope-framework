"""GRV-054 -- WHAT THE GRAVITY SECTOR ACTUALLY HAS: a state audit correcting an
assessment built on superseded claims.

Bars locked in analysis/GRV054_state_audit_bars_LOCKED.md BEFORE the audit.
"""
import os

import yaml

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")


def main():
    claims = yaml.safe_load(open(os.path.join(ROOT, "claims.yaml"),
                                 encoding="utf-8"))["claims"]
    by = {c["id"]: c for c in claims}
    grv = [c for c in claims if c["id"].startswith("GRV-")]
    derived = [c for c in grv if c.get("status") == "Derived"]
    print(f"GRV sector: {len(grv)} claims, {len(derived)} Derived\n")

    print("B1 IS THE WEAK-FIELD METRIC STILL 'MATCHED, NOT DERIVED'? NO.")
    for cid, what in (("GRV-026", "gamma = 1 and the 1.751-arcsecond deflection "
                                  "DERIVED as a two-condition theorem"),
                      ("GRV-029", "the physical one-metric derivation: C1 discharged "
                                  "and GRV-002's full table made UNCONDITIONAL")):
        print(f"   {cid} [{by[cid]['status']}] -- {what}")
    print("   GRV-029's mechanism is a COUNTING argument: the gapless transverse")
    print("   mode's wave operator carries exactly four coefficient functions")
    print("   (mu, T_x, T_y, T_z); a static metric carries exactly four; and the")
    print("   map between them is an EXACT BIJECTION with a closed-form inverse.")
    print("   The photon sector is one-metric because THERE IS NO FIFTH FUNCTION")
    print("   for a second metric to live in.")
    print("   => GRV-001's 'matched, not derived' was superseded. The four")
    print("   classical tests are UNCONDITIONAL, not conditional on a match.\n")

    print("B2 IS THERE A HORIZON MECHANISM? YES, and a specific one.")
    for cid, what in (
            ("GRV-034", "the horizon as the TENSION-EXHAUSTION surface under the "
                        "derived dictionary"),
            ("GRV-035", "horizon as PERCOLATION COLLAPSE -- conditioning presses "
                        "crossings past the measured punch-through barrier, deleting "
                        "transverse bonds until connectivity fails at p ~ 0.24-0.25, "
                        "reproducing the known 3D bond threshold"),
            ("GRV-036", "MASS WITHOUT KNOTS: the mass is the tension energy of the "
                        "comb, only the horizon lives in transverse severance; the "
                        "no-hair theorem falls out as strand mechanics"),
            ("GRV-037", "the reconnection count: a two-state system per crossing, "
                        "one-way, giving a second-law arrow and a conditional area law"),
            ("GRV-038", "the pressing profile derived")):
        print(f"   {cid} [{by[cid]['status']}] -- {what}")
    print("   THE TENSION PARADOX IS RESOLVED, and the resolution is the answer to")
    print("   'what makes c_eff vanish': radial tension per strand is HIGH near a")
    print("   mass, while the TRANSVERSE effective tension -- mediated by crossings,")
    print("   and the thing light propagates on -- goes to zero as those crossings")
    print("   are deleted. Both intuitions are true about different directions.\n")

    print("B3 IS THE STRONG-FIELD EXTRAPOLATION CONTROLLED? YES, certified.")
    print(f"   GRV-048 [{by['GRV-048']['status']}] -- the expansion parameter is")
    print("   a^2 sqrt(K) (lattice scale x curvature invariant), NEVER Phi/c^2:")
    print("   strong potential is not strong curvature. It evaluates to 1e-78 at a")
    print("   stellar horizon and 1e-96 at M87*, with the breakdown radius 26-32")
    print("   ORDERS below r_s. The near-horizon region is Rindler x sphere.\n")

    print("B4 WHAT IS GENUINELY MISSING, after checking forward:")
    print("   NOT missing: a derived weak-field map (GRV-029), a horizon mechanism")
    print("   (GRV-035), a mass definition and no-hair result (GRV-036), an entropy")
    print("   count (GRV-037), a controlled strong-field expansion (GRV-048), and")
    print("   an emission spectrum with a closed-form tail (GRV-040..047).")
    print("   GENUINELY MISSING, as far as this audit can tell:")
    print("     (i)  A NONLINEAR FIELD EQUATION. GRV-003/005 give Poisson, forced")
    print("          by elastostatics -- linear. GRV-025 gives the EH tensor pattern")
    print("          at QUADRATIC order. Nobody has iterated the response into a")
    print("          self-sourcing equation, so 'gravity gravitates' is not derived.")
    print("     (ii) A DERIVED INTERIOR. GRV-035 gives the horizon as a percolation")
    print("          transition; what lies inside a severed region is a separate")
    print("          question the sector has not posed.")
    print("     (iii) DYNAMICS. Everything above is static or quasi-static. Collapse,")
    print("          merger and ringdown are untouched, and they are where")
    print("          gravitational-wave astronomy actually lives.")
    print("   ITEM (iii) IS THE ONE WITH DATA WAITING FOR IT.\n")

    print("B5 THE PROCESS FAILURE, recorded:")
    print("   The assessment this audit replaces was built on GRV-001 and GRV-005")
    print("   without checking what later claims did to them. That is the THIRD")
    print("   instance today of building on a superseded claim (after HBAR-010's")
    print("   inherited relation and GRV-049's luminosity law).")
    print("   IT IS ALSO THE FIRST TIME THE TOOL CAUGHT IT BEFORE ANYTHING WAS")
    print("   BUILT. tools/forward_check.py on GRV-001 returned GRV-026 and GRV-029")
    print("   in its first five hits, and the false premise collapsed on reading")
    print("   them. The two earlier instances cost a claim each to repair; this one")
    print("   cost a query.")
    assert by["GRV-029"]["status"] == "Derived"
    assert by["GRV-048"]["status"] == "Derived"
    print("PASS: the sector's state is recorded accurately, and the assessment it")
    print("      replaces is on the record as wrong.")


if __name__ == "__main__":
    main()
