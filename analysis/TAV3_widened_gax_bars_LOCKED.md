# COMMISSION TAV3 -- THE WIDENED G-AX SWEEP: BARS, LOCKED BEFORE COMPUTING

Locked 2026-08-13, before any number is computed. Tier: T4 TOP per
docs/STRATEGIC_TARGETS.md section D. Successor to TAV2 (FND-082) as
directed by its named next-order and sharpened by FND-094 into a
PRE-COMMITTED TWO-NUMBER DECIDER on GRANT-THRESHOLD's Chain A
purchase (FND-080). The verdict corners below are fixed at lock; no
corner may be renegotiated after numbers exist.

## The two questions (both settled or the sweep failed)

Q1 THE ASYMPTOTIC EXPONENT: does axial/web contact SETTLE at
   full-section scaling (p -> [0.85, 1.15]) once the sweep is wide
   enough for the edge-dominated transient TAV2 observed (monotone
   downward drift from p ~ 1.2) to relax?
Q2 THE SETTLED MULTIPLICITY: at what value does m_eff(n)/n plateau?
   TAV2's displayed figure was ~3-4 (hex ~4, f_c ~3) at the locked
   gaps. Chain A's inversion (m_b = n) requires ~1.

## Instrument, inherited VERBATIM from TAV2's lock (no retuning)

- Engine contact form: E_pair = Ac/(1 + (r/sigma)^4), Ac = 1,
  sigma = 0.12 (FND-STRAND-004 registered form, Phase 3 value).
- Geometry: G-AX ONLY. Two coaxial bundles, facing cross sections at
  end-plane gap equal to the internal gap; pairwise energy summed
  over facing constituent ends; end-to-end nearest distance for
  aligned pairs = pitch(gap). G-LAT is NOT re-run: TAV2's lateral
  exclusion is half-sweep stable and stands.
- Packings and gaps, locked at TAV's values: hex at g = 0.050 sigma,
  f_c at g = 0.799 sigma; centerline pitch = sigma + g (the
  r_s = sigma/2 contact-range radius convention, carried).
- Hex-spiral bundle construction identical to
  benchmarks/foundations/tav2_bundle_contact.py.

## The widened sweep, locked

- n = the full hex-centered sequence {7, 19, 37, 61, 91, 127, 169,
  217, 271, 331, 397, 469, 547}. This extends TAV2's top (91) by a
  factor 6 in n, chosen at lock as the widening; NO further
  extension by this commission regardless of outcome (the
  no-bar-shopping clause, second application).
- M1: E(n) per facing section, both packings.
- M2: m_eff(n) = E(n)/E_1, E_1 the single aligned end pair at the
  same gap (self-normalizing, as TAV2).
- M3 SETTLING CRITERION (the exponent): local exponent
  p_k = dlnE/dlnn on consecutive triples; SETTLED iff the last three
  local exponents agree within 0.05 AND the TAV2 half-sweep check
  (halves within 0.10) passes on the top half of the widened sweep.
  The reported p_inf is the mean of the last three local exponents.
- M4 SETTLING CRITERION (the multiplicity): r(n) = m_eff(n)/n;
  SETTLED iff the last three values agree within 10 percent
  (relative). The reported r_inf is the mean of the last three.
- Cross-packing agreement is REPORTED, not required; verdicts are
  per-packing with the hex cell (the pin's window (kappa250, hex))
  carrying the Chain A confrontation.

## The pre-committed verdict corners (from FND-094, fixed at lock)

At the hex cell, with both M3 and M4 SETTLED:

- CORNER 1 (CHAIN A SURVIVES): p_inf in [0.85, 1.15] AND
  r_inf in [0.5, 1.5]. Chain A's full-section conditional converts
  to a MEASURED geometry premise with the inversion's currency
  validated; the engine-level n_b readout {n : m_eff(n) in
  [63.0, 73.4]} is reported, conditional on GRANT-THRESHOLD.
- CORNER 2 (FULL-SECTION, WRONG CURRENCY): p_inf in [0.85, 1.15]
  AND r_inf outside [0.5, 1.5]. The pin inverts through the
  MEASURED multiplicity to n = [63.0/r_inf, 73.4/r_inf]; if that
  window misses every registered window, the tension is CONFIRMED
  AT SETTLED LEVEL and the grant's Chain A n_b purchase RETURNS TO
  ADJUDICATION under FND-080's armed return clause. Reported to the
  author; nothing retracted by this commission.
- CORNER 3 (NOT FULL-SECTION): p_inf outside [0.85, 1.15] settled.
  Chain A's geometry premise is CONVICTED at engine level (adverse
  outcome pre-authorized, as TAV2's bars already authorized);
  adjudication as in Corner 2.
- CORNER 4 (UNSTABLE-PERSISTENT): M3 or M4 fails its settling
  criterion even at n = 547. Registered Failed-and-kept; NO further
  widening by this commission; the question passes to the author's
  desk as an instrument-limit finding.

The classification bands [0.85, 1.15] / [0.40, 0.60] / [0.61, 0.84]
are TAV2's, final, no re-binning.

## Guard disclosures

G1: the targets are all in context (the pin [63.0, 73.4], the windows
    [5, 9] / [14, 27] / [40, 81] / [47, 198], TAV2's displayed ~3-4n
    and n ~ 16-24 inversion, the survival corner (p -> 1, r -> 1)).
    Protection: zero free numbers anywhere in the instrument, the
    sweep and all criteria fixed at lock, verdict corners
    pre-committed with the adverse corners pre-authorized.
G2: pre-lock scoping expectation disclosed: the pair form's r^-4
    tail makes m_eff ~ 3-4 per facing constituent plausible as a
    GEOMETRIC fact of the facing-disk kernel (each end sees several
    opposite ends within range), in which case Corner 2 is the
    likely landing. Disclosed so the landing cannot be presented as
    a surprise; the corners bind regardless.
G3: the FND-STRAND-004 standing caveat carries: engine parameters
    unscaled; every verdict is Modeled, about the contact MODEL's
    scaling class and multiplicity currency, not a direct physical
    n_b measurement. Resemblance is not identification; grants and
    adjudications are the author's.

## Deliverables

benchmarks/foundations/tav3_widened_gax_sweep.py;
analysis/TAV3_widened_gax_results.md; claim via tools/add_claim.py;
annotations to FND-094, FND-082, FND-080, FND-079; CHANGELOG;
HANDOFF refresh; verify_corpus --quick; re-zip; present_files.
