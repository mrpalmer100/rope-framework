# COMMISSION AXIS-MEANING (ITEM 6b) -- RESULTS (2026-09-05)
Charter analysis/ITEM6_charters_LOCKED.md section 6b + amendment (box
scaled with s; point spacing fixed). Engine: ELEC-099's
pe2_pbc_prefactor.py functions reused byte-identically
(benchmarks/foundations/axis_meaning_ladder.py); logs analysis/axis/.

## VERDICTS
  Q3  ** NO CALL ** under the locked forms (neither R3-COARSE nor
      R3-FIXED): the s-ladder does not track s^(-3/2) and is not
      monotone -- the fitted harmonic amplitude CHANGES SIGN rung to
      rung and the fit quality collapses on two of four rungs.
  Q1  ** NOT EVALUABLE **: the conversion to the physical electron
      rests on the fixed s^(-3/2) scaling from s = 1.5 (ELEC-096 as
      input, ELEC-099's stated conditionality); the ladder shows that
      premise is not exhibited on the registered engine. R1-EXCLUDED /
      R1-LIVE cannot be rendered.
  Q2  DEFERRED (registry sweep; not started this session).
  Joint: no reading is closed. The commission's finding is upstream of
  all three readings: ELEC-099's measured pinning is a
  commensurability-regime number, and the extrapolation ELEC-099
  itself labelled conditional is now shown NOT to hold at the next
  three accessible sizes.

## v1 -- ELEC-099 reproduced exactly
Six-axis energies 23.3572 ... 24.7365, K-projection amplitude -5.2273,
R^2 0.7098, mean E 24.9464, fraction 0.2095, floor 3.152e-2, signal/
floor 165.8 (byte-identical rerun).

## Q3 -- the s-ladder (protocol verbatim; L = 8, 11, 16, 21; npts = 3L;
## six axes, 250-step full relaxation, three-seed floor at each s)
  s     amp      fraction   line s^-3/2   seed floor   R^2   reading
  1.5  -5.2273   0.2095     0.2095        0.0000       0.71  (anchor)
  2.0  +0.8553   0.0295     0.1361        0.0022       0.03  below line
  3.0  -8.3608   0.2733     0.0741        0.0000       0.68  ABOVE line
  4.0  +2.5596   0.0669     0.0481        0.0304       0.08  on line (large floor)
The amplitude alternates in sign; R^2 on the pre-fixed harmonic is
0.03 and 0.08 at s = 2 and 4 (no cubic-harmonic structure) and ~0.7 at
s = 1.5 and 3. The log-log slope of the fraction (display only) is
-0.19 against the fixed law -1.50. The pattern correlates with the
inclusion endpoints' registration against the half-integer strand
planes (on-strand at s = 1.5, 2, 4; between strands at s = 3), i.e. the
signal at accessible s is a commensurability effect of the prolate
proxy on the mesh, not an asymptotic pinning law. ELEC-099's own
conditionality ("s = 1.5 is inside the pre-asymptotic regime") is
therefore not a caveat but the whole story at accessible sizes.

## Consequences (drafts; the author grants)
- ELEC-099 rider: "AXIS-MEANING Q3: on the same engine and protocol
  the anisotropy fraction at s = 2, 3, 4 is 0.03, 0.27, 0.07 with
  sign-alternating amplitude and R^2 0.03-0.68; the s^(-3/2)
  extrapolation is not exhibited; the 0.21 at s = 1.5 is a
  commensurability-regime number. Any predicted splitting for the
  physical electron is UNSUPPORTED by this instrument."
- ELEC-096 rider: the scaling law remains the registered fixed form
  by symmetry; its exhibition on the engine is now negative at
  accessible s (C_pin not extractable, ELEC-097, stands and is
  sharpened).
- ELEC-091's three readings stay open; the discriminating step is no
  longer a laboratory bound but an instrument question: an engine in
  which the inclusion is not a 25-point line on a half-integer mesh
  (a smooth proxy, or the registered core itself), so that a scaling
  regime can be reached. Named as the next-order; its own charter.
- Q2 (the coupling sweep) is still worth running as reading; deferred.

## Process
Ladder rungs and the s^(-3/2) line fixed before any point existed; box
scaling recorded as a pre-data amendment; every rung's fraction read
against the line and its own floor, fit-free. One session.
