# GR54-B -- 5/3 FLAT-CELL CONTROL AT 144x54: RESULTS (2026-09-02)

## VERDICT: ** CTRL-FAIL **

Per the locked charter, CTRL-FAIL fires if EITHER discriminator
fires on a cell registered FLAT at 36. Discriminator 1 fired:

  r(logV_pt, -logRate) = +0.9999   (line 0.8)   -> FIRES
  f_dir rise           = +0.0015   (line +0.15) -> does not fire

12/12 points gated at full bars, no refusals, protocol identical to
GR54 in every respect but the cell.

## CONSEQUENCE (pre-registered, honored)
GR-ARTIFACT is SUSPENDED pending an instrument/discriminator
commission. The charter states CTRL-FAIL is the decisive outcome
and that it "becomes the priority finding." It does. No claim is
drafted from GR54 until this is resolved.

## What the control actually shows (diagnosis, not excuse)
 i     A2          rate         V_pt      f_dir
 0  0.0048083  +4.6335e-04  3.5667e-03  0.09892
 5  0.0049923  +4.5685e-04  3.5811e-03  0.09972
11  0.0052098  +4.4949e-04  3.5986e-03  0.10070
(full table in analysis/gr54b_ckpt.pkl)

Across the whole march the rate falls 3.0 pct, V_pt rises 0.9 pct,
f_dir moves 0.0018 absolute. There is NO collapse here by any
physical reading -- the branch is flat, as registered at 36.

But r is a CORRELATION: it measures whether -log(rate) and
log(V_pt) move together, NOT how much they move. On this branch
both are smooth and monotone, so r pins at +0.9999 on a 3 pct rate
change. Discriminator 1 therefore has a false-positive mode on any
smooth monotone branch, independent of collapse magnitude. It is a
CO-MONOTONICITY detector, not a collapse detector.

## What this does and does not touch
- It does NOT show the 54 protocol flattens branches (the control
  reproduced FLAT-looking magnitudes correctly; f_dir, the
  magnitude-bearing line, behaved exactly as a flat cell should).
- It DOES show that r alone cannot separate flat from collapsing
  branches, which bears on EVERY verdict that used it, including
  the registered FND-153-era columns and FND-163 itself.
- GR54's own r came back NEGATIVE (-0.4812) -- on this diagnosis
  that means the 5/4 branch at 54 is not even co-monotone, a
  stronger statement than "not collapsing." GR54's f_dir line
  (-0.0007 vs +0.15) is the magnitude-bearing one and did not fire.
  The GR-ARTIFACT reading may well survive; it may not. That is for
  the commission, not for this document.

## Recommended next (author's call; nothing chartered)
D1. DISCRIMINATOR COMMISSION (priority): re-derive what the two
    FND-153-era lines actually measure; determine whether r should
    be replaced or paired with a magnitude criterion (e.g. total
    rate decline, or f_dir rise alone); re-score the registered
    columns' profiles and GR54 under the corrected rule. All data
    already exist -- no new solves.
D2. Only after D1: resume A (4/3 replication at 54).

States: analysis/gr54b_ckpt.pkl. Charter:
analysis/GR54B_charter_LOCKED.md.

## AMENDMENT (2026-09-03, post-review)
The CTRL-FAIL was produced by THIS charter's "EITHER line fires"
verdict form, which is stricter than the registered adjudication
rule (BOTH lines required for a collapse verdict). Under the
registered rule the control reads FLAT correctly. The r weakness is
real (co-monotonicity statistic, fires on flat branches) but was
never load-bearing: no registered verdict rests on r alone. The
suspension of GR-ARTIFACT was conservative rather than necessary;
DISC lifted it correctly. "The control found a fault in the
adjudication machinery" overstates the finding.
