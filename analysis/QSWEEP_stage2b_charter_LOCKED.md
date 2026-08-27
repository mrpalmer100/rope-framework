# Q-SWEEP STAGE 2b CHARTER (LOCKED) -- PT-VELOCITY SIGNATURES
# Chartered 2026-08-26 at the author's word ("continue with the
# next brick") under the FND-150 consequence: the direction field
# cannot be frozen, so compare its EVOLUTION between cells. Bars
# locked BEFORE the measurement script runs.

## THE QUESTION

Do the collapsing cells and the flat cell move their winding
fields differently? Operationally: the pt-velocity
  V(interval) = RMS_over_nodes( delta pt ) / delta s
computed from SURVIVING gated states of the stage-1 record (no
new solves; this brick is a measurement of data in hand), where
delta s is the free-sector arclength between the states and
delta pt is taken modulo 2 pi per node.

## THE DATA (fixed in advance; all full-bar states)

Per branch (q = 4/3 and q = 5/3), the stage-1 checkpoint retains:
  (i)  member 1 (A2 = 0.0018792) and member 2 (A2 = 0.0046979):
       the RAMP interval, matched exactly across branches;
  (ii) the final arc pair of each rate march: the ANCHOR-REGION
       interval (q4/3 near A2 ~ 0.0050 where its rate had
       collapsed 5x; q5/3 near A2 ~ 0.0063 where its rate was
       flat).
Two intervals per branch. The stage-2 X3a optimum states are NOT
inputs (they are frozen-pt artifacts).

## PRE-REGISTERED COMPARISONS AND THE LINE

C-A (matched interval): V_ramp(4/3) vs V_ramp(5/3) over the
  IDENTICAL A2 interval. A ratio >= 2 either way is a signature;
  within [0.5, 2] is signature-absent on this interval.
C-B (behavioral interval): V_anchor / V_ramp within each branch.
  Pre-registered direction-field expectation: the COLLAPSING
  branch shows V_anchor/V_ramp elevated by >= 2 relative to the
  same ratio on the flat branch (the winding accelerating where
  the amplitude stalls). The DOUBLE RATIO
    Q = [V_anchor/V_ramp](4/3) / [V_anchor/V_ramp](5/3)
  is the statistic; Q >= 2 fires E-DIRECTION, Q <= 0.5 fires
  E-ANTI (winding decelerates where collapse lives), otherwise
  E-NULL on this data.
NOTE (honest scope): the anchor intervals sit at different A2 by
necessity of what survived; C-B is therefore a within-branch
normalized comparison, and the verdict language is "on this
data". A finer profile would need re-marching with state
retention (recorded as the follow-up, not chartered).

## NO-RESCUE

pt differences modulo 2 pi, node-uniform, no weighting, no
exclusion of any node class; delta s is the same free-sector norm
for every interval; the statistic and thresholds above may not be
revised after the numbers are seen.

## VERDICT FORMS

E-DIRECTION (Q >= 2) / E-ANTI (Q <= 0.5) / E-NULL (otherwise) /
E-DATA (surviving states insufficient or corrupt: report and
stop). None of these lifts the FND-147 interpretive freeze by
itself; E-DIRECTION or E-ANTI would justify chartering the full
re-march-with-retention experiment.
