# FND-STRAND-011 — the N-sweep: results

Bars: analysis/STRAND011_N_sweep_bars_LOCKED.md. Audit addendum (written
after data collection, before the replay, informed status owned on its
face): analysis/STRAND011_N_sweep_audit_ADDENDUM.md. Dataset archived:
analysis/STRAND011_N_sweep_data.json (new points; the N = 48 point is the
STRAND-010 archive, reused as pre-committed).

## Locked-protocol outcome first, unsoftened

N = 24 carried one censored run (1/64) at the locked window ->
NO-VERDICT at the locked protocol. Design miss owned: the STRAND-010
pricing lesson was applied to the seed budget but not to the window, and
the smallest (slowest) box paid for it.

## Execution ledger (after the audit replay)

h = 0.55, T = 0.40, c0 = 0.35; S = 64/point; escape = mean(phi) > pi.

| N  | mean tau | censored | notes                                    |
|----|----------|----------|------------------------------------------|
| 24 | 1569.2   | 0        | window 24000 (audit re-lock); straggler escaped at 17015 |
| 48 | 457.7    | 0        | STRAND-010 archive, reused as locked      |
| 96 | 156.8    | 0        | window 12000                              |

Local-first-passage diagnostic (max_i phi_i > pi, new points only):
294.2 (N = 24) and 42.3 (N = 96), slope -1.40.

## The measured verdict: SUPER-EXTENSIVE — registered as measured, not promoted

Three-point fit: s = -1.661 at r^2 = 0.9984 (pairwise: -1.778 on 24 -> 48,
-1.545 on 48 -> 96). This is OUTSIDE every originally committed grammar
(intensive; extensive; intermediate) and inside the addendum's added
SUPER-EXTENSIVE class — which was written informed, so per the addendum's
own ceiling this classification is REGISTERED AS MEASURED and promotion is
reserved for a blind four-point session.

What the clean subset alone establishes (registrable at full strength): the
48 -> 96 leg is censor-free at full budget on both points, and its slope
(-1.545, standard error ~0.18) excludes the INTENSIVE grammar by many
sigma. WHATEVER the final classification, nu is NOT box-free.

## Consequence for STRAND-010, stated exactly

The promoted identification survives AS THE N = 48 STATEMENT and acquires a
scope note: nu(N) grows ~N^1.66 over this range, so O(1)-window membership
is N-dependent (nu ~ 0.14 at N = 24, 0.45 at N = 48, ~1.4 at N = 96 — the
window [1/3, 3] happens to contain the latter two). The "medium's own
clock" reading NARROWS: the band gap sets the SCALE of the per-event
kinetics (the Arrhenius clock at fixed N), while the N-dependence carries
the entropy of WHERE the event can happen — and it carries more than pure
rate-additivity (s = -1 would be per-site nucleation; -1.66 is steeper).

## Named suspects for the excess over -1 (pre-named in the addendum + one)

(i) finite-size barrier at the smallest box: ring-periodic kink-pair
    interaction raising the effective barrier at N = 24 (the 24 -> 48 leg
    IS the steeper one, consistent);
(ii) growth convolution in the mean-crossing observable — though the
    local-first-passage diagnostic is itself super-extensive (-1.40), so
    growth is NOT the whole excess;
(iii) multi-seed conversion: at larger N, multiple pairs nucleate and grow
    in parallel, accelerating the mean-crossing beyond first-event
    statistics.

## Next-order (pre-named, now specified)

The blind four-point sweep, N = 24..192, window priced PER-N, bars covering
the full slope line including the super-extensive class, with the
local-first-passage channel promoted from diagnostic to co-instrument and a
first-event-only observable added to separate (iii) from (i).

## Hygiene

- Zero imputation: the censored run was COMPLETED by deterministic replay
  under a uniform window extension (bit-identical trajectory through the
  original window), not filled in.
- The informed-addendum ceiling is respected: nothing from this session is
  promoted; the intensive-exclusion consequence rests only on censor-free,
  originally-locked data.
- Status: Modeled. Absolute scale untouched (FND-MATTER-003).
