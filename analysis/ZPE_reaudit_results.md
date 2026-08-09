# ZPE BAR RE-AUDIT -- RESULTS (2026-08-09)
# Both branches computed, nothing adopted. TWO CATCHES in the registered
# usage of the old bar, logged. Verdict flips named per consumer.

Bars: analysis/ZPE_reaudit_bars_LOCKED.md (locked first; held).
Script: benchmarks/foundations/zpe_reaudit_pipeline.py (MATTER041 code
path, constants unchanged; only the T0 band varies per branch).

## The bands
  OLD (25% reading):  s in [0, 2/3]      -> l_q width x1.73
  BRANCH A (open):    s in [0, 0.999)    -> l_q width x31.6 (UNBOUNDED
                       in principle; 0.999 is a display cap only)
  BRANCH B (056/057): s in [0.064,0.093] -> l_q width x1.016

## Consumer verdicts
C1 (l_q/a vs 1-100 window):
  OLD [33.4, 57.8] INSIDE. A [33.4, ~1055] EXITS ABOVE. B [34.5, 35.0]
  INSIDE, tight. UNIVERSAL EXIT CONDITION derived: the F-2SCALE
  reconciliation survives iff the zero-point share s < 0.889 -- the
  window verdict is robust to ANY share below 89%, a much weaker
  requirement than either old or new reading. Registered as the
  window's honest condition.
C2 (T0 anchors):
  Lattice/Sigma/rigidity were naked under OLD already (041 said so).
  FLIP under B: the R1 quantum-area anchor (factor 2.0, previously
  "inside ZPE bar") becomes a NAKED TENSION at slack x1.03.
C3 (l_q vs registered 1.39e-15 m, factor 2.40):
  CATCH #2: MATTER041 tagged this "inside ZPE bar" against a factor-3
  excusal applied in l_q-space -- but the bar's own mechanics (T0 in
  [t0/3, t0], l_q ~ T0^{-1/2}) give only sqrt(3) = 1.73 of l_q slack.
  The 2.40 was NEVER excused by the bar as registered; the tag used
  the wrong space. Naked under OLD-corrected and under B; excused
  only under A's unbounded band.
C4 (n_q vs snap band [1.1e-4, 4.6e-4]):
  BELOW under every branch (1.55x OLD/A, 1.65x B).
  CATCH #1: MATTER041's "recoverable within the same ZPE band"
  sentence is DIRECTIONALLY WRONG -- the bar moves T0 down only, so
  l_q up only, so n_q = k/l_q^2 DOWN only, away from the band it sits
  below. The miss was never recoverable by the bar; under B it
  hardens to a standing unexcused 1.65x miss.
C5 (4.6 blind-mass whisper): outside every branch's band (trivially
  inside A's). Stays whisper; no flip.
C6 (FND-029 nuclear import): verdict UNCHANGED at any width (the
  [0.019, 87] straddle absorbs even Branch A).
C7 (Commission E conditionality): under B the ZPE term drops out of
  the M-point error model almost entirely (x1.016), leaving the
  reopened-049 cube-root sensitivity as the DOMINANT and effectively
  sole term of E's conditionality note. Under A the note widens.

## The shape of the fork (equal volume, per bar)
BRANCH A is honest and useless: with the share unconstrained the bar
is unbounded, every tension is excusable, and the pipeline loses its
power to say no -- the corpus would be trading a mispriced band for
no band. Its one derived product is the C1 exit condition (s < 0.889).
BRANCH B is sharp and adverse: bands collapse ~1.02x, the window
answer tightens to l_q/a = 34.5-35.0, E's conditionality simplifies --
and the price is FOUR naked tensions (R1 anchor 2.0x, l_q 2.48x, n_q
1.65x below, plus the pre-existing lattice/Sigma/rigidity spread) that
the old bar had been absorbing, two of them absorbed INCORRECTLY even
under the old bar's own mechanics (the catches).

## Catches (the audit's independent product, branch-free)
1. The n_q "recoverable" sentence in FND-MATTER-041 is directionally
   impossible under the bar it cites. Face correction owed regardless
   of branch choice.
2. The l_q 2.40x excusal used factor-3 in the wrong space (l_q slack
   is sqrt of the T0 slack). Face correction owed regardless.
Both are the same error class: a band quoted where its square root
applies. Neither changes any headline (F-2SCALE survives; both were
coherence-table tags), but both must be corrected superseded-not-
erased.

## Registry deltas (draft, Mark's adoption)
- FND-MATTER-041 face: catches 1 and 2 corrected; coherence table
  re-tagged per the corrected slack; C1 exit condition (s < 0.889)
  added as the window's honest robustness statement.
- The ZPE bar's registered status: "2-3x" REVOKED as a priced width
  (its price dissolved with the 25%); replaced by the branch pair
  above pending the grant decision on MATTER056's prediction.
- If Branch B is granted: four naked tensions registered on their
  faces as open coherence items; E's conditionality note simplified.
- If no grant: Branch A's unboundedness registered; every downstream
  consumer carries "ZPE width undetermined" until a share constraint
  exists.
- Spend unchanged; nothing adopted in-session.
