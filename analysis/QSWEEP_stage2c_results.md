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

## THE CONTROL PROFILE (q = 5/3, the flat branch) -- E-NULL

Chartered as the optional second march and run under the
IDENTICAL instrument, ds, budget, gates and statistic. Twelve
gated triples; rates reproduce the FND-147 registered q = 5/3
profile point-by-point.

  ---------------- q = 4/3 (collapsing) ----------------  |  ---------------- q = 5/3 (control) ------------------
  A2        dA2/ds     V_pt      f_dir      |  A2        dA2/ds     V_pt      f_dir
  0.004721  5.806e-04  0.00471  0.1101   |  0.004721  5.789e-04  0.00442  0.0987
  0.004767  5.672e-04  0.00466  0.1125   |  0.004767  5.691e-04  0.00437  0.0989
  0.004812  5.555e-04  0.00477  0.1177   |  0.004812  5.670e-04  0.00437  0.0991
  0.004856  5.495e-04  0.00502  0.1296   |  0.004858  5.649e-04  0.00438  0.0993
  0.004899  5.328e-04  0.00558  0.1586   |  0.004903  5.628e-04  0.00438  0.0994
  0.004940  4.808e-04  0.00676  0.2264   |  0.004948  5.608e-04  0.00438  0.0996
  0.004975  3.890e-04  0.00830  0.3309   |  0.004993  5.588e-04  0.00439  0.0998
  0.005001  2.707e-04  0.00923  0.4166   |  0.005037  5.569e-04  0.00439  0.1000
  0.005019  1.857e-04  0.00952  0.4584   |  0.005082  5.550e-04  0.00440  0.1003
  0.005032  1.404e-04  0.00961  0.4755   |  0.005126  5.532e-04  0.00440  0.1005
  0.005042  1.046e-04  0.00968  0.4841   |  0.005170  5.515e-04  0.00441  0.1007
  0.005050  8.308e-05  0.00971  0.4882   |  0.005214  5.497e-04  0.00441  0.1009

VERDICT ON THE CONTROL: ** E-NULL ** (as the mechanism requires)

  statistic         line      q = 4/3        q = 5/3
  r(logV, -logRate) >= 0.8    0.870 FIRED    0.227 NULL
  f_dir rise        >= +0.15  +0.378 FIRED   +0.002 NULL
  V_pt change       --        +106 percent   -0.2 percent
  rate change       --        -86 percent    -5 percent

At MATCHED amplitude A2 ~ 0.00494 (the collapsing branch's cliff
step, -9.8 percent): q = 4/3 had V_pt 0.00676 and f_dir 0.226
(+0.116 from its own baseline); q = 5/3 had V_pt 0.00438 and
f_dir 0.0996 (+0.0009). Same instrument, same step size, same
budget, same amplitude: a factor of ~130 in sector rotation.

WHAT THE NULL EXCLUDES (its whole purpose): the boring readings of
FND-152. Arc steps do NOT accumulate winding of their own accord;
the arclength normalization does NOT drift with A2; the
instrument has no systematic that manufactures sector rotation.
The co-movement is pinned to the COLLAPSE, not to marching. Read
with FND-150/151/152, the S1-SPLIT selectivity now reads:
THE COLLAPSING CELL DEMANDS WINDING; THE FLAT CELL DOES NOT.

WHAT THE NULL DOES NOT SETTLE (stated plainly): WHY the q = 4/3
cell demands winding where q = 5/3 does not. That is the next
question, and it needs its own charter; nothing here answers it.

## STANDING

The charter's own words: E-LEDGER lifts nothing by itself; it
completes, with FND-150/151, the evidence set the author may
weigh against the FND-147 interpretive freeze. The q = 5/3 control
COMPLETED and returned the required E-NULL (section above),
registered as FND-153. Draft registration:
analysis/QSWEEP_stage2c_draft_registration.md -- GRANTED by the
author 2026-08-28 and registered as FND-152.
