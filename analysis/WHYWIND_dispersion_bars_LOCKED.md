# WHY-WINDING BRICK 1 -- DISPERSION LATTICE: BARS (LOCKED 2026-08-28)
# Authorized by the author 2026-08-28 ("yes lets derive om2(q) and the
# resonance condition from the linear operator on the composed state").
# Locked BEFORE any lattice, order, or distance is computed.

## THE QUESTION
WHY does the q = 4/3 cell demand winding where q = 5/3 does not
(FND-152/153)? Candidate mechanism under test: RESONANCE PROXIMITY --
the collapsing cells' om2 marches onto a commensurability line of the
linear operator; the flat cell's does not.

## HONESTY CLASS
NOT blind for the three run cells: their om2 profiles are registered
(FND-147, stage-1 results) and known to the desk. The analytic lattice
below is derived independently of those numbers, but the confrontation
is registered-vs-derived, not committed-vs-revealed. The BLIND element
is the fourth-cell prediction (section P), committed here before any
fourth-cell computation exists anywhere in the corpus.

## LOCKED DERIVATION (all from the charter operator, no new physics)
The stage-2 charter operator (truestate_stage2.py docstring), rotating
frame, phi = Om2 t:
    -Om1^2 w + 2i Om1 Om2 w_phi + Om2^2 w_phiphi = (T w_s)_s
At the linearization point T = TBAR = 1.5 (constant-T reference; the
solved T deviates by the registered 1-3 percent), a mode
w ~ exp(i n phi) exp(i k_m s), k_m = 2 pi m / LCELL, LCELL = N1 sqrt(3),
satisfies
    (Om1 + n Om2)^2 = TBAR k_m^2 = (m / N1)^2 Om1^2
using Om1 = K1 sqrt(TBAR), K1 = 2 pi / sqrt(3) (registered, q-blind).
RESONANCE LINES (locked): for integers n >= 1, m in Z,
    Om2(n, m) = Om1 (m/N1 - 1) / n,   kept iff Om2 > 0.
(The m sign convention covers both dispersion branches.)

## LOCKED ORDER FUNCTION
The branch's primary content on cell (N1, N2):
    C = { (+-1, +-N2),  (0, +-N1) }
((1, N2): the level-2 wave in the rotating frame; (0, N1): the level-1
tension/geometry modulation at the cell period.) The ORDER of lattice
point (n, m) is the minimal number of elements of C (with repetition)
summing to (n, m), computed by breadth-first search, capped at order 8
(uncapped points reported as >8). Lower order = stronger nonlinear
coupling route from the state's content to the resonant mode. The order
function is fixed by this definition; no per-cell tuning.

## LOCKED STATISTIC AND VERDICT LINES
For each run cell, at its deepest registered full-bar member:
    delta(n, m) = (om2_member - Om2(n, m)) / Om2(n, m)
and the APPROACH check: |delta| at the deepest member strictly smaller
than |delta| at member 1 (om2 marching toward the line).
Verdict RES-CONSISTENT fires iff ALL of:
  R1. q = 4/3 and q = 3/2: nearest line of order <= 5 has
      |delta| <= 0.02 at the deepest member, approach holds.
  R2. q = 5/3: every line of order <= 5 has |delta| >= 3x the largest
      collapser |delta| from R1, OR its nearest line (any distance)
      has order >= 2 above the collapsers' firing lines.
  R3. The firing lines of the two collapsers are DIFFERENT lattice
      points (the mechanism predicts cell-dependent lines, not one
      magic frequency).
Any miss: RES-OPEN (registered as such; no salvage clause).

## P: THE FOURTH-CELL PREDICTION SLOT (blind element)
Before computing the lattice, the desk commits: a fourth cell will be
NAMED in the results doc together with its PREDICTED verdict
(collapse / flat) derived from (a) the empirical om2(q) interpolation
through the three registered members at matched A2 and (b) the fourth
cell's own lattice under the locked order function. The prediction
registers BEFORE any fourth-cell march is chartered; the march (Opus 5
per the author's standing instruction) confronts it.

## REGISTERED INPUTS (copied from the corpus, not computed here)
  Om1 = K1 sqrt(TBAR) = 4.442883
  om2 registered members (stage-1 results):
    q = 4/3: 2.14842 (m1), 2.21540 (m2/deepest full-bar)
    q = 3/2: 3.20 -> 3.27 (registered march span)
    q = 5/3: 4.23408 (m1), 4.30871 (m2), 4.38221 (deepest, target reached)
Grants reserved to the author. Failures kept.
