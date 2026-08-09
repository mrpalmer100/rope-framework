# FND-MATTER-059 — the FND-017 directional reading is not a reading: the factor 3 is a Crofton theorem, and the lever lands at 1.44×

Date: 2026-08-09. Commission: MATTER058's named settler.
Benchmark: `benchmarks/foundations/matter059_directional_reading.py`.

## Contamination, disclosed first

058 required this question settled TARGET-BLIND, and this session is not
blind: it read the 058 record (target, gap, and which reading lands) before
running. Under 058's own logic, a session that knows the target cannot be
trusted to CHOOSE the reading. This session therefore does not choose. It
proves the choice does not exist: the displacement count is forced by a
theorem of convex geometry, verified numerically, and the consequence of
each outcome was pre-committed by the blind 058 session before this one
existed. The adjudication rests on (a) checkable geometry and (b) a decision
rule locked blind by a prior session — the only two things a contaminated
session is entitled to use.

## The question, restated as geometry

Does a displacing strand inclusion (radius r, dilute r ≪ a) exclude ambient
mode content from ONE strand family (its own channel; the a² face reading)
or from ALL THREE (the a²/3 share reading)?

## The theorem

For a family of parallel straight lines with length density ρ = 1/a², the
total line length excluded by a convex body of volume V is exactly ρV,
**independent of the family's direction** (Cauchy: the chord-length integral
over any transverse plane is the volume). For a cylinder of radius r and
length L, each of the three families loses exactly πr²L/a²:

- parallel family: full-length chords L over the disk πr² → πr²L/a²
- each transverse family: chords 2√(r²−y²) over (y,z) → πr²L/a²

Verified analytically (exact to quadrature precision) and by Monte Carlo
(2×10⁶ samples, agreement to 10⁻³). **The displacement is direction-blind by
theorem.** There is no convention to choose: the inclusion removes identical
strand length from every family, so the displaced mode content counts all
three directions. The reading resolves to a²/3 — not adopted, DERIVED.

## The confrontation (under 058's pre-committed rule)

| | |
|---|---|
| λ = 2 (polarizations, forced at 058) × 3 (directions, derived here) × π(r/a)² | 1.666e-5 |
| target (MATTER055) | 1.156e-5 |
| gap | **1.44×, derived OVER target** |
| bar (inherited) | 2.00× |

**INSIDE the bar.** Per 058's pre-committed consequence: the mechanism
becomes **the sector's first derived lever**. λ = 6π(r/a)² is parameter-free:
every factor forced (πr² geometry, 2 polarizations by the transverse band's
structure, 3 directions by the Crofton theorem). Calibration spend remains
ONE.

## What the sign of the miss says

The derived value sits 44% ABOVE the target — the construction now displaces
slightly too much rather than too little. The natural refinement class is
physical rather than conventional: the dilute-exclusion picture treats the
inclusion as removing medium entirely, while a strand deforms around a thin
inclusion rather than terminating on it, recovering part of the mode content
(a compliance correction, strictly reducing λ toward target). Named as the
refinement lead; NOT computed; NOT required for the grade.

## Grade and scope

Modeled → the mechanism is promoted at 058's pre-committed threshold with
this session's contamination on the face. The promotion survives if and only
if the Crofton argument survives independent scrutiny — it uses no corpus
input beyond straight strand families and a convex inclusion, so it is
checkable by anyone without reference to λ. If a future blind session
faults the geometry, the promotion reverts and 058's near-miss verdict
stands.

## Not claimed

An exact λ (the 1.44× residual is open, refinement lead named); any lepton
mass (PM-004 stands); any new parameter; any change to the FND-017 tension
relation itself (T₀ = Σa²/3 is untouched — what is settled is which area a
displacing inclusion sees, and the answer is: all of it, three times).
