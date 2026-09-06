# WHY-WINDING BRICK 1 -- RESULTS: RES-OPEN (partial structure found,
# flat-cell exclusion FAILED; failure kept)
# Executed 2026-08-28 under analysis/WHYWIND_dispersion_bars_LOCKED.md.
# Benchmark: benchmarks/foundations/whywind_dispersion.py (pure desk
# computation, seconds).

## VERDICT: ** RES-OPEN ** (R1 PASS, R3 PASS, R2 FAIL)

## WHAT THE LATTICE SAYS

Every resonance line near a measured branch is an INTEGER-HARMONIC
line: Om1 + n Om2 = j Om1 with j = m/N1 an integer, i.e. the resonant
wavenumber is always a harmonic of the LEVEL-1 mode. The measured
placements at the deepest registered members:

  cell    om2/Om1   nearest line          order  delta     approach
  q=4/3   0.4986    Om1/2  (n=2, m=6, j=2)  4    -0.27%    YES
  q=3/2   0.7360    3Om1/4 (n=4, m=8, j=4)  5    -1.87%    YES
  q=5/3   0.9863    Om1    (n=3, m=12, j=3) 4    -1.37%    YES

R1 PASSED: both collapsers sit within the 2 percent window of an
order-<=5 line and march toward it -- the q = 4/3 hit is striking
(om2 lands 0.27 percent off Om1/2 exactly where the collapse bites,
and Om1/2 is the SAME n = 1 cell-mode frequency FND-140 registered as
the inhabited resonant window on the 3/2 cell).
R3 PASSED: the firing lines are different lattice points, as a
cell-dependent mechanism requires.

R2 FAILED, and this is the finding: the flat cell sits 1.37 percent
from the 1:1 line Om2 = Om1 -- CLOSER than the collapsing 3/2 cell
sits to its line, at comparable coupling order, also approaching.
PROXIMITY ALONE CANNOT BE THE MECHANISM. If distance-to-line drove
winding demand, q = 5/3 would collapse too. It measurably does not
(FND-153: f_dir moved +0.0009 across the whole span).

## THE SHARPENED QUESTION (what RES-OPEN buys)

The discriminator is not WHERE the lines are but WHAT COUPLES to
them. All three branches live near integer-harmonic lines; only two
turn their arclength into winding. The refined hypothesis: the
resonant COUPLING COEFFICIENT (the matrix element of the linearized
operator between the branch state and the resonant mode) is large for
the collapsers' lines and suppressed -- possibly by an exact
selection rule -- for the flat cell's 1:1 line. Candidate selection
rules visible from the desk, none adjudicated here:
  (a) parity in n: the collapsers fire on even-n pairs (n=2, n=4);
      the flat cell's nearest reachable pairs at the 1:1 line are
      odd-n (n=3) or higher-order even (n=2, m=9: order 5, and m=9
      is NOT a level-1 harmonic multiple on N1=3... it is, j=3; the
      n=2 route exists at order 5) -- the parity bookkeeping needs
      the actual operator, not the BFS.
  (b) j - n structure: 4/3 fires on (j=2, n=2), 3/2 on (j=4, n=4)
      -- both j = n, the DEGENERATE co-rotating class
      Om1 + n Om2 = n Om1, i.e. Om2 = Om1 (1 - 1/n)... no: j = n
      gives Om2 = (n-1)/n Om1 = Om1/2, 3Om1/4 for n = 2, 4. The
      flat cell's 1:1 line requires j = n + 1 (j=3, n=2 or j=4,
      n=3): NO j = n line exists near om2(5/3) = 0.986 Om1, because
      j = n lines accumulate at Om1 FROM BELOW ((n-1)/n -> 1) and
      0.986 Om1 needs n ~ 70 (order astronomically high). THIS is a
      clean candidate law: WINDING DEMAND = PROXIMITY TO A j = n
      (SELF-DEGENERATE) LINE. It fires 4/3 (n=2), fires 3/2 (n=4),
      and acquits 5/3 (nearest j = n line of sane order is 5Om1/6
      at n=6, 18 percent away). Noted as the LEADING refinement;
      NOT granted; brick 2 must compute the matrix elements.

## P: THE FOURTH-CELL PREDICTION (committed per the locked slot)

Named cell: q = 5/4 (N1 = 4, N2 = 5). Empirical interpolation
om2 ~ 6.50 q - 6.46 (residuals < 2e-2 across the three registered
members) puts om2(5/4) ~ 1.664, which is 0.12 percent from the
j = n line 3Om1/8... check: (n=8? ) -- mechanically: nearest
order-<=5 line is (n=4, m=10, j=2.5)? No: N1=4, m=10 -> j = 2.5,
Om2 = 1.5 Om1 / 4 = 0.375 Om1 = 1.6661. j non-integer (half-integer
lines exist on N1=4 because level-1 harmonics sit at m = 4k; m=10
is NOT one) -- under refinement (b) this line is NOT j = n class.
The two hypotheses therefore SPLIT on this cell:
  - Naive proximity (RES-OPEN'd but not dead): om2 lands 0.12
    percent from an order-4 line -> predicts COLLAPSE.
  - Refinement (b) (j = n class only): the nearest j = n line to
    0.375 Om1 is Om1/2 (n=2) at +33 percent -> predicts FLAT.
Committed: the q = 5/4 column, when chartered and run (Opus 5 per
the author's standing instruction), ADJUDICATES between the two
readings. Prediction of record from the desk's leading refinement:
q = 5/4 marches FLAT. Registered here before any fourth-cell
computation exists in the corpus.

## STANDING

RES-OPEN registered; failure kept. Nothing granted. Proposed brick 2
(unchartered, awaiting the author): compute the resonant coupling
matrix elements directly -- project the linearized stage-1 operator
at the retained stage-2c members (12 per cell, in
analysis/qsweep_stage2c_ckpt.pkl) onto each cell's near lines and
measure numerator (coupling) against denominator (detuning); the
j = n selection rule either shows up in the numbers or dies there.
