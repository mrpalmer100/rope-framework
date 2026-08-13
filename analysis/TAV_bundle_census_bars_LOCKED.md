# COMMISSION TAV -- THE BUNDLE CENSUS: BARS, LOCKED BEFORE COMPUTING

Locked 2026-08-12, before any number is computed. Successor acquisition
named by FND-076: is the tube constituent (ELEC-050's lattice band
w_c in [0.0395, 0.0565] fm) a bundle of n_b vacuum-mesh strands
(w_vac = 0.6272 a at the two live floor readings, FND-040)?

## Scope fence

The census uses GEOMETRY AND COUNTS ONLY. The T0 chains (K_ME
calibration vs additivity; ELEC-053's fork; the NUCQ-002 coincidence
flag) are OUT OF SCOPE: no cell below requires resolving them, and any
argument that does is refused. This keeps the census fork-free.

## Registered inputs, closed at lock

- w_c band [0.0395, 0.0565] fm (ELEC-050 B2, tube sector, survives
  FND-076).
- w_vac = 0.6272 a at a = 1.63e-17 m (kappa 50) and 0.953e-17 m
  (kappa 250) -- the only live readings post-SHIN.
- f_c = 0.309 (FND-MATTER-038, measured percolation coverage).
- n_t = f_c (D/w_c)^2 (QGATE-004's registered constituent count;
  lattice D = 2R, R in [0.35, 0.5] fm).
- n_struct = 3 pi (R/a)^2 (NUCQ-003, non-circular), with the 3 read per
  FND-MATTER-059-hist as a PER-DIRECTION family partition, so the
  axial-family share is n_ax = pi (R/a)^2.
- Solidity criterion: bundle solid iff internal gap <= 1.5 sigma,
  gap = w_vac (1/sqrt(phi) - 1), sigma = w_vac (FND-STRAND-004,
  QGATE-004's usage).

## The three censuses

B1 GEOMETRY: n_b = phi (w_c/w_vac)^2. Packing fraction phi enumerated,
   BOTH evaluated, neither selected by outcome:
   phi_A = f_c = 0.309 (the registered internal-packing usage,
   QGATE-004's own convention) and phi_B = 0.9069 (hexagonal close
   packing, the geometric ceiling for a SOLID bundle). Deliverable:
   integer n_b windows per (floor x phi) cell; non-empty windows with
   n_b >= 2 are a PASS (weak, and said so -- n_b is otherwise free).
B2 SOLIDITY: the gap criterion at each phi. A bundle read by the
   lattice as a width-w_c object must sit on the solid side.
B3 COUNT CONFRONTATION, the census's teeth: the hierarchy demands
   n_count = n_t x n_b = f_c phi (D/w_vac)^2 vacuum strands in the
   tube; the registered structural count supplies n_struct (all-family)
   or n_ax (axial share). FOUR CELLS, closed at lock:
   {all-family, axial} x {phi_A, phi_B}. Ratio reported per cell;
   within L1 (factor 3) is CONSISTENT.
   The PHYSICALLY-NATURAL cell is declared BEFORE computing: a solid
   bundle packs near the ceiling (phi_B), and constituents of an axial
   tube bundle axial strands (n_ax). This declaration is made at lock
   precisely so the natural cell cannot be chosen after the numbers.

## Guard disclosures (pre-lock, displayed so refusal is auditable)

G1: pre-lock scoping noticed that FND-068's coverage convention
    (pi w_vac^2 / (4 a^2) = f_c) may cancel f_c in the B3 ratio
    exactly, reducing it to 1/phi. If the computation confirms this,
    the FND-067 PRECEDENT APPLIES AND IS PRE-COMMITTED: a cancellation
    running through a shared registered convention is a
    CONSISTENCY-THAT-COULD-HAVE-FAILED, not independent evidence.
    The demotion is locked now, before the result exists.
G2: order-of-magnitude scoping of the windows was done pre-lock; the
    grammar below was written before the benchmark.

## Verdict grammar, pre-committed

- BUNDLE-CONSISTENT: B1 windows non-empty (integer n_b >= 2) at both
  floors for at least one phi; B2 passes; B3's declared natural cell
  within L1. Carries the G1 demotion if the cancellation confirms.
- BUNDLE-EXCLUDED: any of -- B1 empty at both phi; B2 fails at both
  phi; all four B3 cells beyond L1.
- BUNDLE-UNDERDETERMINED: anything else; spread on the face.
In no case does the census DETERMINE n_b: an independent n_b constraint
is a named acquisition regardless of verdict (candidate routes: the
registered super-additivity calibration point delta_fusion = +12.5
percent at kappa_rel = 2.25, PHI; the bundle-binding relation owed
under FND-050's N-universality grant).

## Adverse outcomes pre-authorized

All three verdicts registerable without rescue.

## Deliverables

benchmarks/foundations/tav_bundle_census.py;
analysis/TAV_bundle_census_results.md; claim via tools/add_claim.py;
annotations to FND-076, QGATE-004, ELEC-050, NUCQ-003, FND-066.
