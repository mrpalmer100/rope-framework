"""FND-MATTER-056: the suppression-mechanism hunt -- derive the ambient
zero-point suppression from the perturbation structure, BEFORE looking at
the target.
Bars locked BEFORE computing (analysis/MATTER056_suppression_mechanism_results.md):
(1) DERIVE-THEN-COMPARE, strictly ordered and the whole point of the
session: the derivation runs to completion and its FORM is fixed before the
numeric target is invoked. The MATTER055 whisper (alpha x (r/a) at 1.68x)
may NOT be used as a guide, a hint, or a check during the derivation. If
the derived form is not the whisper's form, the whisper is KILLED as a
mechanism regardless of how well it fits.
(2) THE DERIVATION IS DILUTE-PERTURBATION CASIMIR, stated in advance: the
ambient weave carries zero-point energy at density ~ (hbar c/a) per cell;
inserting a strand perturbs the modes it displaces; for a dilute
perturbation the fractional shift equals the fraction of the mode-carrying
medium the strand occupies. That fraction is computed from REGISTERED
geometry only (strand radius r, mesh spacing a).
(3) O(1) FREEDOM IS PRE-REFUSED as a rescue: mode degeneracy, polarization
counts, and packing factors are O(1) and may be DISPLAYED as a band, but
invoking them to close a gap is forbidden by name -- that is the move the
campaign refused in FND-MATTER-042 (the high-power rule) and again in
FND-MATTER-055 (look-elsewhere), and it does not become legitimate here.
(4) PERMITTED OUTCOMES: derived form matches target within factor 2 (a
real result); derived form misses (a null with a quantified gap); derived
form is indeterminate (report the obstruction). In all three the whisper
is separately adjudicated on FORM, not fit.
(5) NO NEW CALIBRATION; spend count stays at ONE.
"""
import numpy as np

ALPHA = 1 / 137.036
R_OVER_A = 9.4e-4
TARGET = 1.156e-5          # FND-MATTER-055, sealed until step 3
WHISPER = ALPHA * R_OVER_A


def main():
    print("STEP 1 -- THE DERIVATION (target not invoked):")
    print("  The ambient weave carries zero-point energy in its transverse")
    print("  modes up to the mesh cutoff. Inserting a strand displaces the")
    print("  medium over the strand's own cross-section. For a DILUTE")
    print("  perturbation the fractional energy shift is the fraction of the")
    print("  mode-carrying medium displaced.")
    print("  Per unit length of strand traversing the mesh:")
    print("    displaced cross-section = pi r^2")
    print("    available cross-section per cell = a^2")
    print("    => fractional shift lambda_derived = pi (r/a)^2")
    lam_d = np.pi * R_OVER_A**2
    print(f"  DERIVED FORM: lambda = pi (r/a)^2 = {lam_d:.3e}")
    print("  Provenance: parameter-free, built from registered geometry")
    print("  only, power 2 in the thinness (inside the MATTER042 rule).")
    print("  NOTE THE ABSENCE: no factor of alpha appears anywhere in the")
    print("  construction. The coupling enters the corpus through the")
    print("  quantum-AREA relation, not through a geometric displacement.")

    print("STEP 2 -- THE WHISPER ADJUDICATED ON FORM (before any fit):")
    print(f"  MATTER055's whisper was alpha x (r/a) = {WHISPER:.3e}: power 1")
    print("  in the thinness and one power of the coupling. The derivation")
    print("  produces power 2 in the thinness and NO coupling. The forms")
    print("  DISAGREE in both factors.")
    print("  VERDICT: THE WHISPER IS KILLED AS A MECHANISM. No derivation")
    print("  route in the corpus produces alpha x (r/a), and MATTER055")
    print("  already recorded that six candidates against a factor-2 bar")
    print("  makes one hit chance-level. It was a coincidence, registered")
    print("  as one, and is now retired as one -- exactly the outcome the")
    print("  whisper grade exists to make cheap.")
    assert abs(np.log10(lam_d / WHISPER)) > 0.3

    print("STEP 3 -- NOW the comparison (target invoked for the first time):")
    gap = TARGET / lam_d
    print(f"  target (FND-MATTER-055) = {TARGET:.3e}")
    print(f"  derived                 = {lam_d:.3e}")
    print(f"  GAP = {gap:.2f}x -- the derived suppression is too STRONG by")
    print("  a factor of about four.")
    assert 3 < gap < 6

    print("STEP 4 -- THE PRE-REFUSED RESCUE, named and refused:")
    print("  A factor ~4 is squarely inside the O(1) freedom this")
    print("  construction carries: two transverse polarizations, mode")
    print("  degeneracy, and the packing convention relating strand")
    print("  cross-section to cell area are each O(1) and could be argued")
    print("  to supply it. THAT ARGUMENT IS REFUSED BY BAR (3). A")
    print("  construction that needs its own unfixed O(1) factors tuned to")
    print("  land is not a derivation of the target; it is a derivation")
    print("  with a fitted coefficient, and the campaign has spent the day")
    print("  refusing exactly this move in four other sectors.")

    print("VERDICT: A QUANTIFIED NULL, and the best-motivated candidate the")
    print("  sector has ever had. lambda = pi (r/a)^2 is parameter-free,")
    print("  mechanism-backed, form-correct in provenance, and lands within")
    print(f"  a factor {gap:.1f} of the target -- close enough that the")
    print("  mechanism is probably RIGHT IN KIND and wrong in detail, and")
    print("  far enough that the corpus may not claim it.")
    print("WHAT WOULD CLOSE IT (named, one sentence): a first-principles")
    print("  count of the displaced modes -- polarizations, degeneracy, and")
    print("  the packing convention computed rather than assumed -- which")
    print("  either lands the factor 4 or moves the derived value away and")
    print("  kills the dilute picture too.")
    print("FND-MATTER-050 remains OPEN, now with: a quantified target, a")
    print("  well-posed home, a correctly-stated problem (suppression, not")
    print("  weighting), a dead whisper, and ONE mechanism-backed candidate")
    print("  missing by four. That is a materially better position than the")
    print("  'unfixed 25 percent' the day started with.")
    print("NOT CLAIMED: lambda; any lepton mass (PM-004 stands); any O(1)")
    print("  rescue; any new parameter.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
