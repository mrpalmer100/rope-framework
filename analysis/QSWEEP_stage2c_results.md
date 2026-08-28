# Q-SWEEP STAGE 2c -- RESULTS: E-LEDGER FIRED (r = 0.870)
# Executed 2026-08-27/28 under the locked charter (the docstring of
# benchmarks/foundations/qsweep_profile.py; statistic, lines, ds,
# and node treatment fixed before any number). State:
# analysis/qsweep_stage2c_ckpt.pkl (all 12 retained full states).
# The q = 5/3 control profile is chartered and IN PROGRESS at
# close of this document; its record appends here when complete.

## THE QUESTION

Does the winding velocity's rise quantitatively account for the
amplitude rate's fall along the collapsing branch -- is the
S1-SPLIT collapse the branch's arclength rotating from the
amplitude sector into the direction sector?

## VERDICT: ** E-LEDGER ** (all three locked conditions met)

  r = Pearson(log V_pt, -log dA2/ds) = 0.870   (line: >= 0.8)
  V_pt monotone through the collapse: one -1.1 percent tie at
    point 2 (allowance: ties within 2 percent), strictly rising
    thereafter                                  (line: monotone)
  f_dir rise start-to-end: 0.110 -> 0.488, +0.378
                                              (line: >= +0.15)

## THE PROFILE (12 gated triples, ds = 0.08, every point from a
## full-bar member; rates reproduce the FND-147 registered
## profile within 1 percent point-by-point -- the instrument
## credential)

  A2        dA2/ds     V_pt      f_dir
  0.004721  5.806e-4   0.00471   0.110
  0.004767  5.672e-4   0.00466   0.113
  0.004812  5.555e-4   0.00477   0.118
  0.004856  5.495e-4   0.00502   0.130
  0.004899  5.328e-4   0.00558   0.159
  0.004940  4.808e-4   0.00676   0.226   <- the -9.8 pct cliff
  0.004975  3.890e-4   0.00830   0.331
  0.005001  2.707e-4   0.00923   0.417
  0.005019  1.857e-4   0.00952   0.458
  0.005032  1.404e-4   0.00961   0.476
  0.005042  1.046e-4   0.00968   0.484   <- stage 1's last point
  0.005050  8.308e-5   0.00971   0.488   <- NEW deepest member

## THE MECHANISM, IN NUMBERS

Across the collapse the branch's per-step arclength allocation
rotated from 89 percent amplitude-sector / 11 percent winding to
51 / 49: the winding velocity DOUBLED (0.00471 -> 0.00971) in
lockstep with the rate's SEVENFOLD fall (5.806e-4 -> 8.308e-5),
correlation 0.870 over the full profile. TIMING: the winding's
acceleration PRECEDES the rate's break -- V_pt and f_dir moved
decisively at points 4-5 (A2 0.00486-0.00490) while the rate was
still in its gentle-wobble phase; the -9.8 percent cliff arrived
at point 6. The collapse is not the branch stopping; it is the
branch TURNING: its motion rotating out of the amplitude sector
into the direction sector, watched across twelve gated states.
Read with FND-150 (the winding field is load-bearing) and FND-151
(the coarse two-interval signature), the S1-SPLIT
rationalization-selectivity now has a measured mechanism:
CELL-DEPENDENT WINDING DEMAND.

## BONUS: THE MARCH OUTLIVED ITS PREDECESSOR

The retention pipeline gated a member at A2 = 0.005050 with rate
8.308e-5 -- past the asymptotic squeeze where the stage-1 march
closed (best full-bar 0.005042). The measured collapse factor
within the same span extends to 7.0x (nearest-point pairing,
target still unreached; the FND-147 registered figure of 5.31x
stands as registered).

## INSTRUMENT RECORD

- Checkpoint unification (the gn_lean round-persistence path and
  the driver store were split across two files; the first launch
  clobbered the stage-1 /tmp record -- restored from the durable
  analysis/ export, which existed precisely because of the
  standing close-out rule; annotated in the driver).
- Cadence: 4-8 feed cycles per point, lengthening through the
  collapse exactly on the stage-1 schedule.

## STANDING

The charter's own words: E-LEDGER lifts nothing by itself; it
completes, with FND-150/151, the evidence set the author may
weigh against the FND-147 interpretive freeze. The q = 5/3
control (flat branch: V_pt and f_dir should NOT move) is in
progress; its null or surprise appends here. Draft registration:
analysis/QSWEEP_stage2c_draft_registration.md -- GRANTED by the
author 2026-08-28 and registered as FND-152.
