# STAGE-3 RESOLUTION REPLICATION AT 144x54 (S3R) -- CHARTER
# (LOCKED 2026-08-29, before any solve or spectrum at 144x54)
# Authorized by the author ("Let's lay the next brick"), queue item 2
# of WHYWIND_queue_action_approved.md, executable in-container per
# SJ-CREDENTIALED (analysis/SPARSEJ_credential_results.md). PRIOR:
# ** P42-ARTIFACT ** (FND-161) -- the verdict forms below are
# written expecting the winding-band content to dissolve, and they
# name in advance what would count as it NOT dissolving.

## THE QUESTION
Does the 4/3 deep-end n = 17 winding content persist ANYWHERE in
the phi band as it opens to Nyquist 27, or does it dissolve --
and does the flat 5/3 cell stay unremarkable? FND-161 answered
phi 36 -> 42 for the 4/3 pair (ARTIFACT), but its headroom window
was [19, 21]: content at |n| >= 22 was invisible to BOTH its
lines. 144x54 closes that loophole. s stays at 144 THROUGHOUT --
the original stage-3's s-reduction confound (its S3-CRED refusal
at 96x36) is absent by construction, and the RETAINED 144x36
states are the baseline (no baseline re-solves).

## OBJECTS (locked)
- The deep arc pair per cell: prof-4/3 states[11], states[12] and
  prof-5/3 states[11], states[12] (2c ckpt, read-only).
- FOUR solves, all at 144x54: each member re-solved under ITS OWN
  A2 (a2 pin mode; pin measured from the retained state at load).
- Seeds: phi-only FFT zero-pad 36 -> 54 per field, s untouched,
  pt unwrapped with winding trend carried (the FND-160 seed rule);
  om1, om2 carried.
- Gates: stage-1 full bars unchanged (RMS < 1e-8, closure < 1e-6,
  pin < 1e-8, geometry floors). A member that cannot gate within
  the budget is a recorded refusal, evidence-bearing under this
  instrument's full-f64 exact solve (SJ charter scope clause).
- Solver: the SJ-CREDENTIALED instrument ONLY (SparseJac +
  BandedTorusSolver + gn_sparse), SJ_MEMO=jac, 60-round budget per
  member, reap-window chunked, per-round persistence, durable
  export to analysis/ at each gate/refusal.
- Order of execution: 5/3 prev, 5/3 deep (the control cell first,
  it is the credential), then 4/3 prev, 4/3 deep.

## LOCKED STATISTIC (the registered band machinery of
## whywind_stage3.py, unchanged)
For each gated pair: t = x_deep - x_prev; P = |FFT2(t_pt)|^2
normalized to pt total. BAND(17, 19) as registered (+-1 both
indices, both conjugates). Baseline reference: F17(144x36) =
0.9325 on the RETAINED 4/3 tangent (registered in FND-161; an
input here, not a measurement).
  F17_54   = BAND(17, 19) on the 4/3 144x54 tangent.
  HIBAND54 = pt mass at 19 <= |n_phi| <= 27 (the FULL headroom --
             the loophole-closing window).
  DOM54    = the dominant pt mode of the 4/3 144x54 tangent.
Display (non-verdict): top-mode tables both cells; 5/3 beat
spectrum; pt_share; per-member om2 placement vs Om1/2.

## CREDENTIAL (must pass before any 4/3 verdict renders)
  S3R-CRED: both 5/3 members gate at 144x54 AND the 5/3 tangent's
      top mode lies on its beat ladder (|n| = k, |m| = 2k, k in
      1..6). Failure: S3R-F-INSTRUMENT, kept; no adjudication.

## LOCKED VERDICT LINES (exactly five; no salvage, no post-hoc)
  S3R-ARTIFACT-CONFIRMED: F17_54 < 0.05 AND HIBAND54 < 0.10.
      The winding demand exists at NO resolvable band beyond the
      36-grid. The artifact call is FINAL for the FND-150..153
      interpretation re-pricing.
  S3R-RELOCATED: F17_54 < 0.05 AND HIBAND54 >= 0.10 with a
      coherent dominant mode at |n| >= 19. The demand is physical
      but was ALIASED at 36 -- the reading FND-161's window could
      not see. FND-161 receives a locating rider (its lines stand
      as honest for [19,21]); the mechanism question reopens at
      the named band.
  S3R-PHYSICAL: F17_54 >= 0.4663 (0.5 x the registered baseline)
      AND DOM54 in the (17,19) band AND HIBAND54 < 0.10.
      CONTRADICTS FND-161's grid-refinement reading; both records
      kept; a reconciliation commission is proposed to the author
      (the 42-grid would then be the anomaly to explain).
  S3R-DEEP-REFUSAL: the 4/3 deep member refuses to gate within
      budget under the exact-f64 instrument at 54 (having gated at
      42, FND-160). Evidence-bearing: grid-parity fragility
      returns as a 54-specific fact; registers on its own.
  Anything else: S3R-OPEN, kept.

## CONSEQUENCES (in advance)
  ARTIFACT-CONFIRMED: the re-pricing proposal RIPENS to a
      chartered commission over the FND-150..153 interpretation
      (rates and D bounds untouched); the q = 5/4 column proceeds
      as next queue item with artifact-final prior.
  RELOCATED or PHYSICAL: the q = 5/4 column proceeds with the
      rendered verdict as prior; riders/reconciliation as above.
  Either way the committed q = 5/4 FLAT dispersion prediction
      stands as committed and is untouched by this charter.

## NO-RESCUE RULE
No per-member or per-grid tuning of the instrument, seeds, pins,
budget, or lines after any 144x54 number is seen. The pattern for
(144x54, a2) is built fresh per the FAULT-9 rule and cached.
Failures kept. Grants reserved to the author. Ships in the NEXT
release.
