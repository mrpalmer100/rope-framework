# COMMISSION TRAVERSE -- RESULTS (2026-08-18/19)

Executed under analysis/TRAVERSE_bars_LOCKED.md (locked before
computing; three pre-lock amendments recorded there). Benchmark:
benchmarks/foundations/traverse_steepened.py, checkpoint-driven.
Verdict prose written AFTER the run. Outcome, per the pre-registered
sheet: CHART/TAIL HALT -- failed-and-kept, with the halting control
named, the last accepted member registered, and two structural
measurements that change what FND-142's steepening IS.

## GATE CONTROLS (all PASS)

Control (0), representation equivalence: two registered FND-142
members re-solved in the tangent-sphere chart; Om2/gamma/A2 reproduced
to max rel dev 1.2e-12 (mid-branch) and 4.7e-9 (endpoint) against the
1e-6 bar, re-solved field RMS 3.1e-14 and 3.1e-11. One instrument
catch is recorded in the code: an implementation-added converted-
residual sub-bar (1e-7, NOT in the locked bars) halted on the endpoint
member; the converted residual (4.3e-7) is the seed's own stage-2
convergence level (6.1e-9) amplified ~50x by the chart map, and it is
now a printed diagnostic while the locked bar governs.

Control (i), level-1 recovery: theta constant to 8.4e-12, value
4.7e-7 from 0.955317, Om1 rel 4.9e-5 (the known discretization shift,
matching stage 2's record), max|T - 3/2| = 1.1e-6.

Control (vii), declared influence pattern: 0 of 25 probed columns
escape the dense-band pattern.

## FINDING 1 -- NO FOLD: THE BRANCH PASSES THROUGH THE FND-142
## ENDPOINT

The registered endpoint (gamma = 0.545, A2 = 0.0107697) is NOT a
terminus and NOT a turning point. Pseudo-arclength continuation in the
new chart produced bars-clean solutions beyond it:

    point            arc s      A2         gamma    Om2      min z'  RMS
    member 5 (s2)      --   0.0103290   0.55800  3.50902  +0.4780  6.4e-09
    member 6 (s2)      --   0.0105409   0.55200  3.47034  +0.4275  1.9e-09
    member 7 = seed   0.000  0.0107697   0.54500  3.43726  +0.3623  3.1e-11
    arc +0.005        0.005  0.0107698   0.54499  3.43722  +0.3622  2.0e-09
    accepted step 0   0.020  0.0107700   0.54495  3.43708  +0.3620  7.6e-09
    (display only)    0.032  0.0107703   0.54492  3.43697  +0.3618  1.2e-08

Every trend continues smoothly through the old wall. The stage-2
obstruction was therefore the CLOSURE, as the bars' diagnosis stated:
the |w_s|^2 + z'^2 - 1 constraint row losing rank as its 2z' factor
shrinks. Remove the row (constraint identically satisfied on the
tangent sphere) and the branch simply continues. A false intermediate
reading during the run -- an apparent A2 decrease suggesting a fold at
the endpoint -- was a rounding artifact of 5-digit displays against a
mistyped reference and is retracted here by the 7-digit table; the
uncorrected-then-corrected sequence is preserved in the session record.

## FINDING 2 -- THE STEEPENING IS AN ASYMPTOTIC REGIME OF THE A2
## FUNCTIONAL

Measured on the continued branch: dA2/ds = +1.5e-5 per unit X-space
arclength (vs 6.5e-5 averaged over the preceding member interval -- a
~3x decay), while dgamma/ds = -2.5e-3 and the field configuration
reorganizes at full speed (the member-6-to-7 interval alone is 3.56
X-space units for 2.3e-4 of A2). The branch is not turning; its
|c2|-growth is COLLAPSING while the state marches. Every stage-2
parametrization (A2 pin, gamma pin) went near-vertical for this one
reason. Whether A2 asymptotes below R2 = 0.09396 or re-accelerates
after the reorganization completes is UNDECIDED at this instrument's
resolution -- and that question is now THE question, because if A2
asymptotes, the registered R2 pin is unreachable on this family at
q = 3/2 and the pin set itself is what the desk must reconsider
(FND-142's competing job, the resonant root / de-rationalized q,
gains standing from this side too).

## THE HALT -- RESOLUTION EXHAUSTION, NAMED CONTROL (v)

The halting control is (v), closure residuals, corroborated by the
printed ws-Nyquist tail: from 1.2e-8 (seed) to 1.8e-6 (+0.005) to
8.0e-6 (+0.020) to 1.3e-5 (+0.032). The reconstructed chart projects
mean and s-Nyquist slope content by construction; its growth by three
orders over 0.03 arc units means the reorganizing state is developing
grid-scale slope structure the 64 x 24 grid cannot carry. The same
invisible content acts as an effective inconsistency in the field
rows: solves beyond step 0 stall at 1.2-1.6e-8, immediately above the
1e-8 acceptance bar, with trf terminating at first-order optimality --
a floor, not a slowdown. This is NOT a chart failure (min sin theta =
0.675, far from the pole bar of 0.05; min z' = +0.362, far from the
old degeneracy): the chart is healthy and the GRID is spent. The last
accepted member is step 0 (arc +0.020, RMS 7.57e-9); the +0.032
iterate is registered DISPLAY ONLY.

Sigma_wave is NOT re-priced. The FND-139 rider STANDS. FND-142's
PIN-UNREACHED verdict stands and is sharpened, not superseded: the pin
is unreached because the family's |c2| growth collapses in the
steepened regime, not because the path or the chart was wrong.

## INSTRUMENT RECORD (for the successor commission)

1. The tangent-sphere chart + FD-consistent reconstruction is PROVEN
   at control-(0) grade and should be inherited as-is.
2. Pin weighting: stage 2's PW = N destroys Krylov (lsmr) conditioning
   in this chart; PW = 50 with unweighted reporting restores it. The
   lsmr inner iteration must NOT be capped (a 200-300 cap produced
   fake stalls at 2e-7).
3. Arc-step geometry through the reorganization: hyperplanes at
   ds >= 0.22 MISS the branch (nonzero local minimum, residual scaling
   with overshoot); ds <= 0.02 converges. Growth cap 0.08.
4. The successor needs resolution from the start -- 96 x 36 minimum,
   ideally with the tail monitored as a promotion trigger -- and
   should expect ~2 orders more arc length before A2 moves decisively.
   On this container that is out of session scope; on the author's CI
   it is an overnight run.

## FINAL LEG -- COMPARISON (clean room opens here)

The registered Sigma_wave box [3.222, 4.313], the level-1-exact 2.598,
and FND-142's price display 2.62 are unchanged by this run: no
solution at R2 exists to price, and no display re-pricing is offered
from sub-R2 members (their kb = 0 corner prices are within noise of
FND-142's display and add nothing). The two-frequency TRUE-STATE
remains real, continued, and now measurably HARDER to push in
amplitude than any prior instrument could see.

## PROPOSED CLAIM TEXT (author's grant required; not registered)

FND-143 (Modeled): THE ALIGNED BRANCH PASSES THROUGH THE FND-142
ENDPOINT -- NO FOLD; THE STEEPENING IS AN ASYMPTOTIC REGIME OF THE
AMPLITUDE FUNCTIONAL. In a tangent-sphere chart with the
inextensibility constraint identically satisfied (control-(0)
equivalence to the stage-2 instrument at 1e-6 grade or better),
pseudo-arclength continuation produces converged members beyond the
registered endpoint (best RMS 2.0e-9) with all state trends smooth,
and measures dA2/ds = +1.5e-5, decaying ~3x per member interval, while
the configuration reorganizes at ~10^4 x that rate in X-space. The run
halts by control (v) -- closure/Nyquist tail growth of three orders
over 0.03 arc units: resolution exhaustion of the 64 x 24 grid, chart
healthy. R2 remains unreached; Sigma_wave is not re-priced; the
FND-139 rider stands. Benchmark: traverse_steepened.py; bars:
TRAVERSE_bars_LOCKED.md.
