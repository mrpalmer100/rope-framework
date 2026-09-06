# COMMISSION FINE-GATE -- RESULTS (2026-09-05)
Executed under analysis/FINE_GATE_charter_LOCKED.md (+A1 from PEV-IDENT).
Legs 0-4: analysis/fine_gate/ (control logs, leg4_leg5.log). Table:
analysis/FINE_GATE_provenance_table.md (durable). Targets loaded in
Leg 5 only.

## VERDICTS (locked grammar)
  Q1  ** GATE-CLEAN-CEILING **
  Q2  ** GATE-UNDERDETERMINED **
  Q3  ** RAD-EXCLUDED **  (run as a BOUND per D5; excluded across the
      entire admissible interval, and for every coarse length as well)

## Leg 0 -- controls (all pass)
v1 LEAD-RAD kernel re-run byte-identically: Delta(100) = 0.582669,
   Delta(30000) = 6.996994, subtracted-sum exponent 0.281, the
   reactive/radiative ratio -> -sqrt3 (worklog's -1.732 at m = 60).
v2 Chain: D_E = 1.1051029 at five (r_min, tol) settings (seven-digit
   agreement), x* = e^(pi^2) = 19333.7; R* = x* in solver units.
v3 Table completeness against ROPE_PARAMETERS section 6: complete.
v4 Clean room: no target string in any Leg 1-4 file (grep-verified).

## Leg 1 -- Q1 (the table)
No alpha-clean fine VALUE exists; the alpha-clean fine CEILING is a_f
(with p, R_1, R_2, r_s riding on it), suspended on the LHAASO anchor
and the unknown multiplier m. GATE-CLEAN-CEILING. Q3 licensed as a
bound (D5).

## Leg 2 -- Q2 (the inventory)
Relations with a_f as the sole unknown after the n_sub cancellation:
  1. frame-dragging amplitude: Lambda_nat(a_f) vs chi   -- chi remains
  2. rotation quantum: E_rot = 2 sqrt2 x E_ceiling(a_f) -- DEPENDENT on
     3 (PEV-IDENT identity; A1); not a separate equation
  3. photon ceiling: a_f <= h c/(4 m x 1.4 PeV)           -- m remains
  4. Casimir coefficient (F3, unrun)                       -- per-mode action remains
  5. LEAD-RAD A2 sum at M* = R*/r_core                    -- no other unknown given a
     certified r_core (Q3)
  6. n_sub packing relation                               -- n_sub remains
No pair shares a_f and no other unknown with both measured sides held:
GATE-UNDERDETERMINED. The single relation that would close the most
pairs: an independent m (any confirmed photon above the anchor fixes a
floor, not m) or the CASIMIR-PLATE per-mode action (CAS-PIN would pair
with 3). Recorded as the gate's equation ledger.

## Leg 3 -- licensing
GATE-CLEAN-CEILING -> RUN-CEILING (D5). Regulator r_core carried as a
symbol proportional to a_f; every registered length, fine or coarse,
satisfies r_core <= the chain solver's radial unit, so M* >= x* for all
of them, and M* = x* (a / r_core) for the fine ceilings.

## Leg 4 -- w2(M*) on the byte-identical kernel (alpha out of the room)
  r_core = solver unit (coarse floor)   M* = 1.93e4   w2 = 5.93
  r_core = a_f,ceil (m = 1)             M* = 5.24e9   w2 ~ 208 (M^0.281 law)
  r_core = r_s bound = 0.1874 a_f,ceil  M* = 2.80e10  w2 ~ 333
  Any m > 1 lowers a_f,ceil and RAISES M* and w2. Across the admissible
  interval a_f in (0, a_f,ceil], w2 is monotone increasing in 1/a_f and
  its MINIMUM over every registered regulator is 5.93 (the coarse floor).
  w1 (energy side): NOT FORMABLE -- its source-to-medium normalization is
  unregistered (LEAD-RAD's A3 caveat); reported per D4; P2 confronted
  alone at LEAD-RAD's own "derived P2 with P1 pending" status.

## Leg 5 -- targets loaded once
  P2 target: the Schwinger coefficient w2 = 1/(2 pi) = 0.1592.
  Coarse floor:    w2/target =   37x   over
  Fine ceiling:    w2/target = 1307x   over
  r_s bound:       w2/target = 2092x   over
  The target is crossed by the exact sum at M* ~ 14.7 (Delta(14) =
  0.1621, Delta(13) = 0.1529): the regulator that lands P2 would have to
  be ~R*/15 -- a "core" one fifteenth of the orbit itself, more than
  three orders of magnitude larger than the largest registered length.
  No a_f in the admissible interval lands P2; P1 cannot be formed.

  ** RAD-EXCLUDED **: the radiative back-reaction with any physical-
  length regulator the corpus registers -- fine or coarse, value or
  ceiling -- OVERSHOOTS the Schwinger coefficient by 37x to 2000x. The
  fence re-closes on the stronger footing the charter named: a computed
  exclusion, not an absence of regulator. The +178.8 ppm residual and the
  moment gap remain fenced as quantum-radiative; the mechanism "classical
  mode sum cut at a material length" is refuted as their source. Failed
  and kept.

## What this settles and what it names
- LEAD-RAD's go-decision is now OPENED AND CLOSED: the one number the
  fence re-opens at (w2 at M* = R*/r_core) is computed for every
  registered r_core, and none is within an order of magnitude of the
  landing. The fence holds by computation.
- The a_f gate stays underdetermined (Q2). The named next-order is the
  CASIMIR-PLATE per-mode action (F3): CAS-PIN would give the first
  registered pair closing on a_f.
- Not touched: the chain's 4 pi^3 prefactor, D_E, the SHIN grant, the
  M-point, LEAD-RAD's classical ladder.

## Process
Table frozen before the inventory; inventory before licensing; w2
formed with alpha out of the room; targets loaded once. One session
(the charter budgeted two). An arithmetic slip in the small-M scan
line ("between M* = 1 and 2") was corrected by the exact crossing scan
(M* ~ 14.7) before the verdict was written; the exclusion is unaffected
either way (both are >1000x below the registered floor M* = x*).
