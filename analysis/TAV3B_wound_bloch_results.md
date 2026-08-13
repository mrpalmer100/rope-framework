# COMMISSIONS TAV3/TAV3B -- THE WOUND-CARRIER DISPERSION CHECK: RESULTS

Executed 2026-08-12 under analysis/TAV3_wound_dispersion_bars_LOCKED.md
(time-domain; returned INSTRUMENT-INVALID -- no clean propagation in
its own control) and analysis/TAV3B_wound_bloch_bars_LOCKED.md (Bloch
eigenanalysis with plane-wave spectral identification; valid and
decisive). Benchmarks: benchmarks/foundations/tav3_wound_dispersion.py,
tav3b_wound_bloch.py.

## Verdict: FAILED-AND-KEPT. No adoption.

The control behaves as required (straight medium: 45 percent
directional phase-speed spread at lambda = 6 a_f -- the obstruction
is visible to the instrument). The wound medium then fails all three
bars:
- B1 PROPAGATION: group speed collapses to 0.046 along the lattice
  axes (bar 0.3).
- B2 ISOTROPY: phase-speed spread 31 percent (bar 5 percent).
- B3 STRAIGHTNESS: group-velocity misalignment up to 109 degrees
  (bar 15), with plane-wave spectral weight fragmenting to 0.11-0.26
  in most directions -- the short wave is strongly scattered, not
  cleanly carried.

## Why it failed, and what the failure teaches

The scattering is physics, not artifact: at lambda = 6 a_f against
winding periods (24, 60) a_f, each wavelength lives on locally
STRAIGHT fibers pointing one particular way -- direction-averaging
requires the winding to turn WITHIN a wavelength, i.e. pitch at or
below lambda. SHIN2's coverage geometry (necessary) and this
dispersion check (the sufficiency test) together sharpen the
candidate into its surviving form: TIGHT winding, pitch <= the
propagation wavelength, which at the PeV demand means winding at the
fine-lattice scale itself -- a maximally twisted medium. Whether such
a geometry is constructible with spacing-separated fibers, and
whether it then propagates isotropically, is a well-posed successor
question with fresh bars. Loose hierarchical winding is EXCLUDED as
the repair.

## Standing after this session

GRANT-CANDIDATE-SUBSTRUCTURE: NOT adopted (the author's
pre-authorization was conditional on a pass; the condition failed).
The candidate returns to the desk in sharpened form
(tight-winding variant). KNOWN_LIMITATIONS' route (c) disclosure
stands unchanged. FND-083's length-axis result (redistribution at
zero Lorentz cost) is untouched by this failure -- the length
purchase remains sound; the direction purchase does not yet exist.
