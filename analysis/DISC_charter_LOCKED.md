# DISC -- DISCRIMINATOR COMMISSION (CHARTER, LOCKED 2026-09-02;
# triggered by GR54-B CTRL-FAIL, which the charter named the
# priority finding)

## Question
The FND-153-era discriminator pair -- r = corr(logV_pt, -logRate)
vs 0.8, and f_dir rise vs +0.15 -- adjudicated every q-sweep
column. GR54-B showed r fires at +0.9999 on a branch that is flat
by every physical measure (rate -3.0 pct, V_pt +0.9 pct, f_dir
+0.0018): r is a co-monotonicity detector, blind to magnitude.
What do the two lines actually measure, which registered verdicts
depend on the faulty one, and what is the corrected rule?

## Inputs (all existing; NO new solves)
The five profiles now on disk, each 12 gated points with per-point
rate/V_pt/f_dir: 4/3 @36, 5/3 @36 (analysis/qsweep_stage2c_ckpt),
5/4 @36 (q54_profile_ckpt), 5/4 @54 (gr54_ckpt), 5/3 @54
(gr54b_ckpt). The registered verdicts: 4/3 C, 5/3 F, 5/4 C(@36).

## Step 1 -- FAULT SCOPE (compute first, before any new rule)
Recompute r and f_rise for all five profiles under the registered
formulas and tabulate against the registered verdicts. Determines
which registered verdicts r alone would have carried, and whether
f_dir alone reproduces them. Pure audit; no discretion.

## Step 2 -- CORRECTED RULE (locked candidates, fixed here, BEFORE
## step 1's numbers are seen)
Exactly three candidate rules are eligible; no others may be
introduced after the audit:
  C1  f_dir rise vs +0.15 ALONE (drop r).
  C2  f_dir rise vs +0.15 AND total rate decline
      (rate[0]-rate[-1])/rate[0] >= 0.25 (magnitude pair).
  C3  r vs 0.8 AND the C2 magnitude criterion (keep r, add
      magnitude).
SELECTION RULE (locked): the corrected rule is the candidate that
reproduces the registered 36-grid verdicts for 4/3 (C) and 5/3 (F)
-- the two columns whose verdicts predate and are independent of
this dispute. If more than one candidate does, prefer the simplest
(C1 > C2 > C3). If none does, verdict DISC-OPEN and no rule is
adopted.

## Step 3 -- RE-SCORE (only after step 2 selects)
Apply the corrected rule to 5/4@36 (FND-163) and 5/4@54 (GR54).
Verdict forms (LOCKED):
  DISC-CONFIRM: corrected rule leaves BOTH FND-163 (collapse @36)
    and GR-ARTIFACT (no collapse @54) standing -> GR-ARTIFACT
    unsuspended; GR54 claim drafting proceeds; A (4/3 @54) opens.
  DISC-REVISE: corrected rule changes either -> the affected
    verdict gets a rider or a re-adjudication commission; FND-163's
    registered text is NOT edited without the author's grant.
  DISC-OPEN: no candidate reproduces the independent verdicts ->
    the discriminator question is escalated, GR-ARTIFACT stays
    suspended, and A does not run.
In ALL forms: a rider naming the r fault is drafted for the
FND-153-era claims that used it.

## Deliverables
One script, all numbers logged; analysis/DISC_results.md; rider and
claim drafts for the author's grant.
