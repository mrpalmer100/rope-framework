# QGATE-015 — Born-relaxation robustness over mode count: bars locked before data

Date locked: 2026-07-29

## Question
Does the QGATE-014 relaxation result persist as the number of modes changes, and is stronger relaxation associated with richer mode mixing rather than numerical integration alone?

## Frozen protocol
- 2-D unit hard-wall box and de Broglie guidance law used in QGATE-014.
- Deliberately nonequilibrium initial ensemble sampled from the ground-state density.
- Nested, energy-ordered excited-mode sets with M = 1, 2, 4, 8, 16, 32, 64; the ground mode (1,1) is excluded from the guiding superpositions.
- Three predeclared coefficient seeds: 17, 29, 43.
- For each seed, one 64-element complex Gaussian coefficient pool is generated; each M run uses the first M coefficients, renormalized. This makes the sweep nested rather than independently cherry-picked.
- 1,500 trajectories, 800 midpoint steps, total time 4.0, 14 x 14 coarse cells.
- Deterministic 8 x 8 midpoint quadrature for the Born target.
- Reflective hard-wall handling and the same velocity limiter as QGATE-014.

## Pre-committed bars
1. **One-mode control:** median absolute fractional change in H is below 15%.
2. **High-mode robustness:** for M = 16, 32, and 64, the median H reduction exceeds 50%.
3. **Metric agreement at high mode count:** for M = 16, 32, and 64, the median L1 reduction is at least 50%.
4. **Broad robustness:** at least four of the six multimode counts (2–64) have median H reduction above 50%.
5. **Directional scaling:** Spearman rank correlation between log2(M) and median H reduction over M = 2–64 is positive (> 0).

## Interpretation locked in advance
- Passing all bars supports robustness across mode count, not universal Born attraction.
- Failure of the directional bar with high-mode bars passing means relaxation is robust but not monotonic in raw mode number; flow structure, not count alone, is then the likely control variable.
- Failure of high-mode bars weakens QGATE-014 to a state-specific existence result.
- No bars will be altered after inspecting results.

## Disclosed numerical qualification
The first fixed-resolution run at 800 steps failed the M=64 bars: median H change was -10.3% and median L1 reduction was 16.8%. This was not hidden or overwritten. The highest-mode set raises the maximum box energy index from 26 at M=16 to 128 at M=64, making the fixed timestep an unequal numerical test.

A timestep diagnostic was therefore run before registration. At 1,200 steps, every M=64 seed showed strong relaxation; the median H reduction was 68.3% and median L1 reduction was 56.6%. The final registered campaign uses 1,200 steps uniformly for every mode count. The original 800-step failure remains part of the audit trail and establishes that high-mode claims require timestep convergence.
