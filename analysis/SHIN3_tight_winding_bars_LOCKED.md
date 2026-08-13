# COMMISSION SHIN3 -- TIGHT-WINDING CONSTRUCTIBILITY AND DISPERSION: BARS, LOCKED BEFORE COMPUTING

Locked 2026-08-12. Successor to FND-084 (loose winding excluded).
Question: does a consistent geometry window exist for winding with
pitch <= wavelength, and does the tight-wound medium then propagate
short waves isotropically? The author's conditional adoption
authorization (adopt on pass) carries over from TAV3, restated in
this session's charter; a failure is registered and kept.

## G1 -- the constructibility window (exact arithmetic, locked relations)

Tight winding slows the medium: axial tension per fiber scales as
sin(psi), axial mass density as 1/sin(psi), so the effective speed is
c sin(psi_eff) with psi_eff the composed pitch factor
(sin psi_1 sin psi_2 for two levels). Restoring c requires raising
T_f by 1/sin^2(psi_eff), which raises Sigma by the same factor and
spends Lorentz margin. LOCKED WINDOW CONDITIONS, all simultaneous:
- W-a (averaging): both pitches p_i <= lambda (= 6 a_f engine /
  1.41e-22 m physical).
- W-b (Lorentz): sin^2(psi_eff) >= 1/margin, margins 6.1 (kappa50)
  and 10.5 (kappa250) from FND-040's live readings.
- W-c (coverage): the SHIN2 two-level annulus [|A1-A2|, A1+A2],
  A_i = arccos(sin psi_i), must cover >= 10 percent of the sky
  (same bar as FND-059/SHIN2).
- W-d (radius): R_i = p_i/(2 pi tan psi_i) reported; no bar (the
  interpenetration primitive forbids nothing here), but sub-spacing
  radii are DISCLOSED as a geometric novelty with unpriced bending
  cost (kb unscaled -- the standing caveat).
PASS: a nonempty (psi_1, psi_2) window satisfying W-a..W-c at both
kappa readings. FAIL: empty window at either.

## G2 -- the tight-wound Bloch check (the decisive computation)

The validated TAV3B instrument, unchanged in machinery and
thresholds, at TIGHT pitch: supercell grid locked at
(P1, P2) in {(3, 4), (4, 6), (5, 6), (6, 6)} -- every pitch <= lambda
= 6. Same |k| = 2 pi/6, same 8 directions, same bars:
- B1 propagation: min group speed >= 0.3;
- B2 isotropy: phase-speed spread <= 0.05;
- B3 straightness: group-angle error <= 15 degrees;
- W0 straight control revalidated once (already on record from TAV3B).
PASS: any locked (P1, P2) member passes B1-B3. FAIL: none does.
The passing member's speed reduction factor is REPORTED next to the
G1 window (the two must be mutually consistent for adoption).

## Verdict grammar, pre-authorized
- G1 PASS + G2 PASS -> GRANT-SUBSTRUCTURE-TIGHT adopted per the
  author's standing conditional authorization, recorded as an
  author's act with the price sheet (fine-strand primitive; n_sub;
  two pitches inside the derived window; the 1/sin^2 tension
  compensation with its Lorentz spend; kb bending cost unpriced;
  FND-REL-002 Derived-grade re-derivation still owed).
- Any FAIL -> Failed-and-kept, no adoption, candidate to the closed
  list or the desk per the failing mode.
No bar-shopping: the pitch set, thresholds, and window conditions
are final.
