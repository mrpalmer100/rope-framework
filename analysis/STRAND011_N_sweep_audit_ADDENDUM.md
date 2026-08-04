# FND-STRAND-011 — AUDIT ADDENDUM, locked before the replay

Date: 2026-08-03, same session, written after data collection and BEFORE the
audit replay. Two facts triggered this addendum, both owned on its face:

1. CENSORING: N = 24 batch 2 carries one censored run (1/64), invalidating
   the point under the locked clause -> NO-VERDICT at the locked protocol.
   Diagnosis: the tmax = 12000 window was priced off STRAND-010's N = 48
   statistics; any decreasing-in-N scaling makes N = 24 the slowest box, and
   the window was not re-priced for it. The STRAND-010 lesson (price the
   budget to the estimator) was applied to seeds but not to the WINDOW —
   logged as this session's design miss.

2. GRAMMAR GAP, disclosed at full volume: the pairwise 48 -> 96 diagnostic
   slope (-1.545) was seen before this addendum was written, and it falls
   OUTSIDE every pre-committed outcome (intensive |s| <= 0.3; extensive
   [-1.3, -0.7]; intermediate (-0.7, -0.3)). The locked bars did not
   anticipate super-extensive scaling. Because this addendum is written
   INFORMED, no outcome of this session can be PROMOTED; the ceiling is
   REGISTERED-AS-MEASURED, with any promotion requiring a fresh session
   under blind bars (the 009 -> 010 pattern, invoked in advance).

## The replay (audit action)

Window re-locked at tmax = 24000 units (1.2M steps) for the censored batch
only (N = 24, seed0 = 22, S = 32) — a uniform window extension cannot alter
any already-recorded finite escape, and the trajectory is a deterministic
replay of the locked seed (bit-identical through the original window), so
this completes the censored run rather than imputing it. Censor-free batches
are untouched.

- If the straggler escapes within 24000: the N = 24 point is completed and
  the three-point slope is computed and REGISTERED AS MEASURED (no
  promotion), classified against the full grammar including the added
  outcome: SUPER-EXTENSIVE, s < -1.3 — named suspect, stated now: a
  finite-size barrier effect at the smallest box (ring-periodic kink-pair
  interaction raising the effective barrier at N = 24), which would steepen
  the 24 -> 48 leg beyond pure rate-additivity.
- If it does not escape by 24000: the run is reported as a genuine outlier,
  the N = 24 point stays invalid, and the session registers the two-point
  diagnostic only.

## What survives regardless

The 48 -> 96 leg is censor-free at full budget on both points and its slope
(-1.55) already excludes the INTENSIVE grammar at many sigma: whatever the
final classification, nu is NOT box-free, and STRAND-010's promotion
acquires a scope note (the identification as promoted is the N = 48
statement). That consequence is registrable from the clean data alone.

## Next-order pre-named

A four-point sweep (N = 24..192) under blind bars with the window priced
per-N and the growth/nucleation deconvolution (the local-first-passage
diagnostic recorded tonight becomes an instrument there).
