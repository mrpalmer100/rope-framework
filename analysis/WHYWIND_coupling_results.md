# WHY-WINDING BRICK 2 -- RESULTS: F-INSTRUMENT (statistic annihilated
# by branch-tangent nullity; no physics verdict borne; fault kept)
# Executed 2026-08-28 under analysis/WHYWIND_coupling_bars_LOCKED.md.
# Benchmark: benchmarks/foundations/whywind_coupling.py.

## VERDICT: ** F-INSTRUMENT ** (the locked verdict lines are recorded
## as FAIL/FAIL/FAIL mechanically, but the run is closed F-INSTRUMENT:
## the statistic is structurally incapable of bearing ANY verdict, so
## the FAILs are not evidence against the selection rule.)

## WHAT HAPPENED
All kappa values -- firing lines, 1:1 routes, AND both off-resonant
controls, on BOTH cells -- returned at the FD noise floor (~1e-8
after normalization). Diagnosis, verified mechanically before this
document:
  1. Every tangent's endpoints are full-bar MEMBERS: solutions of
     their own pinned systems (residual norms 5.1e-6 / 1.9e-6).
  2. The residual at a member's neighbor under the member's pin is
     PURELY THE PIN ROW: ||F(x_next; pin_x)|| = 3.851e-5 against the
     pin-row prediction dA2 = 3.847e-5. Identical.
  3. Therefore J t = (pin row) x dA2/||dx|| + second-order curvature
     noise, and every field-sector probe is EXACTLY orthogonal to the
     pin row. The inner products measure curvature noise: ~1e-9
     against probe responses of norm ~6.
The statistic as locked measures zero for any hypothesis. The fault
is a CHARTER DESIGN OVERSIGHT (the desk's, recorded as such): the
coupling was built around the branch tangent, which lies in the
kernel of the linearization restricted to the solution family.

## INSTRUMENT LEDGER (this brick)
- State/meas alignment: profile point i is the arc-pair midpoint of
  states[i+1], states[i+2] (waypoints lead the array); verified
  against registered A2 before the tangent map was patched.
- The credential (states load and gate) PASSED and stands: the
  retained states are sound; only the statistic failed.

## CANDIDATE AMENDED STATISTICS (recorded for the author; none
## chartered, none computed -- no number toward any of these exists)
  (a) MODE-RESOLVED SECTOR ROTATION: kappa = |<v(n,m; pt), t>| --
      the state-space content of the branch tangent itself on the
      resonant winding pattern. Directly extends FND-152's f_dir
      (which is the ALL-mode pt share) to per-mode resolution; asks
      WHICH winding pattern the collapsing branch rotates into.
      Cheap (inner products only, no FD). Selection-rule prediction:
      the 4/3 tangent's pt content concentrates onto (n=2, m=6)
      through the collapse; the 5/3 tangent's shows no concentration
      onto its 1:1 patterns.
  (b) TRUE PERTURBATION MATRIX ELEMENT: <v(n,m; pt), J u> with u a
      locked amplitude-sector pattern of the branch's primary
      content -- the operator's mixing of amplitude motion into the
      resonant winding mode. FD cost as brick 2; measures the
      OPERATOR, not the march.
  (c) RESONANT DENOMINATOR: smallest singular value of J restricted
      to the resonant mode's neighborhood along the branch --
      heaviest, most direct "the mode goes soft" measurement.
Options (a) and (b) answer different questions ((a): what the branch
DOES; (b): what the operator PERMITS); (a) is the closest kin to the
registered FND-150..153 evidence chain.

## STANDING
Brick 2 as chartered: CLOSED, F-INSTRUMENT. The j = n selection rule
remains UNTESTED (not weakened: the FAILs carry no evidential
weight). The brick-1 RES-OPEN registration and the committed q = 5/4
flat prediction are UNTOUCHED. Amended charter awaits the author's
choice of statistic. Grants reserved to the author. Failures kept.
