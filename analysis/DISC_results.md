# DISC -- DISCRIMINATOR COMMISSION: RESULTS (2026-09-02)

## VERDICT: ** DISC-CONFIRM ** (corrected rule C1; GR-ARTIFACT
## UNSUSPENDED)

## Step 1 -- fault scope audit (registered formulas, all five
## profiles now on disk)
  profile    reg   r         f_rise     rate_decline
  4/3 @36     C   +0.8698   +0.3691     +0.8569
  5/3 @36     F   +0.2272   +0.0018     +0.0505
  5/4 @36     C   +0.9413   +0.2342     +0.5690
  5/4 @54     -   -0.4812   -0.0007     +0.0443
  5/3 @54     -   +0.9999   +0.0015     +0.0299

The r fault is real but NARROW. On the four other profiles r
happens to align with the physics; only the 5/3 @54 control
exposes its blind spot (+0.9999 on a 3.0 pct rate decline). The
registered pair R required BOTH lines, so the faulty line never
carried a verdict alone: f_dir gated every registered call.

## Step 2 -- corrected rule (candidates locked before step 1)
All four rules (R, C1, C2, C3) reproduce the independent
registered verdicts (4/3 = C, 5/3 = F). Per the locked simplicity
preference: ** C1 adopted -- f_dir rise vs +0.15 ALONE **.
f_dir is magnitude-bearing and separates the corpus cleanly:
0.3691 / 0.2342 (collapse) vs 0.0018 / 0.0015 / -0.0007 (flat) --
two orders of magnitude, no overlap, no threshold sensitivity.

## Step 3 -- re-score under C1
  FND-163 (5/4 @36): f_rise +0.2342 -> COLLAPSE. UNCHANGED.
  GR54    (5/4 @54): f_rise -0.0007 -> no collapse. UNCHANGED.
  GR54-B  (5/3 @54): f_rise +0.0015 -> FLAT, as registered at 36.
    The control now READS CORRECTLY; its CTRL-FAIL was caused by
    the faulty line, not by the instrument or the protocol.

## Consequences
1. GR-ARTIFACT is UNSUSPENDED. Both it and FND-163 stand under the
   corrected rule; the GR54 conclusion never depended on r.
2. The 54 protocol is vindicated as an instrument: it reproduces
   FLAT on a registered-flat cell (the control's original purpose,
   now achieved).
3. RIDER (draft) for the FND-153-era claims that used the pair:
   "The r = corr(logV_pt, -logRate) line is a co-monotonicity
   statistic and can fire on flat branches (demonstrated: 5/3 @54,
   r = +0.9999 at a 3.0 pct rate decline). Every registered
   verdict using the pair required f_dir to fire as well, so no
   registered verdict rests on r; the corrected rule (DISC
   commission, 2026-09-02) is f_dir rise vs +0.15 alone."
4. A (4/3 replication at 54) is CLEARED to run.

## Process note
The r fault was found by a control chartered for a different
purpose, and the pre-registered CTRL-FAIL consequence (suspend
GR-ARTIFACT) was honored before the diagnosis was known. The
suspension is lifted by the chartered commission, not by argument.

## AMENDMENT (2026-09-03, post-review)
The locked selection rule (reproduce the independent 4/3 and 5/3
@36 verdicts) was NON-DISCRIMINATING: all four candidates
including the original pair R pass it. C1 was therefore selected
by the pre-stated simplicity ordering, not by the data. The case
for dropping r is "simpler and no worse on every profile on disk,"
not "the data demanded it." This is legitimate under the locked
charter and is recorded so it cannot be overclaimed.
