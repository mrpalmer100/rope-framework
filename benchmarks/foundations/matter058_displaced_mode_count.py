"""FND-MATTER-058: the displaced-mode count -- the named closer for the
dilute-Casimir suppression. Bars locked BEFORE computing
(analysis/MATTER058_displaced_mode_count_results.md):
(1) THE FORCED/PERMITTED SPLIT IS THE SESSION'S CENTRAL DISCIPLINE and is
declared before any arithmetic. A factor is FORCED only if the construction
cannot be written without it. A factor that is a defensible reading of a
registered relation but could honestly be read otherwise is PERMITTED, and
PERMITTED FACTORS MAY NOT BE ADOPTED -- they are displayed, their effect
stated, and refused. Only the product of FORCED factors is compared to the
target.
(2) FACTORS ARE ENUMERATED AND CLASSIFIED BEFORE EVALUATION:
    F1 transverse polarizations (the ambient band has two; a displacing
       inclusion removes both) -- claimed FORCED.
    F2 the displaced cross-section pi r^2 for a cylinder of radius r --
       claimed FORCED (geometry, no convention).
    P1 the FND-017 directional share (T0 = Sigma a^2/3 carries a 3 for
       strand directions per cell; whether the per-direction available
       cross-section is a^2 or a^2/3 is a READING) -- claimed PERMITTED.
(3) ONE COMPARISON ONLY, after the forced product is fixed. The
factor-2 admission bar from FND-MATTER-055/056 still binds.
(4) NO RESCUE: if the forced product misses, the session may not promote a
permitted factor to close it. That is the exact move refused in
FND-MATTER-056 and it does not become legitimate by being one session
later.
(5) NO NEW CALIBRATION; target inherited from FND-MATTER-055 unchanged.
"""
import numpy as np

R_OVER_A = 9.4e-4
TARGET = 1.156e-5
BAR = 2.0


def main():
    base = np.pi * R_OVER_A**2
    print(f"BASE (FND-MATTER-056, dilute displacement): pi (r/a)^2 = "
          f"{base:.3e}")

    print("FORCED FACTORS (classified before evaluation):")
    print("  F1 polarizations = 2. The ambient transverse band carries two")
    print("     independent polarizations at every wavevector; a displacing")
    print("     inclusion removes the medium for BOTH. The construction")
    print("     cannot be written with one -- FORCED.")
    print("  F2 cross-section = pi r^2. Cylinder geometry, no convention")
    print("     available -- FORCED (already in the base; listed for")
    print("     completeness, contributes no additional factor).")
    forced = 2.0
    lam_forced = base * forced
    print(f"  FORCED PRODUCT = {forced:.0f}  ->  lambda = {lam_forced:.3e}")

    print("PERMITTED FACTOR (displayed, NOT adopted):")
    print("  P1 the FND-017 directional share. T0 = Sigma a^2/3 carries a 3")
    print("     counting strand directions per cell. Whether the")
    print("     cross-section available to a displacing strand is a^2 (all")
    print("     directions share the cell face) or a^2/3 (one direction's")
    print("     share) is a READING of that relation, not a consequence of")
    print("     it. Both are defensible; the corpus has never had to choose.")
    lam_permitted = lam_forced * 3.0
    print(f"     If adopted it would give lambda = {lam_permitted:.3e}, "
          f"landing {max(lam_permitted,TARGET)/min(lam_permitted,TARGET):.2f}x"
          f" from target -- INSIDE the bar.")
    print("     IT IS NOT ADOPTED. Per bar (4), a permitted factor that")
    print("     happens to close a gap is precisely the fitted coefficient")
    print("     this campaign has refused five times today. Adopting it")
    print("     BECAUSE it lands would invert the logic: the reading must be")
    print("     settled on its own merits, by a session that does not know")
    print("     the target.")

    print("THE ONE COMPARISON (forced product only):")
    gap = TARGET / lam_forced
    print(f"  target {TARGET:.3e} / forced {lam_forced:.3e} = {gap:.2f}x")
    inside = gap <= BAR
    print(f"  bar = {BAR:.0f}x  ->  {'INSIDE' if inside else 'OUTSIDE'}")
    assert not inside and gap < 2.2

    print("VERDICT: A NEAR MISS, OUTSIDE THE BAR BY 4 PERCENT. The forced")
    print("  construction lands at 2.08x where 2.00x was required. The")
    print("  corpus does not round bars: the candidate is NOT promoted,")
    print("  lambda REMAINS OPEN, and the honest statement is that the")
    print("  mechanism is now within a factor of two of the target and")
    print("  cannot be certified at a factor of two.")
    print("  Compare the day's trajectory on this quantity: an unfixed 25")
    print("  percent this morning, a factor 4.16 miss two sessions ago, a")
    print(f"  factor {gap:.2f} now -- each step from forced structure, none")
    print("  from fitting, and the calibration count still ONE.")

    print("WHAT WOULD SETTLE IT, named precisely and target-blind: a session")
    print("  that resolves the FND-017 directional reading ON ITS OWN")
    print("  MERITS -- does a displacing strand see the full cell face or")
    print("  one direction's share? -- WITHOUT reference to lambda or its")
    print("  target. That reading is a fact about the corpus's own")
    print("  geometry, it is decidable, and it is currently the single")
    print("  unsettled convention standing between this mechanism and a")
    print("  verdict. If it resolves to a^2, the mechanism misses by 2.08")
    print("  and is likely wrong in detail; if to a^2/3, it lands at 1.44")
    print("  and becomes the sector's first derived lever.")
    print("NOT CLAIMED: lambda; the permitted factor; any lepton mass")
    print("  (PM-004 stands); any new parameter.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
